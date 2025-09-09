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

## Dados Diários - Página 75

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2bd22589-fd86-36da-9b72-800816d1ee16 | -11.9923 | -51.034 | 2025-09-09 12:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 92871ce0-5524-3b6c-8c86-af61a68554c9 | -7.8622 | -46.2616 | 2025-09-09 12:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 98.2 |
| 61e9b57f-246c-3053-b1a5-fbaffafc082c | -12.2938 | -50.0121 | 2025-09-09 12:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 99.8 |
| 4d5ad018-d4bc-3437-a44c-da679ad01aea | -15.2686 | -53.7801 | 2025-09-09 12:20:00 | GOES-19 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 99.6 |
| 9ecdbeb3-5dca-3e39-86fc-6a3b53605bd0 | -17.2762 | -46.7305 | 2025-09-09 12:20:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 89.4 |
| e19596ed-7a03-32ba-a49c-11ab4495a6a1 | -13.9564 | -48.2493 | 2025-09-09 12:20:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 119.5 |
| c926fd3a-9bb1-33ba-be54-426db8da9cfa | -11.9735 | -51.0148 | 2025-09-09 12:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 90.7 |
| 2b913630-fcac-312f-b8b5-74c9770f4dd1 | -5.5504 | -45.1891 | 2025-09-09 12:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 9014c646-2a20-3741-89f7-59264a605ce9 | -5.589 | -42.9048 | 2025-09-09 12:20:00 | GOES-19 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 89.5 |
| 1d2aaf6a-2079-3d96-beae-dd4bc2b8edc8 | -15.2683 | -53.8012 | 2025-09-09 12:20:00 | GOES-19 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 87.9 |
| e4cc9a78-ce84-3509-bf6e-f2b1ad513578 | -7.789 | -46.0891 | 2025-09-09 12:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 79.3 |
| 26262f0d-2568-3e8e-b899-f68d99270370 | -13.9568 | -48.2269 | 2025-09-09 12:20:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 978b91e7-9e52-3667-b19b-6dba694b8a9d | -9.7014 | -46.8547 | 2025-09-09 12:20:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 5520d3e9-1e42-3e83-bd76-8766e43a4f1a | -11.3389 | -46.5419 | 2025-09-09 12:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 3c70660b-fa03-324a-b143-6d97f8ba88d4 | -6.199 | -45.8186 | 2025-09-09 12:20:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 334f2278-e110-3bb0-8ec0-223f69824ca1 | -12.0295 | -51.0935 | 2025-09-09 12:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 58749135-d1a1-3b88-ae90-6346192ee0c5 | -9.7203 | -46.8526 | 2025-09-09 12:20:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 139.6 |
| a1544930-2adf-3693-8deb-3969d2fcbae6 | -6.2224 | -43.3693 | 2025-09-09 12:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 96.0 |
| 9c20cdcc-8bf1-3f94-928e-6331f52dfda6 | -6.2226 | -43.3459 | 2025-09-09 12:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 7cace64f-ad09-3c8f-975a-e5659aff013e | -5.898 | -43.9523 | 2025-09-09 12:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 917504a0-2c3c-323b-a544-38a018a77628 | -13.0165 | -48.0326 | 2025-09-09 12:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 101.6 |
| 43de1e43-e9b3-3902-9335-57244d3bc02b | -11.9739 | -50.9935 | 2025-09-09 12:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 230.7 |
| 972e53b9-4a54-37fd-aa8a-7961e760c356 | -12.2941 | -49.9904 | 2025-09-09 12:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 107.0 |
| 9bc8daf1-cdff-3bd7-9163-4280f22158fd | -12.1988 | -53.9024 | 2025-09-09 12:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 37eb5102-9e7e-3e2d-a949-58533f7b6754 | -13.0357 | -48.0298 | 2025-09-09 12:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 107.4 |
| 4fe563f4-edb2-3927-90b3-c99f95157807 | -12.0291 | -51.1149 | 2025-09-09 12:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 9ec38c21-e9f2-3cb6-a962-ab05c2f33e18 | -15.8205 | -52.2444 | 2025-09-09 12:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 120.7 |
| e3e28387-7f2b-3262-b18c-22ae7948bd70 | -11.0231 | -46.0412 | 2025-09-09 12:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 79.3 |
| 531ae941-e992-3eaa-89a5-9bd0fb5ed08f | -5.5504 | -45.1891 | 2025-09-09 12:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 68.1 |
| eb0a0427-c6f0-3779-bfe3-00ded9a9ef18 | -17.2762 | -46.7305 | 2025-09-09 12:30:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 86.1 |
| 0e28d781-7723-31b5-905a-5c9e45b1f20f | -13.9564 | -48.2493 | 2025-09-09 12:30:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 117.9 |
| a391f058-e269-3303-9671-4d6558ebd058 | -15.2492 | -53.7826 | 2025-09-09 12:30:00 | GOES-19 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 105.6 |
| 44eb1da5-6b59-3936-886a-2b4f0dae4cc1 | -9.7203 | -46.8526 | 2025-09-09 12:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 135.9 |
| 311e882d-c704-3536-94c2-60a04a8bc9db | -5.8395 | -44.2103 | 2025-09-09 12:30:00 | GOES-19 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 5c69b128-c9aa-34a0-b77d-61df91219ee4 | -12.2941 | -49.9904 | 2025-09-09 12:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 2f59a249-e973-3859-ac49-f63f8c914141 | -13.937 | -48.2522 | 2025-09-09 12:30:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 122.0 |
| a28716a2-a424-34e7-95cf-7ee2180870b7 | -11.9923 | -51.034 | 2025-09-09 12:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 137.4 |
| 40883ec1-4f4d-3e89-a869-bebd048e6463 | -17.2563 | -46.7346 | 2025-09-09 12:30:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 86e34bd1-1827-3f77-85b9-0b7118c87413 | -5.5702 | -42.9062 | 2025-09-09 12:30:00 | GOES-19 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 87.3 |
| 013d2e42-1ce2-36e6-92c7-d236a94f8637 | -5.589 | -42.9048 | 2025-09-09 12:30:00 | GOES-19 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 95.9 |
| 6b8f9fbc-2473-3b68-a1fd-d2f226a3d247 | -11.9926 | -51.0126 | 2025-09-09 12:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 215.7 |
| 250ad20b-0393-3265-ad5f-0fb4c1e7516d | -6.2407 | -43.4144 | 2025-09-09 12:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 510a833a-6e99-3aaa-a0e8-b8ccbb993f7f | -20.0357 | -47.7815 | 2025-09-09 12:30:00 | GOES-19 | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 112.7 |
| ab22d453-2c05-3ae4-a360-14ed746b300e | -11.3389 | -46.5419 | 2025-09-09 12:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 147.0 |
| 84d7ac0a-ee96-32e2-ac3a-e41c26a9bb6a | -5.9191 | -45.7717 | 2025-09-09 12:30:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 9b0634db-9bf5-383e-b0ad-36fa935fc95f | -12.0291 | -51.1149 | 2025-09-09 12:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 76744c4e-d227-3135-9d51-c8f50219f7c2 | -11.3018 | -46.4792 | 2025-09-09 12:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 170b3fe6-a1a8-3f88-90eb-245a0b23793e | -17.2757 | -46.7538 | 2025-09-09 12:30:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 20e3233e-7b48-38d3-be82-1bfd13b817ad | -13.9375 | -48.2299 | 2025-09-09 12:30:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 90.5 |
| 036cc9a3-cc39-35bb-ab01-16a257d51b15 | -7.789 | -46.0891 | 2025-09-09 12:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 128.4 |
| 5f81b6a6-d116-39fd-b6f9-ce6b386a6b36 | -6.199 | -45.8186 | 2025-09-09 12:30:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 15ca8766-e578-36aa-bd6d-fe35d4553650 | -6.2224 | -43.3693 | 2025-09-09 12:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 94.9 |
| 4025be31-bcaa-3c0f-89ed-e9ab36e32b81 | -12.1991 | -53.8817 | 2025-09-09 12:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 73.5 |
| a8c79295-b2cd-3751-a1af-1b8afba3096c | -12.2938 | -50.0121 | 2025-09-09 12:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 00181621-1baa-3f53-a86e-e8cc4860a291 | -13.0165 | -48.0326 | 2025-09-09 12:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 2cb51e32-2eaf-3e60-a104-aebc9a4d614a | -13.0357 | -48.0298 | 2025-09-09 12:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 154.5 |
| 1ae940bf-4778-38a1-b4fe-9b2e33c652ac | -12.0295 | -51.0935 | 2025-09-09 12:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 84.7 |
| f7edf25a-7f14-3194-ae9d-06debcf4971d | -15.8205 | -52.2444 | 2025-09-09 12:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 139.6 |
| 01f0e179-ecbe-367b-88cf-47f046a14832 | -15.2489 | -53.8036 | 2025-09-09 12:30:00 | GOES-19 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 77.3 |
| f5ebba57-431f-3759-8cea-44b39d615ca1 | -11.3385 | -46.5645 | 2025-09-09 12:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 71.6 |
| ad019938-0087-3420-b5ae-312417577f85 | -13.9568 | -48.2269 | 2025-09-09 12:30:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 3fd3857d-f788-3bf3-8543-3bce2cfa4038 | -6.6364 | -45.107 | 2025-09-09 12:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 91.6 |
| 35ba393c-fb2b-34e8-8f1a-6423e444b9e5 | -6.3572 | -43.0303 | 2025-09-09 12:30:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 2691a7b1-7bde-34f4-87f4-203f0af5e3ba | -15.2683 | -53.8012 | 2025-09-09 12:30:00 | GOES-19 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 106.6 |
| 065eb38b-fa0e-374a-9d88-c36169b7f133 | -15.2686 | -53.7801 | 2025-09-09 12:30:00 | GOES-19 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 149.9 |
| c1b3cb49-fc2a-33f3-9ee2-61c0857e9e13 | -14.4471 | -53.2124 | 2025-09-09 12:30:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 154.5 |
| 0537ecda-c23b-3f89-9208-5963b3eaf08b | -11.0436 | -45.9476 | 2025-09-09 12:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 429.9 |
| 308498cb-435a-3c6d-968e-145ac6469cf2 | -17.2757 | -46.7538 | 2025-09-09 12:40:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 76.9 |
| f61fddcc-9618-3cb4-9348-0ff54f360509 | -17.2967 | -46.7032 | 2025-09-09 12:40:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 88.8 |
| ac3b2349-a787-3a03-acf9-513969725083 | -19.863 | -48.1673 | 2025-09-09 12:40:00 | GOES-19 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 151.2 |
| 560fcc9b-d2b5-3e69-a231-2b81475a50d8 | -6.6364 | -45.107 | 2025-09-09 12:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 204d9188-a369-32f7-9bf5-73187dd4d071 | -13.0357 | -48.0298 | 2025-09-09 12:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 172.1 |
| 5462d549-9e35-3b78-b721-f27e3ff98c45 | -17.2563 | -46.7346 | 2025-09-09 12:40:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 69066df8-6b3b-3020-8b98-dfb1bb70a53e | -5.8406 | -44.0951 | 2025-09-09 12:40:00 | GOES-19 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 86.8 |
| f1165d6b-123a-3dd5-a5b8-97887e8f7f30 | -5.589 | -42.9048 | 2025-09-09 12:40:00 | GOES-19 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 143.4 |
| 3650abe6-8210-3d51-932d-fd25f1c1dd94 | -7.7107 | -44.7369 | 2025-09-09 12:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 120.8 |
| 4716e776-141f-3155-898c-f96b144cf3ce | -13.937 | -48.2522 | 2025-09-09 12:40:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 6df3bcf8-c619-31d5-b227-fa9cf2a74c5c | -11.4277 | -43.6017 | 2025-09-09 12:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 83.5 |
| e38301f5-58e5-39dc-9451-190a5d0d4d68 | -15.2489 | -53.8036 | 2025-09-09 12:40:00 | GOES-19 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 7060a8b5-cb7a-3f96-ad89-65e7006963c1 | -14.4471 | -53.2124 | 2025-09-09 12:40:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 137.7 |
| 89afad6e-c985-3d6d-8a3d-ba4756043795 | -15.2683 | -53.8012 | 2025-09-09 12:40:00 | GOES-19 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 98.6 |
| 9d8e9c10-1f5e-3c79-bb1b-70630116f064 | -11.9923 | -51.034 | 2025-09-09 12:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 165.7 |
| 04d88ac7-28e2-33dd-bf2e-91a5c0138830 | -5.5504 | -45.1891 | 2025-09-09 12:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 82.6 |
| fd631330-e6e1-3b73-8b32-842ed05b219b | -9.7206 | -46.8302 | 2025-09-09 12:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 74.7 |
| e669f138-d5d5-349a-a55b-2e61c2f750c1 | -11.0245 | -45.9502 | 2025-09-09 12:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 180.6 |
| 4d9c2f6e-0860-338b-9a13-51230ff14925 | -12.0291 | -51.1149 | 2025-09-09 12:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 64a55575-b573-3b55-889e-5e26b0fba44d | -6.199 | -45.8186 | 2025-09-09 12:40:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 112.0 |
| d40e600d-1089-3a17-aad6-51a87def2f80 | -11.9739 | -50.9935 | 2025-09-09 12:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 94.7 |
| 6f874d18-4bb6-36db-b052-f79f2ed80b04 | -11.3385 | -46.5645 | 2025-09-09 12:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 536082ba-3028-36e9-904f-05b89bcb49e4 | -5.8395 | -44.2103 | 2025-09-09 12:40:00 | GOES-19 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 205.6 |
| fe1e84dd-761b-3dcf-9a7e-55dc2014e06e | -9.7203 | -46.8526 | 2025-09-09 12:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 134.7 |
| 5fcb2a4a-509e-3a08-93bf-b163ebfdabac | -6.2407 | -43.4144 | 2025-09-09 12:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 7d9d8f35-e16f-3990-b371-b7cf074b84fe | -13.9564 | -48.2493 | 2025-09-09 12:40:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 89b4dea9-7561-3039-8b18-736a78faabbd | -7.881 | -46.2598 | 2025-09-09 12:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 77.6 |
| ded8410d-9289-37af-bc7f-73f0e260bf86 | -12.0295 | -51.0935 | 2025-09-09 12:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 84.1 |
| c8df4148-9fd6-3927-85d0-1f5fb49fffaa | -17.2973 | -46.6799 | 2025-09-09 12:40:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 4e561c85-be03-3b5b-a04b-c9cc4733ec16 | -7.7104 | -44.7598 | 2025-09-09 12:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 80.8 |
| dc5452e5-7cd9-3839-b4c0-6289c64d0488 | -19.8223 | -48.1763 | 2025-09-09 12:40:00 | GOES-19 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 93.8 |
| 4b6a1385-8650-36fc-9bb9-599cee15b121 | -12.2938 | -50.0121 | 2025-09-09 12:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 90.1 |
| 721ab0d1-f5ac-3c61-9d02-dc7c7db2f003 | -17.7328 | -44.4637 | 2025-09-09 12:40:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 111.1 |


[Clique aqui para ver as próximas entradas](README76.md)
