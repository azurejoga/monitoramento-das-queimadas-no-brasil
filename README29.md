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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 51f23ca1-6d06-361d-aafd-a2ec2a54e58d | -6.13492 | -57.68361 | 2026-09-04 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6ef870fb-240e-3572-b8f3-a999b0540b70 | -17.09399 | -56.86274 | 2026-09-04 05:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| b794e8a5-2453-3a16-9048-809801911e6b | -3.21929 | -61.17661 | 2026-09-04 05:25:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 8820560c-6462-364f-8d35-530e4275d530 | -9.03548 | -65.73716 | 2026-09-04 05:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d6f8fd51-f7e1-3faa-adba-c8728717272c | -5.32686 | -60.13964 | 2026-09-04 05:25:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 315f3564-7124-39bc-b53d-42cfadfbdc3a | -10.45528 | -61.2053 | 2026-09-04 05:25:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ca9ad2ed-7873-32fe-abcb-50b071ba32bc | -15.42339 | -48.88164 | 2026-09-04 05:25:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 7a96f85c-9382-3a17-b45d-187ce05bfa06 | -4.47259 | -55.42744 | 2026-09-04 05:25:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eb8464da-3734-3ded-98d8-24b366401715 | -12.08296 | -64.23424 | 2026-09-04 05:25:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 11ebf7dc-a5d2-3265-a52b-96df1c5ffbbf | -6.13369 | -57.6918 | 2026-09-04 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 27f36549-5c09-3273-9d39-54e778c05dc8 | -5.17269 | -60.27819 | 2026-09-04 05:25:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4a44325b-2efa-330a-aff7-ecc7a2070e86 | -3.61737 | -60.56689 | 2026-09-04 05:25:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 59bd732c-b970-319a-923f-1256602bbe91 | -6.15591 | -57.76147 | 2026-09-04 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b10f5318-f0f7-3719-a630-2e8aafc7b98f | -3.75763 | -61.75242 | 2026-09-04 05:25:00 | NOAA-21 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 95076ebd-a983-3b44-b559-19b38f71ee3d | -4.19723 | -59.94526 | 2026-09-04 05:25:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c4ed59c5-dfa9-34a8-a2fa-22381ef7b4cd | -7.89082 | -71.73865 | 2026-09-04 05:25:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 754994fe-9ecb-3879-a1cf-ec13fa7c6f82 | -17.10178 | -56.84864 | 2026-09-04 05:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 31399dde-8e78-3e33-b424-cb89355c2269 | -5.17822 | -60.28612 | 2026-09-04 05:25:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1c560392-419a-3f15-ad68-1f66252d7207 | -9.66547 | -67.3987 | 2026-09-04 05:25:00 | NOAA-21 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0dd8a9b6-8508-315a-92f9-de97a7a66795 | -8.87436 | -68.61501 | 2026-09-04 05:25:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 12e70d27-b453-32ab-a004-fa957878f995 | -9.11707 | -65.49744 | 2026-09-04 05:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 19e63f59-79b5-3aa7-879f-d8c493088ee3 | -18.13441 | -51.80298 | 2026-09-04 05:25:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1c5fc7d8-7cd6-3b71-a44c-f348c7e9febd | -4.81229 | -62.78554 | 2026-09-04 05:25:00 | NOAA-21 | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7a975cd1-75d9-35a6-acb7-fe45e781ade3 | -9.04696 | -65.74746 | 2026-09-04 05:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ec9e753f-86fd-3395-9a7b-83bf65104ecb | -6.31539 | -56.04241 | 2026-09-04 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a31c8f03-ff7c-3021-9fc6-3691b15e2a0c | -4.62743 | -55.73554 | 2026-09-04 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d265e046-e04d-3687-bc13-d987f252fa6b | -4.70573 | -55.97133 | 2026-09-04 05:25:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9f4b1b89-f1df-34d3-b0ed-ba24b69127b2 | -10.64733 | -61.76209 | 2026-09-04 05:25:00 | NOAA-21 | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a48f9373-8089-38d6-8445-378448388b3b | -5.16607 | -60.27718 | 2026-09-04 05:25:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 937179bb-0f23-318c-b6d5-d94d9f819460 | -3.6146 | -60.56292 | 2026-09-04 05:25:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 704c1285-c73b-31be-a538-1db60f7c3a09 | -3.21594 | -61.17609 | 2026-09-04 05:25:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 78036da2-a20c-3beb-91c7-3e4261827f3b | -8.73337 | -69.59235 | 2026-09-04 05:25:00 | NOAA-21 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b9b8561c-4938-3562-a97a-327d2412cd73 | -4.2205 | -59.55629 | 2026-09-04 05:25:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8fac87d3-4037-3c7b-bb61-a1b2b80f661f | -5.07741 | -56.28993 | 2026-09-04 05:25:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 268122ed-43a2-35ae-a3f5-e466811e0091 | -6.12889 | -57.69941 | 2026-09-04 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b87a41eb-d069-3689-a9e0-41628d0fc85e | -5.52121 | -60.20219 | 2026-09-04 05:25:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d1509759-855b-3838-9337-88caed991957 | -4.66402 | -55.94789 | 2026-09-04 05:25:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 52334db7-e6ea-38c4-b07a-f6fd0f213147 | -4.48188 | -55.0781 | 2026-09-04 05:25:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 940c57c5-9127-350d-a7a5-c337203baa01 | -13.30869 | -61.09763 | 2026-09-04 05:25:00 | NOAA-21 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d21a8382-2f77-3327-8c6a-d7bc58351482 | -4.28982 | -59.96306 | 2026-09-04 05:25:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 30138aa1-747d-3b22-b77c-16fefa13dbf4 | -11.21615 | -61.29718 | 2026-09-04 05:25:00 | NOAA-21 | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0e8ae7c0-c558-3d5f-848a-ee354edc450b | -5.33455 | -60.13376 | 2026-09-04 05:25:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 04f9b249-b10c-3de0-bdcb-d50eccb3561b | -3.93438 | -59.34096 | 2026-09-04 05:25:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b8427ed3-06b5-3b82-99c8-ed993ecaf3b0 | -5.32355 | -60.13913 | 2026-09-04 05:25:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| db933d53-3a9d-3852-befc-7aba92ce530e | -5.16938 | -60.27769 | 2026-09-04 05:25:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 383d04ef-32b0-3790-81df-3f9b9915cf10 | -9.04323 | -65.7384 | 2026-09-04 05:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e7d3ebc7-8ff1-3339-a81e-9156dc3b2027 | -6.14967 | -57.70671 | 2026-09-04 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2df0fcf2-6967-319c-bd4d-5177a2be1699 | -7.88102 | -71.75871 | 2026-09-04 05:25:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6ab7508a-2623-384c-b2ac-7fa5023cfb08 | -8.87739 | -68.61215 | 2026-09-04 05:25:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1776d1c8-1b82-376b-af72-68787f66a788 | -8.60393 | -67.17572 | 2026-09-04 05:25:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 31.3 |
| a1314e53-89ec-3075-a086-8a278163c5a6 | -17.09941 | -56.85476 | 2026-09-04 05:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 33127162-2f58-30e3-b743-3c20e22d80a0 | -10.9825 | -60.78232 | 2026-09-04 05:25:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 59614114-1fdd-3d47-865e-5cfb694c1be2 | -17.10075 | -56.85723 | 2026-09-04 05:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 2cc003f9-e1ac-3913-b4df-38eee1e42e0b | -9.20383 | -65.91302 | 2026-09-04 05:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3816b978-165c-3334-8380-780f062a31f3 | -17.09487 | -56.86951 | 2026-09-04 05:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| e7184e08-e057-3bc0-994f-41daff16a679 | -5.26259 | -60.1827 | 2026-09-04 05:25:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 452a1467-cf92-3ae6-b86b-658b83caa386 | -17.10484 | -56.84679 | 2026-09-04 05:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 8805fadb-28e5-3a96-8e04-589035bc09b8 | -9.03703 | -65.73574 | 2026-09-04 05:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a51bd071-ea60-384f-86c8-b5bef719536e | -3.77458 | -61.75506 | 2026-09-04 05:25:00 | NOAA-21 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 3679c4c1-eed2-3ab9-bdf3-76cb0b8b38e2 | -4.24763 | -55.80703 | 2026-09-04 05:25:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9c0ffc44-e92f-3a9e-bae5-b69a2bd489ba | -9.03629 | -65.73228 | 2026-09-04 05:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| efc1bbf3-0a57-3427-9aa7-5c47da0310e0 | -5.17215 | -60.28164 | 2026-09-04 05:25:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c112641a-950d-3d58-98fb-8379e9ca9fe0 | -9.09863 | -65.5138 | 2026-09-04 05:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c31149af-1d7d-3ade-8b23-3fff8ebd6ed1 | -9.03161 | -65.73656 | 2026-09-04 05:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3067b06a-dd6d-34bc-9cb0-83c32fa9b127 | -6.31492 | -56.04512 | 2026-09-04 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5632798f-1df4-32d4-8e7f-cbf98762d087 | -7.87675 | -71.75552 | 2026-09-04 05:25:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2bb023de-c904-3c76-a760-bf81c4567cc6 | -3.81652 | -59.22303 | 2026-09-04 05:25:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b74e7f7d-8f07-3615-9bf2-5a27e71ad22d | -9.03323 | -65.72676 | 2026-09-04 05:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6f9c242a-1dc1-3560-aacf-f858c6e72542 | -3.75987 | -61.76021 | 2026-09-04 05:25:00 | NOAA-21 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| fada61d2-c534-319f-bdd3-05f89c599772 | -5.77755 | -59.18017 | 2026-09-04 05:25:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4ce942d8-92b2-3784-97ba-3149cc716c2d | -6.1299 | -57.741 | 2026-09-04 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4aff4769-77a2-3f8d-b6de-7602d5e23860 | -3.54137 | -59.78973 | 2026-09-04 05:25:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9bc1e206-743a-32a6-ae36-23230a52d5c9 | -9.04016 | -65.7329 | 2026-09-04 05:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d8b87fba-508d-3e5d-815d-bafb185b3b88 | -11.94719 | -55.91343 | 2026-09-04 05:25:00 | NOAA-21 | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3b6b0ab4-6d73-3294-9c8e-8aa65e9841fe | -5.12425 | -56.3374 | 2026-09-04 05:25:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 43f69441-0b7a-3b61-9e9f-cbbe468554d1 | -7.87356 | -71.76622 | 2026-09-04 05:25:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bb3b71a1-99a5-38df-8aa2-476df927799e | -9.11326 | -65.4968 | 2026-09-04 05:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 723b8d82-1954-3884-9f82-4bc202db3b0f | -11.21062 | -53.98407 | 2026-09-04 05:25:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f419965f-430e-37c5-881e-b6a847db912c | -3.76532 | -59.42185 | 2026-09-04 05:25:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 98108236-0f4d-3823-b412-68b226a9fd86 | -8.77674 | -69.37965 | 2026-09-04 05:25:00 | NOAA-21 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eae4bf78-1aad-3ec8-b2ae-787974521589 | -4.09853 | -60.66698 | 2026-09-04 05:25:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 196817a6-dad4-3537-b1bc-9ee40f906e04 | -11.22447 | -53.98115 | 2026-09-04 05:25:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ce651a09-b8af-3012-9e63-06cf999cf1ab | -15.90758 | -50.15868 | 2026-09-04 05:25:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 32ed7bd0-6ab3-32df-b7e7-305e2c770feb | -5.83211 | -55.72458 | 2026-09-04 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7b24bb8f-2853-3fc8-ba8e-d300cc51fe78 | -8.92469 | -69.47249 | 2026-09-04 05:25:00 | NOAA-21 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2789c2a5-5dff-3212-a370-94e287c11aa5 | -5.26205 | -60.18615 | 2026-09-04 05:25:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e226ec71-86d4-37ad-bb1c-3bd7b1b4679a | -5.52451 | -60.20271 | 2026-09-04 05:25:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 282232d7-3632-3f14-977d-8d91ccfda0df | -9.10324 | -65.50974 | 2026-09-04 05:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 45b3fbc4-80f4-3ce8-9158-55dfeb3274cf | -9.53306 | -68.62921 | 2026-09-04 05:25:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8d4214d9-f1b7-3b3a-ab8c-124f362b1aac | -10.54231 | -69.02756 | 2026-09-04 05:25:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 945f7d4f-fb35-353e-b9b0-9f18237cef54 | -3.39778 | -61.3168 | 2026-09-04 05:25:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9979be4f-0a89-3f36-9c0f-f2209197d493 | -10.33866 | -68.00145 | 2026-09-04 05:25:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4e3d523b-eb37-3783-bdd0-ce4a03797d4e | -4.2816 | -59.97238 | 2026-09-04 05:25:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4a5101d8-7ba7-3189-a54c-31c61bb816fd | -15.90844 | -50.16402 | 2026-09-04 05:25:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ee75fa80-9506-36d9-9134-73b73facd869 | -8.59896 | -67.17903 | 2026-09-04 05:25:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 73f95a37-5e3e-3d87-bbed-b4cea99d7ddb | -8.60182 | -67.18786 | 2026-09-04 05:25:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 13f21be2-9032-38d1-baa0-2663dd568e17 | -17.10265 | -56.86392 | 2026-09-04 05:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| c8cf4aee-e73c-3021-b522-7de00a2cdc78 | -3.97641 | -60.03434 | 2026-09-04 05:25:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 62f31406-06a7-319b-b7e5-e177c00410e8 | -5.16277 | -60.27666 | 2026-09-04 05:25:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bc3669ba-63c2-3e08-b504-d7d1bec24c55 | -9.03619 | -65.74062 | 2026-09-04 05:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |


[Clique aqui para ver as próximas entradas](README30.md)
