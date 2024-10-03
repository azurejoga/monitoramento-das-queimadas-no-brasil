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
| a620f277-130a-3a41-9d5b-1e8fae5f69a3 | -6.6793 | -44.5158 | 2024-10-03 00:11:30 | METOP-B | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d6d2fd20-6439-38b6-aeb5-fcff13432bda | -6.6809 | -44.523399 | 2024-10-03 00:11:30 | METOP-B | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8020709e-bf91-3793-b8b0-c4e43a7b04b5 | -6.2946 | -43.015598 | 2024-10-03 00:11:31 | METOP-B | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7ddccca0-d075-3136-a318-f510de32fe56 | -6.2962 | -43.022499 | 2024-10-03 00:11:31 | METOP-B | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b355eb2d-ea14-3296-84bb-7e63d49fc4f0 | -6.2977 | -43.0294 | 2024-10-03 00:11:31 | METOP-B | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e2315d99-7949-37d5-98e9-55698a97426d | -6.2993 | -43.036301 | 2024-10-03 00:11:31 | METOP-B | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ab0a2ae2-08cb-3b8b-9a2d-dc3d591fee78 | -6.2864 | -43.0247 | 2024-10-03 00:11:31 | METOP-B | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5dc01a59-17c1-39f7-acc8-2f2d49e4c007 | -6.6695 | -44.518002 | 2024-10-03 00:11:31 | METOP-B | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a0247dd8-ee14-399f-92db-71c234c5cd9a | -6.6711 | -44.525501 | 2024-10-03 00:11:31 | METOP-B | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8df4827a-1ca3-34bf-813e-c71a97aa05e7 | -6.6766 | -44.6436 | 2024-10-03 00:11:31 | METOP-B | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1b84f0da-ca8a-34f9-8db7-854653559b44 | -6.6782 | -44.651199 | 2024-10-03 00:11:31 | METOP-B | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8b69e392-3dbc-3c19-be77-c24b631238e3 | -6.5726 | -44.219002 | 2024-10-03 00:11:31 | METOP-B | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a576e672-0da6-3ba6-870f-6b85973edc84 | -6.5742 | -44.226299 | 2024-10-03 00:11:31 | METOP-B | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 07cf9ddc-7062-3c8b-a831-4a967e845441 | -7.1426 | -46.927601 | 2024-10-03 00:11:31 | METOP-B | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 75010819-08dc-3cfc-ba13-c2eb4e662c92 | -6.1502 | -42.463402 | 2024-10-03 00:11:32 | METOP-B | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 87c4abd5-b4d7-3ec3-bf12-0839f7dc0b8f | -6.1517 | -42.470299 | 2024-10-03 00:11:32 | METOP-B | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 8db4756a-f78c-31dc-a21c-e9a87847ac27 | -7.7304 | -49.854099 | 2024-10-03 00:11:32 | METOP-B | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e1222a7c-ca84-3880-9cdf-8bb15744b274 | -7.7337 | -49.8703 | 2024-10-03 00:11:32 | METOP-B | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a5f75b0d-557e-3a0f-8b78-e79e90fcb8b0 | -7.7239 | -49.872299 | 2024-10-03 00:11:32 | METOP-B | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ae7c0a5f-3a92-30d5-b696-ebcbc0b5a909 | -6.1574 | -42.908501 | 2024-10-03 00:11:33 | METOP-B | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 9901c676-724f-3baf-aa1f-e24a5392faa1 | -6.159 | -42.915401 | 2024-10-03 00:11:33 | METOP-B | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| c1ade5bc-9f5d-38b3-b59f-d20b0a61ed02 | -6.1626 | -42.8857 | 2024-10-03 00:11:33 | METOP-B | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| eb68c2e7-cd27-3192-9841-e51a001a5121 | -6.1641 | -42.892601 | 2024-10-03 00:11:33 | METOP-B | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 395b84f3-ac08-3ab8-9c67-a1d177a555c0 | -6.1672 | -42.906399 | 2024-10-03 00:11:33 | METOP-B | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| f03aaee1-3922-3983-98b4-005ba41b1625 | -6.1688 | -42.9133 | 2024-10-03 00:11:33 | METOP-B | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 60caf342-5c46-34db-bcea-86a6f59737c9 | -6.2933 | -43.424301 | 2024-10-03 00:11:33 | METOP-B | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7af03f26-87d1-3788-b8cf-16ceab3fe8e0 | -6.2949 | -43.431301 | 2024-10-03 00:11:33 | METOP-B | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 02ff9db1-ab16-32c7-8bdd-68ae8107ed5b | -6.253 | -43.381802 | 2024-10-03 00:11:33 | METOP-B | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c9e9b066-d0e0-3846-8604-94eb1d773529 | -6.5362 | -44.706299 | 2024-10-03 00:11:33 | METOP-B | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a4160f67-8772-33e9-8293-4980130db0dd | -6.1717 | -43.202599 | 2024-10-03 00:11:34 | METOP-B | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | nan |
| a1a6a889-8634-352e-9d0e-349deefcbe06 | -6.189 | -43.417999 | 2024-10-03 00:11:34 | METOP-B | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9a078d6a-09aa-3cee-b388-8932888ed100 | -6.3181 | -43.7668 | 2024-10-03 00:11:34 | METOP-B | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ebe10ac9-5d33-3653-a970-5754e2499490 | -6.6516 | -45.325699 | 2024-10-03 00:11:34 | METOP-B | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cbc25b3f-7511-3f92-97bc-b05769a7ee2b | -6.6534 | -45.3339 | 2024-10-03 00:11:34 | METOP-B | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| aa775f7d-cfca-31e3-a323-6e9a39aa645c | -7.1069 | -47.859798 | 2024-10-03 00:11:35 | METOP-B | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 79d0b6be-f498-3dd4-b25a-a02fe8fdecd5 | -7.1094 | -47.871399 | 2024-10-03 00:11:35 | METOP-B | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 654e1d4e-5f73-3e03-ae81-3012e738ab26 | -6.3175 | -44.367802 | 2024-10-03 00:11:36 | METOP-B | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ec69b7bc-79a1-3528-a22f-11c9fc00f100 | -6.3192 | -44.375198 | 2024-10-03 00:11:36 | METOP-B | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3326f73a-8786-35e2-acba-c28ccdd9271f | -5.9237 | -42.830601 | 2024-10-03 00:11:37 | METOP-B | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 8c0b2b41-4086-3efb-b8f6-618bb56db26e | -7.0586 | -48.016499 | 2024-10-03 00:11:37 | METOP-B | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d44fe7da-d28d-38cb-ad53-8d847e23a3f1 | -6.0763 | -43.790199 | 2024-10-03 00:11:38 | METOP-B | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 57e4402e-890d-3ca1-9e21-f46f6474c5d3 | -6.1206 | -44.035702 | 2024-10-03 00:11:38 | METOP-B | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bea3accc-9fb8-3a19-87c4-d4a11992c03c | -6.1222 | -44.0429 | 2024-10-03 00:11:38 | METOP-B | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| de0df934-5cc9-35c0-8bf7-8b8760e61d69 | -6.1398 | -44.122501 | 2024-10-03 00:11:38 | METOP-B | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3be4cc43-ec56-3792-9ecd-098af32d41cf | -6.1414 | -44.129799 | 2024-10-03 00:11:38 | METOP-B | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0d62cb01-c801-31d7-974c-583e6758574f | -6.1108 | -44.0378 | 2024-10-03 00:11:38 | METOP-B | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a5f36a3d-4b2f-38b8-8fc8-22ec39f0d960 | -6.1124 | -44.045101 | 2024-10-03 00:11:38 | METOP-B | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7d073045-752b-3498-b074-2dd2343f33eb | -6.2614 | -44.7183 | 2024-10-03 00:11:38 | METOP-B | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6a767bcd-de83-3589-841b-1cd0b55f2ad1 | -6.2631 | -44.726002 | 2024-10-03 00:11:38 | METOP-B | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cfb94ce6-d87b-3523-801a-df6d06cb1ba6 | -6.101 | -44.040001 | 2024-10-03 00:11:38 | METOP-B | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4c2509fe-478b-3b39-ad6a-b9e30fa90694 | -6.1026 | -44.047199 | 2024-10-03 00:11:38 | METOP-B | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f7e6dc38-f692-3b7a-89ba-1103c1b42ad3 | -6.0896 | -44.034901 | 2024-10-03 00:11:38 | METOP-B | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0579e15d-034c-3cb9-a86f-979bb8d47de5 | -6.0912 | -44.042099 | 2024-10-03 00:11:38 | METOP-B | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ed6be7f1-10a5-30aa-b3d8-e4d1c68495e7 | -5.7247 | -42.587101 | 2024-10-03 00:11:39 | METOP-B | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| b646d83d-10e8-35a0-aa06-fab0dca49afa | -5.7263 | -42.593899 | 2024-10-03 00:11:39 | METOP-B | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| f51d069d-9267-342c-a561-5429b66da4ad | -5.7278 | -42.6008 | 2024-10-03 00:11:39 | METOP-B | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| dc99c771-fae5-3b10-8c33-c5f7eab3c941 | -5.8693 | -43.415501 | 2024-10-03 00:11:40 | METOP-B | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| dc91278f-04f2-35db-b752-42baa05e8253 | -5.8708 | -43.422501 | 2024-10-03 00:11:40 | METOP-B | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 964ba699-1e63-3f3a-af90-6908a51fe2e9 | -5.8595 | -43.417599 | 2024-10-03 00:11:40 | METOP-B | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 325e849f-38fa-3b53-bcaf-9757dbb43e46 | -5.8844 | -43.713799 | 2024-10-03 00:11:40 | METOP-B | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f962b25c-eb3f-3669-8854-75f4ba4ac830 | -5.8306 | -43.7034 | 2024-10-03 00:11:41 | METOP-B | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 87f4cd5a-73d9-3101-acb9-096a98bdfa96 | -5.8322 | -43.710499 | 2024-10-03 00:11:41 | METOP-B | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fe15e4e9-9180-3669-a3e7-0e93e9c39e64 | -6.4787 | -46.462002 | 2024-10-03 00:11:41 | METOP-B | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3dea5eff-78e9-3a95-b5a6-92408ce768b8 | -6.4807 | -46.471298 | 2024-10-03 00:11:41 | METOP-B | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c555ba5c-873c-3b4b-8a50-89057a44fe30 | -6.0813 | -44.694099 | 2024-10-03 00:11:41 | METOP-B | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fe7d2a7e-7cd1-3f97-8d7b-5ddca734dbfa | -6.0829 | -44.701599 | 2024-10-03 00:11:41 | METOP-B | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f46de3aa-206d-392b-a949-724a941fc088 | -6.0731 | -44.7038 | 2024-10-03 00:11:41 | METOP-B | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 08fb092d-2fea-3b94-910d-efe5ce0078a5 | -6.1106 | -44.920101 | 2024-10-03 00:11:41 | METOP-B | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| eea0023d-f043-320f-b1c7-afe6e3ec96f3 | -6.1123 | -44.927799 | 2024-10-03 00:11:41 | METOP-B | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6e954e7a-b0cf-3382-9aad-f2697ded42dc | -6.114 | -44.935501 | 2024-10-03 00:11:41 | METOP-B | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c5352e8d-86bd-3143-8972-ed747b35c52e | -6.0072 | -44.544899 | 2024-10-03 00:11:41 | METOP-B | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4154fa25-3938-3ed9-ae68-6beea5b1cab7 | -6.0088 | -44.552299 | 2024-10-03 00:11:41 | METOP-B | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b7c31343-3621-34f5-a641-c6edbf171b25 | -6.0105 | -44.559799 | 2024-10-03 00:11:41 | METOP-B | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 637c1dc9-0606-3b18-aa1d-f31074aa4415 | -5.5284 | -42.767399 | 2024-10-03 00:11:43 | METOP-B | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 829fcccc-012a-3eed-b1b7-8b5c5a6923cc | -5.5299 | -42.7743 | 2024-10-03 00:11:43 | METOP-B | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 77c045d2-7b3c-30c9-bd0f-2f3588146e49 | -5.5186 | -42.7696 | 2024-10-03 00:11:43 | METOP-B | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| cd35ddfc-5a43-3fd3-bf57-3ae85aa08e6a | -5.5201 | -42.776402 | 2024-10-03 00:11:43 | METOP-B | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| f77d354b-e19d-3e56-b7e9-da36ac7ae23a | -5.5615 | -43.098701 | 2024-10-03 00:11:43 | METOP-B | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Caatinga | nan |
| 69a2dcf8-4ce8-3131-a6da-671861b1ae72 | -5.5631 | -43.105598 | 2024-10-03 00:11:43 | METOP-B | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Caatinga | nan |
| 2fb69f9d-c871-35de-a84f-69b60bfb025a | -5.7141 | -43.780899 | 2024-10-03 00:11:43 | METOP-B | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8cdd678c-6ad6-3f87-bde9-8d59f60e7a77 | -6.3514 | -46.4893 | 2024-10-03 00:11:43 | METOP-B | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e1c832aa-de5b-390d-accd-71f19450eb02 | -6.3534 | -46.4986 | 2024-10-03 00:11:43 | METOP-B | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 096007c1-732d-3ff3-8c55-16269968f2c0 | -6.9651 | -49.404202 | 2024-10-03 00:11:43 | METOP-B | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f34e913f-b439-367d-88a9-490eaaf8c8e7 | -6.9682 | -49.4188 | 2024-10-03 00:11:43 | METOP-B | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 278f92ad-1459-3053-a89d-85dbd09d942b | -5.9108 | -44.6208 | 2024-10-03 00:11:43 | METOP-B | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 847c9d05-e644-3ba8-ade2-9346f7ca1ebf | -5.9125 | -44.6283 | 2024-10-03 00:11:43 | METOP-B | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f2e6986e-0100-38f8-bd7d-318d83413c27 | -5.7033 | -43.917198 | 2024-10-03 00:11:44 | METOP-B | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 82321f3a-665d-301c-9100-72c6974df740 | -5.7049 | -43.924301 | 2024-10-03 00:11:44 | METOP-B | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 776abc27-0636-3c5d-bcfa-86df9cbc7b4d | -5.8519 | -44.5867 | 2024-10-03 00:11:44 | METOP-B | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0db86034-af89-3446-9993-cdb5791bca32 | -5.8536 | -44.5942 | 2024-10-03 00:11:44 | METOP-B | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 03f8cce1-09c0-34c1-a422-eed58011ba2a | -5.8552 | -44.6017 | 2024-10-03 00:11:44 | METOP-B | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 17b00948-2113-36a3-aaa6-bc1620a677e6 | -5.8421 | -44.588799 | 2024-10-03 00:11:44 | METOP-B | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4f512d6d-9ede-3c64-b20e-968e1003b60e | -5.8438 | -44.596298 | 2024-10-03 00:11:44 | METOP-B | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 55fefcf6-b944-33ba-96b8-5686ae2ef39e | -5.8454 | -44.603802 | 2024-10-03 00:11:44 | METOP-B | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a2ecae9c-8d94-35b8-b473-5e58bd859880 | -5.4059 | -42.909801 | 2024-10-03 00:11:45 | METOP-B | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| a9828c1c-ac74-3687-8b43-df9f00144640 | -5.4074 | -42.916599 | 2024-10-03 00:11:45 | METOP-B | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 82ea05d8-f4af-3b15-9147-1d57ce1fb449 | -5.3961 | -42.911999 | 2024-10-03 00:11:45 | METOP-B | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 3ee1830b-d42a-32d4-8858-6653fe5fddef | -5.3969 | -43.099098 | 2024-10-03 00:11:46 | METOP-B | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 61b5650a-26de-3121-8b9d-6e2cdeb835a6 | -5.3984 | -43.105999 | 2024-10-03 00:11:46 | METOP-B | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| dfbe2242-8ca0-3145-a208-9c452e5efec3 | -6.2728 | -46.977402 | 2024-10-03 00:11:46 | METOP-B | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README9.md)
