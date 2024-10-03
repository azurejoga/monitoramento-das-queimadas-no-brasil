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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 76416669-b723-318e-a014-378963f7b676 | -13.9453 | -52.572498 | 2024-10-03 01:03:26 | METOP-C | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ab0aaaaf-6252-3921-b7d8-cc02e0e95862 | -13.9551 | -52.570301 | 2024-10-03 01:03:26 | METOP-C | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0bb898bd-a0fc-376b-9879-f7c64e7656c4 | -13.9567 | -52.577599 | 2024-10-03 01:03:26 | METOP-C | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d1f614f0-36d3-31eb-b51c-76d88d8d3df4 | -11.8344 | -43.817799 | 2024-10-03 01:03:27 | METOP-C | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 01a3ec43-dcc8-3b7f-b2e3-9d82d0086a53 | -11.8385 | -43.833698 | 2024-10-03 01:03:27 | METOP-C | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1209c9b0-6253-3579-a9a2-4c9eafbe6f45 | -13.6151 | -51.181198 | 2024-10-03 01:03:27 | METOP-C | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2b1c15ca-6d7f-347c-bd72-3cfcebb13805 | -13.5545 | -51.232201 | 2024-10-03 01:03:28 | METOP-C | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 400566ba-2ccf-33d3-b05f-8306563f4575 | -13.5561 | -51.239201 | 2024-10-03 01:03:28 | METOP-C | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4b08b70a-b56b-315e-a42e-5866b49db39c | -13.5576 | -51.2463 | 2024-10-03 01:03:28 | METOP-C | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ff5c9b09-a3f2-38d5-95b6-3a51c65161c9 | -13.5624 | -51.2673 | 2024-10-03 01:03:28 | METOP-C | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c501b3c0-61c2-358f-84bc-1eda64ebd0f4 | -13.564 | -51.274399 | 2024-10-03 01:03:28 | METOP-C | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 98f87008-90f5-3541-948c-289a574efc0b | -13.5431 | -51.227501 | 2024-10-03 01:03:28 | METOP-C | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 15670bae-11ea-3ea4-a578-4a707b29d876 | -13.5447 | -51.234501 | 2024-10-03 01:03:28 | METOP-C | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 367d5d8d-6cc1-3eb7-a813-f6e5cb55e285 | -13.5463 | -51.241501 | 2024-10-03 01:03:28 | METOP-C | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 07d9b6aa-6db1-364e-99ac-c6c14e884c41 | -13.5478 | -51.2486 | 2024-10-03 01:03:28 | METOP-C | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a46e7789-563b-3a6d-9a30-496b2aa0a802 | -13.5494 | -51.2556 | 2024-10-03 01:03:28 | METOP-C | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| bb4d4170-dbee-35e4-bb17-0d54f0c08d53 | -13.551 | -51.2626 | 2024-10-03 01:03:28 | METOP-C | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| bee62e07-b42c-34c8-8c17-5d3159e0c824 | -13.5111 | -51.131599 | 2024-10-03 01:03:28 | METOP-C | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6c9bf677-8e90-3692-9292-c60b6b6ff7f0 | -13.5127 | -51.138599 | 2024-10-03 01:03:28 | METOP-C | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 91150b9a-5daa-3eaf-99c0-bb3170200cd5 | -13.5143 | -51.145599 | 2024-10-03 01:03:28 | METOP-C | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9a88de5a-bd11-31b6-9b5b-16e2a2105bc9 | -13.5159 | -51.152599 | 2024-10-03 01:03:28 | METOP-C | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5b513ec2-5e89-3c30-82f2-e4932b210bae | -13.5412 | -51.2649 | 2024-10-03 01:03:28 | METOP-C | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a86abae9-eb17-3fb1-af3e-a03d42492317 | -13.5428 | -51.2719 | 2024-10-03 01:03:28 | METOP-C | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 85a5b0ae-182c-3085-8444-88c36407fe56 | -13.5045 | -51.1479 | 2024-10-03 01:03:28 | METOP-C | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 29b91019-c23d-3aee-9e12-cd92d89718aa | -13.5172 | -51.203999 | 2024-10-03 01:03:28 | METOP-C | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8fb10b4c-c2cf-3f4a-98f0-fe5d9d22a929 | -13.5188 | -51.211102 | 2024-10-03 01:03:28 | METOP-C | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 308f8e8e-d56a-3011-bcba-01e31a37e1ec | -14.5104 | -45.2229 | 2024-10-03 01:03:29 | METOP-C | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 08d055c6-f1ab-37e1-8c76-eff792d20b55 | -14.5133 | -45.2346 | 2024-10-03 01:03:29 | METOP-C | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2e7e9b08-241c-3a48-81ba-af7300b8117c | -12.261 | -45.9538 | 2024-10-03 01:03:29 | METOP-C | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| dc35caa6-51f3-311d-9ec3-ea7ca450e45c | -12.2639 | -45.965199 | 2024-10-03 01:03:29 | METOP-C | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e23d2aaa-bf92-38ef-b22d-aa99da4bab13 | -12.2667 | -45.976501 | 2024-10-03 01:03:29 | METOP-C | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7adc9347-51c1-3abc-8756-36cb87516dc9 | -13.5118 | -51.271702 | 2024-10-03 01:03:29 | METOP-C | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 939263ac-6986-3e0a-a399-88de8f567191 | -13.5134 | -51.278702 | 2024-10-03 01:03:29 | METOP-C | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 44dd15b5-3469-33c2-bfc1-b75fb4098671 | -15.1491 | -48.087101 | 2024-10-03 01:03:30 | METOP-C | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| e007d5fb-4f95-3d1b-8fee-3bc2d80326d7 | -13.2515 | -51.2141 | 2024-10-03 01:03:33 | METOP-C | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d7d6980c-8dd4-3d1c-abaf-054dfafedc58 | -12.1883 | -46.748798 | 2024-10-03 01:03:33 | METOP-C | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fa18648b-513f-3dba-85c5-6f33d43ba7b9 | -12.1908 | -46.758999 | 2024-10-03 01:03:33 | METOP-C | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b70f4cca-2131-33e7-be6a-4ba4d367d648 | -16.9111 | -57.693901 | 2024-10-03 01:03:34 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 794d06f2-e573-3f6e-bf8c-92b604ce1d07 | -13.1946 | -51.190399 | 2024-10-03 01:03:34 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| adc7b5ba-8210-3bc7-a115-43106bdc4b77 | -13.1962 | -51.197399 | 2024-10-03 01:03:34 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6f16fcd0-9f4d-32e2-be9d-dd2df62f5a00 | -13.188 | -51.206699 | 2024-10-03 01:03:34 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| cedfcb09-0552-3573-b538-c990b5f3de26 | -16.9013 | -57.6959 | 2024-10-03 01:03:35 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 4eea9844-1e1b-3c97-8a68-b273db2a6e47 | -16.8887 | -57.682899 | 2024-10-03 01:03:35 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 1acb55b8-374f-3075-93f1-bf6c4b6e5d4e | -12.4915 | -48.604401 | 2024-10-03 01:03:35 | METOP-C | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 707c3343-8d45-308b-98e6-21aeb6e3751c | -12.4934 | -48.612499 | 2024-10-03 01:03:35 | METOP-C | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 827b6570-5560-3eb1-aa1b-363a45180abd | -13.0856 | -51.164101 | 2024-10-03 01:03:35 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 28b29274-c9d0-383f-a77a-aa81369546e3 | -13.0872 | -51.171101 | 2024-10-03 01:03:35 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c32bff48-9a03-3d4b-a4fe-54f4bf06ec70 | -13.0743 | -51.159302 | 2024-10-03 01:03:35 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b0e8f5ff-7fe7-3eca-875d-bbc773e92c4b | -13.0759 | -51.166401 | 2024-10-03 01:03:35 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0d7eb37a-f9ea-3161-8d4a-891ef9b8752c | -13.0645 | -51.161598 | 2024-10-03 01:03:36 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9fbcc6ae-87ee-372f-8927-fffa5db4b419 | -13.0661 | -51.168701 | 2024-10-03 01:03:36 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 92b4816b-05f8-300a-8bd2-9607c2c598d5 | -13.0531 | -51.156799 | 2024-10-03 01:03:36 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b8c0ce5c-92b8-3ed7-9939-a7b49ac9127e | -13.0385 | -51.1381 | 2024-10-03 01:03:36 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 21539b77-69e6-36b0-9d21-ee41abd72774 | -13.0401 | -51.1451 | 2024-10-03 01:03:36 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f72a5343-b99a-3d39-bbf2-68b36957581a | -13.0417 | -51.1521 | 2024-10-03 01:03:36 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9549cbf9-56ba-3c80-830d-db26c51e5618 | -13.0271 | -51.1334 | 2024-10-03 01:03:36 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| bf47441b-1a48-3a86-b052-91fd34b9149f | -13.0287 | -51.1404 | 2024-10-03 01:03:36 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6c19e800-26ec-338d-930e-0ed471992627 | -13.0028 | -51.117001 | 2024-10-03 01:03:36 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0045592b-5d8c-3e52-8635-7bfb134df0b1 | -13.0043 | -51.124001 | 2024-10-03 01:03:36 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 672d212f-d792-3121-8126-c301689c2ecd | -13.0059 | -51.131001 | 2024-10-03 01:03:36 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 65b5cb3d-36c0-3fed-bad8-0ca79be56851 | -15.0538 | -49.487801 | 2024-10-03 01:03:37 | METOP-C | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 0257de5f-6195-3ff3-a4ae-e5decac5f68b | -15.6777 | -52.5079 | 2024-10-03 01:03:37 | METOP-C | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 74d8d7d3-1e68-36f8-b04c-45be736f6d90 | -12.9945 | -51.126202 | 2024-10-03 01:03:37 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a4c39c8b-2e9c-3832-972b-81ea89f772a5 | -12.9961 | -51.133202 | 2024-10-03 01:03:37 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a227e927-c3a6-3cb4-bce3-f68f01332f48 | -14.7887 | -48.793098 | 2024-10-03 01:03:38 | METOP-C | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 801f0712-724a-3456-b2dc-f47f595a4f84 | -14.7905 | -48.8008 | 2024-10-03 01:03:38 | METOP-C | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 14c645a4-7830-366c-b408-73a31c752798 | -14.779 | -48.795502 | 2024-10-03 01:03:38 | METOP-C | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| d5d04f57-51fa-304e-82d6-5303a2caeaf0 | -14.7808 | -48.8032 | 2024-10-03 01:03:38 | METOP-C | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 7aebe8b3-8cae-3125-81fc-48bfeb8a0f0c | -15.6679 | -52.510101 | 2024-10-03 01:03:38 | METOP-C | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 3b94b6d4-6ec6-36a0-8cb1-734b4d5f1216 | -14.1881 | -46.4659 | 2024-10-03 01:03:39 | METOP-C | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| aa3f9b94-db44-3202-999d-c63a76fc2af3 | -16.5954 | -58.218201 | 2024-10-03 01:03:41 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 0e4914c9-fcac-3a47-883f-b4a57703ba89 | -16.5856 | -58.2201 | 2024-10-03 01:03:41 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f6bc1a6a-a9fe-3383-99b9-41699f98bfe0 | -16.5886 | -58.236 | 2024-10-03 01:03:41 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f5d2851b-fc8a-3a1f-8405-8d1eff6ba0ec | -13.3057 | -43.708698 | 2024-10-03 01:03:42 | METOP-C | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c2794ede-c23e-3059-be69-086f80d794c9 | -13.3097 | -43.723999 | 2024-10-03 01:03:42 | METOP-C | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 28b55534-e2e0-36b2-a291-3c662a27ee13 | -13.296 | -43.7113 | 2024-10-03 01:03:42 | METOP-C | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 526a561e-2dea-3916-93c9-480acbf91788 | -16.573 | -58.2061 | 2024-10-03 01:03:42 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| fe964298-4cee-3f9a-9a97-fe07fb083a56 | -16.575899 | -58.222 | 2024-10-03 01:03:42 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 8db6fd13-0c04-3aa0-854f-a8704e778a61 | -16.578899 | -58.237999 | 2024-10-03 01:03:42 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 5f368dcc-88ee-3e1f-bf4d-b3e3dd291543 | -16.5602 | -58.1922 | 2024-10-03 01:03:42 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 9563709f-624e-3ce3-bf95-7c711bd99730 | -16.5632 | -58.208 | 2024-10-03 01:03:42 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 9c85c4c1-a695-30a0-aaee-ffa792bb7ce2 | -16.566099 | -58.2239 | 2024-10-03 01:03:42 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b55eaa8d-032d-3c7d-a947-c8d38fbd8e21 | -16.550501 | -58.194099 | 2024-10-03 01:03:42 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b535775d-3e1a-31e9-9d66-d882eb679ae9 | -16.553499 | -58.2099 | 2024-10-03 01:03:42 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 6a1e2be9-d487-3382-b5d4-2070d376f662 | -16.5564 | -58.2258 | 2024-10-03 01:03:42 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 749a298c-b045-338b-b217-ad269bc9e084 | -12.7246 | -51.984901 | 2024-10-03 01:03:44 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7208eeaf-da40-38c4-99e4-3060918de1c6 | -11.6786 | -47.713299 | 2024-10-03 01:03:45 | METOP-C | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e8732326-986f-3111-831d-e996baa1a13a | -13.6496 | -56.592999 | 2024-10-03 01:03:45 | METOP-C | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 284d2caa-4057-3b31-9b1c-d7b31dfdf66d | -11.6959 | -47.699402 | 2024-10-03 01:03:45 | METOP-C | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5172687c-2a98-3654-a631-cf93bfba1140 | -11.6981 | -47.7085 | 2024-10-03 01:03:45 | METOP-C | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| adc018b5-364d-36cb-b10e-aeb7440f6739 | -11.6862 | -47.701801 | 2024-10-03 01:03:45 | METOP-C | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 51c473c2-ccca-3b9d-82b3-a6c5410ec59c | -11.6884 | -47.710899 | 2024-10-03 01:03:45 | METOP-C | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c882eb4c-0943-3ae9-ae80-1ef12adec255 | -11.6764 | -47.704201 | 2024-10-03 01:03:45 | METOP-C | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 68a60fc9-90a1-3ae8-bc30-f36e085d48a0 | -12.1806 | -50.0518 | 2024-10-03 01:03:46 | METOP-C | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7fed0d6e-98f9-3bd7-90e7-f0f3e901338f | -12.4019 | -51.013199 | 2024-10-03 01:03:46 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 3a761d7e-3708-3560-b25f-d870957d6c0b | -12.1709 | -50.0541 | 2024-10-03 01:03:46 | METOP-C | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d12307ca-8011-39be-a054-453a2cc44558 | -12.1726 | -50.061401 | 2024-10-03 01:03:46 | METOP-C | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 182dc62f-1178-3d73-aba4-e7ae4cc3ffb4 | -12.1743 | -50.068699 | 2024-10-03 01:03:46 | METOP-C | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6598d88d-5b46-306f-8e2c-7a9f6028c42b | -12.3841 | -50.980499 | 2024-10-03 01:03:46 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c390656f-7ce9-3413-9ece-74c3143203f2 | -12.3905 | -51.008499 | 2024-10-03 01:03:46 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README27.md)
