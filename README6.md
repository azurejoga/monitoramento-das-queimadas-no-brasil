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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ec82de27-34af-34b6-9673-cba0f7853def | -31.98341 | -52.03434 | 2025-02-18 04:46:00 | NOAA-21 | SÃO JOSÉ DO NORTE | RIO GRANDE DO SUL | Brasil | 4318507 | 43 | 33 | nan | nan | nan | Pampa | 1.4 |
| f4c0a4ac-0eef-377d-8a79-3892cf84702f | 3.53914 | -60.32825 | 2025-02-18 05:01:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3dcae714-05b2-3dba-9837-b7e75c61ae38 | 3.55724 | -60.32543 | 2025-02-18 05:01:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4aaaa8fa-6fc2-3a43-88d4-26f309c42657 | 1.3126 | -60.40983 | 2025-02-18 05:01:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2c06ab63-00e0-3623-8c0e-de1d021ce28a | 4.15934 | -60.73164 | 2025-02-18 05:01:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7615caac-59d2-385e-9b30-527d0faac92c | 3.47437 | -61.01315 | 2025-02-18 05:01:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3bbbffbe-d43e-30a5-8bf2-b81c468d177d | 1.9064 | -60.56702 | 2025-02-18 05:01:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 02faba2a-3f27-3310-84b9-f3077b425ed0 | 3.55792 | -60.32999 | 2025-02-18 05:01:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1502afe4-71c0-308c-bb02-32d8416cff88 | 3.55656 | -60.32088 | 2025-02-18 05:01:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e239b985-200c-3335-8e8d-6edd73363dee | -10.60739 | -45.10022 | 2025-02-18 05:03:00 | AQUA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 30.1 |
| aeeac22e-c5d2-3a62-9ea8-f64d868ecafe | -2.50084 | -54.13187 | 2025-02-18 05:03:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7a178947-0da9-3459-95c5-e3f4020d0199 | -1.56371 | -54.0262 | 2025-02-18 05:03:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 47405f7c-07f2-3947-89e5-8356cf21e0b3 | -1.5676 | -54.02323 | 2025-02-18 05:03:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2e525ce0-11f0-3463-9244-96d27c993c48 | -7.54752 | -45.86645 | 2025-02-18 05:03:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8152d4b0-489b-3a29-b5b3-518be65a52bb | -2.61243 | -54.22076 | 2025-02-18 05:03:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| da91b29c-02fb-387b-9f2b-6578071a987d | -7.54644 | -45.87462 | 2025-02-18 05:03:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 20aa0fb0-0cfb-3f4a-a8cb-866d26db212d | -1.72186 | -54.67165 | 2025-02-18 05:03:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 29b05bcf-ceb7-37ae-845f-e0646f185f3d | -2.61577 | -54.22127 | 2025-02-18 05:03:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d78ca89e-3ca9-3174-9a2e-38b856fcdad5 | -12.32369 | -52.48391 | 2025-02-18 05:05:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a427b04a-5eb0-330a-b264-89e17d7d62c2 | -10.60947 | -45.1083 | 2025-02-18 05:05:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5d9cb2d8-bf4f-3179-add0-3aeea2be610a | -12.33162 | -52.48508 | 2025-02-18 05:05:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f5fb16ed-633a-3b6c-95e5-bdd6ac84c7f2 | -12.32297 | -52.48907 | 2025-02-18 05:05:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 61aba155-60a0-31a7-a0c0-25e9d33a43f6 | -10.60885 | -45.11353 | 2025-02-18 05:05:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2f3366b0-59d8-3753-afd5-092a165b5fdf | -10.6101 | -45.10308 | 2025-02-18 05:05:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0fc2aef2-1f05-3e0a-a407-dbfa1c07d1f5 | -12.32766 | -52.4845 | 2025-02-18 05:05:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fe748cc6-4a68-35c0-bbe2-8d6f1034c42d | -12.3309 | -52.49023 | 2025-02-18 05:05:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0e2ef00f-edb1-3855-9257-ab85cb1ca5c5 | -19.96253 | -40.42143 | 2025-02-18 05:08:00 | AQUA_M-M | FUNDÃO | ESPÍRITO SANTO | Brasil | 3202207 | 32 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| 4d09b6bf-2549-314c-859a-828f3098b9be | -19.96394 | -40.41154 | 2025-02-18 05:08:00 | AQUA_M-M | FUNDÃO | ESPÍRITO SANTO | Brasil | 3202207 | 32 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 4b7aadc1-6ee2-370b-a8c8-7520a5994671 | -20.61003 | -40.98327 | 2025-02-18 05:08:00 | AQUA_M-M | VARGEM ALTA | ESPÍRITO SANTO | Brasil | 3205036 | 32 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| 8178273d-2b3f-3df2-bfd3-5763230e21b4 | -16.19335 | -60.00654 | 2025-02-18 05:08:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5343616e-3d25-30e7-91c3-a15c3931a7e0 | -21.42034 | -48.55498 | 2025-02-18 05:08:00 | NPP-375D | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 5d52ba12-738e-3d8d-87b2-83766f2b5a1f | -18.40708 | -55.59589 | 2025-02-18 05:08:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| eb72ae37-091f-3b78-a72b-dbdd59831abb | -18.38091 | -55.72699 | 2025-02-18 05:08:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 0755b18f-e974-3b22-ba56-18de686a8466 | -21.07315 | -56.39005 | 2025-02-18 05:08:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d3145ebf-a1d8-3146-9a2d-e17b3730f330 | -21.38361 | -48.57282 | 2025-02-18 05:08:00 | NPP-375D | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 1441953c-daca-3470-9fad-6e7fc81d919e | -21.41452 | -48.55453 | 2025-02-18 05:08:00 | NPP-375D | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| a6b18991-9d95-3c1a-bdcd-0b1976e3c07b | -19.49773 | -55.34113 | 2025-02-18 05:08:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| a1b484e8-7a5d-3d7b-979a-f8aa77ab2f72 | -21.52574 | -47.14375 | 2025-02-18 05:08:00 | NPP-375D | TAMBAÚ | SÃO PAULO | Brasil | 3553302 | 35 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 5fa5ca8f-0931-3abe-b16d-b59488e512d4 | -21.38399 | -48.56865 | 2025-02-18 05:08:00 | NPP-375D | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| b8142620-6aae-371a-94f6-ee36de81030b | -18.41068 | -55.59644 | 2025-02-18 05:08:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 1c454cbb-233a-3795-b4de-a31289594895 | -16.09709 | -60.07623 | 2025-02-18 05:08:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4e196baf-05df-3f06-88a1-f3359ad1d933 | -18.40812 | -55.59406 | 2025-02-18 05:08:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| e7cdfde2-380f-3bb6-9285-a28623b5394d | -20.90423 | -56.56458 | 2025-02-18 05:08:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 63ba1fd0-7db9-3c17-aaf7-dbf01c987c45 | -19.49836 | -55.33657 | 2025-02-18 05:08:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| c29de3ca-b6a8-3ff9-8816-7c42cb48fb5e | -18.40647 | -55.60018 | 2025-02-18 05:08:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 3df5053e-b73e-3480-bd25-ef0e1843385b | -16.09987 | -60.08071 | 2025-02-18 05:08:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f8e9334b-9912-379e-a68f-996c6fb8115b | -18.40752 | -55.59836 | 2025-02-18 05:08:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 71cdd6c0-cb95-3325-b823-8f60d4c5278a | -21.32055 | -48.688 | 2025-02-18 05:08:00 | NPP-375D | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 2017d2bc-66d7-3326-b066-1e9161b9d673 | -16.10052 | -60.07684 | 2025-02-18 05:08:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| df88c352-5870-3148-ae79-736f06b97e6d | -20.50702 | -55.92472 | 2025-02-18 05:08:00 | NPP-375D | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b7f3f82d-fab7-3ee6-8261-6e2d65005aad | -16.19678 | -60.00713 | 2025-02-18 05:08:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a3275a68-a196-390e-8061-77ad8650ba51 | -20.91778 | -56.54549 | 2025-02-18 05:08:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 6.1 |
| b802a906-7998-3ae4-9e6c-7379edf6cec5 | -16.21304 | -59.67501 | 2025-02-18 05:08:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0c0c32dc-88d7-3a94-9263-92c7e4aad0b0 | -21.3263 | -48.68847 | 2025-02-18 05:08:00 | NPP-375D | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 3237f827-80de-3068-9ab2-edb542efa86e | -19.02353 | -57.62321 | 2025-02-18 05:08:00 | NPP-375D | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 7a4243bb-dc4c-3aec-855a-0bd76f754f49 | -21.52619 | -47.13831 | 2025-02-18 05:08:00 | NPP-375D | TAMBAÚ | SÃO PAULO | Brasil | 3553302 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 357bfdd9-b19f-3bac-9a07-42a8cf432913 | -19.50365 | -55.4505 | 2025-02-18 05:08:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| f7af857b-59e5-3bc8-98a4-63fcbd272d35 | -16.09644 | -60.0801 | 2025-02-18 05:08:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 64538d2c-4d6d-3d65-a208-5c6ecc9780e4 | -15.08089 | -48.94436 | 2025-02-18 05:08:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 88dfb7fc-ca10-3a1e-9eff-14e901019e77 | -21.07671 | -56.39065 | 2025-02-18 05:08:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e1f0f76e-dd81-3281-8679-0189cf3ce576 | -20.90717 | -56.56939 | 2025-02-18 05:08:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 11aaaf2d-36b9-3722-bfe4-13d1510ddafc | -21.42074 | -48.55062 | 2025-02-18 05:08:00 | NPP-375D | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 3f4e1155-8a8f-345b-8d2a-9619578eccad | -17.53081 | -55.43879 | 2025-02-18 05:08:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.6 |
| a809cdad-2df5-3a91-b045-05093ce3f1b8 | -22.08772 | -54.5128 | 2025-02-18 05:10:00 | NPP-375D | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 686cd9d8-a846-3073-bf88-5b9ade624bd1 | -22.19818 | -56.96449 | 2025-02-18 05:10:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d48a42df-039b-3d21-bac5-307f8791730a | -22.08606 | -54.51152 | 2025-02-18 05:10:00 | NPP-375D | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 37be50d1-e881-3d31-bb65-e0a54a4cc927 | -22.20171 | -56.96504 | 2025-02-18 05:10:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9456ef0c-e2b6-359d-8088-df92a414edb6 | -21.96541 | -57.58487 | 2025-02-18 05:10:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 2c7fd7ee-c3f2-319e-a558-b130ee80e4f3 | -21.96197 | -57.58429 | 2025-02-18 05:10:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1dc0f8dd-d266-37fe-9e39-3e865b23419d | -21.63115 | -55.97683 | 2025-02-18 05:10:00 | NPP-375D | GUIA LOPES DA LAGUNA | MATO GROSSO DO SUL | Brasil | 5004106 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b10a2a83-6024-3acc-be58-aa177edeefe8 | 3.47625 | -61.0139 | 2025-02-18 05:27:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d506d863-9b25-330e-b563-e56a5d66d2e9 | 2.79296 | -60.20981 | 2025-02-18 05:27:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b736b314-d9df-33cf-90f0-77c4c3fb4dd6 | 1.77065 | -60.38391 | 2025-02-18 05:27:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b0351b3e-efca-3e40-a9b0-a18f70b5a808 | -2.61631 | -54.22188 | 2025-02-18 05:27:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 05223776-dc9f-3f1c-8f88-c97cc75695fc | 2.51436 | -60.98745 | 2025-02-18 05:27:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| be528b56-91ab-3e37-a9f1-f8a49f788d1f | 0.97471 | -60.40331 | 2025-02-18 05:27:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 05ce834e-6da6-377b-b0dc-447343029995 | 1.31159 | -60.40705 | 2025-02-18 05:27:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| df581ed5-5122-332f-b424-daca91dfbe86 | 2.9259 | -60.44894 | 2025-02-18 05:27:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6f532ab8-51dd-3ac1-aa78-5f6701e339fa | 1.90522 | -60.57014 | 2025-02-18 05:27:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2f779ec2-50a2-3dee-9abc-04741ddb8056 | 1.34898 | -60.03895 | 2025-02-18 05:27:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ae4775a7-a727-3fa7-bf06-df0731e9af92 | 4.15959 | -60.73196 | 2025-02-18 05:27:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bc1c493b-1fb6-3759-8597-04537285042a | -2.61165 | -54.22131 | 2025-02-18 05:27:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 87d6ccc4-0d78-333b-9700-f5f8ce0196a2 | -14.98778 | -50.77523 | 2025-02-18 05:29:00 | NOAA-20 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7640191e-dacf-3540-acb8-5eaa4d375d3c | -16.09695 | -60.07556 | 2025-02-18 05:29:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 383cfb89-8432-33f4-87d1-4f07baae246f | -16.09925 | -60.07753 | 2025-02-18 05:29:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6cfcdfdb-51ef-33cc-b122-6efa23fd71a6 | -16.19511 | -60.00639 | 2025-02-18 05:29:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b168ea80-ad8d-39d6-a225-a564d19a4807 | -16.10308 | -60.07811 | 2025-02-18 05:29:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c0ac2fdf-1dde-33e9-93f9-772afb8ecbdc | -16.09627 | -60.08039 | 2025-02-18 05:29:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 14599f87-8b43-328e-a023-c3abba996bfd | -20.91469 | -56.54483 | 2025-02-18 05:31:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ff5f1d03-2d5f-3880-8ef2-f53c662bfcae | -20.90442 | -56.56583 | 2025-02-18 05:31:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 688a4668-5143-3e95-8549-38cf5c8cff75 | -21.07567 | -56.38962 | 2025-02-18 05:31:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6735e6cd-53dc-386e-a091-48537f2923ad | -21.96318 | -57.58574 | 2025-02-18 05:31:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 7d4852fc-7890-31f2-8b9a-c1fa17173700 | -12.33346 | -52.48602 | 2025-02-18 05:31:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a5b17e5f-449a-3714-8936-7175d4d29c0c | -18.40567 | -55.59863 | 2025-02-18 05:31:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| bfd03c68-22b3-3cc6-b403-4ec489cd3038 | -12.32406 | -52.48588 | 2025-02-18 05:31:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cd516d35-b9c4-32c3-b205-30ef5c0978ef | -12.32747 | -52.48528 | 2025-02-18 05:31:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1e3b33a7-04c0-3a1a-9613-395d4219670b | -20.91655 | -56.54857 | 2025-02-18 05:31:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cdbde1bc-1287-3dd2-826e-5256b1d6906e | -12.33292 | -52.49048 | 2025-02-18 05:31:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5582e986-18c7-3c6f-b917-0f68a338dc83 | -12.32147 | -52.48453 | 2025-02-18 05:31:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2999933d-0809-36f1-b607-8eac0edb0198 | -18.40604 | -55.59521 | 2025-02-18 05:31:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |


[Clique aqui para ver as próximas entradas](README7.md)
