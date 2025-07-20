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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8e4f6bdb-8a05-3692-9507-cb74926817ba | -7.26907 | -60.11782 | 2025-07-20 05:55:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 81d57660-e363-3109-9624-4f73335c46cf | -7.26866 | -60.1209 | 2025-07-20 05:55:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a607c774-9f2d-3461-94d4-214208750ab3 | -7.26239 | -60.11702 | 2025-07-20 05:55:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c403982e-0784-3bef-878f-326aa6fa43be | -7.26711 | -60.12068 | 2025-07-20 05:55:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 49e165aa-d623-38da-a279-81b5c83b4f2b | -10.05644 | -64.99303 | 2025-07-20 05:57:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f7072b52-ece0-3101-86bb-2f09d7a7a2c9 | -14.15201 | -58.20117 | 2025-07-20 05:57:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 137e1b50-fdf1-3589-985a-26d940f37b82 | -12.0214 | -63.74895 | 2025-07-20 05:57:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ec72076f-5e62-3bfe-9ab3-b1282451a6c9 | -9.54382 | -62.81176 | 2025-07-20 05:57:00 | NPP-375D | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 80489287-e14c-30af-b5e6-f6bf5f1750c6 | -12.03477 | -63.77998 | 2025-07-20 05:57:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3e6c6797-29f6-3ee7-b4d0-ff30b42cfb43 | -10.38117 | -62.76211 | 2025-07-20 05:57:00 | NPP-375D | CACAULÂNDIA | RONDÔNIA | Brasil | 1100601 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d05fc0f4-314a-3631-94bf-4834726d6d2b | -12.02087 | -63.75303 | 2025-07-20 05:57:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 458a7f82-b214-3b23-83df-34964d2c9137 | -9.73532 | -63.1326 | 2025-07-20 05:57:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8437297c-4769-3acf-8010-0a5ea2bb3cc6 | -12.02425 | -63.74161 | 2025-07-20 05:57:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 18fdd80a-4d8d-34f8-ab33-ce32fdaca218 | -10.50397 | -68.64476 | 2025-07-20 05:57:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5ece596b-7aa6-3830-9210-e4cc7fad7af2 | -9.54441 | -62.80753 | 2025-07-20 05:57:00 | NPP-375D | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2c663b61-f27a-3851-8e54-2081a361efc6 | -9.0119 | -59.76622 | 2025-07-20 05:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 084d90be-38f1-3773-808f-69aaec82c1a6 | -8.97581 | -61.51186 | 2025-07-20 05:57:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2ca31bd5-790e-312f-9144-c9ea022ed7c2 | -12.02249 | -63.74075 | 2025-07-20 05:57:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a5c603a7-5a63-33e6-b6e0-07a3df573dfa | -12.03531 | -63.77593 | 2025-07-20 05:57:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| bac8c11d-718d-39fa-8bf3-9a7b43ae8e11 | -12.03585 | -63.77186 | 2025-07-20 05:57:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d8b5faf8-843d-30d5-890c-5f36f52f0293 | -10.38055 | -62.76667 | 2025-07-20 05:57:00 | NPP-375D | CACAULÂNDIA | RONDÔNIA | Brasil | 1100601 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a75715f3-7a01-3b50-bdb6-e61d5331ed16 | -10.29708 | -60.54417 | 2025-07-20 05:57:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 203a5e4a-630e-3b47-a6e4-77273ab3cf75 | -10.04182 | -64.90167 | 2025-07-20 05:57:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2f6bbd9b-69ab-3f2f-a9c5-3f17f904b719 | -8.17137 | -70.03335 | 2025-07-20 05:57:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 52c8b965-97db-3fdf-a0ab-70fdbee422b6 | -10.05961 | -64.99838 | 2025-07-20 05:57:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9c67a73f-8940-3965-8033-92ad40a13c4d | -10.38564 | -62.76282 | 2025-07-20 05:57:00 | NPP-375D | CACAULÂNDIA | RONDÔNIA | Brasil | 1100601 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8e540197-4401-3085-88b1-fd731c72185e | -14.14563 | -58.20042 | 2025-07-20 05:57:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a57f0af1-dc5a-38be-b895-52e0b400ffcf | -9.47769 | -57.83736 | 2025-07-20 05:57:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d9178d20-bce2-3e2b-b227-3b12d68fda51 | -12.02253 | -63.75384 | 2025-07-20 05:57:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 400cc869-b539-38d5-8d6a-9f913e09de0c | -12.0231 | -63.74978 | 2025-07-20 05:57:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 079803a0-fada-31a6-b073-df3ec89bfb00 | -12.0396 | -63.77653 | 2025-07-20 05:57:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8143d1e3-98a5-3cb8-bc2b-d1fba7908e99 | -8.17195 | -70.02976 | 2025-07-20 05:57:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7c649bd5-9647-3d27-967d-778f59bff98d | -12.03905 | -63.7806 | 2025-07-20 05:57:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a18a8ccb-93ac-381c-a9e8-b53eb26b129e | -9.19631 | -59.6898 | 2025-07-20 05:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9b8f7e2f-d7cd-30dd-92aa-34e699314afb | -12.02194 | -63.74488 | 2025-07-20 05:57:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4d431c89-78e7-3338-aabd-8171c24be171 | -10.37992 | -62.77126 | 2025-07-20 05:57:00 | NPP-375D | CACAULÂNDIA | RONDÔNIA | Brasil | 1100601 | 11 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 3216f38a-4b61-3d02-8d1a-2739fbad8316 | -9.97773 | -67.57681 | 2025-07-20 05:57:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aa2f6edc-d86c-3507-97f7-6044e59f73f4 | -8.97102 | -61.51122 | 2025-07-20 05:57:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 51bb738c-447d-3e35-abde-f5378fdec5b7 | -12.02303 | -63.73663 | 2025-07-20 05:57:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 717c5e63-8b9f-37a6-824e-cdf33f6629c5 | -9.4715 | -57.83683 | 2025-07-20 05:57:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c956a4e0-3f05-3ce8-951b-ffce1f213225 | -12.02367 | -63.74572 | 2025-07-20 05:57:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fff3d9a2-7bbf-3b55-aa93-7e156dbb1302 | -9.98114 | -67.57735 | 2025-07-20 05:57:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e23b8221-7be6-359d-9ae5-21ad6cf57f29 | -9.01683 | -59.77039 | 2025-07-20 05:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 740bb79f-493e-35a1-ad85-e727a0c7c9b5 | -9.01148 | -59.76937 | 2025-07-20 05:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 763d9275-e44e-3db6-84e2-6f6ba3379811 | -12.02482 | -63.73751 | 2025-07-20 05:57:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 954e9f9b-8262-3285-a138-b8943a9cd24f | -10.38441 | -62.7718 | 2025-07-20 05:57:00 | NPP-375D | CACAULÂNDIA | RONDÔNIA | Brasil | 1100601 | 11 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 08554648-4bcf-3552-a86d-bbd1be168ce6 | -10.38503 | -62.7673 | 2025-07-20 05:57:00 | NPP-375D | CACAULÂNDIA | RONDÔNIA | Brasil | 1100601 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 87d7be29-8e86-3a75-a19b-706d755d5a92 | -10.6689 | -46.7853 | 2025-07-20 06:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 47.2 |
| f4716398-a2f7-33ba-8a95-d59793846a52 | -10.688 | -46.7829 | 2025-07-20 06:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 63.7 |
| ddc62042-2ee1-31d8-baeb-116d5c5fa85f | -10.688 | -46.7829 | 2025-07-20 06:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 61729350-47d7-324d-bba6-45b4b26db948 | -10.688 | -46.7829 | 2025-07-20 06:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 58.4 |
| 77c481dd-255e-34e5-b0f7-5d1a647e28f8 | -10.6689 | -46.7853 | 2025-07-20 06:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 0ade0d0e-271c-34cd-b188-a900bb1daf0d | -10.37658 | -62.77499 | 2025-07-20 06:20:00 | NOAA-20 | CACAULÂNDIA | RONDÔNIA | Brasil | 1100601 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 16fc7649-a2be-36b0-80f7-cb9d2b9cc0ef | -12.02163 | -63.74189 | 2025-07-20 06:20:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| af39f68d-2566-3a97-87c3-42e0faf0273d | -10.38343 | -62.77553 | 2025-07-20 06:20:00 | NOAA-20 | CACAULÂNDIA | RONDÔNIA | Brasil | 1100601 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| affefaba-0513-335b-80cb-a284dc5c38d5 | -10.38494 | -62.76289 | 2025-07-20 06:20:00 | NOAA-20 | CACAULÂNDIA | RONDÔNIA | Brasil | 1100601 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2a45d8d3-1730-3154-bb48-ef40177829c3 | -8.17213 | -70.02969 | 2025-07-20 06:20:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 82ee3386-8222-3285-a4af-fa6e50bb483d | -12.02144 | -63.75095 | 2025-07-20 06:20:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5356e4af-ae20-3a26-a158-e83878a258ce | -12.03687 | -63.78363 | 2025-07-20 06:20:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a2585a15-14dd-39fa-908a-ac8a470d496b | -12.0375 | -63.77807 | 2025-07-20 06:20:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2b2cc0c1-9166-30c3-97b2-9d87b5f22e10 | -12.02279 | -63.73964 | 2025-07-20 06:20:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0ec3437a-4f38-3340-bab4-385aeb4c21d8 | -12.03813 | -63.77249 | 2025-07-20 06:20:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2fdf1920-ad2d-342b-8278-a10713358d59 | -12.03158 | -63.77169 | 2025-07-20 06:20:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 31d445f2-5f53-3b75-8661-22b6b8aedb07 | -10.38419 | -62.7692 | 2025-07-20 06:20:00 | NOAA-20 | CACAULÂNDIA | RONDÔNIA | Brasil | 1100601 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 07f387a9-8a0f-373c-bcf0-1f99cbb59d36 | -10.37734 | -62.7686 | 2025-07-20 06:20:00 | NOAA-20 | CACAULÂNDIA | RONDÔNIA | Brasil | 1100601 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4373632c-4c65-346b-8c9c-d037f3105e09 | -8.17159 | -70.03335 | 2025-07-20 06:20:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6d8a1371-fc54-3a45-8672-bb9926cf4c60 | -12.02099 | -63.74758 | 2025-07-20 06:20:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c95150f7-9524-39f6-a907-88a809ca461b | -12.02211 | -63.74537 | 2025-07-20 06:20:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f3ebdf6d-c2f2-363d-b1d2-a00d2cfcda39 | -12.03096 | -63.7772 | 2025-07-20 06:20:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7f83aef6-90a7-38aa-a565-26d4a087c2bc | -10.6689 | -46.7853 | 2025-07-20 06:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 76.4 |
| fda9d07e-1926-3fd7-a240-7733892db137 | -10.688 | -46.7829 | 2025-07-20 06:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 5fc0d317-08ac-3d67-b017-83d00efd41e1 | -12.1541 | -44.778 | 2025-07-20 06:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 53.9 |
| e7c5f526-b765-39b1-9e77-31ed1185d8fd | -10.6689 | -46.7853 | 2025-07-20 06:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 108.0 |
| 9eef01a0-6ead-3549-afaa-7896526d35bb | -10.688 | -46.7829 | 2025-07-20 06:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 96.4 |
| 43c8778a-263d-36af-927e-e44cc4fe99e1 | -10.688 | -46.7829 | 2025-07-20 06:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 144.2 |
| 57e610f2-994e-30b5-8b7d-da1b1b1553bd | -10.6689 | -46.7853 | 2025-07-20 06:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 135.9 |
| c1b3f3ba-ea34-3af4-96e4-de9348e1d48a | -10.6499 | -46.7876 | 2025-07-20 06:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 49.9 |
| c012eb14-844c-385d-addb-e359435bf446 | -10.688 | -46.7829 | 2025-07-20 07:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 116.2 |
| 6dfb62c1-db4f-3f7f-ba80-e649d5122211 | -10.6689 | -46.7853 | 2025-07-20 07:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 116.1 |
| eaae9ef6-fe6a-3e62-b7a8-ae06e4919445 | -10.6499 | -46.7876 | 2025-07-20 07:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 61.4 |
| 435ee506-1db2-39a5-9602-143f4be556a3 | -10.688 | -46.7829 | 2025-07-20 07:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 67.3 |
| d99e2b56-8fed-3198-b6f2-be7e7a2aa1f7 | -10.6689 | -46.7853 | 2025-07-20 07:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 91.7 |
| bb99c029-c667-3086-8800-7c7c63b93328 | -12.37797 | -41.57943 | 2025-07-20 11:32:00 | TERRA_M-M | SEABRA | BAHIA | Brasil | 2929909 | 29 | 33 | nan | nan | nan | Caatinga | 14.8 |
| eb1ee7fd-56a4-3f32-b1f8-f85b1c79b4ef | -12.1544 | -44.78323 | 2025-07-20 11:32:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 137.6 |
| b222c48f-52e4-351a-a665-fcc016219115 | -12.14479 | -44.78757 | 2025-07-20 11:32:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 160.2 |
| 3ad0976b-68f8-32e8-b76c-0d88a57ff6ca | -6.7446 | -45.5282 | 2025-07-20 12:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 631c73e2-a9b4-378d-885f-b83e344f861a | -6.896 | -45.38 | 2025-07-20 12:40:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 695a3771-b924-3256-83aa-5bb35a68552d | -6.896 | -45.38 | 2025-07-20 12:50:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 83.5 |
| b825fce3-5599-30d2-9672-36eb169fa23a | -12.1541 | -44.778 | 2025-07-20 12:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 86.5 |
| d19007b8-3acc-39e9-bf4e-ee845c90ab89 | -5.6131 | -42.3128 | 2025-07-20 13:10:00 | GOES-19 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 81.6 |
| 7e736356-0a8a-3cd3-b08a-8f84bc7d3387 | -6.4469 | -45.3263 | 2025-07-20 13:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 363d8c09-3c1d-3313-a7b3-a653b8b95b1c | -12.1541 | -44.778 | 2025-07-20 13:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 108.7 |
| 70381b1b-ad1d-341e-a4db-00d17e50ce39 | -8.0061 | -43.6905 | 2025-07-20 13:20:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 99dc4bed-fc0e-3e8e-a9fb-73d5037ca32c | -7.4338 | -44.2812 | 2025-07-20 13:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 88.2 |
| 814f503c-a977-3657-b5e7-a660191f7423 | -12.1541 | -44.778 | 2025-07-20 13:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 75.7 |
| e7020601-9e92-3025-bdbf-db986f4fd29a | -10.3775 | -49.9293 | 2025-07-20 13:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 00a836fd-78be-3566-a580-4eb20f4b7b5d | -9.4034 | -47.9487 | 2025-07-20 13:30:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 55.5 |
| 8c460939-9ae3-3c58-88fc-d96b7a827fd6 | -7.4338 | -44.2812 | 2025-07-20 13:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 107.4 |
| cc93c500-690e-3721-9095-62a809dbe8e8 | -12.1541 | -44.778 | 2025-07-20 13:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 100.8 |
| fa910fbc-0d11-38ed-a5a0-64ba6ee495db | -10.3775 | -49.9293 | 2025-07-20 13:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 98.0 |


[Clique aqui para ver as próximas entradas](README20.md)
