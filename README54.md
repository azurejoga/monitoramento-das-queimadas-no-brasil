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

## Dados Diários - Página 54

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5d4bccca-b9e5-3cfe-9046-12bb36364a3e | -13.8894 | -44.15907 | 2026-10-10 04:10:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 13d1ca2c-fca5-3ccb-b9b5-bf4b1fb9569e | -10.92761 | -45.52783 | 2026-10-10 04:10:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6b94b1d7-7e59-3601-ad11-385b6e7ace25 | -11.98113 | -43.5056 | 2026-10-10 04:10:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9fbac573-777f-3431-a1ac-7923dfe96337 | -11.73646 | -44.9522 | 2026-10-10 04:10:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6c56f3b9-508d-30ec-adfb-32a3d23872da | -12.22473 | -44.69148 | 2026-10-10 04:10:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| d8ebfac6-f24d-3fe1-9c84-c0623fc3ee90 | -13.26115 | -43.99996 | 2026-10-10 04:10:00 | NOAA-21 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b0588cba-6f56-3055-8445-438229bbe744 | -11.76414 | -43.52461 | 2026-10-10 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 145dc0b9-fba3-3e4e-825a-7698bf5e36f4 | -11.3721 | -54.02563 | 2026-10-10 04:10:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 18ce0874-3ce9-3f98-ac0a-e07e31a2fe9a | -15.02433 | -46.25774 | 2026-10-10 04:10:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 47903b69-e8d7-3dbb-a2c7-9c9d21311222 | -12.37013 | -46.56249 | 2026-10-10 04:10:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7f00688b-0687-359a-a478-aacfb7d2099a | -11.59778 | -43.69237 | 2026-10-10 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 791d695d-3e5c-3a30-99b6-c6d563122f34 | -11.75141 | -46.7785 | 2026-10-10 04:10:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0d4d4c4b-2db3-34e6-9d96-d2919111e7bc | -16.6029 | -46.75592 | 2026-10-10 04:10:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4441ef09-af4f-374b-8285-220e57759ad4 | -11.83131 | -43.59333 | 2026-10-10 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5901869e-8a34-3c78-a9e0-4259835fa1ae | -11.58341 | -43.6972 | 2026-10-10 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6cb7ecd9-3baa-3f96-82cc-46a1e7e37f72 | -14.46398 | -43.94815 | 2026-10-10 04:10:00 | NOAA-21 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 63c8c1c7-a4da-3cf1-9f1f-a6ba7646264c | -11.60498 | -43.68985 | 2026-10-10 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c2771612-3810-3ba3-aef0-ff8109ccb53e | -13.0364 | -47.16972 | 2026-10-10 04:10:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f8cc1ef4-76e3-3166-b1ce-a089e84f2631 | -12.7743 | -44.88519 | 2026-10-10 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6e5e887d-cc72-3b59-915c-5ca8912d2fe6 | -11.02723 | -45.43308 | 2026-10-10 04:10:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cd8d2faf-f2ec-3610-8522-92f577127523 | -11.01869 | -44.05946 | 2026-10-10 04:10:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 605a612c-6799-34bb-9ac7-386df2de2bcc | -14.44254 | -43.93368 | 2026-10-10 04:10:00 | NOAA-21 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5fcd4f1b-db25-3246-a3a4-7f95b2b48402 | -13.37259 | -43.89815 | 2026-10-10 04:10:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2c7d0dc7-7a61-35ad-a406-fde71c8ac9fb | -11.95416 | -43.48319 | 2026-10-10 04:10:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 47834349-edc6-3948-9840-d31d4f2ec1b2 | -15.05788 | -41.80209 | 2026-10-10 04:10:00 | NOAA-21 | PIRIPÁ | BAHIA | Brasil | 2924702 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 0790f66e-af2f-3543-ad25-26b9cb69a7e2 | -15.45612 | -48.06076 | 2026-10-10 04:10:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8f18bff1-0a55-350f-b4e4-46ed37fffc14 | -11.95141 | -43.47912 | 2026-10-10 04:10:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 03876e65-7abd-381d-a808-90867a45d5ab | -12.0378 | -43.45039 | 2026-10-10 04:10:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6aad8653-78e5-3358-815f-2f848d958d55 | -15.37959 | -41.90118 | 2026-10-10 04:10:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 4d9cb421-a7d7-35dc-8166-e12e16e87065 | -15.42268 | -43.31974 | 2026-10-10 04:10:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 5f1b74d4-3fcc-361e-a180-cbd2b57a344e | -11.02271 | -44.03423 | 2026-10-10 04:10:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b6fdf394-8e53-340f-8444-21c16efd9348 | -11.36527 | -54.02888 | 2026-10-10 04:10:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d685186f-bf83-3bf9-8892-13d9e282da00 | -13.72627 | -49.12398 | 2026-10-10 04:10:00 | NOAA-21 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cc232fe6-40c1-351e-9e79-a1d243713ef4 | -12.07783 | -47.37873 | 2026-10-10 04:10:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e0d238e8-387d-3291-841d-afa6e701ac3e | -10.73757 | -52.0316 | 2026-10-10 04:10:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8a6a088e-0b8d-3f64-980f-d89b2e068a50 | -11.84013 | -46.8073 | 2026-10-10 04:10:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 325b1b2d-43b5-344c-ac3b-07328604e913 | -15.77365 | -43.27058 | 2026-10-10 04:10:00 | NOAA-21 | NOVA PORTEIRINHA | MINAS GERAIS | Brasil | 3145059 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1da55fd3-c06e-3a03-a0f1-7d09f05e36ec | -11.84461 | -46.80342 | 2026-10-10 04:10:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 30f0d2a4-b2e5-379c-925d-82bf91039e62 | -11.01838 | -45.41497 | 2026-10-10 04:10:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9634e6f2-5f45-396f-953c-71ad26bd15b6 | -15.65807 | -48.13131 | 2026-10-10 04:10:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d6c1816e-f45b-3c7d-bdff-70c2e7006dfd | -17.98725 | -47.21135 | 2026-10-10 04:12:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cef8e323-f522-34e7-bc0b-48d84fe20808 | -17.99005 | -47.21613 | 2026-10-10 04:12:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 080705ea-c6be-3232-aa3f-3a4b47776567 | -18.91669 | -47.91668 | 2026-10-10 04:12:00 | NOAA-21 | INDIANÓPOLIS | MINAS GERAIS | Brasil | 3130705 | 31 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 76cc056e-d57b-3bc0-9b8a-ff75bdea437b | -18.85154 | -41.96727 | 2026-10-10 04:12:00 | NOAA-21 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 1030902c-4687-30d0-90db-fa7b8c80e53a | -19.64894 | -45.92991 | 2026-10-10 04:12:00 | NOAA-21 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| be1ba8fc-e327-3401-b0ee-247a5ffae9b3 | -18.91388 | -47.9116 | 2026-10-10 04:12:00 | NOAA-21 | INDIANÓPOLIS | MINAS GERAIS | Brasil | 3130705 | 31 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 22e64156-4576-3c5b-a8c3-bd7ce6da3f85 | -18.32365 | -42.36485 | 2026-10-10 04:12:00 | NOAA-21 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 749b0dd0-3cab-35b3-8b65-17c45dd6acd1 | -19.55451 | -43.59017 | 2026-10-10 04:12:00 | NOAA-21 | TAQUARAÇU DE MINAS | MINAS GERAIS | Brasil | 3168309 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 0d16e0fb-c6ae-3384-8896-2c56ce815225 | -16.82731 | -52.0724 | 2026-10-10 04:12:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a2bdb195-d587-3fd5-b3f1-7d5318b6dcb6 | -18.91311 | -47.91596 | 2026-10-10 04:12:00 | NOAA-21 | INDIANÓPOLIS | MINAS GERAIS | Brasil | 3130705 | 31 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 4e7ea364-b422-3157-9b0f-59a2718ef4a9 | -19.08377 | -48.14451 | 2026-10-10 04:12:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| ba5a69ff-d6f4-3616-a39c-32b66f84af5d | -18.35574 | -42.26522 | 2026-10-10 04:12:00 | NOAA-21 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 6a6d1907-203c-3de5-a9bb-e01172c1c618 | -18.85096 | -41.97141 | 2026-10-10 04:12:00 | NOAA-21 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| c9856c69-72a1-394d-9301-2e74ab00888e | -19.55117 | -43.58963 | 2026-10-10 04:12:00 | NOAA-21 | TAQUARAÇU DE MINAS | MINAS GERAIS | Brasil | 3168309 | 31 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 09fe8eb6-9c95-330c-b412-2eedf431f8a8 | -19.08016 | -48.1438 | 2026-10-10 04:12:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 678e6a61-f8ca-3b0c-9da4-2f858624f5d9 | -18.96437 | -43.08282 | 2026-10-10 04:12:00 | NOAA-21 | SENHORA DO PORTO | MINAS GERAIS | Brasil | 3166105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| e8fcb0f5-2260-360c-90a7-dcda5c3f3ea1 | -18.91745 | -47.91232 | 2026-10-10 04:12:00 | NOAA-21 | INDIANÓPOLIS | MINAS GERAIS | Brasil | 3130705 | 31 | 33 | nan | nan | nan | Cerrado | 7.8 |
| ca913737-93d1-337c-82de-2ea5e6912ade | -18.9339 | -47.52487 | 2026-10-10 04:12:00 | NOAA-21 | ROMARIA | MINAS GERAIS | Brasil | 3156403 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0535291d-8c63-3628-8cf7-d3c0d470070d | -20.30117 | -43.9531 | 2026-10-10 04:12:00 | NOAA-21 | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 0968f144-5dd2-32fe-82f5-24d3015414da | -19.64561 | -45.92931 | 2026-10-10 04:12:00 | NOAA-21 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a9be90c2-915a-3335-9b20-baeb396626c5 | -19.08299 | -48.14892 | 2026-10-10 04:12:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5fa38009-173f-39a1-ae35-c88884e7b537 | -18.61935 | -48.25657 | 2026-10-10 04:12:00 | NOAA-21 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 35927849-3809-3e68-8c22-9780a48c6b28 | -17.04705 | -50.87823 | 2026-10-10 04:12:00 | NOAA-21 | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| aac15ac9-0d70-3faf-9829-5eba0e999746 | -20.07169 | -41.36531 | 2026-10-10 04:12:00 | NOAA-21 | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| ee0403cc-86d5-3d9e-8b86-b2cdc7fd0d8c | -19.88345 | -43.68535 | 2026-10-10 04:12:00 | NOAA-21 | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 6995a4be-1c54-3325-b655-0a5b7a74f184 | -18.32022 | -42.38843 | 2026-10-10 04:12:00 | NOAA-21 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| f2a03181-dd85-392d-81c7-211cf99dcd78 | -20.30172 | -43.94947 | 2026-10-10 04:12:00 | NOAA-21 | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| e6e7bb1a-0af0-3d79-9d04-67e08bae0509 | -19.15089 | -46.61259 | 2026-10-10 04:12:00 | NOAA-21 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0bef342a-0e1d-3297-b879-51e501b2ac4a | -18.3345 | -42.38673 | 2026-10-10 04:12:00 | NOAA-21 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 6796429a-b09a-38bc-b8d9-aa79d14a6740 | -19.48384 | -43.90082 | 2026-10-10 04:12:00 | NOAA-21 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 7fccbfa3-dc49-3472-8195-4b290547cb01 | -18.33395 | -42.39054 | 2026-10-10 04:12:00 | NOAA-21 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| d2c2cfe2-9934-3236-820a-0dfc28486dd1 | -18.63994 | -41.33233 | 2026-10-10 04:12:00 | NOAA-21 | MENDES PIMENTEL | MINAS GERAIS | Brasil | 3141504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 04e7daf7-8765-3b00-80b9-d0d1d1322615 | -18.31967 | -42.39222 | 2026-10-10 04:12:00 | NOAA-21 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| b58277ab-1614-365b-bb9b-90cfa3beb81a | -17.99075 | -47.21203 | 2026-10-10 04:12:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b4b0d427-cb37-31b9-a475-296f6b1d5202 | -20.7334 | -41.87965 | 2026-10-10 04:12:00 | NOAA-21 | CAIANA | MINAS GERAIS | Brasil | 3110103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 4fc0f18a-cae7-3447-8bc8-c6f7f474a6bd | -19.89234 | -44.0751 | 2026-10-10 04:12:00 | NOAA-21 | CONTAGEM | MINAS GERAIS | Brasil | 3118601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| ac1ed487-4070-3c84-89c9-465717328130 | -17.99356 | -47.21682 | 2026-10-10 04:12:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ada88ab7-5d9d-3280-8263-8dc3c7a8b061 | -18.32763 | -42.38572 | 2026-10-10 04:12:00 | NOAA-21 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 9ebb8e10-ccbb-3919-afb4-8e9d6c103704 | -19.12388 | -46.15939 | 2026-10-10 04:12:00 | NOAA-21 | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9430ab4a-a479-3e6f-be40-bd77ce243318 | -18.64353 | -41.33287 | 2026-10-10 04:12:00 | NOAA-21 | MENDES PIMENTEL | MINAS GERAIS | Brasil | 3141504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 3968ba4b-7481-3a31-abb3-51c0b536079d | -18.54485 | -43.99681 | 2026-10-10 04:12:00 | NOAA-21 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f681cf0e-43bc-3c92-8628-3f77ae302634 | -18.32421 | -42.38514 | 2026-10-10 04:12:00 | NOAA-21 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 9ba92506-daad-39f8-98a0-7489a33fb4bd | -18.32708 | -42.38951 | 2026-10-10 04:12:00 | NOAA-21 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 174e776b-f711-3c26-b1ac-acd585e1f1bc | -18.31624 | -42.39165 | 2026-10-10 04:12:00 | NOAA-21 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 7201e362-1dfe-3450-988e-f743fd407a36 | -18.06398 | -44.59807 | 2026-10-10 04:12:00 | NOAA-21 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7858ed7c-0106-3619-819b-23bb2bc1ab16 | -19.21104 | -46.52412 | 2026-10-10 04:12:00 | NOAA-21 | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f2b3f1b6-e2ce-3369-846e-f6b47c10ce5f | -18.63933 | -41.33674 | 2026-10-10 04:12:00 | NOAA-21 | MENDES PIMENTEL | MINAS GERAIS | Brasil | 3141504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| fbb60a5d-12d2-381a-a7e4-b484027a911f | -17.64767 | -51.04388 | 2026-10-10 04:12:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dfbe3e48-bea5-3e90-9187-d4d0ce61c482 | -18.32365 | -42.38898 | 2026-10-10 04:12:00 | NOAA-21 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 05a71071-4a55-349c-be9e-36f310542f7c | -19.48328 | -43.90452 | 2026-10-10 04:12:00 | NOAA-21 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c7fc507b-aacd-344e-8237-24e06cdafc4a | -18.76876 | -47.51241 | 2026-10-10 04:12:00 | NOAA-21 | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5339bea5-6028-3bfb-a5a8-81b17331381d | -18.93742 | -47.52558 | 2026-10-10 04:12:00 | NOAA-21 | ROMARIA | MINAS GERAIS | Brasil | 3156403 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| df70eb01-682a-3eff-a48e-f2d32e4c92c8 | -17.98655 | -47.21545 | 2026-10-10 04:12:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a998ccda-99b7-30c9-85bb-0e7bfb884750 | -18.91821 | -47.908 | 2026-10-10 04:12:00 | NOAA-21 | INDIANÓPOLIS | MINAS GERAIS | Brasil | 3130705 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| eaff9f41-5cc8-3e77-8e92-e9bad93cc09b | -22.0819 | -48.99535 | 2026-10-10 04:12:00 | NOAA-21 | AREALVA | SÃO PAULO | Brasil | 3503406 | 35 | 33 | nan | nan | nan | Cerrado | 37.6 |
| afa2db87-52d4-3097-8aae-bb963488c9c5 | -22.08606 | -48.99507 | 2026-10-10 04:12:00 | NOAA-21 | AREALVA | SÃO PAULO | Brasil | 3503406 | 35 | 33 | nan | nan | nan | Cerrado | 13.2 |
| dd9fc246-b6b7-34e7-a380-b0b3b56851d0 | -20.48088 | -45.23962 | 2026-10-10 04:12:00 | NOAA-21 | ITAPECERICA | MINAS GERAIS | Brasil | 3133501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 22593ebd-1f6e-3e26-8dce-1e1a262ff2c9 | -22.08361 | -49.00861 | 2026-10-10 04:12:00 | NOAA-21 | AREALVA | SÃO PAULO | Brasil | 3503406 | 35 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 7bd22ca5-615c-3314-b64e-b387742d0114 | -22.07872 | -49.01348 | 2026-10-10 04:12:00 | NOAA-21 | AREALVA | SÃO PAULO | Brasil | 3503406 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fe7db520-64c1-33a2-bc2d-b54ae564ed73 | -22.08688 | -48.99055 | 2026-10-10 04:12:00 | NOAA-21 | AREALVA | SÃO PAULO | Brasil | 3503406 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README55.md)
