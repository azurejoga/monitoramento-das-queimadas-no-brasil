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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e4e87390-17dc-3037-9ac5-4083e59cbc9c | -12.34493 | -48.20252 | 2026-09-19 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d6acd794-bea5-353b-a970-e44e5de98c6d | -12.12374 | -46.99572 | 2026-09-19 04:04:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 81bf4c95-4766-3074-8249-df01c31f496a | -11.97029 | -45.77631 | 2026-09-19 04:04:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1a0ec9cf-b245-3444-9f88-1681b9600c01 | -10.55986 | -51.31577 | 2026-09-19 04:04:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| fa0c2f52-a108-336a-a1db-7b1086b8c2c6 | -11.06177 | -49.76297 | 2026-09-19 04:04:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b558dd1e-04d7-36a9-82e7-fe7eebfcd4ac | -14.79539 | -48.54827 | 2026-09-19 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 76856b5d-ca70-38f9-bb5b-274da2b64291 | -13.0196 | -46.97816 | 2026-09-19 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2079094c-26ba-3565-a29e-a02cf524fc78 | -13.88581 | -48.60294 | 2026-09-19 04:04:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5f00daf6-5f65-332d-8217-f3669017918b | -11.30616 | -51.72239 | 2026-09-19 04:04:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| f71235aa-b630-3779-9d01-0e4a39630cdd | -12.12997 | -47.00861 | 2026-09-19 04:04:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 35dca8ff-686c-3e82-8e2c-a564a0738e4f | -10.91513 | -48.41792 | 2026-09-19 04:04:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b9907047-acf6-3092-84d0-1805ff14bc72 | -11.80442 | -46.84319 | 2026-09-19 04:04:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ea6a4821-e785-31ad-9d7a-116219745b59 | -12.14036 | -47.02221 | 2026-09-19 04:04:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 33209689-d486-3e24-a09a-39ab258cdad9 | -13.2361 | -46.9394 | 2026-09-19 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 28274f9a-4873-3eff-ad46-ce36b227c088 | -12.49065 | -50.04943 | 2026-09-19 04:04:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 00c0c511-a88f-3c86-9a09-4107f52a3470 | -11.06005 | -49.76389 | 2026-09-19 04:04:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 28363597-56d5-3110-93a4-6bf9d7b8e08c | -10.4647 | -51.26271 | 2026-09-19 04:04:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| cac92a11-9fbd-34ea-9170-cc62d91d92df | -16.83908 | -47.63639 | 2026-09-19 04:04:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 56d7baaf-bcc5-3d84-8c13-901a4ba50a3b | -11.30137 | -46.76852 | 2026-09-19 04:04:00 | NOAA-21 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c8454675-8163-3595-a853-5dc3c494688d | -14.1515 | -45.21096 | 2026-09-19 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6efc2916-18e1-370e-909d-7ef814626119 | -13.60921 | -48.31013 | 2026-09-19 04:04:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 0d7a8827-c1e1-3c77-9ae9-a0c60996d484 | -11.42509 | -51.45355 | 2026-09-19 04:04:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7bed704c-2f78-3533-88db-1552f6a63613 | -14.66205 | -46.66168 | 2026-09-19 04:04:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 7.3 |
| c26e720b-6773-3b03-a802-258241e84b19 | -13.60392 | -48.31413 | 2026-09-19 04:04:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e04eea63-ba7a-33dc-96aa-10e221e61b24 | -15.63391 | -52.7221 | 2026-09-19 04:04:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 337aae88-c325-3b33-905c-4a1b31b6dd84 | -12.41632 | -45.04568 | 2026-09-19 04:04:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1e6e6177-3349-3e16-bccb-fc5f9f7b72da | -10.83384 | -50.91474 | 2026-09-19 04:04:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 905c32ac-bfe3-3782-9b09-b3e20825fed1 | -11.08754 | -48.2753 | 2026-09-19 04:04:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 246485e7-5bb0-3898-b46a-9f741b1debc6 | -12.12249 | -45.15828 | 2026-09-19 04:04:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3b5edc87-4243-3e5f-88c5-53259debb3f3 | -12.97679 | -46.98419 | 2026-09-19 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b1ac10ad-4c93-3c28-99fe-fb6e779b3953 | -13.64548 | -46.94892 | 2026-09-19 04:04:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ae6e5f4d-e99b-37bb-968c-58f3e74d20fe | -16.59974 | -46.99182 | 2026-09-19 04:04:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 00b769a6-29d0-39d6-877e-a7a1b55a5e2c | -13.01936 | -46.93241 | 2026-09-19 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 68a7a301-9550-3f0a-a26d-72834dd17496 | -12.58698 | -42.22406 | 2026-09-19 04:04:00 | NOAA-21 | IBITIARA | BAHIA | Brasil | 2913002 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 1cdfeca5-67a1-3226-9ae5-c718e6df8c3c | -13.59693 | -46.93534 | 2026-09-19 04:04:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a84c7373-9237-3827-82bf-c8b5536c83b4 | -10.92602 | -47.8573 | 2026-09-19 04:04:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 6afcbc55-6736-3246-83fe-ec1089633947 | -10.83243 | -50.92198 | 2026-09-19 04:04:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| afb4e789-547e-3744-980c-f951acc4d42f | -17.95856 | -45.12177 | 2026-09-19 04:04:00 | NOAA-21 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 33c81258-26c9-30f8-a9b2-2965fc1a0226 | -10.99377 | -48.32174 | 2026-09-19 04:04:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 52851182-a835-36c6-ba92-1f630533895f | -13.74086 | -48.7868 | 2026-09-19 04:04:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0ef256fa-3726-35be-99b7-2a95e5ad8d96 | -10.44849 | -48.67629 | 2026-09-19 04:04:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a5b6dee9-eb71-3494-b8eb-1db50eeb6934 | -10.83127 | -50.16642 | 2026-09-19 04:04:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5b4177cf-4e10-39fd-b008-ed38d8bb5190 | -11.80964 | -46.82928 | 2026-09-19 04:04:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 85ea61c2-8950-32ad-9d26-223593bf0b93 | -9.93978 | -53.9883 | 2026-09-19 04:04:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| fec79f5c-1dd2-341b-8e28-218a702b1e4a | -14.67458 | -46.65878 | 2026-09-19 04:04:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| b0a6d061-5c25-34db-a776-62c21a9a407d | -11.8335 | -46.83815 | 2026-09-19 04:04:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f27db33c-808b-32a8-9c86-6adbc67a8757 | -18.56754 | -45.88377 | 2026-09-19 04:04:00 | NOAA-21 | VARJÃO DE MINAS | MINAS GERAIS | Brasil | 3170750 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 02f90122-0e10-349a-813f-949a877b3be9 | -11.72288 | -47.73231 | 2026-09-19 04:04:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 83d87e39-438a-3344-9bbb-c07cba8aecf0 | -12.58513 | -49.09513 | 2026-09-19 04:04:00 | NOAA-21 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 5ed1c71b-73ec-36cb-9717-526406858010 | -11.67744 | -54.4481 | 2026-09-19 04:04:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 96b5ec4b-3468-33e8-af9a-b98407aa1944 | -11.79986 | -46.79594 | 2026-09-19 04:04:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 38031d99-c297-3438-af71-c4a07b82056a | -10.93122 | -47.85394 | 2026-09-19 04:04:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 77d074cf-e801-33ce-b869-c4c40f909a3b | -11.83006 | -46.83362 | 2026-09-19 04:04:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d6afcdd5-bfc9-315a-a558-19bce07ace47 | -12.33445 | -50.73157 | 2026-09-19 04:04:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5efca464-de54-3a51-a80e-6d23c39ecc94 | -11.47147 | -47.40921 | 2026-09-19 04:04:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 23c515fb-5da4-39d9-bac7-e12dd59757f5 | -14.68053 | -46.6517 | 2026-09-19 04:04:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 132bc316-d08e-361b-8e7e-0b93467cdd29 | -10.70088 | -50.25622 | 2026-09-19 04:04:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0f9a96bc-f0ac-3ebf-aa33-7fe12d4ded79 | -11.80459 | -46.79302 | 2026-09-19 04:04:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 034abf96-bb23-3c22-ba5b-65de58aaf7a8 | -15.03106 | -48.57467 | 2026-09-19 04:04:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 29eaa383-c903-3a24-be6f-63286c3402d0 | -15.02919 | -48.56044 | 2026-09-19 04:04:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5ba555cf-0587-389f-9019-4c1dc6f26d04 | -12.13069 | -47.00459 | 2026-09-19 04:04:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| cfd1472d-cb97-3bec-959a-06de412301cc | -11.41474 | -47.28107 | 2026-09-19 04:04:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 535ab7fe-b9c6-33d8-afed-6e5eaebb439b | -15.88176 | -49.89183 | 2026-09-19 04:04:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3df10c77-77e6-3954-8314-aa7973b2c8dc | -14.93776 | -49.93699 | 2026-09-19 04:04:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 076a39bd-da77-308d-b398-a78f209f5076 | -12.99653 | -44.8338 | 2026-09-19 04:04:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 71a61372-2ad6-3c83-aa73-86c220089273 | -14.92442 | -49.929 | 2026-09-19 04:04:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 8e2c7edf-0985-329a-a0dc-b1eabef7549c | -13.60631 | -48.30147 | 2026-09-19 04:04:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 42d2196c-7743-3250-b8d3-5c7dce07b5bb | -14.15316 | -45.21656 | 2026-09-19 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fdcb1dd7-9a6e-3cb3-804a-81734611b21e | -11.42435 | -51.45738 | 2026-09-19 04:04:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a500d822-3ba4-3856-a49c-33415b1e824a | -11.97961 | -52.45266 | 2026-09-19 04:04:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| b246c13c-7aef-373e-b6bc-0c0e18e1147d | -11.43631 | -51.45575 | 2026-09-19 04:04:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 08d58172-53c9-331a-af72-73a7ff49b8bf | -15.02669 | -48.57389 | 2026-09-19 04:04:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 8.8 |
| ce8171de-a98a-3b25-b2bf-e7d769ce22a0 | -10.27496 | -50.0131 | 2026-09-19 04:04:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fe19dabe-c3d7-3548-a285-43d7137cf94b | -11.05314 | -48.30867 | 2026-09-19 04:04:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 794c6dea-4e92-3f11-a527-169fcfcfa4b4 | -10.32391 | -53.58134 | 2026-09-19 04:04:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| af6e0f25-fae3-37f5-a56a-4cfb311f1122 | -10.98359 | -49.70491 | 2026-09-19 04:04:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 606d9c8f-4f37-375a-bebe-4f0d75cfa155 | -11.02017 | -54.13218 | 2026-09-19 04:04:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 704150c0-bb04-3b92-b5c0-0e5201071a8c | -10.83348 | -50.91468 | 2026-09-19 04:04:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1142a99c-6f82-303b-9a78-ec5da1bdb454 | -12.50353 | -38.2069 | 2026-09-19 04:04:00 | NOAA-21 | CAMAÇARI | BAHIA | Brasil | 2905701 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 8946e981-4ddc-37e7-9451-0d573c78b90b | -10.86731 | -54.09835 | 2026-09-19 04:04:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 332d1503-e0f8-3531-b0ec-25f15a997996 | -13.38631 | -48.0396 | 2026-09-19 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8a39ee02-8700-39ae-a166-a8751544d1cf | -12.3994 | -45.05662 | 2026-09-19 04:04:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7831f3d2-6d7e-3faa-88cd-6ea434101c1b | -11.91374 | -50.11958 | 2026-09-19 04:04:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| b6d87f50-50e8-3a88-9f9a-bcb926265ad5 | -17.05674 | -45.63774 | 2026-09-19 04:04:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 402ec9f5-9434-31f9-b3c4-64f1b2448108 | -13.62492 | -48.29898 | 2026-09-19 04:04:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| c36f773c-db3b-30e4-90c7-0a0a2945c7de | -13.64079 | -46.9519 | 2026-09-19 04:04:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| df5a5ba5-2512-3f30-83a4-9046e606ddcf | -11.30617 | -46.78955 | 2026-09-19 04:04:00 | NOAA-21 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c149be5c-86f1-3ea7-a104-5f2df4f065ab | -10.97121 | -49.74297 | 2026-09-19 04:04:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ce3592c8-a498-3f60-8d0d-4e6130230652 | -11.36829 | -47.32629 | 2026-09-19 04:04:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b7f97528-293e-3968-862c-be71fb4d13e3 | -11.43556 | -51.45959 | 2026-09-19 04:04:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 332d10e0-9f25-3955-8ded-52ce8ddc251b | -13.62048 | -46.9667 | 2026-09-19 04:04:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 4dc43e41-3242-352f-9aae-e72fc1052224 | -13.00215 | -46.9818 | 2026-09-19 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| a867373f-5bbc-39e2-914c-44e38aab1628 | -12.99223 | -44.83733 | 2026-09-19 04:04:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d343b938-b022-3873-ad11-3ab4c108d2e0 | -11.08058 | -48.28775 | 2026-09-19 04:04:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 23.8 |
| 7e641097-c173-304d-9a8e-bd538d8b0dd8 | -10.83524 | -50.90751 | 2026-09-19 04:04:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d285077b-2e94-3e9c-a3f6-694bf3f7f9d6 | -12.1425 | -47.01017 | 2026-09-19 04:04:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 48f8849b-1e39-3410-8f0c-e3120db81f48 | -13.74173 | -48.78944 | 2026-09-19 04:04:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4d648367-cdd7-335d-8717-90e8fad322eb | -11.08138 | -48.28327 | 2026-09-19 04:04:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 40d93075-3d7b-346b-b495-b2e84ccab14e | -10.45233 | -48.68227 | 2026-09-19 04:04:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3853ebcb-1ac0-3cbf-b877-45f6592e7d9d | -12.12305 | -46.99958 | 2026-09-19 04:04:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |


[Clique aqui para ver as próximas entradas](README40.md)
