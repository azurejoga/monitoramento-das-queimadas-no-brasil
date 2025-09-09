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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c849bde1-0574-3c18-99d5-b0830cc5f0b0 | -7.5688 | -44.65687 | 2025-09-09 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 02b6a45f-6ba4-3f39-84c5-4e0d9b8e2b56 | -11.43337 | -43.60253 | 2025-09-09 04:34:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| d84413c1-0ca1-38ad-b723-afa546ca44aa | -14.43341 | -48.47362 | 2025-09-09 04:34:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ef309100-b891-3828-8eeb-86c1bd899f25 | -9.0945 | -45.72051 | 2025-09-09 04:34:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e24ad765-8eec-38ad-a15c-8793c47c3577 | -10.577 | -52.01592 | 2025-09-09 04:34:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1e99734b-14ac-3354-ab6d-5ee8d24bc43b | -9.29131 | -60.85723 | 2025-09-09 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e77d5a92-5d73-3d52-af07-65145005d750 | -13.94358 | -48.23193 | 2025-09-09 04:34:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ea98d77d-5f46-3431-abcc-976d601f139e | -13.96216 | -48.24598 | 2025-09-09 04:34:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0b9f5b3d-4dfd-398d-88bf-4684ee3bf108 | -10.09126 | -48.18006 | 2025-09-09 04:34:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e41cd6a0-6cb1-3be9-a8e1-8491a2ad5231 | -11.2133 | -55.00914 | 2025-09-09 04:34:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 77c6094f-a4cc-3596-980c-5fb8cd9d3f5f | -12.61322 | -56.97457 | 2025-09-09 04:34:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 55403710-40b4-3004-a370-77fe5fe89ed0 | -12.19779 | -53.89098 | 2025-09-09 04:34:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 10177f3f-6189-32da-879c-ea50cbb3aa0c | -13.95597 | -48.24127 | 2025-09-09 04:34:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 12e9dbec-bc07-3b5e-a757-77aa321fe09c | -9.44748 | -60.52026 | 2025-09-09 04:34:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 055574b4-3c3f-384b-a029-ce7925c9a989 | -7.66599 | -50.292 | 2025-09-09 04:34:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d311e406-0b45-3a24-8faf-01873ec90b78 | -13.65707 | -46.96749 | 2025-09-09 04:34:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 96b504ba-caf7-3ed1-9414-24c782ac0543 | -8.69721 | -48.87425 | 2025-09-09 04:34:00 | NOAA-21 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c10dcef3-a7c4-3fb6-9702-3d04f6dfc708 | -10.57343 | -52.01527 | 2025-09-09 04:34:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 26f72e38-504c-364c-bac6-14aca38366ec | -13.01976 | -48.0325 | 2025-09-09 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 67c29349-74ae-3b24-9481-151ddcb1801e | -10.9695 | -45.10991 | 2025-09-09 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 25.9 |
| bd7e0362-f316-30c3-950a-73aa81ad8f6b | -10.90204 | -55.70096 | 2025-09-09 04:34:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 554f2405-4559-3139-9aa3-fef1550bb500 | -11.34568 | -46.57273 | 2025-09-09 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6b468010-5949-348d-b991-7b1a9a7e71f9 | -13.29714 | -51.73271 | 2025-09-09 04:34:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 07100047-2eec-3090-bbf9-57e0dee93c92 | -6.86911 | -47.90549 | 2025-09-09 04:34:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 24f96fce-7b73-3a72-90f0-e2876ce1b729 | -11.11563 | -48.37078 | 2025-09-09 04:34:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1c7f34d8-8a69-3234-8752-284714f03517 | -7.85826 | -44.7974 | 2025-09-09 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3a916b55-5999-3b03-8ba2-fab7726a11a4 | -14.29954 | -49.41769 | 2025-09-09 04:34:00 | NOAA-21 | NOVA IGUAÇU DE GOIÁS | GOIÁS | Brasil | 5214879 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 0978c169-dd84-3bb5-8764-90784a523d36 | -7.74494 | -50.73658 | 2025-09-09 04:34:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3233b0ef-5dc4-35b0-8350-2a2ea54f6f20 | -11.4256 | -43.59746 | 2025-09-09 04:34:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a6134ca1-ab78-336e-84fd-5c38379e6366 | -12.62455 | -56.96617 | 2025-09-09 04:34:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a162ca48-e7ea-3f60-8087-56b05c081e1a | -13.18204 | -47.25028 | 2025-09-09 04:34:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0b5d0856-441b-32ef-9dd8-5277d8c5de0c | -9.61852 | -46.0413 | 2025-09-09 04:34:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 25be2bb9-b76a-3479-aead-3847eacf5d45 | -12.95178 | -54.81127 | 2025-09-09 04:34:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 35908f0e-8b80-354a-87db-a76d6cf19c50 | -10.7766 | -47.72337 | 2025-09-09 04:34:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8537861b-782c-35bc-a093-0d6d321149a5 | -12.94432 | -54.80614 | 2025-09-09 04:34:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3151315d-fc1b-308a-b22b-184935393e59 | -13.93908 | -48.23893 | 2025-09-09 04:34:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 9.9 |
| eb9b00fe-fc8e-31e0-bb0c-892dcbf518fd | -10.57918 | -52.02483 | 2025-09-09 04:34:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 37b70ee8-34ec-32d0-b19b-5cc350025322 | -5.50286 | -60.13949 | 2025-09-09 04:34:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 87d3f15c-c7db-3cdb-b0dc-674b866a975c | -11.95238 | -50.97145 | 2025-09-09 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 20a977ac-e132-3e41-a8cd-8fbb2cb825c6 | -9.27763 | -56.89997 | 2025-09-09 04:34:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 61746ffc-c07f-33c2-ac58-617ee075a513 | -12.62734 | -56.97712 | 2025-09-09 04:34:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 404e6acc-a431-3fdf-9731-2e08ba806c5f | -12.92527 | -54.7724 | 2025-09-09 04:34:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c3a87bbc-c477-30cf-abfd-e26117590bb1 | -13.02258 | -48.03661 | 2025-09-09 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 86d38256-94e1-3bd5-b8d0-f0efb0b05b83 | -8.40193 | -49.10534 | 2025-09-09 04:34:00 | NOAA-21 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 9eea5915-4780-3f43-8d5c-7b84ba67770d | -9.17097 | -60.79575 | 2025-09-09 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6c143883-fa01-3b05-a6ee-b961e96c6b7a | -8.03719 | -48.63336 | 2025-09-09 04:34:00 | NOAA-21 | COLINAS DO TOCANTINS | TOCANTINS | Brasil | 1705508 | 17 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c9f0ceae-aef2-3fbe-b833-ce7f8ad91c23 | -10.33622 | -47.7362 | 2025-09-09 04:34:00 | NOAA-21 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 55b22598-d042-3210-917e-5c508d34a5b3 | -6.98392 | -50.29619 | 2025-09-09 04:34:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| beb7dbff-95b4-389d-b32b-d58bf3f1f648 | -12.18933 | -53.8872 | 2025-09-09 04:34:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ae24ee59-e7ee-3922-8520-f904a88c63cd | -11.43752 | -43.60313 | 2025-09-09 04:34:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 3b905c57-ea3c-3d79-9d53-3d992c629b26 | -11.35554 | -50.43003 | 2025-09-09 04:34:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f9645bd7-1aba-3e47-8544-36251ef992ab | -12.8439 | -52.94643 | 2025-09-09 04:34:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 537a09e2-7598-3d03-bc8b-aa43487d1b54 | -10.33588 | -46.35072 | 2025-09-09 04:34:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e97a3925-5cbf-34da-b2b1-a52e759b672d | -11.3049 | -46.50225 | 2025-09-09 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 1c5f9695-e324-3459-aefd-d0b2d07f1c50 | -11.89194 | -51.5117 | 2025-09-09 04:34:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c7c4f1e2-9cf3-332e-bfb3-cb952da825c6 | -12.94092 | -54.80172 | 2025-09-09 04:34:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 10677b41-900a-391a-bd5b-b59b6daa6373 | -10.97132 | -45.1243 | 2025-09-09 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 20.8 |
| d562b99d-3eba-33d5-ba11-d1187d14fb89 | -8.1952 | -44.7643 | 2025-09-09 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 54408d62-77fe-3a11-a64e-049c2828ea70 | -11.86249 | -47.54937 | 2025-09-09 04:34:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1705e8ce-c5ef-32d7-a78b-bd5cc0bfee36 | -8.48583 | -48.2682 | 2025-09-09 04:34:00 | NOAA-21 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 0a8a3ac6-9e7f-37e6-9037-4389762caf01 | -8.12064 | -44.86775 | 2025-09-09 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e6116c3b-159c-3660-807f-d00cc9fce86f | -13.94189 | -48.24315 | 2025-09-09 04:34:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 8a3ab4f8-ff05-37fb-ac8d-5a448610f0eb | -11.84074 | -46.77544 | 2025-09-09 04:34:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2499377b-3e6e-310e-83ef-12533361ee6c | -12.8903 | -47.98684 | 2025-09-09 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bfaf9d02-b4d2-346a-856b-d8287fad0079 | -12.01624 | -51.07707 | 2025-09-09 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7b926357-773e-353e-9182-6bbb2ed4a6d2 | -13.20278 | -51.77275 | 2025-09-09 04:34:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4ed72240-f766-347c-bee9-8b6b5b22d62b | -8.03607 | -48.61899 | 2025-09-09 04:34:00 | NOAA-21 | COLINAS DO TOCANTINS | TOCANTINS | Brasil | 1705508 | 17 | 33 | nan | nan | nan | Amazônia | 2.6 |
| aca867fb-266b-32f2-9e83-74bf27a4379e | -13.00931 | -54.81789 | 2025-09-09 04:34:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1637dbf6-cbdb-330a-b85a-47146d794ee4 | -8.00275 | -46.34247 | 2025-09-09 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c9b2c53e-ecc5-3a60-abce-6ea847660c2f | -11.83424 | -47.55271 | 2025-09-09 04:34:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a4b0a046-f86b-3b82-a6be-75af7a00043a | -8.43294 | -47.29158 | 2025-09-09 04:34:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| c6479628-a106-3ddd-8d05-cf63ec909bd3 | -9.87957 | -46.58909 | 2025-09-09 04:34:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e61550e6-f774-3a7c-9e4d-30e35da53f86 | -7.80407 | -45.41861 | 2025-09-09 04:34:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 16dd79f2-52e0-3fb2-b711-5aa8010f78e8 | -10.10485 | -48.1137 | 2025-09-09 04:34:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 46678364-37e4-37fe-a587-1e7a256ca082 | -12.8314 | -47.98866 | 2025-09-09 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 208fbefe-9370-3d6b-b9e9-2eb24dbce956 | -10.97261 | -45.11508 | 2025-09-09 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 25.9 |
| 45a53f81-69d8-3ace-91ba-ba81aaf381a8 | -10.15269 | -46.19548 | 2025-09-09 04:34:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c24b5195-a8a2-3a10-bf79-f6d340da62eb | -13.72873 | -46.89579 | 2025-09-09 04:34:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f2f0c95b-d1af-3595-8592-f0265aec7cfb | -10.16532 | -46.21309 | 2025-09-09 04:34:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 4f87b6b9-1d9b-31f9-ab5a-00ca02f96d00 | -12.19539 | -53.89853 | 2025-09-09 04:34:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 00d40036-251b-322f-863f-aeb95ee16d5d | -10.62416 | -47.34261 | 2025-09-09 04:34:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 3f046533-9ffe-385d-baa1-6c139af1920e | -8.06391 | -45.52184 | 2025-09-09 04:34:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| d55e64e1-5d66-344e-aa44-db13e9cfa804 | -8.04998 | -48.64244 | 2025-09-09 04:34:00 | NOAA-21 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 98939fe0-b74f-33de-8569-792f954757be | -7.14479 | -46.05704 | 2025-09-09 04:34:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cd822553-fe71-3004-86c3-f93ed7a67aee | -13.02424 | -48.0257 | 2025-09-09 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6866c32f-5c54-3f25-8d5e-f517a9d3ebe5 | -13.65651 | -46.9714 | 2025-09-09 04:34:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 47338270-f470-35b6-b177-d4a9b8392fbd | -12.61204 | -56.97207 | 2025-09-09 04:34:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9220eddd-1b03-3045-9984-501bd32eba81 | -9.47483 | -48.77522 | 2025-09-09 04:34:00 | NOAA-21 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| eed07283-530e-34d6-b4b1-cae67d945517 | -11.6705 | -46.89062 | 2025-09-09 04:34:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2c51414d-035d-3010-8d73-d5bbbb5633ce | -9.70587 | -46.81037 | 2025-09-09 04:34:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 474f2ce7-9ddb-34e1-a508-8bd5f0d39797 | -12.93141 | -54.78477 | 2025-09-09 04:34:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d77fbab0-23d9-3458-8f42-45ea0e2bb2c9 | -12.8337 | -52.94019 | 2025-09-09 04:34:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 86f53171-dd67-3a17-9c98-5e8f1318ef85 | -10.83533 | -47.26934 | 2025-09-09 04:34:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5c671c34-8eb0-3952-bb85-665a39465cae | -11.43287 | -43.63733 | 2025-09-09 04:34:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 69685869-0681-3cdd-8ca2-864ccded42cb | -12.63393 | -56.96801 | 2025-09-09 04:34:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d5d855e0-10ca-3b1c-8b3a-1fe131ab7466 | -11.18479 | -48.38561 | 2025-09-09 04:34:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fa547ed3-7a51-39b1-a285-8b787da0aec3 | -11.42562 | -43.62852 | 2025-09-09 04:34:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6f0648b6-7233-3370-8108-7a5f356189f6 | -11.62365 | -52.23009 | 2025-09-09 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 49d6c7b4-1a77-32f1-bf5f-f95482f6d470 | -9.15565 | -45.57951 | 2025-09-09 04:34:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 50415046-0869-3119-bd63-cb19c4caac68 | -11.3323 | -46.54193 | 2025-09-09 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README40.md)
