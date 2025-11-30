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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 56ab2f22-50ab-36c3-87e7-6b425eca2cb6 | -5.24006 | -41.23917 | 2025-11-30 04:25:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| bece48c0-3e2b-36bb-a2bc-822d250fa53d | -12.01474 | -49.26645 | 2025-11-30 04:25:00 | NPP-375D | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8a8c7455-5989-36bd-9b3c-f8767c2994f5 | -5.7308 | -39.8317 | 2025-11-30 04:25:00 | NPP-375D | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| b7f82853-b85d-32ba-9256-482e2d37ae0e | -2.44585 | -49.02877 | 2025-11-30 04:25:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a2f4ee80-b24e-3b26-aa2d-d902781ced80 | -5.51289 | -42.57798 | 2025-11-30 04:25:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 6e8ae0d3-dde3-3ac1-9416-0517307990b6 | -5.50544 | -42.58063 | 2025-11-30 04:25:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 4fe43784-5899-343e-8af6-7de8c9f91668 | -3.97915 | -44.02703 | 2025-11-30 04:25:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 71d85a65-a432-35d8-ab29-71775c6b5976 | -4.35901 | -43.16562 | 2025-11-30 04:25:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 8da8df75-aeb8-3de3-ae8a-c5a0ece1df6e | -2.63409 | -48.54617 | 2025-11-30 04:25:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 786020e3-116e-33a5-8019-562e4cc2ad71 | -12.45243 | -44.88791 | 2025-11-30 04:25:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c20f116f-1c0f-3d81-850c-6078387d5e27 | -2.64199 | -48.54747 | 2025-11-30 04:25:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 82ac30fe-9b18-3aea-9624-9700e439209e | -3.97584 | -44.02651 | 2025-11-30 04:25:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2a99c4a5-04a6-3196-9a5a-29ecf905a10a | -2.96431 | -49.2123 | 2025-11-30 04:25:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 02321cf6-302c-3751-a584-45e8057c6fc8 | -4.35846 | -43.16916 | 2025-11-30 04:25:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| e830ddd1-84fc-367b-943a-90a6075b2b66 | -3.62417 | -42.75801 | 2025-11-30 04:25:00 | NPP-375D | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 45720262-0dba-3fbf-ad94-4d7a121d6988 | -12.83542 | -47.39217 | 2025-11-30 04:25:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| db2f50e7-1152-3cae-9cbc-a10868a120ec | -12.01332 | -49.27493 | 2025-11-30 04:25:00 | NPP-375D | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6b4b95b2-702f-3eaa-9d22-9b9248b1ba2e | -4.81305 | -43.08684 | 2025-11-30 04:25:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 304a0864-637a-379f-b65a-2e683aeb50ff | -2.7468 | -47.13394 | 2025-11-30 04:25:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 59da7074-0c9e-3a24-b79e-421622e31848 | -4.54675 | -40.47089 | 2025-11-30 04:25:00 | NPP-375D | NOVA RUSSAS | CEARÁ | Brasil | 2309300 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 24459b42-7f2e-3a60-b64a-ffa83be7c158 | -2.64215 | -48.03093 | 2025-11-30 04:25:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| cbb10a43-4071-3ed5-9613-c9417016027f | -2.63565 | -48.54452 | 2025-11-30 04:25:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5f104fef-8616-3112-a375-4023ed59ed0a | -3.44533 | -45.41189 | 2025-11-30 04:25:00 | NPP-375D | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f860e20e-f886-32d5-9e5b-745e41ca9cfb | -14.26377 | -44.38654 | 2025-11-30 04:25:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bc507d59-01ae-3b2c-a805-409fc8ada734 | -3.6281 | -42.75496 | 2025-11-30 04:25:00 | NPP-375D | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 1497f92b-49ac-3bf9-b503-e69f7b69dac2 | -3.88142 | -45.027 | 2025-11-30 04:25:00 | NPP-375D | PIO XII | MARANHÃO | Brasil | 2108702 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 01dfc333-1054-330d-8090-541af9c307e1 | -4.63615 | -43.23034 | 2025-11-30 04:25:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 99fec043-66d7-3dfb-9738-46a7e4e47d13 | -4.54921 | -43.22427 | 2025-11-30 04:25:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bd209a81-d0c4-350e-a7ab-008bc97713ac | -2.63326 | -48.5512 | 2025-11-30 04:25:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| a4348438-cc00-3e90-beca-9fcf35f0cc98 | -4.52493 | -44.75009 | 2025-11-30 04:25:00 | NPP-375D | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| da29f876-199b-37fa-b57d-d55be871cd2e | -2.6002 | -49.26466 | 2025-11-30 04:25:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| ae4e7c99-d2e6-334c-8a52-a7694edd0d83 | -2.64062 | -48.04032 | 2025-11-30 04:25:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 96daec1d-4cd9-3f59-9ad2-86e6866b14fb | -3.23134 | -45.52935 | 2025-11-30 04:25:00 | NPP-375D | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 6d105d0f-03cd-3c25-bc1d-82fefa72eadf | -5.51115 | -42.58915 | 2025-11-30 04:25:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 21e5c9f2-70ca-3c2d-afdd-e0f3abd91658 | -3.23076 | -45.53296 | 2025-11-30 04:25:00 | NPP-375D | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 959f2392-af7a-3bf1-b279-af233509a0b2 | -4.52161 | -44.74956 | 2025-11-30 04:25:00 | NPP-375D | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 08c78181-93ac-35f5-b841-06ae094b902d | -10.71464 | -47.25564 | 2025-11-30 04:25:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 0653d576-7ae9-3d67-beab-4fe77f4ad6db | -2.51016 | -49.09888 | 2025-11-30 04:25:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 34000283-29f1-38db-b873-2cccfbea0b83 | -3.03416 | -45.12103 | 2025-11-30 04:25:00 | NPP-375D | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4e942c96-6763-38fb-804b-df46f4810d04 | -11.39933 | -49.19318 | 2025-11-30 04:25:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 09d13e99-88ff-3f86-ac0c-44f3657d10b0 | -2.45581 | -50.2501 | 2025-11-30 04:25:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e64ee94e-8313-32de-b283-647561bda978 | -3.27043 | -45.50224 | 2025-11-30 04:25:00 | NPP-375D | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3ff6926a-bfb3-3e26-822f-d825d94912d1 | -12.14647 | -40.36241 | 2025-11-30 04:25:00 | NPP-375D | MACAJUBA | BAHIA | Brasil | 2919603 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 2e63bf73-f7be-367a-becb-a89ccf1e4657 | -12.00821 | -49.26092 | 2025-11-30 04:25:00 | NPP-375D | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e82f0efb-23bd-3466-b638-2db9984afeed | -2.50834 | -49.21598 | 2025-11-30 04:25:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fe9205eb-363b-3a1c-b231-5110e3b73523 | -12.65832 | -46.75074 | 2025-11-30 04:25:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c1c2f162-d590-33e0-9922-c71bb7c88c93 | -13.65298 | -44.2564 | 2025-11-30 04:25:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ab104a4d-2586-39a9-9b36-262674bccca9 | -4.36871 | -43.16033 | 2025-11-30 04:25:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dbc379a3-8d5b-3f3e-afd1-967fd56b5b40 | -4.10455 | -42.09205 | 2025-11-30 04:25:00 | NPP-375D | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 721beb78-6ad8-3633-a705-a53996c7fecb | -2.64595 | -48.54811 | 2025-11-30 04:25:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 4e327e37-56e0-3adc-b98c-72de161d941b | -13.72219 | -48.73771 | 2025-11-30 04:25:00 | NPP-375D | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 44525a0c-aacf-30b7-89bc-7a602d2eda42 | -3.97604 | -42.51637 | 2025-11-30 04:25:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| bfc527c4-cb40-348a-b094-0b381adeb3c7 | -5.73402 | -39.83751 | 2025-11-30 04:25:00 | NPP-375D | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| d5bbfedf-3c38-3365-a886-8e90831f3f94 | -2.8752 | -49.07161 | 2025-11-30 04:25:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b91c4d81-e96d-30d1-8b62-a67e8a0b3015 | -12.50218 | -52.38963 | 2025-11-30 04:25:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e249f55d-e2e6-356b-8f51-483524a77a1c | -12.23287 | -54.38162 | 2025-11-30 04:25:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8ccd63dd-734a-3129-994e-f7173e3bd245 | -5.50946 | -42.57743 | 2025-11-30 04:25:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 4221c95a-d754-3356-b186-2720af9aa70c | -12.01908 | -49.26285 | 2025-11-30 04:25:00 | NPP-375D | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ec1dd78e-0b1f-3bca-966a-2f5e22c9a4d9 | -12.65499 | -46.75019 | 2025-11-30 04:25:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| df4f7ede-ec9d-3188-a2e0-75b40df24cb9 | -2.6317 | -48.54385 | 2025-11-30 04:25:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e5544605-05dc-3339-aace-4bf3d311309b | -3.58951 | -41.66475 | 2025-11-30 04:25:00 | NPP-375D | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 12d931b7-6d2e-36b1-b0f7-179316878bfb | -12.00607 | -49.27363 | 2025-11-30 04:25:00 | NPP-375D | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9c696a1c-12fc-34ab-aa44-d07119e6082b | -5.50888 | -42.58117 | 2025-11-30 04:25:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 044d100e-fa86-3522-b3c5-5cd6aed8ea0e | -4.36535 | -43.15981 | 2025-11-30 04:25:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8d5bf7c7-2ec0-38d8-8c12-eefa84e3b6f7 | -12.01112 | -49.2658 | 2025-11-30 04:25:00 | NPP-375D | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 77b8a50e-6f32-338b-9d9a-ad06f0293529 | -12.01403 | -49.27069 | 2025-11-30 04:25:00 | NPP-375D | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 09ef6da6-5863-3f5e-a7c4-13991648be29 | -2.64198 | -48.55589 | 2025-11-30 04:25:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3aaaafbd-d43d-3f23-94ea-9ef79b9c5a32 | -13.48664 | -46.71287 | 2025-11-30 04:25:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| e15ab4d4-01cd-3f38-8084-afc502714410 | -2.69865 | -49.32195 | 2025-11-30 04:25:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c3c110f0-e168-3bb7-b217-0479a4e4e960 | -12.70834 | -46.79539 | 2025-11-30 04:25:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 07831099-0cc5-37d9-a437-63b4937f9328 | -5.36739 | -43.02086 | 2025-11-30 04:25:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 14f68906-510f-3773-bea7-408022947ef4 | -3.94742 | -42.02982 | 2025-11-30 04:25:00 | NPP-375D | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| ada3b262-73b9-3a30-a31c-fd53602f748a | -2.64512 | -48.55313 | 2025-11-30 04:25:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 5238b0d7-73bc-3645-a709-02a1c2efe281 | -2.96842 | -49.21295 | 2025-11-30 04:25:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f60dc7b1-e8f5-3b80-80da-a9264e478d9e | -2.92267 | -48.22866 | 2025-11-30 04:25:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 06622390-7336-3e96-a2f3-a9cef9845818 | -3.23415 | -45.5335 | 2025-11-30 04:25:00 | NPP-375D | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5eab7357-cc61-32d4-906c-12e1840f3c78 | -12.00969 | -49.27428 | 2025-11-30 04:25:00 | NPP-375D | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f981490a-f15f-3c7f-ac57-840bfd028aa7 | -4.2732 | -40.66993 | 2025-11-30 04:25:00 | NPP-375D | PIRES FERREIRA | CEARÁ | Brasil | 2310951 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 1f719af2-9f7e-3149-b2ec-5dc48f571551 | -12.83206 | -47.3916 | 2025-11-30 04:25:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 35745578-654c-3097-bf2b-527592375cf1 | -13.72567 | -48.73827 | 2025-11-30 04:25:00 | NPP-375D | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| a35121e0-d5f6-39b1-8eb8-31b0d031be0d | -2.8718 | -46.70366 | 2025-11-30 04:25:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 25b4da89-7f2d-338c-abdb-dd5943e79fb1 | -4.4478 | -44.48982 | 2025-11-30 04:25:00 | NPP-375D | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8ee77f4c-5383-3fe8-b7f5-17e7c9b29c76 | -4.44448 | -44.4893 | 2025-11-30 04:25:00 | NPP-375D | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 484ec046-cdd0-3e12-a677-7f20ae29690e | -2.57639 | -49.09796 | 2025-11-30 04:25:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c0e98704-133b-30b4-820b-6c5f29a8bed9 | -3.44476 | -45.41547 | 2025-11-30 04:25:00 | NPP-375D | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d37ca3db-386c-34a7-bf0c-b8ae609f0b14 | -4.41732 | -44.4461 | 2025-11-30 04:25:00 | NPP-375D | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fe299850-3d46-37b9-a391-3af4ab95d5b8 | -2.92654 | -48.22925 | 2025-11-30 04:25:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 47d869d6-3f63-3df6-97b1-199d5e47da5f | -2.59604 | -49.26403 | 2025-11-30 04:25:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 81c884cf-0405-396e-98c3-5ecb04830de3 | -2.65757 | -48.1306 | 2025-11-30 04:25:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f11a5830-23a5-3448-884a-29da1a45f160 | -3.97547 | -42.52001 | 2025-11-30 04:25:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 3e1c7dae-83c3-3523-8825-b22cb6829491 | -2.64674 | -48.02684 | 2025-11-30 04:25:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 11ccd81f-8d57-3d22-bd13-48fa908db526 | -4.21678 | -44.32279 | 2025-11-30 04:25:00 | NPP-375D | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5c346cda-56ca-3a74-a4e2-e25f99f9a5f0 | -2.9637 | -49.21595 | 2025-11-30 04:25:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 582caba4-19a1-3bb8-a3ed-5ef01c613da1 | -12.50652 | -52.39049 | 2025-11-30 04:25:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4a8da944-8596-3a02-a2f8-12ad7e2cc488 | -3.87982 | -42.30606 | 2025-11-30 04:25:00 | NPP-375D | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 080b00f9-5dce-3ec8-9c8c-245d89b101bd | -12.00315 | -49.26874 | 2025-11-30 04:25:00 | NPP-375D | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0168a70f-10ea-3dfe-86b2-617e7633479d | -13.62717 | -49.6559 | 2025-11-30 04:25:00 | NPP-375D | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4ec3d94c-f1dd-39a8-b229-bd88263d4549 | -5.11238 | -43.29281 | 2025-11-30 04:25:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a9d240b0-58fd-3160-af78-c926e81536b1 | -2.70597 | -48.35369 | 2025-11-30 04:25:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| aa3c2308-5ecf-31c3-a71b-798f6deb6bdf | -12.70891 | -46.79183 | 2025-11-30 04:25:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |


[Clique aqui para ver as próximas entradas](README14.md)
