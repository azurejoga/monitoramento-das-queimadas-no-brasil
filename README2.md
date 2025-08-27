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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 22a801c8-9e41-3a7d-ab32-0a2738636595 | -10.0977 | -62.9085 | 2025-08-27 00:10:00 | GOES-19 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 82b066f0-eb33-347c-a7ee-fb384e1a0460 | -9.1527 | -59.5803 | 2025-08-27 00:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 48.2 |
| cb4b8f67-d74e-3df5-93f9-1f9b24a1e11f | -10.2743 | -64.4907 | 2025-08-27 00:20:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 4a4abc18-775b-301c-b279-85cbe171c2c1 | -19.5767 | -47.5367 | 2025-08-27 00:20:00 | GOES-19 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 57.9 |
| 3ebf83d5-8ba4-3fde-b21f-64106277828a | -6.8412 | -58.9746 | 2025-08-27 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 83.4 |
| b600cca8-8baf-3e63-aa79-1eae0f2dfdbe | -13.1837 | -45.2865 | 2025-08-27 00:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 99.9 |
| 4f7e4a58-075d-36a6-8458-fb26d7ac9fcf | -13.1644 | -45.2897 | 2025-08-27 00:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 156.4 |
| 32dcbd52-da95-3e72-8829-8bc7f29440d5 | -12.9068 | -44.658 | 2025-08-27 00:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 44.7 |
| 20152219-4b35-32b3-b879-d14304ae5cfd | -9.0819 | -49.5853 | 2025-08-27 00:20:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 123.0 |
| 906d88c1-c10e-368b-bcb5-4f285b3664f7 | -5.5582 | -44.2769 | 2025-08-27 00:20:00 | GOES-19 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 62.6 |
| bcf8ed9e-ef7d-36ac-97cd-ab2447e4ed33 | -21.5783 | -47.4614 | 2025-08-27 00:20:00 | GOES-19 | SANTA RITA DO PASSA QUATRO | SÃO PAULO | Brasil | 3547502 | 35 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 54caefa4-9962-3688-ab65-b53815f4428e | -6.8413 | -58.9552 | 2025-08-27 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 78.3 |
| a7d9f509-a765-3eff-a854-e88a3d554c44 | -5.118 | -43.2198 | 2025-08-27 00:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 2391b082-ef55-3023-8097-e06a68b17a1c | -9.5811 | -55.3713 | 2025-08-27 00:20:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 237f1a01-f798-36be-b75c-f4a77e4232d2 | -9.1529 | -59.5609 | 2025-08-27 00:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 103.0 |
| 2dc2b9bc-0015-3ca7-b883-cf740407d4d4 | -9.1009 | -49.5621 | 2025-08-27 00:20:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 132.3 |
| c7779f19-e6e5-3920-8a82-f587a08c44cb | -6.5769 | -47.3881 | 2025-08-27 00:20:00 | GOES-19 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 66.2 |
| c32a014b-6001-3917-8988-180950c2aab0 | -8.271 | -45.1149 | 2025-08-27 00:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 103.5 |
| 6d9635d1-e115-385a-a57e-3b8fef6b1fed | -5.1181 | -43.1964 | 2025-08-27 00:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 85.4 |
| ebb00273-c05c-35d7-953c-65f15c12316e | -6.8228 | -58.9753 | 2025-08-27 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 3c6b69db-c91f-38b9-892a-78c73393e193 | -8.9028 | -60.7498 | 2025-08-27 00:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 81.9 |
| d808c439-a73b-36ab-83e5-a152a828eb5e | -9.8102 | -64.2454 | 2025-08-27 00:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 49.1 |
| b9b80c0f-9fd8-3273-9aff-27f8fd5a07f0 | -8.2707 | -45.1377 | 2025-08-27 00:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 53.2 |
| e6635a1f-4ce9-33e7-9a42-383c6fd3b3f0 | -4.4977 | -46.3731 | 2025-08-27 00:20:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 69.9 |
| b3cc40ca-a046-3d63-880d-db6595c60919 | -9.1715 | -59.5599 | 2025-08-27 00:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 91.5 |
| 869aab15-fb99-3f12-8b0a-0cde40cd8a5b | -6.8229 | -58.956 | 2025-08-27 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.1 |
| cdbc2ac5-7e76-34f1-a246-759223b6ac75 | -10.2742 | -64.5096 | 2025-08-27 00:20:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 44.0 |
| c97996ba-8a5c-362d-becb-5eb5bc8d04f8 | -9.7915 | -64.265 | 2025-08-27 00:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 284ec1e0-5607-3818-a75c-eb5e03e12095 | -9.0771 | -66.0695 | 2025-08-27 00:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 30.7 |
| d9de8e5a-770b-3d77-8b9f-a636b9051d40 | -9.0821 | -49.5638 | 2025-08-27 00:20:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 102.3 |
| 015ea67a-e0b9-3c0a-98cb-e9479e2ba01d | -9.7916 | -64.2461 | 2025-08-27 00:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 85.3 |
| 8f362a9a-9648-3e93-90cf-680850bb0a37 | -5.5584 | -44.2539 | 2025-08-27 00:20:00 | GOES-19 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 1fc6bf27-80d7-3494-bcb2-9da66a22280b | -21.5776 | -47.4852 | 2025-08-27 00:20:00 | GOES-19 | SANTA RITA DO PASSA QUATRO | SÃO PAULO | Brasil | 3547502 | 35 | 33 | nan | nan | nan | Cerrado | 109.9 |
| 53d01492-dd56-3ef2-b428-61631252f22b | -8.8841 | -60.7699 | 2025-08-27 00:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 239.4 |
| 060f62fc-b20d-3059-a983-70c8e1788c10 | -8.9026 | -60.769 | 2025-08-27 00:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 122.3 |
| d87f31ef-86e4-34e3-a17c-64e16a4fb64e | -9.8101 | -64.2642 | 2025-08-27 00:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 43.4 |
| 13a6cc66-080d-3805-909a-08632db74bca | -8.8842 | -60.7507 | 2025-08-27 00:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 141.7 |
| f3e4377a-3d35-3e86-907f-5bea028940dd | -9.1007 | -49.5835 | 2025-08-27 00:20:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 221.6 |
| eaf1b17c-78e5-3c8e-97f7-020b02018714 | -9.572 | -45.7425 | 2025-08-27 00:22:00 | METOP-B | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| d4286dbf-76ab-33a6-963e-e7bb24c88c93 | -9.0962 | -49.565201 | 2025-08-27 00:22:00 | METOP-B | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c93c1c53-3962-3c7f-b5f7-eab02e0f7fbd | -19.570499 | -47.516102 | 2025-08-27 00:22:00 | METOP-B | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 0bf50cfd-6f35-33a9-b55c-360918cd5472 | -12.7503 | -48.176899 | 2025-08-27 00:22:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 63cbc484-95c5-3c3b-bcbd-c1a7f2d093a7 | -6.836 | -51.380798 | 2025-08-27 00:22:00 | METOP-B | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e1b58836-1b6f-31f7-98bc-93726caef05f | -21.5835 | -47.493401 | 2025-08-27 00:22:00 | METOP-B | SANTA RITA DO PASSA QUATRO | SÃO PAULO | Brasil | 3547502 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 3dfcd6c4-a81d-312c-bab7-1a00d5e0fcd7 | -6.825 | -58.919498 | 2025-08-27 00:22:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e8c46652-70cc-3670-b98c-e93a2924dd6b | -13.4269 | -46.856701 | 2025-08-27 00:22:00 | METOP-B | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| a9efc034-9657-3446-b229-5c23993e9e0c | -13.4447 | -46.843899 | 2025-08-27 00:22:00 | METOP-B | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| ee0acf99-9c82-3382-b876-de7ae320af9a | -6.6908 | -48.375099 | 2025-08-27 00:22:00 | METOP-B | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 89a49785-0d5b-369c-923f-fe99cfd812e3 | -9.1947 | -46.722599 | 2025-08-27 00:22:00 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 877115b2-8e47-3eea-a38c-1c6a245b6586 | -7.8052 | -51.063999 | 2025-08-27 00:22:00 | METOP-B | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 36757096-6b47-38af-93bf-16cceb3d73d9 | -16.7166 | -50.396198 | 2025-08-27 00:22:00 | METOP-B | AURILÂNDIA | GOIÁS | Brasil | 5202601 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| c7a7135e-f2c2-30f5-8156-4b1ea9bb302f | -8.3317 | -50.563 | 2025-08-27 00:22:00 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 38bd2ae9-700e-3872-a57f-b3f80a67d154 | -9.4027 | -60.452999 | 2025-08-27 00:22:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 05fe8694-3bc6-3fcc-93ab-6830023ac7b0 | -7.2603 | -57.646999 | 2025-08-27 00:22:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c2dc3a7d-c78b-320d-bc37-d3fbc4129666 | -19.2686 | -44.403702 | 2025-08-27 00:22:00 | METOP-B | PARAOPEBA | MINAS GERAIS | Brasil | 3147402 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 8cf96230-815f-383b-9649-6e9559ee765f | -15.6261 | -52.694199 | 2025-08-27 00:22:00 | METOP-B | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c739d6b2-dafd-3a86-9fe4-49569475a7fa | -6.7931 | -59.5933 | 2025-08-27 00:22:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 81ea63f1-a267-32db-b38c-8f380aeb6972 | -12.7728 | -48.094398 | 2025-08-27 00:22:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ee43c5a3-5bb6-382c-9714-0a98285392e5 | -15.0949 | -48.609798 | 2025-08-27 00:22:00 | METOP-B | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 5ce73ec4-5789-31d0-990b-cce5885fea71 | -10.0876 | -62.809502 | 2025-08-27 00:22:00 | METOP-B | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 8bc0e3c9-7f0a-333f-9e46-a6910d1c8f35 | -11.0366 | -52.009998 | 2025-08-27 00:22:00 | METOP-B | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e0b24704-efd1-345c-9d07-1a7e01510578 | -15.0986 | -48.5341 | 2025-08-27 00:22:00 | METOP-B | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 4919f047-5b87-3d31-9976-2aec6dd2490d | -7.7417 | -50.275002 | 2025-08-27 00:22:00 | METOP-B | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fafc7f67-353c-3d41-bb8b-25a3e901ab8f | -9.1389 | -50.765999 | 2025-08-27 00:22:00 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8a644103-6973-3e0e-aeb0-befa478d18bc | -9.1927 | -46.713699 | 2025-08-27 00:22:00 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c4b22cd6-696c-32b3-b46c-e4b21e9d3440 | -20.531 | -46.0933 | 2025-08-27 00:22:00 | METOP-B | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 13190190-c76b-32ac-88ca-a3fd09363c1a | -15.1062 | -48.6147 | 2025-08-27 00:22:00 | METOP-B | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 70fa8251-b700-33cc-ba1c-1e01ebf364aa | -5.7657 | -53.7467 | 2025-08-27 00:22:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0261ff04-dbef-389a-9f40-66489d1a1fa6 | -7.1777 | -59.6884 | 2025-08-27 00:22:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 418328a1-f83d-359e-a710-c48b289c83cb | -19.5737 | -47.530701 | 2025-08-27 00:22:00 | METOP-B | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| bd1ff08e-a3e8-35b9-b12a-75a2818794a5 | -15.6297 | -52.7122 | 2025-08-27 00:22:00 | METOP-B | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| bd17d3e6-b14e-3a3c-a54f-fdc7f1ebd4d3 | -8.7315 | -49.729301 | 2025-08-27 00:22:00 | METOP-B | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d05a069d-df1f-3a69-9243-4178bc755fde | -9.4215 | -60.497299 | 2025-08-27 00:22:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 84eb4746-7154-38f9-92d9-3439a47c3a1e | -15.1369 | -48.659801 | 2025-08-27 00:22:00 | METOP-B | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 83dbcc27-ad87-3a22-8673-5259bcc18ba8 | -13.0633 | -46.3167 | 2025-08-27 00:22:00 | METOP-B | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| b953536a-e6f8-3eda-b2b2-19d7d61ad63e | -4.4907 | -46.349602 | 2025-08-27 00:22:00 | METOP-B | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b8bf4ea2-3c81-3018-9c30-3a99d03a425f | -10.5967 | -52.303101 | 2025-08-27 00:22:00 | METOP-B | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4ea7f084-f576-3855-b19d-59787dc3e95f | -10.5989 | -54.874699 | 2025-08-27 00:22:00 | METOP-B | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 86ee887d-81ef-3ce8-887a-b9c611f135c2 | -21.5737 | -47.4958 | 2025-08-27 00:22:00 | METOP-B | SANTA RITA DO PASSA QUATRO | SÃO PAULO | Brasil | 3547502 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 7c28c6ef-0738-3431-b735-01bcb5d12925 | -6.6565 | -53.170898 | 2025-08-27 00:22:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7f543f32-0818-3701-8d7f-fddadf5870cb | 0.777 | -51.3298 | 2025-08-27 00:22:00 | METOP-B | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 02385b0e-9d4d-35f8-8bcd-ebe9d03cff50 | -12.7761 | -48.1091 | 2025-08-27 00:22:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 956db3ee-dc09-360a-898b-b1419dc60ecb | -6.8382 | -58.933899 | 2025-08-27 00:22:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| fd9d9a9e-7ef1-35e2-a2ea-532058cd34f7 | -14.9114 | -49.597599 | 2025-08-27 00:22:00 | METOP-B | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| eae3f57c-c7e9-36e1-ac9a-77417419a03e | -7.2779 | -46.993401 | 2025-08-27 00:22:00 | METOP-B | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f9e02d2b-7559-34ff-8973-a8294fb38605 | -17.788099 | -44.488998 | 2025-08-27 00:22:00 | METOP-B | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 723edc76-aed8-3209-9229-c154b95804d9 | -12.7601 | -48.174599 | 2025-08-27 00:22:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4e12b568-3afe-35b8-ae99-c53e9694b69c | -9.1872 | -60.738602 | 2025-08-27 00:22:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 39823842-7256-3a62-8cf0-7c045d428a4e | -9.093 | -49.551102 | 2025-08-27 00:22:00 | METOP-B | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ee9de236-25d8-3c05-a85e-53b290a86830 | -12.9282 | -46.313599 | 2025-08-27 00:22:00 | METOP-B | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ba8e6151-0ef3-3841-80c3-44667a900393 | -7.8022 | -51.050201 | 2025-08-27 00:22:00 | METOP-B | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c1b47f47-7033-36b8-a30d-f5ac1aff1d1c | -9.2905 | -56.8811 | 2025-08-27 00:22:00 | METOP-B | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9bcd4aed-2c8c-38e5-ba88-b30bd8817cec | -11.0347 | -45.125599 | 2025-08-27 00:22:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 22e80099-c776-3102-b056-d95a30afb32e | -13.2168 | -44.536098 | 2025-08-27 00:22:00 | METOP-B | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4d714fb3-d750-3192-ac54-baca66a428fe | -21.5853 | -47.454201 | 2025-08-27 00:22:00 | METOP-B | SANTA RITA DO PASSA QUATRO | SÃO PAULO | Brasil | 3547502 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| a9ff608f-f770-342e-a37f-c031a3722cc0 | -9.1583 | -40.592701 | 2025-08-27 00:22:00 | METOP-B | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| a30615d6-f808-3458-9a09-d862cd9dd4e8 | -12.7666 | -48.1577 | 2025-08-27 00:22:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b2455f75-29b2-3d2c-b7ba-e1b09110aea7 | -12.7372 | -48.1646 | 2025-08-27 00:22:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b926609c-d236-3ad7-9002-c9b278a1e481 | -10.8611 | -47.318901 | 2025-08-27 00:22:00 | METOP-B | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 54fad18b-8ebe-344b-859a-7726d241add3 | -6.8445 | -58.915501 | 2025-08-27 00:22:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README3.md)
