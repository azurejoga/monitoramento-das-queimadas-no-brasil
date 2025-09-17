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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 58751397-5a59-3aa1-8899-c35d331c2c09 | -0.75377 | -47.75312 | 2025-09-17 04:29:00 | NOAA-20 | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c683c2ee-4ee3-3191-a833-6d708605af9e | -3.03516 | -43.25275 | 2025-09-17 04:29:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 69ef1be6-636d-3abd-abda-b079e85e9b05 | -3.0694 | -49.4589 | 2025-09-17 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8b7e5e54-1ff2-3e18-aaa5-1c00ef31ac82 | -1.95433 | -48.11402 | 2025-09-17 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 39b676c4-f91a-3e54-bd60-aca45f83cc1c | -3.42214 | -46.96821 | 2025-09-17 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b0cab22b-2031-3c5d-86a0-376ba0163e2e | -3.61165 | -41.35714 | 2025-09-17 04:29:00 | NOAA-20 | COCAL DOS ALVES | PIAUÍ | Brasil | 2202729 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 48b0b98b-f681-359f-bd4b-26d5fe2db417 | -0.75712 | -47.75364 | 2025-09-17 04:29:00 | NOAA-20 | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 344dd659-c075-3efc-94e5-cde47394871f | -3.41992 | -47.60632 | 2025-09-17 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c52b63e2-a026-3c90-8bba-4004ce02bf9f | -2.9182 | -48.3044 | 2025-09-17 04:29:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 23257b11-e53d-378b-9c6d-9101212fecd8 | -2.92099 | -48.30849 | 2025-09-17 04:29:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 20.7 |
| 4feb8171-7c6f-34c4-bc4c-55aa35a05bfe | -2.29522 | -48.14207 | 2025-09-17 04:29:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 894ddcae-4dc5-34d6-af03-d48a3d59f2ca | -2.25936 | -47.19064 | 2025-09-17 04:29:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 54bf658b-649f-3e1f-b56d-df6f9cbbeb32 | -3.60373 | -38.95116 | 2025-09-17 04:29:00 | NOAA-20 | SÃO GONÇALO DO AMARANTE | CEARÁ | Brasil | 2312403 | 23 | 33 | nan | nan | nan | Caatinga | 13.6 |
| 8ec61980-5abd-3188-8e00-121fa4544b7d | -3.59828 | -38.95328 | 2025-09-17 04:29:00 | NOAA-20 | SÃO GONÇALO DO AMARANTE | CEARÁ | Brasil | 2312403 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 7e3b9f86-e848-3ad6-9a95-9f9311c58f30 | -3.81258 | -41.683 | 2025-09-17 04:29:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| f90c48b0-24b5-38a3-aa56-d520a1bb777d | -1.97492 | -47.98297 | 2025-09-17 04:29:00 | NOAA-20 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cace1704-d2b3-3c12-8ca0-e7d6641598b0 | -2.37993 | -47.63099 | 2025-09-17 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 36e9fe2e-2f88-3081-8971-1c07f962da45 | -2.82918 | -48.65859 | 2025-09-17 04:29:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 892aab5e-9570-31a8-bc09-8454fbf033b5 | -3.17734 | -48.80925 | 2025-09-17 04:29:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 8943012c-342c-30f4-af70-d798a367fa65 | -2.37439 | -51.9086 | 2025-09-17 04:29:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3042f8d7-c5d0-3e21-a56d-dbe3517e9276 | -3.01089 | -41.83434 | 2025-09-17 04:29:00 | NOAA-20 | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 159cda23-4f0c-3a31-941e-9c5ff061cb1a | -2.98738 | -49.2939 | 2025-09-17 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| aff045ac-ed17-3a96-9308-d5f7bff89fb5 | -3.23557 | -46.79405 | 2025-09-17 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 7bad3ab1-010d-39f5-be3e-67a7c1b86398 | -2.26454 | -47.88781 | 2025-09-17 04:29:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ca53cc47-d982-3ef4-8655-b95ab6ba5120 | -3.06879 | -49.46273 | 2025-09-17 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 714f4e65-ec5d-3204-979a-246a2e411a84 | -3.60416 | -38.94825 | 2025-09-17 04:29:00 | NOAA-20 | SÃO GONÇALO DO AMARANTE | CEARÁ | Brasil | 2312403 | 23 | 33 | nan | nan | nan | Caatinga | 9.1 |
| 7f4b129e-a891-3192-a288-f364cc0e89bc | -2.98392 | -49.29335 | 2025-09-17 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a1f6b149-dc7e-35bb-97de-35bd36a55370 | -3.23888 | -46.79457 | 2025-09-17 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 52719805-1764-3e3f-9eca-74ed6867615b | -3.36514 | -46.50984 | 2025-09-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 6959ab6a-4da5-33eb-9410-2a911ec1339a | -2.37661 | -47.63047 | 2025-09-17 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1a002040-c800-3dda-a4e3-e460498eb9e3 | -2.96318 | -48.58649 | 2025-09-17 04:29:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6edd6ec6-8608-30e4-98a1-c13cbd093fb1 | -3.75792 | -38.7024 | 2025-09-17 04:29:00 | NOAA-20 | CAUCAIA | CEARÁ | Brasil | 2303709 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 29c9a1cd-bfb0-3a84-9a0f-a16ecd0d0976 | -2.37496 | -51.90508 | 2025-09-17 04:29:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a61a9c2f-156a-3778-9268-f7eca77326dc | -2.26175 | -47.88378 | 2025-09-17 04:29:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b7c91948-3db3-3c60-b5a1-c7d1f94f66ac | -1.62346 | -49.94274 | 2025-09-17 04:29:00 | NOAA-20 | CURRALINHO | PARÁ | Brasil | 1502806 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6b80ba4c-6468-3ff9-a3d2-0668d17da5de | -2.96261 | -48.5901 | 2025-09-17 04:29:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 765ac166-dcb9-35e4-a371-28bf0e84ec41 | -3.60331 | -38.95407 | 2025-09-17 04:29:00 | NOAA-20 | SÃO GONÇALO DO AMARANTE | CEARÁ | Brasil | 2312403 | 23 | 33 | nan | nan | nan | Caatinga | 13.6 |
| b3e29b28-dfcc-38d3-8755-ce32341bc433 | -3.18016 | -48.81342 | 2025-09-17 04:29:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 4154def2-b28d-3d39-befa-ef1bfacdbf60 | -5.19251 | -35.8686 | 2025-09-17 04:29:00 | NOAA-20 | PEDRA GRANDE | RIO GRANDE DO NORTE | Brasil | 2409506 | 24 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 0e9d7b56-c260-3cb7-809e-fbe60cef4b81 | -3.898 | -40.9207 | 2025-09-17 04:29:00 | NOAA-20 | IBIAPINA | CEARÁ | Brasil | 2305308 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 2a9fca8a-e22d-39b0-a4ce-d8edcd87d449 | -3.59912 | -38.94749 | 2025-09-17 04:29:00 | NOAA-20 | SÃO GONÇALO DO AMARANTE | CEARÁ | Brasil | 2312403 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| f6e118db-7fe7-33b1-837b-c781e327268f | -2.91877 | -48.30086 | 2025-09-17 04:29:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| ae56d4c2-23b4-3650-b252-9d205480d0cf | -3.78203 | -43.35601 | 2025-09-17 04:29:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 77321ee8-172f-30ba-9d6f-2beaec1160d3 | -2.8395 | -48.83922 | 2025-09-17 04:29:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 50a7edd7-7318-31f9-bd87-233d2f1189fd | -2.25785 | -47.84369 | 2025-09-17 04:29:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 36f2db91-1907-3cb0-b006-9fbbc6aea5e1 | -2.83257 | -48.65913 | 2025-09-17 04:29:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 1bac4077-455e-350a-ad9f-4d68aa7954b8 | -3.42268 | -46.96477 | 2025-09-17 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 529bee05-af87-35e6-b839-d32d6248ecd1 | -3.23611 | -46.79061 | 2025-09-17 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 5227b7fb-af7e-30df-bba7-0cab7555e816 | -2.92156 | -48.30493 | 2025-09-17 04:29:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 36756499-8a68-3723-9548-41715926eea8 | -3.21676 | -47.12959 | 2025-09-17 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bbae00b0-d524-380a-8de9-e782e1ddaaa6 | -2.82975 | -48.65496 | 2025-09-17 04:29:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f2db3eda-073c-3c4f-b348-90fe9141cbbf | -3.75747 | -38.70547 | 2025-09-17 04:29:00 | NOAA-20 | CAUCAIA | CEARÁ | Brasil | 2303709 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 1dfb69dd-3ed8-33cf-8240-ca5a9e244877 | -2.39244 | -48.62769 | 2025-09-17 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 95a768ba-0e37-3eb2-b519-4be209b1542a | -3.18074 | -48.80978 | 2025-09-17 04:29:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| c078b46c-1866-3151-8b91-e9c73e899a60 | -2.91764 | -48.30796 | 2025-09-17 04:29:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c4cdca5e-340e-3963-a412-9cc5e3667b3f | -3.15465 | -49.48425 | 2025-09-17 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 959b4a54-8305-3ef6-af8a-9354b3a73a6b | -2.61568 | -43.46865 | 2025-09-17 04:29:00 | NOAA-20 | HUMBERTO DE CAMPOS | MARANHÃO | Brasil | 2105005 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9050a34d-6545-3077-9521-1fcea07a5758 | -2.37938 | -47.63446 | 2025-09-17 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 110387fa-73d3-36d1-8844-7b836a47280a | -3.2328 | -46.79009 | 2025-09-17 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a6163bc2-a9e9-32b9-9201-ac460e798e66 | -3.4192 | -43.14898 | 2025-09-17 04:29:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a19a103d-9494-3c0c-870d-7f8788498295 | -3.5987 | -38.95039 | 2025-09-17 04:29:00 | NOAA-20 | SÃO GONÇALO DO AMARANTE | CEARÁ | Brasil | 2312403 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 5575ad7b-3c53-38ab-9b9f-e5899c8630fa | -3.39433 | -44.75136 | 2025-09-17 04:29:00 | NOAA-20 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9bb1b234-e5ef-3095-ba8f-bd20d917c04c | -2.26119 | -47.84421 | 2025-09-17 04:29:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5a5db4c5-e030-3e63-a3f5-943296ef92e3 | -4.51448 | -38.54958 | 2025-09-17 04:29:00 | NOAA-20 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| dedf3fc2-42c6-389c-b07b-b9ca1e08bf94 | -1.95097 | -48.11349 | 2025-09-17 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fa9bb2ab-4862-3a2b-b027-8e132225f37a | -2.83314 | -48.6555 | 2025-09-17 04:29:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| fb17a044-6938-361e-90c4-95b296ffc2c4 | -2.29801 | -48.14614 | 2025-09-17 04:29:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b3ff1260-1baf-3ef9-a143-5c47f0b37c73 | -3.30903 | -42.16751 | 2025-09-17 04:29:00 | NOAA-20 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 1dffa162-89a9-3477-9490-e9bde04c2bfb | -2.29858 | -48.1426 | 2025-09-17 04:29:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 82a5eef8-eb77-3dab-910d-8852a31ec49d | -3.03212 | -43.2477 | 2025-09-17 04:29:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2e8caca1-de06-3f04-8ef3-4906a1e980b3 | -2.37606 | -47.63394 | 2025-09-17 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 8c5bd197-d012-35ae-a42b-15f5aaeb9ff6 | -1.8085 | -47.69822 | 2025-09-17 04:29:00 | NOAA-20 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0d6134a2-42f0-3eda-a0c0-db3f00e092cd | -3.15626 | -49.48412 | 2025-09-17 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7ce75b0d-a327-3947-9091-ede748147a7e | -3.15278 | -49.48357 | 2025-09-17 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c02037bc-16b2-3871-bbc6-878f6e957c58 | -3.07464 | -48.8158 | 2025-09-17 04:29:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c16221e7-3b7c-35f8-8137-94ba96c0a2e7 | -2.7855 | -49.62305 | 2025-09-17 04:29:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ed7ded9e-92f4-3e16-b892-bf46600179e2 | -3.39723 | -44.75574 | 2025-09-17 04:29:00 | NOAA-20 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f59976d3-3ae9-30c3-a553-db01cdc20af9 | -2.26509 | -47.8843 | 2025-09-17 04:29:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0677e359-eaa3-33d2-a8f3-cc2b798ae467 | -3.2173 | -47.12615 | 2025-09-17 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1ac7bb25-6a3b-360e-a6e2-57a376fd70b5 | -2.64596 | -48.05183 | 2025-09-17 04:29:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 80ceb938-6f10-3b45-bd2b-a65307eea0ef | -2.26213 | -47.1946 | 2025-09-17 04:29:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 54535877-3c46-36c0-8ec5-7278110ba7fc | -3.23335 | -46.78664 | 2025-09-17 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7186cd5d-971f-31b1-aca3-c263b8b89f98 | -2.832 | -48.66275 | 2025-09-17 04:29:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4f6b16fa-5005-3414-8710-6b7424cbd1ad | -3.23666 | -46.78716 | 2025-09-17 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 7ef7d251-fc28-343a-b8fe-827b0e54bd1c | -1.69355 | -47.07341 | 2025-09-17 04:29:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4687b7d5-ae6b-3e6d-8b6f-c1d34b053772 | -8.96508 | -45.75286 | 2025-09-17 04:32:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1895dc94-f078-37a1-bbd7-869f33a7b68d | -8.87172 | -50.14397 | 2025-09-17 04:32:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1af2575e-e76b-3dbc-80d6-08cef7a3410e | -6.15867 | -44.52539 | 2025-09-17 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a704457c-31dc-37de-9678-a11d4845f448 | -7.81265 | -46.11838 | 2025-09-17 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a9a22480-fa7c-35d7-b008-d07f7dc47a52 | -7.97833 | -45.63227 | 2025-09-17 04:32:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fcbbaae4-25e5-3b0e-ab91-8ef1fd5a0bfd | -7.44396 | -46.19327 | 2025-09-17 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0d484816-7a0a-3e2f-afc4-d96484af522e | -4.39991 | -48.90299 | 2025-09-17 04:32:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9fd9c8c9-8784-319d-80e7-da134319db80 | -8.21052 | -49.48215 | 2025-09-17 04:32:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 070c3ce9-d579-3cc5-9f4b-73dcb7658c8d | -8.15665 | -46.75452 | 2025-09-17 04:32:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9b5cbb8b-d791-323e-86d3-64d399230943 | -5.81617 | -46.36383 | 2025-09-17 04:32:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 58546228-7c2a-3f21-b58f-4d1026a8c907 | -7.41176 | -49.99846 | 2025-09-17 04:32:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8fc5ca0d-32f5-3395-aa29-9b20f45ec63b | -7.40029 | -50.00426 | 2025-09-17 04:32:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e59e61da-c5d0-3a45-be5d-fae3548162d8 | -7.06766 | -44.34543 | 2025-09-17 04:32:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 60225734-01e8-3c73-9ee5-632debecd404 | -9.13706 | -46.9336 | 2025-09-17 04:32:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 41ae5def-43ff-3638-9a99-5ab7c98c6f65 | -8.24605 | -47.58392 | 2025-09-17 04:32:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README34.md)
