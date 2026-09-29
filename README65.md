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

## Dados Diários - Página 65

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0467d7c3-d153-317e-8edc-772e52482545 | -13.17454 | -48.54744 | 2026-09-29 05:12:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d1b48b4d-005b-376a-b654-4f9a0177167d | -13.52928 | -46.90284 | 2026-09-29 05:12:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e7d34539-2afd-3f11-a409-d67621b78a3b | -10.72379 | -53.99053 | 2026-09-29 05:12:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6d4a3357-30ff-33e1-83fa-bae29dbc9e0e | -12.00816 | -50.9796 | 2026-09-29 05:12:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b1b6a862-eaf1-3858-a7b7-2d1063e37780 | -10.27836 | -44.64002 | 2026-09-29 05:12:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e13256bb-9024-3501-950c-6401bb5f7b54 | -12.69169 | -47.2599 | 2026-09-29 05:12:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 74c1a5f9-6d37-36ee-a187-75b0bf835db6 | -11.13057 | -48.33681 | 2026-09-29 05:12:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 91649c5e-97b1-3a10-8e78-aa66ba455d8e | -9.13397 | -49.97598 | 2026-09-29 05:12:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dfdf2f68-75c7-32ab-aaed-6e140c7b8e01 | -13.09007 | -47.43617 | 2026-09-29 05:12:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4974cf9a-a884-3af9-9a6b-9a253fa421c3 | -10.59422 | -46.21681 | 2026-09-29 05:12:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4ff5d373-1328-3c90-aff9-ac7928d5e7f0 | -11.47776 | -49.73259 | 2026-09-29 05:12:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| acb338b9-34dc-374f-89e6-85961cfb551e | -12.74956 | -54.05266 | 2026-09-29 05:12:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2915bc05-8baf-3515-9fed-40b7aea9f1d4 | -10.39101 | -61.24038 | 2026-09-29 05:12:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 71e8434d-d651-3421-8103-9d61d265f066 | -12.60807 | -60.8998 | 2026-09-29 05:12:00 | NOAA-20 | CHUPINGUAIA | RONDÔNIA | Brasil | 1100924 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 88be3618-ad5a-3dfd-8c83-dfcc8f86a7c1 | -11.36194 | -54.04491 | 2026-09-29 05:12:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fae7607e-9baf-379d-bf52-e7a0898dca2e | -11.41011 | -43.42959 | 2026-09-29 05:12:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0ed82b71-7275-36db-820e-4d81b65bf9ba | -10.39786 | -61.24657 | 2026-09-29 05:12:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 668c4404-2ec0-32a9-a0e4-42968ee24f6d | -12.74062 | -47.28314 | 2026-09-29 05:12:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d80bee44-fc40-3743-a0b3-a60625eb49c2 | -13.54489 | -49.17334 | 2026-09-29 05:12:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 80b83500-db21-3d8a-8a09-bd269395d235 | -10.79228 | -48.75454 | 2026-09-29 05:12:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 3f907e60-514c-36cc-8b9e-574979d60105 | -11.39253 | -54.03678 | 2026-09-29 05:12:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 96739a89-12f4-3934-b0f1-3e8c3abe9d37 | -9.14294 | -49.97725 | 2026-09-29 05:12:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3db6283c-c9ed-37d0-b0d8-b5663b1584cc | -11.38472 | -54.03989 | 2026-09-29 05:12:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3bf1f018-db47-30fd-b971-677e66d642b5 | -12.00091 | -51.00029 | 2026-09-29 05:12:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 495ba818-b20f-36ff-a51c-364c64139edb | -14.11261 | -46.29 | 2026-09-29 05:12:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1e07a631-d4d5-355c-afa6-d4f7aa7b5e77 | -12.6073 | -60.90419 | 2026-09-29 05:12:00 | NOAA-20 | CHUPINGUAIA | RONDÔNIA | Brasil | 1100924 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 16b72c3e-c0d7-3c80-9118-7846d1853ff0 | -7.50219 | -55.03789 | 2026-09-29 05:12:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ee758ac1-0004-3ec5-b916-7c7cfc6da0b6 | -9.08672 | -49.88624 | 2026-09-29 05:12:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1c722cee-0c19-31d8-a3b7-2a63752ad05d | -12.93962 | -46.65337 | 2026-09-29 05:12:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e80450c5-09f0-3435-9f51-6620f811d2ca | -10.26171 | -59.03164 | 2026-09-29 05:12:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bd0a01dc-540d-37c7-8d61-5c58a9dfdfd9 | -12.05787 | -46.49691 | 2026-09-29 05:12:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0df91c6e-8ebf-3fb2-b857-18c3c0b4793a | -9.14357 | -49.97276 | 2026-09-29 05:12:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 71c610ce-6b2d-3ee0-8c28-eb58fb9756f4 | -12.78315 | -54.02679 | 2026-09-29 05:12:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d30ecde6-aa87-38e0-9bb6-c2abbeb1b40d | -12.76143 | -47.3007 | 2026-09-29 05:12:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 01428dc9-b19e-3297-a894-debd460ad6f3 | -11.39529 | -45.41622 | 2026-09-29 05:12:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 42241a39-4fbf-303f-bc5f-90562ec5ce55 | -7.51 | -55.03178 | 2026-09-29 05:12:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| fe8d8ea3-9b41-3d9d-8011-6922a58748e9 | -11.43371 | -43.47419 | 2026-09-29 05:12:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 29951830-8062-3422-a862-69b90af66ccc | -11.93165 | -50.88322 | 2026-09-29 05:12:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ecb97c6e-b79b-3e61-99a2-4b7a11f954cf | -12.05278 | -50.94656 | 2026-09-29 05:12:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 08575d67-5bdb-31db-b45f-e8bcb22f0901 | -11.93107 | -50.88754 | 2026-09-29 05:12:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 10b9355b-81db-3724-b498-dad46164ff6b | -11.99851 | -50.95209 | 2026-09-29 05:12:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1756d3db-bae2-383c-9345-284578e99169 | -12.55753 | -47.1562 | 2026-09-29 05:12:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 86fc30a4-ab50-388c-a9b7-e09aa6348931 | -12.0131 | -50.97594 | 2026-09-29 05:12:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| df4adb92-f553-3c95-9481-cf7e8f1e1e3c | -9.93206 | -60.72707 | 2026-09-29 05:12:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6406de4e-10ee-3d51-9b83-a3ad605023f9 | -9.92613 | -60.71663 | 2026-09-29 05:12:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b53bb0ea-8d3c-39c4-a5f7-b3616f2316b1 | -13.17763 | -48.56556 | 2026-09-29 05:12:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3fddd1e7-cffe-3c07-b275-5238ef8c19e3 | -12.47402 | -47.48888 | 2026-09-29 05:12:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| df6d5c26-8c1c-3fe8-9200-da129161a2f5 | -11.90076 | -50.62016 | 2026-09-29 05:12:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d56bcc48-cf2e-37ca-9cd1-ef2ab046bf82 | -13.53945 | -49.17587 | 2026-09-29 05:12:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 27694666-a9fc-3f53-ade7-9079d6615790 | -12.59773 | -51.96745 | 2026-09-29 05:12:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0a480744-6f6b-3c1b-a4ed-ffe405171ef0 | -11.98101 | -50.94963 | 2026-09-29 05:12:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e967fd43-68b7-34ec-8d2b-33874c615a95 | -12.15948 | -50.82296 | 2026-09-29 05:12:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 38be978e-a042-39d6-a79a-47ff51af2814 | -10.70006 | -44.42329 | 2026-09-29 05:12:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 98bb0c55-69cb-348f-9a98-84f5790bda09 | -10.40087 | -61.25204 | 2026-09-29 05:12:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 07413909-277c-37b0-baa8-6062f23bd3d9 | -12.77285 | -52.81589 | 2026-09-29 05:12:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9db902e0-8266-3398-96a6-8c7b5f00b3fb | -11.39202 | -45.41163 | 2026-09-29 05:12:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4cadb4ae-6fad-30b5-b19e-123955b2198f | -12.62574 | -47.26044 | 2026-09-29 05:12:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 40330258-3c04-3a77-ac58-c95334c993f7 | -12.74293 | -47.28886 | 2026-09-29 05:12:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 24da211d-65f0-3d76-b3f9-fe216c3b1cf1 | -11.40633 | -43.42245 | 2026-09-29 05:12:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 88844a9c-e110-3930-be97-373855e588e1 | -7.51056 | -55.02821 | 2026-09-29 05:12:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5696da14-9cc7-3e9f-9172-ae4e913073ef | -9.76055 | -44.83216 | 2026-09-29 05:12:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 448609fa-8970-3fcf-a865-0143b0dbe7d0 | -12.01395 | -50.93676 | 2026-09-29 05:12:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 363e6341-77e3-389d-8657-8a9ce8d15798 | -12.39008 | -50.22252 | 2026-09-29 05:12:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1c69c8aa-6642-3cd3-a113-9a8b45bda741 | -7.50945 | -55.03537 | 2026-09-29 05:12:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 738d3520-4c46-3d02-9a8e-36cac4e092c1 | -14.21812 | -48.50858 | 2026-09-29 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 776076dd-e8cf-305f-84d2-e68ddc240d94 | -10.41582 | -53.77816 | 2026-09-29 05:12:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| a0ddc9d2-a36e-32eb-93c5-f24afcb19dbe | -13.06492 | -47.45574 | 2026-09-29 05:12:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d7daeafb-098f-3eaf-9556-015b9f250275 | -11.15372 | -48.32 | 2026-09-29 05:12:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f1316e63-cf39-3cd6-82b0-0425f1e8701f | -13.48118 | -48.61433 | 2026-09-29 05:12:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 04d2a8a4-3a3b-3abb-9083-098db6929ad5 | -12.05337 | -50.94227 | 2026-09-29 05:12:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 01725c93-51ea-3398-a65b-cc51a6a4bbac | -8.29465 | -54.71555 | 2026-09-29 05:12:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5eb144bf-24bc-3882-a2c8-2a53b171872e | -11.34077 | -54.11382 | 2026-09-29 05:12:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 69e311e2-fd34-3931-a872-bd5f8c10f2fc | -15.00994 | -51.40421 | 2026-09-29 05:14:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7138eaf0-65d9-383e-9ca0-8068436c0e5d | -15.08252 | -48.33504 | 2026-09-29 05:14:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| da13e17e-a3cd-3021-b501-3c605cae26fd | -18.10084 | -44.35776 | 2026-09-29 05:14:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 784aebdd-a19e-3403-ab12-a7e099b78b51 | -15.45082 | -46.14261 | 2026-09-29 05:14:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 740501ad-393b-39d5-9e2d-a90180574147 | -21.0554 | -48.87635 | 2026-09-29 05:14:00 | NOAA-20 | CATANDUVA | SÃO PAULO | Brasil | 3511102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 6092a981-665a-3998-8649-1360cd197738 | -14.77217 | -47.15712 | 2026-09-29 05:14:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8502725c-59a4-35a1-9b28-571d8d6b47fe | -15.44404 | -46.14665 | 2026-09-29 05:14:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d0a9a358-15dc-3128-ab09-799cae39cc9b | -12.84716 | -62.16993 | 2026-09-29 05:14:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 315d0bb0-c6b7-386e-bf26-7706f47501fd | -15.00324 | -47.8684 | 2026-09-29 05:14:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e6015b06-24f8-3149-bf23-eb1b9bd3ea14 | -15.21999 | -46.17173 | 2026-09-29 05:14:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8425061a-c60a-3ff2-827d-1abe7fb2aecd | -16.33247 | -47.69514 | 2026-09-29 05:14:00 | NOAA-20 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 21d28758-5d66-3a24-b889-c92963785d4c | -14.95804 | -47.54455 | 2026-09-29 05:14:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9edd0f0c-d622-3454-8e6c-e1eabd8c2158 | -14.63631 | -52.07855 | 2026-09-29 05:14:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 9069ac66-3a9d-3917-ae33-1a7f263f979e | -14.09703 | -54.30388 | 2026-09-29 05:14:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 68caa679-1492-3399-af38-8063ad78a887 | -15.01041 | -51.40581 | 2026-09-29 05:14:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5189e81f-9509-37d1-8c3f-cfde87157a31 | -18.57218 | -48.42138 | 2026-09-29 05:14:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 38c34ccf-d67e-3bc4-bd0b-112ac3f86e77 | -15.38266 | -47.91667 | 2026-09-29 05:14:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c44c9ad7-a1cd-31e4-9240-baa236d62da0 | -18.57521 | -48.42127 | 2026-09-29 05:14:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| d51cc054-edd5-356d-a700-9e2b8e9462ea | -20.09644 | -57.20749 | 2026-09-29 05:14:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Cerrado | 5.9 |
| b1718d15-073b-35ed-b627-6f0cc729473b | -15.22338 | -46.18016 | 2026-09-29 05:14:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 4e98ab62-2e0c-3050-b8c0-8d0afdbc0b80 | -16.69439 | -51.84088 | 2026-09-29 05:14:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fbdbe862-fb66-3e88-9715-76cb301bb159 | -19.90975 | -54.58265 | 2026-09-29 05:14:00 | NOAA-20 | ROCHEDO | MATO GROSSO DO SUL | Brasil | 5007505 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| dab0f1f5-5308-37a0-8ce5-9d6c7e4f1000 | -15.38918 | -47.9094 | 2026-09-29 05:14:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| faf3333e-8e73-3472-a7ad-0f885aab015e | -12.81974 | -61.57735 | 2026-09-29 05:14:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e2841e66-83b4-3dba-9dff-bc122999c819 | -14.49872 | -59.74793 | 2026-09-29 05:14:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 08107b45-3be1-3202-aa79-35e2c7958887 | -15.3818 | -47.92426 | 2026-09-29 05:14:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 1e3674f3-cea9-3dea-8239-8d2d816b9964 | -14.10315 | -54.28708 | 2026-09-29 05:14:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bb0eb579-7555-3536-9e09-d580c29871e7 | -14.63335 | -52.13353 | 2026-09-29 05:14:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README66.md)
