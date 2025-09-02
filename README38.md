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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c8d699c1-16b8-376e-b9e0-9c812b0b4cd4 | -6.84005 | -52.81257 | 2025-09-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6a1569d5-0365-3436-bb3d-b2359ff3c1d7 | -10.87908 | -55.75543 | 2025-09-02 04:14:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ba88d1df-cc69-3745-a50b-65bc3c9de184 | -6.80092 | -52.80728 | 2025-09-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e3d62f08-84af-3403-8015-7f3d6fb9a49a | -12.59351 | -48.24677 | 2025-09-02 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 746eabf6-9420-3fb4-992f-9be4d165accf | -11.89632 | -44.88784 | 2025-09-02 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 39ba0497-cc5f-3e7d-92f4-d3776f9cd117 | -7.99455 | -49.2927 | 2025-09-02 04:14:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 25c9cef3-3c09-3425-8f09-251d7bf1d9c8 | -12.97686 | -48.10727 | 2025-09-02 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c4c13e30-9724-3fc6-8328-d4edfb1b0718 | -11.65826 | -52.20541 | 2025-09-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 31.2 |
| 24ba8b90-bb5d-362a-b5a1-88e87e4bea2c | -11.89653 | -46.67238 | 2025-09-02 04:14:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 186969c3-b209-3e19-a213-b8802ba03e2b | -8.87331 | -45.77497 | 2025-09-02 04:14:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 186edc2c-25b1-3482-8448-3d793dd2e9c6 | -9.97272 | -46.41251 | 2025-09-02 04:14:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b375e365-1cdc-30d7-8bda-136534128de7 | -12.95707 | -48.09167 | 2025-09-02 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 33e4a13b-43d6-32bb-b59a-a03574f656a2 | -9.61546 | -47.83363 | 2025-09-02 04:14:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 5c764fb5-270a-3170-b688-508d3c473604 | -9.11257 | -46.04723 | 2025-09-02 04:14:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c115118e-e5d6-3814-832f-26d42dc1d081 | -9.12929 | -46.05389 | 2025-09-02 04:14:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| aca6f759-afd1-3d9f-af06-0e1616d779ea | -11.94081 | -50.61511 | 2025-09-02 04:14:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9312692e-da0d-3e40-a1f6-ced1ea10ffd7 | -10.96616 | -50.78183 | 2025-09-02 04:14:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5a668871-e430-3419-aeb3-6af1ddc9b99e | -11.35495 | -43.66843 | 2025-09-02 04:14:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 13f41a67-9950-38ba-b323-93eb0c07f6a6 | -11.3731 | -43.55172 | 2025-09-02 04:14:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2495488e-c449-3216-924f-863128841b42 | -12.80965 | -48.05421 | 2025-09-02 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0ae34c3a-30b5-3ecc-9d2a-1424d750ca7c | -6.88685 | -43.83412 | 2025-09-02 04:14:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 019e7db8-2d57-3fc4-a8bd-e236bd1edc6a | -6.72957 | -43.38974 | 2025-09-02 04:14:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.7 |
| b83356c5-bf86-3df3-a448-265665b86627 | -12.85799 | -48.05597 | 2025-09-02 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8ab70525-2680-3ad8-9d33-7da7c97d1d6b | -6.98354 | -44.31367 | 2025-09-02 04:14:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7b65bc77-89e1-3027-9763-291294a2dffb | -11.10152 | -44.63124 | 2025-09-02 04:14:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 12.1 |
| e5c19f5d-78a3-3688-adb4-96cbafd7e8c4 | -6.84358 | -52.82427 | 2025-09-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e32079f5-7546-39ac-a181-ab3144d0f42d | -11.09765 | -44.63423 | 2025-09-02 04:14:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 31.0 |
| 00d5dad2-27dd-39b4-a9c6-c5c557ff7589 | -6.96001 | -44.35348 | 2025-09-02 04:14:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 54eb6467-4c70-3fa4-afad-8230178a2032 | -13.37574 | -46.93755 | 2025-09-02 04:14:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 78073a78-a67b-3c80-b6ad-de24af9a0835 | -11.66324 | -52.17821 | 2025-09-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 70574d53-1373-3384-9cd0-8636785435ae | -11.54592 | -44.84842 | 2025-09-02 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c9d84084-a53c-3506-a61a-7ce42bb16e05 | -7.06923 | -44.58671 | 2025-09-02 04:14:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9f824d7b-89d5-3db8-89aa-b1be9eb26f7e | -7.16457 | -43.90388 | 2025-09-02 04:14:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a30cc238-6ae1-3e79-bc1c-31af31f0eaef | -10.05265 | -48.14006 | 2025-09-02 04:14:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0882bc73-7ab0-32c5-b082-de3283a43083 | -12.61635 | -48.19336 | 2025-09-02 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 50.0 |
| 88841ed1-a740-36d2-8703-ca912475c451 | -12.55788 | -44.7859 | 2025-09-02 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ba1abcf9-751c-3cbf-970a-0a1da9fb8141 | -7.55233 | -45.7016 | 2025-09-02 04:14:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1f2b7fe8-8bbb-3a3a-926e-4dca26b7f036 | -12.85858 | -48.05351 | 2025-09-02 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 4d80e8da-4dc4-3407-899a-d035b7290c6c | -12.81256 | -48.0592 | 2025-09-02 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7038a20b-bbc6-3565-a709-cd9b8efcb5f5 | -10.44808 | -50.2844 | 2025-09-02 04:14:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bfc836de-c83e-327e-a93b-db4c0ad0932f | -10.05462 | -48.08292 | 2025-09-02 04:14:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7b2fc6ea-6204-3502-b0d3-5696f1270705 | -8.71082 | -50.44867 | 2025-09-02 04:14:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3d7df751-c529-386c-8ecb-e57db04e4c75 | -11.89307 | -46.67179 | 2025-09-02 04:14:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 101edb41-9db3-3fef-9dd1-74c82f56906b | -7.11556 | -44.75943 | 2025-09-02 04:14:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 289722ce-346f-3da2-94b5-05383ca6d311 | -7.55741 | -45.71424 | 2025-09-02 04:14:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 15feda33-7f49-3783-a7df-ac1703b3eddd | -7.3247 | -44.2848 | 2025-09-02 04:14:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a822c5a6-7d95-3a0d-97ea-ce39644b9bbe | -7.98696 | -46.45929 | 2025-09-02 04:14:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 8b345e9e-bd6f-32a3-b27f-9f6391d9ce49 | -11.91632 | -46.45153 | 2025-09-02 04:14:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3cbd2d49-80e2-3360-bb33-1923a6d3de40 | -9.75451 | -46.92654 | 2025-09-02 04:14:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a4a14da3-828d-3f7a-9ea6-865c4e3ff72b | -9.83427 | -48.61462 | 2025-09-02 04:14:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d5590d42-91d3-3961-bb1d-8f08993467f7 | -7.00796 | -44.3539 | 2025-09-02 04:14:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 95505904-7af9-3271-8a68-6d3eb5980e31 | -9.65328 | -47.79527 | 2025-09-02 04:14:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7bf173a8-01c7-32b0-859f-dfe5677d9796 | -11.88905 | -46.68359 | 2025-09-02 04:14:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5426abb3-33b2-3ad8-a403-9f071c48d85e | -11.7995 | -43.82233 | 2025-09-02 04:14:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0d39a4a2-d26d-3ff0-839c-6d1a195f6387 | -10.28739 | -47.46555 | 2025-09-02 04:14:00 | NOAA-20 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e8e016bd-c3b0-3bec-9c35-55bbbf37da81 | -11.09325 | -44.61909 | 2025-09-02 04:14:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| a1336664-f45c-35ec-9a25-2d3d82cf6d86 | -11.42199 | -46.9055 | 2025-09-02 04:14:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b517d793-dad9-3099-bda7-672987a17b39 | -6.99267 | -43.229 | 2025-09-02 04:14:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 494c3b44-025c-3685-b0f6-281190095be6 | -11.43115 | -46.91541 | 2025-09-02 04:14:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 05ae4c88-5bcb-30db-9438-72ba422865b0 | -12.76355 | -48.08177 | 2025-09-02 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 189bd9bd-6e16-3598-a3eb-fba74551eeb1 | -7.94041 | -46.43023 | 2025-09-02 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ba935327-8bf2-3438-8f62-2d00afe651a0 | -11.02572 | -46.84525 | 2025-09-02 04:14:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 00ff9efc-7058-3bb9-bdb0-0a49bbf812d0 | -12.32729 | -45.71694 | 2025-09-02 04:14:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f2698ee3-75f8-384b-a2bd-19125229f3b8 | -13.6582 | -48.16096 | 2025-09-02 04:14:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 11049ab7-302a-339c-8711-d060f87bf897 | -9.28547 | -47.1114 | 2025-09-02 04:14:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9c4adf5a-7cb8-37c2-ba51-7494fcee8184 | -6.83747 | -52.82686 | 2025-09-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1729285d-513f-3e2d-8aa1-c0284787023f | -9.84069 | -48.31678 | 2025-09-02 04:14:00 | NOAA-20 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b0c51ae7-f0db-3990-bcd6-ed038c8592b5 | -11.66626 | -52.2084 | 2025-09-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 34.4 |
| f35a4811-03af-3f01-984f-8572d71b2c18 | -9.44184 | -48.86887 | 2025-09-02 04:14:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d1ba61a4-142d-3280-a57c-d7e7009b25e3 | -6.76321 | -45.71998 | 2025-09-02 04:14:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dc896676-6aa9-3058-aeca-259e4e7bdcf1 | -10.96976 | -50.77987 | 2025-09-02 04:14:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e8619d1c-03e5-34ac-a83e-785028f183fe | -9.22519 | -47.09226 | 2025-09-02 04:14:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 23ba284e-6a28-3a17-9389-f79bcd5a1a4b | -7.3758 | -45.40533 | 2025-09-02 04:14:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3e78d73c-e796-35e6-be5b-006acd40d9e1 | -8.71243 | -50.43941 | 2025-09-02 04:14:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 92486321-8336-3fcd-a74b-261c57574dfc | -7.66867 | -43.87363 | 2025-09-02 04:14:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b2427e39-2c3f-31e4-bee8-e4ca4adb619d | -8.18577 | -46.78326 | 2025-09-02 04:14:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 25.3 |
| 67e26e06-0b88-3cdb-abb0-7bc5e6b76a6c | -7.47558 | -45.22184 | 2025-09-02 04:14:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 51dc4e6f-bd5e-3d47-a1e7-6c7717189b75 | -8.83178 | -45.7915 | 2025-09-02 04:14:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e08e6fe2-605f-3bd2-b09a-31bf1407785f | -8.81248 | -47.83043 | 2025-09-02 04:14:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d843e1dd-a9c9-32db-8b81-151d5ba17972 | -9.83693 | -44.67849 | 2025-09-02 04:14:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dafd6c7c-ed63-36be-ab1a-53a6cf23c3d1 | -12.64254 | -48.2396 | 2025-09-02 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2d387efb-953c-30b7-a08f-d80fbada89d2 | -11.08659 | -44.63964 | 2025-09-02 04:14:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 95db36df-788e-3683-b251-bddfaccaa7f3 | -7.06622 | -44.32711 | 2025-09-02 04:14:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1daf7d20-dfa6-36ac-a8da-16c76af33395 | -12.9761 | -48.11166 | 2025-09-02 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 185cd4b4-26bb-3e6e-b493-1f71d376c7eb | -7.58193 | -45.21564 | 2025-09-02 04:14:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 00f125f4-60d2-35ca-a006-9430ffed8b3e | -6.84811 | -52.79904 | 2025-09-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7f46fb4c-ac02-3001-ac9e-2e27e3b7e7cc | -11.86345 | -52.41873 | 2025-09-02 04:14:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 00b81b66-b5d0-3a17-b445-b7526fbf3ca4 | -6.81207 | -45.68395 | 2025-09-02 04:14:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4d146a94-d127-3bed-a1b8-cfb960705997 | -12.86757 | -48.04399 | 2025-09-02 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 3795a8ab-de1e-3089-b3db-7b79be8e3b51 | -6.82176 | -52.82019 | 2025-09-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 86df7489-28d8-38af-bc09-7ee24f762727 | -11.66309 | -52.20628 | 2025-09-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 31.2 |
| 7adb03fb-95da-362f-9dcc-28e693a478fd | -13.69905 | -46.93536 | 2025-09-02 04:14:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 6ddbc350-dda4-38f1-8cd9-5b7978d8af29 | -11.67089 | -52.1909 | 2025-09-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 46e074c0-27f9-36fe-93db-caf8c85ef70a | -13.70508 | -46.8996 | 2025-09-02 04:14:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3ae081de-c553-3fda-91f8-127ec0367caa | -11.92787 | -50.61266 | 2025-09-02 04:14:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a05e478b-f56a-3845-8d8e-ec6cb8b8457b | -11.65292 | -44.8586 | 2025-09-02 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c1be6c9b-859c-3d46-90d7-c90164706860 | -6.87236 | -45.85053 | 2025-09-02 04:14:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| e3faeb0a-77c5-3b6a-b882-ccf5e0c478de | -13.49036 | -46.92393 | 2025-09-02 04:14:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8999c063-0370-3e49-a1fc-4c48cb139129 | -13.69093 | -46.88301 | 2025-09-02 04:14:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1a7828ca-fe5b-3591-ab88-060e67b85b0e | -11.43277 | -46.81415 | 2025-09-02 04:14:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |


[Clique aqui para ver as próximas entradas](README39.md)
