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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2e12bb34-b2ad-38d3-90ea-bd43fc06a2b2 | -5.77942 | -51.66701 | 2025-08-05 04:17:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| de5df7cb-ff94-31db-bddf-4ded9ee346d7 | -6.54818 | -44.01596 | 2025-08-05 04:17:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 007f81bb-60ee-3bc1-9cc9-d87b609b94bf | -9.62129 | -48.49167 | 2025-08-05 04:17:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 81e7d9ef-beb5-3262-a0be-252e1e9c40bc | -7.39596 | -44.63387 | 2025-08-05 04:17:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 106c5eb2-4ca1-3bff-bdb1-a6372a48d3de | -9.65817 | -47.12771 | 2025-08-05 04:17:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 72dc91d2-90c8-30e4-8f8d-06d197d47a6b | -9.05663 | -45.06289 | 2025-08-05 04:17:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6b378b4f-3799-354b-8337-a5bd1963e91a | -7.38509 | -45.28623 | 2025-08-05 04:17:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1f74a67b-0fe8-3506-8297-1221129533b2 | -8.8467 | -47.60765 | 2025-08-05 04:17:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b2f92c34-ad61-3fee-9531-5ded71aa9bd7 | -11.92153 | -44.95921 | 2025-08-05 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 4445ab5a-779e-3606-bb81-564eb3173b34 | -8.15471 | -49.14383 | 2025-08-05 04:17:00 | NPP-375D | JUARINA | TOCANTINS | Brasil | 1711803 | 17 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 333c89c1-aaa5-3dc0-87c5-9b0ff30212af | -11.9143 | -44.96165 | 2025-08-05 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6eee0f71-ed87-3242-855b-02ec73d378c1 | -9.40262 | -45.49267 | 2025-08-05 04:17:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9aa3584b-8c47-3568-8a73-10092924f6a7 | -11.7517 | -45.00846 | 2025-08-05 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3782c38d-ad09-33ff-81b6-b40c2994ad0a | -17.20925 | -44.83273 | 2025-08-05 04:17:00 | NPP-375D | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| dcc95fe6-9417-3889-835b-c99935eea34e | -11.92429 | -44.96332 | 2025-08-05 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 5c23ece7-94f5-3384-9aac-b2f665a36b14 | -7.85239 | -46.73465 | 2025-08-05 04:17:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a2f9eb8b-68e4-3b80-9302-7faea7038a81 | -17.21651 | -44.82225 | 2025-08-05 04:17:00 | NPP-375D | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0de22a7d-5bd8-3d47-aae3-7ce8174bee84 | -7.56681 | -44.87286 | 2025-08-05 04:17:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0b8fba68-0567-31b9-840f-7fae3686e0bf | -8.37964 | -46.57528 | 2025-08-05 04:17:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cfff32a2-ffbe-3820-ba85-232bfa58a9d8 | -5.80871 | -46.98455 | 2025-08-05 04:17:00 | NPP-375D | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7c8a6dcb-93c0-3641-bf03-f3c70d5189fd | -7.3704 | -44.16502 | 2025-08-05 04:17:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dc258665-9a3c-3f73-8cc9-cd0ace5c98c3 | -6.3796 | -43.71469 | 2025-08-05 04:17:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e02f09a8-4089-3e08-a57e-ac34d1b5a9d4 | -12.22492 | -44.19773 | 2025-08-05 04:17:00 | NPP-375D | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7319a740-3352-33a0-b72b-69275c4f74ac | -7.56666 | -44.87337 | 2025-08-05 04:17:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 83b165aa-c2ef-3572-a3d6-4447231ee2a5 | -12.54847 | -44.72407 | 2025-08-05 04:17:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 338369a5-0ffc-37cc-9564-be1191ef4e5f | -11.77075 | -44.97495 | 2025-08-05 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 79df78e5-7a89-3513-98a4-33115155247e | -8.87981 | -44.79038 | 2025-08-05 04:17:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| af5ee2de-6a2d-3c40-a5f4-b50b7f4c6492 | -7.56943 | -44.89959 | 2025-08-05 04:17:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6202c334-4e46-3472-9858-04bb2fa6daf5 | -9.40081 | -45.50385 | 2025-08-05 04:17:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ef8609c0-8f82-3440-a5f7-ecc77a71f9ca | -7.76036 | -45.22972 | 2025-08-05 04:17:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3a92088c-b998-3b5b-9234-2bc3ff1b931f | -12.51931 | -47.18571 | 2025-08-05 04:17:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7a1cab24-87bb-379c-9522-7c0ae96a15b6 | -12.72586 | -45.07753 | 2025-08-05 04:17:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e05ee2cd-4a6d-37c9-aa60-07538725d310 | -7.14093 | -44.08106 | 2025-08-05 04:17:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a660c8b2-2025-3c03-9b6c-904af7d6de1a | -8.13482 | -49.58702 | 2025-08-05 04:17:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 334af829-f670-30c3-9e62-08d59e4a4d23 | -5.82435 | -46.35001 | 2025-08-05 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 352707b3-0830-39b2-b346-dc6a71b9669f | -11.92047 | -44.94451 | 2025-08-05 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fa52f390-7441-3c3f-a7db-1787b611186a | -11.81647 | -44.25805 | 2025-08-05 04:17:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5064cba4-0630-3d6f-be17-623165d3eaa6 | -7.75975 | -45.23345 | 2025-08-05 04:17:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 70965091-16a9-3481-8e37-d30cd7607d98 | -10.79825 | -47.25835 | 2025-08-05 04:17:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| adf4bfd5-ef7a-3c4b-9f46-37e4cf810f08 | -6.4222 | -44.82009 | 2025-08-05 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ee8ec596-93e0-3bf4-b372-b5babaa34153 | -8.01568 | -43.12971 | 2025-08-05 04:17:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 5f48fd7a-e5fa-334e-86bd-f4debf9a3405 | -10.77848 | -46.64149 | 2025-08-05 04:17:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7d18284a-09f2-381e-82d7-b53bafe45f17 | -11.75194 | -47.54151 | 2025-08-05 04:17:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d421b33e-3c29-393b-83c8-c914a9948f33 | -12.51862 | -47.18979 | 2025-08-05 04:17:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 49a9ed10-74c6-366d-afca-a06879ce6b0d | -10.47848 | -44.37248 | 2025-08-05 04:17:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0138457c-111c-3218-9096-ecd154c7c6d9 | -5.77476 | -51.66297 | 2025-08-05 04:17:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4e355a76-a76d-3e7a-aa54-7cd795c2d15a | -11.76114 | -45.01368 | 2025-08-05 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b0f45c7f-4d65-3e5d-9736-db8b5b1379ea | -7.14349 | -44.46446 | 2025-08-05 04:17:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8322affb-8e91-30ad-b147-2982c65d128a | -8.947 | -46.7338 | 2025-08-05 04:17:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 17.8 |
| d08818a6-323a-393b-8f68-1baead2fc439 | -17.20704 | -44.82488 | 2025-08-05 04:17:00 | NPP-375D | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 11.1 |
| ef41c5da-5a81-32e6-9f78-f6c8a0e32bed | -8.23551 | -45.05887 | 2025-08-05 04:17:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 60c72529-2ff5-32cb-8070-98f61fcf35b6 | -11.91487 | -44.9581 | 2025-08-05 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 424c2c8a-591c-3ff2-9fb2-af266360d50e | -5.77997 | -51.66389 | 2025-08-05 04:17:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 6c19deb5-8e62-3049-8550-ee18ebcc9872 | -11.7864 | -44.99919 | 2025-08-05 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 32597611-1932-36a0-a98a-af1119f8ddfa | -11.91763 | -44.9622 | 2025-08-05 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 933dabdf-eef5-3554-8b76-f80ed7ec4c01 | -6.95897 | -44.50169 | 2025-08-05 04:17:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| eb70183e-ddb2-340b-bb6a-a13c0ab5667c | -11.7925 | -45.00388 | 2025-08-05 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a8c1293c-f569-3ff1-8b13-15e392053d40 | -17.22263 | -44.82701 | 2025-08-05 04:17:00 | NPP-375D | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 54f75fc8-4fea-381f-a358-5d5d70a8a6fe | -7.07009 | -43.6963 | 2025-08-05 04:17:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 96b56f39-48e0-3588-8bf6-a32b070d8c79 | -7.11759 | -47.84285 | 2025-08-05 04:17:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 9b119961-2318-3340-a77c-e0d2bebfa216 | -7.39423 | -44.64457 | 2025-08-05 04:17:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a16eda8b-7036-35e4-9541-e8439c7eb0ff | -8.96076 | -46.74045 | 2025-08-05 04:17:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dc523f68-8881-350b-908d-6e59b68f023a | -11.74731 | -44.9931 | 2025-08-05 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 25824f51-aeeb-3096-acbb-ccaf87b910bd | -6.89948 | -52.86345 | 2025-08-05 04:17:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 07d9b9c0-75e3-3565-90ad-9ae62df1a5c5 | -6.55064 | -43.915 | 2025-08-05 04:17:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c0260320-b5b8-35cc-a73e-b6643f604da6 | -17.20371 | -44.82433 | 2025-08-05 04:17:00 | NPP-375D | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 246e994e-fec9-3dbc-8000-32053b9ef31a | -7.85605 | -46.73528 | 2025-08-05 04:17:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c7276af7-5acd-3661-a130-a2d2a35c5355 | -10.78034 | -45.50773 | 2025-08-05 04:17:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 14.6 |
| c012c6fc-de4b-3955-9b6e-db7986b89c54 | -8.01908 | -43.17303 | 2025-08-05 04:17:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| c7888fef-277e-31b3-9106-5b9875f9ec0f | -7.90574 | -45.53545 | 2025-08-05 04:17:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a70bc605-8651-3c43-a266-d1768780e96b | -8.2661 | -45.06385 | 2025-08-05 04:17:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d5328088-57d4-347d-9234-29c98f98fe9c | -5.81165 | -46.98262 | 2025-08-05 04:17:00 | NPP-375D | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0177c8ce-be39-3a49-a4e8-6df8db03be09 | -7.74199 | -45.23436 | 2025-08-05 04:17:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ba961269-49fd-3afe-8303-fdeba0445fbf | -7.3094 | -44.6721 | 2025-08-05 04:17:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cf9ca60a-7bb4-3e7f-8558-586b61f4b7f3 | -10.3464 | -44.907 | 2025-08-05 04:17:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0000606a-bfd2-3b0c-a422-db6f4ff4c0db | -11.91877 | -44.9551 | 2025-08-05 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 06cec685-c120-3823-8fb9-f0e864ea7265 | -5.77495 | -51.6634 | 2025-08-05 04:17:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 793279b4-53f5-383e-a93d-fb70a96176dd | -8.84591 | -47.61227 | 2025-08-05 04:17:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| f37f73b8-b80b-3c54-b2c2-f57eb0306456 | -11.76188 | -44.9662 | 2025-08-05 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 262da06b-3f04-3ac0-a7e5-a7ce3d6285ec | -11.92662 | -44.92745 | 2025-08-05 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3d982678-a39b-34ee-937e-584265cfb5da | -7.75914 | -45.23717 | 2025-08-05 04:17:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| f056dfb6-506b-3c69-9523-3f14acdbe3f2 | -10.46237 | -44.38794 | 2025-08-05 04:17:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0282160b-ef55-3494-92e2-b6bb1396e8c1 | -7.0578 | -47.462 | 2025-08-05 04:17:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| ec79c0f8-cb5b-36d8-b570-f80d31a26796 | -10.79617 | -46.51397 | 2025-08-05 04:17:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f6930dfb-151b-3014-afcc-ea513fac2003 | -7.99362 | -43.16187 | 2025-08-05 04:17:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 8562194d-ac52-39f0-bbfe-c184c2e9ff61 | -7.57003 | -44.89592 | 2025-08-05 04:17:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 894e4c61-3500-3e2d-b2b0-331b68e67aae | -10.92542 | -48.37272 | 2025-08-05 04:17:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8e342704-13bd-33f1-a5c2-d1bdf3b784c4 | -17.21985 | -44.82281 | 2025-08-05 04:17:00 | NPP-375D | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e7967dbd-2cdf-3b24-b172-65ef78d92115 | -5.67807 | -50.26558 | 2025-08-05 04:17:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 34a6a1c8-4b72-391c-9d42-02a0bc4e44a0 | -5.78792 | -43.60683 | 2025-08-05 04:17:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 5452909b-3911-36de-8499-5d8d9743b877 | -7.54275 | -44.89211 | 2025-08-05 04:17:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 20e4f816-ef75-3038-a33a-118f971cffdb | -7.57062 | -44.89226 | 2025-08-05 04:17:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c615b391-6696-327e-bf92-93aa29e66ab7 | -10.45009 | -44.36454 | 2025-08-05 04:17:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8f9a6239-2776-35bf-9a24-985ec77efb50 | -7.53857 | -45.04568 | 2025-08-05 04:17:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d740da0c-6ab9-33ba-99aa-6a530b1ad968 | -5.88388 | -43.74764 | 2025-08-05 04:17:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 168399f7-0277-3625-a86a-9caaba1ce11e | -11.74894 | -45.00434 | 2025-08-05 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e7559e85-4c5d-32c7-9c92-9b40627dbbe1 | -9.61972 | -43.85727 | 2025-08-05 04:17:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 06d9f378-b9e5-3ba4-aea8-5a77687d1d62 | -5.65538 | -42.58294 | 2025-08-05 04:17:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 926e67de-a445-303a-964a-547fa09e2bcb | -7.75106 | -45.24352 | 2025-08-05 04:17:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 34ef9d08-6643-3aad-9fb0-c8e1e81d99fa | -11.75333 | -45.01972 | 2025-08-05 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README15.md)
