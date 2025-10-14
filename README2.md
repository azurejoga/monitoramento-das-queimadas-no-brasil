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
| e8d311a1-6ffb-3bcc-8fcd-98ba274d432a | -4.6509 | -43.1337 | 2025-10-14 00:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 61.0 |
| ba1655e3-5db1-35f7-b6d0-73e768cbec1b | -13.0064 | -50.8694 | 2025-10-14 00:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 57.7 |
| ff15dd81-da4d-3eed-8687-c32c5af9ea03 | -5.0994 | -43.1977 | 2025-10-14 00:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 2b19676f-bf1b-311b-9a52-0d9cc7f67ddc | 1.8951 | -55.7027 | 2025-10-14 00:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 86.4 |
| 6c97b472-8f1b-39d7-828c-21756867d185 | -5.5125 | -43.0747 | 2025-10-14 00:50:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 84593199-7836-3c5f-aa73-311c338849a4 | -10.4594 | -57.4831 | 2025-10-14 00:50:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 89.4 |
| 6d1ee13a-997c-33f6-9f65-6e7df83110ca | -4.1048 | -50.0647 | 2025-10-14 00:50:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 118.9 |
| e579c633-0982-3b21-8484-83292f7114da | -7.7898 | -46.0217 | 2025-10-14 00:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 104.6 |
| b0d58245-0a47-32ee-a458-c95ea7d79c66 | 1.8768 | -55.7029 | 2025-10-14 00:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| b207a3ea-d571-3960-b267-b95e4da566e8 | -4.105 | -50.0436 | 2025-10-14 00:50:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 191.5 |
| 6f2cb915-381c-32c7-a19e-c307b8be1ba8 | 1.8768 | -55.7227 | 2025-10-14 00:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 3274c14d-bc19-3974-9c60-d1aa052fb7e7 | -5.5127 | -43.0512 | 2025-10-14 00:50:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 56.1 |
| 430b76b4-cfb4-32e8-9811-920af6a1a6b1 | -13.5145 | -50.3084 | 2025-10-14 00:50:00 | GOES-19 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 108.6 |
| f9d4a5e1-0300-364e-a7d2-6bd08bc897e8 | -4.1233 | -50.0639 | 2025-10-14 00:50:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 1e7c5755-4623-3ec5-a973-db3acefd810c | -13.0256 | -50.867 | 2025-10-14 00:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 016d3f3f-cbbc-3954-9666-ef3e1338f91c | -4.6696 | -43.1326 | 2025-10-14 00:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 0410007f-f04a-3f48-9a89-04d996a24384 | -4.6319 | -45.7863 | 2025-10-14 00:50:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 59f656a6-ccbc-3830-a55d-5c0c7f76e1d3 | -7.8086 | -46.02 | 2025-10-14 00:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 79.7 |
| ad0bd269-1358-3367-ac85-e8cbe428d79d | -5.4937 | -43.0761 | 2025-10-14 00:50:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 91.2 |
| d1c5c1e5-a22d-39ba-924c-871c36c6bcfa | -4.1235 | -50.0428 | 2025-10-14 00:50:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 91.2 |
| a487b4aa-a089-3784-8080-178c6e8853f4 | -5.1181 | -43.1964 | 2025-10-14 00:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 62.3 |
| c24efcb2-16ce-3c91-bdbb-ec9710af4f4c | 1.8951 | -55.7224 | 2025-10-14 00:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 90.1 |
| 06ee1adc-db79-3bc1-980a-503a3e6d27cd | -5.494 | -43.0526 | 2025-10-14 00:50:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 26989d83-5a84-3ebe-b5eb-7b792e05f164 | -7.8086 | -46.02 | 2025-10-14 01:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 95.6 |
| 5b2298e6-b736-3213-bd53-2cd2329e769d | 1.8952 | -55.6829 | 2025-10-14 01:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 57.2 |
| dc3609ce-5b51-38c6-bc23-23f6243c1220 | -4.1233 | -50.0639 | 2025-10-14 01:00:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 77.3 |
| 6677c149-2a40-358d-95b9-1f481d4906be | -4.6694 | -43.1559 | 2025-10-14 01:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 44.4 |
| 860d1a38-e7a6-3658-8d54-a65c83b5f5b9 | -4.105 | -50.0436 | 2025-10-14 01:00:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 148.7 |
| 8c5afab6-1ab2-31d8-9ff0-54369536cc9d | -4.1235 | -50.0428 | 2025-10-14 01:00:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 100.4 |
| a057e880-9ac4-307b-95f5-84cf0f8bf9e5 | -4.6696 | -43.1326 | 2025-10-14 01:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 93.3 |
| 3bc33af8-8ac8-3c9e-902e-524546b16ae4 | -5.0994 | -43.1977 | 2025-10-14 01:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 32.6 |
| 7e9a4087-bd89-36e7-8ce0-e1ccd97a177c | -7.7898 | -46.0217 | 2025-10-14 01:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 106.8 |
| e9584fd0-41ef-346b-a529-cafac7ee4e1c | -13.5145 | -50.3084 | 2025-10-14 01:00:00 | GOES-19 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 98.4 |
| 6244c391-ff5d-3c9e-8cdf-bed82ecb5253 | 1.8768 | -55.6832 | 2025-10-14 01:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 511ee716-14a9-361f-a7de-5934c405a500 | -4.6509 | -43.1337 | 2025-10-14 01:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 46.7 |
| 015d58b9-7755-3273-a451-5e7b3e408d79 | -5.1181 | -43.1964 | 2025-10-14 01:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 39.8 |
| 90c9dc5e-0406-3e46-a4ce-51e47239c89f | -4.6133 | -45.7874 | 2025-10-14 01:00:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 79.5 |
| b8e7b288-91ea-33a8-95d0-9d1a155317ef | -7.0414 | -39.2229 | 2025-10-14 01:00:00 | GOES-19 | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 86.3 |
| 42303b7c-92e3-39a5-96fb-20097a1a8491 | -4.6134 | -45.765 | 2025-10-14 01:00:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 62.4 |
| d20b0612-7d24-3696-a50d-d8711d6b7848 | -4.1048 | -50.0647 | 2025-10-14 01:00:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 109.7 |
| d772d569-0000-3f69-9a8c-1924630cdd8a | -7.1652 | -46.524 | 2025-10-14 01:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 9298b4fc-fc02-33d7-8831-e1627ed2221c | -4.6883 | -43.1314 | 2025-10-14 01:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 38.7 |
| fd9e3544-244a-31d5-98a7-3a59ea90c0d1 | -10.4594 | -57.4831 | 2025-10-14 01:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 16ca74de-3892-35f5-b6cc-1bd4469349bd | 1.7667 | -55.8031 | 2025-10-14 01:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 62.3 |
| aa33cd42-908d-316d-afd4-d9d16c8345fc | -5.1181 | -43.1964 | 2025-10-14 01:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 56.0 |
| 7ba4871f-dfc1-34c9-a737-8bf3ffd4dda7 | -4.1233 | -50.0639 | 2025-10-14 01:10:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 78.5 |
| e3c16b30-5c2c-3579-b183-a04042195617 | -3.0416 | -40.108 | 2025-10-14 01:10:00 | GOES-19 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 75.1 |
| 60b353c3-31ec-3dff-8245-3328885bcc01 | -11.7594 | -43.2898 | 2025-10-14 01:10:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 92.9 |
| da647b8d-2c39-31e1-9992-561e0ca9dd5e | -4.1048 | -50.0647 | 2025-10-14 01:10:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 132.9 |
| 3b6715fb-e767-36f2-891c-b160bbd25ccc | -7.9631 | -44.113 | 2025-10-14 01:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 116.4 |
| 3869b125-8f4b-3633-a2b3-07e16df8d549 | -4.6509 | -43.1337 | 2025-10-14 01:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 35.8 |
| 791a7f9f-47ea-3e1b-a0bc-13f26a0a1f70 | -7.9253 | -44.1169 | 2025-10-14 01:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 105.1 |
| f669acb8-f060-330c-a8e6-b2410cd6b3ee | -11.7401 | -43.2928 | 2025-10-14 01:10:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 98.7 |
| aefff99a-8f20-3141-8a2a-888e54dc5bfc | -4.6133 | -45.7874 | 2025-10-14 01:10:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 73.4 |
| aa25fba2-eee8-351f-a1d6-ffabbb646ec1 | -7.8086 | -46.02 | 2025-10-14 01:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 120.0 |
| 19771483-175a-3988-92a0-38abbebc2328 | -13.5145 | -50.3084 | 2025-10-14 01:10:00 | GOES-19 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 97d21b4e-6566-32a8-83b0-6e53ba267d3f | -4.6694 | -43.1559 | 2025-10-14 01:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 39.8 |
| 1038670d-a904-31c8-9a60-6a33ebc5a10d | -4.6319 | -45.7863 | 2025-10-14 01:10:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 148.9 |
| 65a15add-bb91-3e57-a533-16787cf9da01 | -4.6696 | -43.1326 | 2025-10-14 01:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 103.4 |
| 6646969c-d380-330d-90cf-c4e94161122d | -7.9442 | -44.115 | 2025-10-14 01:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 283.7 |
| 93e2e451-210a-342f-b95d-3c0d7fcf0adf | -4.6321 | -45.7639 | 2025-10-14 01:10:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 145.2 |
| 47d6c61b-b8a4-3137-8cbd-676a48411786 | -5.4937 | -43.0761 | 2025-10-14 01:10:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 26eadbe0-7ce8-340a-91c9-bd6c8e591c86 | -4.6134 | -45.765 | 2025-10-14 01:10:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 2a19cee9-a4b5-39f1-9254-457b026fa5f6 | -5.0994 | -43.1977 | 2025-10-14 01:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 1eaa074d-135d-34dd-ba8f-f743dc950a77 | -4.1235 | -50.0428 | 2025-10-14 01:10:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 101.0 |
| 7fc7f1d0-29bb-3e05-9706-071ef3362897 | -5.5125 | -43.0747 | 2025-10-14 01:10:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 58.3 |
| 17c6ea8d-96ab-3b3d-a549-7d0fe65ebda6 | -7.9439 | -44.1381 | 2025-10-14 01:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 128.1 |
| 2e38feb7-5500-37bd-a3f5-dcb2899a0af3 | -7.9628 | -44.1362 | 2025-10-14 01:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 68.4 |
| c528d4fd-43fd-3550-94c3-9604bc01a353 | -7.7898 | -46.0217 | 2025-10-14 01:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 140.2 |
| a3e82ab6-b5ee-32d2-a830-feb56b75144a | -4.105 | -50.0436 | 2025-10-14 01:10:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 173.6 |
| de41976c-e028-37e8-9e9e-81aba161473f | -4.6698 | -43.1092 | 2025-10-14 01:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 39.2 |
| 7ccbb35f-a936-3f2e-8832-d24caa0c0914 | -4.1235 | -50.0428 | 2025-10-14 01:20:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 143.0 |
| 13722aeb-196f-33fe-b050-fef9df0c3af2 | -5.494 | -43.0526 | 2025-10-14 01:20:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 75.7 |
| ebd65449-bb68-3dcf-ad74-1e3f12605866 | -7.7898 | -46.0217 | 2025-10-14 01:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 4a840743-4f2f-3e41-a2c6-4d81746d4b75 | -7.9628 | -44.1362 | 2025-10-14 01:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 59.1 |
| ee8178a9-27fc-32e3-92d5-c8f2bf61f182 | -7.9251 | -44.1401 | 2025-10-14 01:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 0431df3f-50b4-32f1-b871-691a03752edb | -4.6321 | -45.7639 | 2025-10-14 01:20:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 75.3 |
| 7e98df41-66c7-3f25-a0e9-583c7edaecfa | -7.9439 | -44.1381 | 2025-10-14 01:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 100.7 |
| a5e77709-1a6a-35c3-b2ce-22bd2ecff546 | -13.5145 | -50.3084 | 2025-10-14 01:20:00 | GOES-19 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 2f8061ad-340a-3bfd-9c18-b6383d24c2e1 | -11.7594 | -43.2898 | 2025-10-14 01:20:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 102.0 |
| 065dc93c-279a-3c71-a2ba-81a615610112 | -4.6696 | -43.1326 | 2025-10-14 01:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 112.9 |
| 231269c6-0af4-3e26-9461-60337135b311 | 1.7667 | -55.8031 | 2025-10-14 01:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 6b5035be-5cbc-393c-9b4d-0bf9b7afb08f | -5.118 | -43.2198 | 2025-10-14 01:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 44.7 |
| bfdd1968-6c36-3b9f-ba32-22e36e67e819 | -5.1181 | -43.1964 | 2025-10-14 01:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 87.7 |
| 8f74e97f-cc2a-3b64-9980-ce2ef4235525 | -4.6319 | -45.7863 | 2025-10-14 01:20:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 92.7 |
| 3e0e6c7c-db24-3c33-9b83-d63e19e9d650 | -7.9442 | -44.115 | 2025-10-14 01:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 196.2 |
| 292e25f0-d12f-3f5f-a7d5-f983c77b18ef | -4.1048 | -50.0647 | 2025-10-14 01:20:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 99.3 |
| 0a0ec415-f881-3946-8df3-08fe44f5b9fd | -11.7401 | -43.2928 | 2025-10-14 01:20:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 153.2 |
| 0d563c9e-f2af-3b65-9732-093432c5cdd9 | -4.6133 | -45.7874 | 2025-10-14 01:20:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 76.4 |
| 4d1333c8-fd51-3bec-9708-c22b30d7b429 | -7.9253 | -44.1169 | 2025-10-14 01:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 122.9 |
| 3842c859-c73b-358c-810d-3326d9d7799a | -4.1233 | -50.0639 | 2025-10-14 01:20:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 83.7 |
| b6c4003b-79f0-32ab-8b8e-3babd7db37b7 | -3.0416 | -40.108 | 2025-10-14 01:20:00 | GOES-19 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 68.3 |
| 1e991b94-6600-3e26-880b-2c68dae44a33 | -4.105 | -50.0436 | 2025-10-14 01:20:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 170.9 |
| ff8cbb5b-dd9e-3883-bb06-594e83df7d18 | -5.0992 | -43.2211 | 2025-10-14 01:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 36.6 |
| ccd6aab8-5358-39a3-a3b5-be233517fc93 | -4.6698 | -43.1092 | 2025-10-14 01:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 38.6 |
| e54e018a-2137-343a-89c5-4c22cbbcb8d2 | -4.6694 | -43.1559 | 2025-10-14 01:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 46.0 |
| 1f36edc1-7d19-3189-a031-60b25529214c | -4.6509 | -43.1337 | 2025-10-14 01:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 41.9 |
| c1be86a5-0526-3058-a284-8235b9541e7f | -5.0994 | -43.1977 | 2025-10-14 01:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 2a895d7b-70a6-3566-be02-063bc002f24b | -7.8086 | -46.02 | 2025-10-14 01:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 9180c671-2083-3401-a80b-aec6baac11e4 | -5.4937 | -43.0761 | 2025-10-14 01:20:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 91.8 |


[Clique aqui para ver as próximas entradas](README3.md)
