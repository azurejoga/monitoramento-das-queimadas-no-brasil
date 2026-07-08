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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e3fb34a8-8a74-31c3-886c-5e8a022151a1 | -5.66733 | -44.30574 | 2026-07-08 03:30:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| dd52f006-b19e-37f3-9755-2edd86140474 | -5.98486 | -43.61809 | 2026-07-08 03:30:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9149c356-e5d3-3102-ada9-3c3023d0e1d0 | -8.04504 | -37.73429 | 2026-07-08 03:30:00 | NOAA-21 | CUSTÓDIA | PERNAMBUCO | Brasil | 2605103 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 0a55d92d-0e4d-33e0-835f-a996e96c7e4a | -6.64366 | -43.91423 | 2026-07-08 03:30:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ed87ca7e-8c63-374f-85a4-a0814fe102ff | -6.92338 | -43.69953 | 2026-07-08 03:30:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5b7aed12-2aa2-325d-aa3c-4b19f056b74c | -6.49505 | -42.22281 | 2026-07-08 03:30:00 | NOAA-21 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 11.5 |
| c0e37bd3-a679-3c3d-a7e9-c777a939035b | -6.9404 | -43.70235 | 2026-07-08 03:30:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 2998b288-dbd8-3e2e-929a-7c51b37328ad | -6.50077 | -42.22374 | 2026-07-08 03:30:00 | NOAA-21 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 11.5 |
| c48dce35-73be-32be-b50d-113dafdeed1e | -6.49006 | -42.21785 | 2026-07-08 03:30:00 | NOAA-21 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 260c1202-e390-39f9-a628-5df125cf0265 | -7.01045 | -42.7807 | 2026-07-08 03:30:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 9ab3a165-4115-3224-b365-0a9819827443 | -6.64458 | -43.90918 | 2026-07-08 03:30:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c8166a76-6532-3912-a33c-789c45e8035c | -7.01206 | -42.77821 | 2026-07-08 03:30:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| eeca2b31-d2fa-3ee9-8e64-155aee31a856 | -5.66176 | -44.2991 | 2026-07-08 03:30:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 40d73494-0bc4-35a4-b432-ba183204a7ae | -5.30609 | -43.06469 | 2026-07-08 03:30:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1d60a786-7457-33cf-9ff2-83c054209599 | -5.66808 | -44.30996 | 2026-07-08 03:30:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| a36eb557-b942-3562-846f-af7b67fb0b93 | -7.01125 | -42.77636 | 2026-07-08 03:30:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 8e5d8e96-ae73-37e6-a330-35734aa0e186 | -6.91361 | -43.71793 | 2026-07-08 03:30:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 795cb01e-a179-3dbe-9405-7762b360758f | -6.94129 | -43.69761 | 2026-07-08 03:30:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 715e17bf-0585-3038-b97b-037f8fcb7ef8 | -6.92707 | -43.70492 | 2026-07-08 03:30:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 581b193b-7f42-35b8-9829-b861083b4ca6 | -5.6671 | -44.31553 | 2026-07-08 03:30:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 2dd7fcb2-45e4-37a7-9786-475c21a3c48e | -7.00695 | -42.7729 | 2026-07-08 03:30:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| ebfddf4d-0d67-3b62-a172-68584c329a6c | -4.83559 | -44.06458 | 2026-07-08 03:30:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 46763a4a-090d-3b35-888a-20ede19ecab1 | -6.91451 | -43.71297 | 2026-07-08 03:30:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| dda10be9-a60f-3d58-809a-8d3263dbdf39 | -7.08872 | -41.35085 | 2026-07-08 03:30:00 | NOAA-21 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 5ce7ee46-9340-34f0-9e8c-bbf5c5680ba4 | -6.9154 | -43.70808 | 2026-07-08 03:30:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8d713636-2feb-38a4-8c8a-296e355acd0c | -4.93425 | -37.92775 | 2026-07-08 03:30:00 | NOAA-21 | RUSSAS | CEARÁ | Brasil | 2311801 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 4595b1bf-f53b-3ed8-b7b7-f0702730aa67 | -6.91629 | -43.70321 | 2026-07-08 03:30:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| e0ae72cd-e478-3123-bfee-c0357fc711b0 | -5.66632 | -44.3112 | 2026-07-08 03:30:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 729e41ab-fcf1-3bf6-936b-f034d6237c57 | -5.66905 | -44.30449 | 2026-07-08 03:30:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| a6a5ecc8-f0d8-386b-a13e-09f9a8972696 | -5.79665 | -43.6353 | 2026-07-08 03:30:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4da2e22e-8978-3626-87ed-968052731012 | -6.9395 | -43.70716 | 2026-07-08 03:30:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 8.2 |
| e7f23090-357c-3f1f-b2b6-6d5e60f16a42 | -6.49579 | -42.2187 | 2026-07-08 03:30:00 | NOAA-21 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 73c7f35f-fc6b-3e42-a9bc-91e4498602c8 | -6.50223 | -42.21559 | 2026-07-08 03:30:00 | NOAA-21 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 7e3a1357-9866-38c8-88d7-7ec35216fe99 | -5.6587 | -44.3157 | 2026-07-08 03:30:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 9fad9855-a825-3bfd-8821-641b501caa54 | -7.00964 | -42.78506 | 2026-07-08 03:30:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| dde4b785-1aa9-3263-9dea-d5643b0d5136 | -5.82741 | -43.47778 | 2026-07-08 03:30:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5b15154b-8076-3d3c-a8a3-223cbb1e5c81 | -6.93405 | -43.71155 | 2026-07-08 03:30:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 33fc6dc8-4606-337e-bdec-132de17cb4c7 | -5.82654 | -43.48273 | 2026-07-08 03:30:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ddf305ae-7c22-3af0-9bbb-5075fb644c97 | -6.50002 | -42.22791 | 2026-07-08 03:30:00 | NOAA-21 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 11.5 |
| e21d4466-c91a-3bcc-8128-1dd4f1deed3d | -4.82902 | -44.06343 | 2026-07-08 03:30:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7dfd9247-d1c7-3a01-af62-294f0c115659 | -6.92616 | -43.70974 | 2026-07-08 03:30:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 17d9d72f-573a-3c8e-a973-d930274849fa | -6.92162 | -43.70923 | 2026-07-08 03:30:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| fe55a7d4-d3cc-3c26-9d8d-92aec8c16214 | -6.90295 | -43.7059 | 2026-07-08 03:30:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bf1d6b7c-a1ea-3fbe-8282-8356e5df7b0d | -5.80676 | -43.79611 | 2026-07-08 03:30:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e809f2a4-f26f-31f1-af79-3db6842863cc | -4.83505 | -44.06057 | 2026-07-08 03:30:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0601e50a-9e91-3309-8fbf-5c456c39da7b | -5.30695 | -43.05982 | 2026-07-08 03:30:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 89690feb-0f69-3ae6-afae-5b8ad4b884ba | -6.92249 | -43.70441 | 2026-07-08 03:30:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 68bd4215-75d6-3cf1-97c5-27e9830f5dd0 | -5.50102 | -44.0808 | 2026-07-08 03:30:00 | NOAA-21 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0813b07d-e8d9-3f67-bec8-b92eb4c76417 | -6.90204 | -43.71089 | 2026-07-08 03:30:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f453937e-b933-3738-98f4-f067bb86397d | -6.94287 | -43.69825 | 2026-07-08 03:30:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 0302ac57-bf9a-3684-bc46-8750983bce7f | -12.74762 | -44.4566 | 2026-07-08 03:32:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 25.7 |
| b5019867-d57d-382c-a272-ad124ffe37e6 | -10.76712 | -45.03338 | 2026-07-08 03:32:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 483d60fa-1900-320d-986a-d8f0befd9c26 | -15.77012 | -43.23574 | 2026-07-08 03:32:00 | NOAA-21 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e4f3e4c4-c7d2-304c-9273-b98a5e4c0bf9 | -10.94677 | -43.05626 | 2026-07-08 03:32:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 13.0 |
| c93f5453-97dc-3523-8139-91238ad6e1e5 | -12.77798 | -44.45821 | 2026-07-08 03:32:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 1a8643cd-9210-30d7-b19a-efe514106542 | -12.74969 | -44.45698 | 2026-07-08 03:32:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 32.8 |
| 4d19c263-f047-3f06-b1e5-c490d4ee64e7 | -12.78475 | -44.45506 | 2026-07-08 03:32:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 12e81413-68dc-3d98-94e1-a38b4053bbac | -12.36235 | -47.42348 | 2026-07-08 03:32:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| cdca21d9-936b-3b10-ac2c-e41221294b71 | -12.85011 | -44.39466 | 2026-07-08 03:32:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 42498572-2656-37c3-a097-76b103d161d1 | -10.94263 | -43.04754 | 2026-07-08 03:32:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 13.5 |
| e1b475ad-f5d8-359a-86f4-70749c76ad30 | -9.37398 | -44.71791 | 2026-07-08 03:32:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 824c53a5-bde2-3510-93b9-47bde448c005 | -12.78386 | -44.45945 | 2026-07-08 03:32:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 1a6200d0-f8ed-3c36-a8a0-03e939e97c0f | -9.37201 | -44.72801 | 2026-07-08 03:32:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| c6975fc7-5763-3169-b9a7-79aa0a7a2b1e | -13.94958 | -45.23518 | 2026-07-08 03:32:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| eb72c9d3-7f43-37c5-b261-cc7085636705 | -10.94192 | -43.05135 | 2026-07-08 03:32:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 21.3 |
| 8f7ff62c-f69f-35fb-9d31-fd44b92b825f | -12.75769 | -44.52822 | 2026-07-08 03:32:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 9cf7044b-436a-3cea-b051-b48bb59093a0 | -12.74673 | -44.46098 | 2026-07-08 03:32:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 26e71743-af3f-364f-97ab-f2fe450de928 | -12.85101 | -44.39026 | 2026-07-08 03:32:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 615ea0bf-d6d0-3811-8aac-d376330eaa63 | -12.75263 | -44.46218 | 2026-07-08 03:32:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 16.2 |
| e96946b3-e0b0-354a-9d6a-9169309b55d6 | -12.79649 | -44.45767 | 2026-07-08 03:32:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 21.6 |
| b32c0fec-2ab5-3780-b359-737000df9106 | -13.27986 | -45.18113 | 2026-07-08 03:32:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1699f6ec-7ab9-3943-912c-d79c935b7c08 | -12.36506 | -47.42442 | 2026-07-08 03:32:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 505bf22e-5335-38e8-a908-17341a54e28b | -12.7559 | -44.53707 | 2026-07-08 03:32:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| bdd145d6-05da-37d2-b35f-7569a905a8bd | -10.92519 | -43.04807 | 2026-07-08 03:32:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| c12f8379-b258-34c4-9248-7f550f9b58c3 | -11.12485 | -38.62816 | 2026-07-08 03:32:00 | NOAA-21 | TUCANO | BAHIA | Brasil | 2931905 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 965eb405-4929-3a3d-b124-1302c64b993d | -12.85154 | -44.39608 | 2026-07-08 03:32:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 1a80ebe8-f42c-3673-bbe6-d42d36c2e556 | -13.95149 | -45.22585 | 2026-07-08 03:32:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c5beba65-7ece-3167-9abe-a70df516dbc3 | -13.44161 | -43.85084 | 2026-07-08 03:32:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 01745249-5edd-38ba-bebe-092247cb6f47 | -10.94032 | -43.05103 | 2026-07-08 03:32:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 9041dcf6-e575-391e-9ed2-3f685673b273 | -13.44083 | -43.85475 | 2026-07-08 03:32:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2e8ffeae-7bc1-3059-93b8-9f81383e8ba8 | -13.28497 | -45.18723 | 2026-07-08 03:32:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f69e0ac4-8baa-341d-a702-9ec70b9895e4 | -12.74883 | -44.46137 | 2026-07-08 03:32:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 31.5 |
| 29d8b393-6497-3a41-802c-75b1740ee5c3 | -12.74851 | -44.45222 | 2026-07-08 03:32:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 25.7 |
| 5019b1c4-c0f4-35f5-b072-58cc241fa624 | -12.7636 | -44.52949 | 2026-07-08 03:32:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 32.1 |
| 95c9556d-d8b9-3751-ae59-c7ca86a2fdb2 | -13.28187 | -45.17137 | 2026-07-08 03:32:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| a3d1374a-6d6e-338c-a7de-d22a1d1c3570 | -12.75679 | -44.53265 | 2026-07-08 03:32:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 83cea2da-a3d3-3888-b6e8-6e0f48093f68 | -12.76181 | -44.53836 | 2026-07-08 03:32:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 42.5 |
| 28dd93ff-26e6-312e-ac56-49fe5d475e7c | -12.79032 | -44.48842 | 2026-07-08 03:32:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dd503ddc-2926-3716-9e44-9a1c0d64d7c4 | -12.75351 | -44.45781 | 2026-07-08 03:32:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 14.0 |
| f6699415-62d9-3469-9852-c03f93fcc8cb | -13.28599 | -45.18229 | 2026-07-08 03:32:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bdfca6e7-278c-351d-8960-1ec7cb330953 | -12.78621 | -44.47832 | 2026-07-08 03:32:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| fb5dafe9-bc46-3937-ad79-2fdb57c50b10 | -12.7627 | -44.53393 | 2026-07-08 03:32:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 32.1 |
| 3c8c7ffc-ceb8-3a4f-a0b2-2c28aa4ff3a7 | -12.75055 | -44.4526 | 2026-07-08 03:32:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 32.8 |
| 29b6e1d3-831e-3827-97fd-cb4d02221c42 | -11.41053 | -38.09564 | 2026-07-08 03:32:00 | NOAA-21 | ITAPICURU | BAHIA | Brasil | 2916500 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| e7bfbe56-8e41-36da-b181-699013639f7c | -12.35805 | -47.42277 | 2026-07-08 03:32:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| a955025b-a2b9-339c-89f3-a197773f6792 | -13.28699 | -45.17741 | 2026-07-08 03:32:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 141978ad-8fdb-3f12-bfbb-aece961d2a82 | -13.9573 | -45.19759 | 2026-07-08 03:32:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 64a88cd2-e649-3f0d-b9e1-02a34f69aafe | -13.95053 | -45.23052 | 2026-07-08 03:32:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 00b2b254-0fc5-3248-81d6-241c65420819 | -10.94515 | -43.05592 | 2026-07-08 03:32:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 125c64f0-59a7-3379-9c7e-0f00f6d4e6af | -13.95245 | -45.22118 | 2026-07-08 03:32:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |


[Clique aqui para ver as próximas entradas](README8.md)
