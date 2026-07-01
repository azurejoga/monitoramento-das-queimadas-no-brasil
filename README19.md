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
| 976d18ee-26c7-349d-b7d4-75ee133a0fdc | -8.35577 | -46.81417 | 2026-07-01 04:38:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8edba505-80b2-381a-a86b-fd580bd3eb3b | -12.79898 | -54.86213 | 2026-07-01 04:38:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| c099ea8d-5878-39db-a430-72d337a5a545 | -11.42155 | -56.05256 | 2026-07-01 04:38:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5ae98123-2d0f-30dd-9255-f0593c94d63a | -8.12551 | -47.87704 | 2026-07-01 04:38:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e8bb2582-14da-3c52-b75c-37d6fdba998f | -11.43378 | -56.0704 | 2026-07-01 04:38:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 3b2762af-f0f1-3f31-b1bc-3a876bde5684 | -12.77078 | -44.49517 | 2026-07-01 04:38:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 40.1 |
| 7c341e26-8627-3732-9f37-7bdf95b5d13b | -12.83439 | -44.35896 | 2026-07-01 04:38:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| dea685b1-643d-3694-bfff-6ffd61f6fcbc | -12.83195 | -44.34948 | 2026-07-01 04:38:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 32.7 |
| 2a5e0436-7431-3ec5-abc9-6a74b21d3b3d | -11.54364 | -47.4515 | 2026-07-01 04:38:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 6de82a74-b1a6-3bee-9cf9-36e46118fbcb | -9.88402 | -50.39291 | 2026-07-01 04:38:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5e78a9ce-f2aa-3f9a-8271-5fac814a7f61 | -8.34802 | -46.82009 | 2026-07-01 04:38:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| a5ab686a-70ed-3028-887f-1dd9907d0bcb | -12.41952 | -58.38832 | 2026-07-01 04:38:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| c5d70133-472b-32be-b053-a079f603e9b8 | -12.76838 | -44.48587 | 2026-07-01 04:38:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 89.4 |
| b4a0d9fb-2224-31c3-aedd-7ba19b28cf64 | -10.83015 | -48.7617 | 2026-07-01 04:38:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c4c265c8-0b45-3baf-b4cc-a531f48f3bad | -9.19075 | -45.3253 | 2026-07-01 04:38:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e6665a75-0ba3-39bd-b3de-c7adc8e2a841 | -10.76435 | -53.5431 | 2026-07-01 04:38:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5760afe1-a5d1-3e0d-be4a-cfc453232448 | -9.69226 | -56.0937 | 2026-07-01 04:38:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 86b47b9c-5487-3553-bf11-876d18d2e62b | -11.63017 | -59.01818 | 2026-07-01 04:38:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| ff0fd15d-efaf-3439-9cef-dd7a099c4e6f | -10.9205 | -43.0622 | 2026-07-01 04:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 203.0 |
| 702f34e4-be7d-3eb4-ac5f-0f2adbe9c9e0 | -11.4149 | -56.0525 | 2026-07-01 04:40:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 40c29551-58eb-37bb-a896-d5d773faa4a4 | -10.9397 | -43.0593 | 2026-07-01 04:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 101.0 |
| 2d48d1eb-bce4-39ea-baea-81ecda6522c4 | -10.6787 | -54.5153 | 2026-07-01 04:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 69.3 |
| f43910e1-a8da-360d-93e6-9fd7b696454f | -12.8354 | -44.3657 | 2026-07-01 04:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 220.2 |
| 4f0d6abf-4131-35ce-a9c2-5af5c74a015e | -12.8552 | -44.3389 | 2026-07-01 04:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 184.8 |
| f6760b0c-01ec-388d-8aac-3a58534102f8 | -12.8165 | -44.3454 | 2026-07-01 04:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 57.1 |
| 70368b20-93c2-395e-b040-8081f63a2ccd | -10.9401 | -43.0355 | 2026-07-01 04:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 89e2ddc0-4d34-3fa7-bd8c-ff3069f58f58 | -12.7562 | -44.4724 | 2026-07-01 04:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 211.3 |
| f2c63109-bcfd-3e8c-92e5-c09e804c50a2 | -11.4336 | -56.0711 | 2026-07-01 04:40:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 101.0 |
| 61c7c0fd-8a73-3b04-a647-ee42fa71ca13 | -10.6598 | -54.5169 | 2026-07-01 04:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 707aa21e-11c4-3691-ac0f-07f87fa02323 | -12.7755 | -44.4693 | 2026-07-01 04:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 330.6 |
| 9c7a72c3-6e4e-35c6-8a86-e98dc884f0b3 | -12.7751 | -44.4927 | 2026-07-01 04:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 398.6 |
| ad0a1f1c-04fe-3646-94d0-793d415b4209 | -10.6596 | -54.5372 | 2026-07-01 04:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 44.5 |
| b9240b14-918f-325e-9c73-2457d12f2fd7 | -12.8359 | -44.3422 | 2026-07-01 04:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 366.5 |
| 851d5031-b9b2-3794-9502-3b03eed7b86d | -12.7557 | -44.4959 | 2026-07-01 04:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 250.9 |
| db932b32-fceb-39ea-be3e-21a72d0b3d6f | -10.6784 | -54.5356 | 2026-07-01 04:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 1bae40ae-87d7-3f2d-a0df-f39415577065 | -11.4147 | -56.0726 | 2026-07-01 04:40:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 44.6 |
| 16ec5104-b2b7-393c-b43d-4381e4d6e0b1 | -12.8548 | -44.3625 | 2026-07-01 04:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 114.7 |
| 8eab1ecb-5ced-3ed2-9d5e-c8aa92098560 | -12.8363 | -44.3186 | 2026-07-01 04:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 48.1 |
| b0217b30-4bd6-3251-b5f4-95b709e1979c | -11.4338 | -56.0509 | 2026-07-01 04:40:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 96.6 |
| f12232ad-3184-30b5-a05c-8ad5a2688fdf | -10.9209 | -43.0384 | 2026-07-01 04:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 145.7 |
| 6474baf9-6c49-312e-8dc6-2ee225c0b7a0 | -17.91592 | -52.71512 | 2026-07-01 04:40:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 649883b9-c937-3a70-9ade-a82d96851cfa | -15.94863 | -48.14567 | 2026-07-01 04:40:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b68dfb98-9a45-3ce4-80a3-5500cab8ef62 | -17.71738 | -46.79761 | 2026-07-01 04:40:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 23214b99-f355-35ab-a958-d41ee76c6704 | -16.07614 | -45.89816 | 2026-07-01 04:40:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| a5f595eb-da45-31a3-9f2d-c14136f4f3fa | -17.70811 | -46.78791 | 2026-07-01 04:40:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b70c9bd3-acd8-31ba-aa97-d93d8c351101 | -16.35959 | -49.33341 | 2026-07-01 04:40:00 | NPP-375D | NOVA VENEZA | GOIÁS | Brasil | 5215009 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 61b61151-8ba9-3159-87b8-2dd07aa64e3b | -16.58347 | -45.87781 | 2026-07-01 04:40:00 | NPP-375D | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f3f20d60-6dbe-3dfa-8395-b112d58fef7f | -16.36158 | -56.65798 | 2026-07-01 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.5 |
| 331afe72-5cd1-3fbc-be3e-54bf90c4bfb8 | -16.35199 | -56.65993 | 2026-07-01 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.1 |
| f6909d1c-7ef4-3b0e-a3e5-59f9d3017ee7 | -17.71217 | -46.78452 | 2026-07-01 04:40:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 50997577-c012-385f-b890-ceba1e2199d7 | -17.03232 | -43.26096 | 2026-07-01 04:40:00 | NPP-375D | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c5c85d0e-0c8f-3939-af23-61b4a395bb64 | -19.84425 | -49.07054 | 2026-07-01 04:40:00 | NPP-375D | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f18ca537-4feb-3922-8980-ced4ac16d47e | -15.60062 | -43.59929 | 2026-07-01 04:40:00 | NPP-375D | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 8335e23a-4d87-35bb-8d30-e913194c296f | -15.9453 | -48.14511 | 2026-07-01 04:40:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2081e574-8947-3114-a6a0-bc471c522204 | -16.35676 | -56.66093 | 2026-07-01 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.1 |
| 701a659f-f081-39cf-a232-44ef748f5198 | -22.55443 | -46.95628 | 2026-07-01 04:40:00 | NPP-375D | MOGI MIRIM | SÃO PAULO | Brasil | 3530805 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b2e6314f-1677-37ca-985a-dbfe18b973cf | -16.36052 | -56.66325 | 2026-07-01 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.5 |
| 21bf5148-a344-30cb-8472-10944efd6f12 | -16.36529 | -56.66429 | 2026-07-01 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.5 |
| 2ad1f0b6-5b45-34ea-8b6f-8de480f6fe3b | -15.60464 | -43.59985 | 2026-07-01 04:40:00 | NPP-375D | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| d970d4d3-e39b-34e3-ac00-6e4aa2150630 | -17.44024 | -47.16244 | 2026-07-01 04:40:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 19290d1b-39f4-387c-924a-a9fcdeb2c07a | -13.26461 | -56.79987 | 2026-07-01 04:40:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ac936f01-556e-35b1-85ee-cd370f06859c | -17.71507 | -46.78909 | 2026-07-01 04:40:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| f9eef32d-be55-35a5-960c-074ff1b0c822 | -17.7139 | -46.79702 | 2026-07-01 04:40:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 6.7 |
| fe9199b5-55d9-346b-a933-a5f4268e107e | -21.49433 | -48.53976 | 2026-07-01 04:40:00 | NPP-375D | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 965f65a4-48f2-3c06-9697-c7acaaabadd0 | -21.6345 | -44.6581 | 2026-07-01 04:40:00 | NPP-375D | CARRANCAS | MINAS GERAIS | Brasil | 3114600 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 83342e2a-cf22-3210-890f-73665df9e1e1 | -17.43966 | -47.16629 | 2026-07-01 04:40:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e2305f61-5e19-3895-866b-6b45dd02e3cb | -13.26402 | -56.80294 | 2026-07-01 04:40:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 99bce126-677b-3311-9ea0-10fc94ea3536 | -16.36153 | -56.66195 | 2026-07-01 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 20.1 |
| 9e1751b7-caf5-3da1-be3c-ee637c1858b3 | -14.63241 | -54.46519 | 2026-07-01 04:40:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c007ceb8-df7b-3900-aeae-9e2c1ae3c889 | -16.58499 | -45.87621 | 2026-07-01 04:40:00 | NPP-375D | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0c4006af-f2a6-3d93-931a-ef518af8743e | -15.60101 | -43.60039 | 2026-07-01 04:40:00 | NPP-375D | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 8160f19b-f9dc-3e1c-a5c2-52e7b616d6f8 | -14.62975 | -54.46612 | 2026-07-01 04:40:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 02e2d5a8-5259-34e7-bf13-8b1ba1652df8 | -18.52183 | -47.24396 | 2026-07-01 04:40:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 09639bfd-7c9f-38a9-964b-cf357e88a0ea | -17.711 | -46.79247 | 2026-07-01 04:40:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| add7fbcb-174b-3b4e-8b38-44d0672d9987 | -17.70521 | -46.78334 | 2026-07-01 04:40:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e199b723-48ae-38c1-8286-93a6a3ec0a6d | -19.51051 | -52.74078 | 2026-07-01 04:40:00 | NPP-375D | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b6763f84-ee22-3705-9d4f-18d7d8de6b92 | -17.12077 | -50.09134 | 2026-07-01 04:40:00 | NPP-375D | INDIARA | GOIÁS | Brasil | 5209952 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2b7f1816-ae36-3598-8cd2-ba3b0bc48350 | -21.49093 | -48.53917 | 2026-07-01 04:40:00 | NPP-375D | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 9bd562c0-8853-3188-ac28-9cc784e8bee5 | -14.629 | -54.47027 | 2026-07-01 04:40:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 63ad9cbc-2e1d-3178-a683-13f4573a92fa | -17.70869 | -46.78393 | 2026-07-01 04:40:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0e77494b-1888-3881-ac61-873fc36e65dc | -17.11741 | -50.09075 | 2026-07-01 04:40:00 | NPP-375D | INDIARA | GOIÁS | Brasil | 5209952 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2a09affe-ad99-3f3e-881f-dc62698aefde | -18.52123 | -47.24794 | 2026-07-01 04:40:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| caf78118-99fc-3166-8317-6dc41db33385 | -16.04452 | -50.55721 | 2026-07-01 04:40:00 | NPP-375D | NOVO BRASIL | GOIÁS | Brasil | 5215207 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1c37798a-0c36-34c3-9176-d8634f257d98 | -16.58141 | -45.87564 | 2026-07-01 04:40:00 | NPP-375D | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fb2c8877-b2b9-39f6-9c31-ec0dd94e7b43 | -22.5686 | -44.11963 | 2026-07-01 04:40:00 | NPP-375D | BARRA MANSA | RIO DE JANEIRO | Brasil | 3300407 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| e34703ca-256f-3f7e-8b9d-650692071a8d | -17.44309 | -47.16684 | 2026-07-01 04:40:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 601096a5-95fd-33f8-91c5-e090bdb73487 | -16.35573 | -56.66626 | 2026-07-01 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.1 |
| 01b5936e-1d93-3ab2-b6fe-578ad86a3b64 | -19.51409 | -52.74152 | 2026-07-01 04:40:00 | NPP-375D | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ce653176-c052-3bbe-9542-9fdd22d0d7a5 | -14.63164 | -54.46934 | 2026-07-01 04:40:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8e111db4-fba6-3dbf-bb67-a37bbe2d18e7 | -17.71448 | -46.79306 | 2026-07-01 04:40:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| ad7522cf-dace-3c34-a95a-3527323e7a7c | -19.66916 | -46.19765 | 2026-07-01 04:40:00 | NPP-375D | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 65b448f3-6222-30a9-a043-06bd332b7f8a | -18.12978 | -49.09586 | 2026-07-01 04:40:00 | NPP-375D | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2c5f9b83-b759-38ff-9436-023c1b1649c0 | -15.60503 | -43.60096 | 2026-07-01 04:40:00 | NPP-375D | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| b5815eba-25b7-3741-9961-6372d6f29314 | -17.71159 | -46.7885 | 2026-07-01 04:40:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3c0a6692-c5e3-3861-9bf7-adf775cb7f84 | -17.7058 | -46.77935 | 2026-07-01 04:40:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9c0f67c8-58aa-3b72-8301-fd018204f1a1 | -19.51332 | -52.74589 | 2026-07-01 04:40:00 | NPP-375D | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 54b68fc9-7909-3878-97b9-9ea443673dce | -15.23999 | -48.56632 | 2026-07-01 04:40:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b57db4c8-462d-33b0-b950-a9b1d348c940 | -21.09715 | -57.46915 | 2026-07-01 04:42:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 37584e68-baae-3882-af13-517c20739af2 | -21.09256 | -57.46809 | 2026-07-01 04:42:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6f31f99e-8bf9-3bf6-995a-6ffa35c3b46c | -22.22906 | -50.86033 | 2026-07-01 04:42:00 | NPP-375D | RANCHARIA | SÃO PAULO | Brasil | 3542206 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |


[Clique aqui para ver as próximas entradas](README20.md)
