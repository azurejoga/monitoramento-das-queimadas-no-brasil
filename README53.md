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
| 1a38392a-21a9-3519-a312-015a515b42c5 | -6.79503 | -59.44592 | 2026-08-18 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9e3cb795-e903-3ef1-8d23-63b7328f9c42 | -6.85367 | -58.98091 | 2026-08-18 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2f8aabc0-2443-3a1e-a89e-f1f96437738f | -6.86349 | -56.75986 | 2026-08-18 05:42:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6fc597ae-fd53-3a7f-a70c-ed14e824eb49 | -6.71166 | -58.93438 | 2026-08-18 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c169ad41-6671-3ac0-abfe-cd7577feec0b | -6.79013 | -59.44933 | 2026-08-18 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 92e9a309-83b0-3465-9b30-8bd6f22f7560 | -2.3269 | -60.06395 | 2026-08-18 05:42:00 | NOAA-21 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8fd188d6-2cd0-3359-b1e0-a26c3e80c71c | -7.39427 | -55.48359 | 2026-08-18 05:42:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c2693b44-2ce2-33dd-88ec-4b25f118385a | -6.89437 | -59.00651 | 2026-08-18 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ef9d6bd5-26d1-3fb4-8834-b61a76954553 | -7.53363 | -55.58508 | 2026-08-18 05:42:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b1875c45-11cb-3d68-9daa-5a1be838652b | -7.3767 | -55.48488 | 2026-08-18 05:42:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bdceabc9-0403-3420-aa5a-559dbd20d435 | -6.39995 | -54.94188 | 2026-08-18 05:42:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 59791486-0732-36ea-a11c-88e097342ac9 | -6.85364 | -59.01247 | 2026-08-18 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 2d6d8854-be6a-3ce3-9c66-f2b8f6fa1359 | -4.20827 | -59.99495 | 2026-08-18 05:42:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9029844e-aa36-3131-8808-834d1cb124cc | -6.4005 | -54.93781 | 2026-08-18 05:42:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 612d0ffe-36de-32ab-8bcf-30a8fa483c06 | -7.3705 | -55.48793 | 2026-08-18 05:42:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 25dd82ea-9743-3d9d-891c-b24ab380af03 | -6.85048 | -59.00301 | 2026-08-18 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 433e4292-bf82-33e9-8a2d-7d51f04d4627 | -6.68804 | -59.06897 | 2026-08-18 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2527c7d4-a59f-30b4-9d60-c1e4976b54df | -3.09882 | -61.21218 | 2026-08-18 05:42:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| aa4bea68-1a18-30ff-98d6-7e4ae6d5535b | -6.95918 | -59.02954 | 2026-08-18 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 21d8aba2-5b45-3c6e-b5a9-46bffb7da7b8 | -6.75949 | -59.16692 | 2026-08-18 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 6a58286c-3337-3b18-9c9f-77ead1e2b9f8 | -6.74457 | -59.17747 | 2026-08-18 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 09d59396-9104-35bd-bad8-e1bf3a6a79a6 | -6.84602 | -59.00243 | 2026-08-18 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| b4cee496-7c21-373e-a670-4ccce8c563e3 | -6.65003 | -58.95259 | 2026-08-18 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5235ad70-1021-3317-9cff-5cf211e0b13f | -6.95726 | -59.04278 | 2026-08-18 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b7c140a4-704e-3e41-96e2-8d8d8be7f2a4 | -6.60312 | -58.97066 | 2026-08-18 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d6b0ac3c-5994-3472-9fa1-df66210e5629 | -6.74755 | -59.15611 | 2026-08-18 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f531f525-3f5f-37f4-8595-c2d1ed5dc5d2 | -7.07116 | -56.65691 | 2026-08-18 05:42:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9c5e6334-213f-36c7-b9c4-1fc69b4c84cf | -6.85429 | -59.00802 | 2026-08-18 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 135f36b4-bf41-38b1-9bf7-b6b02ac721c0 | -6.84538 | -59.00689 | 2026-08-18 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.0 |
| eafa7f51-4895-34f9-8158-4412e71266f8 | -6.84474 | -59.01131 | 2026-08-18 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 48f71aa4-ddff-3310-a089-135331988372 | -6.76741 | -59.45439 | 2026-08-18 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e96e4e18-9459-3d39-9ab9-e6e6fbda1e96 | -6.85493 | -59.00357 | 2026-08-18 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 175f17d6-52b0-3ea5-8fec-45806dcf7463 | -7.38755 | -55.49056 | 2026-08-18 05:42:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6282642b-53e4-35d8-85c5-b4c778ca4533 | -6.74695 | -59.16043 | 2026-08-18 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 23cd8f6a-cd20-3980-9d33-fbda000e808a | -6.85695 | -59.01461 | 2026-08-18 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 112986bd-4564-37f6-997b-c9066d0a3f67 | -6.86883 | -56.41516 | 2026-08-18 05:42:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ef90ebd4-5993-33e3-995c-9a142ab93b8f | -6.84095 | -59.00616 | 2026-08-18 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 00934ebd-6989-3c42-8b9a-0950384b6690 | -6.79073 | -59.44523 | 2026-08-18 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| de67d78d-9d83-3172-bdf0-b41a20a02f98 | -7.09848 | -55.47399 | 2026-08-18 05:42:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bb5431ba-6bb2-371f-95a6-4b70a2347a60 | -6.86308 | -56.76273 | 2026-08-18 05:42:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6564e6e1-1b39-36c0-a460-b29c53b36b2c | -6.75448 | -59.17071 | 2026-08-18 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 8bdc1708-eea0-319d-8687-1fae73d986bc | -6.75631 | -59.15759 | 2026-08-18 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 83110eee-6151-31d4-8a41-b1d46e493055 | -6.73997 | -59.14608 | 2026-08-18 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5a290345-113e-396d-a66c-7cc1941d40ac | -6.95537 | -59.02447 | 2026-08-18 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 2f50b464-7e87-39d8-aeef-6850bc02deca | -6.77602 | -59.45568 | 2026-08-18 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7686c570-b46a-3a04-85d1-89925ffc1962 | -6.96223 | -59.03191 | 2026-08-18 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c6d05fdb-ea18-335d-8a7c-e09ca0d96b80 | -7.38858 | -55.48271 | 2026-08-18 05:42:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f18620fb-d7e1-3a72-a12c-b7b5304d3520 | -6.76072 | -59.15814 | 2026-08-18 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| cf686fc4-9b28-3bbe-98fc-ececf31535db | -6.64623 | -58.95482 | 2026-08-18 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c98e1ddd-2a78-38af-a126-defddbd8c78a | -6.77112 | -59.45918 | 2026-08-18 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 414ed7a0-86c6-39b3-b7f3-f6a4a499c928 | -6.40688 | -54.93452 | 2026-08-18 05:42:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 42c74ac6-058e-3333-a229-5e644fa1c78d | -6.70592 | -58.94274 | 2026-08-18 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2df65078-eabb-3efb-87c6-43f567dcfc2a | -7.099 | -55.47009 | 2026-08-18 05:42:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a1a47550-1496-37ca-af36-e07e597a121c | -5.49452 | -60.13912 | 2026-08-18 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 15f8c119-cfe0-3c14-9118-c7d411e45055 | -7.37618 | -55.4888 | 2026-08-18 05:42:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 59c12cbf-9473-3df6-8aab-ffc7aefc69e5 | -6.03352 | -57.80918 | 2026-08-18 05:42:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c38a5354-3ee5-3c97-9d55-8ea2d2ad4432 | -6.72182 | -58.9269 | 2026-08-18 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1ce12343-1f5e-30fb-ab69-438375b04d89 | -6.9579 | -59.03836 | 2026-08-18 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 27d9ae63-098d-3854-a909-34e2d9c1871b | -6.95982 | -59.02512 | 2026-08-18 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 13.8 |
| ed57b431-dcf6-33cf-b4bd-e98d47f4d866 | -6.70405 | -58.95598 | 2026-08-18 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2fac2e31-467a-3a50-b29d-0dc280f9e71a | -6.95473 | -59.02892 | 2026-08-18 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| fc7ae220-969d-3a42-a3c4-6188c1920f64 | -6.69574 | -58.95051 | 2026-08-18 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7073ee8f-5235-3d9e-a516-cd7aa77cb67c | -7.07074 | -56.6599 | 2026-08-18 05:42:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b0d3465b-5c7a-3453-8009-388414e29663 | -6.70145 | -58.94224 | 2026-08-18 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9b7065d3-09c1-3972-ab4b-de39a86db32b | -6.76682 | -59.45847 | 2026-08-18 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a410c05e-8259-347e-8f20-f9442a916247 | -6.8595 | -56.75938 | 2026-08-18 05:42:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 65a0f4dc-5f28-338e-922e-08e02db6f874 | -6.84856 | -59.01625 | 2026-08-18 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 16a91126-51b9-32b8-956b-0084fd913d09 | -6.84795 | -58.98909 | 2026-08-18 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d899a809-2d53-3bbf-88b7-10ab8c59ea55 | -6.10662 | -57.74172 | 2026-08-18 05:42:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e9920eb9-7d80-3d48-9142-7eb79a688457 | -6.96362 | -59.03017 | 2026-08-18 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2420485e-eeb7-3036-8835-0a71f25758d0 | -6.75509 | -59.16634 | 2026-08-18 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 29192838-0c69-3410-96be-13a84e4bf6be | -6.78583 | -59.44866 | 2026-08-18 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 93303cc6-192c-301a-a781-e10fc5bb20b8 | -6.87323 | -56.42252 | 2026-08-18 05:42:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 62f4150a-459b-3842-9145-6037325fae87 | -6.74517 | -59.1732 | 2026-08-18 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 6b8834e3-06b6-306d-bf91-20793d9e94cf | -5.1453 | -56.28227 | 2026-08-18 05:42:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 44181eea-e23c-36ef-9c03-0a3388c04e5e | -6.11213 | -57.73729 | 2026-08-18 05:42:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ceaf1bb9-9160-3cf4-9e91-f42bae4f6814 | -7.38238 | -55.48576 | 2026-08-18 05:42:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ba213465-32ba-3a02-99e7-b6dda63b17bc | -6.7557 | -59.16194 | 2026-08-18 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 66b49bb8-d195-3570-94f3-cba65bb73549 | -6.68743 | -59.0733 | 2026-08-18 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b456fbd2-3fa9-3b10-8ca8-4d77ca99819b | -6.74815 | -59.15181 | 2026-08-18 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e7c02b21-2e31-3dfc-9521-aac3cf4401e3 | -6.70082 | -58.94667 | 2026-08-18 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| bcec2014-1a6c-336c-94c7-c037891a57aa | -6.71674 | -58.93063 | 2026-08-18 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 87136263-686e-33b6-b4fa-ee84e71ef912 | -6.76253 | -59.45775 | 2026-08-18 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 10885397-44a1-398b-9c1b-5323706ff02a | -4.20427 | -59.99433 | 2026-08-18 05:42:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2133e058-fa6d-353a-9349-2eafcc68a9b6 | -7.39375 | -55.4875 | 2026-08-18 05:42:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ca674e9a-6eef-3de4-9a8b-f1393e4ad0c9 | -7.36432 | -55.49087 | 2026-08-18 05:42:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8c1388b2-dfc6-3e53-ac21-0603ca7900f7 | -6.73973 | -59.1472 | 2026-08-18 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 51bd29ec-b6aa-3fb4-8f0c-6ba140a5984e | -6.70719 | -58.9338 | 2026-08-18 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4b1d951b-c1f4-37a7-8999-c503bbc52e14 | -6.70655 | -58.93828 | 2026-08-18 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 57f25df7-2b4b-396a-8465-f723c7338991 | -6.95854 | -59.03395 | 2026-08-18 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 02d63cf3-6716-3c43-8f7d-2ff4edcbcbe6 | -3.55416 | -62.0783 | 2026-08-18 05:42:00 | NOAA-21 | CODAJÁS | AMAZONAS | Brasil | 1301308 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f8565e9a-37fa-3b0c-afb8-9c444f2f5561 | -6.85304 | -58.98529 | 2026-08-18 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c96b5d29-6af2-31ef-9f66-dfd66ed87280 | -6.74398 | -59.18174 | 2026-08-18 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 039e032b-4da4-3ecc-9d5d-897e6342fc71 | -8.10343 | -61.34731 | 2026-08-18 05:44:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e5efaeef-8b1a-3076-9212-8a1a63b967d5 | -10.06881 | -60.50431 | 2026-08-18 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 36485cdf-c9a7-3186-b53b-8efeb1b45ced | -8.73188 | -62.90226 | 2026-08-18 05:44:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f276e3a4-8b33-3d04-a628-c9365bda7967 | -8.64011 | -54.7058 | 2026-08-18 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f8f5f876-bbdb-387d-aca5-4e4995bb2bbd | -8.58066 | -54.73481 | 2026-08-18 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 39.1 |
| 627ebc42-3f4d-330e-8a5f-1ee1a272d4d2 | -8.55441 | -55.30856 | 2026-08-18 05:44:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 425bf2e8-e125-31ae-8c36-6619bdbf2cfb | -12.46278 | -54.19222 | 2026-08-18 05:44:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |


[Clique aqui para ver as próximas entradas](README54.md)
