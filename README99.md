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

## Dados Diários - Página 99

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5cb95d41-bff7-33f6-86bc-75f14b414428 | -6.8772 | -43.6152 | 2025-08-28 14:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 205.1 |
| d3087389-c475-3921-81d3-f57c97e1c379 | -11.3517 | -43.566 | 2025-08-28 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 91.6 |
| 55c9ae75-da3d-3c4a-933c-0a20b84b8f15 | -10.4738 | -57.9366 | 2025-08-28 14:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 86.4 |
| 5ec036fe-c3a2-3814-93a6-8d71a7004834 | -5.535 | -42.65 | 2025-08-28 14:10:00 | GOES-19 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 87.8 |
| c2102257-a3de-35f6-9b6e-b27ffd61b946 | -13.8198 | -52.743 | 2025-08-28 14:10:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 57.4 |
| d6539209-412b-3287-b7b4-8517af7a9d78 | -9.6574 | -64.9845 | 2025-08-28 14:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 6c9b51af-cda9-372f-87d1-db6e2567a5a6 | -12.9961 | -56.9201 | 2025-08-28 14:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 86.7 |
| 232554f8-c6b4-33ce-bf9b-d14746f64acf | -6.8583 | -43.6169 | 2025-08-28 14:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 100.2 |
| 91927519-1095-3add-b597-99ee66e9e53d | -5.7981 | -42.6059 | 2025-08-28 14:10:00 | GOES-19 | LAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2205540 | 22 | 33 | nan | nan | nan | Caatinga | 112.6 |
| a2e16532-b8a0-3efb-b05f-0dd055e2d187 | -8.9479 | -65.9616 | 2025-08-28 14:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 3871faff-c2ac-3185-be50-2d1ae4519ecd | -12.8613 | -48.1213 | 2025-08-28 14:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 154.6 |
| 3fc7800f-d54f-37d9-9cbf-c5f8aefe05d0 | -13.4208 | -46.9864 | 2025-08-28 14:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 2c98a6d1-b9f4-3227-adc5-2f47c04ebd3b | -13.0863 | -46.3352 | 2025-08-28 14:10:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 79.3 |
| 0b400c52-beab-36e8-8b0e-5042a01cde33 | -7.3196 | -46.109 | 2025-08-28 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 79b8c350-0a90-3ef4-860c-b22b13ec1060 | -11.6127 | -47.2907 | 2025-08-28 14:10:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 104.8 |
| 8eaaa2d6-1e2c-388d-b04b-07512d0d67e4 | -16.3606 | -43.7858 | 2025-08-28 14:10:00 | GOES-19 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 144.3 |
| dcb04c2c-bd9b-3915-8b1b-89c77fdcccbf | -13.5386 | -46.8775 | 2025-08-28 14:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 7ff3e7d5-76e0-3938-a715-3fd36940364b | -9.1339 | -65.788 | 2025-08-28 14:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 768.3 |
| 2e999582-8601-3ad9-9dec-5481beb368be | -11.1017 | -44.7476 | 2025-08-28 14:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 945498dd-cb38-385d-87c9-37dc28db640a | -14.3696 | -52.0813 | 2025-08-28 14:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 112.9 |
| 9cef296a-fea1-3995-89b9-73a33b2b07a1 | -13.4204 | -47.009 | 2025-08-28 14:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 52.7 |
| 4e1d2a3e-f12f-330b-9a97-dda509cc9993 | -10.4736 | -57.9563 | 2025-08-28 14:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 89.3 |
| 9536db30-6a32-3088-9b71-d17c308545e0 | -14.3116 | -53.2501 | 2025-08-28 14:10:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 149.9 |
| 54a1a249-cdb2-3b3e-9de3-37a5dd735c2a | -6.178 | -44.0688 | 2025-08-28 14:10:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 105.8 |
| d4a7dba6-8a9a-35ca-823b-94ad9ed053d5 | -5.8169 | -42.6043 | 2025-08-28 14:10:00 | GOES-19 | LAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2205540 | 22 | 33 | nan | nan | nan | Caatinga | 102.5 |
| 76eae8b8-a363-3e90-8001-8dea6fee9dcc | -11.3334 | -43.5216 | 2025-08-28 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 127.3 |
| 6aaec72f-75ce-3504-b613-305a75796c57 | -10.8049 | -60.7644 | 2025-08-28 14:20:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 86.1 |
| 40d9b319-7026-3a6f-892b-48c2d3605040 | -12.8617 | -48.099 | 2025-08-28 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 7148f49e-8421-3194-aae9-f767618931bd | -6.6759 | -58.846 | 2025-08-28 14:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 1f89592a-b944-3bf2-bc68-17cb0192b6c6 | -12.9961 | -56.9201 | 2025-08-28 14:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 9e74b724-d8b2-3f15-a577-61ec06699ede | -10.8236 | -60.7633 | 2025-08-28 14:20:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 28ef1ad6-77a1-3dc8-bdc6-0e4a043725f9 | -13.4212 | -46.9637 | 2025-08-28 14:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 48.5 |
| 41c0cc09-0d27-38de-9717-8a2e39fd7a11 | -8.4596 | -43.6645 | 2025-08-28 14:20:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 115.8 |
| 3f80bc56-1b13-3ffe-90c8-d1903d8190e4 | -12.8032 | -48.1516 | 2025-08-28 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 2dc1bd8f-a142-3e20-9133-d65f0f15f271 | -7.6222 | -42.6975 | 2025-08-28 14:20:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 105.8 |
| 19fbb3c9-0da9-393b-8479-b3aac3682f26 | -7.3193 | -46.1314 | 2025-08-28 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 11e3e62b-57c9-3bc0-b327-f0ef0d01ace0 | -14.3696 | -52.0813 | 2025-08-28 14:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 846eae3f-b48c-3d72-ab04-56aab05c16e3 | -4.8751 | -43.1661 | 2025-08-28 14:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 99.7 |
| 4f911ab7-1c3f-3e91-9325-1acedf204146 | -6.1595 | -44.0472 | 2025-08-28 14:20:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 140.1 |
| a5ec8184-d6c3-333a-a813-8f0c19e6a9e2 | -7.1917 | -44.0732 | 2025-08-28 14:20:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 158.9 |
| 0f1470bc-5eb0-35d7-a357-32cbea2f4ece | -14.311 | -53.2921 | 2025-08-28 14:20:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 9e49648a-be83-37ed-a05e-5d67681e5167 | -14.3339 | -51.9157 | 2025-08-28 14:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 54.6 |
| 71901437-ba7f-3268-a96c-5cfcbfdb84d7 | -6.4357 | -44.5535 | 2025-08-28 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 81.6 |
| bf4f6c87-63b1-3901-aac2-8375945585bf | -10.8233 | -60.8019 | 2025-08-28 14:20:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 82.0 |
| 1f25c14f-2e29-3236-a2d2-2692c42029c6 | -10.4738 | -57.9366 | 2025-08-28 14:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 98.7 |
| 1dc9d1af-a41e-3148-bb9c-c08a525812b6 | -10.8421 | -60.8009 | 2025-08-28 14:20:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 73.8 |
| f921e02c-97e4-36b3-a155-67c217786b63 | -13.4204 | -47.009 | 2025-08-28 14:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 5a5ce369-0d13-33ef-980b-e9a7b977c3cd | -9.4372 | -48.2518 | 2025-08-28 14:20:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 118.9 |
| 6f3e30d8-5270-3355-b06a-b7c7a6e23e00 | -12.8228 | -48.1267 | 2025-08-28 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 83.8 |
| 7bee24c8-ced2-3f5f-996a-e16886b4b692 | -9.2446 | -65.8965 | 2025-08-28 14:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 17ec4960-0d48-3074-b13d-a65643ce8a29 | -14.3309 | -53.2477 | 2025-08-28 14:20:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 116.3 |
| 4f9479ca-e4dd-3760-b22a-83e920b97cf9 | -11.2189 | -55.0585 | 2025-08-28 14:20:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 114.1 |
| ac483ad5-039d-3bb6-b247-7da35451961c | -14.3306 | -53.2688 | 2025-08-28 14:20:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 68.0 |
| ca550d91-d54d-3e94-baff-90f2340865ac | -13.0151 | -56.9184 | 2025-08-28 14:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 122.4 |
| eca78c8d-004e-30ab-b8f3-8ffa79ae4d0a | -7.3196 | -46.109 | 2025-08-28 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 79.7 |
| eb0ac515-2154-3545-886f-96a230272741 | -8.7322 | -47.4003 | 2025-08-28 14:20:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 82.9 |
| f32e2dc0-1fef-3d77-bba5-c0e3595e4083 | -12.8998 | -48.1158 | 2025-08-28 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 8a3bd19f-10ab-3792-a820-c158d6b9d8d9 | -8.7325 | -47.3783 | 2025-08-28 14:20:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 92.3 |
| edbfe43d-2a82-31c0-aaa2-922e441aebea | -9.5424 | -62.3823 | 2025-08-28 14:20:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 60.3 |
| a716a41f-bdaf-3128-b09f-49829fbe3bda | -12.8805 | -48.1186 | 2025-08-28 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 62.3 |
| 126788c9-722a-3feb-b1dc-9817f41b2963 | -10.3077 | -46.8292 | 2025-08-28 14:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 5f3ee503-83ee-31f3-8243-cf15c8e918a3 | -9.4363 | -48.3174 | 2025-08-28 14:20:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 124.3 |
| a591710d-6ed5-330f-bdbc-ff004db27519 | -18.2025 | -45.5723 | 2025-08-28 14:20:00 | GOES-19 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 82.7 |
| c27076a4-e9a4-3d92-b365-77ebcd4b706c | -8.4407 | -43.6666 | 2025-08-28 14:20:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 133.4 |
| b10630e4-c237-35b0-9644-3c0a4688cee5 | -9.6574 | -64.9845 | 2025-08-28 14:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 584155cd-4bc4-33fe-badc-2546d4f4f53d | -15.2101 | -53.8086 | 2025-08-28 14:20:00 | GOES-19 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 9842e8aa-1295-3349-b9da-58c799df6b1b | -16.3606 | -43.7858 | 2025-08-28 14:20:00 | GOES-19 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 234.1 |
| 27782627-2066-35f4-a5f5-102694c36535 | -6.3973 | -44.6481 | 2025-08-28 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 9cb64568-1b2a-30fb-89fd-a371d3580449 | -15.191 | -53.79 | 2025-08-28 14:20:00 | GOES-19 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 83.6 |
| 70a035be-c02b-34bd-b503-e9a2e754f9a3 | -9.7322 | -64.9067 | 2025-08-28 14:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 21b606c9-e71d-3fc2-8fb7-f4e2d8edb8a8 | -9.4366 | -48.2955 | 2025-08-28 14:20:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 361ac8a9-8269-31ea-b51e-0018f4ecd860 | -12.6878 | -48.1677 | 2025-08-28 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 90.7 |
| 13ed8633-399e-373a-ae68-c86f8c89e692 | -9.4369 | -48.2737 | 2025-08-28 14:20:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 95.3 |
| ebe2e3e8-aa62-35c6-a329-9becb8b15349 | -11.3526 | -43.5187 | 2025-08-28 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 125.1 |
| fee2c3a2-9331-30b2-afd1-0f5d47404a10 | -7.3541 | -59.6669 | 2025-08-28 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 360bee4d-0b5e-3699-8326-43aa883a76b8 | -11.2378 | -55.0569 | 2025-08-28 14:20:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 86.5 |
| 2cf3d503-854f-3d68-935c-43fbdf0544ae | -13.0154 | -56.8982 | 2025-08-28 14:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 99.3 |
| 9db5b2b4-1280-3521-8cf7-d1dd5cd8670d | -12.9963 | -56.9 | 2025-08-28 14:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 83.6 |
| 262e96e9-2627-3282-9371-f7befaa73093 | -9.6816 | -48.3139 | 2025-08-28 14:20:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 64.7 |
| ab9fff6a-c795-32b4-862d-07ede51fb1a8 | -10.8419 | -60.8202 | 2025-08-28 14:20:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 101.8 |
| d0c044fb-144e-39d4-a3f1-eb6512b1214a | -7.6414 | -42.6718 | 2025-08-28 14:20:00 | GOES-19 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 238.8 |
| 2f66e5ba-e670-30a8-aaff-ed9f54446cfd | -12.8224 | -48.1489 | 2025-08-28 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 125.0 |
| e9943511-ca6a-3fdf-b585-c5beb27be368 | -7.0569 | -44.3623 | 2025-08-28 14:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 98.7 |
| a1871d6a-2752-328e-9bd4-8c412e38ff7d | -7.3357 | -59.6484 | 2025-08-28 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 9d983855-798c-3fb5-9cab-da51f9ae784d | -7.192 | -44.0501 | 2025-08-28 14:20:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 90.5 |
| 6bd17ee3-29ca-3801-b18e-e0a00f7387a0 | -12.8613 | -48.1213 | 2025-08-28 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 114.7 |
| 7d525d07-2704-34c3-880f-14e5a2748245 | -6.0627 | -44.3769 | 2025-08-28 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 73.0 |
| ee1cda7f-4c6d-38c0-9e63-2a82b83b545d | -10.4736 | -57.9563 | 2025-08-28 14:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 127.4 |
| 0d12b81b-352b-31d1-8e27-3b12f61d72cc | -7.6411 | -42.6955 | 2025-08-28 14:20:00 | GOES-19 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 102.7 |
| f28b3e22-d6d3-361a-83e6-fa43a1b4149d | -14.3113 | -53.2711 | 2025-08-28 14:20:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 91.2 |
| f6404495-7e3c-3e8f-8c9a-23ecef4b6417 | -7.3542 | -59.6476 | 2025-08-28 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 76.5 |
| ef892ace-2cf5-31e7-b79b-2192bec1e120 | -14.3116 | -53.2501 | 2025-08-28 14:20:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 127.8 |
| 990b8741-fef1-3c11-b444-4ad9300a647a | -9.1363 | -65.2835 | 2025-08-28 14:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 34893a01-58b2-3c93-a334-a4fd8f58282c | -15.1906 | -53.811 | 2025-08-28 14:20:00 | GOES-19 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 134.3 |
| b0377cf7-8103-3098-80a9-6e0d786d8d68 | -9.4558 | -48.2717 | 2025-08-28 14:20:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 77.4 |
| b2e30eac-4730-3cce-b569-18825b37973f | -7.6225 | -42.6738 | 2025-08-28 14:20:00 | GOES-19 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 276.1 |
| fdad1668-60b6-3879-9d0b-35f28cf312c2 | -9.2632 | -65.8959 | 2025-08-28 14:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 68.7 |
| f060f1e6-21d0-3a26-8b13-8c282f622ada | -13.4208 | -46.9864 | 2025-08-28 14:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 78.4 |
| fd038603-8b90-3bf3-b275-933fdde98ee2 | -6.178 | -44.0688 | 2025-08-28 14:20:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 115.5 |
| e119c881-ed90-3c50-aefd-c5e9bfec08d9 | -13.0863 | -46.3352 | 2025-08-28 14:20:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 99.7 |


[Clique aqui para ver as próximas entradas](README100.md)
