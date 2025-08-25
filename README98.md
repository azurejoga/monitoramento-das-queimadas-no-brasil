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

## Dados Diários - Página 98

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 733c4c90-69c2-3925-b10e-8a2a09b2ff4e | -12.6745 | -47.8366 | 2025-08-25 14:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 103.2 |
| 0d4d63d7-af5a-3263-a48f-03b670cf11af | -7.7834 | -44.9584 | 2025-08-25 14:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 152.9 |
| 5e6216a0-96e6-3988-bd57-f5d6afb67f9f | -10.7096 | -50.5359 | 2025-08-25 14:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 124.4 |
| 95e119d5-e1df-3580-b3f6-1b70e67e59cd | -9.1998 | -60.793 | 2025-08-25 14:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 132.5 |
| 3e6e17a3-ffc2-3c40-91d8-0a65a3c49416 | -7.586 | -47.4835 | 2025-08-25 14:10:00 | GOES-19 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 414.7 |
| d37c4294-b427-3b61-8a36-4cefa9725354 | -8.7584 | -49.9566 | 2025-08-25 14:10:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 122.4 |
| 40b5adcc-a5bf-36c1-b653-b36c6448f8e7 | -6.8202 | -59.4194 | 2025-08-25 14:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 115.2 |
| 491ab782-2fde-3922-8f0b-93017d2a83a3 | -11.2697 | -44.9781 | 2025-08-25 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 79.6 |
| dbe8d200-7b4c-38a5-9557-c1af5509392d | -6.9061 | -44.4217 | 2025-08-25 14:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 271.9 |
| 64405c32-f88c-3b65-b5b9-a6610821757d | -11.8601 | -45.1233 | 2025-08-25 14:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 92.5 |
| 9d4c8704-150e-3f65-b5b8-db8f2fb86f25 | -11.5917 | -46.2591 | 2025-08-25 14:10:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 96.4 |
| 1f8c5558-9f06-3d4f-81aa-5980039fbc42 | -7.9076 | -63.0919 | 2025-08-25 14:10:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 120.1 |
| 067e7962-b5ba-3240-9e8b-65fb8a15bd3a | -16.0556 | -45.7672 | 2025-08-25 14:10:00 | GOES-19 | URUCUIA | MINAS GERAIS | Brasil | 3170529 | 31 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 93dbc069-dc0e-3dea-a0f8-f87a242ba102 | -10.7015 | -47.1388 | 2025-08-25 14:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 087ca607-5e1d-3ac9-b70a-3e55d89a3084 | -21.4303 | -47.5922 | 2025-08-25 14:10:00 | GOES-19 | SÃO SIMÃO | SÃO PAULO | Brasil | 3550902 | 35 | 33 | nan | nan | nan | Cerrado | 206.5 |
| e6329647-b08e-3ea3-9b4b-c5fb0e12f3dc | -14.4362 | -56.4564 | 2025-08-25 14:10:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 102.3 |
| cdc041fa-8e65-3e72-bf01-f452439c6a23 | -18.715 | -45.1684 | 2025-08-25 14:10:00 | GOES-19 | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 172.6 |
| 7b3aa093-6008-31bf-bee2-a66e76f2fd1e | -7.904 | -45.8986 | 2025-08-25 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 96.3 |
| aa0ebd42-fe82-3351-973b-b0c75b35e7d1 | -10.0232 | -51.0712 | 2025-08-25 14:10:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 162.8 |
| 0132b0af-60d3-3e3c-9629-89f056f7565e | -11.5444 | -50.4662 | 2025-08-25 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 110.3 |
| 5543f203-6a70-32a8-aa2e-09a2ee683136 | -6.5216 | -45.343 | 2025-08-25 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 86c2308f-27d4-346e-a25f-06f05443b416 | -5.6254 | -45.1612 | 2025-08-25 14:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 79.4 |
| dc3128d6-a084-3db0-823c-5799bc3f84cd | -10.7093 | -50.5572 | 2025-08-25 14:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 97.7 |
| 39eb17c5-5dc2-3f74-9265-4e87c7e1dd5f | -9.181 | -60.8131 | 2025-08-25 14:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 79.9 |
| 709a9bb6-4efe-3bca-a047-f53cadac4a46 | -5.8612 | -43.8858 | 2025-08-25 14:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 37125670-2c58-3347-ae06-30d913428aeb | -7.7645 | -44.9602 | 2025-08-25 14:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 92.7 |
| dc53cb04-6899-3b5e-a26a-2a120d60ed66 | -14.9252 | -45.5169 | 2025-08-25 14:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 89.1 |
| 4b6c6353-954e-3e19-afd2-f8b6e7fe4d52 | -7.605 | -47.4599 | 2025-08-25 14:10:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 100.1 |
| c18e5790-51fb-329a-9cb9-0d8711a29358 | -5.6817 | -45.1347 | 2025-08-25 14:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 9321e9b7-229e-3b30-938e-09e494b007de | -9.1812 | -60.7939 | 2025-08-25 14:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 242.0 |
| efdda832-9428-3916-98a4-39918c88e9e9 | -14.5072 | -51.9354 | 2025-08-25 14:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 60.1 |
| 6e7b1a93-bef6-3d4c-ab86-b5dc58bbf3ed | -7.9077 | -63.073 | 2025-08-25 14:10:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 107.0 |
| d62d7042-007f-3971-9fea-0629bf212b08 | -10.2572 | -59.1081 | 2025-08-25 14:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 61.4 |
| c42da776-97bf-3604-b6bb-0d5e1bbf0414 | -5.6443 | -45.1373 | 2025-08-25 14:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 3d555267-4f7d-32a1-9439-bf833cd2379f | -9.1813 | -60.7747 | 2025-08-25 14:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 82.7 |
| 600a45d8-9f8b-3281-835f-9ee1be779915 | -13.4132 | -51.7784 | 2025-08-25 14:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 117.0 |
| d12b0156-359a-3673-adca-87f7ee857243 | -6.8873 | -44.4234 | 2025-08-25 14:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 93455c1c-6c0e-37c5-8ae5-469e5928082f | -6.8201 | -59.4386 | 2025-08-25 14:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 149.8 |
| 5d272e16-5a46-3c6f-a32a-93ef6fa51924 | -9.2076 | -59.7129 | 2025-08-25 14:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 0613135f-a639-3f40-aa79-b46e644bb330 | -14.9051 | -45.5439 | 2025-08-25 14:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 110.9 |
| 12b03036-e7d2-34d9-a691-b53fb9057cac | -7.8892 | -63.0737 | 2025-08-25 14:10:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 71.9 |
| fe20b6db-d857-3ecc-bc5d-35faec7190f2 | -14.3722 | -51.932 | 2025-08-25 14:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 82.3 |
| e92071fd-0890-3e28-b928-71b2ba23a4fa | -14.4169 | -56.4584 | 2025-08-25 14:10:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 881b8b02-e45f-3b7e-ae1d-e03c6626e598 | -6.7819 | -59.6711 | 2025-08-25 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 6e35b47e-0e0f-368d-b235-edce5dafb56e | -15.0725 | -48.6745 | 2025-08-25 14:20:00 | GOES-19 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 61.1 |
| 4ab11c57-22c3-3ed0-a054-a0489e7baacd | -21.4303 | -47.5922 | 2025-08-25 14:20:00 | GOES-19 | SÃO SIMÃO | SÃO PAULO | Brasil | 3550902 | 35 | 33 | nan | nan | nan | Cerrado | 526.9 |
| b0962093-c5bf-3b7f-88c0-3cadf4650fa7 | -21.4096 | -47.5973 | 2025-08-25 14:20:00 | GOES-19 | SÃO SIMÃO | SÃO PAULO | Brasil | 3550902 | 35 | 33 | nan | nan | nan | Cerrado | 129.0 |
| 92564303-f3f2-3005-83f9-4632bc7836f9 | -11.5444 | -50.4662 | 2025-08-25 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 146.1 |
| 94e37d11-82c7-3311-aa28-864404d18b1d | -9.1813 | -60.7747 | 2025-08-25 14:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 86.4 |
| ecba5d8f-db57-332e-9e21-1e38a04ca61c | -10.8167 | -48.3192 | 2025-08-25 14:20:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 7e6809fa-65f3-3855-a5b2-54b6c0d07289 | -10.5364 | -46.7568 | 2025-08-25 14:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 172.8 |
| acd3b1d3-f6a2-372a-8fa0-286ead2b943e | -8.0753 | -47.3303 | 2025-08-25 14:20:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 92.4 |
| 5cfe0358-509a-32c2-8c00-c773d36712ab | -14.9247 | -45.5403 | 2025-08-25 14:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 244.1 |
| 27688c17-1b2e-3adb-897f-f352cd7ff217 | -10.7096 | -50.5359 | 2025-08-25 14:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 142.1 |
| 792fefeb-dcfc-3772-890d-c184afc523bb | -11.5441 | -50.4876 | 2025-08-25 14:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 121.5 |
| e9cb6fc4-087c-319b-9ead-443b49327b40 | -6.1377 | -44.3711 | 2025-08-25 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 66ad0e69-26f0-3879-ab30-497c0287c8e4 | -8.8084 | -47.3266 | 2025-08-25 14:20:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 80.1 |
| a9fc11fd-62d2-3507-bab4-778ec4e97558 | -9.1999 | -60.7738 | 2025-08-25 14:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 105a18e5-5758-3813-9749-6fea5ae70bc1 | -6.9061 | -44.4217 | 2025-08-25 14:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 117.3 |
| 64c0ca81-60a7-3449-b688-aab51dd9d6f1 | -10.4054 | -64.3911 | 2025-08-25 14:20:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 70.7 |
| b8a6447b-1ca6-3e05-8aac-4869e9f80564 | -8.7584 | -49.9566 | 2025-08-25 14:20:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 116.9 |
| e4976326-e60a-39b5-90fb-2a47152c584e | -9.2076 | -59.7129 | 2025-08-25 14:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 08187642-4f0a-3d78-818e-83de828371f1 | -18.715 | -45.1684 | 2025-08-25 14:20:00 | GOES-19 | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 101.0 |
| 0a8b5b1b-6900-3251-81c9-86218bd30ebe | -8.1119 | -62.877 | 2025-08-25 14:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 22c9e6b1-e66e-3520-a133-3f0c3eba9fe1 | -8.7896 | -47.3284 | 2025-08-25 14:20:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 107.3 |
| 199355ea-527e-36ad-8e55-7a67ef2f87a2 | -12.6937 | -47.8339 | 2025-08-25 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 216.8 |
| a35104ce-b9a0-316f-8255-2f8f71ce82af | -15.1255 | -59.6054 | 2025-08-25 14:20:00 | GOES-19 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 88be7445-f423-3165-b05f-2a6fcc1eaa4e | -6.8201 | -59.4386 | 2025-08-25 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 139.5 |
| bb2eb0f3-d708-31a3-8dd4-2f8d5ab37f0e | -11.9277 | -46.7322 | 2025-08-25 14:20:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 92.4 |
| 23062d69-d6ee-389d-9423-0cea49a7b0bf | -9.181 | -60.8131 | 2025-08-25 14:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 92.8 |
| a9eb4611-9572-3582-a064-e03291eec431 | -9.1998 | -60.793 | 2025-08-25 14:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 165.8 |
| be9b9ead-394e-3db2-b878-fd568c861384 | -14.3722 | -51.932 | 2025-08-25 14:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 108.6 |
| 602cae18-bd7c-3417-9207-4f119f3736b6 | -8.1304 | -62.8763 | 2025-08-25 14:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 5f8783d9-4e94-311f-a145-e1819f48a24d | -9.1812 | -60.7939 | 2025-08-25 14:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 237.3 |
| 1678aa9e-a24f-31ed-8db2-fce5317e1510 | -7.5862 | -47.4615 | 2025-08-25 14:20:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 130.9 |
| 1a488bed-478d-3852-861d-0829e6448514 | -7.605 | -47.4599 | 2025-08-25 14:20:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 120.0 |
| 7ddd7199-74c6-32dc-afa9-3345c5395c52 | -6.8202 | -59.4194 | 2025-08-25 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 124.4 |
| b3f90c56-6dff-3276-a7c4-8130eb1dc1dd | -9.5702 | -48.1724 | 2025-08-25 14:20:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 84.0 |
| dfbc0d7c-d33c-3602-bc96-f79150f8464c | -6.8873 | -44.4234 | 2025-08-25 14:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 1e9c9cc5-d669-3ae0-adca-b68d9c993bb8 | -14.5072 | -51.9354 | 2025-08-25 14:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 68.7 |
| b3f4231d-b504-3274-9936-5ef4eaf70189 | -6.782 | -59.6519 | 2025-08-25 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.3 |
| aaf13e50-401e-37b7-b220-3a084841b8e3 | -12.6745 | -47.8366 | 2025-08-25 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 120.7 |
| a383d319-557b-3440-a504-c69172da43a3 | -7.6326 | -62.7243 | 2025-08-25 14:20:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 71.9 |
| fbc9d57d-0054-33bb-8f3e-fd274c17f3db | -5.861 | -43.909 | 2025-08-25 14:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 51be78cb-95d5-3ae2-8eea-bbb665cc6425 | -10.7093 | -50.5572 | 2025-08-25 14:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 108.9 |
| 503d3e68-5a3e-3f9f-8c78-966ea4185ad2 | -10.2572 | -59.1081 | 2025-08-25 14:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 4d6251c3-a126-347d-9ef8-8b92546f6f06 | -7.586 | -47.4835 | 2025-08-25 14:20:00 | GOES-19 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 562.3 |
| 0a0a54e0-140a-3b9e-bf98-8870c1ffe8af | -11.6093 | -46.3472 | 2025-08-25 14:20:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 4e7d2432-5c04-3e03-b602-a476cc73d221 | -5.8612 | -43.8858 | 2025-08-25 14:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 83.8 |
| 7d363d17-d04b-3f98-94b1-cadaf7ef28db | -9.1996 | -60.8122 | 2025-08-25 14:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 63.1 |
| f4478f52-f2f8-3bc6-a666-6e8434bba136 | -15.1448 | -59.6037 | 2025-08-25 14:20:00 | GOES-19 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 160.3 |
| 79fc2e81-fec5-385b-a170-358b2d513922 | -8.2129 | -61.3739 | 2025-08-25 14:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 76.8 |
| 89934b32-94bb-37c5-9d2c-97b0d43aa07a | -9.1812 | -60.7939 | 2025-08-25 14:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 299.7 |
| d2c174d7-c3e4-3a2c-a19d-edb0b9f25c71 | -10.4241 | -64.3903 | 2025-08-25 14:30:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 76.7 |
| 4c38f2a8-83ff-3414-8376-8ea3ce46f635 | -9.5702 | -48.1724 | 2025-08-25 14:30:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 98.4 |
| 3f479e4f-1f42-33f5-99f9-95489bf06d6d | -8.2128 | -61.393 | 2025-08-25 14:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 70.7 |
| bb69d9f2-139a-35c8-ae2d-8c2a8c908772 | -21.4096 | -47.5973 | 2025-08-25 14:30:00 | GOES-19 | SÃO SIMÃO | SÃO PAULO | Brasil | 3550902 | 35 | 33 | nan | nan | nan | Cerrado | 382.7 |
| f6123b09-b6a9-32a2-aad6-224ae5a4a740 | -8.2314 | -61.3732 | 2025-08-25 14:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 34045760-90d4-300c-945d-b2fe07be4501 | -10.4526 | -49.9643 | 2025-08-25 14:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 79.5 |
| d3aad052-a2ce-3cba-a933-f19dfcdd4c2b | -7.5862 | -47.4615 | 2025-08-25 14:30:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 134.4 |


[Clique aqui para ver as próximas entradas](README99.md)
