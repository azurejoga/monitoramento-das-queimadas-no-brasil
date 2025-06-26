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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7b373c35-98e2-387e-9744-f7e517dfcf48 | -8.26267 | -47.02062 | 2025-06-26 03:47:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 70cdd532-66c6-30a4-b520-dccbaf714bf3 | -11.07279 | -46.63589 | 2025-06-26 03:47:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0dd1919d-2160-38d9-ac9b-90059e337248 | -2.44321 | -47.49757 | 2025-06-26 03:47:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 411dd7fe-79f0-3bf9-8882-b118ca953eca | -11.0665 | -46.64119 | 2025-06-26 03:47:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bfe6d6cc-f7f9-3be3-9b48-d13324f5361e | -8.97168 | -49.86956 | 2025-06-26 03:47:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9b95326f-5df8-34b5-82ee-ec456cce2c9f | -10.50698 | -47.20682 | 2025-06-26 03:47:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 28.7 |
| ab2224b7-e1d0-3de6-b504-8eff836c605d | -8.26192 | -47.02475 | 2025-06-26 03:47:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 659031fb-e6bd-3db0-b4bf-af9decb559ec | -8.06218 | -46.96856 | 2025-06-26 03:47:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9f8fe4a0-914c-3a3d-aa87-503996ccc373 | -4.98289 | -37.40053 | 2025-06-26 03:47:00 | NOAA-20 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 2348ebb0-880d-376b-8ca0-a98b3155cca7 | -9.78802 | -48.5658 | 2025-06-26 03:47:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1a2776f0-664e-3c52-a8f8-c8d0d1b4e40b | -9.23948 | -49.31238 | 2025-06-26 03:47:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8b87a479-aa08-3b65-973b-7c9eedc8bc88 | -11.58197 | -44.64218 | 2025-06-26 03:47:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 78258373-8b28-39d8-b6c1-c796133c4ef1 | -7.75252 | -47.61751 | 2025-06-26 03:47:00 | NOAA-20 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 19a1a292-42cc-369b-b478-6795a42e4d24 | -5.33608 | -43.75014 | 2025-06-26 03:47:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| dfc154c0-6c86-3e4f-9394-4a3805a0cede | -9.88033 | -48.05309 | 2025-06-26 03:47:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0d7ef641-7e95-333e-b8c6-45f52e41a72a | -10.51233 | -47.20798 | 2025-06-26 03:47:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 3cfe8347-feab-3dd6-b269-306436816558 | -10.51366 | -47.20088 | 2025-06-26 03:47:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b8d051d2-8a98-37bb-acfb-bf82c1f02ddb | -10.2466 | -44.63672 | 2025-06-26 03:47:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 81c49ef9-ab75-3990-a7f7-3b83e8d949e3 | -10.65004 | -44.49235 | 2025-06-26 03:47:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8c720cca-3f5b-30b2-b1b6-eacd92bdd5d3 | -5.49164 | -42.1515 | 2025-06-26 03:47:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 3636cb64-e21f-3426-95f7-7c42a080a5ad | -9.10848 | -49.43594 | 2025-06-26 03:47:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 5778c2be-08c1-37cd-9921-ff87afa45ed8 | -10.5063 | -47.21045 | 2025-06-26 03:47:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 529770d8-d41e-3765-8ea2-38c4216b5dd7 | -10.11775 | -44.15313 | 2025-06-26 03:47:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 92bea931-74dd-39fa-bac7-d8e118a2105d | -4.12496 | -43.06885 | 2025-06-26 03:47:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 61fed599-e1de-36b2-93b4-1d94ee325692 | -5.48748 | -42.15078 | 2025-06-26 03:47:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 8a61928e-0dab-3450-9174-35229bef4733 | -4.27594 | -48.1813 | 2025-06-26 03:47:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cafbdab5-f699-3b2e-b25f-7f764a3f8585 | -5.1947 | -37.69419 | 2025-06-26 03:47:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 0.5 |
| d0e97f9c-0fe5-327c-b38d-abc6a039eb2e | -10.41669 | -47.50627 | 2025-06-26 03:47:00 | NOAA-20 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ed97a55a-de70-3b15-bd46-f3e60fad79a7 | -11.60683 | -46.50623 | 2025-06-26 03:47:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 68508991-ecfa-3553-86c2-edf43f49a0b0 | -9.32992 | -47.83155 | 2025-06-26 03:47:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 95c3b9cd-4738-3381-895b-20eeda267bf0 | -10.06826 | -49.65579 | 2025-06-26 03:47:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 33caef9f-26e3-364d-8583-0ebf90c3bd31 | -9.12257 | -49.44287 | 2025-06-26 03:47:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 9c127122-1b95-3ae0-bed9-63da47a52f6a | -9.671 | -48.77691 | 2025-06-26 03:47:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3c2dee9e-472d-322d-b018-ceaa870a66fc | -8.67393 | -49.9513 | 2025-06-26 03:47:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 9165106e-d190-3dd3-8e49-f5a7b67f2a44 | -9.33067 | -47.82763 | 2025-06-26 03:47:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| a87c14b9-ff97-3861-87eb-700961d529b7 | -4.52627 | -48.04804 | 2025-06-26 03:47:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 5b88c099-d7be-3e29-aa77-39cc74819baf | -8.47654 | -48.26304 | 2025-06-26 03:47:00 | NOAA-20 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 222c542f-cb67-3a59-b28d-47b991fbb4ef | -4.66428 | -40.5622 | 2025-06-26 03:47:00 | NOAA-20 | NOVA RUSSAS | CEARÁ | Brasil | 2309300 | 23 | 33 | nan | nan | nan | Caatinga | 12.8 |
| 670d5373-cf15-3512-8201-2790b5f44829 | -11.07221 | -46.63901 | 2025-06-26 03:47:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7298c012-b69d-3cb8-b6c0-f5fd0dd9fbab | -8.71941 | -48.01698 | 2025-06-26 03:47:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c9fa0e48-2888-388c-90eb-9e4757aba088 | -9.67187 | -48.77236 | 2025-06-26 03:47:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d402c534-e744-377f-91f9-addee5581bfa | -4.18694 | -48.154 | 2025-06-26 03:47:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1aacc288-92aa-3083-9fe2-5ce95201fa08 | -4.12883 | -43.06651 | 2025-06-26 03:47:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 47787074-8d04-3436-9bf9-b441a068945a | -11.60626 | -46.50932 | 2025-06-26 03:47:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a010d06a-5594-3e9f-9195-6dbe8b0a66cc | -5.33142 | -43.7494 | 2025-06-26 03:47:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| a7e5fbf6-e2b2-3e22-9d42-62fa70ae27a2 | -8.47057 | -48.26201 | 2025-06-26 03:47:00 | NOAA-20 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c3200cf0-f7da-3865-93ff-28e30e2264d6 | -7.74672 | -47.61652 | 2025-06-26 03:47:00 | NOAA-20 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 44b02016-28b5-3324-b546-383cd3f3ca32 | -8.23421 | -44.93688 | 2025-06-26 03:47:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 88850697-bcee-3bd6-a637-fb56229c77d4 | -11.08364 | -46.63454 | 2025-06-26 03:47:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 736380aa-4643-371e-bd2f-438a6e29d465 | -9.32844 | -47.83133 | 2025-06-26 03:47:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 67436622-573e-38c5-a996-a0856ca8c74a | -8.4825 | -48.26416 | 2025-06-26 03:47:00 | NOAA-20 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 18715435-3aaa-3b5a-94ef-f5d8be6e62d4 | -11.07468 | -46.6378 | 2025-06-26 03:47:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f9418efd-1318-361f-8962-fd577b7c1f99 | -5.0021 | -39.83495 | 2025-06-26 03:47:00 | NOAA-20 | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 37ea4015-5550-35d3-84b2-d993f9e391d3 | -2.44588 | -47.49663 | 2025-06-26 03:47:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dd56000a-46a2-3c8f-845f-5f84b440f4ed | -5.48813 | -42.14695 | 2025-06-26 03:47:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 700f6aab-2134-32e5-95b8-e00537a3fc9f | -9.11915 | -49.44881 | 2025-06-26 03:47:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| c2904a88-3ef2-3022-8095-8600849985ac | -11.61129 | -46.51028 | 2025-06-26 03:47:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 23ec6a01-1984-35a0-87f0-8ecca9c6977b | -9.12013 | -49.44365 | 2025-06-26 03:47:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| dbf24f71-0619-34ab-aa5a-369d666d70d3 | -4.1243 | -43.06575 | 2025-06-26 03:47:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bb0e5837-0680-3ed5-af53-c00586c161ae | -10.513 | -47.20439 | 2025-06-26 03:47:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| c579b00a-ceaf-3892-a859-2a830fb2ae7f | -8.26118 | -47.02878 | 2025-06-26 03:47:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8e215e95-8826-3057-8e07-b80f2a0b9a89 | -10.51166 | -47.21158 | 2025-06-26 03:47:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 01cf79d5-988e-3be6-88a0-3c7450222251 | -10.27144 | -47.61155 | 2025-06-26 03:47:00 | NOAA-20 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e823fefc-9587-38e2-884e-61bee06b9905 | -10.24572 | -44.63951 | 2025-06-26 03:47:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 11c1ea25-ddbe-354d-bfb0-5d14f7c4aa0a | -8.67284 | -49.95694 | 2025-06-26 03:47:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a76bc0ab-7fa1-31de-bbec-23bcd5e4c666 | -9.11479 | -49.43725 | 2025-06-26 03:47:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| cc48d145-e8df-36a3-9700-db4f36f1a94d | -5.11006 | -43.14503 | 2025-06-26 03:47:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1abdc0b9-bb11-3e5a-a609-738cecbef26f | -11.08042 | -46.63556 | 2025-06-26 03:47:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3414780e-b459-3020-b7c1-1c97233f0924 | -11.08616 | -46.6333 | 2025-06-26 03:47:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fbf1e9a6-9ee3-3425-bedc-266e180880c8 | -11.6264 | -41.83555 | 2025-06-26 03:47:00 | NOAA-20 | IBITITÁ | BAHIA | Brasil | 2913101 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 7dc53e58-648c-3129-9fe6-709c09f22db8 | -10.62469 | -48.08195 | 2025-06-26 03:47:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9ca9480e-1361-3c2e-bae5-c7f61bb08afe | -10.2481 | -47.68087 | 2025-06-26 03:47:00 | NOAA-20 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7fd54118-42b0-3492-b536-d5b532d9e79c | -11.07529 | -46.63467 | 2025-06-26 03:47:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 711e5945-be27-3e67-a158-9be6f370d7a3 | -10.66527 | -46.65148 | 2025-06-26 03:47:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e5b650eb-5573-36b5-9a4a-4b2648a72e9c | -10.24663 | -47.68074 | 2025-06-26 03:47:00 | NOAA-20 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c30026b0-d677-38b0-a530-78ea7b69edcf | -9.37345 | -47.63586 | 2025-06-26 03:47:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d095e90f-43a2-3f4a-9218-ca4a17344a54 | -10.5083 | -47.19975 | 2025-06-26 03:47:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| bac69e06-1a83-33c9-81f7-15206960e760 | -9.78718 | -48.57021 | 2025-06-26 03:47:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5425643c-3c67-353b-9e7b-ba2469f54da4 | -11.0785 | -46.63366 | 2025-06-26 03:47:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 81772bbb-f386-3a03-9db5-aebf27cd21a5 | -11.5856 | -44.64748 | 2025-06-26 03:47:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b76bdb8e-a45f-3796-8ae1-6b225a0c1dbe | -11.61245 | -46.50407 | 2025-06-26 03:47:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0f12fd80-b2db-3054-81cb-3a6d8b5c0ec0 | -4.52681 | -48.00818 | 2025-06-26 03:47:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ee2443fd-3571-39b1-a35f-f58da5061564 | -10.24667 | -44.63409 | 2025-06-26 03:47:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| db2b5fec-73b0-3a37-870e-85c815f398fa | -8.70831 | -47.97958 | 2025-06-26 03:47:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 49d7c72d-8e49-37af-96e8-56d8a827062c | -9.11381 | -49.44239 | 2025-06-26 03:47:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 37d88e19-0025-3d55-949c-4c663085c9ba | -5.48397 | -42.14624 | 2025-06-26 03:47:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 96746bd4-f982-3f13-aed1-eb8be90df12f | -11.08878 | -46.63543 | 2025-06-26 03:47:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a6161976-42a6-3da6-b983-d87b6c0ad86b | -5.19135 | -37.69366 | 2025-06-26 03:47:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 0.7 |
| acdcc27d-55de-393d-834f-3b7f1a09170e | -11.58642 | -44.64301 | 2025-06-26 03:47:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c0bf36c2-deae-3f58-9fba-f707bd1c5817 | -10.66466 | -46.6547 | 2025-06-26 03:47:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| df0d658e-4dfd-335c-a2c9-b643e64c4444 | -4.18793 | -48.14833 | 2025-06-26 03:47:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fff2bc80-6ec1-3653-b93c-aee26da3a779 | -10.416 | -47.50987 | 2025-06-26 03:47:00 | NOAA-20 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 581669f3-d936-33ac-b1c1-40b55a218c4d | -5.49229 | -42.14769 | 2025-06-26 03:47:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| f7ea2a19-ddbc-30b8-99a1-c9267dda2e56 | -4.53313 | -48.00888 | 2025-06-26 03:47:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 526031c7-f645-3c0b-8103-1c59a5935112 | -11.08102 | -46.63243 | 2025-06-26 03:47:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9649f6bd-ece3-320c-885c-9eb15b432178 | -10.24879 | -47.67713 | 2025-06-26 03:47:00 | NOAA-20 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0b283a42-495e-3557-b196-f6c139214102 | -5.19078 | -37.6972 | 2025-06-26 03:47:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 0.7 |
| ddcc118d-a0ff-330b-907c-ed736acef0db | -9.11578 | -49.43211 | 2025-06-26 03:47:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 75c35416-8ea3-39b4-8774-152273030f02 | -4.97956 | -37.4 | 2025-06-26 03:47:00 | NOAA-20 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 16cb72e9-83cd-3b98-8ce5-f2a986670d81 | -10.24735 | -47.67701 | 2025-06-26 03:47:00 | NOAA-20 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README6.md)
