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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ce77c8b3-a03d-399a-b581-00ab6c648394 | -12.6993 | -45.9445 | 2026-09-19 00:41:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 138219d3-9a91-344c-980b-63094a48fa43 | -11.3686 | -44.133202 | 2026-09-19 00:41:00 | METOP-C | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6f6f9d0d-179c-3e6c-94fe-f7d3112290bc | -12.8574 | -44.388 | 2026-09-19 00:41:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| fb836fb7-4c60-3792-baca-cd7050808001 | -14.6786 | -46.688801 | 2026-09-19 00:41:00 | METOP-C | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| d94e31d5-4fc2-35a2-ad0f-918c6aea8303 | -10.8516 | -54.107101 | 2026-09-19 00:41:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 77b3a849-3060-32ba-89dd-1b4966a10fbe | -18.408001 | -49.1567 | 2026-09-19 00:41:00 | METOP-C | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a4dce883-edbb-3915-9400-f428055e016f | -12.1547 | -46.978699 | 2026-09-19 00:41:00 | METOP-C | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b4d0c89a-2def-3a82-a680-d2ce1fb099a0 | -7.6583 | -46.1208 | 2026-09-19 00:41:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1cc772bb-33da-362c-9c6c-1ae10c387c6f | -11.4133 | -51.453999 | 2026-09-19 00:41:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1b2498f8-97d4-3052-abf1-58bb22adf664 | -10.8679 | -56.2117 | 2026-09-19 00:41:00 | METOP-C | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3acbafc6-40cb-3a36-9f67-172f57ceea86 | -6.3491 | -51.735001 | 2026-09-19 00:41:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 45c7b29b-37e8-3d8a-ba53-ceeb286f5476 | -7.8772 | -46.4361 | 2026-09-19 00:41:00 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a4ca33d9-b5d6-39d9-9a82-2a17b5229bef | -10.8319 | -50.903801 | 2026-09-19 00:41:00 | METOP-C | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ddc9cd95-923d-35ec-b4df-cd550d253eb3 | -4.5702 | -42.953999 | 2026-09-19 00:41:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 43880781-9fcf-365b-a9b3-338d4efd52cc | -14.1334 | -45.186401 | 2026-09-19 00:41:00 | METOP-C | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| efabb85f-ea57-3dab-af90-b76407ca2d7e | -17.9538 | -45.124901 | 2026-09-19 00:41:00 | METOP-C | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| c781eddd-d636-376d-b895-5ad24666fd4a | -15.0286 | -48.573101 | 2026-09-19 00:41:00 | METOP-C | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 53074b8e-0d47-3e42-a8da-b3c1bb6c5f0c | -9.5531 | -46.5807 | 2026-09-19 00:41:00 | METOP-C | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1d6e73c8-51fa-3f64-906a-56896bdfb8b9 | -12.2889 | -49.165199 | 2026-09-19 00:41:00 | METOP-C | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 58f501d9-4761-3891-8146-fcc064edcdba | -10.8485 | -50.185299 | 2026-09-19 00:41:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1a9834a6-31bd-3c3f-ac56-611390719f8c | -8.3769 | -47.2038 | 2026-09-19 00:41:00 | METOP-C | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 32c4eb23-f66b-3526-9f0f-2259473d2bee | -7.6545 | -46.104698 | 2026-09-19 00:41:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b221a0eb-d3af-32af-8e9a-c80a128b3e36 | -12.5512 | -47.087101 | 2026-09-19 00:41:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 94fc8362-f31c-3152-a650-89c9da16e31c | -4.606 | -42.9743 | 2026-09-19 00:41:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 053e9f6f-280a-3a27-8f56-73198cd77bd8 | -11.3259 | -47.6833 | 2026-09-19 00:41:00 | METOP-C | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a12e811c-4bc7-35cf-86c7-e22203dd2f62 | -11.3086 | -51.729301 | 2026-09-19 00:41:00 | METOP-C | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e85c913c-52cc-398b-84cf-235fbad141e9 | -10.0643 | -45.6367 | 2026-09-19 00:41:00 | METOP-C | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 1e5acc1e-9c0b-309c-a423-301a8890fd2b | -9.8999 | -46.562 | 2026-09-19 00:41:00 | METOP-C | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 166e327e-c4d1-3fbe-8a24-7f251c144d65 | -15.0757 | -49.594299 | 2026-09-19 00:41:00 | METOP-C | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| e543b447-f80b-3157-816a-ed2dd7b6fa24 | -14.6819 | -46.658001 | 2026-09-19 00:41:00 | METOP-C | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 3cbea4cc-1287-315b-9bd2-7e2a7fdc9503 | -3.7595 | -44.3839 | 2026-09-19 00:41:00 | METOP-C | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3e99a349-eb17-3380-a37e-4638128db51b | -14.6737 | -46.6675 | 2026-09-19 00:41:00 | METOP-C | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 1f5c3091-6d07-3e33-8e52-f955ebb41fac | -13.6165 | -46.962898 | 2026-09-19 00:41:00 | METOP-C | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 8ce9e7b6-8420-3955-9035-78bddfd3dbab | -0.521 | -49.148701 | 2026-09-19 00:41:00 | METOP-C | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0061fa53-5720-33db-a170-edc77fbabd3a | -5.2521 | -48.192699 | 2026-09-19 00:41:00 | METOP-C | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c12ee3e8-87b0-31ff-9e9f-067995619143 | -11.08 | -50.676498 | 2026-09-19 00:41:00 | METOP-C | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5a216530-6218-3293-82c4-d5c09628406b | -12.1515 | -47.009399 | 2026-09-19 00:41:00 | METOP-C | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ae9ccef8-ba29-320e-a6da-d7e4d2c00c7a | -3.8944 | -49.058998 | 2026-09-19 00:41:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 88fbbece-7028-36ac-985b-aeb688dd692b | -4.5605 | -42.956299 | 2026-09-19 00:41:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 78f6c08a-03fd-38d9-bdc1-1abd2cfca718 | -5.4696 | -49.000301 | 2026-09-19 00:41:00 | METOP-C | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d3c58416-428c-30b6-9e0c-1e95488b08b7 | -11.3142 | -47.272598 | 2026-09-19 00:41:00 | METOP-C | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 908bef9f-7d64-3317-b09f-e2e6d5c6f4fc | -12.1629 | -46.969299 | 2026-09-19 00:41:00 | METOP-C | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| faf3ce88-1e45-3d77-87a7-c92fa149a15b | -1.5884 | -54.429401 | 2026-09-19 00:41:00 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 04504573-352e-3034-a506-f6d6ef3aa1c7 | -11.3663 | -44.124001 | 2026-09-19 00:41:00 | METOP-C | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8ddff532-7eea-3315-badf-2ecd78223185 | -10.53 | -46.7397 | 2026-09-19 00:41:00 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a0241beb-c462-39c9-8d18-6a1798383046 | -11.3125 | -47.265499 | 2026-09-19 00:41:00 | METOP-C | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7c0a4046-a75a-30e9-a63a-2ed51ce4c387 | -6.667 | -50.906101 | 2026-09-19 00:41:00 | METOP-C | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c5f555e7-1e9f-3db6-b618-6e58b472b8ed | -11.0576 | -48.315601 | 2026-09-19 00:41:00 | METOP-C | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3b23ddee-fdba-35c8-b9ea-7f720c235c67 | -8.7688 | -48.678501 | 2026-09-19 00:41:00 | METOP-C | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 74468f25-3cc1-3276-9766-be1dcff60269 | -6.9502 | -46.974098 | 2026-09-19 00:41:00 | METOP-C | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 638d2ac9-c2d3-347b-b30a-20981e4ca82f | -5.5132 | -43.7906 | 2026-09-19 00:41:00 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ec989e96-fc28-3a38-b953-d16a9dd2c5e5 | -12.5414 | -47.089401 | 2026-09-19 00:41:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6e472038-f472-3a10-b0ce-afcba4747f1c | -8.4495 | -45.711102 | 2026-09-19 00:41:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 54ce2d96-3241-3995-bef1-e5f3e31e01b4 | -13.615 | -48.3246 | 2026-09-19 00:41:00 | METOP-C | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| b563d739-b213-3deb-ab39-dc5811730de7 | -11.9351 | -50.124802 | 2026-09-19 00:41:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6e90e98c-d664-3b01-9271-b0fd771184eb | -3.1515 | -53.931702 | 2026-09-19 00:41:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a6f87075-0a83-393b-946f-8aad2a69da99 | -3.0337 | -51.375801 | 2026-09-19 00:41:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cf3acae5-4298-3d07-baf7-31858bc127ee | -0.2676 | -48.407501 | 2026-09-19 00:41:00 | METOP-C | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 92f0768e-26af-37ee-9ec7-7df2f344b70d | 1.2301 | -50.997501 | 2026-09-19 00:41:00 | METOP-C | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| ba60bf77-1dfc-3f74-8bd8-5ee5bf7d3fda | -9.6112 | -45.382401 | 2026-09-19 00:41:00 | METOP-C | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 812ebb4e-6dbc-3a2e-bfae-2e41ffd02d8e | -4.2604 | -48.544201 | 2026-09-19 00:41:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 555db79c-4ac0-33ad-bac2-dfa252e8be9d | -10.8646 | -56.195202 | 2026-09-19 00:41:00 | METOP-C | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bb28f1ea-6d79-3439-8d9c-767ccc0644b9 | -9.9149 | -46.582001 | 2026-09-19 00:41:00 | METOP-C | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 420451df-25ea-3b9c-8561-da62e9a922de | -8.1263 | -44.831402 | 2026-09-19 00:41:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| de7c2cc0-aa0b-37e3-a76e-953c059bd8ad | -6.4901 | -43.8223 | 2026-09-19 00:41:00 | METOP-C | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3b2ae994-e286-3566-91ea-f6ae40085f99 | -2.8345 | -50.460602 | 2026-09-19 00:41:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7748f7ea-c774-3359-a264-5069ee9d90d0 | -11.1266 | -45.279499 | 2026-09-19 00:41:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 277942d9-6030-326f-abd6-383cea8fe496 | -8.7672 | -48.6716 | 2026-09-19 00:41:00 | METOP-C | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 368450e1-6925-308a-a5a0-2bd2d7e58f6c | -4.5963 | -42.976601 | 2026-09-19 00:41:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7724088c-01ef-37c0-9fb4-9ad178212648 | -12.1188 | -47.002102 | 2026-09-19 00:41:00 | METOP-C | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 79429764-003f-3865-81b2-c767dac21ff9 | -7.6876 | -46.113899 | 2026-09-19 00:41:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| aea3ce9d-dbea-3f48-b680-4bca703980ba | -3.3665 | -50.4422 | 2026-09-19 00:41:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 408ec651-d57a-3409-aa16-d65e16483110 | -21.0247 | -48.239601 | 2026-09-19 00:41:00 | METOP-C | PITANGUEIRAS | SÃO PAULO | Brasil | 3539509 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| e3314832-f14b-3aba-ad0d-b4bbf547a7df | -12.1498 | -47.0023 | 2026-09-19 00:41:00 | METOP-C | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2a8227bf-8583-3d4d-86e0-0f889715dfd1 | -5.295 | -50.082802 | 2026-09-19 00:41:00 | METOP-C | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 24f28717-311b-39ab-8319-ec7fce39d50a | -6.581 | -44.157101 | 2026-09-19 00:41:00 | METOP-C | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 01ddfdc8-4479-376d-b0e4-6cede216ff51 | -13.2349 | -46.918701 | 2026-09-19 00:41:00 | METOP-C | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 8eff4e27-9b2d-3f03-94c1-c3be354cb96a | -4.5042 | -54.971001 | 2026-09-19 00:41:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c200ce60-913f-3f3d-81d8-efbe349aba5e | -8.4905 | -57.615299 | 2026-09-19 00:41:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 036c4504-d92a-36b1-bc04-8445f41b3ea0 | -13.6818 | -48.578098 | 2026-09-19 00:41:00 | METOP-C | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 1201ac9a-2a02-32a0-8e57-fe660d13159f | -6.0268 | -51.7658 | 2026-09-19 00:41:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ae24717d-b1f3-3616-aa9f-5d03e83818a9 | -4.5897 | -42.949402 | 2026-09-19 00:41:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0e58c0d8-8b9d-30a7-a69d-3d132bcca55a | -3.549 | -50.293701 | 2026-09-19 00:41:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e0235138-104c-3294-bc77-49a6962f6c07 | -8.3705 | -47.220501 | 2026-09-19 00:41:00 | METOP-C | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 002181b8-d5bc-3e8f-a179-464f308d68ab | -11.0643 | -49.7668 | 2026-09-19 00:41:00 | METOP-C | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ca2640b0-bd10-3d0a-ac5b-4f9cf65f88af | -9.9454 | -45.2672 | 2026-09-19 00:41:00 | METOP-C | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| c4268eaa-eea7-3e4b-8923-71bc0666babd | -13.2333 | -46.911598 | 2026-09-19 00:41:00 | METOP-C | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 1b16e22a-de7f-3665-8736-b19b845d6bda | -6.649 | -50.917702 | 2026-09-19 00:41:00 | METOP-C | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f2ae3f47-4ea2-3bc3-a9b8-e0109b08f4ce | -7.6955 | -46.1036 | 2026-09-19 00:41:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c2f444fd-ddf5-36ae-a5e8-6281f38ed6f6 | -10.8338 | -50.165199 | 2026-09-19 00:41:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| acbc4d92-8e6a-36c6-a502-7f02318714c3 | -10.8354 | -50.1726 | 2026-09-19 00:41:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0ede4976-6417-3bff-95b2-4fc56500b9ba | -9.9474 | -45.2756 | 2026-09-19 00:41:00 | METOP-C | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 693ce05e-4d82-3531-81df-927690e772be | -11.493 | -50.733501 | 2026-09-19 00:41:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 40843d32-fb96-32e8-9680-12886441ce42 | -10.5275 | -44.8484 | 2026-09-19 00:41:00 | METOP-C | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 4d133901-7d98-3f65-814d-467e38ea966d | -13.6315 | -48.306 | 2026-09-19 00:41:00 | METOP-C | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 6cb65fb3-47d7-3a86-908a-dca0e071ade0 | -8.9998 | -44.985199 | 2026-09-19 00:41:00 | METOP-C | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| b4e0297e-5358-3d7e-8499-dc3fa3aa51b1 | -4.0615 | -56.248402 | 2026-09-19 00:41:00 | METOP-C | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fc6e01a6-47e4-30db-a48d-e81e903ee756 | -9.9281 | -46.594501 | 2026-09-19 00:41:00 | METOP-C | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| aefb4bae-11d3-3ea4-b725-d004dc0d9f8d | -13.6003 | -46.936901 | 2026-09-19 00:41:00 | METOP-C | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 575437a8-bd6e-31f2-b02e-b02e9c186e24 | -13.6201 | -48.301102 | 2026-09-19 00:41:00 | METOP-C | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README21.md)
