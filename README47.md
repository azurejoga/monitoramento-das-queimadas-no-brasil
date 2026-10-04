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

## Dados Diários - Página 47

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6462489f-48f5-30c0-aa42-6b9ddb5e1c25 | -11.81499 | -43.54145 | 2026-10-04 04:57:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7cba539e-6879-3f74-8913-f8819a614e1e | -8.34657 | -62.83382 | 2026-10-04 04:57:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ff30b50e-86b2-39a2-8ebc-0f4ede304d3f | -5.6323 | -50.02949 | 2026-10-04 04:57:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 731671be-12e2-3ec0-bca0-5bfae12d8d55 | -4.81577 | -49.86964 | 2026-10-04 04:57:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 03a4b663-f812-322d-88b9-ddedb63b58e3 | -4.20227 | -53.46465 | 2026-10-04 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b2f98931-1e7a-393d-adce-4b18e10899ef | -3.87116 | -55.80814 | 2026-10-04 04:57:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 29.9 |
| 4b8f45fd-a547-3bc8-bd13-1a615197eaa5 | -6.89663 | -43.68323 | 2026-10-04 04:57:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 817ecb85-9a2d-3256-a701-43f1b2f5b8f8 | -4.21013 | -53.46172 | 2026-10-04 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5b13f5c1-7ba9-3e60-92c6-0e258ab342fd | -9.09395 | -61.16183 | 2026-10-04 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e8e6cdc2-2a89-3ae6-9bba-c8d43a8cbc8f | -4.81745 | -49.88068 | 2026-10-04 04:57:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0af4639d-cfb2-3e61-bada-50b5380655a5 | -8.70972 | -61.39685 | 2026-10-04 04:57:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 559d58ab-d929-3066-b5c9-fd38c8574957 | -5.5853 | -49.01622 | 2026-10-04 04:57:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e80f807d-7e52-3173-b605-986b78d16599 | -9.24943 | -60.33312 | 2026-10-04 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 7dc469bc-df3a-349e-a949-14c0e6ce68cd | -9.48104 | -64.69197 | 2026-10-04 04:57:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 60a1c8da-8ee3-3dea-8378-deb7c652c58a | -6.07344 | -53.47406 | 2026-10-04 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 67c8071f-4211-3218-8dcb-5b153aeb39f6 | -5.85088 | -53.46747 | 2026-10-04 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| adb138b0-e70c-3ee2-9ccb-41423c44706d | -6.023 | -53.53853 | 2026-10-04 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5b33af80-88bf-3283-8977-a8adf27ff0da | -6.38656 | -49.8098 | 2026-10-04 04:57:00 | NPP-375D | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 869593bc-0f9a-36fe-8602-33d9d81601b6 | -4.81687 | -54.73246 | 2026-10-04 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2c83bc0c-4e87-3744-87fa-ac30f58cc2a7 | -5.99812 | -53.64566 | 2026-10-04 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1685205b-d229-3ba6-9c57-2dad6c7cc77c | -4.1169 | -54.41388 | 2026-10-04 04:57:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1f73c993-99fd-3212-bd23-eaeb448f9b2b | -10.25212 | -49.66268 | 2026-10-04 04:57:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5d5e79c6-dc5b-372a-a528-46261c9b09f9 | -6.2128 | -52.80045 | 2026-10-04 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0cc5039d-81fa-319c-8c0f-0bb0e461af41 | -9.46197 | -64.33255 | 2026-10-04 04:57:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 177f2819-f5ec-3e6f-9a2b-47a5cabb2a21 | -11.81581 | -43.53499 | 2026-10-04 04:57:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ad52499d-fe4e-314a-88af-5bdc86c19044 | -6.43841 | -52.70737 | 2026-10-04 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 80f5153c-c810-3a99-8b92-7cdbaf161788 | -6.00012 | -53.52288 | 2026-10-04 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| cf677187-c470-3e5b-bbb3-ba70acba9ded | -3.73246 | -57.14909 | 2026-10-04 04:57:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5e3f147e-5dc4-37c3-8b10-48d053d6bd6c | -10.60133 | -53.97091 | 2026-10-04 04:57:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 18009f46-a18d-31d3-bca1-187dd1b8985c | -7.28156 | -50.44236 | 2026-10-04 04:57:00 | NPP-375D | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6d3ddb93-005f-3fd8-9c13-475b96e9abb1 | -6.07761 | -53.47068 | 2026-10-04 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 2948c08a-205e-306f-8b51-30a8602fee8b | -6.57338 | -44.15004 | 2026-10-04 04:57:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 0a9b9e22-7e1f-3f38-a6fe-49a05c3dd356 | -4.46844 | -54.97214 | 2026-10-04 04:57:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 01bbefd7-c850-3142-95c2-2244d77a3ecb | -4.81521 | -49.87316 | 2026-10-04 04:57:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ac4a0ad4-1d98-39ee-8897-5eb64afe3bae | -9.08303 | -61.15975 | 2026-10-04 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c203cea8-0b72-379f-b982-1052b9370697 | -6.20532 | -52.80305 | 2026-10-04 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b22b5d1a-d43c-36de-8093-d6e6e18758b4 | -3.78653 | -59.37972 | 2026-10-04 04:57:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 64ae57da-1bdb-395d-87de-6ba076842c17 | -5.80579 | -50.1283 | 2026-10-04 04:57:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0ad2ba58-000c-3194-bf89-bb649cb36fd8 | -4.45168 | -54.90488 | 2026-10-04 04:57:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6a9fa6e0-0853-3459-b69f-ebb0fd0510a6 | -9.79498 | -60.14053 | 2026-10-04 04:57:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9bf34605-df26-3522-98d5-27649a426857 | -5.86264 | -55.71043 | 2026-10-04 04:57:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 48bcea99-b324-3a44-83be-a6fcc970149e | -10.22405 | -59.08942 | 2026-10-04 04:57:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e00d0e62-cd99-31a7-ac5a-d13d2e28b3b1 | -7.87835 | -61.43287 | 2026-10-04 04:57:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 043e315f-3767-32ab-9bc1-322ad5e4b406 | -7.75242 | -49.20285 | 2026-10-04 04:57:00 | NPP-375D | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2347dec8-61e0-3719-bd50-87bfee35bb0a | -4.54184 | -55.97795 | 2026-10-04 04:57:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f24b8aef-cf9b-3934-9cfa-2b6b7932ef7c | -5.99657 | -53.63289 | 2026-10-04 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 65913f88-f477-3ede-92a0-b1dcecc57970 | -4.81856 | -49.87366 | 2026-10-04 04:57:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 57bce950-0807-38c5-a8b1-a019d343ceae | -6.2342 | -53.14837 | 2026-10-04 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1cbd7e08-1463-3429-9493-3b3f633ac2c0 | -6.20638 | -52.80393 | 2026-10-04 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3c253def-9f27-3f42-819e-398c987f82bd | -5.77978 | -50.20663 | 2026-10-04 04:57:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9ba8db12-1e12-3ab1-98c7-bd495bd0f527 | -5.41667 | -51.11065 | 2026-10-04 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d5a4f52a-13d7-325c-811e-03e86109d837 | -4.8219 | -49.87418 | 2026-10-04 04:57:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cb210e9e-de20-3306-bec6-3465260160d7 | -9.7021 | -57.44917 | 2026-10-04 04:57:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c9ba291f-a68a-3347-9ce7-65e03fa620e2 | -4.31828 | -55.62481 | 2026-10-04 04:57:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4c71be47-2109-3f75-ac14-b4d374526c2c | -5.9959 | -53.63695 | 2026-10-04 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e87de0da-62c6-3994-a9ac-bb7cf90d1dd4 | -6.0622 | -53.4763 | 2026-10-04 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a334f038-34a2-3492-8d1a-1d9bf25c5f57 | -6.57225 | -44.15672 | 2026-10-04 04:57:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 40365f45-237c-3749-a588-9d00f9215b32 | -5.79232 | -48.82675 | 2026-10-04 04:57:00 | NPP-375D | SÃO DOMINGOS DO ARAGUAIA | PARÁ | Brasil | 1507151 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8981f8d3-a1b5-3d9c-ac0b-0ee7de2ed4a9 | -8.71457 | -61.40171 | 2026-10-04 04:57:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| abb9ad10-2c26-31d7-8149-cebb7a76e349 | -6.61267 | -41.55624 | 2026-10-04 04:57:00 | NPP-375D | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 7f08ea5e-a081-3d59-abc7-a58e94b3dcde | -9.10382 | -49.7815 | 2026-10-04 04:57:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 97d9b446-4a75-37d7-803a-1e5ecd1d2116 | -4.54662 | -55.97492 | 2026-10-04 04:57:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 54594d8d-8a83-33f0-be12-f119a3f4d7c3 | -6.57291 | -44.15203 | 2026-10-04 04:57:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 388bcc1a-3a80-32b8-9a15-70ec371ba8ad | -6.06574 | -53.47686 | 2026-10-04 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 27987a54-061a-3a70-94ad-7f87777b2e2a | -9.12689 | -65.46511 | 2026-10-04 04:57:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dc971faa-87c0-3e3a-9012-24e68687390e | -8.35189 | -62.8312 | 2026-10-04 04:57:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a449b31c-b712-3e97-9361-cac26273bc6e | -4.82175 | -49.28318 | 2026-10-04 04:57:00 | NPP-375D | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c9de915a-4387-3cad-a668-8aa3d58020d8 | -6.28339 | -45.85012 | 2026-10-04 04:57:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 98e766cd-a935-3541-b53f-9053d380a633 | -9.13136 | -65.46457 | 2026-10-04 04:57:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2d1f9b9c-ab1f-38bb-b7e6-9710025dd903 | -4.42938 | -55.74996 | 2026-10-04 04:57:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 132c6d5a-6ad8-37d2-8483-7e6c763bf537 | -6.50468 | -51.05574 | 2026-10-04 04:57:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cb59a066-8e78-34d8-afc3-3635764a764f | -8.34569 | -62.8386 | 2026-10-04 04:57:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d776c96f-5b6d-3cbb-add5-d80b2c7e4327 | -11.8154 | -43.53821 | 2026-10-04 04:57:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 57312859-0bc3-3fb8-9f95-8fe559610e3d | -8.34745 | -62.82907 | 2026-10-04 04:57:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d843e586-4fa3-3e2a-a9fb-bfa3afffaa7c | -6.20998 | -52.79614 | 2026-10-04 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eb2587bb-c46d-31dd-83e6-535a3d94b508 | -9.79047 | -60.13665 | 2026-10-04 04:57:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5f6492a3-7ab7-3a1c-a10a-abfd31b2a8c8 | -6.61316 | -41.55266 | 2026-10-04 04:57:00 | NPP-375D | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| bc31edc6-f856-34cc-b04c-54f28bb01af9 | -12.35235 | -48.03941 | 2026-10-04 04:57:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a844a0dd-9e6b-34f2-9a4d-1a41acbbe759 | -9.08298 | -61.15878 | 2026-10-04 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 77e0b1c3-c887-3937-93b0-929ed9dd6fd5 | -9.08844 | -61.15984 | 2026-10-04 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0ff8d6ce-45b8-3b6c-b240-ceebdd46c0fd | -5.54936 | -45.26826 | 2026-10-04 04:57:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 62494834-64d8-37f6-9437-1b27869f15ee | -5.89302 | -57.67237 | 2026-10-04 04:57:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1c904085-d650-3fd3-9c69-2e486b1d6899 | -6.00721 | -53.52399 | 2026-10-04 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6be7c1b4-11b9-3b07-8b76-924f931a5f0d | -6.07634 | -53.47853 | 2026-10-04 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 389104bf-162a-3b64-8358-1706a9937383 | -5.85507 | -53.46402 | 2026-10-04 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 647d3bf6-28ca-34e3-a077-daa456bb233c | -9.13396 | -65.46653 | 2026-10-04 04:57:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ae281b7a-5999-3188-bde0-5af458268599 | -3.79183 | -59.38065 | 2026-10-04 04:57:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6cb4e37e-8755-3170-991d-15af793f6d24 | -4.20586 | -53.46524 | 2026-10-04 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ea94e5eb-afdf-3cb7-8d0b-2c0446f6b164 | -3.90926 | -55.88749 | 2026-10-04 04:57:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f6c6852a-78e5-3415-8276-ffa29951e059 | -9.01858 | -65.69719 | 2026-10-04 04:57:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| f813b32c-8f68-3e5c-8c65-5b7b6cf4411e | -9.55959 | -62.03733 | 2026-10-04 04:57:00 | NPP-375D | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| eb240f97-9e41-3b41-bee6-af3120b94065 | -10.60196 | -53.96712 | 2026-10-04 04:57:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 87c641dd-0f70-3ded-8d2b-3a4f65363007 | -4.81325 | -49.28906 | 2026-10-04 04:57:00 | NPP-375D | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 05eac70a-3eb6-3df2-9ba8-dbef54619f85 | -3.87179 | -55.80442 | 2026-10-04 04:57:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 29.9 |
| 12fb44a9-1009-3b64-8fc5-98b1476efa2e | -4.2072 | -53.45704 | 2026-10-04 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b578e63c-e0be-3866-b52a-b4b367b9e3ea | -4.818 | -49.87718 | 2026-10-04 04:57:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bf4e1642-a6a3-3c37-8b0f-3a0190cf0272 | -5.74269 | -45.15114 | 2026-10-04 04:57:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| eb74dade-6171-3b13-9f54-105636807510 | -10.24635 | -49.65392 | 2026-10-04 04:57:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9eb24e9a-82d5-30ee-8bc8-bb9ae46a06ab | -8.35098 | -62.83594 | 2026-10-04 04:57:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 00c60aa5-ea81-36f5-909f-912236084f97 | -6.07698 | -53.47461 | 2026-10-04 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |


[Clique aqui para ver as próximas entradas](README48.md)
