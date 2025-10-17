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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| be1d3d13-5ffd-3e02-a908-6bcb743f3354 | -6.60398 | -42.06849 | 2025-10-17 04:19:00 | NOAA-21 | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| cb98fc54-da0a-3496-945d-7a7038625ff2 | -9.10192 | -48.91279 | 2025-10-17 04:19:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 11f828b1-5e89-3a2c-b49c-6a5b21b9349e | -6.99077 | -39.23201 | 2025-10-17 04:19:00 | NOAA-21 | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 6b3972bb-0943-3b43-be39-3919e752237f | -10.10803 | -44.62769 | 2025-10-17 04:19:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e6b346da-db8b-3880-a62f-2674e2d58dc7 | -10.26737 | -44.05214 | 2025-10-17 04:19:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6a115060-8c70-3824-83be-57d016e74cbc | -7.50964 | -46.87636 | 2025-10-17 04:19:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cbcb3e64-4395-3acf-a3f6-71f8f51ec77c | -6.88003 | -44.69178 | 2025-10-17 04:19:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 074db40d-ad25-3fe8-bd39-689cee8de83a | -6.74577 | -44.37331 | 2025-10-17 04:19:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b220d3eb-4f21-38bf-91e7-bf42a0d82fd9 | -7.48364 | -44.65969 | 2025-10-17 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f74de0a6-5efc-30c0-8edd-add0b6f95678 | -5.41473 | -44.24802 | 2025-10-17 04:19:00 | NOAA-21 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4d4a28c3-7973-3f45-a573-a6e8e2941f85 | -10.16242 | -44.5384 | 2025-10-17 04:19:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e1400bbd-c04f-3bea-a9f6-e3dfb67b73ac | -7.96342 | -44.09049 | 2025-10-17 04:19:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 067c6a6a-6e08-337c-a789-9e5803015bfc | -10.28694 | -44.03668 | 2025-10-17 04:19:00 | NOAA-21 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 3a357afe-87c6-382e-9a42-df842dfcd71b | -10.17863 | -44.78662 | 2025-10-17 04:19:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 590c38cc-a817-3ca9-bc5a-0a9661fc0c08 | -7.94811 | -44.14581 | 2025-10-17 04:19:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a248f9ef-61be-3694-b8d9-9d429bc39559 | -5.59138 | -44.74814 | 2025-10-17 04:19:00 | NOAA-21 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8fd3c4bd-eb4c-367b-9af1-6fca2d29aa90 | -9.15301 | -46.62959 | 2025-10-17 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0bb19f9a-13a2-38d6-87fb-6eb52c799f9c | -9.71449 | -44.55518 | 2025-10-17 04:19:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6d7412f8-a9ee-392e-a33a-84af52d7cf55 | -7.18339 | -42.375 | 2025-10-17 04:19:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| dd56b32d-c3cb-35c0-b03d-b1c9fa61176a | -10.65168 | -45.24599 | 2025-10-17 04:19:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 52b3efbd-daf8-312f-8e81-727a55f1592d | -10.29595 | -44.04542 | 2025-10-17 04:19:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 0b07759f-7a24-3a9a-b810-34c245836fa9 | -5.21202 | -46.19455 | 2025-10-17 04:19:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 11e12768-a166-390e-8c43-7c431dde6999 | -8.18762 | -43.95902 | 2025-10-17 04:19:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d4080f77-486f-3cf1-8c5e-e30c905321d6 | -4.24903 | -48.55813 | 2025-10-17 04:19:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| edcab764-ed2d-3e61-844c-ebd484471b8d | -6.59182 | -47.07275 | 2025-10-17 04:19:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 6e476a3d-26b3-32f9-8d38-1257e3a73b5a | -6.45133 | -43.88308 | 2025-10-17 04:19:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6c9912d6-7e9b-37a1-bccf-0cdb21b33049 | -6.25978 | -44.50156 | 2025-10-17 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a28b9cf7-38d3-3f17-805b-fca74391dcc0 | -8.45038 | -46.23812 | 2025-10-17 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ef413900-33da-3383-9653-1a6865b7b0f9 | -9.14178 | -46.64244 | 2025-10-17 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 222f2825-27f8-346b-9983-0574a24c5d7f | -10.01419 | -45.64664 | 2025-10-17 04:19:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e37ee86e-0b7c-3ccc-b100-3e742b173877 | -8.62884 | -45.69063 | 2025-10-17 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5f3f6def-ea17-355a-8ac1-41c39309769e | -6.07559 | -41.9161 | 2025-10-17 04:19:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 194726dd-3e3f-3d85-9bd7-63a3af5cfeb8 | -11.44702 | -44.18329 | 2025-10-17 04:19:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 07db0134-5622-3ca5-aba3-5183b7e64519 | -6.76123 | -42.36137 | 2025-10-17 04:19:00 | NOAA-21 | CAJAZEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202075 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 92fd996c-210b-305a-9d21-6be1122b036e | -5.88069 | -43.92182 | 2025-10-17 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 00b2721b-2e12-3771-9b8b-f74b425e2b95 | -10.26117 | -44.04758 | 2025-10-17 04:19:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 1601b72a-a6f5-3b7f-96a8-aa0c1220099f | -8.41636 | -46.28004 | 2025-10-17 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c9813660-bcf5-3a60-bb7c-52afbf789935 | -4.96607 | -44.96004 | 2025-10-17 04:19:00 | NOAA-21 | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b6aa16e2-fa34-35f8-aa18-82632554e6b6 | -10.9637 | -47.38051 | 2025-10-17 04:19:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8e0292c0-6356-3676-90da-64a6b794b36d | -10.2853 | -44.04744 | 2025-10-17 04:19:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a6a4231b-efd3-3b49-8c8c-d9118518b769 | -10.27629 | -44.03875 | 2025-10-17 04:19:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4a558c07-13de-36e4-9a03-b4cfcd09774d | -6.40455 | -47.21453 | 2025-10-17 04:19:00 | NOAA-21 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fb79001c-c66d-3b2f-b43a-41d2dea7800e | -5.07527 | -40.96531 | 2025-10-17 04:19:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| b96ccfab-d61b-38a0-bc36-c9320442e15c | -6.31614 | -45.52737 | 2025-10-17 04:19:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fb61f322-12c6-32c7-a47a-8a1ab784e5c6 | -10.29932 | -44.04588 | 2025-10-17 04:19:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c2b4ef35-7f2c-3b6e-a84e-8d6cddbd2e58 | -9.62162 | -49.12334 | 2025-10-17 04:19:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 680e9fc8-261d-38ce-b06c-aa16b4d08d98 | -5.22844 | -43.38828 | 2025-10-17 04:19:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6a8548ec-df5a-376b-8eca-546a5df116f3 | -10.52563 | -43.36451 | 2025-10-17 04:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d221f92b-b1bd-379e-a8b2-175f1298fb52 | -7.61422 | -47.83876 | 2025-10-17 04:19:00 | NOAA-21 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5e0ea4ee-80d9-35dd-b23e-6e70cd4a0420 | -5.47737 | -44.67326 | 2025-10-17 04:19:00 | NOAA-21 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 76a50069-4bf4-383c-ba68-0cd9a19fed86 | -3.65844 | -50.26576 | 2025-10-17 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 236fb8fa-d536-382c-a5cd-7ce5b0be3f86 | -7.00555 | -39.8955 | 2025-10-17 04:19:00 | NOAA-21 | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 7a32bea8-50b2-3132-b4d6-0c3e95b0bd83 | -10.49462 | -43.40653 | 2025-10-17 04:19:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 15e11feb-7ef8-3ab6-bbaf-343ebf658a80 | -10.1163 | -44.61814 | 2025-10-17 04:19:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5f44eaf5-d077-3ded-96c4-bc4c00558a76 | -9.65506 | -48.72325 | 2025-10-17 04:19:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ba10ac25-b1cb-324a-84b2-dd3071c42ab1 | -8.39764 | -46.22577 | 2025-10-17 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 73d73aff-24f0-35dd-b1d8-f0492ed95e28 | -6.20715 | -41.76686 | 2025-10-17 04:19:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 348475f2-7961-3475-a07b-a1cdd051bdab | -8.30074 | -43.39828 | 2025-10-17 04:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 26629a3e-32e5-3b2b-8a9c-839a1502be94 | -6.13033 | -41.74886 | 2025-10-17 04:19:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 8c67d89b-0f4a-3484-b58c-cb28007afdcb | -11.48925 | -44.17857 | 2025-10-17 04:19:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2ed89232-c7b2-3e82-ae5a-87e7bfc539bf | -11.40269 | -44.22526 | 2025-10-17 04:19:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| b251a27f-fc5e-3a2b-99b8-0b179df89d6a | -6.08656 | -42.39074 | 2025-10-17 04:19:00 | NOAA-21 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 58345f89-be3e-3cec-9d8e-0a341d6f0b04 | -7.45679 | -42.67398 | 2025-10-17 04:19:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 1a1d04ce-2ef6-359d-8648-b54eab6cfed8 | -11.37838 | -44.19201 | 2025-10-17 04:19:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 45337ce2-6d07-3f65-81a7-f123c3dbbb4a | -5.88561 | -43.91196 | 2025-10-17 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d55a793e-bb68-3635-9dec-c685bd1039a0 | -5.89106 | -43.89856 | 2025-10-17 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3c47a3a4-dc8c-3c3d-b7f6-f5aae11f7b3a | -6.21568 | -41.54528 | 2025-10-17 04:19:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 2fdae937-7e66-3553-a26e-c7576b233cf5 | -8.3393 | -46.23075 | 2025-10-17 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| faebfb04-25fa-307b-ae6a-d1f49ec4ddd0 | -6.37794 | -41.47063 | 2025-10-17 04:19:00 | NOAA-21 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 6edcd704-b69b-3dfa-a4cf-84bedeac4496 | -8.46096 | -44.17159 | 2025-10-17 04:19:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 2ab3bb34-60a5-3d69-91be-2282c7b9677c | -7.28975 | -42.31942 | 2025-10-17 04:19:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 46508120-eadd-3571-ab12-c1e2a0f7c768 | -7.47743 | -46.90195 | 2025-10-17 04:19:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cd5cddd4-e2d0-3f4b-9bf9-7a78033ea6fb | -10.80753 | -44.30191 | 2025-10-17 04:19:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 366b1981-c47b-330e-a952-097eef5cdd70 | -6.28278 | -42.96618 | 2025-10-17 04:19:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8d1c668b-0da8-34fe-af88-6dc3a385d00c | -4.93125 | -41.53365 | 2025-10-17 04:19:00 | NOAA-21 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 6cbffd9d-53e3-3c32-a076-5bc82f2765d8 | -5.16386 | -45.21576 | 2025-10-17 04:19:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1724777a-28a4-342b-85cb-9ccc0a4de8f4 | -5.44303 | -44.1749 | 2025-10-17 04:19:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 90fa26a9-32ac-3ca2-990d-186f7d1de240 | -5.25329 | -44.21151 | 2025-10-17 04:19:00 | NOAA-21 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 498ead93-c64c-39b9-8ae6-bb5251ba791f | -6.43878 | -43.92035 | 2025-10-17 04:19:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 16db01f9-c446-3a2f-a512-b5b8e1aeeeee | -5.47985 | -48.65145 | 2025-10-17 04:19:00 | NOAA-21 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ca7606a7-2ff4-35b9-bc7b-89d7599934b3 | -10.60206 | -47.40101 | 2025-10-17 04:19:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dc81b197-7385-3855-ae8b-7528973b7a7b | -5.38346 | -42.80724 | 2025-10-17 04:19:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 0ce7a1ed-bdc0-3e96-8b22-38e5ad3b946f | -9.89339 | -47.672 | 2025-10-17 04:19:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1d448891-9950-314e-b1c8-81f69ec7bc3e | -7.17412 | -42.36572 | 2025-10-17 04:19:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| c028d7ec-29e5-386b-9ad1-4a8527dcbb79 | -11.32892 | -44.93596 | 2025-10-17 04:19:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| eacb096b-40da-3112-b3f3-b43fe66f336e | -10.36312 | -47.7245 | 2025-10-17 04:19:00 | NOAA-21 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d0f8c165-f55c-3c09-938e-386c1d534df2 | -8.24663 | -44.01893 | 2025-10-17 04:19:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| acc0ddb5-7af5-3173-83b9-a85e6cdc5652 | -5.53306 | -44.0795 | 2025-10-17 04:19:00 | NOAA-21 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d9c362f2-ace4-3b30-ac03-793b748f7460 | -7.95143 | -44.14632 | 2025-10-17 04:19:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 834eb49d-379d-36a7-82e1-1415fbc938a0 | -6.3532 | -41.51361 | 2025-10-17 04:19:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 36d0256a-6896-3e09-b8a8-8e64235554ca | -5.17191 | -42.65598 | 2025-10-17 04:19:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| abe3c0ae-a98c-37c0-bbec-7a676ca9bf80 | -6.01031 | -46.62784 | 2025-10-17 04:19:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3f95f0e4-3a0a-386d-8d6f-1e97b95817b2 | -10.14578 | -44.53591 | 2025-10-17 04:19:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 2b0a0570-c6e5-3128-8781-945e84c1261e | -11.47687 | -44.19171 | 2025-10-17 04:19:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d6523ed5-c0e8-34b8-9216-48fab46ad1e5 | -7.45954 | -42.15731 | 2025-10-17 04:19:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 1fb8b35a-bb83-3954-8a24-7f2d63a3d63a | -3.2681 | -53.25439 | 2025-10-17 04:19:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 500fa235-ba15-31ee-84a6-88fdb8b94393 | -10.57486 | -44.53046 | 2025-10-17 04:19:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 968272b0-04ba-30a3-84ea-6fce75896e24 | -9.23884 | -45.27299 | 2025-10-17 04:19:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6b362a4e-357a-3334-83b6-39fbb0c44181 | -6.48737 | -43.18612 | 2025-10-17 04:19:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| def8896e-46e5-3fb2-b7b9-61b4bcba3e99 | -5.84574 | -47.03613 | 2025-10-17 04:19:00 | NOAA-21 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |


[Clique aqui para ver as próximas entradas](README43.md)
