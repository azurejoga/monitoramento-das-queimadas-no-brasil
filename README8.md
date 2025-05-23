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
| 5d01105e-414e-382e-9ea5-36491f9c9837 | -12.32879 | -49.99593 | 2025-05-23 04:04:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 52558d13-347c-3ea1-90c7-c4298b7c2528 | -9.02068 | -47.7475 | 2025-05-23 04:04:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 02bf1670-ef78-3fac-83e9-697a69b8911c | -11.93617 | -43.9325 | 2025-05-23 04:04:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1564d7dc-0231-3349-a4e2-d5c20f21961a | -12.33447 | -49.99381 | 2025-05-23 04:04:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7b54ea22-d651-3996-996f-42f881800c4e | -12.07775 | -47.3444 | 2025-05-23 04:04:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| acc39fc2-d0f5-3e5b-8758-9734a84edf96 | -11.55826 | -47.45583 | 2025-05-23 04:04:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0a320921-e9b0-3ce7-b79f-c4609143827f | -12.07702 | -47.34855 | 2025-05-23 04:04:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 450be3be-4fd6-3441-ad88-6cc262eb276e | -12.85145 | -47.38844 | 2025-05-23 04:04:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6e8d06b6-72d0-3e95-83f6-2127c6431333 | -14.04232 | -53.37578 | 2025-05-23 04:04:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bc7daa7c-6466-3e9f-8fb7-abf5ee2e7b5e | -12.0662 | -47.34543 | 2025-05-23 04:04:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 87c11d56-3609-34a1-8441-a0a39c541d91 | -15.42881 | -41.40673 | 2025-05-23 04:04:00 | NPP-375D | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 46f0c538-e68c-371c-93f7-050c4e3678c0 | -13.9814 | -56.02554 | 2025-05-23 04:04:00 | NPP-375D | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 17.8 |
| a5e9c96e-a699-3cf9-99d2-9e2035539b4f | -12.39113 | -49.9844 | 2025-05-23 04:04:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5ea49fe8-62b2-3102-8913-4c14c737c472 | -9.04479 | -47.7468 | 2025-05-23 04:04:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2cc0545e-865f-3a89-9fcd-e510b06a6152 | -12.26703 | -47.00441 | 2025-05-23 04:04:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 666af8f0-cab7-3677-83b9-a8760b3d9438 | -12.71783 | -54.97474 | 2025-05-23 04:04:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 41562f17-faac-3eb5-b500-e11510c31cf1 | -13.10073 | -52.29088 | 2025-05-23 04:04:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f3df58a4-b960-3c24-9dec-64df8da54642 | -12.06696 | -47.34132 | 2025-05-23 04:04:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 05214489-bd47-3131-8fa6-cc9b3a1606c3 | -13.97873 | -56.01714 | 2025-05-23 04:04:00 | NPP-375D | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 11.4 |
| a5c51e61-7803-3846-8dac-ca66cc6e46bd | -13.09491 | -52.2897 | 2025-05-23 04:04:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2def54a8-7b30-3389-aa42-6688ad26a734 | -14.01917 | -55.13406 | 2025-05-23 04:04:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5a3e6c1d-0e94-3537-a3e3-ceea59aecc2d | -12.85071 | -47.39246 | 2025-05-23 04:04:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3606f4bd-a429-36f6-a98a-57af1c574fc4 | -12.29779 | -52.49536 | 2025-05-23 04:04:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 5e188880-0ad7-3447-a3ad-fbf0e548a7da | -13.98411 | -56.02633 | 2025-05-23 04:04:00 | NPP-375D | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 16.4 |
| b0135049-44f3-3055-99c5-3b5fb627b520 | -14.0405 | -53.37912 | 2025-05-23 04:04:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0f06908f-36f3-3e4a-a1a9-86accd5d8a2e | -11.26656 | -52.4742 | 2025-05-23 04:04:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fbe846b6-a88b-3cbc-b771-16f295bae02e | -14.03948 | -53.38393 | 2025-05-23 04:04:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 13f11a65-fd27-3f5f-a335-69aa015040e3 | -12.06485 | -47.34207 | 2025-05-23 04:04:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 9c059cf9-15a1-3085-ae4c-c2c81cb8fff1 | -12.39795 | -49.97629 | 2025-05-23 04:04:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e8208d69-41e0-3ab3-9c22-adf58b4476c2 | -12.0791 | -47.34775 | 2025-05-23 04:04:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 35ec486a-70be-3487-9d0b-469a6b9ae67a | -12.33789 | -49.98661 | 2025-05-23 04:04:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 36bbca79-b1a4-3291-9b78-7c94bb08589c | -12.07272 | -47.34776 | 2025-05-23 04:04:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d0e0cdfb-fa4f-3330-85f6-707642365616 | -12.85496 | -47.39329 | 2025-05-23 04:04:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8a43ded7-6d5c-3d18-a020-80ee18f5491c | -14.04151 | -53.37433 | 2025-05-23 04:04:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9b102fb6-0d12-35c5-9ae1-d1beec8dd71a | -10.71349 | -48.82431 | 2025-05-23 04:04:00 | NPP-375D | OLIVEIRA DE FÁTIMA | TOCANTINS | Brasil | 1715507 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 7f1c4c55-abd9-3392-8563-87238fab4277 | -11.78428 | -44.27893 | 2025-05-23 04:04:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 07f34af6-99f3-33f5-a8fa-f66175383210 | -13.78638 | -54.31897 | 2025-05-23 04:04:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 37673e87-27c9-3ca4-abf8-81f0b27bc50c | -10.49227 | -42.41879 | 2025-05-23 04:04:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 8ff17264-6485-3ac5-8191-2928a5a8935a | -12.31859 | -49.99393 | 2025-05-23 04:04:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 109f7d6e-323f-326a-bbc6-86f587141e3c | -14.68109 | -45.1091 | 2025-05-23 04:04:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 37055fd6-01c8-317b-a35f-59aad3b36a17 | -14.01785 | -55.14013 | 2025-05-23 04:04:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 665f19b6-77b9-3be7-9eb0-13a715d11889 | -12.28497 | -52.49732 | 2025-05-23 04:04:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 581686e4-6c69-3d7f-bf68-db4f1a299d88 | -11.79367 | -44.28917 | 2025-05-23 04:04:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 5e321f4b-bed7-349d-89e2-db750d7f5295 | -14.03721 | -53.36962 | 2025-05-23 04:04:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6f394b36-8472-32a8-a4fe-f3ce29e4e2e3 | -13.05838 | -44.04688 | 2025-05-23 04:04:00 | NPP-375D | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4873b6b6-c214-3ef8-881c-fee37d29a222 | -12.13617 | -54.65909 | 2025-05-23 04:04:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fbea3562-f67d-3664-a430-289932c7bc13 | -12.2966 | -52.50868 | 2025-05-23 04:04:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4562509d-736e-3a66-93d5-3593d0e630e1 | -11.29653 | -53.99126 | 2025-05-23 04:04:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| df053b6b-124e-3a90-83c2-4770f8fb993c | -9.04394 | -47.75162 | 2025-05-23 04:04:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3bc7627c-d70c-3ec6-8a3a-50b18a7e4975 | -12.06987 | -47.33874 | 2025-05-23 04:04:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e44128e8-07ba-303c-93b4-ea82a7489059 | -10.65787 | -49.47925 | 2025-05-23 04:04:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8912ec29-52a5-3b2e-8806-839c25915427 | -13.78876 | -54.30776 | 2025-05-23 04:04:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e2685d22-141f-3fa4-8450-abacd2c78204 | -9.04308 | -47.75648 | 2025-05-23 04:04:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7eeeb8fc-9c74-3dcd-bd2b-ff10118b0f3e | -11.51471 | -48.55669 | 2025-05-23 04:04:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 47ddb8db-8ddb-3ad7-ba68-37a5f1946a66 | -12.32937 | -49.99286 | 2025-05-23 04:04:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6df8a66f-fcbf-3b70-af8b-6f5700cd0f14 | -15.74356 | -43.48647 | 2025-05-23 04:04:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5a1f2691-9895-3e4f-a0c6-9f1f3f792001 | -12.33219 | -49.98875 | 2025-05-23 04:04:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1dc2f2cc-1b6d-34ec-80ab-0a90a142b320 | -11.93971 | -43.9331 | 2025-05-23 04:04:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 77d15028-2dca-3031-8b02-4e19d2e18b25 | -12.0705 | -47.34618 | 2025-05-23 04:04:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 6b1a43cb-9ed9-3373-a252-c09ec4d9b2b6 | -13.78759 | -54.31325 | 2025-05-23 04:04:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 48904a2b-d241-3618-ba52-171966ecdc6b | -11.57261 | -47.89845 | 2025-05-23 04:04:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 26445097-5199-36a2-868d-120fc20a75bd | -14.04558 | -53.38526 | 2025-05-23 04:04:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c4a239ae-573c-3abd-a502-908dc40a8b71 | -9.02533 | -47.74832 | 2025-05-23 04:04:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 838d5463-65a5-33e0-a729-86710bcad163 | -11.27261 | -52.47556 | 2025-05-23 04:04:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c073ca5e-e683-3ea7-a970-a3f5e1224719 | -15.43215 | -41.40728 | 2025-05-23 04:04:00 | NPP-375D | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 58623bd2-cedc-37da-a3c7-111bba72c2c2 | -11.56774 | -47.45329 | 2025-05-23 04:04:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7d8345b6-c8a4-3bec-bf05-4abea9894915 | -12.39622 | -49.98536 | 2025-05-23 04:04:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e29f7911-2014-3249-9f99-046a688f9f53 | -14.03135 | -55.14317 | 2025-05-23 04:04:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 55ff73e6-df4a-3a08-996b-b48e08c89309 | -10.49286 | -42.41512 | 2025-05-23 04:04:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| cef351d2-b582-33cf-b0c8-7434f9632d8a | -12.39171 | -49.98135 | 2025-05-23 04:04:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 33d8be5c-ba5b-3abf-a7c7-820c0cfcf013 | -15.421 | -41.41288 | 2025-05-23 04:04:00 | NPP-375D | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| d7c29f07-d3ad-306e-9750-e334d93f2df7 | -13.32007 | -43.00917 | 2025-05-23 04:04:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| f8cb945e-53c7-3345-9b3f-7f84efa31405 | -11.56993 | -54.56934 | 2025-05-23 04:04:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 42fd1037-013c-312e-bc3e-b8da9b8651a4 | -12.33906 | -49.98059 | 2025-05-23 04:04:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0f6c59fe-36dc-31c9-a418-e34f620dbd98 | -12.32994 | -49.98978 | 2025-05-23 04:04:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b1926a61-41af-34d6-87c0-c546066cd00f | -12.40072 | -49.98947 | 2025-05-23 04:04:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 35d6e1eb-7cd2-3b3a-b49c-c64bde6a9161 | -12.28649 | -52.49715 | 2025-05-23 04:04:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 1e77883b-87fd-39fc-ad6e-bb2452ff60da | -11.79077 | -44.28436 | 2025-05-23 04:04:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 1015a0fd-184b-3f21-84e4-af65f5d01ce8 | -12.29337 | -52.49392 | 2025-05-23 04:04:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 68385fbc-3a1e-30fb-8370-5ca5c9ce2dee | -12.33848 | -49.9836 | 2025-05-23 04:04:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a006ce4c-d756-3aa2-872c-b831b1b9232c | -12.4013 | -49.98639 | 2025-05-23 04:04:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 688acc6b-5a99-3ce0-9800-54e7a6ef2cf4 | -10.71596 | -48.82307 | 2025-05-23 04:04:00 | NPP-375D | OLIVEIRA DE FÁTIMA | TOCANTINS | Brasil | 1715507 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2019597a-7a3d-3943-9bf4-6ddc883b1ace | -15.84882 | -46.48904 | 2025-05-23 04:04:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 83ab176d-dccd-332c-8509-c2889b4b2d4e | -11.97185 | -44.15678 | 2025-05-23 04:04:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d864d9b2-f605-3a9d-96be-95585a3778f0 | -12.0748 | -47.34697 | 2025-05-23 04:04:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6d4bfedd-f1f1-32dd-93be-1d53a32c0ae7 | -14.05451 | -53.37851 | 2025-05-23 04:04:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8241b830-f734-343c-bb3d-859b9d8df24d | -8.72427 | -50.25647 | 2025-05-23 04:04:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1e94f02c-6dad-3155-9b4b-133b2663d5d3 | -10.64659 | -49.48339 | 2025-05-23 04:04:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5f05bedb-f80b-3aeb-8f8f-aa212bb1bdb2 | -14.04862 | -53.37091 | 2025-05-23 04:04:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| aeae2013-7bc2-3c22-a041-a013ab00d5b9 | -8.69619 | -47.71581 | 2025-05-23 04:04:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7713519e-8bdd-32bd-8259-8b5b71982e18 | -14.0527 | -53.38181 | 2025-05-23 04:04:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0d01904b-a476-3aea-9302-34e5fbb055e4 | -10.48947 | -42.41455 | 2025-05-23 04:04:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| c4170033-45a4-3a4f-98da-47edde3f936a | -14.02461 | -55.14158 | 2025-05-23 04:04:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f5fe4d95-9016-3f74-82cb-cd66fd886a09 | -12.33337 | -49.98268 | 2025-05-23 04:04:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0d6c2ab4-0948-3b29-b870-a87e822accfb | -14.05371 | -53.37702 | 2025-05-23 04:04:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0c92f4a4-7a71-336f-bb80-b7df4812caec | -12.42271 | -49.98475 | 2025-05-23 04:04:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7cf3cd04-0a68-3a55-97c2-7e23285dbbc5 | -10.48888 | -42.41822 | 2025-05-23 04:04:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 010c500f-da6a-3c1a-a747-667a91486005 | -12.29867 | -52.49088 | 2025-05-23 04:04:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 6ebb8550-d134-3844-86ee-4b4424c4b71a | -12.29843 | -52.49968 | 2025-05-23 04:04:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 26a17756-13c6-3e37-a0d8-4a25b6d92001 | -13.9857 | -56.01929 | 2025-05-23 04:04:00 | NPP-375D | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 16.4 |


[Clique aqui para ver as próximas entradas](README9.md)
