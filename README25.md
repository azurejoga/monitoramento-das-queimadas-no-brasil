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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bff38634-70e0-3715-80ec-b43fe1c1ba66 | -8.53562 | -37.72567 | 2025-08-24 03:42:00 | NOAA-20 | IBIMIRIM | PERNAMBUCO | Brasil | 2606606 | 26 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 54506bd9-65d2-37f4-8ef5-9cae87b8b55d | -6.31051 | -43.76258 | 2025-08-24 03:42:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b398c3fb-a854-3cd2-9004-1819ffb2ae33 | -10.54521 | -47.14377 | 2025-08-24 03:42:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| aeeb50ef-6554-3c86-be66-aad2d06bf487 | -7.25024 | -45.3717 | 2025-08-24 03:42:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3639027b-c8b0-36b2-9d18-cea0a2d6779f | -10.40872 | -47.19566 | 2025-08-24 03:42:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 297b7a0f-6c56-34d9-a868-1eb4d81686c5 | -7.62569 | -45.24181 | 2025-08-24 03:42:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b0096cd5-5dd1-3753-9b4e-afd55972d54c | -6.46865 | -43.46763 | 2025-08-24 03:42:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3b57678f-56c5-3033-b677-784c7ecc1354 | -6.71245 | -43.86068 | 2025-08-24 03:42:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3b39b7d6-14ee-3d40-a934-6237eec55bbd | -10.54607 | -47.1394 | 2025-08-24 03:42:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 03f9c1d5-f00f-3cc2-894e-48424c8501de | -7.81133 | -46.62335 | 2025-08-24 03:42:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 38a90b94-6de3-30ce-9b58-eab7a7b6760c | -11.12341 | -44.79388 | 2025-08-24 03:42:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a37970b7-2ff0-33c2-8827-4c2d3362d3d3 | -10.41143 | -47.18196 | 2025-08-24 03:42:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 482c668a-4451-371a-8935-107870e9612e | -9.61683 | -48.32962 | 2025-08-24 03:42:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5795e450-a65c-3ec4-b0b3-d6687bf423b6 | -6.4688 | -43.46657 | 2025-08-24 03:42:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2f37dc4f-8415-3955-8b69-64a493003a76 | -10.80353 | -46.40746 | 2025-08-24 03:42:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ab1fa8ff-b359-3561-aed2-06d5c27de758 | -7.0322 | -44.6638 | 2025-08-24 03:42:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| e13e645a-70c1-36a6-9b08-c293b953e5c7 | -6.10904 | -44.36485 | 2025-08-24 03:42:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cfe111e9-a7f4-37ea-9d30-e4b69a2b5193 | -8.77038 | -49.96138 | 2025-08-24 03:42:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e33e05d1-eef2-3ae1-8843-491676b14d89 | -6.03807 | -44.00217 | 2025-08-24 03:42:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 59f6fbf7-e59e-3099-b8a5-d5a5ac5d97fe | -10.4819 | -46.45458 | 2025-08-24 03:42:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a637b487-07d8-3d37-ba18-944ecb581891 | -6.89327 | -45.69051 | 2025-08-24 03:42:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| bca28aa6-2e91-357a-b75f-2f26ff79865b | -7.61954 | -45.24445 | 2025-08-24 03:42:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f28d369a-b3bf-3c5a-a216-0adb31438d94 | -6.87667 | -45.68407 | 2025-08-24 03:42:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e6263ae1-efeb-34a5-8365-67d96533892b | -7.75165 | -47.35225 | 2025-08-24 03:42:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 07b071a4-0d14-35ca-bcca-f80fde2c236b | -10.60215 | -44.32134 | 2025-08-24 03:42:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 22.3 |
| 4718e827-83c2-35bd-87d7-7cba2179dc7e | -6.88673 | -45.69395 | 2025-08-24 03:42:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 3eb8f770-ad8c-3a17-9b2e-6cb4d1c2b707 | -6.89177 | -45.69889 | 2025-08-24 03:42:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| b284cd1b-7ebe-3084-90a8-329b21fa540a | -6.91323 | -43.78003 | 2025-08-24 03:42:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| fc41645e-347d-39e7-a091-50002ab6cba1 | -10.60603 | -44.32794 | 2025-08-24 03:42:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 38.8 |
| 230d21dd-8a31-3418-8692-b7bed07f592f | -7.48207 | -44.93332 | 2025-08-24 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8071f9bd-966e-39a5-b7cb-a53d7c235a17 | -9.73501 | -47.93903 | 2025-08-24 03:42:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9b1d20b1-e939-313a-936f-d444da7ea570 | -8.21504 | -45.1175 | 2025-08-24 03:42:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1dec63ba-2802-3585-8d8f-72b4df526971 | -11.15439 | -44.71173 | 2025-08-24 03:42:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7ca5c0f0-855a-3537-914a-b7ae306af58c | -11.10284 | -44.76514 | 2025-08-24 03:42:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b2f717d4-7089-3c46-9d07-02b5d9fa93e9 | -6.4698 | -43.46067 | 2025-08-24 03:42:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1f286262-4082-3242-bd52-32e5f035a1dd | -11.10558 | -44.77809 | 2025-08-24 03:42:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 20cdd125-b78c-3ae5-823f-121073a742f5 | -10.41055 | -47.18643 | 2025-08-24 03:42:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 003ac668-473b-332f-b7d9-556f7c72e180 | -5.74721 | -40.44856 | 2025-08-24 03:42:00 | NOAA-20 | INDEPENDÊNCIA | CEARÁ | Brasil | 2305605 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 8a1120ba-95bc-3791-adcd-7783a54a471e | -9.0231 | -47.64612 | 2025-08-24 03:42:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 13f4f056-3778-359c-a77f-2d39e494a6ac | -10.80485 | -46.40067 | 2025-08-24 03:42:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f416a18d-82f9-3c2c-8083-1f11435917b7 | -7.42828 | -45.41929 | 2025-08-24 03:42:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3d0f6387-12f1-3b77-ae91-75c09d1ab2b8 | -10.40633 | -47.17661 | 2025-08-24 03:42:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a1367675-ad05-39b4-8dc2-16427140b04e | -10.80075 | -46.40485 | 2025-08-24 03:42:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 89bd0d67-5cf7-38e8-b47d-62a5ff69fafe | -6.58594 | -44.56081 | 2025-08-24 03:42:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4909e20c-72bf-30e7-95e0-7003f8e07406 | -7.91331 | -45.90331 | 2025-08-24 03:42:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1c501a7c-9628-3067-a9a1-62c46c5e0558 | -8.11318 | -47.1428 | 2025-08-24 03:42:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 74b51e39-3f6a-3b82-9396-e95cfc8fe56f | -10.40365 | -47.19012 | 2025-08-24 03:42:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5274b784-2ddf-3445-a49f-d83465f832d3 | -9.60267 | -40.57019 | 2025-08-24 03:42:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 6a4b6ee7-e2d4-330d-a9ab-b223c0119aff | -6.06449 | -43.4539 | 2025-08-24 03:42:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c072b51f-c7d7-3700-b690-3b64f0b1c971 | -6.79576 | -44.99847 | 2025-08-24 03:42:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 30cc85a3-6ce8-3fa0-91ac-71189a2b0d13 | -7.18654 | -44.68119 | 2025-08-24 03:42:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 51569c4c-94ae-3182-b926-91ce8ed8bb1a | -9.62336 | -48.33045 | 2025-08-24 03:42:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2468e0b0-9ffb-3370-8ae3-189fcc06fabc | -10.57662 | -47.1399 | 2025-08-24 03:42:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bdc5045b-2642-3d18-bfa9-7663c6a2cd9f | -5.4983 | -41.40244 | 2025-08-24 03:42:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| cc7c5199-b426-31e8-bed6-6aa4443fde89 | -7.01986 | -44.64051 | 2025-08-24 03:42:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 9cb87743-952b-35e8-98c3-df2a0c089717 | -8.16714 | -34.95058 | 2025-08-24 03:42:00 | NOAA-20 | JABOATÃO DOS GUARARAPES | PERNAMBUCO | Brasil | 2607901 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 5a9a421a-7b79-3b9e-ad17-041c845119bd | -6.89402 | -45.68634 | 2025-08-24 03:42:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 2aa3be00-ad5b-3978-9300-c65a6ebab4bf | -8.06643 | -49.65704 | 2025-08-24 03:42:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 76d1714b-4155-3e16-81f3-a5b71acf3a52 | -5.88112 | -43.38477 | 2025-08-24 03:42:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4c20d13e-c6d4-3cbc-ab85-e280e475e407 | -5.58599 | -43.24761 | 2025-08-24 03:42:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ae6b9735-5479-3340-8526-bc628b155796 | -7.59606 | -45.24849 | 2025-08-24 03:42:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6cee9bc8-3464-3014-b4ff-6bae53bcedc6 | -7.42897 | -45.41554 | 2025-08-24 03:42:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dd4b9526-a58e-364c-aeae-a6c36c0c34e6 | -7.00664 | -41.37208 | 2025-08-24 03:42:00 | NOAA-20 | SUSSUAPARA | PIAUÍ | Brasil | 2210938 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 56b23e03-52b9-3c51-9b31-f84fd4bb8ca8 | -8.21677 | -45.11874 | 2025-08-24 03:42:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f487bde6-921f-3c1f-8bee-ee9ffa39bbe7 | -8.74814 | -46.75557 | 2025-08-24 03:42:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1f053b72-3c79-34d1-868a-c80911be6988 | -6.23204 | -44.12877 | 2025-08-24 03:42:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b64c14cd-2edc-3b00-9372-cef5d09966d4 | -6.59122 | -44.56216 | 2025-08-24 03:42:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1cb3ce2e-743c-3b38-beb8-24362b7b8374 | -6.12629 | -44.39161 | 2025-08-24 03:42:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3df93849-6e77-3c29-a634-57eb2fa29e1a | -6.87595 | -45.68808 | 2025-08-24 03:42:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 67be924d-d7c1-336c-a90d-fe1c55c18dd5 | -8.18043 | -45.09284 | 2025-08-24 03:42:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8cce02bb-7031-37f6-b114-dd9838d4dcb9 | -10.53844 | -47.14699 | 2025-08-24 03:42:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1bf7d90f-0ba7-36d9-ad1e-6d1e83b66bd0 | -7.01862 | -44.64734 | 2025-08-24 03:42:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| f4e463b4-c924-3845-825d-cc914edde6d6 | -6.03283 | -44.00143 | 2025-08-24 03:42:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 868bf6dc-8433-3a01-a9b7-b24c6ed8b285 | -10.60111 | -44.32699 | 2025-08-24 03:42:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 23.7 |
| 649c9514-e4ce-3f22-9c1c-e2e4f49d9caa | -10.40047 | -47.19043 | 2025-08-24 03:42:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 59bac114-8dd2-313d-9fbd-42dbf3513b96 | -10.29277 | -46.75078 | 2025-08-24 03:42:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 20e28951-ccbc-383e-8598-20c98bfa10dd | -6.71193 | -43.86362 | 2025-08-24 03:42:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b212ab0f-75d5-3246-a034-46bfd060c8ee | -10.8262 | -46.41071 | 2025-08-24 03:42:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| cf5d1b29-8001-339e-853d-ebf6fccd0996 | -10.40816 | -47.18241 | 2025-08-24 03:42:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 06620b7f-eb11-3a63-bc99-072e086bb8f0 | -10.53931 | -47.14259 | 2025-08-24 03:42:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fb8a4252-d0cc-32b0-bf84-f011a37720f8 | -6.14194 | -43.15531 | 2025-08-24 03:42:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.9 |
| d8dc5aa3-fa89-365c-b1a2-d6f6bcec2261 | -5.41565 | -44.98687 | 2025-08-24 03:42:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3e249a76-b92b-36c8-aec7-4c9893fd7c8b | -5.66202 | -45.15783 | 2025-08-24 03:42:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a060bda0-a723-39fb-b8a2-7793ffa0e461 | -7.02285 | -44.63661 | 2025-08-24 03:42:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| ded010f0-f261-376d-afe1-1149bbe03ee5 | -7.07838 | -44.62143 | 2025-08-24 03:42:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9a8e5c83-aa9a-365c-87f0-d7ba53b037f8 | -9.81718 | -46.44567 | 2025-08-24 03:42:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 95f8e531-6cb9-395e-902f-d3253255524e | -7.69898 | -42.12887 | 2025-08-24 03:42:00 | NOAA-20 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 038c2ff2-3c03-3848-b519-e15373b249d7 | -10.60705 | -44.32231 | 2025-08-24 03:42:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 6039a572-05ca-34cc-ae55-fa8d35a832b5 | -7.0258 | -44.63816 | 2025-08-24 03:42:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| de342690-2d4a-3e89-8ab2-f5afd25019ad | -7.18121 | -44.68013 | 2025-08-24 03:42:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5f0371a6-fbf6-31f7-bf29-2c8e3a7dd95b | -8.84057 | -49.9086 | 2025-08-24 03:42:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 27acd6ee-8f65-3331-881d-b1dcfd8c1df0 | -9.24681 | -48.19659 | 2025-08-24 03:42:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 9a41a37f-1ee5-3de7-848f-50a6d88dd981 | -11.11895 | -44.78995 | 2025-08-24 03:42:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 00574c53-a92f-3f94-8cf0-9ab0a9b1803d | -7.62502 | -45.24554 | 2025-08-24 03:42:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c60f0da7-1d51-3743-8f73-736ec5939655 | -7.50385 | -43.90054 | 2025-08-24 03:42:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 04bb70f5-e580-33d4-b5d7-44868ed429cf | -10.80834 | -46.4127 | 2025-08-24 03:42:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 45fd1de9-1c11-30df-9590-9464a147dcc9 | -7.47656 | -44.93289 | 2025-08-24 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6504e874-e5ce-3c23-a278-b99bf05782f8 | -11.10944 | -44.78515 | 2025-08-24 03:42:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9db325ee-b6cc-3323-b55a-ab8939646c53 | -8.23434 | -47.46689 | 2025-08-24 03:42:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e9ef11d7-c44a-3116-a050-283289630349 | -9.80295 | -46.42656 | 2025-08-24 03:42:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README26.md)
