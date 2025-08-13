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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c63553c6-59ee-3dd5-b6de-f89843629b80 | -12.31123 | -46.05273 | 2025-08-13 05:08:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 20659e20-0395-3fae-a928-3f6a3c0bc0a5 | -12.67171 | -46.96794 | 2025-08-13 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 20243bff-25b4-39aa-937f-2894d3332ba8 | -10.10172 | -68.96477 | 2025-08-13 05:08:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 786b764e-1bf1-390b-ab63-4d387d517272 | -12.48523 | -46.96375 | 2025-08-13 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8ba2961e-55fe-39ad-9acc-95c23481b039 | -12.31016 | -46.06176 | 2025-08-13 05:08:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4b07f1c7-5f3f-3157-9722-a7b6ec463d62 | -9.17114 | -59.67635 | 2025-08-13 05:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a50a4d2f-cf77-3e80-ab76-0a44de1bef90 | -12.58418 | -46.97696 | 2025-08-13 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 54451a32-becc-3ac7-807c-92f8cdb5ef80 | -12.31561 | -46.06711 | 2025-08-13 05:08:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| be5d1c1d-bcf9-33fb-b0ad-dd10bd9d618c | -9.19666 | -59.65854 | 2025-08-13 05:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| cd9101ac-edbc-32f6-84e4-f6a00cf6e62e | -18.53828 | -46.05497 | 2025-08-13 05:08:00 | NPP-375D | VARJÃO DE MINAS | MINAS GERAIS | Brasil | 3170750 | 31 | 33 | nan | nan | nan | Cerrado | 7.5 |
| f3f672bd-94e7-3baf-a761-b05db7e6e06d | -16.59719 | -47.03431 | 2025-08-13 05:08:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 85cfcc89-f9a3-3bde-9c1c-b8da22478337 | -16.38977 | -50.88606 | 2025-08-13 05:08:00 | NPP-375D | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0d61f8a6-772f-396b-830f-090ee046ac47 | -9.05945 | -60.6552 | 2025-08-13 05:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f1ae0677-7f41-3e63-95ac-42f6d48eda4f | -12.57572 | -46.9772 | 2025-08-13 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0d43b0b0-f6ed-3f5a-890d-8b1c5473eab2 | -9.16749 | -59.67572 | 2025-08-13 05:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5301aace-6101-3c27-9c88-27932106bdc1 | -9.20101 | -59.65489 | 2025-08-13 05:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b31d961f-335e-3e04-8b38-9dd483fb1af2 | -16.40281 | -50.89397 | 2025-08-13 05:08:00 | NPP-375D | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6ea1c672-9ac0-3ac2-a396-73861add9db2 | -16.9654 | -48.42002 | 2025-08-13 05:08:00 | NPP-375D | ORIZONA | GOIÁS | Brasil | 5215306 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6c9cc9e0-4b00-3627-9644-2ac3a47bce5f | -16.39494 | -50.882 | 2025-08-13 05:08:00 | NPP-375D | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 89669d58-62a0-3d9f-8f16-881156abeae6 | -12.14581 | -48.01991 | 2025-08-13 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c621db41-66ad-3f10-bc9e-0d672f6898dc | -16.30049 | -52.91267 | 2025-08-13 05:08:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b5805994-7789-3287-936f-df1e8479baca | -12.50267 | -46.9623 | 2025-08-13 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 65535f19-0961-3d59-acec-7f3b66efbc40 | -12.32971 | -46.05088 | 2025-08-13 05:08:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a6c41b75-5405-382d-8eca-a62066d8915b | -10.96972 | -49.57546 | 2025-08-13 05:08:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| bc9ec66e-fe2f-3d70-ac8b-30331189cd52 | -8.92441 | -60.76119 | 2025-08-13 05:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7cc93278-3704-3edd-9f2b-8afab0a1c1bb | -9.47281 | -57.84092 | 2025-08-13 05:08:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 47d984bb-aa53-3918-9156-cd52ef3103b7 | -11.07384 | -55.37505 | 2025-08-13 05:08:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a46798ee-b836-3dac-bb79-d511007b080c | -17.0472 | -51.7943 | 2025-08-13 05:08:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 16c8f3c8-3a33-3c0d-9ca1-fded5d41bad3 | -9.70309 | -56.09715 | 2025-08-13 05:08:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3f484e3b-6f04-3801-83c9-66d247139811 | -12.32159 | -46.068 | 2025-08-13 05:08:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 771052df-603b-3dec-8f9f-5a8c25eee765 | -18.5442 | -46.06116 | 2025-08-13 05:08:00 | NPP-375D | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 32.5 |
| 195c8dee-8ff9-3dfe-a963-132b1e1b3016 | -10.76008 | -69.08608 | 2025-08-13 05:08:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 796b2043-6dc1-344e-9421-24c90deae317 | -9.37684 | -61.53576 | 2025-08-13 05:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cec35401-3ce3-37b6-a0eb-06cd7bf22ff1 | -8.92355 | -60.76614 | 2025-08-13 05:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9df3ed12-2408-3d87-90da-7bd2c1c3ce8e | -16.30298 | -52.91622 | 2025-08-13 05:08:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| be0808b8-f13f-317b-9bb9-32d819c75f03 | -12.47957 | -46.96297 | 2025-08-13 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d6f55862-2541-36e2-b8de-16b584bd7cb8 | -12.57109 | -47.03963 | 2025-08-13 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 97935782-1e7f-39ee-bbab-eddeffca6639 | -12.5776 | -46.98397 | 2025-08-13 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e98021f3-ca64-3e28-9da4-06d86c92d049 | -15.60899 | -48.24063 | 2025-08-13 05:08:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 587b6387-0be7-3c3d-990d-6efc8f8c0f99 | -9.38561 | -61.53356 | 2025-08-13 05:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 90c048f7-99b1-394c-a9b7-722475e0c0af | -16.3117 | -52.91235 | 2025-08-13 05:08:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 9.4 |
| d56f6d55-751e-37f7-b82b-8e253666d460 | -9.06269 | -60.65366 | 2025-08-13 05:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| e5521039-aa6f-3e57-b1ac-bc7e42c32c6b | -9.06029 | -60.65034 | 2025-08-13 05:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 818adc8c-9d89-365d-9ccc-45e003de15cd | -15.15154 | -53.51388 | 2025-08-13 05:08:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7ba157c1-a481-3484-811f-e7c6aa7dd508 | -11.31668 | -55.22514 | 2025-08-13 05:08:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 29746f76-edee-3d51-8a34-0c5f2a6d04b2 | -10.97233 | -49.56915 | 2025-08-13 05:08:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c283606f-4446-3c37-9569-8d29912b8e05 | -16.4034 | -50.88923 | 2025-08-13 05:08:00 | NPP-375D | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 837265f0-b61d-3ef6-a367-a2109f96820e | -16.30451 | -52.91324 | 2025-08-13 05:08:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a160812d-8f51-3431-8c89-ea27b4e0a369 | -9.05882 | -60.653 | 2025-08-13 05:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| df285048-2e42-3005-9a96-3701c006223c | -10.75819 | -69.08948 | 2025-08-13 05:08:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 034a8cf2-51bc-3974-b30c-38280b02825b | -9.05642 | -60.64965 | 2025-08-13 05:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9275f7a2-e1ed-3425-aeb4-6db690df5faf | -15.09915 | -51.35021 | 2025-08-13 05:08:00 | NPP-375D | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4f05525d-bcac-3f8e-b4b1-929c2f6b7501 | -9.19158 | -59.66651 | 2025-08-13 05:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cecf5a0a-c574-3d08-8af4-29d373e6d4a6 | -9.05558 | -60.65454 | 2025-08-13 05:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 29809f6e-9bf5-3e35-85b3-2d4dfd125639 | -12.47789 | -46.96061 | 2025-08-13 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2595a079-5b81-3f03-9093-bf628013290a | -16.29647 | -52.91211 | 2025-08-13 05:08:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| be8a3979-c754-349a-af6f-f46865904940 | -16.30786 | -52.91896 | 2025-08-13 05:08:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2855dfb1-ff13-3bc1-9ec9-ea7236c8b928 | -9.37873 | -61.52489 | 2025-08-13 05:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f079b37c-01b7-3c76-9ad7-f772384e67f2 | -18.53774 | -46.0607 | 2025-08-13 05:08:00 | NPP-375D | VARJÃO DE MINAS | MINAS GERAIS | Brasil | 3170750 | 31 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 95dbc3ec-d14c-3eb0-9095-cf31b63928f8 | -18.05282 | -47.94487 | 2025-08-13 05:08:00 | NPP-375D | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 80eccb6d-3d23-3fa0-af5f-42cb7483a64f | -12.30275 | -50.00688 | 2025-08-13 05:08:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fca473eb-e12b-3ff2-b526-eaa429bfe5f9 | -9.51294 | -62.37431 | 2025-08-13 05:08:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a10e2f1b-78b2-30ba-a66f-b0c70b7d6c03 | -11.63805 | -50.14415 | 2025-08-13 05:08:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c7ca7063-8a53-322b-83c4-4c932cdf92e9 | -15.70857 | -56.40111 | 2025-08-13 05:08:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fa910c3a-20b0-31f8-80c7-3d46b9ce4a59 | -12.58607 | -46.98657 | 2025-08-13 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d5ec0686-e0dc-3b95-bb9e-e75229e239dc | -12.58025 | -47.05919 | 2025-08-13 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a425424f-b965-39bb-8e1a-5fc45f7bfa77 | -9.3734 | -61.53143 | 2025-08-13 05:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f8286124-9810-3f79-9c6f-645c17d897fc | -16.3077 | -52.91169 | 2025-08-13 05:08:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a7dbe3fd-6122-3a3c-9e06-81357c65a401 | -9.19959 | -59.66351 | 2025-08-13 05:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f6b44c46-248c-3d55-81cf-326cda51ba2a | -16.30699 | -52.91684 | 2025-08-13 05:08:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 686166d4-b121-303a-9d4c-9afd967c7cb5 | -12.36461 | -59.84358 | 2025-08-13 05:08:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4fc38c02-8d0b-390f-bd13-bee755d23d82 | -12.52439 | -46.97328 | 2025-08-13 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b254f8d5-a7dd-39d0-824d-3d3021a664d5 | -9.05861 | -60.66006 | 2025-08-13 05:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8844c8b9-2175-353d-9adc-404195176a48 | -16.315 | -52.91813 | 2025-08-13 05:08:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 7d8c529d-0e29-3155-882d-0d476c63b89c | -12.3107 | -46.05723 | 2025-08-13 05:08:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8c5ecb15-3854-3e2e-b7c6-826cc0ee5456 | -9.19523 | -59.66717 | 2025-08-13 05:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5d931e03-4071-3e92-92c6-e6f617b7ea5a | -9.05495 | -60.65232 | 2025-08-13 05:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0a903092-96c1-3b01-9317-3b50550e9d31 | -12.58282 | -46.98855 | 2025-08-13 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b8282547-9bb7-3327-851b-99a92a459dc3 | -12.49089 | -46.96455 | 2025-08-13 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 697420f6-4729-378c-af87-6a933c525526 | -12.6739 | -46.96274 | 2025-08-13 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3efe1d2a-5e2e-3d04-b509-552a0dbeed53 | -12.32265 | -46.05904 | 2025-08-13 05:08:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a5fe970e-94c8-3321-bfc5-0f8f05d2ff01 | -16.29983 | -52.91772 | 2025-08-13 05:08:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0066cf15-a420-38bd-a484-5f0c0ecd004f | -18.54473 | -46.05555 | 2025-08-13 05:08:00 | NPP-375D | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 17.5 |
| c91e5b56-78dc-38b9-b659-1ea65cb88fc8 | -9.2003 | -59.65921 | 2025-08-13 05:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5efa4fe0-bb64-3d64-b266-6331b42d4bb6 | -16.3112 | -52.92469 | 2025-08-13 05:08:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 26.6 |
| e5435baa-f7ce-386f-9778-54035d5e02db | -15.61067 | -48.24041 | 2025-08-13 05:08:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| fdf047db-1cec-3a66-bc38-0a7bda27b1dc | -9.06416 | -60.65103 | 2025-08-13 05:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e58fb7e3-903e-393e-8f51-0f32249ccbb3 | -12.50221 | -46.96618 | 2025-08-13 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9b9641b9-7ee3-3343-b342-52371db54eba | -10.01919 | -58.43439 | 2025-08-13 05:08:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 284dd922-f3ab-3a77-b5ed-be53170b2ac8 | -16.39884 | -50.88832 | 2025-08-13 05:08:00 | NPP-375D | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| cda58161-2a0d-39d1-af93-47ff7ec79331 | -11.64256 | -50.14478 | 2025-08-13 05:08:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 396ee6e4-ed8c-3641-a6be-418d14620149 | -10.4754 | -61.3271 | 2025-08-13 05:08:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d0aea921-a9f6-34d1-b3e1-9cab563cb0fd | -9.47619 | -57.8415 | 2025-08-13 05:08:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 458e4735-42a9-3678-b2c0-803103f88077 | -15.09421 | -51.35392 | 2025-08-13 05:08:00 | NPP-375D | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c8327f79-2f74-3324-a2fb-20c6912214a2 | -11.74506 | -58.33509 | 2025-08-13 05:08:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 024a0ab5-6f4c-3ac5-aba9-645073a54f90 | -9.38686 | -61.52631 | 2025-08-13 05:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 53d68b87-86cc-3375-82c8-cedadab0f901 | -12.51353 | -46.9678 | 2025-08-13 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 7880e4da-bcde-3c14-88b1-6b86471fd940 | -15.56167 | -58.72267 | 2025-08-13 05:08:00 | NPP-375D | FIGUEIRÓPOLIS D'OESTE | MATO GROSSO | Brasil | 5103809 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8f1e453a-2cd2-364e-ac3f-534bbf1a8137 | -9.37403 | -61.5278 | 2025-08-13 05:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 629e64b9-5ca4-3598-9aa9-638f5b7d2303 | -10.97099 | -49.56576 | 2025-08-13 05:08:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |


[Clique aqui para ver as próximas entradas](README29.md)
