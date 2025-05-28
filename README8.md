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
| 1f823514-65bd-3dcd-9ca7-ed90c1b42936 | -7.96791 | -45.93327 | 2025-05-28 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7525afb9-2a2c-3d0a-8ac0-3bb98f28f833 | -11.40357 | -44.8305 | 2025-05-28 04:10:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ddaff9ea-3c69-3d74-b6f4-4d63c55fff60 | -12.82515 | -47.39244 | 2025-05-28 04:10:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 88f072c0-cb6b-3eb1-a24f-0b1b397905e5 | -9.04024 | -47.74526 | 2025-05-28 04:10:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 17f11591-b83e-3fb9-aaaf-5161016d349f | -11.82227 | -44.27567 | 2025-05-28 04:10:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 839e29f2-a3b9-3c9a-8899-18d9edc298e2 | -7.68479 | -46.09872 | 2025-05-28 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 18f7017a-4705-3857-9a73-1f6d5a89a4d9 | -13.09294 | -45.27814 | 2025-05-28 04:10:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| db9fe473-b950-3407-8c66-b15b7f9ec4ec | -12.41023 | -49.99611 | 2025-05-28 04:10:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 49cef29e-06a8-3ac0-8b71-e4f144f97b88 | -10.46867 | -47.94379 | 2025-05-28 04:10:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 055279f9-6435-3b2c-9c88-ed4f014703ff | -8.72887 | -47.99182 | 2025-05-28 04:10:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 00dfa500-3f4c-3a61-8965-7e3da7fedb83 | -12.60358 | -46.7337 | 2025-05-28 04:10:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b954efa6-b5db-3ebd-964a-4fc56b71d5d4 | -10.65864 | -49.44693 | 2025-05-28 04:10:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9f01ef35-dee4-3bc9-95e7-6197af550ebe | -15.51699 | -41.96944 | 2025-05-28 04:10:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 93e39f56-90a8-36c1-9378-0619de258a49 | -7.62953 | -45.76032 | 2025-05-28 04:10:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 3e1db9a4-66d5-3d70-94f3-c525092fb0a2 | -10.65418 | -44.49628 | 2025-05-28 04:10:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 29adb58b-7c9e-3d45-832a-81862c20e37a | -10.66152 | -44.40856 | 2025-05-28 04:10:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6605521c-b46c-3b1b-b5b0-cb8da220d5b9 | -7.62197 | -45.75914 | 2025-05-28 04:10:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 90d75b51-8983-3531-8b43-3dd328af4b0c | -11.768 | -47.26355 | 2025-05-28 04:10:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 105ad3c6-945e-31a4-8b9f-aad7d2fee232 | -7.67244 | -46.10154 | 2025-05-28 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 14.8 |
| e1c89fe6-c27a-327d-b50f-43f7e58453db | -10.22583 | -47.42977 | 2025-05-28 04:10:00 | NPP-375D | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| eb0fc24f-8036-3964-bd07-6d47541d8240 | -11.81429 | -44.28189 | 2025-05-28 04:10:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a95936c0-3605-3825-9ac2-f8b34496bcc2 | -7.46989 | -47.05981 | 2025-05-28 04:10:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c20f777d-ea6d-39b9-8d25-92915ca163d9 | -10.45491 | -47.94918 | 2025-05-28 04:10:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| bff7cd15-166c-36fc-8df3-6ce57494ed70 | -8.87995 | -49.04444 | 2025-05-28 04:10:00 | NPP-375D | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7f03c59b-9214-36ab-ab4e-26470c69ab90 | -14.61825 | -47.94569 | 2025-05-28 04:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e0d5a9a5-48b2-3563-9474-0e0f90dbc80e | -8.14439 | -46.48785 | 2025-05-28 04:10:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 05c01123-d26f-368a-823f-f712ab9e921c | -8.01441 | -49.68951 | 2025-05-28 04:10:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bb676e59-70bb-30c7-a6ac-160427721304 | -12.61027 | -46.73951 | 2025-05-28 04:10:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 517897ac-cb22-371a-a881-3376d93354d2 | -11.81828 | -44.27878 | 2025-05-28 04:10:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 0d60ff2d-2764-35a3-8ffa-c59c60bf130e | -7.6694 | -46.09611 | 2025-05-28 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 14.8 |
| a8fa4c9e-494f-3b0b-adf3-e10aa9c721fa | -9.02901 | -47.73549 | 2025-05-28 04:10:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1f231aca-5d66-371f-9c33-b1f5456189c9 | -11.82346 | -44.26831 | 2025-05-28 04:10:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 42561893-b087-3a3e-b4fe-dfce2950c261 | -11.814 | -46.14273 | 2025-05-28 04:10:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f5f04fe7-cd3e-3625-816b-f609785a815a | -7.68174 | -46.09329 | 2025-05-28 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 298459bf-afbe-3e1b-a620-30450231ca5a | -8.02054 | -43.18502 | 2025-05-28 04:10:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| d7df06dc-e206-37bd-902d-82e6bff5c4ed | -8.7785 | -47.95918 | 2025-05-28 04:10:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1c741e17-c720-3cb0-bb9f-032bbbd6686d | -7.68559 | -46.09393 | 2025-05-28 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| aebddd48-8554-340d-aa9d-99355b926568 | -8.72959 | -47.98777 | 2025-05-28 04:10:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b54b7506-a0c8-3dc9-a544-aaeb1f224b50 | -11.56993 | -47.62202 | 2025-05-28 04:10:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4e22e7aa-3de5-3126-a25f-a8e7fdf52ace | -12.82382 | -47.39534 | 2025-05-28 04:10:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d21cbb0a-ac7d-3135-aa49-97dc52104c30 | -10.24381 | -52.23021 | 2025-05-28 04:10:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 02da389f-25a4-3a65-8017-5d8ce3f88456 | -13.08255 | -45.27635 | 2025-05-28 04:10:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5e5ca57e-4f09-3e5d-a12e-0282226ca6ef | -9.03319 | -47.73622 | 2025-05-28 04:10:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 97614742-2e7a-35b9-bc9b-b854f086ccfb | -11.577 | -47.62866 | 2025-05-28 04:10:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| daa82f76-c05d-3644-ae2c-d164fb8d7913 | -11.56594 | -47.62134 | 2025-05-28 04:10:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1e1d9571-c2f3-33ad-aff2-80c08bd4e1f1 | -13.07908 | -45.27575 | 2025-05-28 04:10:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f4254176-56c2-38c4-8f2e-bce434e614a5 | -7.67164 | -46.10632 | 2025-05-28 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 6a43b240-cfbe-3d8a-9ab1-5b9ea4eaeeb1 | -7.97546 | -50.71143 | 2025-05-28 04:10:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1f7728e6-222c-3a05-912c-b84430f0c7e7 | -12.27453 | -44.60821 | 2025-05-28 04:10:00 | NPP-375D | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 563d2181-4e24-3780-99c1-eb502c901813 | -11.56903 | -47.62724 | 2025-05-28 04:10:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e276297f-9644-3858-8658-a64c496985b2 | -10.65409 | -49.44608 | 2025-05-28 04:10:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bcaa3be1-ba03-313a-9d4b-edc552ed7e9c | -10.98272 | -44.62452 | 2025-05-28 04:10:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6c60c47a-bc99-3594-9130-e2c8abe7730a | -12.25329 | -53.27872 | 2025-05-28 04:10:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9edc9150-2c7b-3b73-8877-cbb04b5a9fa2 | -11.97715 | -52.47056 | 2025-05-28 04:10:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 30e55388-ee70-356e-97fe-c2f6f3dc04a6 | -7.6686 | -46.10086 | 2025-05-28 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 5a9d88b2-c2c9-3f01-8016-a81020933ab0 | -11.29936 | -54.01751 | 2025-05-28 04:10:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 903db184-4680-3e8a-b38f-cd2e9db16f24 | -14.68663 | -45.09199 | 2025-05-28 04:10:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cb235aef-aa08-35cb-b805-12eadca8e777 | -13.07713 | -45.28735 | 2025-05-28 04:10:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a63e7d76-8089-35d0-b908-78fd6a23aff8 | -11.10826 | -44.62931 | 2025-05-28 04:10:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f0b32332-0176-3aa1-a083-6b67790ff278 | -12.26894 | -44.59954 | 2025-05-28 04:10:00 | NPP-375D | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 57e6ad6d-0933-3948-9866-b522c13ec5ec | -9.84845 | -48.14784 | 2025-05-28 04:10:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3cbfa5f6-1eee-37c1-9490-e074ba9071fb | -10.45558 | -47.94541 | 2025-05-28 04:10:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| a0dce1fb-4ad7-36f9-b995-66dea8923f1f | -10.66774 | -49.44868 | 2025-05-28 04:10:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 069d5994-8fab-3044-b715-878c9c225c19 | -10.52796 | -47.58499 | 2025-05-28 04:10:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e2d7160f-61ba-35ea-9108-2c4161cf7101 | -12.11033 | -54.67199 | 2025-05-28 04:10:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4bad20f1-d357-3ec4-80ed-6b3f54259145 | -9.03959 | -47.74906 | 2025-05-28 04:10:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 136af9b4-078e-39ac-b28b-9691cb0ffd0c | -11.30446 | -54.02353 | 2025-05-28 04:10:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3ea4e253-3b49-3877-8e1c-e2709756213c | -11.91341 | -54.41402 | 2025-05-28 04:10:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 85b28ec7-07b8-380b-8d4d-4517664c8296 | -11.82625 | -44.27256 | 2025-05-28 04:10:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d763047e-a622-3d65-8bc4-017f16d0ddee | -7.6702 | -46.09138 | 2025-05-28 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dcc974d7-f099-3ce8-bcde-61d03c4e88f7 | -14.68602 | -45.09571 | 2025-05-28 04:10:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a411713d-e0c2-3181-9660-d9abfa080ebd | -8.17004 | -43.4015 | 2025-05-28 04:10:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 21f06d6a-bd99-3070-9adc-9df05c6daff0 | -10.72246 | -45.04384 | 2025-05-28 04:10:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2dfe3a38-2f58-34da-9c3b-abd17d800d60 | -9.19607 | -49.47397 | 2025-05-28 04:10:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| dad75895-70e3-33e3-aeac-bc198291e392 | -11.14206 | -53.91866 | 2025-05-28 04:10:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c65d3bd3-fe21-3836-b3a8-f8f344d09e1e | -12.45989 | -44.28612 | 2025-05-28 04:10:00 | NPP-375D | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fd6b7c38-59fd-35d1-ab12-0136c31eda86 | -12.10837 | -54.66692 | 2025-05-28 04:10:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5590a595-8268-3c0a-a238-3834cd45329c | -7.97603 | -50.70825 | 2025-05-28 04:10:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8aa84087-43b2-3d5a-9ec2-11099bccda02 | -7.62652 | -45.75514 | 2025-05-28 04:10:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 4b76c601-a790-3c16-ab72-7e0a6dbaba2c | -10.4728 | -47.94454 | 2025-05-28 04:10:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 98660b8a-b83e-36cb-9e91-c3536b961271 | -9.18301 | -40.31263 | 2025-05-28 04:10:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 7.0 |
| bb31591e-b1a2-3dc2-ac7b-00f5056bafa7 | -10.23831 | -52.2291 | 2025-05-28 04:10:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 17fe6091-1300-3920-9007-3141e21e077f | -7.68094 | -46.09807 | 2025-05-28 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 25.8 |
| 89ae04ae-38f9-35cc-95c2-047d65d67083 | -8.82142 | -49.84261 | 2025-05-28 04:10:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d03746b9-0f07-35b1-9468-5aed2942f618 | -10.72172 | -44.08309 | 2025-05-28 04:10:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9ac065bb-e3b2-32c5-9a28-6a5f720d08d2 | -12.11131 | -54.66705 | 2025-05-28 04:10:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d91601a1-0e6c-3940-aa5a-ccc4cd012f57 | -8.1483 | -46.48852 | 2025-05-28 04:10:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8a3d60ce-88e7-3ae6-82d3-450ab2ff7d72 | -11.77361 | -47.3227 | 2025-05-28 04:10:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 44848c52-dc0e-300f-bb24-90ed691d84f7 | -12.28721 | -43.54409 | 2025-05-28 04:10:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| dc0b2040-fc37-3e78-8802-09f7cb42aaa2 | -13.08666 | -45.27308 | 2025-05-28 04:10:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0e2a9c2e-2f29-37f9-b317-d3b827ac04d4 | -10.23762 | -52.23269 | 2025-05-28 04:10:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 3d9d06c5-057a-3f2a-adaf-251dad46254b | -11.03344 | -44.20618 | 2025-05-28 04:10:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 03017833-c868-3676-b849-b8509b831c79 | -9.03893 | -47.75286 | 2025-05-28 04:10:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2321ce75-bb92-3d77-9018-4436f13a0635 | -9.19967 | -49.47313 | 2025-05-28 04:10:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| ee58eabe-d8b0-382a-9494-33ed0bf7cb43 | -8.01926 | -49.69035 | 2025-05-28 04:10:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b69e162e-0a0a-33d6-b3d0-009b84ac1137 | -11.82007 | -44.26774 | 2025-05-28 04:10:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 2e084690-6ec4-3c64-8a13-835c89a715d4 | -12.26955 | -44.59581 | 2025-05-28 04:10:00 | NPP-375D | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9b61cb41-0fdb-32ae-a4ac-6b3a1cec955d | -12.60791 | -46.73691 | 2025-05-28 04:10:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8356728a-ca44-3a7b-b2f7-a49412e60f16 | -7.46823 | -47.05862 | 2025-05-28 04:10:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 71887cce-cc9b-3891-9a9e-5854b54b2c60 | -7.68014 | -46.10286 | 2025-05-28 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 25.8 |


[Clique aqui para ver as próximas entradas](README9.md)
