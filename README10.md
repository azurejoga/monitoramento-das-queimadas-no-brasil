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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a1e155cb-08d0-3571-a8ca-9e3f3f44c1a6 | -3.6102 | -47.531101 | 2024-10-05 00:24:37 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e241db59-90b1-39e1-ba07-47d5b01314aa | -3.596 | -47.513699 | 2024-10-05 00:24:37 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2fefec39-19a9-3ab7-9edd-2a444894ffc7 | -3.5982 | -47.523499 | 2024-10-05 00:24:37 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6b095289-66b4-3f36-b5bf-91931558af60 | -3.271 | -46.3456 | 2024-10-05 00:24:38 | METOP-C | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 28c28aaa-0a15-34d7-8791-4c7d5c119271 | -3.2612 | -46.347801 | 2024-10-05 00:24:38 | METOP-C | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 5a8e460b-77c3-31b2-911a-ed522d272258 | -3.3103 | -46.974899 | 2024-10-05 00:24:40 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d4bc5a0d-4f2d-32d1-a2fe-402393698257 | -3.3124 | -46.983898 | 2024-10-05 00:24:40 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 39e1123a-80bd-3e70-b30d-77d06f2c243b | -3.3087 | -47.013199 | 2024-10-05 00:24:40 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7bcfd836-6dd4-32fa-9755-ea3d28945605 | -3.3749 | -49.224899 | 2024-10-05 00:24:47 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bec12582-24cf-372a-8071-8e357c8f7fc0 | -3.3777 | -49.237499 | 2024-10-05 00:24:47 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 81fff312-806f-3caa-b3d1-bf18738826c6 | -2.733 | -46.785801 | 2024-10-05 00:24:48 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9bb8eca0-a8f5-31cc-90a2-939bcdf839d0 | -2.7135 | -46.7901 | 2024-10-05 00:24:49 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dfe76c72-ef20-303e-8018-4af1365d0f34 | -3.3032 | -49.4538 | 2024-10-05 00:24:49 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| af8a6006-68c3-37b9-af0d-4fd939a4ca41 | -3.3061 | -49.466702 | 2024-10-05 00:24:49 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e4b63739-f858-310e-b6f5-fb07b6f192b7 | -3.2935 | -49.455898 | 2024-10-05 00:24:49 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cbb130e6-2418-3edf-b710-b793d00f8fed | -3.2373 | -49.387299 | 2024-10-05 00:24:50 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 317dd7e4-385c-32ab-936b-d2182d4c3124 | -3.2401 | -49.400101 | 2024-10-05 00:24:50 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5d211eeb-efdc-3644-84ec-18a5283cd8ba | -3.1183 | -48.948502 | 2024-10-05 00:24:50 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b89a1517-45f8-3ca6-95d9-3eac56d4246e | -2.6157 | -46.903301 | 2024-10-05 00:24:51 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0d3bc615-c556-3639-a235-30ba731e9bfb | -3.8322 | -52.3386 | 2024-10-05 00:24:51 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f6605e9b-a3c9-3e82-8885-82a5422849b5 | -2.3553 | -46.119301 | 2024-10-05 00:24:52 | METOP-C | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9ece3f72-accb-391a-8eec-7191cdf9d6f5 | -2.9018 | -48.896702 | 2024-10-05 00:24:53 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5b8b2051-c74b-3a01-957b-f2057e5694fe | -2.9044 | -48.908401 | 2024-10-05 00:24:53 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4d977afb-7c88-3860-88d0-cf0917f5522e | -2.892 | -48.898899 | 2024-10-05 00:24:54 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9438206c-ac33-3f6d-9062-4fb980fb624a | -2.8946 | -48.910599 | 2024-10-05 00:24:54 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e3b68a4c-3210-321b-86f5-16c0a20385ec | -2.8698 | -48.891399 | 2024-10-05 00:24:54 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f934a579-afe8-372f-9d5a-f7e0e2602d22 | -2.8725 | -48.903099 | 2024-10-05 00:24:54 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c95e12c2-ac3f-3d0b-95a7-4eb3b7d7224d | -2.7759 | -48.565899 | 2024-10-05 00:24:54 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 26bcd15b-b945-3a5c-8958-e20c5a146d0e | -2.7785 | -48.577 | 2024-10-05 00:24:54 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 29ba1b66-12e2-35c7-8b1d-c8f1e352d918 | -2.7662 | -48.568001 | 2024-10-05 00:24:54 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2c279fca-350c-3da1-806b-08f19961b7b6 | -2.7687 | -48.579102 | 2024-10-05 00:24:54 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6d1e7edc-aa8d-3f1c-bcc9-ac2b1a31460a | -3.2181 | -50.809898 | 2024-10-05 00:24:55 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2d2d8e15-6f81-3182-b104-50744cd127e7 | -3.2217 | -50.825901 | 2024-10-05 00:24:55 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 01b24cde-1913-318a-94f1-dd395cd7ffa7 | -2.7096 | -48.817101 | 2024-10-05 00:24:56 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ef4cfd7d-2f2a-3086-a5ef-9e3c760f15d5 | -2.7122 | -48.828602 | 2024-10-05 00:24:56 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f68ceda7-3bf9-3db8-9de2-5d0858014954 | -2.7252 | -48.886398 | 2024-10-05 00:24:56 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 65e33a86-57a9-3545-b179-d49834fc09dd | -2.2259 | -46.726398 | 2024-10-05 00:24:56 | METOP-C | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b85f2f9f-0789-34c6-8df8-6608dc97fb38 | -2.5687 | -49.055901 | 2024-10-05 00:24:59 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cc01fa95-694d-3831-ae40-8c09405f553f | -2.5589 | -49.058102 | 2024-10-05 00:25:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 46cc893f-1b85-34df-a1ac-e37ac69238a4 | -2.5616 | -49.07 | 2024-10-05 00:25:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 849ee613-bcc2-34f3-b082-7c55893299b2 | -2.8839 | -50.684502 | 2024-10-05 00:25:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8441db13-d456-342e-b0a9-78b42fed547a | -2.8874 | -50.700001 | 2024-10-05 00:25:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d839c4f8-c462-3a4f-aef1-e8fc7f43f311 | -2.8909 | -50.715599 | 2024-10-05 00:25:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5672387a-d4fc-35d2-ab96-72a369bedb81 | -2.7868 | -50.297501 | 2024-10-05 00:25:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d33b598f-7346-3b24-8613-7e0743e92684 | -2.79 | -50.312 | 2024-10-05 00:25:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9dabe969-36e6-3c20-916c-203caf6f3a60 | -2.8741 | -50.686699 | 2024-10-05 00:25:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ed6e7cb9-8d56-372c-a71f-2f8c754cd593 | -2.8776 | -50.702202 | 2024-10-05 00:25:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f942d268-94d8-313c-b75b-cc7f90336b84 | -2.0181 | -47.983898 | 2024-10-05 00:25:04 | METOP-C | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ac186396-411c-3e5c-ba8e-25db85f12c6c | -2.0061 | -47.9762 | 2024-10-05 00:25:05 | METOP-C | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f5cc70ec-f110-3b1a-8dc8-1be3264cd1e8 | -2.0083 | -47.986099 | 2024-10-05 00:25:05 | METOP-C | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a88e1cdd-87ea-3158-8ab7-19ff96e92c63 | -2.1907 | -48.835098 | 2024-10-05 00:25:05 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1c6488f9-f656-35c9-834f-87e7d65e9b1b | -1.1942 | -46.5935 | 2024-10-05 00:25:13 | GOES-16 | AUGUSTO CORRÊA | PARÁ | Brasil | 1500909 | 15 | 33 | nan | nan | nan | Amazônia | 87.5 |
| 4fb73bf1-b822-3cfb-acb5-8a965140cceb | -1.1942 | -46.5714 | 2024-10-05 00:25:13 | GOES-16 | AUGUSTO CORRÊA | PARÁ | Brasil | 1500909 | 15 | 33 | nan | nan | nan | Amazônia | 48.7 |
| 73806ea6-e88c-3084-b839-a994b943fb83 | -1.2663 | -47.6643 | 2024-10-05 00:25:13 | GOES-16 | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 48.0 |
| 6e42ff60-b767-3b64-abd4-525263463a05 | -1.1922 | -46.571301 | 2024-10-05 00:25:13 | METOP-C | AUGUSTO CORRÊA | PARÁ | Brasil | 1500909 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a16773fd-72dc-3ad5-a258-a94b1a85156f | -1.1941 | -46.579399 | 2024-10-05 00:25:13 | METOP-C | AUGUSTO CORRÊA | PARÁ | Brasil | 1500909 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5f442fb6-30fb-37dc-8851-44302d4d9cb5 | -1.1959 | -46.587601 | 2024-10-05 00:25:13 | METOP-C | AUGUSTO CORRÊA | PARÁ | Brasil | 1500909 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f4fbbbd6-5fa1-3c09-b805-235e8796219b | -1.1824 | -46.573399 | 2024-10-05 00:25:13 | METOP-C | AUGUSTO CORRÊA | PARÁ | Brasil | 1500909 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9b362945-9b0f-3442-bf15-a37b7c60dd22 | -1.1843 | -46.581501 | 2024-10-05 00:25:13 | METOP-C | AUGUSTO CORRÊA | PARÁ | Brasil | 1500909 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 834cdfb8-ee59-3704-b0ca-26448e0f7ae0 | -1.1861 | -46.589699 | 2024-10-05 00:25:13 | METOP-C | AUGUSTO CORRÊA | PARÁ | Brasil | 1500909 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 09d7a95e-95fc-3960-8bef-e79f7fc677dd | -1.2533 | -47.648998 | 2024-10-05 00:25:16 | METOP-C | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0e2843ce-1de7-3329-91b5-1153bc95776b | -1.2554 | -47.658298 | 2024-10-05 00:25:16 | METOP-C | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7a5de35f-c94c-3deb-bcb4-dbf8fadd02d8 | -1.2575 | -47.667599 | 2024-10-05 00:25:16 | METOP-C | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5affdb0b-6d6c-3fec-a5c2-e919300671ac | -2.8829 | -50.7147 | 2024-10-05 00:25:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 79.3 |
| 03801f09-5e82-3c63-99d8-8c3dcdae9d80 | -2.9014 | -50.7142 | 2024-10-05 00:25:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 115.8 |
| 22820963-a876-3ccf-8f47-660cb4a52dce | -2.9015 | -50.6933 | 2024-10-05 00:25:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 72d8072f-db1b-3111-ad0a-d9326e057303 | -3.239 | -49.3986 | 2024-10-05 00:25:24 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 162a25c8-a3c3-3392-bf54-42160befa6e0 | -3.2575 | -49.398 | 2024-10-05 00:25:24 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 50.1 |
| e5cba8e0-2563-3dc4-9f32-a763ff38de23 | -3.2899 | -50.4516 | 2024-10-05 00:25:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 0bcf3fc1-7ed5-33c6-9229-d26f9b2238d4 | -3.3083 | -50.4719 | 2024-10-05 00:25:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 112.2 |
| be5a3236-8260-375a-a1be-b08f8e0073c0 | -3.3084 | -50.451 | 2024-10-05 00:25:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 101.7 |
| 8c221943-872a-3d2d-a431-f8b8f904a99f | -3.3127 | -49.4599 | 2024-10-05 00:25:25 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 36.1 |
| f2e33431-57ff-32d4-9255-82e5fcc9fc12 | -3.5994 | -47.5359 | 2024-10-05 00:25:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 301d7bb4-5540-370c-a5f7-129088cafab0 | -3.5995 | -47.5142 | 2024-10-05 00:25:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 92.0 |
| a386132a-cc1f-382a-a501-73bf3620a505 | -3.618 | -47.5352 | 2024-10-05 00:25:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 105.0 |
| 7573dad6-9490-3231-a913-0e73906625e8 | -3.6181 | -47.5134 | 2024-10-05 00:25:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 143.1 |
| 31b0b93f-7c4a-35f8-a509-84dab951654d | -4.0148 | -43.2408 | 2024-10-05 00:25:29 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 61.2 |
| d07c2154-944c-3ff6-909c-9a8603bb30f3 | -4.0608 | -47.9511 | 2024-10-05 00:25:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 83264764-002d-320d-9033-83acbdcdf39b | -4.0793 | -47.9719 | 2024-10-05 00:25:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 80.9 |
| 3d78eef6-8e79-34f1-b538-fce4515e02ee | -4.0794 | -47.9502 | 2024-10-05 00:25:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 241.8 |
| 9923c3f2-32d5-36c3-956e-0d39ea817414 | -4.0795 | -47.9285 | 2024-10-05 00:25:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 78.6 |
| 36a8b5c4-9051-3108-b6e7-568ed9d7f449 | -4.0979 | -47.9494 | 2024-10-05 00:25:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 71.9 |
| d1a479de-0ce6-328d-8957-bbe24d40dd07 | -5.3911 | -46.4322 | 2024-10-05 00:25:36 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 82.3 |
| b9ce11ee-9758-3ec4-902f-93b4f4385ebb | -0.2439 | -48.7626 | 2024-10-05 00:25:36 | METOP-C | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 30ad2316-044e-3089-9040-165e6f8c721e | -5.8214 | -44.1426 | 2024-10-05 00:25:39 | GOES-16 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 136.0 |
| 488aa86c-59a8-3cd7-ae8d-0bbb8da95a99 | -5.8216 | -44.1196 | 2024-10-05 00:25:39 | GOES-16 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 180.8 |
| 1876bad6-19eb-3fc3-a66f-ee1b0e85eec8 | -6.9514 | -59.0666 | 2024-10-05 00:25:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 82.7 |
| 258ae813-686f-3768-b94c-00356e5d275f | -7.0233 | -59.3918 | 2024-10-05 00:25:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 91c6c345-a64d-3f31-a4b1-f6b4c7bb5a2a | -7.1346 | -59.3099 | 2024-10-05 00:25:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 85.0 |
| 1c698000-d4ef-3e16-9582-123bb1d50cfb | -7.1347 | -59.2906 | 2024-10-05 00:25:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 82.8 |
| a27c7e57-0609-35e0-b475-d0385b35db0b | -7.7362 | -49.2297 | 2024-10-05 00:25:50 | GOES-16 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 208.6 |
| 75592086-cc68-37ca-afa6-a2dda092b52b | -7.7364 | -49.2082 | 2024-10-05 00:25:50 | GOES-16 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 235.0 |
| dd88ca60-fc29-3279-b70e-19e09be9441c | -7.7549 | -49.2282 | 2024-10-05 00:25:50 | GOES-16 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 169.8 |
| c646beb2-217f-3ece-834d-28bfc068158d | -7.7551 | -49.2067 | 2024-10-05 00:25:50 | GOES-16 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 192.8 |
| e0410de5-f0d9-39e9-9b95-f6408cf45537 | -7.7736 | -49.2267 | 2024-10-05 00:25:50 | GOES-16 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 41.1 |
| 029b3399-1722-3f1c-bbed-bc2f4c025e9a | -7.7738 | -49.2052 | 2024-10-05 00:25:50 | GOES-16 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 45.0 |
| 0dbc6387-e5cf-3d5b-9db8-bd643aa15a42 | -8.2323 | -61.2205 | 2024-10-05 00:25:53 | GOES-16 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 93.7 |
| ad64390b-d5d5-3a81-93af-9ebe0269275c | -8.7655 | -44.8106 | 2024-10-05 00:25:55 | GOES-16 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 1d4d3f72-1cf3-3195-8cdb-201dfe08c3bf | -8.6367 | -49.11 | 2024-10-05 00:25:55 | GOES-16 | PEQUIZEIRO | TOCANTINS | Brasil | 1716653 | 17 | 33 | nan | nan | nan | Cerrado | 42.6 |
| 91a36fae-ceec-3531-bffa-ff9af79b99ac | -8.6555 | -49.1083 | 2024-10-05 00:25:55 | GOES-16 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 70.2 |


[Clique aqui para ver as próximas entradas](README11.md)
