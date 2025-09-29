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

## Dados Diários - Página 85

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6aa9702d-2d10-3087-b645-6eeeabef5dba | -12.65317 | -46.91722 | 2025-09-29 12:19:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 23814a9b-4868-3fbd-a6c3-77f482410984 | -16.55754 | -45.31127 | 2025-09-29 12:19:00 | TERRA_M-T | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 23.3 |
| c53478ef-123b-3821-a876-78be89f1641d | -10.84461 | -47.77755 | 2025-09-29 12:19:00 | TERRA_M-T | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 518b8923-3e69-3651-868d-017578b514a4 | -11.94231 | -47.9007 | 2025-09-29 12:19:00 | TERRA_M-T | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 7f64768f-35fd-3d12-87ff-8719f838ac99 | -13.22288 | -50.97336 | 2025-09-29 12:19:00 | TERRA_M-T | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 35.4 |
| e8e56d78-3680-38ca-a7e2-d2e336e12a3f | -10.81245 | -46.64344 | 2025-09-29 12:19:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 11.8 |
| f2e36590-fbf7-37a6-b4b1-d1b1eb26ac0e | -15.23181 | -46.20051 | 2025-09-29 12:19:00 | TERRA_M-T | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 21.8 |
| cd4c1778-1a11-3fc6-8197-77d18974b2c2 | -20.0553 | -41.34015 | 2025-09-29 12:19:00 | TERRA_M-T | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 33.7 |
| 1e59a504-56c7-364c-8e9d-2fb45ac08c11 | -14.5725 | -48.27626 | 2025-09-29 12:19:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 3095a0b2-4f41-3846-8a54-ba2ca16d0ecf | -12.93969 | -46.7734 | 2025-09-29 12:19:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 560c99d8-2fb2-3998-87fb-4d7bceefacd9 | -13.01056 | -49.43579 | 2025-09-29 12:19:00 | TERRA_M-T | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 27.5 |
| 4e14aea3-598b-36e3-b3d6-9bba5302cec8 | -11.80132 | -48.24025 | 2025-09-29 12:19:00 | TERRA_M-T | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| e3c2b32c-831c-3e1b-8d88-b7733c478ff1 | -13.43423 | -45.89772 | 2025-09-29 12:19:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 0883fd75-c171-3b83-91d1-2c291413fde4 | -13.72411 | -48.6595 | 2025-09-29 12:19:00 | TERRA_M-T | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 40b11475-eedf-35a3-88df-f593398d520f | -12.94879 | -46.7746 | 2025-09-29 12:19:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 53.3 |
| 810b8649-8649-339a-9650-dd38d073a30e | -15.52221 | -47.93584 | 2025-09-29 12:19:00 | TERRA_M-T | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 6.4 |
| ca29b808-19e7-32b3-9af6-f8ecbc722510 | -11.66876 | -45.35034 | 2025-09-29 12:19:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 9308d451-32ff-3454-9942-a2b1aed58493 | -13.79743 | -47.89344 | 2025-09-29 12:19:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 8c4e87a9-5e07-3930-bd0f-b7c153e790da | -18.32076 | -44.23234 | 2025-09-29 12:19:00 | TERRA_M-T | SANTO HIPÓLITO | MINAS GERAIS | Brasil | 3160603 | 31 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 7f8b7486-4263-3aed-bfde-e13f254b82c2 | -10.81883 | -46.66328 | 2025-09-29 12:19:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 40.5 |
| b94af495-5b79-3d16-8ef9-e4150051fc59 | -12.93218 | -46.766 | 2025-09-29 12:19:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 23.3 |
| 0f0d6781-48c1-3d80-88a8-342393094895 | -11.36576 | -45.08643 | 2025-09-29 12:19:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 5872ea8a-51a6-3f3c-b31a-34624e09ca4e | -15.52351 | -47.92655 | 2025-09-29 12:19:00 | TERRA_M-T | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 33.3 |
| 455df478-13ed-3aab-802b-e00246a0e0a9 | -18.08586 | -45.79787 | 2025-09-29 12:19:00 | TERRA_M-T | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 10.1 |
| e5867170-95d8-381f-9fea-92bd653e2d40 | -11.92298 | -48.03533 | 2025-09-29 12:19:00 | TERRA_M-T | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 61b37cf4-d907-3b8d-b039-92f14f4e6f98 | -13.01908 | -49.44308 | 2025-09-29 12:19:00 | TERRA_M-T | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| c2899cdc-1c2a-3ed1-98b1-ea3beac790f0 | -9.72751 | -47.78835 | 2025-09-29 12:19:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 4271c6cc-dd9e-35b9-b21e-f8dabb5bbe5a | -11.45199 | -44.97906 | 2025-09-29 12:19:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 57c5c7ac-a958-3104-82a2-a689b7805700 | -18.1276 | -45.71418 | 2025-09-29 12:19:00 | TERRA_M-T | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 90358c11-6d1f-309d-a0ae-6f5c8b704d9e | -12.26899 | -47.75228 | 2025-09-29 12:19:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 0b798c09-048b-315c-8e2c-78b33caaa797 | -11.57873 | -45.483 | 2025-09-29 12:19:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 9.4 |
| f457adbb-c67b-39d0-894f-465447fdac04 | -9.79318 | -46.95031 | 2025-09-29 12:19:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| ae3396d6-8cec-378f-bdbf-443c0965fe4c | -15.2304 | -46.21135 | 2025-09-29 12:19:00 | TERRA_M-T | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 0ea270a2-61a9-33bc-a6c8-ec9ede9aaa6e | -11.90801 | -44.84379 | 2025-09-29 12:19:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 47.4 |
| be838375-4a9a-33ff-b1d6-bba92b6a39cf | -12.85147 | -46.88118 | 2025-09-29 12:19:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 5cf5e01f-2260-30bd-8c55-50c94fbae26d | -12.95009 | -46.76511 | 2025-09-29 12:19:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 24.6 |
| bddd9fa4-99eb-35f9-a783-f029f788cf44 | -14.58024 | -48.22155 | 2025-09-29 12:19:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 06d11d00-f7be-3fa1-966d-13325633647b | -14.5642 | -48.25927 | 2025-09-29 12:19:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 21.0 |
| 4fed39e0-3234-3707-aed1-2fadd16cd80d | -15.5552 | -41.47271 | 2025-09-29 12:19:00 | TERRA_M-T | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 42.0 |
| 631ad4cc-5bfa-3d69-a9e2-db92023e3db6 | -11.90768 | -44.85022 | 2025-09-29 12:19:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 60.2 |
| f8da0a58-fae7-3aba-b3d5-e382da92ceb4 | -13.18797 | -50.7233 | 2025-09-29 12:19:00 | TERRA_M-T | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 38.8 |
| 58582e59-f95e-38c8-a6a9-441f344adefb | -15.25719 | -48.77106 | 2025-09-29 12:19:00 | TERRA_M-T | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 16.7 |
| d4b1bc39-faf3-3bc8-bb05-6f6233885c83 | -14.71609 | -45.21044 | 2025-09-29 12:19:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 25.7 |
| 36ab1b3d-1f04-3ce3-9e49-cc6be3fb208a | -12.65186 | -46.92669 | 2025-09-29 12:19:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 85e3cd18-3eb8-33b6-9e9b-06308cd2b2e1 | -17.14023 | -48.28387 | 2025-09-29 12:19:00 | TERRA_M-T | ORIZONA | GOIÁS | Brasil | 5215306 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| db5d51b4-d5a5-3c29-a4fc-83a0cae16fbc | -12.36899 | -47.17192 | 2025-09-29 12:19:00 | TERRA_M-T | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 38.5 |
| a46f8280-675a-362c-be48-acb25c3ed339 | -9.7124 | -47.76799 | 2025-09-29 12:19:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 52ef331f-d3a4-33b0-acf8-f85b73f2b02c | -12.28929 | -44.0958 | 2025-09-29 12:19:00 | TERRA_M-T | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 110.7 |
| 42bac7e0-f414-3b0d-9bc0-08e41447d694 | -14.70739 | -45.2037 | 2025-09-29 12:19:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 45.9 |
| 12b57b02-0522-3b2c-a43a-fcb6f0fdca91 | -12.78524 | -46.89433 | 2025-09-29 12:19:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 1d039bac-0a34-3637-b685-56a736426b37 | -10.80571 | -45.36552 | 2025-09-29 12:19:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 48.7 |
| d3a75fa1-9bcb-310c-8e47-13a4ef187020 | -10.38406 | -49.04346 | 2025-09-29 12:19:00 | TERRA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 29.3 |
| 72f69f96-7814-324c-bdb6-88a27ca0bf6e | -9.93948 | -48.80433 | 2025-09-29 12:19:00 | TERRA_M-T | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| cd096e76-e773-3a67-a147-be6e102f3d07 | -10.54922 | -49.54496 | 2025-09-29 12:19:00 | TERRA_M-T | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 1f1e6ea9-49b5-3f3f-871b-d855cdddc44d | -11.43428 | -44.94761 | 2025-09-29 12:19:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 063277cc-968e-35fc-ba8a-2b2538042a54 | -15.89866 | -48.14544 | 2025-09-29 12:19:00 | TERRA_M-T | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 6.5 |
| b656be50-7423-3b68-bdcf-81fa0f900880 | -15.89737 | -48.1547 | 2025-09-29 12:19:00 | TERRA_M-T | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 7.4 |
| a7534346-da6c-36f6-a2df-5883cb5d0b45 | -10.31369 | -48.19923 | 2025-09-29 12:19:00 | TERRA_M-T | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| e0af94a3-e3c7-3097-ac52-24cd497f86ec | -9.7803 | -46.18753 | 2025-09-29 12:19:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 60.1 |
| cae99de6-a185-3bc8-a50c-5b740379bc46 | -10.63337 | -48.53796 | 2025-09-29 12:19:00 | TERRA_M-T | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 55.6 |
| 3af38e90-fdf3-3419-8456-2dae55421a0b | -12.00927 | -47.43178 | 2025-09-29 12:19:00 | TERRA_M-T | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 59a9cfe9-79d9-3ce2-93c5-a697244492b1 | -13.23411 | -50.96414 | 2025-09-29 12:19:00 | TERRA_M-T | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 285.9 |
| b85d15f2-44fd-3f8d-98b4-3cdc73bb1d9d | -14.89041 | -51.0583 | 2025-09-29 12:19:00 | TERRA_M-T | ARUANÃ | GOIÁS | Brasil | 5202502 | 52 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 32c5e55d-5f51-3e3b-9f25-959d5dcabcc5 | -9.77767 | -46.20626 | 2025-09-29 12:19:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 3f9af112-cb1d-34cc-ae4a-a408a0575540 | -15.4322 | -48.25287 | 2025-09-29 12:19:00 | TERRA_M-T | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 10.1 |
| a099ce2b-aab1-3873-96aa-baed2ae79726 | -13.25862 | -48.44004 | 2025-09-29 12:19:00 | TERRA_M-T | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| d06b93b3-9ae4-31d5-b3db-d95b4c920658 | -11.35602 | -45.08509 | 2025-09-29 12:19:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 93590070-4eba-32f9-aa2a-72a342583cbb | -10.63053 | -49.06073 | 2025-09-29 12:19:00 | TERRA_M-T | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| c48271fe-4db7-3a0c-8e2a-055270ecb3b2 | -15.38313 | -41.12275 | 2025-09-29 12:19:00 | TERRA_M-T | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 21.6 |
| 838b086f-a9f9-3f5c-97e4-488b04d60738 | -13.35451 | -47.30435 | 2025-09-29 12:19:00 | TERRA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| b2cf485f-5c83-3767-9c32-9599f39761f4 | -14.60818 | -45.02323 | 2025-09-29 12:19:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 16.9 |
| e64a31e8-a0b0-3d68-91be-3750b2e488c2 | -15.38571 | -41.09833 | 2025-09-29 12:19:00 | TERRA_M-T | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 43.0 |
| be5e885c-93c9-392e-b055-af0153d5578b | -9.75775 | -47.7805 | 2025-09-29 12:19:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 3d38f2bc-9a91-3f69-8f0d-d32e6c927fed | -9.8916 | -45.91794 | 2025-09-29 12:19:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 1173d400-b7f1-3f22-9a54-ce4140f4c1ec | -11.93458 | -47.95457 | 2025-09-29 12:19:00 | TERRA_M-T | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| fc4be467-7519-31f2-941a-53b747734bee | -10.63468 | -48.52893 | 2025-09-29 12:19:00 | TERRA_M-T | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 8a0f31fb-f7c2-3df9-9164-e41dcfecac3b | -11.91414 | -48.03405 | 2025-09-29 12:19:00 | TERRA_M-T | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 54.2 |
| 30c9e7f3-f495-39e9-85f1-b9521d7aa035 | -13.1785 | -50.72182 | 2025-09-29 12:19:00 | TERRA_M-T | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 213.6 |
| 223e9ef1-fc67-3b6d-8e15-2b7dc79d65ed | -12.28764 | -44.10894 | 2025-09-29 12:19:00 | TERRA_M-T | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 44.3 |
| 3be19a94-a272-3669-bfa7-47ba1dce34ac | -12.00229 | -46.63176 | 2025-09-29 12:19:00 | TERRA_M-T | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 04b11a72-d131-3822-adf9-82a9893fdbf2 | -18.12643 | -45.70701 | 2025-09-29 12:19:00 | TERRA_M-T | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 42263264-ce85-3af0-83df-733868f05f3d | -15.26734 | -48.76328 | 2025-09-29 12:19:00 | TERRA_M-T | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 27.8 |
| 8c191147-153f-394d-abd0-f3770b28c9dc | -11.71726 | -44.43187 | 2025-09-29 12:19:00 | TERRA_M-T | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 24.6 |
| 8a685876-1a22-3778-94c4-02bd8ec418c5 | -9.99081 | -45.40876 | 2025-09-29 12:19:00 | TERRA_M-T | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| ee68c63c-ab5e-3c7a-8a84-b5f220b39efa | -11.30859 | -43.79123 | 2025-09-29 12:19:00 | TERRA_M-T | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 6042e468-2f01-34bc-941b-e6414591ca47 | -14.90693 | -41.32974 | 2025-09-29 12:19:00 | TERRA_M-T | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Caatinga | 27.3 |
| ab666fe6-a2a1-3143-8bf8-502c5b7f08f8 | -10.82014 | -46.654 | 2025-09-29 12:19:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 41.7 |
| 682964c7-aad9-3f1e-9da4-000285b0ab65 | -9.76401 | -47.79959 | 2025-09-29 12:19:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 9fcb7654-15b5-3e22-bb73-35f141da2004 | -12.85791 | -46.90132 | 2025-09-29 12:19:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| d1443501-cde7-3b99-a407-58484dbc69df | -15.54909 | -47.87967 | 2025-09-29 12:19:00 | TERRA_M-T | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 00a4e3b6-dc10-32e9-97b8-8a01b25f1f7d | -13.04575 | -47.07394 | 2025-09-29 12:19:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 3601cf84-26a9-3a43-a2cc-52b61b66782d | -18.21227 | -53.29765 | 2025-09-29 12:19:00 | TERRA_M-T | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 459aa204-b7cc-3546-883a-d9d57d95589e | -12.75427 | -46.85122 | 2025-09-29 12:19:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 7d45da0a-3ee2-3dec-9e28-181517d31232 | -10.81115 | -46.65272 | 2025-09-29 12:19:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 18.3 |
| f354c76a-b13b-38ac-a668-ce4044aafb67 | -14.59638 | -45.0342 | 2025-09-29 12:19:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 0aa81c12-ab56-3215-a464-39d5a13e5268 | -14.53822 | -48.44109 | 2025-09-29 12:19:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 24.4 |
| ad95f989-2d82-3d9d-822f-bdfa1db81801 | -11.26947 | -47.19375 | 2025-09-29 12:19:00 | TERRA_M-T | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 17.6 |
| be347358-25a7-316b-95e7-d792dc120671 | -11.41907 | -44.91189 | 2025-09-29 12:19:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 21.3 |
| 2580856e-1d39-399c-8858-d6ac7f99b198 | -12.70223 | -46.89561 | 2025-09-29 12:19:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 8df3fbed-ed20-3f6c-bdfa-0486aedc2f63 | -11.84399 | -51.79587 | 2025-09-29 12:19:00 | TERRA_M-T | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 20.0 |


[Clique aqui para ver as próximas entradas](README86.md)
