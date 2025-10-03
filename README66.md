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

## Dados Diários - Página 66

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8f3ec3f1-0857-321a-8807-43030cb817f2 | -12.60789 | -46.99451 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 8f160e8b-efe1-3437-bfec-637f29eb9d22 | -9.76056 | -47.81106 | 2025-10-03 04:12:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0078eb5a-2c6f-3ef8-9ea5-13c15d76f09e | -10.93154 | -46.73403 | 2025-10-03 04:12:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c6d7d88a-86dd-3bf6-b288-8e511a7f9658 | -13.77016 | -48.06602 | 2025-10-03 04:12:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| b34d911f-3005-3fd0-a8e8-19aae78bd462 | -13.29594 | -47.26653 | 2025-10-03 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| cac0cf6a-5072-3482-a7d1-f50d09185c5c | -13.14903 | -47.83095 | 2025-10-03 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 78d81875-273e-305e-a016-ad12a23de662 | -12.53337 | -47.31085 | 2025-10-03 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 24678101-3eb7-3522-99ef-8c10193c0624 | -12.85138 | -46.8611 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ca53e0af-6f1e-3b0e-a054-84441cdf08aa | -9.76352 | -46.23104 | 2025-10-03 04:12:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8964cddd-e2c2-3fb3-a0d2-1281973606c7 | -13.76911 | -48.06219 | 2025-10-03 04:12:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| dd15ecfc-07b1-33ac-861f-d89b605ffebc | -9.33411 | -45.68039 | 2025-10-03 04:12:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 239b08cd-0ff3-3ce9-93dc-4a0eaa24a537 | -13.25783 | -47.26025 | 2025-10-03 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 57477ae1-8fae-3b8c-978f-0f5655f07662 | -13.68542 | -48.63866 | 2025-10-03 04:12:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 800cabf9-9aea-32cf-872e-0381a6b88883 | -9.90989 | -43.72178 | 2025-10-03 04:12:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 13.2 |
| 04207f84-a812-3c4b-b6e5-85db3c175c86 | -13.13943 | -47.88625 | 2025-10-03 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 14.7 |
| ba440c8f-94a1-3abe-97ed-d7689cc30b17 | -8.79981 | -46.66629 | 2025-10-03 04:12:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c7830cb1-1bce-32f4-912b-2888899f98e6 | -12.19545 | -47.79103 | 2025-10-03 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| be20b703-e310-3289-a23d-6d4332b7d875 | -10.92621 | -47.04952 | 2025-10-03 04:12:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1c9be541-33a5-30c9-9745-230d7d673f8a | -13.79032 | -47.58207 | 2025-10-03 04:12:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 8.6 |
| fafc4152-dbf8-357d-b3aa-2cf7b014e2c9 | -12.83703 | -46.94473 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fcba2aae-9912-32ef-a3c3-72b45203f638 | -14.70229 | -43.88405 | 2025-10-03 04:12:00 | NPP-375D | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Caatinga | 1.6 |
| bee25ca0-e6dd-3cb7-9d94-b86178867f63 | -10.00735 | -50.25154 | 2025-10-03 04:12:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 16.7 |
| f6c7e17a-d41f-3dc5-bd85-0af517972761 | -8.5208 | -50.03909 | 2025-10-03 04:12:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1b93624f-44dd-3e47-972f-fcfcd3b7757d | -14.19291 | -46.06894 | 2025-10-03 04:12:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 29.1 |
| 99c6f374-f340-3e97-93d6-367ad939c1dc | -14.69505 | -43.88651 | 2025-10-03 04:12:00 | NPP-375D | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 8f409e39-f2b2-33c7-bc8c-56cd53270781 | -11.55841 | -47.64809 | 2025-10-03 04:12:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 7b0b5e9a-fcc1-3f66-8be3-311aa7bcdc7e | -9.08314 | -48.02453 | 2025-10-03 04:12:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ce5cca05-7fc9-33e5-976c-d4d4696f3dc6 | -11.77446 | -46.82467 | 2025-10-03 04:12:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2143be7a-f4d6-30eb-a917-78c221040765 | -11.41513 | -43.49459 | 2025-10-03 04:12:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 399ed93f-6106-3374-b10d-cf57075da4b7 | -12.61039 | -46.97998 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 235ef757-91d1-3757-8190-ce8af83c52b7 | -13.33812 | -48.1154 | 2025-10-03 04:12:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7e7bb1a4-beb0-32c7-98a7-ee1227b6c20d | -13.24004 | -47.34874 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e6abb4f9-31cf-35ba-9537-639c148c8019 | -14.21886 | -44.79427 | 2025-10-03 04:12:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b1eb0438-fbd6-3804-b7cb-6134e546c1e5 | -14.4097 | -47.87094 | 2025-10-03 04:12:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 93ab8972-c3e6-30e1-94a3-696222da0722 | -12.61881 | -46.97624 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 15.4 |
| e59f492c-e48a-390c-87a2-bfdfe829be4b | -10.22629 | -48.24127 | 2025-10-03 04:12:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e57f7129-3aff-3e64-9600-0b489baaf5eb | -13.94276 | -48.15371 | 2025-10-03 04:12:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 73780791-c159-3075-bc0c-0e59f2145255 | -11.08569 | -47.70572 | 2025-10-03 04:12:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 220e2b2e-a10f-3eb2-b582-d47745a3a54b | -12.64934 | -46.9998 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6c0d4e38-3cef-3923-b0bf-197a2bcbf371 | -11.63058 | -47.99149 | 2025-10-03 04:12:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ea5f217a-9cad-375d-be36-3a50c13811a5 | -13.75464 | -48.08477 | 2025-10-03 04:12:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 07318840-bc51-3ad2-bbf1-2fdc7e5e3f78 | -14.32756 | -45.86765 | 2025-10-03 04:12:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c4baf56e-faca-38e6-8850-d711e0120fe9 | -9.07182 | -46.6601 | 2025-10-03 04:12:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 64f671d7-3706-397f-b8e2-bd4e8177a33b | -9.94049 | -43.75315 | 2025-10-03 04:12:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| e7806bf4-6984-3d40-95d5-3ae03f9c26bb | -11.10413 | -47.83503 | 2025-10-03 04:12:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7c50ce35-6095-34b8-8918-5d6959b8414d | -13.34095 | -48.09966 | 2025-10-03 04:12:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 09e85978-a513-39e3-9fc2-f92fa1688356 | -13.79883 | -47.57874 | 2025-10-03 04:12:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| b02b991b-29db-3ad2-9e5e-2c0d2caa400e | -11.44801 | -43.50367 | 2025-10-03 04:12:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 797d2168-791a-3dc1-b1a0-67dfa5fd1d66 | -13.21337 | -47.82803 | 2025-10-03 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 6f50158c-fda0-336c-a9d9-fc725950ad44 | -9.41553 | -47.53593 | 2025-10-03 04:12:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b5d64ecf-859d-3582-9d35-d81bddb02695 | -13.55868 | -47.29505 | 2025-10-03 04:12:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cc5c86d6-7742-3efd-bcc8-cf7d65a4904e | -12.61963 | -46.97146 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f9d33981-18ab-3d4e-ba17-572165726318 | -11.14068 | -43.39513 | 2025-10-03 04:12:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f5b48898-77fe-35d5-9b6d-6bd0b12c7ceb | -11.61781 | -45.03068 | 2025-10-03 04:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 62e218ce-cb89-3337-9583-eed4fedb444d | -9.91151 | -43.73327 | 2025-10-03 04:12:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| e22aaefe-82be-3c5f-a0a9-7e8e11b31916 | -13.78147 | -44.24335 | 2025-10-03 04:12:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8b989f1d-a259-30fe-9804-09c9a41ace90 | -14.19594 | -46.11615 | 2025-10-03 04:12:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5b8a88f3-d2cf-3031-afd7-d3540edffa7e | -11.81143 | -45.01861 | 2025-10-03 04:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b656ca31-031f-3133-b687-71f064ae3286 | -10.2257 | -48.24466 | 2025-10-03 04:12:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c499f734-6614-3cc2-b907-0327eece9e5d | -13.30622 | -47.25255 | 2025-10-03 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| bf543409-9f3d-30de-b038-32747fab8c3c | -10.87386 | -47.82498 | 2025-10-03 04:12:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 68aa42e9-9b15-307b-ba14-69781c4fee0c | -11.90857 | -46.74277 | 2025-10-03 04:12:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 454a06e9-b5f8-3c6f-beb6-233d9c62f1d3 | -12.75404 | -46.88845 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 48b1683f-65f8-334e-8e09-4a1d5bf51961 | -13.97675 | -48.15807 | 2025-10-03 04:12:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3cf5f2f4-2058-34aa-86a2-5985f3935a7a | -12.62175 | -46.98182 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 51ca6b42-1c2b-3203-b196-759c5f45c741 | -12.6827 | -48.54717 | 2025-10-03 04:12:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e0b67b85-cdcf-3d43-ac85-eaea03fa2f23 | -10.96748 | -51.0921 | 2025-10-03 04:12:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9443f2fe-67f8-3291-a451-c7209d5eeef0 | -10.33846 | -43.73141 | 2025-10-03 04:12:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c0564305-7648-3e72-bcd2-af51eb21a668 | -11.49655 | -43.50075 | 2025-10-03 04:12:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 049408d6-1bda-31c9-b73a-2764d4039d7c | -11.83939 | -45.04375 | 2025-10-03 04:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9db01a41-7199-3c6a-ab7c-e35b4004b9cf | -11.08471 | -47.87314 | 2025-10-03 04:12:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e9bb4948-3153-3201-a667-b07f38efdba9 | -10.85907 | -45.41789 | 2025-10-03 04:12:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2b8bc051-a7db-37dd-9f0a-8a6bbdc50842 | -11.14412 | -43.37374 | 2025-10-03 04:12:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 5145958b-b988-3bbf-8095-c58492ef8531 | -11.59645 | -47.66584 | 2025-10-03 04:12:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 53555f35-383e-34be-98cf-6f3536c574bd | -10.96666 | -44.33939 | 2025-10-03 04:12:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 74a3ea38-ff51-31c3-808d-7dc0ae5b2be5 | -12.67462 | -46.85353 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 79e5e5b2-4e59-35b9-a807-263cfa8f9373 | -10.00248 | -50.25061 | 2025-10-03 04:12:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 124d07f1-08dd-3cc1-a4ac-ff5ce7d732a4 | -13.2569 | -48.4306 | 2025-10-03 04:12:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e4f7c88b-ba28-37ec-9874-2b03b680f829 | -14.20201 | -46.05815 | 2025-10-03 04:12:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 29.7 |
| 2502370d-08e4-3f6c-8409-0bf3dbb2357a | -14.68982 | -45.18137 | 2025-10-03 04:12:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5a898f7b-1c73-3902-92e8-5731d215566a | -9.94387 | -43.7537 | 2025-10-03 04:12:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| ba624ec1-5077-3ce9-9148-0dde21133475 | -13.3531 | -48.1239 | 2025-10-03 04:12:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fb73be9e-7ba4-3fa7-85d9-f4ede6824616 | -12.92573 | -46.38162 | 2025-10-03 04:12:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3093d61a-8fe3-3e8e-9cb5-be3df7abea97 | -10.92924 | -47.05512 | 2025-10-03 04:12:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ded1f86a-6e7c-311b-89b6-8aad6dec6d8d | -10.88244 | -44.27611 | 2025-10-03 04:12:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b52e656a-8dd2-3d87-8897-3dd848803e90 | -13.3051 | -47.60164 | 2025-10-03 04:12:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 00a99fd1-1ca7-377e-af95-e8d0cfd5443a | -11.46968 | -45.03415 | 2025-10-03 04:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 15736cb3-5652-359a-87c3-50e9369fa11f | -13.38443 | -47.2898 | 2025-10-03 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| d2108951-d485-3e08-bf43-459590b42767 | -12.93586 | -48.43532 | 2025-10-03 04:12:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6ca81b60-95c2-337f-86b3-12a25d8e4341 | -14.41052 | -47.86633 | 2025-10-03 04:12:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b37deb28-ba5b-371a-8b65-51289a5fbf53 | -15.25984 | -44.12457 | 2025-10-03 04:12:00 | NPP-375D | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 1408c7ce-9ac9-3955-9765-18510b695380 | -13.59051 | -48.19317 | 2025-10-03 04:12:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d3d3521a-57d7-3f12-be10-9a6224b2f0f0 | -13.12129 | -47.8735 | 2025-10-03 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9265b6be-e13e-339c-a2ef-fe01c66b6d7c | -13.67407 | -48.03203 | 2025-10-03 04:12:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| a9595cad-a4b9-37b0-98fd-3899f9679011 | -9.42307 | -47.54111 | 2025-10-03 04:12:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bdf4ada0-a701-307b-9910-ed281f994406 | -12.93722 | -48.43927 | 2025-10-03 04:12:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 98ae81b8-4847-3a53-9806-1465debbfa10 | -12.62195 | -46.958 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7e7c89e4-8f6a-3357-860c-16796dc2edf2 | -10.01122 | -50.22984 | 2025-10-03 04:12:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 17.3 |
| da020cd3-e26a-3493-a93e-9a6badd11d66 | -14.20439 | -46.10927 | 2025-10-03 04:12:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 3d789cf8-88fd-349d-96b5-f097ad197cf8 | -8.54007 | -50.15931 | 2025-10-03 04:12:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |


[Clique aqui para ver as próximas entradas](README67.md)
