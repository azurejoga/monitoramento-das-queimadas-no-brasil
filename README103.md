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

## Dados Diários - Página 103

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fcac2b90-fc88-3aea-80a4-2077d6e4d661 | -7.02279 | -48.54549 | 2024-10-10 04:44:00 | NOAA-20 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0dbb1e6e-2fd6-3ac1-b501-8f7092872275 | -7.01556 | -48.54135 | 2024-10-10 04:44:00 | NOAA-20 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8155c41f-0691-3032-a51e-6871c47b7a39 | -7.00794 | -48.54423 | 2024-10-10 04:44:00 | NOAA-20 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c29d9808-af91-3391-9483-453f5d3b9711 | -7.62238 | -49.44259 | 2024-10-10 04:44:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 61579858-9730-3fb9-9e5d-3da240d2ce4a | -7.61898 | -49.44205 | 2024-10-10 04:44:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 01a20dfa-28d9-3093-9cc2-ead532f2f4c4 | -7.60138 | -49.39759 | 2024-10-10 04:44:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fef3faa4-aaed-3250-af29-f9d0773237bb | -7.59854 | -49.39335 | 2024-10-10 04:44:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6fb9b41e-625a-3a8d-bc3a-45da8e735919 | -7.59797 | -49.39706 | 2024-10-10 04:44:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2e0676dd-65e7-3ab1-8faa-3fc7ccba68c2 | -7.54074 | -49.49804 | 2024-10-10 04:44:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 871d0db3-8282-3682-8106-b1c99a6aad94 | -7.5193 | -49.52477 | 2024-10-10 04:44:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| efbfa3a1-6f6e-37da-9398-1089b1df3f88 | -9.05533 | -49.71299 | 2024-10-10 04:44:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 26eb2ab2-48b8-33c5-b979-8b6dc6abcb2b | -8.79274 | -49.66689 | 2024-10-10 04:44:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| c204838d-026e-3d4d-bec0-c038770df22f | -8.78933 | -49.66636 | 2024-10-10 04:44:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d30e7980-3521-3b64-a8bc-9c45ac99df36 | -8.7815 | -49.78905 | 2024-10-10 04:44:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| c6634878-c111-371b-8b3c-af586876338d | -8.75752 | -49.7827 | 2024-10-10 04:44:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ea199195-c5a4-3d59-814e-629c29bdbfd3 | -8.75412 | -49.78217 | 2024-10-10 04:44:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3537a6c1-9ca3-3a74-a1ee-d7774c236a4b | -8.75072 | -49.78163 | 2024-10-10 04:44:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7ef23068-d4d9-3ff8-ba5b-8429373d20c7 | -8.66432 | -49.42912 | 2024-10-10 04:44:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9d0b5064-25f6-37a7-8414-d5a70952b502 | -8.66089 | -49.42858 | 2024-10-10 04:44:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 64d7a460-fb40-3513-8773-1e2e6bb1d727 | -8.6288 | -50.19433 | 2024-10-10 04:44:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 57ee1e3b-13b7-317f-94be-5dc8779c1e02 | -8.62657 | -49.03196 | 2024-10-10 04:44:00 | NOAA-20 | PEQUIZEIRO | TOCANTINS | Brasil | 1716653 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e8431a7f-1cc5-34be-8385-23ed90d04ac6 | -8.62598 | -49.03585 | 2024-10-10 04:44:00 | NOAA-20 | PEQUIZEIRO | TOCANTINS | Brasil | 1716653 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| aaf533e2-43ec-3118-a571-92aa6674b0de | -8.57429 | -49.21382 | 2024-10-10 04:44:00 | NOAA-20 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| e48f4e87-b05b-3f3c-8004-7dd3c16ceab8 | -8.57372 | -49.21766 | 2024-10-10 04:44:00 | NOAA-20 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 756cfd3d-9df7-3640-a25b-63d3b13583e6 | -8.4938 | -48.64149 | 2024-10-10 04:44:00 | NOAA-20 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 4.1 |
| ff75c6bb-a989-373c-896e-57dc5e18f446 | -8.49318 | -48.64557 | 2024-10-10 04:44:00 | NOAA-20 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 79efd518-fd40-38ad-8d26-8b7adae359c2 | -8.40264 | -49.5622 | 2024-10-10 04:44:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 59b4e6d2-5019-3f48-b070-4504f33b161e | -8.40207 | -49.56593 | 2024-10-10 04:44:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 006c3dab-2ed9-3de9-bde9-5c088828e814 | -8.39922 | -49.56168 | 2024-10-10 04:44:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c715485d-31b9-3e32-ae2e-2fc2735d94ad | -8.39866 | -49.56541 | 2024-10-10 04:44:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0aec9cd8-9c4c-31f1-8979-aa567e063dcd | -8.3981 | -49.56915 | 2024-10-10 04:44:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b2d7a809-0feb-3f8d-8b5d-629350aff1fe | -8.33874 | -49.65898 | 2024-10-10 04:44:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 84503878-f258-32a8-8441-85635b2746d6 | -8.32851 | -49.98207 | 2024-10-10 04:44:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f5495bf8-2cc8-378c-bcd2-16a2bd94cf03 | -8.32796 | -49.98568 | 2024-10-10 04:44:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4a1b83ea-1cd4-3c59-b8fc-6868f37d341d | -8.32459 | -49.98516 | 2024-10-10 04:44:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ddbabfe5-db07-342a-a0c9-36e01e1565f5 | -8.23418 | -49.76756 | 2024-10-10 04:44:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1c1e08ae-70ba-3274-969c-cf80788914ed | -8.1866 | -49.18862 | 2024-10-10 04:44:00 | NOAA-20 | JUARINA | TOCANTINS | Brasil | 1711803 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2b71be5d-4b6b-3265-a597-4d40a49b79a5 | -8.18315 | -49.18808 | 2024-10-10 04:44:00 | NOAA-20 | JUARINA | TOCANTINS | Brasil | 1711803 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 438a9259-1dc0-3625-b90d-d6266238e909 | -8.14451 | -49.09232 | 2024-10-10 04:44:00 | NOAA-20 | JUARINA | TOCANTINS | Brasil | 1711803 | 17 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e65af2e6-3d5f-3896-b75f-2199ec9a5390 | -8.07209 | -49.66438 | 2024-10-10 04:44:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d2582a07-e8c2-3775-a6f0-02a75b923e05 | -8.07154 | -49.66805 | 2024-10-10 04:44:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 2edd8ce2-edb9-3b48-ac89-c9b954807b71 | -8.07098 | -49.67173 | 2024-10-10 04:44:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3c08883e-9966-310b-b836-a5737998b5f7 | -8.0687 | -49.66386 | 2024-10-10 04:44:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| abca4a25-c6a8-383f-b6af-4d5c0f90c60a | -8.06814 | -49.66753 | 2024-10-10 04:44:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1f3eda43-e2bd-3538-b391-35e00effe4fc | -8.02155 | -49.76878 | 2024-10-10 04:44:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 87cdf5fe-fb5d-3a2b-a563-800423cab835 | -8.02027 | -49.7686 | 2024-10-10 04:44:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b25dce2d-1a49-3891-8150-5ca6280adfde | -8.00167 | -49.2267 | 2024-10-10 04:44:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2727b188-26be-3cd4-90aa-7c5bfe84a041 | -7.99049 | -49.8494 | 2024-10-10 04:44:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 00d53f02-b3bd-3081-a320-1503a25e7f22 | -8.50089 | -48.64256 | 2024-10-10 04:44:00 | NOAA-20 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 2.1 |
| da39f98d-ffae-379c-a4c1-ba369495a308 | -8.49735 | -48.64202 | 2024-10-10 04:44:00 | NOAA-20 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 4.1 |
| bcf71b5a-6f69-3435-9da1-96454ab82803 | -8.49673 | -48.64611 | 2024-10-10 04:44:00 | NOAA-20 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 6aad9a31-be74-3e35-abd9-2963ef01a0ad | -9.28632 | -49.7821 | 2024-10-10 04:44:00 | NOAA-20 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 011195c2-0c8a-35d0-bfa6-3975bf6d0be7 | -9.08731 | -50.26086 | 2024-10-10 04:44:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a87599c9-8aeb-35a4-b5ad-0679d1115353 | -9.05192 | -49.71246 | 2024-10-10 04:44:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8cfdcda5-a506-3d09-b788-b983852e6aa2 | -8.7849 | -49.78957 | 2024-10-10 04:44:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 740b17bf-f7d5-31c9-976a-358ab3a35590 | -8.75129 | -49.77795 | 2024-10-10 04:44:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4b715a45-adef-3509-9f0e-fccf797c265a | -8.62554 | -50.04621 | 2024-10-10 04:44:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3249d451-3fdc-3023-beab-3ba22f89bd5a | -10.86473 | -49.75607 | 2024-10-10 04:44:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 997a74ef-18eb-3795-a689-a6b31b4961e7 | -10.86416 | -49.75992 | 2024-10-10 04:44:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 44bbc159-2dc5-3803-8b7b-85d050a07f0c | -10.86359 | -49.76377 | 2024-10-10 04:44:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9de12827-550e-37f6-ace9-8255dcf0f5d2 | -10.86184 | -49.75169 | 2024-10-10 04:44:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 65db4490-86a1-3c5a-af69-d7376a93a9b4 | -10.8607 | -49.75939 | 2024-10-10 04:44:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| aad8c932-a569-38af-988f-8822ff80efc8 | -10.85781 | -49.755 | 2024-10-10 04:44:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e7e19066-e7fb-3ae4-a05f-fb9976d0b8ba | -10.85549 | -49.74677 | 2024-10-10 04:44:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 162e4385-6f1d-33ab-9ff5-e1af211da2c0 | -10.85492 | -49.75062 | 2024-10-10 04:44:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ee8ecb77-04e4-3780-b123-f37b19d64f6c | -10.73696 | -49.56369 | 2024-10-10 04:44:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 602e6928-0a01-3878-af46-5e37ac4e8d1f | -10.48754 | -49.80231 | 2024-10-10 04:44:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0135357d-8198-328e-95d7-714f6ef0684e | -10.48409 | -49.80178 | 2024-10-10 04:44:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d9a6a3e7-1a6a-3a7c-a9b1-99407342b8b3 | -9.62621 | -48.99315 | 2024-10-10 04:44:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| cdddb622-262b-3365-b5d3-b355a2af0769 | -9.62268 | -48.9926 | 2024-10-10 04:44:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 54316a23-f8ad-3711-adde-74448790452b | -9.56852 | -48.94365 | 2024-10-10 04:44:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 664fa8cc-bef9-3a81-bf89-7100363bdcbf | -9.56793 | -48.94765 | 2024-10-10 04:44:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4c716224-8b6c-3fd4-905e-41485e45f0ca | -9.56498 | -48.94316 | 2024-10-10 04:44:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c25e1667-ef18-3f6a-807e-25260bef2b58 | -9.56439 | -48.94716 | 2024-10-10 04:44:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f7a748f8-0028-3674-9af3-1b2967419d0e | -10.52329 | -49.10681 | 2024-10-10 04:44:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 14a97cf4-5c1e-36f9-9ca8-a90e23870df4 | -10.5227 | -49.11082 | 2024-10-10 04:44:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9a343c6f-6b56-3817-ac90-3437268ac372 | -9.94948 | -50.07438 | 2024-10-10 04:44:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| aaf3ebb8-f5bf-343d-8503-e159c93defcf | -9.94324 | -50.06964 | 2024-10-10 04:44:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1e95e5fd-bf07-3e08-b65c-48cb372630bf | -9.93645 | -50.06859 | 2024-10-10 04:44:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a983a55a-060b-3ab6-86f4-9b33ca8f3056 | -9.90335 | -50.07493 | 2024-10-10 04:44:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 61685f14-cf83-3255-bf91-9e33d70ceb81 | -9.80178 | -50.07536 | 2024-10-10 04:44:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 356d7b73-e117-3b42-a143-c53b5efc3d0f | -9.79895 | -50.07116 | 2024-10-10 04:44:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8586e81e-d1a3-3a96-bc69-74944d125df9 | -9.77073 | -50.11948 | 2024-10-10 04:44:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4693dd1c-277c-380a-9138-1fbcb9916136 | -9.7679 | -50.11529 | 2024-10-10 04:44:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ae294883-24c0-3820-9102-1e93cf603bc0 | -9.76734 | -50.11896 | 2024-10-10 04:44:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e0aecc03-3a0d-3275-9657-345ea8bd0a28 | -9.58428 | -50.22155 | 2024-10-10 04:44:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| af307182-437f-3776-89ae-91cf6ecfa266 | -9.57981 | -50.22831 | 2024-10-10 04:44:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 61eec87e-10e6-36ce-954b-9cd8a0bce7b6 | -9.57926 | -50.23194 | 2024-10-10 04:44:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 861323b6-5ce7-349b-a93e-a058ac237a60 | -9.57837 | -50.22839 | 2024-10-10 04:44:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9f13bc54-13a5-35b6-b127-aa182f5cd532 | -9.57781 | -50.23203 | 2024-10-10 04:44:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4a7cdd1b-0b6b-3c97-83d8-0f7fd1e96135 | -9.57444 | -50.23151 | 2024-10-10 04:44:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 90b1791f-e433-3fda-ae9a-772636dc885f | -9.57388 | -50.23513 | 2024-10-10 04:44:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4344c30a-dcf0-363f-95d0-3809a94fa357 | -9.57051 | -50.23461 | 2024-10-10 04:44:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b7032483-766f-3b03-b3cf-c5b0e6c1b76e | -9.56602 | -50.24135 | 2024-10-10 04:44:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cf7d772a-c439-3913-b37c-5458db05ea5f | -9.5632 | -50.23719 | 2024-10-10 04:44:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a6ed7326-1617-323c-b535-3f97f9bf8490 | -9.54857 | -50.22005 | 2024-10-10 04:44:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4ca914f7-66c0-361e-b2c3-308594718a83 | -10.06712 | -49.54919 | 2024-10-10 04:44:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dafa3280-8310-3328-8dfb-46267ff59e83 | -10.06654 | -49.55304 | 2024-10-10 04:44:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 2e0859f1-e502-33b2-94af-d82e12d28ff2 | -11.96216 | -50.11761 | 2024-10-10 04:44:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 68307721-5197-33b1-be0b-f944ad8a66fc | -11.93519 | -50.17987 | 2024-10-10 04:44:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README104.md)
