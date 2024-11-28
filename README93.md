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

## Dados Diários - Página 93

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5150ec83-caa2-3399-9e7d-2101cf2e6b16 | -2.6327 | -51.76958 | 2024-11-28 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a404cca7-1ecf-32ba-9168-2ec73a0adaeb | -1.62836 | -55.71022 | 2024-11-28 05:40:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 342907ff-7577-3f3c-b9a2-8c55d00292bc | -3.24154 | -53.93398 | 2024-11-28 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c1f7c1d9-bf8a-3bd7-ab5f-d27b10d871b4 | -0.45286 | -52.01595 | 2024-11-28 05:40:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4bf1f439-b272-3232-9e27-e99e5e0814df | -1.49803 | -54.46476 | 2024-11-28 05:40:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 4ba892f8-94a0-3392-9a01-1da7ca2b07f9 | -3.249 | -53.64053 | 2024-11-28 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 99d88161-8c94-3634-b92f-cae5c2ec4534 | -3.24967 | -53.63602 | 2024-11-28 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9b155a2a-ad1b-3312-b3af-8ba39ac00f06 | -2.23165 | -55.89893 | 2024-11-28 05:40:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bec3a9b1-076b-3fab-807d-4d6da20d55ea | -4.09308 | -54.76293 | 2024-11-28 05:40:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 71e3b149-7cc7-391d-8d51-a4118222e924 | -3.91873 | -53.67193 | 2024-11-28 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 6935bba7-970a-3fbf-adae-416d6d3acfd5 | -1.69135 | -52.4929 | 2024-11-28 05:40:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 46ed89be-9123-3430-a3ff-d44233a8c03f | -1.68076 | -52.43417 | 2024-11-28 05:40:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bc8de9ee-f4de-3c65-b8c8-aa65e602dd61 | -0.36184 | -49.95451 | 2024-11-28 05:40:00 | NPP-375D | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e9c16638-78fd-32f2-a1d5-c558ccc475e8 | -3.27282 | -50.62043 | 2024-11-28 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e1a07b44-fbf6-3fc8-a22a-02fefa0e05f5 | -1.4986 | -54.46098 | 2024-11-28 05:40:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 1a735b8b-744b-304b-8f4c-e39396fa6dbb | -1.1546 | -53.56988 | 2024-11-28 05:40:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 36fb33e6-c809-357a-9fe6-5d039d6f23fe | -3.50061 | -53.80814 | 2024-11-28 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fcc6593f-c38f-3e61-98a3-7928c078ebe7 | -2.59578 | -53.97571 | 2024-11-28 05:40:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cf0e0c57-355b-32e8-acc3-b660648f9426 | -2.90268 | -54.17833 | 2024-11-28 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| cef4fcee-e2ac-364a-b25a-6adc2228b600 | -1.78637 | -52.73709 | 2024-11-28 05:40:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 78c9450c-aa30-3a99-8f18-c105f23bcc92 | -1.61823 | -53.87075 | 2024-11-28 05:40:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0df6bc28-e91a-3cc9-bf27-585e5b044e49 | -0.45923 | -52.01717 | 2024-11-28 05:40:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8e4f498b-0e28-3bd8-bfe3-4f8e43854468 | -3.34132 | -50.51811 | 2024-11-28 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 514e9092-bde4-3a8a-a7ba-6b3ca068654c | -1.36688 | -55.01468 | 2024-11-28 05:40:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 75a85b54-d82d-3d49-a1d5-623e799b2474 | -2.89758 | -54.17541 | 2024-11-28 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ccb0f360-6c47-35d6-8e62-acbcfb63c8f5 | -3.50001 | -53.81227 | 2024-11-28 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0034715f-1c6c-34e1-b508-7e0498dcf4c9 | -1.59092 | -52.27628 | 2024-11-28 05:40:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| de53fcd8-5a97-3f35-86bb-70bff92d21a9 | -1.64299 | -52.46983 | 2024-11-28 05:40:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 5e40680c-94a7-3092-9c9b-78936c6907e3 | -2.59729 | -53.96965 | 2024-11-28 05:40:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 44b2f25e-018b-3e93-804b-d5293c19e3f1 | 1.24373 | -55.93562 | 2024-11-28 05:40:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b8dd9ace-a772-3d97-9f1f-27ff501d322b | 1.24685 | -55.92455 | 2024-11-28 05:40:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b07a1e6c-3dd2-3b12-8d40-93ed32e10299 | -2.82896 | -54.11981 | 2024-11-28 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b3301a9d-11d5-347c-9e27-8c01de6b05f4 | -3.30458 | -54.17731 | 2024-11-28 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 128b74e8-db7a-3cf7-abe8-c13ce2f86bd8 | -1.5811 | -52.26493 | 2024-11-28 05:40:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e2420599-9bb7-326b-8957-73550ecc1857 | -3.36969 | -50.82859 | 2024-11-28 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| cb5ddee5-55de-303d-9c1e-c0e2e351ff1b | -1.32208 | -51.92489 | 2024-11-28 05:40:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| d0fb069f-f536-3c8d-8cad-2ec1b0ca8f4e | -2.94004 | -51.58665 | 2024-11-28 05:40:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e4af972e-9fd1-35ca-838e-68384da9986b | -2.59699 | -53.96743 | 2024-11-28 05:40:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5561d393-6f64-3ac6-a306-2262bb8fa21f | -1.44362 | -52.60045 | 2024-11-28 05:40:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a97e9c43-b488-3a14-b371-5f8083e3919f | -1.06713 | -53.6397 | 2024-11-28 05:40:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c6f55910-3658-301a-bb58-4da77fc93ccd | -4.22399 | -50.88651 | 2024-11-28 05:40:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1d1d672e-61ad-3805-9adb-6255ee8dea9e | -2.94943 | -51.58124 | 2024-11-28 05:40:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 616e9ef9-b626-31d5-89aa-16983c9056d3 | -2.83476 | -54.1207 | 2024-11-28 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 36578383-a06d-321f-968f-9081dd885245 | -3.10474 | -53.81625 | 2024-11-28 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 6bf7219c-26e6-32b6-a658-3dba3d171760 | -1.68711 | -52.43516 | 2024-11-28 05:40:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| de6f02b4-858f-3d5b-bf01-befc9083777c | -3.06243 | -51.058 | 2024-11-28 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7359bdb5-69c5-339d-9508-cfce4cc7cd7b | -3.34752 | -50.52659 | 2024-11-28 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| fa3ada5d-24ba-393c-9759-15e64871d2ca | -1.70586 | -54.72297 | 2024-11-28 05:40:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 873ac8f0-fae1-3345-8f44-72dcd8fa028f | -3.57156 | -53.02537 | 2024-11-28 05:40:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d2dc62b4-7c2e-3ef2-b385-d4cd408c7895 | -1.16293 | -53.67339 | 2024-11-28 05:40:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6e2b8235-a646-3f10-91ce-a79e58c608cf | -2.25189 | -53.46306 | 2024-11-28 05:40:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 09723467-898e-38e2-b8ad-182ed23638da | -1.56786 | -55.78252 | 2024-11-28 05:40:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4265d07a-4f40-36de-bfeb-f1abb59bc2e2 | -0.24094 | -51.5929 | 2024-11-28 05:40:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4839d28b-bec5-31b1-831c-13154a58dc62 | -3.10607 | -53.25819 | 2024-11-28 05:40:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b0d2c223-305f-30bd-9635-a760b9523977 | 1.25648 | -55.92296 | 2024-11-28 05:40:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7706fefc-f503-38f8-b2f7-551344a93d49 | -1.30214 | -55.7445 | 2024-11-28 05:40:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 6e9391d4-ed88-38d6-a763-09508ea9e20d | -1.64384 | -55.22902 | 2024-11-28 05:40:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 247bda77-bb42-3bfd-a9d4-dfda0d9c85b4 | -2.94684 | -51.58768 | 2024-11-28 05:40:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d2f71cea-0dba-3da0-8057-bf998e945bfe | -1.16257 | -53.67817 | 2024-11-28 05:40:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 69a447f4-32e5-3686-9094-33baebf5da91 | -2.96534 | -51.00726 | 2024-11-28 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e895e71a-db99-313f-a503-71c800aa0459 | -1.08826 | -53.36339 | 2024-11-28 05:40:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3f9735eb-443b-301e-ae64-8977cf745d5a | 1.43774 | -55.89662 | 2024-11-28 05:40:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8337786a-fd34-3bbd-937b-f6ecd8688a18 | 1.24288 | -55.93045 | 2024-11-28 05:40:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7deee6d9-b932-3854-bc00-1370adbb10d7 | -3.50027 | -50.50129 | 2024-11-28 05:40:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| be43d900-d12c-3214-ab99-a9cc7e4be51a | -4.09462 | -54.76561 | 2024-11-28 05:40:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 04943678-a915-3d08-bd5a-71db2dcc2912 | -1.15981 | -53.5752 | 2024-11-28 05:40:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4559488d-cc78-39f8-a651-ef1b3b6dfeac | -1.64208 | -52.73337 | 2024-11-28 05:40:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| e58e8356-09fe-3072-8b6c-f4cde48a3f97 | -4.2166 | -50.89798 | 2024-11-28 05:40:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 56ae7270-1cbb-3192-a050-e7e8d81bb89b | 1.24054 | -55.93737 | 2024-11-28 05:40:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d02d0e21-4ebc-38f8-abc7-fafe739c51ae | -2.25824 | -53.74671 | 2024-11-28 05:40:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 48e41436-7d40-37f2-a146-018ce6b95318 | 1.24936 | -55.93064 | 2024-11-28 05:40:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ce5bf682-44f3-3f3f-85fb-ff7f4b87c1ca | -2.80608 | -51.59435 | 2024-11-28 05:40:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b6ddf02c-25fa-3ce6-97cb-f9a4d9741ef6 | -1.38924 | -54.99725 | 2024-11-28 05:40:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ac0d7cb9-639e-33bc-a8a3-1608c15eb4f1 | -2.14625 | -54.82028 | 2024-11-28 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c418aaa8-287d-3548-8f9d-06d36ea08a64 | -3.10537 | -53.81199 | 2024-11-28 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 89e677b9-ab81-38a1-a499-ec196b602812 | 1.44649 | -55.91236 | 2024-11-28 05:40:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2b364cbc-6459-3e10-9ebc-76b52523e22c | -1.62407 | -53.87132 | 2024-11-28 05:40:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6de2fc60-a987-3d44-951d-f2236c51ba09 | -2.1468 | -54.81676 | 2024-11-28 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6f0627c4-66f6-334c-a5d0-39acd1dc4c6c | -1.57893 | -52.26912 | 2024-11-28 05:40:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| ca154a1e-d0de-3dab-bd57-717b604c78cb | -3.1115 | -53.26393 | 2024-11-28 05:40:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bdfb6a0d-ff77-3ea3-a0ac-0d9464606de2 | -1.16046 | -53.57087 | 2024-11-28 05:40:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e724db73-98ed-3da1-95fe-30c8a793189b | -3.80314 | -52.35963 | 2024-11-28 05:40:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dc591871-6f9c-3f07-82b5-23f0bc671a5e | -2.2612 | -53.46704 | 2024-11-28 05:40:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ff053341-c6cc-329e-8393-e9df1eda76a4 | -2.23107 | -53.68618 | 2024-11-28 05:40:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 62b512dd-5afe-3026-aa84-5091577eeb46 | -1.67936 | -52.43304 | 2024-11-28 05:40:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c5362d3d-da97-39e7-ae60-97c8ebc19fab | -3.39589 | -54.28481 | 2024-11-28 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3a1dcd05-4124-316d-b128-3adc219f7d04 | -3.39496 | -54.28856 | 2024-11-28 05:40:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7f12da30-aa84-3e1d-85c9-a7c1a49c09aa | 1.24855 | -55.92548 | 2024-11-28 05:40:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 186d80a1-7dfd-3533-b36e-c7e9d88ef44c | -3.05891 | -53.27949 | 2024-11-28 05:40:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 858fb6fe-68cd-3a27-8b48-0aba89ced208 | -1.56277 | -55.78175 | 2024-11-28 05:40:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4ec8b28d-fd99-3c7e-a1c0-16037c29cde5 | -1.04028 | -51.73611 | 2024-11-28 05:40:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 99d704e5-452a-30e8-a82e-3e191010d809 | -2.31531 | -51.95834 | 2024-11-28 05:40:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| a5b95ed6-3196-370f-b059-6b853aa2df54 | -1.15747 | -53.67273 | 2024-11-28 05:40:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 381738d4-666e-3fd5-a23a-367c548ab25c | -1.66775 | -52.73236 | 2024-11-28 05:40:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 9c6350f5-4f04-3862-a4e0-269944b2c832 | -2.60344 | -53.96416 | 2024-11-28 05:40:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ab56ce1e-d849-39dd-b88c-45ae7e8adbc8 | 1.2477 | -55.92968 | 2024-11-28 05:40:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 077b3e2e-172e-31c6-a0e0-7722abf00bf3 | -2.60313 | -53.97051 | 2024-11-28 05:40:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ce291f3a-508b-3198-84d9-36e856d9c51a | 1.8866 | -60.48447 | 2024-11-28 05:40:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f75e94a4-18d1-34a0-bc86-6a8c9c1a9c26 | -1.5623 | -55.78471 | 2024-11-28 05:40:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d8aa4270-f4ad-3a11-945f-aa6bb400b488 | -1.1609 | -54.0697 | 2024-11-28 05:40:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README94.md)
