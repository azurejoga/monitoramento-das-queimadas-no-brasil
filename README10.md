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
| 3c85ec4a-138f-3cec-a047-bd21269cd28f | -12.43588 | -50.03051 | 2025-07-02 04:27:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a3600360-8d70-3a37-aafe-e66b167d3d72 | -9.22974 | -50.04273 | 2025-07-02 04:27:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4b61a659-a6c8-3716-96e5-a599125ad0cc | -14.90687 | -45.13964 | 2025-07-02 04:27:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a75bd142-0719-391c-ab42-5978e52b6002 | -9.19576 | -49.69371 | 2025-07-02 04:27:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 90460e7b-6038-367c-baee-3ae848e21ed5 | -9.24908 | -58.75301 | 2025-07-02 04:27:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e3d34dbb-672a-36d9-995f-6cf6502e3df9 | -10.99086 | -49.5414 | 2025-07-02 04:27:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d5465abf-8024-38ac-bd8c-9681935eea40 | -10.9948 | -49.38741 | 2025-07-02 04:27:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e0fa8c0e-1cc5-3d99-b630-d230da117732 | -10.29766 | -57.14044 | 2025-07-02 04:27:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| afba8db5-7539-34fa-8e22-50d5b1f69a25 | -11.33089 | -51.44872 | 2025-07-02 04:27:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3472933c-5cc7-387f-8055-8d8f7bbc7a8b | -9.79652 | -47.7458 | 2025-07-02 04:27:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| f216bc3c-a252-3349-a234-e4fb3943add2 | -10.50996 | -49.79125 | 2025-07-02 04:27:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 820bf6c5-0fe6-352d-ac96-34e3da8c885d | -11.14396 | -43.3272 | 2025-07-02 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 7.0 |
| de1822a0-4c88-3bb2-b0c1-98aac3405731 | -15.92556 | -43.51719 | 2025-07-02 04:27:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |
| dcc05b7c-eab8-355d-8623-23915c815a57 | -15.92156 | -43.51659 | 2025-07-02 04:27:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e48413d2-acd7-3d2c-a77e-f99ef9ad951f | -9.95838 | -54.17255 | 2025-07-02 04:27:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 8fd545bd-7f9f-3af3-afc0-58f0c115cf34 | -10.86458 | -53.78031 | 2025-07-02 04:27:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bfefa449-c7a1-3eac-8eec-320cb3382c16 | -10.30384 | -57.13793 | 2025-07-02 04:27:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f921e4c4-993c-3e46-929c-b14fc6ffaf71 | -12.43524 | -50.03437 | 2025-07-02 04:27:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6173fa90-4436-38bc-a04d-9afb44925238 | -10.24599 | -47.67908 | 2025-07-02 04:27:00 | NOAA-21 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a94ff9ed-e7ff-3527-a8ff-13a76a3bf262 | -12.61935 | -54.21089 | 2025-07-02 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d7a0735c-fcdb-3f48-843a-89e4a5e7cd69 | -8.35187 | -48.45787 | 2025-07-02 04:27:00 | NOAA-21 | BRASILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1703602 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 217845ad-a98f-3089-bb8d-c3abb9a33dee | -12.11092 | -43.6511 | 2025-07-02 04:27:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 983dc40d-0522-37c9-b868-f4307ffa65c3 | -10.8898 | -56.45335 | 2025-07-02 04:27:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| bd3f3d37-f9f1-3e61-a492-ac0d001f74cf | -14.44436 | -48.86517 | 2025-07-02 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f3440f5b-6762-3fa7-ac52-289bae2433a2 | -11.24198 | -49.48948 | 2025-07-02 04:27:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6f4349d3-8a21-31a1-b5d3-98fc9c77ff8b | -13.42499 | -47.81791 | 2025-07-02 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7af832a2-c820-3225-b98c-5a62de08c924 | -13.39255 | -47.85235 | 2025-07-02 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b710fd58-90b8-306e-806e-e02d97fc0429 | -13.41069 | -47.82281 | 2025-07-02 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 243e875e-3183-3ed6-9b95-4ec2d3880da4 | -11.58414 | -54.56915 | 2025-07-02 04:27:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 33c898f6-a7d1-311a-9ae5-577566cb75d7 | -8.00443 | -47.39296 | 2025-07-02 04:27:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 76a0874e-6dd2-3582-b89c-c25d7050a3f0 | -14.44711 | -48.8693 | 2025-07-02 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e036eab7-9d4f-3c1f-a0c1-61d80081a904 | -10.72918 | -49.48717 | 2025-07-02 04:27:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ac22ae10-8e59-3bfa-a8e5-0db11b4c7520 | -9.7921 | -47.75229 | 2025-07-02 04:27:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dbe4f67f-177f-3a4e-bd74-66bfd95277f8 | -11.14328 | -43.33193 | 2025-07-02 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 55c04b30-d572-3576-a204-16a69449a115 | -10.51061 | -49.78735 | 2025-07-02 04:27:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 93affcfe-f78f-3aac-9e27-eed3b94e8160 | -13.42888 | -47.84001 | 2025-07-02 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1719cb0c-24da-3b7a-bc49-cd1b75d7289d | -11.74536 | -54.72274 | 2025-07-02 04:27:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c3cc250c-ff6e-38f4-9f20-302fc8fe0af9 | -10.8661 | -53.77167 | 2025-07-02 04:27:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 35488220-d868-3961-a92a-f71bea921468 | -9.79596 | -47.74931 | 2025-07-02 04:27:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b5a6c9f8-f7f5-357c-a8df-d7302d40b7fa | -13.3854 | -47.85481 | 2025-07-02 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 425f8859-66ab-312d-bdeb-34c056cc5ae8 | -10.51126 | -49.78345 | 2025-07-02 04:27:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8e9656aa-af39-3c65-9cc8-0a79c7d595e4 | -10.24269 | -47.67855 | 2025-07-02 04:27:00 | NOAA-21 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1f1b3e0b-edd0-3573-9469-9a093be45cf5 | -7.3081 | -55.30714 | 2025-07-02 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| afbaefd6-eec5-354a-9acd-c559ede1ce5e | -14.35354 | -48.90134 | 2025-07-02 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 35c0d54d-37bf-34ef-ac2a-c51af2a8d58e | -9.04063 | -51.14198 | 2025-07-02 04:27:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0aa34c22-1a0b-36a7-9153-65c5b443d07d | -13.41839 | -47.81684 | 2025-07-02 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| b108988f-4b29-3def-96b2-124be098b549 | -10.25258 | -46.89719 | 2025-07-02 04:27:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 21baec23-1038-39a3-9541-031a1e24aafa | -9.24864 | -58.74739 | 2025-07-02 04:27:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fa915379-b8d5-374e-939b-d33f8737e304 | -12.6767 | -45.03817 | 2025-07-02 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| eed2baf0-b5f0-3a63-ba72-84c1e148ff72 | -10.64888 | -44.48867 | 2025-07-02 04:27:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 09c9b1e8-a03a-384c-aacf-be41f7f839de | -8.43916 | -49.19682 | 2025-07-02 04:27:00 | NOAA-21 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d6a2db5b-2453-3661-8836-c21a4853516f | -10.70901 | -49.67635 | 2025-07-02 04:27:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 557035d2-8ac4-3ada-89f9-053122b276ae | -11.74992 | -54.7236 | 2025-07-02 04:27:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e7de1134-2d43-3cf0-898e-685b17fea1ee | -10.87857 | -53.75188 | 2025-07-02 04:27:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 42a3d191-265f-3747-a2f9-d42c457b2ffe | -9.23599 | -50.02692 | 2025-07-02 04:27:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 666136c4-01c0-3b87-beef-5296fa4f2c04 | -9.25293 | -58.75834 | 2025-07-02 04:27:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 39d95df8-b756-3a4e-b2cb-14273dfb30c4 | -9.70368 | -56.18682 | 2025-07-02 04:27:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3d40bab9-17b3-35d2-b5b1-b2caf830d34f | -10.89501 | -56.45427 | 2025-07-02 04:27:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 97f4dc97-2577-323a-9b9d-46c6bdad0a35 | -9.25 | -58.74812 | 2025-07-02 04:27:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 01534d73-190d-3818-9ba6-70a607d1ca4e | -9.85372 | -44.70089 | 2025-07-02 04:27:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5e78214d-bd74-3a36-a899-460c6b466aac | -8.19422 | -49.67081 | 2025-07-02 04:27:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 42908777-9b0e-34e7-9d64-ed30834562ff | -14.44768 | -48.86572 | 2025-07-02 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0189c854-c91e-36bf-9569-460e3821e7f7 | -13.38925 | -47.85182 | 2025-07-02 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d73c81b8-8d02-3a26-b30a-40467e3b341a | -10.87498 | -53.74684 | 2025-07-02 04:27:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2f7a5537-6914-3c13-b7e7-bb3527ffe6f4 | -11.23794 | -49.49268 | 2025-07-02 04:27:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0731c12a-c416-32f8-9862-d1151e91ffdd | -9.70427 | -56.18357 | 2025-07-02 04:27:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6a8dfdf6-6988-3967-b26c-5ce085e114f5 | -10.89559 | -56.4512 | 2025-07-02 04:27:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| da0dbb2f-63c3-3c2f-ba60-8f9f4d16305d | -9.23041 | -50.03862 | 2025-07-02 04:27:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0bf3e41a-458e-3959-8408-33c6362c561a | -12.38538 | -44.25095 | 2025-07-02 04:27:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 378d3c57-8655-3c0b-9e4a-e7e44deb2927 | -9.23465 | -50.03512 | 2025-07-02 04:27:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0b98c571-a7ae-315c-b1ff-9fa893898a6e | -9.24769 | -58.75228 | 2025-07-02 04:27:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 164f8fe9-d79a-3cfa-bfe9-805463cc1359 | -10.68719 | -47.20664 | 2025-07-02 04:27:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7d034218-3bc4-30c9-85b1-c6b607f7f29f | -10.29835 | -57.13681 | 2025-07-02 04:27:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7dbd88d0-ad50-3431-a30d-9f835abc4104 | -10.86534 | -53.77599 | 2025-07-02 04:27:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dc495f5f-20a1-3cf0-a8c7-024cb43ca6d2 | -12.035 | -44.42754 | 2025-07-02 04:27:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 82b39bb0-752d-3e8e-880e-42582ede24b2 | -9.57579 | -49.10244 | 2025-07-02 04:27:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a171e03d-5c4b-3624-ac5b-5b75bbdfd3d4 | -10.45723 | -49.57985 | 2025-07-02 04:27:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 64185586-5596-31b4-9407-457c80de9059 | -9.85023 | -44.70035 | 2025-07-02 04:27:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9981174e-f1bb-3356-a5ac-7547a14b2adc | -8.43853 | -49.20068 | 2025-07-02 04:27:00 | NOAA-21 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fc512950-556b-30e3-a369-d9752401dcf6 | -9.79541 | -47.75282 | 2025-07-02 04:27:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 23fb1558-85f2-3733-8f06-b316c4070436 | -13.21177 | -43.12666 | 2025-07-02 04:27:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| fd987306-ef81-3167-8fe0-4d01aed310eb | -10.93085 | -57.1334 | 2025-07-02 04:27:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6da385fb-3f38-3a82-a7db-dad566730af1 | -10.88399 | -56.45555 | 2025-07-02 04:27:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 105e2ed6-c48b-33dc-a3b4-a9b2e6e56747 | -10.88459 | -56.45236 | 2025-07-02 04:27:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 9e0940b8-97d6-3738-a544-95e3178bd8cb | -15.14996 | -47.94248 | 2025-07-02 04:27:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2886e19b-2d57-3ee9-a102-43e2543fb99d | -15.07809 | -48.94559 | 2025-07-02 04:27:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4f53d3fe-d37b-3a50-93a8-49915d582453 | -8.3126 | -46.31479 | 2025-07-02 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1d1b2aab-bd77-377f-896c-d926eb5fe9e6 | -9.70411 | -56.18591 | 2025-07-02 04:27:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dc1c93e5-8ec4-3a20-96c9-532872f32472 | -13.41509 | -47.81631 | 2025-07-02 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b14c2c0c-e991-30f7-8f19-66c99b63d8d0 | -10.88216 | -53.75698 | 2025-07-02 04:27:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2e8f11e4-6937-3ad2-85fb-d6c9604694f2 | -14.48837 | -46.97932 | 2025-07-02 04:27:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ff1d0860-c4a5-3668-bba6-f4cc76d1a924 | -9.24111 | -50.0404 | 2025-07-02 04:27:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e4c6c0d0-708a-3aaa-865f-763badb7c6a7 | -12.43179 | -50.03377 | 2025-07-02 04:27:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2eb081cb-5ae6-33f9-bf05-ad7c8e9bf6d4 | -15.89505 | -43.45862 | 2025-07-02 04:27:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 24.3 |
| 245b1e9e-3929-3074-b9e8-0f0b51ec7b2f | -14.01634 | -45.52525 | 2025-07-02 04:27:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7530b644-ae25-3c7d-b34c-0703e389d96e | -12.76712 | -44.4035 | 2025-07-02 04:27:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ad638b71-6b77-356f-9794-9bd2e5018141 | -9.23108 | -50.03453 | 2025-07-02 04:27:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 22761350-8b77-308c-bc4a-e94e6bd90a35 | -10.88582 | -56.44589 | 2025-07-02 04:27:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 075ddab4-1379-35b1-acca-a0b4e7ed4e70 | -9.57237 | -49.10189 | 2025-07-02 04:27:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 380a7dc8-7eb9-3011-8084-b2961c655d4f | -11.23856 | -49.48891 | 2025-07-02 04:27:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README11.md)
