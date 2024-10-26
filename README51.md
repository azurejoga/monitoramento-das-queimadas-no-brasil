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

## Dados Diários - Página 51

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5c38712c-d7c2-355e-a38d-472c6bd68302 | -7.54316 | -45.83801 | 2024-10-26 04:19:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 97ead0b2-8053-32cd-9e92-0db7cc3a30d0 | -7.54259 | -45.84156 | 2024-10-26 04:19:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ecc451a8-63a4-3eb3-b045-921ee5ea30a0 | -7.53981 | -45.83747 | 2024-10-26 04:19:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| d60407d0-6d8c-3fca-b78a-281ce6dd3970 | -7.53924 | -45.84101 | 2024-10-26 04:19:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| a94b753d-9588-39d1-8083-fabecce830bf | -7.53867 | -45.84456 | 2024-10-26 04:19:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 77acff43-11c4-32d8-b92d-379247632fe6 | -7.53646 | -45.83694 | 2024-10-26 04:19:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 30255a3b-54d2-37b0-af4b-7fe491e2d34b | -7.53589 | -45.84048 | 2024-10-26 04:19:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 6ccdc812-e2e2-392c-8aef-6f61202e4b1e | -7.53475 | -45.84757 | 2024-10-26 04:19:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a835aa45-32b3-3b58-9de4-97e1611b96e5 | -7.53448 | -45.83672 | 2024-10-26 04:19:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c3193787-8fda-314a-92f8-a9914545ff4b | -7.53418 | -45.85111 | 2024-10-26 04:19:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| fe6a8239-3d51-32e0-9f48-07d80fb055e1 | -6.50669 | -46.58635 | 2024-10-26 04:19:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 676a5086-85b4-32e3-8651-ce6d14e2f135 | -7.98961 | -46.85834 | 2024-10-26 04:19:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4810caa8-ec4e-37a7-8f02-29a0b406bbe6 | -7.89907 | -46.6842 | 2024-10-26 04:19:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 325c104a-f60a-371d-ab31-ba0089e0b5d7 | -7.89848 | -46.68789 | 2024-10-26 04:19:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 28a691cc-a7d6-339e-ad7c-ccd78d49665c | -7.89566 | -46.68364 | 2024-10-26 04:19:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 2380a7d0-a398-3cea-9c16-b83b2e28864f | -7.89506 | -46.68733 | 2024-10-26 04:19:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 79923b90-1480-38c4-8a2d-cb9c007b35e4 | -7.89224 | -46.68308 | 2024-10-26 04:19:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a5595a29-3099-3757-ba7e-69383dff7906 | -9.36266 | -46.46632 | 2024-10-26 04:19:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5136b07f-110d-3732-998f-883c46390029 | -9.36208 | -46.4699 | 2024-10-26 04:19:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9e5a2682-bff8-3a2c-8e26-e38aa9051229 | -9.26475 | -46.23056 | 2024-10-26 04:19:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 60b055b1-95c5-3ce5-a687-493042f23ed8 | -9.14377 | -47.11205 | 2024-10-26 04:19:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1c1ef3b0-b56e-3a2a-822e-60e6a474ceff | -9.14095 | -47.10774 | 2024-10-26 04:19:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5d98b8a7-5885-3337-8003-286b6df7f454 | -8.4176 | -46.99971 | 2024-10-26 04:19:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6cd843d4-f659-3cb9-a477-6b9789a72bfb | -8.76339 | -45.8916 | 2024-10-26 04:19:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 22e69089-2b46-3a73-a465-97578ea0de09 | -8.52745 | -45.6343 | 2024-10-26 04:19:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 39ea18cb-3167-3d50-ae51-ddfc52a44486 | -8.52412 | -45.63379 | 2024-10-26 04:19:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 4f77fc8a-bbda-3d25-b4ab-c51809eed001 | -8.52357 | -45.63728 | 2024-10-26 04:19:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 2b159c9f-7161-374d-8bb7-6268ca7813f9 | -8.52301 | -45.66233 | 2024-10-26 04:19:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f8676ac2-9b53-33d1-9acc-fef249050b5f | -8.52079 | -45.6548 | 2024-10-26 04:19:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 833872a5-0624-3ef5-9f5a-e73c10557dd8 | -8.09954 | -45.68819 | 2024-10-26 04:19:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 73caa517-9663-3273-8110-3a22d8be98d8 | -9.58493 | -47.12857 | 2024-10-26 04:19:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a8774d72-0dcf-3bd2-be5b-63a0110bfdd8 | -9.50811 | -46.62998 | 2024-10-26 04:19:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0da8b907-eb44-3282-81af-2991883c7514 | -9.4624 | -46.71939 | 2024-10-26 04:19:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d2860030-321c-3e6e-8de4-4039a4e7400a | -10.24593 | -46.56499 | 2024-10-26 04:19:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 1df1f187-8eab-376b-b3eb-8a818bd56e78 | -12.21565 | -47.23949 | 2024-10-26 04:19:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a1896175-34a3-32f2-a9a7-07f388cec534 | -11.94207 | -47.56581 | 2024-10-26 04:19:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d9db4b1b-1c4f-32cf-96a0-21bb9910d560 | -11.94146 | -47.56953 | 2024-10-26 04:19:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 6e85341b-589d-36ee-8ed9-4ad236dc12a7 | -11.19705 | -47.5701 | 2024-10-26 04:19:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 72ef67a2-333d-3a7e-b38f-47e8cce6a6c9 | -10.89993 | -47.5061 | 2024-10-26 04:19:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cc167405-3749-3229-ae27-5ffaade97ee4 | -10.82083 | -47.54411 | 2024-10-26 04:19:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 67339cab-1fb9-38e0-ba23-8e25f7616127 | -13.16969 | -47.90147 | 2024-10-26 04:19:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a04bfbe3-4ce6-37ab-95bb-eeef2d6bbc43 | -13.1678 | -47.91288 | 2024-10-26 04:19:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5d2ba335-8583-3fd6-9657-12e25b93da9f | -13.16629 | -47.90085 | 2024-10-26 04:19:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 74f62cb9-c87c-3b8c-916f-120ce25a3f1f | -13.16226 | -47.90402 | 2024-10-26 04:19:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 466b7b27-2d3f-3356-9678-e1c43d8ea58f | -13.0946 | -47.14271 | 2024-10-26 04:19:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 96b77c6f-fdde-30b8-b573-2f54587cc7b3 | -12.71101 | -47.6314 | 2024-10-26 04:19:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 930935f5-e71f-3d07-aaba-25c63f210313 | -12.56714 | -47.07757 | 2024-10-26 04:19:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 94fe5644-84cb-3db8-8a98-03f8124c7013 | -12.42739 | -47.37636 | 2024-10-26 04:19:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0cbe9639-4531-3a36-891f-aa17bddb5b64 | -12.33056 | -47.00892 | 2024-10-26 04:19:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3b7bab8e-4ff4-3ce1-9eb7-f32eae44657f | -12.32998 | -47.01254 | 2024-10-26 04:19:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e0b2b801-197c-3ebe-ab0a-a048d0c40ef1 | -1.7777 | -46.30822 | 2024-10-26 04:19:00 | NPP-375D | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 49a4da8c-87cf-3a32-be43-0b9a282ae86a | -1.17465 | -46.72539 | 2024-10-26 04:19:00 | NPP-375D | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0c36ef17-898a-35bd-afe6-b097cb4e9978 | -1.11597 | -46.8343 | 2024-10-26 04:19:00 | NPP-375D | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3b7c02ae-0f65-3afc-89e5-f14bf8385e55 | -6.45275 | -47.65981 | 2024-10-26 04:19:00 | NPP-375D | SANTA TEREZINHA DO TOCANTINS | TOCANTINS | Brasil | 1720002 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 74f31fdb-025e-3ad1-924d-5932e7f4fdfd | -5.6503 | -47.91338 | 2024-10-26 04:19:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f52c2484-052b-3056-82a5-6ec6ef1369a7 | -6.51805 | -47.03328 | 2024-10-26 04:19:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0780c8f6-55b2-39c9-9e69-d6b99b4c6b8e | -6.51741 | -47.03716 | 2024-10-26 04:19:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 386e91fc-4cc9-350c-a9f2-9e092b3179c8 | -6.51455 | -47.03271 | 2024-10-26 04:19:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c00428e4-c9ab-3c63-9093-a73a0bb1ae7e | -6.4671 | -46.72211 | 2024-10-26 04:19:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6d16c166-29ca-3b0e-b35a-a4f4288b0ad0 | -6.46364 | -46.72157 | 2024-10-26 04:19:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8d9b8bb4-ee60-34b6-a563-b500246b9f83 | -6.46304 | -46.72527 | 2024-10-26 04:19:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0a01c22b-dd67-31e3-9699-5f827a9f1af1 | -6.45979 | -46.98879 | 2024-10-26 04:19:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 79771115-15eb-3a57-b5df-ab4d9750c510 | -6.3826 | -47.37777 | 2024-10-26 04:19:00 | NPP-375D | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9cd99251-1a56-3f13-825b-c91cb61dda16 | -6.37904 | -47.37723 | 2024-10-26 04:19:00 | NPP-375D | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d562b67c-e74d-3470-9f6a-694d9111d519 | -6.2939 | -47.34813 | 2024-10-26 04:19:00 | NPP-375D | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bd84403b-4ceb-3607-a93a-2b22dc069782 | -6.13308 | -47.0023 | 2024-10-26 04:19:00 | NPP-375D | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 78c1ec23-310b-30b9-a647-42f9af4ecaac | -6.13246 | -47.00618 | 2024-10-26 04:19:00 | NPP-375D | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9072e1cb-9f48-3c1a-8bbc-4da208cf9d83 | -6.08631 | -47.22551 | 2024-10-26 04:19:00 | NPP-375D | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| dca8ac40-5c23-34ca-bd0a-ea235cad9b3e | -6.08277 | -47.22491 | 2024-10-26 04:19:00 | NPP-375D | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ad51b0a3-3c2b-3c16-8ca7-dbdf2df3906d | -6.02251 | -47.21514 | 2024-10-26 04:19:00 | NPP-375D | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9e9a1d2e-ca16-3df3-b047-b9da5097b33b | -5.85396 | -46.56161 | 2024-10-26 04:19:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 379714d2-283c-3e30-ba76-ddda15945edf | -5.85376 | -47.19004 | 2024-10-26 04:19:00 | NPP-375D | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5ea2c20f-ba67-3a20-82ac-7f2ef7c48630 | -5.84524 | -47.28762 | 2024-10-26 04:19:00 | NPP-375D | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| af6589f3-4ce8-3681-bda7-e29a9b5833de | -5.84168 | -47.28703 | 2024-10-26 04:19:00 | NPP-375D | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a6c0de3c-8243-3b4a-91cd-8362bf00fe14 | -5.83249 | -47.18655 | 2024-10-26 04:19:00 | NPP-375D | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c1976e2d-2324-3c65-8975-76848c323d8d | -5.83183 | -47.19055 | 2024-10-26 04:19:00 | NPP-375D | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bb28f239-fac0-34d5-a87f-1c4f577de9e3 | -5.82894 | -47.18597 | 2024-10-26 04:19:00 | NPP-375D | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| acb8bbbd-e550-354c-a9ca-b3a3c5058610 | -5.82829 | -47.18998 | 2024-10-26 04:19:00 | NPP-375D | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5f9faa05-4f21-3ffb-b289-abce17ee347a | -5.76767 | -46.53653 | 2024-10-26 04:19:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6b897a11-e520-3832-9555-080d2581b03c | -5.76422 | -46.53595 | 2024-10-26 04:19:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 41b2c383-8a22-3ec0-86fc-af844074724f | -5.76362 | -46.53969 | 2024-10-26 04:19:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 30dbe8c8-aa04-3646-8590-012a43424b46 | -5.74933 | -47.03119 | 2024-10-26 04:19:00 | NPP-375D | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6ac6ee64-689b-3d52-b70e-7d59225ed958 | -5.74869 | -47.03513 | 2024-10-26 04:19:00 | NPP-375D | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 45b588f1-0f12-3002-b371-bbd0eb932b1d | -5.71874 | -47.10749 | 2024-10-26 04:19:00 | NPP-375D | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 02349623-7124-3455-8634-b473f2c1631f | -5.71808 | -47.11148 | 2024-10-26 04:19:00 | NPP-375D | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6edcd2e8-c0ce-3d57-b618-387169409f0b | -5.71454 | -47.11094 | 2024-10-26 04:19:00 | NPP-375D | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 31700056-9d25-3755-9386-7e43f8b5723b | -5.66606 | -46.98997 | 2024-10-26 04:19:00 | NPP-375D | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0fd4c27d-f0fd-3f98-8c4c-ae12266c6210 | -5.66542 | -46.99389 | 2024-10-26 04:19:00 | NPP-375D | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5f237714-4773-3025-922d-09b7d6dc466c | -7.49527 | -48.08737 | 2024-10-26 04:19:00 | NPP-375D | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b0160d3f-e122-3066-96ce-4119bda97bd9 | -7.49249 | -48.0836 | 2024-10-26 04:19:00 | NPP-375D | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e28aaa30-fb37-31d1-8d42-c1d53390ea1a | -7.49235 | -48.08252 | 2024-10-26 04:19:00 | NPP-375D | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 14c9899d-cb48-3ce4-8505-fbc25839d5bd | -7.48885 | -48.08298 | 2024-10-26 04:19:00 | NPP-375D | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b7f5abc0-c55c-378c-ae99-2bc09231258a | -7.25177 | -48.0035 | 2024-10-26 04:19:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 854c06aa-3352-353b-9598-51a647a8bc93 | -7.24813 | -48.00295 | 2024-10-26 04:19:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8b133cc5-fab5-3672-bcc6-aa95a4dc8da1 | -7.01807 | -47.97162 | 2024-10-26 04:19:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3e7707c3-3f3e-32e7-8c62-69d8679b9a8a | -7.01444 | -47.97099 | 2024-10-26 04:19:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 91b947d0-368f-324d-a935-3514135f3801 | -6.84922 | -48.26828 | 2024-10-26 04:19:00 | NPP-375D | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 1.2 |
| adb2a0f2-2257-3af2-9298-398ef16edef3 | -7.96796 | -47.03653 | 2024-10-26 04:19:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 420d273e-47b8-3519-96ab-d1de1087ebae | -7.96451 | -47.03595 | 2024-10-26 04:19:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 27f2c9b4-37ff-3729-b18a-f9ede221ed41 | -7.68199 | -47.3111 | 2024-10-26 04:19:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README52.md)
