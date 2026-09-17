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

## Dados Diários - Página 53

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 87c9a7e5-678b-34b0-918c-0d36b8a40e4c | -12.37451 | -48.45828 | 2026-09-17 04:42:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 94e52507-1803-3baa-8603-cfb8aeac2888 | -13.20409 | -51.61813 | 2026-09-17 04:42:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3e0b0166-3414-3566-8f24-c1bbc027f979 | -14.18582 | -45.14025 | 2026-09-17 04:42:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7c0cc3da-15ed-333f-96fa-3b6146db5ed5 | -12.48063 | -50.76349 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 460de52f-6438-30b2-80ad-f3b81e536068 | -16.14334 | -43.5523 | 2026-09-17 04:42:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a815be9e-ab22-334e-b077-670d286952e0 | -12.47071 | -50.7619 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7bfd922d-ff3a-33af-be89-2ef8430a02e5 | -14.17983 | -45.15266 | 2026-09-17 04:42:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5cfd29b9-572f-3fbf-99d9-0199cfd11b1f | -15.8414 | -56.19792 | 2026-09-17 04:42:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| f5d45bda-d83a-3088-b1ff-665c2a0a45eb | -12.45925 | -50.8574 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 2959e283-1b7e-336d-a595-3ea65c01789b | -12.48613 | -50.81823 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0fb3513e-9615-3d9d-a2ef-e68ec84ac0b7 | -12.43245 | -48.48684 | 2026-09-17 04:42:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e6ad9be6-59bc-35e0-8dc2-c0cc23a0257e | -12.47514 | -50.77703 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 9e521f45-c590-381c-b45f-458e54d2a0aa | -12.46246 | -50.77139 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1ea69a04-f5f4-3428-9e03-aef1483148cf | -13.43285 | -43.81377 | 2026-09-17 04:42:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 12.9 |
| d94de5c7-62dc-3801-a620-9764899fbeb2 | -12.40012 | -48.47837 | 2026-09-17 04:42:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 21d50e39-0fc6-3d86-bc36-5d2203439551 | -14.55842 | -46.60564 | 2026-09-17 04:42:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 5d9de9bd-14a5-3a4d-a1ad-17222f6b9264 | -12.46136 | -50.77842 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ecf75f6c-fdea-37a9-a1c4-b087368200de | -12.45871 | -50.86092 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 5b9338dd-203e-35a8-8ec8-e0c6932753a1 | -12.4878 | -50.76103 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0c10f81f-be37-3376-ac9b-cf373173a537 | -12.44769 | -50.86636 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7fd035de-f8f0-39e7-8a76-772e324d57d1 | -13.60772 | -46.95297 | 2026-09-17 04:42:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| de77ba86-d202-3490-b18a-f238883713a3 | -12.46418 | -50.82576 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5e079554-0bbd-3dee-a4ed-449b7f8d023a | -12.44051 | -50.84718 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 23642bcc-1a17-303c-98f1-42248baff3e6 | -12.41848 | -48.48465 | 2026-09-17 04:42:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 61191f02-22ca-3427-ad3c-3576a6239934 | -12.70814 | -48.28034 | 2026-09-17 04:42:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 12b1e364-fd6c-3d23-b9d5-15d02097b26f | -12.46907 | -50.77245 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 10.6 |
| ab8b6d00-1686-38a3-959e-bbac9518db74 | -12.78044 | -51.28456 | 2026-09-17 04:42:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1f887e2c-584a-353f-9de0-25a35aceee4d | -16.09391 | -45.1334 | 2026-09-17 04:42:00 | NOAA-21 | PINTÓPOLIS | MINAS GERAIS | Brasil | 3150570 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| acabd7a5-4ba8-33d8-85c5-acd16c0ad0d1 | -15.49732 | -53.80604 | 2026-09-17 04:42:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1c871bf0-3a39-3d0b-ac3d-d33c8bb67069 | -12.4785 | -50.82085 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 41041e96-3681-3b0c-bfd8-bfce5b999197 | -12.44652 | -50.8085 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 11e408ac-f299-3059-b55d-4f814cd6c4c1 | -12.46475 | -50.84387 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 40ae6f3b-b3ad-33d5-957c-370bbab17319 | -14.226 | -48.50809 | 2026-09-17 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 89ac2cbb-3a83-35c1-9929-e81c077caef0 | -15.46358 | -53.77708 | 2026-09-17 04:42:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1587f4a7-a7d1-3c77-a4a8-e4a922a93dce | -12.46306 | -50.81115 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6204e47a-c50c-35db-9759-0169dccfb915 | -12.50466 | -50.69852 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 78bc6408-517d-32cd-8824-444b9d07a7fc | -12.95628 | -48.61433 | 2026-09-17 04:42:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 98b5ae6e-4ea9-3ed8-8de6-c272334ca8cc | -12.47569 | -50.77351 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 3f81e1d9-30e1-3299-8197-fb6ca80e9c90 | -12.4559 | -50.81361 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 376fc90f-9866-338a-80a5-12716a9c2e3b | -12.47243 | -50.81627 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 82eef787-6276-33ae-9b74-910256b0fe2e | -13.58364 | -45.47023 | 2026-09-17 04:42:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| eebcd87b-a4c5-36d9-a746-16073e277d5d | -12.4592 | -50.81414 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 19a32323-1560-3d13-825b-73bf26a5fe2b | -12.49376 | -50.76897 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 63066cab-0faa-3c48-a9e7-6ec5da34181f | -11.49749 | -54.46611 | 2026-09-17 04:42:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d6eb65dc-58ec-36b5-b3f2-e9c64c71427d | -14.14793 | -47.3791 | 2026-09-17 04:42:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fa62bf2c-d70d-3973-aa73-8680c24a89fb | -12.46472 | -50.82224 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 140d8968-9ec2-38ae-bc1d-a3210352a390 | -14.56041 | -39.63494 | 2026-09-17 04:42:00 | NOAA-21 | ITAPITANGA | BAHIA | Brasil | 2916609 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 716a6a8c-c359-36ee-8b13-6460dd8b60dd | -12.41149 | -48.48357 | 2026-09-17 04:42:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| a182d6be-01c2-37a2-b207-7f337c4c663d | -11.98324 | -52.46761 | 2026-09-17 04:42:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 85e5d11e-e5ae-3204-8738-61d6acd088c8 | -12.446 | -50.83364 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 9b0e9547-af57-39d7-8fc0-18b85a9ef922 | -12.14176 | -57.18818 | 2026-09-17 04:42:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5dee3a3f-dbe5-3dcb-972e-469343197999 | -14.55413 | -39.63435 | 2026-09-17 04:42:00 | NOAA-21 | ITAPITANGA | BAHIA | Brasil | 2916609 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 726c6a0b-ca46-3000-b98f-84324bed966b | -12.44874 | -50.81607 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 31436d62-6447-3db6-b354-afc2a29a00d4 | -14.56609 | -39.64114 | 2026-09-17 04:42:00 | NOAA-21 | COARACI | BAHIA | Brasil | 2908002 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 87baf905-0e39-39ce-8ff9-27680853f153 | -14.13138 | -48.73827 | 2026-09-17 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 180515c4-761f-3037-ab0c-06dbf47fc520 | -12.47904 | -50.81733 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 01b38f2f-3a32-3a80-8f09-c2a0860c9592 | -12.8072 | -60.48717 | 2026-09-17 04:42:00 | NOAA-21 | CHUPINGUAIA | RONDÔNIA | Brasil | 1100924 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ad98a4ac-5a98-34f4-b9ca-e27949030569 | -10.2823 | -60.53795 | 2026-09-17 04:42:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2cd08c8b-671c-3435-acb9-29a9067fd51c | -12.47407 | -50.80571 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 85a0aef9-3128-364c-a6a7-5e518929d522 | -12.46142 | -50.82171 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 03a905e0-8412-3195-86e7-3607529fe801 | -12.4416 | -50.84015 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 12fd31fb-9225-3e1b-a9d9-45365b6eb847 | -12.45814 | -50.8428 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 6889b02d-990a-3b02-aa12-151ca5f27b58 | -12.4036 | -48.47892 | 2026-09-17 04:42:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a884f73b-8930-398c-b0ed-6c89677957f9 | -12.46415 | -50.80412 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 19eda11d-e073-388c-97f6-304698f55778 | -11.97927 | -52.47073 | 2026-09-17 04:42:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 69906ba7-0947-365c-809c-92e1a7ba84c7 | -14.2332 | -48.63236 | 2026-09-17 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 57536621-6666-3f84-89e6-1a60d5490b3f | -12.45918 | -50.7925 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 056f30db-89bb-3c48-9b19-79bd1e275053 | -12.42895 | -48.48632 | 2026-09-17 04:42:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b2ec7cdf-c1ad-3aa2-b61b-ac5acc4bbdb5 | -12.48561 | -50.7751 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 39dd4553-734e-3db8-bec5-d332142e4b6a | -12.75227 | -52.84246 | 2026-09-17 04:42:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5d9a3e0e-1214-35d5-a8ab-655dd77e63f2 | -14.55912 | -46.60042 | 2026-09-17 04:42:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 8.1 |
| e1458212-7e5b-3abd-b679-0f22df7ce61e | -12.44767 | -50.84473 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bce78c47-767d-3a18-ac66-c8f49cb9bf0a | -12.42254 | -48.48125 | 2026-09-17 04:42:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| fa3d3f85-d406-3937-9627-6b3003d2297a | -13.74774 | -43.75591 | 2026-09-17 04:42:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| eb939ec9-6527-347b-9323-e85ffc31241a | -14.15229 | -47.37543 | 2026-09-17 04:42:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b0f38dc2-46a7-3aad-82f1-863050bdada2 | -12.4823 | -50.77457 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 691aaa6f-f69a-36c5-b1fd-3f159bf6513e | -12.78499 | -47.56449 | 2026-09-17 04:42:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 977b9e71-443e-36b1-a4db-6f37684b8b6e | -11.98265 | -52.47129 | 2026-09-17 04:42:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 38a76eb9-a659-31b3-af87-813be41ac701 | -12.45092 | -50.80199 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8e2dcd1a-eb74-3739-8e88-c9d689d4528f | -12.4911 | -50.76156 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2c70e8bc-acf1-3dac-8670-fe6c55b49980 | -12.49213 | -50.77953 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8885bc6c-0c98-341d-856c-7b32ac3bfe0a | -12.48285 | -50.77106 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 745aad74-2112-3f6d-a157-6840dfaad870 | -14.18527 | -45.14458 | 2026-09-17 04:42:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 00c6fdee-44f6-3274-9f87-1a252e8ecf42 | -12.48121 | -50.78161 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6aadcb70-8546-3a8b-beec-ba9fdb2085d8 | -12.49274 | -50.81929 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 79ed1276-582b-341c-81da-132092626a2c | -12.45314 | -50.80956 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2d2ea187-3089-3d17-abd7-0cafeb2e8460 | -12.45704 | -50.84983 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| eb36f15d-ebc3-3cf9-bfa5-f8fdbc4396ba | -12.4636 | -50.80764 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8daddfa5-62bb-3f5c-8156-21631a05f1b8 | -12.47793 | -50.80272 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| aef242fb-f4a4-3112-b15f-f7c5b6b7b91e | -12.70932 | -48.27224 | 2026-09-17 04:42:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 62643d3f-b910-39ad-81e1-c6f3f4761433 | -12.42546 | -48.48576 | 2026-09-17 04:42:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 020abb9c-3c00-33af-9e1c-9bc96faa1d9b | -12.47293 | -50.76946 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1ebeacf2-931f-34b4-8120-d1d21d88bf5f | -16.98841 | -45.47146 | 2026-09-17 04:42:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5f3f0e9f-8cf1-3d53-88f7-c03a05202a0e | -10.87965 | -61.39536 | 2026-09-17 04:42:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 51aae6e0-09db-36f0-94ba-d22d82a561ba | -14.22184 | -48.5117 | 2026-09-17 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 65aff98c-a016-38d4-beab-9443c6ad95d8 | -12.59734 | -50.73505 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 300e341f-7b50-36ce-9bb6-b1dfd24e164b | -12.46529 | -50.84035 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 381d58dc-102c-3e4c-b88a-6e47ee460ffa | -12.47678 | -50.76648 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b48aa20c-e077-3a35-89bc-1dfa3e429e84 | -12.40565 | -48.47457 | 2026-09-17 04:42:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e45c2b80-2b3b-3ec9-90a6-361191f7e683 | -12.14386 | -61.16757 | 2026-09-17 04:42:00 | NOAA-21 | PARECIS | RONDÔNIA | Brasil | 1101450 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |


[Clique aqui para ver as próximas entradas](README54.md)
