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

## Dados Diários - Página 86

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 39504f34-d7be-3eac-86f9-1a57baaee9d3 | -5.8692 | -45.0759 | 2025-09-07 12:50:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 105.3 |
| 7891018b-821d-316d-94c0-4c59a42ee48c | -12.8444 | -47.9905 | 2025-09-07 12:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 63.2 |
| dff17cfa-6370-3a4e-9032-46cb4c99fd4c | -5.9899 | -44.1528 | 2025-09-07 12:50:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 350.2 |
| 4bad71f6-cdaf-378a-a941-e13d05595022 | -6.2127 | -42.4532 | 2025-09-07 12:50:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 261.8 |
| 62a144e6-0a98-37ac-9dea-caa89abb180b | -5.9711 | -44.1542 | 2025-09-07 12:50:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 148.0 |
| 4a44a8fe-65cf-3f3c-954f-5035a9fdbaf4 | -7.6173 | -44.6772 | 2025-09-07 12:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 68.1 |
| d428e8b0-dfb9-3247-9741-a19fce509fbd | -12.8252 | -47.9932 | 2025-09-07 12:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 92.0 |
| 27361e36-981a-3df4-86f2-25bfc8d3a3a3 | -6.0086 | -44.1513 | 2025-09-07 12:50:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 120.6 |
| bd36cd9e-17bc-3f75-b2de-c3ddc84a93d7 | -11.2636 | -46.4843 | 2025-09-07 12:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 134.5 |
| b9b371a7-962b-350f-b35f-37a0e0071c3f | -6.2315 | -42.4515 | 2025-09-07 12:50:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 150.6 |
| 3ef7772b-1f62-35e1-a485-96be724c2bed | -5.8879 | -45.0745 | 2025-09-07 12:50:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 5b1684b8-8235-3247-8bfa-66a8ae7ad087 | -15.1235 | -48.0852 | 2025-09-07 12:50:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 83f83d44-48cd-3e5b-8e05-80ae83a77133 | -11.264 | -46.4617 | 2025-09-07 12:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 138.9 |
| 9127dbd7-15b6-368c-9ebf-812bb31833f2 | -13.0542 | -48.0716 | 2025-09-07 12:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 0eec8bea-cef6-38c0-b221-63bef5a2e87f | -8.1421 | -44.8769 | 2025-09-07 12:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 112.7 |
| a03638f8-1fa0-3f31-b0c9-e7cb17a5135c | -8.161 | -44.875 | 2025-09-07 12:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 242.0 |
| bd5bda89-1d5d-3b2a-9081-564621884f0f | -11.5669 | -47.7638 | 2025-09-07 12:50:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 100.3 |
| f5ed0d12-064d-3692-a5b6-d97f20b189ad | -14.5076 | -48.7641 | 2025-09-07 12:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 104.5 |
| 7f744558-c4c6-3b45-8f95-7977af034d31 | -6.2062 | -45.0506 | 2025-09-07 13:00:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 86.5 |
| c41de68f-575d-3a61-81c9-a55d47af1a6e | -8.1421 | -44.8769 | 2025-09-07 13:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 131.8 |
| 5b3e7252-fb29-3b8c-a8c8-a4a92924ac9b | -15.1235 | -48.0852 | 2025-09-07 13:00:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 65.7 |
| 90400c44-a26b-39cc-b994-12872b09fb52 | -16.9427 | -45.7982 | 2025-09-07 13:00:00 | GOES-19 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 83.6 |
| ce467b8f-e7fc-3bb5-bf1c-676a24b11cae | -6.2108 | -42.6426 | 2025-09-07 13:00:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 88.9 |
| b03e6cf8-efe7-3913-b525-0f296c80b61c | -14.4882 | -48.7671 | 2025-09-07 13:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 143.7 |
| e7ca4a4a-f8eb-32e0-b9b5-3683c967f7ef | -5.9899 | -44.1528 | 2025-09-07 13:00:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 371.1 |
| 30155d20-df9b-38eb-b429-33c6b786caa4 | -5.8403 | -44.1181 | 2025-09-07 13:00:00 | GOES-19 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 76.7 |
| f318dba8-84d9-3fc2-a37f-665dae0eb215 | -11.264 | -46.4617 | 2025-09-07 13:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 246.1 |
| 17519b7e-2996-314a-84b5-b5b0b8611869 | -13.8407 | -46.2598 | 2025-09-07 13:00:00 | GOES-19 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 045e0efc-d14d-31e9-84df-afbb8e0cd0c6 | -5.9711 | -44.1542 | 2025-09-07 13:00:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 177.6 |
| da9a9bb5-8245-3417-8d4a-a4105a4d3f38 | -7.7439 | -50.316 | 2025-09-07 13:00:00 | GOES-19 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 93451b1a-8531-3026-8204-a86c5c08bf0a | -11.5669 | -47.7638 | 2025-09-07 13:00:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 121.0 |
| b9916224-4a71-3d99-ae6f-ad36053fed2c | -12.7641 | -52.9498 | 2025-09-07 13:00:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 127.0 |
| 70798c16-4206-3f22-ad35-b3552270f128 | -6.1923 | -42.6205 | 2025-09-07 13:00:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 88.4 |
| d71625a5-3d2b-3f01-ba00-0725c7a3719c | -8.1612 | -44.8521 | 2025-09-07 13:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 103.7 |
| 743537a1-7853-37cc-987a-5b13b9cd3d89 | -11.4093 | -43.5573 | 2025-09-07 13:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 3cb89b8c-d45e-3168-a00f-7cc6069c94ad | -19.4891 | -47.7879 | 2025-09-07 13:00:00 | GOES-19 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 91.7 |
| b87f368d-87dc-3734-aafe-8a6f5b88006e | -12.3016 | -47.2416 | 2025-09-07 13:00:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 90.0 |
| e1fcab5a-48d1-3446-bdc0-4da5c31dca2b | -11.586 | -47.7613 | 2025-09-07 13:00:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 147.8 |
| f9e22ad1-b489-388b-90b0-de5095c9a603 | -5.8216 | -44.1196 | 2025-09-07 13:00:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 84.6 |
| a0116a20-e9b8-353c-8f65-fd10b7f5ec69 | -11.1575 | -48.3883 | 2025-09-07 13:00:00 | GOES-19 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 38691d31-f51a-374e-945e-b5715c09db1b | -11.5856 | -47.7836 | 2025-09-07 13:00:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 58.2 |
| d4ba6033-d337-3f3a-8d9e-d887ffa108a3 | -5.8959 | -44.183 | 2025-09-07 13:00:00 | GOES-19 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 8e8c5aba-14e8-3912-ad4b-b190f6f4f862 | -12.8444 | -47.9905 | 2025-09-07 13:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 55.4 |
| 43d5a17f-98dd-3d3b-9210-26c42de9872f | -8.161 | -44.875 | 2025-09-07 13:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 231.7 |
| de809fb6-2c57-3187-acca-6aa8c8c98bb7 | -7.725 | -50.3386 | 2025-09-07 13:00:00 | GOES-19 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 144.3 |
| 1ff9b897-a1f4-3684-b626-73949b579fa9 | -12.948 | -54.7724 | 2025-09-07 13:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 143.6 |
| 3c73b8e2-f644-39a3-9f0e-e58cce3d5615 | -13.2404 | -51.7997 | 2025-09-07 13:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 1470183f-79f1-3025-ac16-dafa3bbd3e07 | -6.2064 | -45.0278 | 2025-09-07 13:00:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 88c76495-ae74-3502-b4bd-54656272b6a0 | -14.5076 | -48.7641 | 2025-09-07 13:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 134.4 |
| f20b137b-3d7e-3733-ba78-7d84fd15b35e | -12.9289 | -54.7744 | 2025-09-07 13:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 81.1 |
| 93d8f152-0706-3bb8-957a-095576680114 | -12.8248 | -48.0155 | 2025-09-07 13:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 3bcb9667-0a37-32b0-9f4d-a4afd0ae7405 | -6.2127 | -42.4532 | 2025-09-07 13:00:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 93.5 |
| 07ecf943-802f-3b89-952d-1627e758fa3b | -11.2636 | -46.4843 | 2025-09-07 13:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 239.3 |
| fdc6b2ee-6e91-3e7f-8b6c-0fd089d8cee5 | -13.8213 | -46.2631 | 2025-09-07 13:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 62.2 |
| 4977eaa2-6bda-3328-9f63-4653b6994d60 | -5.9713 | -44.1312 | 2025-09-07 13:00:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 84.8 |
| 57d694e4-ce69-3de7-9b35-952dabe87dbb | -7.8154 | -45.4329 | 2025-09-07 13:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 2ca95b3c-3b37-3c2b-bd74-9c294c9d5b49 | -6.6581 | -44.8093 | 2025-09-07 13:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 64.8 |
| cab944ee-2d61-3f76-8666-22341de2d7fd | -5.9901 | -44.1297 | 2025-09-07 13:00:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 148.7 |
| b0840b2e-a9e2-35fd-97d4-7306bfcb5808 | -12.9477 | -54.793 | 2025-09-07 13:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 785be312-292c-37de-83fe-ff1b29c6e78e | -6.0086 | -44.1513 | 2025-09-07 13:00:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 141.1 |
| fbe37717-61a1-372d-bacb-8bb55a6db17f | -12.8252 | -47.9932 | 2025-09-07 13:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 8641f8c9-f58d-3d22-98b3-067c5de9d990 | -12.7832 | -52.9477 | 2025-09-07 13:00:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 102.1 |
| 47eb5893-51e1-39d0-a7a8-f09c4eaad810 | -7.7252 | -50.3174 | 2025-09-07 13:00:00 | GOES-19 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 94.1 |
| 3786cedd-7570-390e-82b9-51cf6bf6be0b | -7.7437 | -50.3372 | 2025-09-07 13:00:00 | GOES-19 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 95.5 |
| dd557d9d-f5c1-3325-aaf7-c1834bc48df2 | -6.192 | -42.6442 | 2025-09-07 13:00:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 115.1 |
| 15e41d19-3792-3262-b47a-fa656ac6c79a | -15.5413 | -42.6545 | 2025-09-07 13:00:00 | GOES-19 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 136.1 |
| 32d91639-4876-3a1a-aab1-4348f2529e2b | -5.8403 | -44.1181 | 2025-09-07 13:10:00 | GOES-19 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 81.2 |
| f27e4ebb-3805-3de6-aac6-167aa3d3c161 | -9.0229 | -49.8048 | 2025-09-07 13:10:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 65.3 |
| 0e7ff003-642d-3086-ad7c-27d59ff3bbae | -5.8214 | -44.1426 | 2025-09-07 13:10:00 | GOES-19 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 2f048280-90a1-33c2-9c60-d9981b10c4bc | -12.8029 | -52.9037 | 2025-09-07 13:10:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 76.4 |
| 53035ee5-a923-337b-873a-3a37d48f9d23 | -6.5915 | -43.9883 | 2025-09-07 13:10:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 67.2 |
| ecdfd592-c8af-33bb-a05b-af8662175857 | -18.043 | -47.0812 | 2025-09-07 13:10:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 90.7 |
| b1fd2018-30bb-315f-8209-cb4d49d68138 | -12.3016 | -47.2416 | 2025-09-07 13:10:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 40ffc14d-e3b1-32df-a765-36ff3036655b | -6.4976 | -43.9963 | 2025-09-07 13:10:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 602cccb1-44d2-3100-aa31-733d7339dc57 | -8.1612 | -44.8521 | 2025-09-07 13:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 141.1 |
| 4f9f5c83-2dd8-3efb-b21f-6d71c0214462 | -13.0521 | -47.1328 | 2025-09-07 13:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 32f59800-ee7d-3152-8d74-0d315d477aab | -15.1235 | -48.0852 | 2025-09-07 13:10:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 103.6 |
| f812c719-87dd-31b0-baba-12d09032fabb | -16.9427 | -45.7982 | 2025-09-07 13:10:00 | GOES-19 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 79.5 |
| ec77812f-476b-3b35-a806-713ce5c1d289 | -15.103 | -48.1334 | 2025-09-07 13:10:00 | GOES-19 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 50bcebe5-cb11-3850-87ba-34436b9bc40e | -11.3901 | -43.5602 | 2025-09-07 13:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 23617682-9bf3-32a3-b5aa-4247e6a35eea | -11.5669 | -47.7638 | 2025-09-07 13:10:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 17ba0f54-bb65-3dd0-a957-66bc6b16c42a | -6.8939 | -45.5835 | 2025-09-07 13:10:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 00cc062e-0bb1-332b-b5a1-9a4510bf3c17 | -11.586 | -47.7613 | 2025-09-07 13:10:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 99.0 |
| abc84fd1-b446-345c-93cc-0a8bbdabf86b | -6.2108 | -42.6426 | 2025-09-07 13:10:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 95.7 |
| 7c53a8b4-2a8d-39d1-8e22-425b22f83896 | -11.264 | -46.4617 | 2025-09-07 13:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 266.0 |
| 006ad64d-4e9a-337e-8933-1bb657976938 | -6.1923 | -42.6205 | 2025-09-07 13:10:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 103.3 |
| f643a9ab-a3f6-3232-ac25-70eb7962cbe0 | -14.5076 | -48.7641 | 2025-09-07 13:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 112.4 |
| 949a3b40-679c-373b-ae5b-37c7ce8a8d84 | -11.2636 | -46.4843 | 2025-09-07 13:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 232.9 |
| 93a8f1bc-782b-3bcd-88f6-773e93fb18a7 | -12.8248 | -48.0155 | 2025-09-07 13:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 9b916618-7e11-31d5-ad7b-081e18cc914e | -12.7829 | -52.9686 | 2025-09-07 13:10:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 5434ce00-1007-37ec-abd5-73c468abbe19 | -12.7644 | -52.9289 | 2025-09-07 13:10:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 104.1 |
| c912a58d-586f-37e3-b79b-2163ee4ee1d6 | -12.9477 | -54.793 | 2025-09-07 13:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 92.1 |
| f8a69c37-7def-3786-b525-0f49f1eafb4a | -5.9899 | -44.1528 | 2025-09-07 13:10:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 238.9 |
| f84abff4-cf25-3aa8-94cb-2da3ad65bb38 | -6.0086 | -44.1513 | 2025-09-07 13:10:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 88.0 |
| cecb4dfd-0453-3eab-9f54-8e080bc64fb2 | -5.9711 | -44.1542 | 2025-09-07 13:10:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 137.4 |
| a032592d-588a-3e97-8b5c-c36fca967360 | -19.4891 | -47.7879 | 2025-09-07 13:10:00 | GOES-19 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 301.5 |
| f1563bc2-7bf6-3f06-b91c-e6d54300171d | -12.8252 | -47.9932 | 2025-09-07 13:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 93.8 |
| 37da1abd-4e2a-3e15-95ce-fd044f35ecad | -5.9901 | -44.1297 | 2025-09-07 13:10:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 133.7 |
| 7626b269-740f-3d4b-b99c-622c6e319c19 | -5.8216 | -44.1196 | 2025-09-07 13:10:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 128.0 |
| 234c01b9-b224-3d21-a4a7-c9a030edcf69 | -7.6173 | -44.6772 | 2025-09-07 13:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 82.6 |


[Clique aqui para ver as próximas entradas](README87.md)
