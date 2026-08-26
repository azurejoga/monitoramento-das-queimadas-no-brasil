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
| ad3fa19f-6d3e-3122-b2b8-70a47ef3d874 | -4.05684 | -50.34322 | 2026-08-26 04:51:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4ed912bd-a82e-318d-bd4f-b8f17e242172 | -6.14799 | -57.69937 | 2026-08-26 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 135aa90d-d198-3ea1-986e-c00f74cdf18b | -6.30289 | -53.56845 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0b785f02-5741-355d-a29e-990bce768cdd | -6.62884 | -58.51658 | 2026-08-26 04:51:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| fee2ff3c-a5a6-39b4-a22b-f6f8a5d04658 | -6.29791 | -53.57846 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4722f1b9-4235-39e6-a5c5-1cd9252f7cd1 | -8.64805 | -54.75365 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3cdf9648-753e-34bd-87d1-35573435c51c | -6.00589 | -57.85044 | 2026-08-26 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 699aa40d-33ef-3fe8-89ce-3aa48cd794a3 | -8.86416 | -49.71871 | 2026-08-26 04:51:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 82623114-373d-3256-a1f7-19f9e9d73878 | -9.17406 | -49.9748 | 2026-08-26 04:51:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 714f997e-7401-3e6e-be44-83c574ca39bb | -7.5209 | -61.3907 | 2026-08-26 04:51:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 638c9a0d-9bff-3454-988f-4c5f9439fea3 | -9.30663 | -50.29109 | 2026-08-26 04:51:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 226e5ce5-5d81-3cad-aab8-cf4f2307eae8 | -6.77277 | -59.44125 | 2026-08-26 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f8cccaf2-3634-3700-bc5e-7e1800a0abf4 | -3.53337 | -48.17854 | 2026-08-26 04:51:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 7ca8b5a3-0dcb-3b5c-858b-d32adaa49a1d | -5.74365 | -43.27668 | 2026-08-26 04:51:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dcb2c565-783d-3817-b373-eacf3344f1b4 | -7.13951 | -42.76434 | 2026-08-26 04:51:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e14b3b5a-bd97-3ed7-b327-353824dca574 | -8.14959 | -47.51304 | 2026-08-26 04:51:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 28.0 |
| d25561c5-b4d4-3bc5-ac32-09383978f00e | -6.44126 | -54.97448 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f5d67680-12cb-33d2-ad58-e92b1ec9de34 | -8.9923 | -52.39143 | 2026-08-26 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1b59dd22-26a7-3336-a127-d72a16457853 | -5.92913 | -44.97651 | 2026-08-26 04:51:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 83d74542-4678-3670-82e0-eb618534940d | -6.63351 | -58.48917 | 2026-08-26 04:51:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cd1d4a89-3edc-3751-9f6f-85c5bcec14be | -4.89141 | -56.26857 | 2026-08-26 04:51:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 798b1c19-e529-3050-8c48-785b2a62031a | -6.80773 | -58.6138 | 2026-08-26 04:51:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f82b79df-b3c6-3b1a-a116-88551daa8f12 | -7.03064 | -59.23417 | 2026-08-26 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9139f2c1-30cf-3b2f-aea3-1b5e87991a32 | -8.63598 | -54.75505 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f59cd806-a7f1-311c-b0c8-0440bb267807 | -8.10708 | -51.6708 | 2026-08-26 04:51:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1ae68aef-f7a4-3fef-aaab-5ea0a1ccd42f | -3.13142 | -61.19317 | 2026-08-26 04:51:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| ec5a9680-bc34-32b9-b6be-74e276acdd4a | -6.18069 | -57.70137 | 2026-08-26 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7315c8f7-98a9-3138-af9c-3fe53c78f9a4 | -9.30602 | -50.29524 | 2026-08-26 04:51:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4d9f226d-10e5-34a5-b2fa-7a2c374b06ab | -8.01785 | -51.80479 | 2026-08-26 04:51:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c9f45b6c-9fcb-3e31-af96-a27912d064e8 | -9.44657 | -51.66725 | 2026-08-26 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4a260a94-d51b-3a38-a65c-a186a6c35f89 | -7.28369 | -45.3573 | 2026-08-26 04:51:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| cea1b65d-29ef-3e32-b555-d02e5a1a7afb | -6.53852 | -56.26072 | 2026-08-26 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d7dd9fc3-4a04-33f7-88eb-9af7fb4c71ce | -6.98572 | -59.28566 | 2026-08-26 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ff74e1ed-764a-3215-82f5-ceb6678b0ff0 | -9.62652 | -48.29657 | 2026-08-26 04:51:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 85e7f033-0d1e-3f82-8f0d-01d41a61e9f1 | -9.56742 | -49.28056 | 2026-08-26 04:51:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ece57c0d-5b25-3a9c-9eee-45bc4b02c619 | -7.29279 | -44.08165 | 2026-08-26 04:51:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7d7da383-05f6-3900-b1af-fea417e76188 | -6.13078 | -57.85342 | 2026-08-26 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 17cd3a6b-2e41-37c8-a020-fff328f7c269 | -9.45273 | -51.58101 | 2026-08-26 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7e978657-6a7f-3a50-8722-1f0e0c4b1da9 | -8.13812 | -47.5035 | 2026-08-26 04:51:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 599207d4-a263-3883-976c-034261ca721b | -9.17283 | -49.98339 | 2026-08-26 04:51:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 29ac29da-12ad-3948-826e-dfced01bbaeb | -3.09857 | -61.22593 | 2026-08-26 04:51:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 211e2435-9617-3005-8c59-bd3d970fc499 | -7.3731 | -55.19088 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 787f8e15-4164-36fe-8454-3596bebcbf37 | -7.75679 | -44.74427 | 2026-08-26 04:51:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c0575507-002a-3b19-9010-8939e175c7c0 | -7.12202 | -42.79221 | 2026-08-26 04:51:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 3d7e2ecf-ad53-36f9-ac9f-ddb414749cfb | -7.39503 | -55.15867 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| eb098706-4059-31b4-9bb9-585290058494 | -7.01202 | -59.23687 | 2026-08-26 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a9654e62-8f82-35f5-8516-271145bf54ee | -6.24124 | -44.80158 | 2026-08-26 04:51:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b2e36cd6-25ae-335f-8718-a6f03c68234d | -8.60183 | -54.70866 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6956dd4a-3ed2-34c5-98a4-775c1777e220 | -7.2827 | -44.08239 | 2026-08-26 04:51:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d676e0b9-f71d-32e2-84d1-4c1560744305 | -6.99232 | -59.27342 | 2026-08-26 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5fea362b-4f9c-3fc9-b244-3a8d2f6773e7 | -6.63572 | -58.50155 | 2026-08-26 04:51:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 509818e4-93e8-3d70-b91a-12bc741bad79 | -7.02879 | -56.61645 | 2026-08-26 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 48f0d1bd-ba2b-35ac-9e8d-eb99f8c45bae | -6.12456 | -57.81558 | 2026-08-26 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 82caa02c-fbfc-3793-a9d0-d683882fd6ef | -4.95021 | -43.1959 | 2026-08-26 04:51:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ce12c4f3-f78c-3c5f-8f5f-b9e679bab2ff | -6.12453 | -53.74958 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eaaa59b3-b64c-3442-b48d-648268c7b8a2 | -6.91443 | -44.66392 | 2026-08-26 04:51:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fc686ef9-667c-3175-89a8-c7d6a323f695 | -7.77906 | -61.56679 | 2026-08-26 04:51:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| acb4b8e6-5ee3-32d6-ba0f-e8c12fedda88 | -6.78559 | -59.74366 | 2026-08-26 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 82fc61e8-011d-3026-aabb-370a09c75254 | -7.06648 | -59.23577 | 2026-08-26 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 00cd3724-61e2-32bd-a4d2-66e5298a6a61 | -6.14509 | -59.92748 | 2026-08-26 04:51:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 0fa1cdce-1253-3c6b-a1da-5468ad5e443c | -5.5664 | -50.49173 | 2026-08-26 04:51:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b1764409-fb03-3de3-8f9e-262b9762d650 | -5.95397 | -53.58128 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b5c191c2-83cd-34e6-80d8-b0f71bd2c022 | -9.59259 | -46.0153 | 2026-08-26 04:51:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| eee72ac1-4e98-31bc-af0b-7f01b1885853 | -6.88056 | -56.50733 | 2026-08-26 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f4dca524-6c97-3dc3-8de0-fb1c75e3b2bf | -3.1093 | -61.22767 | 2026-08-26 04:51:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6c19018c-8a12-3c0d-9da3-e54e52967142 | -6.26504 | -53.3764 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| ad39b833-a36a-3df9-8e3c-9f76e7a42a39 | -6.77876 | -59.43327 | 2026-08-26 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a31ed1b1-c5be-371f-8714-2412cc30704c | -6.14846 | -53.81498 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4c1d732f-2493-3897-bc96-c796100dbb16 | -6.62509 | -58.48786 | 2026-08-26 04:51:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| e4123ba7-e55e-31e5-991c-946bb78a1def | -5.49226 | -49.10373 | 2026-08-26 04:51:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a9e505aa-63ee-3415-a208-435655bbce38 | -7.50137 | -55.34909 | 2026-08-26 04:51:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5c2ed7af-b29c-3f73-9fda-dd2bd225a251 | -8.59451 | -54.71117 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7888ee1c-6051-3492-81bf-004fb1407ca5 | -7.13609 | -43.18156 | 2026-08-26 04:51:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| cb671518-7d61-356d-beb0-f2d140817816 | -5.97054 | -57.63298 | 2026-08-26 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5b7dbe67-8f60-38a9-a921-55b3c7917341 | -7.0621 | -59.23504 | 2026-08-26 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 194c857a-7a1d-3e6e-b293-bfaf061c0a2b | -8.56908 | -55.28315 | 2026-08-26 04:51:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9d1e3bc9-c093-372d-be36-a40e5bb046a3 | -3.12998 | -61.1897 | 2026-08-26 04:51:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a31404fe-706d-328e-914c-d2ed16392bdd | -7.09931 | -55.45347 | 2026-08-26 04:51:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ab3610c7-b8fe-3156-aaeb-4b21fa248ad5 | -7.0285 | -59.22057 | 2026-08-26 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 94f9ed30-111d-380e-ac30-c78856aef56a | -10.02787 | -46.42041 | 2026-08-26 04:51:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4f6f8303-25ec-3bdf-b933-32ed6b98c6a5 | -7.5238 | -61.37923 | 2026-08-26 04:51:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 21.1 |
| 0a5c2374-d18d-3b33-ad02-a531e04ebeab | -7.40194 | -55.15975 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 592c0a5e-b6a8-34ba-b8ab-c79ca8276e88 | -7.39316 | -55.17019 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 533fb491-a38f-31d3-a60c-68ba08970345 | -8.06898 | -47.52993 | 2026-08-26 04:51:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| fafcc092-793d-38d8-97be-ab44a518102f | -8.5156 | -55.35562 | 2026-08-26 04:51:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ba702d04-be5d-34bc-a625-fde06acaad20 | -6.6532 | -58.50044 | 2026-08-26 04:51:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 18.2 |
| a0e9e5b9-a3e6-3f16-afec-895d95564e7e | -6.61577 | -58.38293 | 2026-08-26 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 71ca723f-c181-35bf-accb-27cf856d0da8 | -6.25786 | -53.37885 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 81390ae6-4778-3172-b874-e38706bc24e3 | -8.95114 | -50.71339 | 2026-08-26 04:51:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 95bf6a6e-6ddd-3c26-b9d0-e69101d90e61 | -8.01676 | -51.81208 | 2026-08-26 04:51:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ec74fb23-acaa-3968-8245-4d4ff46eadfc | -7.86244 | -46.10764 | 2026-08-26 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| d462f633-e652-38c8-8643-3ff53717130d | -8.01474 | -51.81132 | 2026-08-26 04:51:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 19fdf095-5144-3626-97c3-f931a69f16ed | -9.17344 | -49.97909 | 2026-08-26 04:51:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fb84c7f6-0c18-37b5-8d0a-9811ee3746c6 | -8.22406 | -55.00589 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 34e9e6e3-ca44-3b25-8f95-2a460668901a | -6.15515 | -53.68572 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9635fda7-f039-3d8b-b6fc-3c1308f2370b | -7.38503 | -55.17658 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9d8e795c-a43b-3d85-9142-66c2af6efb01 | -7.19909 | -42.75302 | 2026-08-26 04:51:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| c3367475-4d7c-3b81-9f68-13196b63d806 | -6.26339 | -53.38685 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1d476b20-04b5-3f8a-b9f3-95c8ce818f75 | -8.29879 | -55.10942 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cbaff8a4-2351-338d-8ed6-0a34f07bbfab | -6.18013 | -57.7048 | 2026-08-26 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |


[Clique aqui para ver as próximas entradas](README40.md)
