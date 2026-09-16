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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8a60a8f1-43c1-3918-a7c1-f4b8509240e9 | -3.76242 | -47.55207 | 2026-09-16 04:14:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e897bde7-13d2-3a7f-8300-733a4507376a | -11.25649 | -43.45398 | 2026-09-16 04:14:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| de8a4d41-0a58-3647-ba3e-7a2a83e1660d | -5.14374 | -47.60323 | 2026-09-16 04:14:00 | NOAA-20 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| fdb00b2e-b2ca-3561-ae65-d7b3c85beca4 | -6.62776 | -55.13719 | 2026-09-16 04:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 94b0966f-2fcd-3ca6-a238-8ea8c12a39f3 | -9.11069 | -45.73288 | 2026-09-16 04:14:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 10.4 |
| d1c086fe-809a-3c6a-b136-b98bd4ee2240 | -3.15311 | -49.22538 | 2026-09-16 04:14:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b3166b60-6324-3c11-9f79-5637d28d3ebf | -10.81354 | -46.17718 | 2026-09-16 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cc17c010-c557-34c4-952f-f0cbdba63a13 | -9.86897 | -49.83356 | 2026-09-16 04:14:00 | NOAA-20 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c82a036c-5303-3a12-ba4e-1fda6b21baaf | -6.81692 | -35.14603 | 2026-09-16 04:14:00 | NOAA-20 | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| b39c5841-ec49-39d5-86b9-a459665fa5ca | -7.26457 | -46.18142 | 2026-09-16 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8cf7d681-9533-3f2b-920b-bf3220f3474e | -8.85602 | -44.91122 | 2026-09-16 04:14:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fc0f9d1d-1578-3211-b1a1-e32103979d2a | -7.30104 | -42.35273 | 2026-09-16 04:14:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 05c0b336-77c2-3bb2-a9a4-100317eeb524 | -7.11134 | -41.81461 | 2026-09-16 04:14:00 | NOAA-20 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 40252cff-77a6-3a97-8af8-b02588d78300 | -11.21559 | -43.43275 | 2026-09-16 04:14:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 45762c6f-2f61-31ab-96f1-ad4feedc41ff | -9.14436 | -51.56876 | 2026-09-16 04:14:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 776876cd-c025-31ba-a46a-cd4cef9f9e0a | -8.55707 | -44.48213 | 2026-09-16 04:14:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0448992a-bab3-3785-a327-19892eae0370 | -2.90756 | -50.41767 | 2026-09-16 04:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0e674a17-9a73-3ce6-ab45-e0bc81c26dda | -6.32215 | -44.09811 | 2026-09-16 04:14:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f0ebb733-c800-31c7-a54c-6cbd20195861 | -10.8245 | -46.1791 | 2026-09-16 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 34ac3c69-d029-345d-a776-b5b04b6f442a | -7.14134 | -42.0962 | 2026-09-16 04:14:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 471b795c-8201-3b36-9ba5-94447f82d6fc | -9.47224 | -45.45589 | 2026-09-16 04:14:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 19e66e6c-f27a-3535-8024-117e53ce4a44 | -3.99879 | -44.82417 | 2026-09-16 04:14:00 | NOAA-20 | LAGO VERDE | MARANHÃO | Brasil | 2105906 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 5e1b5691-f9a8-33ed-8884-be227a9f1406 | -9.8424 | -48.35513 | 2026-09-16 04:14:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0582b025-bd90-3fe2-bb1c-ebcfb0353926 | -10.46302 | -44.94822 | 2026-09-16 04:14:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 3730b2d2-188e-36ba-bb8c-ed587f4bad3e | -8.77896 | -45.90102 | 2026-09-16 04:14:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7843bdb4-ee00-3726-9116-909acce11223 | -10.30343 | -45.32216 | 2026-09-16 04:14:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d865f349-9c11-3663-9208-0276fbbc6b21 | -5.99321 | -46.62921 | 2026-09-16 04:14:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f29531a5-5af1-31ac-afa9-67e49d0e34a5 | -7.17201 | -41.81713 | 2026-09-16 04:14:00 | NOAA-20 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 4d5337aa-9df5-3b36-91fe-f498ac9fc328 | -10.09841 | -45.61391 | 2026-09-16 04:14:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 2fd876a6-e3b7-3b4d-bd7f-6a3597eeafe9 | -7.15517 | -44.23648 | 2026-09-16 04:14:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e86c622c-7dc9-3b33-8428-e26fb531df13 | -7.82289 | -41.24236 | 2026-09-16 04:14:00 | NOAA-20 | JACOBINA DO PIAUÍ | PIAUÍ | Brasil | 2205151 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 8d1cf813-7112-388e-8095-0869489c1da6 | -11.19873 | -42.81366 | 2026-09-16 04:14:00 | NOAA-20 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 8a21e579-b419-3c49-a723-85d4c26d75ff | -10.76377 | -46.22657 | 2026-09-16 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| da6cdc18-d886-3ae1-bff8-5425f36dac24 | -9.15833 | -49.99761 | 2026-09-16 04:14:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 046a26fb-fa37-3bcd-9daa-b482b44ca1e3 | -6.92828 | -44.97104 | 2026-09-16 04:14:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1b1f4b2f-65fc-3904-a3a3-f9b8dd38c8b9 | -9.10776 | -45.72802 | 2026-09-16 04:14:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 2304cac6-0f8a-339f-9cf4-75fff3ef4589 | -9.70239 | -52.02035 | 2026-09-16 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 6c252a96-9f8a-3c2a-af5b-22334b108048 | -9.54728 | -45.41676 | 2026-09-16 04:14:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| bfbf183e-23b2-3190-a843-1ccfe1f67bb3 | -7.04077 | -42.04435 | 2026-09-16 04:14:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 867e0a4c-dd68-3b5a-8535-eaf6e41b6150 | -2.90638 | -50.42474 | 2026-09-16 04:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 53769673-4d22-3757-9689-860c0e041ef3 | -9.78724 | -46.48541 | 2026-09-16 04:14:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9279c6df-d068-3e85-9ca4-0df9a2ee9716 | -7.73323 | -44.70888 | 2026-09-16 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 96f11bf5-2421-3585-bfd6-f8b3893b9129 | -10.41841 | -48.6572 | 2026-09-16 04:14:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 24cdf10f-f70a-3f0d-a031-fdcafbfcd460 | -10.10604 | -45.56857 | 2026-09-16 04:14:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b0b9c025-6696-3f2d-926d-c92e2ef219bb | -10.75768 | -44.81838 | 2026-09-16 04:14:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5014ab61-1d1b-314c-a456-11e45de5ecb0 | -9.23435 | -46.69518 | 2026-09-16 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7717536f-0354-3e42-811e-9e22cfbaf7e3 | -7.08344 | -42.09763 | 2026-09-16 04:14:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 20fbbe0c-01a2-3a7a-9e76-37cb881bfe60 | -8.28042 | -45.65427 | 2026-09-16 04:14:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1055f3d2-c1dd-3287-b114-cf6fb0035704 | -10.60749 | -47.76132 | 2026-09-16 04:14:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7d94c4ef-b67e-3b7e-af2a-f18fbcbcbc29 | -5.6354 | -51.67575 | 2026-09-16 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d933b5a1-aa58-3287-9b48-055c275e7f50 | -10.75424 | -44.81781 | 2026-09-16 04:14:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3456ef7a-3dc0-3d17-8f1a-a1a34bf77dd9 | -9.36488 | -50.26781 | 2026-09-16 04:14:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 267a5439-0822-397d-be3c-01f97e7d5dbf | -7.07533 | -41.82629 | 2026-09-16 04:14:00 | NOAA-20 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b9a14bc8-7ab2-3a15-a0a5-9478ec142b70 | -2.89059 | -50.41842 | 2026-09-16 04:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 40b7f2b6-42d8-393a-9597-f856de7ef635 | -5.49591 | -43.67855 | 2026-09-16 04:14:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ce9e47a7-bc08-3026-88c1-d7d5e81fbb20 | -2.90875 | -50.4106 | 2026-09-16 04:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fb63459b-d1fb-3377-bc1c-769301662064 | -4.3439 | -46.61358 | 2026-09-16 04:14:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 0e9770ff-433b-3332-8424-1940726aad44 | -3.07905 | -50.57583 | 2026-09-16 04:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bc00e5f8-c9f0-389c-b0dd-d4a91d5d7623 | -3.02055 | -51.3417 | 2026-09-16 04:14:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| dfe741b0-0804-36b2-a50e-a4dff9eff36e | -2.89545 | -50.42287 | 2026-09-16 04:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 618e1067-5396-3c7a-83a5-86faca3ce959 | -5.29697 | -42.71315 | 2026-09-16 04:14:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| cc240f26-41fe-31bc-9b98-096b21e97df4 | -7.1342 | -42.14124 | 2026-09-16 04:14:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| af6cd231-8850-3bf6-89de-41b5deaa96b1 | -11.24257 | -43.47706 | 2026-09-16 04:14:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3a077bf7-33f1-36ec-b6f5-34bffd419f1d | -7.72906 | -44.7122 | 2026-09-16 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0f903227-1e08-3784-b4e0-fc837710bd5f | -7.11818 | -42.09251 | 2026-09-16 04:14:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| dbe207bb-171f-35e5-acb4-2a8ffd44cf0f | -4.67866 | -40.1359 | 2026-09-16 04:14:00 | NOAA-20 | CATUNDA | CEARÁ | Brasil | 2303659 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a112d9dd-b5c1-3426-82b4-eb52ada9c921 | -3.99647 | -44.82525 | 2026-09-16 04:14:00 | NOAA-20 | LAGO VERDE | MARANHÃO | Brasil | 2105906 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 94aa21e1-0da0-3df5-a69a-0bef20ced025 | -6.65542 | -43.64661 | 2026-09-16 04:14:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 914dbbc2-f04d-34fd-9ec2-6637656b9c61 | -6.37263 | -55.83076 | 2026-09-16 04:14:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 20e39d04-1a8c-31a8-8311-23e6d44ada01 | -5.1236 | -47.61687 | 2026-09-16 04:14:00 | NOAA-20 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 10.1 |
| a9788840-b825-3862-be40-315c8f15a239 | -7.51233 | -47.56846 | 2026-09-16 04:14:00 | NOAA-20 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3554c71d-e546-38f8-9e9d-23c68f836466 | -2.91538 | -50.40446 | 2026-09-16 04:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e921c6d3-f0bd-3de5-8a56-ed223eaafd3b | -7.51716 | -47.56535 | 2026-09-16 04:14:00 | NOAA-20 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5c2d0d43-d774-3002-933a-ca2cbc4c32bc | -10.60287 | -47.76403 | 2026-09-16 04:14:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6c6a790f-0fbb-3922-8efa-c35901db34b6 | -11.82698 | -37.5756 | 2026-09-16 04:14:00 | NOAA-20 | CONDE | BAHIA | Brasil | 2908606 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 2dafe470-fa39-3808-8aa1-47a4ee861eac | -8.38258 | -42.21648 | 2026-09-16 04:14:00 | NOAA-20 | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| c606dec6-84ba-3c6a-9bb5-a1e196fd7f0b | -2.9002 | -50.39468 | 2026-09-16 04:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f34262d0-5621-3780-adda-48fdba9449fa | -2.89367 | -50.43346 | 2026-09-16 04:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cab1e43f-1fcd-3f1c-a473-d21179baebde | -9.70777 | -52.02151 | 2026-09-16 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2bc458fc-f086-3246-b2bb-84a8f05b5898 | -5.14336 | -45.76875 | 2026-09-16 04:14:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c267e57b-df05-3f5d-a7f9-829f6cdbcc5b | -9.80051 | -46.49996 | 2026-09-16 04:14:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c44d03fe-2078-32c8-95eb-56e8318d95af | -8.21217 | -43.78168 | 2026-09-16 04:14:00 | NOAA-20 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 718d5994-af62-32e2-9af2-6c3a1dd56ff6 | -7.11189 | -41.81115 | 2026-09-16 04:14:00 | NOAA-20 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 42b94e27-981b-3235-b3e3-f3172fb94c79 | -9.09975 | -45.73106 | 2026-09-16 04:14:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a39bd93e-2194-3496-8f6a-464e98d5e33c | -2.90151 | -50.42025 | 2026-09-16 04:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0944e65e-bd75-3890-91c2-118148bc02cf | -7.13695 | -42.12391 | 2026-09-16 04:14:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 1f1b7fb9-02ad-39ca-bf46-c3c427c8d4bf | -10.5881 | -47.75371 | 2026-09-16 04:14:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1073f030-5288-3f14-8610-49c9721826d6 | -4.72701 | -46.13108 | 2026-09-16 04:14:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5d651b30-a172-309b-bee6-0cdf204caff3 | -8.95321 | -44.40179 | 2026-09-16 04:14:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cec15916-19b6-3390-81cc-46990aecdb8f | -3.3785 | -50.84624 | 2026-09-16 04:14:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 6b9aff3c-018b-300a-a466-9ae9c410076a | -9.7633 | -46.5815 | 2026-09-16 04:14:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| df94ed14-9062-3bec-b824-578175a0340d | -8.03227 | -45.54486 | 2026-09-16 04:14:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 132e61c9-306a-351e-80a0-744aa360a0dc | -5.98692 | -44.83691 | 2026-09-16 04:14:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3afcf284-e833-3c50-8fe7-f145b4b5c172 | -6.77976 | -48.65506 | 2026-09-16 04:14:00 | NOAA-20 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a72c5ef3-478a-39ec-a2d0-09f02723828d | -2.91479 | -50.40799 | 2026-09-16 04:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a90b09a1-9c93-323a-8952-9e3562d09edc | -11.25155 | -43.4423 | 2026-09-16 04:14:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7cabf048-fb4a-3b0b-95de-1234f738fe2d | -9.85008 | -48.36106 | 2026-09-16 04:14:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dec3b3b4-cc0b-3f9e-ab34-c92112cec518 | -8.36637 | -54.72777 | 2026-09-16 04:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| de086852-771d-3d2b-b20b-67c2536b3d39 | -5.11995 | -47.61192 | 2026-09-16 04:14:00 | NOAA-20 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 0a694747-d43c-37d7-9eb9-2c22e6ee66af | -7.17907 | -43.5111 | 2026-09-16 04:14:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |


[Clique aqui para ver as próximas entradas](README25.md)
