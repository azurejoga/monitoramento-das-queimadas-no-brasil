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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0cdd6f82-2a1b-3a4d-bf74-e7c1f48918fb | -3.97613 | -42.49014 | 2025-10-17 04:17:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 65ab0d4c-24e2-3613-8f51-83e9a66b7b4d | -2.73216 | -49.38982 | 2025-10-17 04:17:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e6dbaeb0-09d2-302b-8a3a-31059a8cde06 | 1.03202 | -51.10518 | 2025-10-17 04:17:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8228997d-e168-3e67-b0d5-ec535332ae0c | 1.71733 | -55.80311 | 2025-10-17 04:17:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8c524597-88c9-35b1-a4a8-745642fdc63a | 1.72413 | -55.80201 | 2025-10-17 04:17:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b81414ac-2894-35e1-a815-f95d8a40e763 | -1.25673 | -49.03696 | 2025-10-17 04:17:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0a209614-c7d0-3bbc-8cd3-dbb5ddd0390c | -2.7356 | -48.30774 | 2025-10-17 04:17:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| bf6088e2-bef8-34e6-9ea2-43700fce2e0e | 1.0993 | -51.14425 | 2025-10-17 04:17:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8d366f2b-a257-3780-9d2c-ae91760df384 | -2.42358 | -48.59455 | 2025-10-17 04:17:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| df5a275d-dfac-336c-b05c-481b9ebf610b | -2.74111 | -49.38734 | 2025-10-17 04:17:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 03ad4cfc-2b3f-3ba6-9618-5ce013bd553f | 1.78777 | -55.9007 | 2025-10-17 04:17:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c2baee1c-7d8c-3073-b574-509eeecd448b | 1.10019 | -51.14996 | 2025-10-17 04:17:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6dad3a46-5248-32af-9ed0-7806626a3dd9 | 1.82743 | -55.70442 | 2025-10-17 04:17:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 55b1fb1e-ef53-369d-b349-7cd5644417fa | -1.4948 | -47.81107 | 2025-10-17 04:17:00 | NOAA-21 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| d4cb5fca-69c4-3624-8c80-6ba663b51cf6 | -3.32366 | -42.79529 | 2025-10-17 04:17:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b56ae695-5d63-3f27-9ad0-b939812f33e3 | -0.90055 | -47.54391 | 2025-10-17 04:17:00 | NOAA-21 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| eaf605eb-ce06-384d-aaab-585ee5f552f8 | -1.89736 | -51.01046 | 2025-10-17 04:17:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 34805741-f34f-3720-aab5-139d5e65b349 | -2.13189 | -48.00447 | 2025-10-17 04:17:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 679590d5-c73e-3200-ab4f-ebc8e3a0c48c | 1.824 | -55.7131 | 2025-10-17 04:17:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 11188b5c-39bf-3af3-9da0-8b4bcca3e1fd | -2.68844 | -48.70441 | 2025-10-17 04:17:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 77ad2783-69b0-3841-bf07-d491c5782469 | -2.96462 | -48.58518 | 2025-10-17 04:17:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 61ea47cf-a827-3bc4-a250-32f48e0c9785 | -2.74336 | -48.30901 | 2025-10-17 04:17:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 9ff82375-f401-3147-85be-075f3dd0dbbe | -2.26839 | -47.19236 | 2025-10-17 04:17:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 17231314-7c6a-30bf-899c-93bf56b8931f | -2.73278 | -49.38601 | 2025-10-17 04:17:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7e295030-d8b1-3edf-bc08-48c52867eeb3 | -2.71524 | -49.41458 | 2025-10-17 04:17:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 39f837fa-151a-362c-b06f-60b1bf34ec89 | -2.73948 | -48.30838 | 2025-10-17 04:17:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| f608476e-c3b0-3092-a971-2ac3b27d2e7b | 1.84752 | -55.68494 | 2025-10-17 04:17:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 59178e06-4e48-396d-b076-b0694fd376ed | -2.74724 | -48.30962 | 2025-10-17 04:17:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| f316c13b-ece0-3cf6-acbe-d7f6a5c3e435 | -3.23399 | -45.97077 | 2025-10-17 04:17:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d61196db-6bdc-3875-8557-c29762b5e6e7 | -3.62974 | -42.77379 | 2025-10-17 04:17:00 | NOAA-21 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 747cf163-92b6-35fe-8df9-7bfada17340e | -0.8801 | -48.08225 | 2025-10-17 04:17:00 | NOAA-21 | VIGIA | PARÁ | Brasil | 1508209 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c5be0da6-db63-347b-b735-7ff65652287f | -2.95087 | -47.31213 | 2025-10-17 04:17:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4fefd338-ea9c-3d3c-8d55-a698df7ce014 | -3.61421 | -41.58668 | 2025-10-17 04:17:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| ba500aba-cade-3c3a-a4ff-5cb2a9dc07bc | -2.74048 | -49.39116 | 2025-10-17 04:17:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 4aeab8b3-4a7d-3664-a8f8-4608e540afba | 1.09974 | -51.1471 | 2025-10-17 04:17:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 45f8f676-5f8c-36e9-9ced-e73a4d3aef45 | -3.97497 | -40.86309 | 2025-10-17 04:17:00 | NOAA-21 | IBIAPINA | CEARÁ | Brasil | 2305308 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 01d286e1-4df5-37c1-a45d-28b4c2e2c22d | -3.2373 | -42.07183 | 2025-10-17 04:17:00 | NOAA-21 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 43f3caf1-dc43-32e1-8783-dd0e0801a576 | -0.90436 | -47.54446 | 2025-10-17 04:17:00 | NOAA-21 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6c96e9ca-e8bd-3c9d-95c0-10881ce627ce | 1.83577 | -55.69901 | 2025-10-17 04:17:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 4c59e557-2601-3032-890b-078ad0a75c66 | -3.23624 | -45.97878 | 2025-10-17 04:17:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1e5e879d-e175-349e-9272-3eee9eb8f840 | 0.327 | -51.36246 | 2025-10-17 04:17:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 607448b0-f9fd-3fce-9e0a-26a56fbf2b3f | 1.72999 | -55.79465 | 2025-10-17 04:17:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9dfdb462-d4b7-3592-bf93-80519e900688 | -3.97557 | -42.49374 | 2025-10-17 04:17:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 3cbb7f11-1894-3b98-a55f-7b1822fc8235 | -2.71007 | -49.41032 | 2025-10-17 04:17:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 313039d3-9cb2-3f8c-9fef-4b70bc8a5861 | -3.23858 | -45.96389 | 2025-10-17 04:17:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 159a0443-3d82-3aea-be2e-e03eadc42ad5 | -0.89982 | -47.54857 | 2025-10-17 04:17:00 | NOAA-21 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| dd57330b-afaf-3d46-9fcf-8b4697bdd609 | 1.04067 | -51.09503 | 2025-10-17 04:17:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c48bf6be-f867-338b-aa97-fd2fea769a12 | 1.01906 | -51.15791 | 2025-10-17 04:17:00 | NOAA-21 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 3.0 |
| efa1455e-ea79-390f-8f23-3c4e44e1344a | -3.28015 | -40.88987 | 2025-10-17 04:17:00 | NOAA-21 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 4066956e-8586-3614-822e-75db3902a333 | -2.94722 | -47.31152 | 2025-10-17 04:17:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6484d740-ff32-3d97-9b17-cd1935f3cec7 | -3.23741 | -45.9713 | 2025-10-17 04:17:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c79e9f7e-2974-3755-bf0c-fc2399b7dd47 | -2.78174 | -48.723 | 2025-10-17 04:17:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 170da02b-ee8a-3a3d-b20c-5a86344e6feb | -3.34643 | -42.15997 | 2025-10-17 04:17:00 | NOAA-21 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Caatinga | 2.0 |
| b910fd79-28fe-36a4-a28c-b943bb067f93 | -3.29562 | -43.23747 | 2025-10-17 04:17:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f5127e89-4e52-39ad-9474-c10669c16225 | -3.238 | -45.9676 | 2025-10-17 04:17:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dec6fd67-9655-3176-91e2-75036d4d2c72 | -3.2334 | -45.9745 | 2025-10-17 04:17:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 76305989-a5e8-35fe-aed1-3fcf4a8f6d34 | -2.74589 | -49.38425 | 2025-10-17 04:17:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 614b1cad-d44d-3d1a-9b61-c922ea5c98c4 | 0.33201 | -51.36167 | 2025-10-17 04:17:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 2f9e7605-7990-34d5-9da2-008b1f5f6df4 | 1.79937 | -55.931 | 2025-10-17 04:17:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 8729c1a8-d433-3f42-a30b-7e3fab550d7a | -2.29647 | -47.9911 | 2025-10-17 04:17:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8675df28-6d0c-3207-9b0f-267f076a540c | 1.82839 | -55.71064 | 2025-10-17 04:17:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 1b35829e-d75c-3d6e-92a8-a98323175c8f | -3.24543 | -45.96496 | 2025-10-17 04:17:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1735c448-74d5-37a1-a4d4-03696c268e4b | 1.09885 | -51.14138 | 2025-10-17 04:17:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f197e53c-6632-33ce-91f3-bd54445a4fbb | 1.03613 | -51.09867 | 2025-10-17 04:17:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7e293526-6fae-3e96-99a4-4f0fb4f6cd31 | -3.98964 | -42.49221 | 2025-10-17 04:17:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 1153fc9c-7c25-32c3-8923-fc8cee88f95c | -3.24309 | -45.97984 | 2025-10-17 04:17:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b7c30a92-f5af-39c7-9a28-893ffee8dc0e | -2.79752 | -48.9408 | 2025-10-17 04:17:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c185ca21-4260-3fa2-ba38-bea99a2c7da8 | -3.60595 | -41.61691 | 2025-10-17 04:17:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 43734765-6165-3786-83dd-2b4ad0b79e5a | 1.739 | -55.77491 | 2025-10-17 04:17:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1cec9e5b-8d74-30b0-a9a8-bbab5d279359 | -3.6264 | -42.77328 | 2025-10-17 04:17:00 | NOAA-21 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| f762f334-1bc8-3f20-bda4-7a6e5712ac2d | 0.34067 | -51.35135 | 2025-10-17 04:17:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| eea3e9b9-a874-3472-bdfd-aea0b2faac05 | -2.60363 | -45.0243 | 2025-10-17 04:17:00 | NOAA-21 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3b518ce0-d93a-339e-9b37-1dbcf2b4800e | -3.24485 | -45.96866 | 2025-10-17 04:17:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 460ae44f-858a-3889-bde8-e3d54acb753c | 1.78475 | -55.92721 | 2025-10-17 04:17:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| eca4dec1-8ed5-3f5e-831c-fd76580758a7 | -3.24084 | -45.97184 | 2025-10-17 04:17:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e273c762-e82c-3bdf-843c-30b294238b19 | -3.98177 | -42.4984 | 2025-10-17 04:17:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c0fc97ce-43f2-3afd-acbe-ea7cf31bd700 | -3.242 | -45.96443 | 2025-10-17 04:17:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e4150bd6-15e3-3447-a058-3824d74c704b | 0.33611 | -51.35505 | 2025-10-17 04:17:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dd9d3649-b0a4-3e6e-86d2-8f74eadfda8a | -3.45025 | -41.84998 | 2025-10-17 04:17:00 | NOAA-21 | CAXINGÓ | PIAUÍ | Brasil | 2202653 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 65341a51-16ae-3c84-a0c0-da448c7fc304 | -3.2471 | -45.97665 | 2025-10-17 04:17:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5fe630b2-f882-34a5-a206-7e588a1b3548 | -3.24651 | -45.98038 | 2025-10-17 04:17:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 695704b4-8928-3cec-8acf-01ab86d7eb80 | -2.44441 | -52.25261 | 2025-10-17 04:17:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 11afaf9b-104a-32de-93ed-cef4208ab3ba | 0.1306 | -51.42046 | 2025-10-17 04:17:00 | NOAA-21 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 546f68a9-2236-3a2e-af53-b2314ea36ff2 | -3.97951 | -42.49065 | 2025-10-17 04:17:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 9c0ad673-7bf7-30de-b4e3-899b85ce1a31 | 0.87515 | -51.12306 | 2025-10-17 04:17:00 | NOAA-21 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 6.8 |
| af162de9-8dbb-32d2-8fbe-288538d944fb | -3.98682 | -42.48808 | 2025-10-17 04:17:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| fcb57278-dae3-3070-95cd-0b18d2a1e7e0 | 1.78293 | -55.9215 | 2025-10-17 04:17:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 5c56debb-e1a3-3b31-bbdd-46b8beed1a8b | 0.3311 | -51.35583 | 2025-10-17 04:17:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 5.6 |
| bfe8d390-d9a6-3fb7-ad14-81136c3c0d55 | 1.79066 | -55.91984 | 2025-10-17 04:17:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 22c988cc-e5fd-3373-ab48-4832f6535aa8 | -2.74527 | -49.38803 | 2025-10-17 04:17:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| fbfa0400-dde7-3cb3-9b88-45115cee5821 | -1.49863 | -47.81167 | 2025-10-17 04:17:00 | NOAA-21 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7c578d55-9db0-3d3f-99fa-14cd9f151063 | -2.70947 | -49.41416 | 2025-10-17 04:17:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5d1adfaf-c444-3121-b922-ca9d68bb71ab | 1.03569 | -51.09577 | 2025-10-17 04:17:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fd6f34d9-c381-3fa2-ba72-f9c2015fa6ec | -3.24071 | -42.07234 | 2025-10-17 04:17:00 | NOAA-21 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e2710d96-4273-31a7-98a3-2f02040b7810 | -3.49217 | -44.09232 | 2025-10-17 04:17:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f9608a6b-c5f7-39b1-9e9f-ba567c010d6f | 0.87062 | -51.12665 | 2025-10-17 04:17:00 | NOAA-21 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6a305739-aa63-3ec2-a639-83094834b007 | 1.84165 | -55.69199 | 2025-10-17 04:17:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 17929f31-e576-30db-80f2-9c4b83764390 | -3.24768 | -45.97292 | 2025-10-17 04:17:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a1f148a2-de71-3f24-b2c0-8f4b50ae1c0c | -3.5887 | -42.83979 | 2025-10-17 04:17:00 | NOAA-21 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 13a8fded-8b9a-333b-b64b-30a8e5512380 | -3.03606 | -44.48146 | 2025-10-17 04:17:00 | NOAA-21 | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README36.md)
