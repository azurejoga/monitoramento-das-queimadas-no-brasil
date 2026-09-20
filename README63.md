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

## Dados Diários - Página 63

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1d73de3e-fb87-30c0-a14f-090905543b0c | -12.75784 | -46.21687 | 2026-09-20 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2a78c579-9162-3f8e-889f-0a17dfe808ef | -6.45226 | -48.44391 | 2026-09-20 04:40:00 | NOAA-20 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f27a61af-a433-3bca-9562-2162579bf14c | -5.76383 | -57.45466 | 2026-09-20 04:40:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ec28e2b9-ade1-32b3-9304-e7c3fd7c5d7f | -6.66973 | -50.89224 | 2026-09-20 04:40:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1185e2db-7289-3e17-be5e-1d7e4f87921a | -7.36769 | -44.86988 | 2026-09-20 04:40:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0f2858b1-27da-3e3e-8302-09b7ee85baf3 | -9.23689 | -46.18232 | 2026-09-20 04:40:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8a5c5b38-7352-3e9a-afe6-5534f052ed0c | -10.27908 | -50.24261 | 2026-09-20 04:40:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7a6a9804-2af5-304a-a186-d0d1255bbf4f | -7.44797 | -44.73625 | 2026-09-20 04:40:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 02001228-ebdc-3b86-a0be-136a3bb08c78 | -11.86171 | -47.65382 | 2026-09-20 04:40:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 231b9cb7-d236-38bc-8e09-bf77f89473f6 | -13.39717 | -49.45853 | 2026-09-20 04:40:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0f260ecc-6c56-3ef7-b0eb-f3be34355756 | -7.62745 | -46.75271 | 2026-09-20 04:40:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6b88e918-2902-3c41-9ed0-6bc4f20fc0cc | -8.05258 | -46.28864 | 2026-09-20 04:40:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| c7321d7f-5eaf-315b-a652-eb8690fe400a | -6.99308 | -49.80398 | 2026-09-20 04:40:00 | NOAA-20 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6b34e80c-75e8-3453-8a5b-61e2ffdb2a14 | -6.6662 | -50.89162 | 2026-09-20 04:40:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7136d2f1-f66d-34e9-9fb5-82a203a76db7 | -9.94461 | -45.54644 | 2026-09-20 04:40:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cbc9aa4a-4742-3795-9675-ec8cf42c9484 | -8.43773 | -43.86433 | 2026-09-20 04:40:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 611dc943-6759-3f0c-8dea-66b95389ef08 | -10.44964 | -51.24369 | 2026-09-20 04:40:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4e517226-a981-3045-a49e-68266a2671b3 | -11.02104 | -54.15528 | 2026-09-20 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 267843f4-2562-367a-90af-6a50e7e8c662 | -11.0167 | -54.13265 | 2026-09-20 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| effe894a-21e0-3e8f-82d9-3d29efb73636 | -9.69841 | -48.32146 | 2026-09-20 04:40:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a31a75ee-6f73-3eb2-8f44-4e3794c84f0b | -11.90543 | -49.95255 | 2026-09-20 04:40:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cf2727a5-0fd6-39eb-b4e0-59ead2fe39a9 | -11.03643 | -54.16186 | 2026-09-20 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5198be7c-0bed-3dbd-b2a4-8c42b4bbe542 | -8.05092 | -46.25343 | 2026-09-20 04:40:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| c20386cd-3a56-3ec6-8e0f-f8825cfa1b8a | -8.76458 | -48.66532 | 2026-09-20 04:40:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 7.2 |
| a8106c08-e01b-3132-aec4-a813495b8e8d | -7.0904 | -44.72663 | 2026-09-20 04:40:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 59f1d1bf-3a02-3f93-99e5-de848249fe54 | -9.79342 | -45.07048 | 2026-09-20 04:40:00 | NOAA-20 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8396810c-ef6d-33fa-952f-0986cf7a5fe0 | -5.84164 | -53.54528 | 2026-09-20 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 50e309d6-fd8b-34f0-b690-ef32f0a0a81e | -8.04515 | -46.26804 | 2026-09-20 04:40:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ff0280f3-4d00-31d2-97e5-433f4b4edff0 | -11.36831 | -51.39404 | 2026-09-20 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cd51fdd9-c060-3d4a-8e5a-ea3ca4fcb5e8 | -5.94117 | -53.8277 | 2026-09-20 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 048d786c-914b-323e-98ea-430d486dda36 | -9.26314 | -46.19824 | 2026-09-20 04:40:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 34e960e4-8909-36e5-9465-ae78b22b5521 | -11.0855 | -48.30725 | 2026-09-20 04:40:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| a81cda37-6eb5-3106-956c-e9cf9b293809 | -9.67549 | -54.32456 | 2026-09-20 04:40:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c127f62d-c17b-3d26-920d-98eeaaa9a612 | -11.44126 | -45.42037 | 2026-09-20 04:40:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f1452ffa-2390-34e1-b823-d7011a0d4188 | -5.84335 | -53.51024 | 2026-09-20 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c81dba83-c169-3ac9-8aaf-72e7464b4796 | -9.71699 | -48.02884 | 2026-09-20 04:40:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f13efd71-e90d-3496-b762-dcc0fd2e6139 | -11.48177 | -47.78347 | 2026-09-20 04:40:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 933ffa3f-8c70-330c-9e71-6295d1d05b5b | -13.74393 | -48.78084 | 2026-09-20 04:40:00 | NOAA-20 | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 12ff1443-f311-3921-a523-b7d7a6ffc0e9 | -9.30081 | -62.31388 | 2026-09-20 04:40:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b3e25ce8-5c43-3444-b27b-df3fc12d1ed2 | -8.75576 | -48.65678 | 2026-09-20 04:40:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 3.4 |
| fbb41900-95b7-38b6-9d71-f29416d23fbd | -7.63807 | -45.85807 | 2026-09-20 04:40:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 01ddd9fd-c622-3925-a0d6-4fbc4429d8e2 | -5.85916 | -53.49308 | 2026-09-20 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0f1d597b-0183-37c9-af60-bd5fb218b249 | -10.27324 | -50.27879 | 2026-09-20 04:40:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 7128ee61-6eb2-3851-80fa-e9ea61e26175 | -11.45961 | -47.64861 | 2026-09-20 04:40:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7c38d725-dab3-3f3c-b1a8-02ec2c3b9429 | -8.16035 | -54.82407 | 2026-09-20 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 750a02af-403b-3183-9f82-aa97e09c8a9b | -5.86832 | -52.0392 | 2026-09-20 04:40:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9342892f-2eec-3201-b3ca-8af01ef214e6 | -9.25897 | -46.2257 | 2026-09-20 04:40:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 694d8f82-0508-3db0-9a5d-5bda6749e2d7 | -8.41948 | -45.87531 | 2026-09-20 04:40:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 445a125e-806f-395e-a257-f90b3ddbf296 | -10.31295 | -50.21461 | 2026-09-20 04:40:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 70ef6810-7c88-35d2-baca-d803f0b066dd | -7.63985 | -45.82254 | 2026-09-20 04:40:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c115f72f-fa51-3d93-a2b8-9e86929dc880 | -13.02282 | -46.90557 | 2026-09-20 04:40:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 79963dbc-cabb-3033-ac8b-e4777716fb1d | -11.12335 | -54.02703 | 2026-09-20 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 22.6 |
| 473f9b51-06f9-3436-b977-2f3304178dba | -11.44901 | -45.39356 | 2026-09-20 04:40:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e45ab89b-af28-329c-84f8-f5ade2bce642 | -5.85616 | -53.53582 | 2026-09-20 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 72ee46ed-2fe4-392e-af16-d50cc9491634 | -7.44297 | -44.74435 | 2026-09-20 04:40:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8b86b1cf-2977-3388-bc4d-b2ec67387441 | -9.17933 | -60.76778 | 2026-09-20 04:40:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 797494a3-6093-3789-a9cb-f2cc59eba7f9 | -8.50635 | -47.43319 | 2026-09-20 04:40:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8a49312b-ce0d-31b4-912e-7f71bb2cd754 | -6.66607 | -50.93707 | 2026-09-20 04:40:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4db41623-547d-30fb-8976-d2e2d5e2f457 | -5.8436 | -53.53384 | 2026-09-20 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 00c1e0eb-8030-3746-ad91-2b0825e4cf2e | -5.84491 | -53.52621 | 2026-09-20 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 418f4e7b-91ce-3527-962f-b991f4232377 | -9.81653 | -48.32568 | 2026-09-20 04:40:00 | NOAA-20 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4bcdaf14-c167-33b0-9779-9788e5bf1713 | -12.73892 | -46.18898 | 2026-09-20 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b185c0c3-ec81-3fc4-8f82-d7290a72e272 | -11.45512 | -45.40387 | 2026-09-20 04:40:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 67ffae87-0272-3700-8329-a55ab62d5198 | -12.34011 | -50.69032 | 2026-09-20 04:40:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 85a71ec2-e1e1-3e50-b0e3-6f67019d7486 | -8.37649 | -45.63564 | 2026-09-20 04:40:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 95147d7e-ed38-36f1-9751-d34cb4dd6fa8 | -10.47279 | -46.30059 | 2026-09-20 04:40:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0868fbc4-866b-317c-a348-e09744b7568c | -9.81079 | -47.1745 | 2026-09-20 04:40:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d3bb103b-07b0-35d5-aac5-eaf556d6d972 | -11.76313 | -47.45208 | 2026-09-20 04:40:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e6b005ac-9e80-3953-83c7-041e67d8bb9a | -11.22994 | -54.08568 | 2026-09-20 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9640120e-a238-3aba-9046-3e2d045d8329 | -13.72893 | -48.78938 | 2026-09-20 04:40:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e9233098-c266-301a-8d87-ca6bc10877c6 | -12.52696 | -50.08081 | 2026-09-20 04:40:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4ef279ce-1b8d-3e67-b17a-64191166f151 | -7.63927 | -45.82642 | 2026-09-20 04:40:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fbaa3b45-44eb-3f7b-9ad2-8672f941bdaa | -8.5069 | -47.42964 | 2026-09-20 04:40:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dd001ec6-7ca5-367b-aa0b-7dc637241efe | -9.5944 | -45.36407 | 2026-09-20 04:40:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 55e54f30-b65b-3f71-8684-ea63b481a78a | -10.13694 | -45.55751 | 2026-09-20 04:40:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 822de38e-19f6-3273-ae4e-c34722da88e4 | -9.25333 | -45.92832 | 2026-09-20 04:40:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| de9260bf-1bc0-3427-b3e8-2073d4df1702 | -10.78755 | -50.87179 | 2026-09-20 04:40:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| c790a071-92b7-3a2a-be71-07869b6051b4 | -11.00348 | -46.59438 | 2026-09-20 04:40:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 92eef1ee-e90d-3815-9867-1806ef7e5da9 | -11.8651 | -47.65436 | 2026-09-20 04:40:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1ec0a906-c0a4-34ef-9a3c-7aa720038a30 | -8.02001 | -44.80197 | 2026-09-20 04:40:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4a03967b-69d4-3649-b682-55b8a7b9a589 | -11.39059 | -51.40971 | 2026-09-20 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bbabc8f7-9ba4-3d81-bb10-00bb7ada6bfe | -9.93606 | -60.72576 | 2026-09-20 04:40:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 8df2aa0a-ef54-31fd-a3c4-678ffbd47608 | -5.83904 | -53.53002 | 2026-09-20 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dddab2a1-9347-36ee-ac46-fe0ef17de538 | -10.873 | -56.22604 | 2026-09-20 04:40:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 60c30fd4-6e7a-3703-a2dd-d8ec615979e8 | -10.46939 | -45.09379 | 2026-09-20 04:40:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7f0ecd62-58d9-3bf6-a965-0a74e800b211 | -7.78076 | -44.8282 | 2026-09-20 04:40:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| dfdf733e-02a1-333b-a1f0-368a7a53641e | -10.77946 | -46.32719 | 2026-09-20 04:40:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5f81a805-b610-3ca8-a33d-e5ab635a5b28 | -7.50198 | -46.13294 | 2026-09-20 04:40:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| a266fa82-1f52-3c5d-aa2b-01d7228963df | -10.5983 | -51.90249 | 2026-09-20 04:40:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fd612ebc-006a-333f-be16-7196c62339da | -6.78182 | -48.65742 | 2026-09-20 04:40:00 | NOAA-20 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 28407ede-49a4-3102-9740-2ec491de8782 | -9.27329 | -48.23949 | 2026-09-20 04:40:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c76dbe07-e031-3c99-833e-cd5c36e68ea4 | -9.03125 | -48.71848 | 2026-09-20 04:40:00 | NOAA-20 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9ab238ba-aaff-3820-bb73-eae9c7d6fcf1 | -6.65674 | -50.92725 | 2026-09-20 04:40:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fd67c064-bd46-32fc-8c8c-ea45520d02ed | -7.76962 | -44.83242 | 2026-09-20 04:40:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0b1d2d9c-1820-381f-ad63-b2bf503d5e37 | -7.01852 | -45.24846 | 2026-09-20 04:40:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 58da7f90-7e49-312b-aac5-d599b97154a1 | -7.75166 | -46.7644 | 2026-09-20 04:40:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d0a228aa-0784-3e24-ad94-997b18d2c918 | -13.8799 | -48.57999 | 2026-09-20 04:40:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 90fc844c-6a0a-3af8-92ff-e063bf569545 | -13.62553 | -48.29611 | 2026-09-20 04:40:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c7f33120-114f-3b31-8dc7-c3bbc2a4b1a4 | -5.84034 | -53.55291 | 2026-09-20 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e260bde5-8d71-3ecc-bd2c-66f2ba898a16 | -12.7664 | -52.85497 | 2026-09-20 04:40:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README64.md)
