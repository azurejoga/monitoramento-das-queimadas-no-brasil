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

## Dados Diários - Página 126

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d4d66c67-8e2b-3388-9d5d-6fef5f715437 | -7.3289 | -55.2155 | 2026-09-20 14:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 9e2f8b2b-caad-31d6-b87e-1e128087b6e4 | -11.0802 | -54.0302 | 2026-09-20 14:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 185.1 |
| 7d8374b5-e4e5-33f2-b207-34b726a2d3b3 | -8.2315 | -61.3541 | 2026-09-20 14:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 100.1 |
| 5529c0b7-2775-3d3e-b54c-ebdd22403fb8 | -10.4547 | -51.2405 | 2026-09-20 14:20:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 79.4 |
| 14241765-91f6-37fb-af3a-8003b97a5f43 | -8.1376 | -46.8155 | 2026-09-20 14:20:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 121.3 |
| 239bcf8a-747c-3a79-a879-34cb4747b87c | -12.0263 | -50.0447 | 2026-09-20 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 87.7 |
| 05739ee5-9515-36b1-8426-7c7d1c53b6c2 | -6.4485 | -59.9909 | 2026-09-20 14:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 177.9 |
| 91c3f31d-5c1c-3204-9fed-201f48a64202 | -9.8313 | -48.4073 | 2026-09-20 14:20:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 121.0 |
| 7d2d0acd-4134-3ed8-bb10-e9ad577c1556 | -12.8893 | -51.0124 | 2026-09-20 14:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 358.5 |
| e395462f-a965-3989-a8f0-fbedda4a19b2 | -8.754 | -44.2589 | 2026-09-20 14:20:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 87.3 |
| bd003f70-242a-3d9e-986d-eec814449e46 | -9.0355 | -48.7487 | 2026-09-20 14:20:00 | GOES-19 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 78.3 |
| fb839cea-961a-3207-a6bd-2140ca9c090d | -6.4486 | -59.9717 | 2026-09-20 14:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 271.3 |
| 7a637e69-066f-3d92-8bec-8206918a019a | -2.7826 | -59.896 | 2026-09-20 14:20:00 | GOES-19 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 68.7 |
| ceaa00ac-e6dd-32c1-ae53-ad5d3a39ee6d | -7.3564 | -44.4726 | 2026-09-20 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 90.8 |
| 82114c11-f525-3b6c-8b8c-a442b3123444 | -10.8028 | -50.6326 | 2026-09-20 14:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 134.3 |
| 3654c017-eac0-3385-a36e-0dbc4a85f736 | -9.2865 | -48.2453 | 2026-09-20 14:20:00 | GOES-19 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 79.7 |
| a55f3e58-fac7-37c8-ab44-c9bceac00d9a | -3.331 | -59.8292 | 2026-09-20 14:20:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 56.8 |
| dcaed8cf-05e2-32ac-a886-3c4186c66a47 | -8.4756 | -46.8498 | 2026-09-20 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 75.7 |
| aae71115-7fea-303f-b0f3-edfbb3953239 | -10.7463 | -50.6172 | 2026-09-20 14:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 117.1 |
| 6c6ebe3d-ab44-3680-9162-702e4e4249a3 | -12.5227 | -50.0267 | 2026-09-20 14:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 162.5 |
| 170a94dc-bedb-3da1-97c3-6283e79619d0 | -11.4905 | -47.7736 | 2026-09-20 14:20:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 80.8 |
| fd55d619-e389-3571-a5d3-32395a6c0175 | -7.9637 | -44.0667 | 2026-09-20 14:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 9e5eb2d0-36ac-3f7d-84a6-a083219da7a1 | -8.1686 | -54.7634 | 2026-09-20 14:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 114.8 |
| 57991e72-cc0a-3402-a3d5-c7ea591c8c8c | -6.4302 | -59.9724 | 2026-09-20 14:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 1d6776e0-63b1-3b38-be89-a365450debae | -10.9665 | -49.7583 | 2026-09-20 14:20:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 104.4 |
| b2190cc5-de70-3dee-9d08-16ed939eec78 | -9.2567 | -46.2098 | 2026-09-20 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 936a6ff9-19d1-38ab-bb83-442986a2cd0e | -11.0509 | -54.9106 | 2026-09-20 14:20:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 733.2 |
| 7b5158e2-8737-3495-b15b-c99f45724ecf | -11.9493 | -50.0971 | 2026-09-20 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 364c7a7f-9b13-3243-8a3c-552c6c7b8b91 | -6.1359 | -59.9446 | 2026-09-20 14:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 83.9 |
| 8223c6f5-84de-3ef9-ae33-2e48c32139ae | -15.866 | -49.9177 | 2026-09-20 14:20:00 | GOES-19 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 72.6 |
| e70675b0-286b-3d51-81a9-31fdbd0286e5 | -8.481 | -44.9102 | 2026-09-20 14:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 8cacc5bd-0e9c-3d8a-b359-5a3af7e2ae91 | -10.7652 | -50.6153 | 2026-09-20 14:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 102.9 |
| aa3ecc48-286d-3c5d-8db8-9539e3711a35 | -11.4345 | -45.3919 | 2026-09-20 14:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 149.1 |
| c10a0205-ac01-3069-bd34-770117a00d32 | -12.2847 | -47.1094 | 2026-09-20 14:20:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 7fcde5f6-6b4b-3a1a-bc24-31998d510d64 | -11.0407 | -54.1772 | 2026-09-20 14:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 91.3 |
| 5e1409aa-6d60-3ab0-817b-05ea03125b0d | -6.9851 | -45.8235 | 2026-09-20 14:20:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 59.4 |
| 0e6b5a83-1d2f-39da-9ee3-3592838f0ce6 | -7.5703 | -57.6962 | 2026-09-20 14:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 2e51972d-8333-3d3e-a15a-f40710c01af1 | -8.6628 | -45.4379 | 2026-09-20 14:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 8a8c005a-f4b2-3d4d-820c-5fa4fd37db60 | -7.5704 | -57.6766 | 2026-09-20 14:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 98.1 |
| 0aedc2ee-5f7a-3008-921f-8406ab1a432b | -14.6661 | -46.6919 | 2026-09-20 14:20:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 59.4 |
| a8a560d4-c9d3-3121-92a2-c6cb48277bb8 | -11.1369 | -54.0251 | 2026-09-20 14:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 85.2 |
| e97c3ba5-14fc-36e0-8ae5-4737a4a06227 | -10.7466 | -50.5959 | 2026-09-20 14:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 83.5 |
| e17ee48a-0eb4-36c1-854e-aa2d15cae9c7 | -12.2341 | -50.1703 | 2026-09-20 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 289.1 |
| 21dc6ea0-74eb-3e87-8f0b-2f4b0e6fcd06 | -3.3454 | -42.7597 | 2026-09-20 14:20:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 139.5 |
| 61923df2-9d98-35e6-8f01-dcee6b700df2 | -3.364 | -42.7824 | 2026-09-20 14:20:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 83.4 |
| f2c7ef07-5f56-3364-979b-317853aeb43a | -8.4549 | -47.0072 | 2026-09-20 14:20:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 9abdc817-001e-3bff-916d-c59bc2b11efe | -10.8364 | -50.9479 | 2026-09-20 14:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 248.1 |
| 71701e8d-39ac-3892-9cb7-f45ebfd764b5 | -2.8974 | -57.8181 | 2026-09-20 14:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 84.9 |
| bbba7c2b-9214-3849-94a2-e0ce2fbc082a | -7.1392 | -42.0811 | 2026-09-20 14:20:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 109.2 |
| 07dd8e3d-91f6-31b4-a914-4ef77890a188 | -3.3138 | -59.4472 | 2026-09-20 14:20:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 1d7a45f3-0437-3d84-b0c4-78a64212ca73 | -2.9143 | -58.3401 | 2026-09-20 14:20:00 | GOES-19 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 89.3 |
| 6d3d31a8-2973-3804-a103-db592eeaf0a8 | -4.0759 | -52.1259 | 2026-09-20 14:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 119.8 |
| c349b4f6-0902-31b6-b249-e75d2a31af48 | -10.8177 | -50.9286 | 2026-09-20 14:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 104.7 |
| 74aa5647-a52f-34ae-ba13-4be7e1527f6e | -6.9225 | -42.9088 | 2026-09-20 14:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 110.0 |
| 24e81c24-0593-342b-b3c7-15a31e1d9fc4 | -16.5984 | -45.3298 | 2026-09-20 14:20:00 | GOES-19 | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 96.5 |
| 6c56038a-3f60-35f6-8f4c-1fe54c36cad9 | -6.2949 | -41.7785 | 2026-09-20 14:20:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 70.4 |
| 4e8e78c7-bc32-3182-a8e4-796a83145902 | -2.8009 | -59.8957 | 2026-09-20 14:20:00 | GOES-19 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 2d0a6b96-9a21-31a8-b66f-acc8bd54c035 | -3.7856 | -60.7335 | 2026-09-20 14:20:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 7aa8dd53-208a-3d01-aa59-a82d97935277 | -5.8088 | -55.7095 | 2026-09-20 14:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 87.8 |
| 53bb4bba-60e4-374e-b967-583c7d6a5ea6 | -12.1524 | -47.0158 | 2026-09-20 14:20:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 87.6 |
| ba634a84-0897-36ff-bcd6-e6bf04196dc2 | -9.7154 | -45.8644 | 2026-09-20 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 555ddfa5-03c2-30c6-84e3-142dd1440d0a | -9.0541 | -48.7686 | 2026-09-20 14:20:00 | GOES-19 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Amazônia | 403.0 |
| 58949e3e-01e6-3d5a-aabf-b7d469aef0d1 | -11.9543 | -49.7728 | 2026-09-20 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 9f078332-f06f-314d-ab04-61a5f1ff7f8f | -10.473 | -51.2808 | 2026-09-20 14:20:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 161.3 |
| 35d15df8-ee64-3c41-978e-3a263806ab8f | -8.3963 | -47.1899 | 2026-09-20 14:20:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 59.3 |
| 24a90789-5a0d-356f-8344-74f87b80fd7f | -13.5907 | -51.4794 | 2026-09-20 14:20:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 194.6 |
| 2a8d9a98-bbad-331e-ab30-782187a50fd7 | -3.3493 | -59.8288 | 2026-09-20 14:20:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 6348ed4f-e024-3bd1-9aa0-66ab4b420564 | -6.7406 | -44.0909 | 2026-09-20 14:20:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 72.7 |
| a7980eb4-0f09-353c-9068-2f9e2e9855a6 | -5.9335 | -59.9515 | 2026-09-20 14:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 102.8 |
| aa256913-e647-301e-b332-e0c7d15b98c9 | -8.4611 | -57.6292 | 2026-09-20 14:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 5f52f430-277f-311b-a537-a5ca384eec34 | -12.5224 | -50.0484 | 2026-09-20 14:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 254.5 |
| 3f8fb41d-de3c-3b09-a09d-ac42a0bee764 | -11.6431 | -50.2191 | 2026-09-20 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 99.9 |
| d0954ad8-24ef-3c7a-bda6-ad092182e7ea | -8.4734 | -47.0275 | 2026-09-20 14:20:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 2fdf97d7-2d11-3bea-bfb9-42efd888bd4c | -11.4537 | -45.3892 | 2026-09-20 14:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 122.2 |
| 26397ea9-1f90-3af8-a689-f9947a61e346 | -8.2314 | -61.3732 | 2026-09-20 14:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 146.7 |
| 841e7dfa-e941-357b-b33c-7f332c0bb37b | -11.9681 | -50.1164 | 2026-09-20 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 92.3 |
| 80313a63-18ce-39a8-a9e7-1a5fdf683b25 | -3.2955 | -59.4476 | 2026-09-20 14:20:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 63.0 |
| b2a7f7a9-bcaa-3db8-bc9f-5adc7cc61439 | -6.7184 | -55.0884 | 2026-09-20 14:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 106.2 |
| 3cda636b-08bb-34d2-a175-9661c741d657 | -9.0353 | -48.7704 | 2026-09-20 14:20:00 | GOES-19 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Amazônia | 100.9 |
| 420e69b0-b5ef-3aa6-997e-1a0ac0dec584 | -12.1715 | -47.0131 | 2026-09-20 14:20:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 87.1 |
| 2d854d40-82e4-33ea-a85c-3b7ef813ae73 | -8.9752 | -44.6722 | 2026-09-20 14:20:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 77.6 |
| b4575e9a-6686-3092-b541-6fd89f52ccd7 | -12.3209 | -50.718 | 2026-09-20 14:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 069cfb4d-a485-31a5-9c42-18d004795c40 | -11.118 | -54.0268 | 2026-09-20 14:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 229.6 |
| 7bc1214a-0663-3f2d-8c27-c212d756f037 | -10.6703 | -50.6465 | 2026-09-20 14:20:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 126.3 |
| 9ff017bd-066e-395a-8d26-ecac3a987b4a | -11.6621 | -50.2169 | 2026-09-20 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 165.2 |
| 006039cb-3506-3da9-9019-252e31ca8c58 | -7.156 | -47.4312 | 2026-09-20 14:20:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 10f96e66-d9a2-3fc6-ace9-01b33a17c009 | -15.4174 | -53.0236 | 2026-09-20 14:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 211.1 |
| a8a8dc07-a9e2-3b88-8b51-439fdb34c64f | -9.0544 | -48.7469 | 2026-09-20 14:20:00 | GOES-19 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 206.0 |
| eab94a7e-76f5-383d-8c23-36cddc19f743 | -14.061 | -52.1 | 2026-09-20 14:20:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 102.3 |
| e400e2db-342b-37c0-b632-ea477c3ab13d | -11.1372 | -54.0045 | 2026-09-20 14:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 100.7 |
| 0f852617-526e-3f54-82a2-b08b15fd3c41 | -12.398 | -50.6659 | 2026-09-20 14:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 6e9e4114-3e3d-362d-8765-b8e111c4f602 | -8.2499 | -61.3724 | 2026-09-20 14:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 155.1 |
| 4b829200-9d62-3d4f-91d5-1aa223e408bc | -8.0279 | -61.3626 | 2026-09-20 14:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 63.0 |
| ee12450a-a8c3-3952-bafb-aba2aade673b | -14.6861 | -46.6657 | 2026-09-20 14:20:00 | GOES-19 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 90.7 |
| b9f3d3e1-cc37-3fe7-88c0-2b55d950bcdd | -8.5803 | -44.5322 | 2026-09-20 14:20:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 82.1 |
| a219ddd8-4dda-3d06-b3d5-a1f37df79ed4 | -11.6624 | -50.1954 | 2026-09-20 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 168.0 |
| 1bdf239b-2daa-3517-bf5a-0d9501a76f7e | -9.84 | -46.4136 | 2026-09-20 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 166.3 |
| 9485f544-7fdc-3329-a485-86d3fd0df558 | -7.7439 | -46.7629 | 2026-09-20 14:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 69.8 |
| c9ab5597-6015-3830-8fd4-0f17b6db2ef9 | -11.398 | -51.418 | 2026-09-20 14:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 101.5 |
| 63c8f853-56a3-3492-9ec3-b96074619780 | -10.8553 | -50.9459 | 2026-09-20 14:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 137.7 |


[Clique aqui para ver as próximas entradas](README127.md)
