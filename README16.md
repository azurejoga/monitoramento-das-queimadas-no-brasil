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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 36fe0e22-5828-3118-b342-6b32c83156fc | -19.73152 | -54.50933 | 2025-05-23 04:27:00 | NOAA-20 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 09b3ce71-5a4d-3c42-8b24-6ea26a674ca2 | -17.31176 | -51.11095 | 2025-05-23 04:27:00 | NOAA-20 | MONTIVIDIU | GOIÁS | Brasil | 5213756 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 21995b0a-fcbd-3f07-b4a7-a13e444ba094 | -17.34261 | -51.90719 | 2025-05-23 04:27:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8e05f248-74b9-3693-b29f-a5acff025d77 | -19.95958 | -45.82891 | 2025-05-23 04:27:00 | NOAA-20 | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2ff99b03-830a-381c-82c4-9af578ddf71c | -20.76464 | -46.76812 | 2025-05-23 04:27:00 | NOAA-20 | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| e1d9d212-da43-3339-803d-9b5cc8cde317 | -16.70588 | -48.17627 | 2025-05-23 04:27:00 | NOAA-20 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 53d5c167-2bff-3b65-aee3-429a458a73c6 | -13.72075 | -58.67478 | 2025-05-23 04:27:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 19980eb7-7d02-3318-b3bf-91e319bc5e99 | -19.0199 | -57.62239 | 2025-05-23 04:27:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 586e1717-939a-363e-bd89-1f1e79fe9832 | -15.26456 | -51.47935 | 2025-05-23 04:27:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 6b5c366e-89d6-350b-9c76-1e84fa3bf5ff | -16.681 | -43.88592 | 2025-05-23 04:27:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| aaf601ea-415d-34ec-8ab8-efb0634882aa | -17.68161 | -46.82343 | 2025-05-23 04:27:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cf700026-e012-3103-9308-4af5ebb8256a | -17.59704 | -43.19731 | 2025-05-23 04:27:00 | NOAA-20 | CARBONITA | MINAS GERAIS | Brasil | 3113503 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b3b9045b-abfe-36d0-aeef-54e256b779d5 | -19.96801 | -44.21651 | 2025-05-23 04:27:00 | NOAA-20 | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| b2fb0466-51f9-3d25-80fd-a47bc3559db8 | -14.90842 | -51.05741 | 2025-05-23 04:27:00 | NOAA-20 | ARUANÃ | GOIÁS | Brasil | 5202502 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fd82b98c-b1aa-3d9c-8d86-61f0bd7acc20 | -20.94446 | -56.59155 | 2025-05-23 04:27:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 76beb928-bf9b-3e89-a1b3-923f5270861e | -15.26096 | -51.47871 | 2025-05-23 04:27:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9ddad258-664c-35db-a20c-b0eeac976332 | -14.026 | -55.14318 | 2025-05-23 04:27:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6998a6a0-e79c-3551-9e34-a84a8b15ceb8 | -15.62385 | -57.30737 | 2025-05-23 04:27:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1cc714af-365b-3d70-a888-2a1ac0a7755e | -13.97962 | -56.00637 | 2025-05-23 04:27:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 4b6e2d6a-28ca-3c07-890f-fda8437a1733 | -16.35331 | -50.05756 | 2025-05-23 04:27:00 | NOAA-20 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b73e9ddd-0e6b-3fc8-a760-81ba587b86e5 | -20.84923 | -53.74783 | 2025-05-23 04:27:00 | NOAA-20 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 407d8d8c-a566-362d-8a49-189d6721b477 | -13.98341 | -56.0128 | 2025-05-23 04:27:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 4df8e4a8-f968-3549-a3cd-17a0021de9ec | -14.02143 | -55.14228 | 2025-05-23 04:27:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c1e70ace-36b1-32d2-b1a8-a680e92d9e81 | -20.70514 | -54.89128 | 2025-05-23 04:27:00 | NOAA-20 | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b68f396c-5ba8-3546-ac47-b15c08dd882c | -19.79763 | -53.83791 | 2025-05-23 04:27:00 | NOAA-20 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7aff8c02-986b-3c34-9fa6-5a9a83085d77 | -13.85542 | -59.72702 | 2025-05-23 04:27:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8bf71dfa-d960-3630-95f0-971c9551e8ad | -22.49477 | -43.51192 | 2025-05-23 04:27:00 | NOAA-20 | MIGUEL PEREIRA | RIO DE JANEIRO | Brasil | 3302908 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 18039d65-cae7-36db-a6a3-c035ce0980b7 | -17.57856 | -47.48576 | 2025-05-23 04:27:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 46629cb2-4ebf-3318-8b9d-d4f25c8314d3 | -20.41831 | -43.55305 | 2025-05-23 04:27:00 | NOAA-20 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 363ed983-fe47-30bd-9a73-f544f129d0ba | -22.47871 | -53.5779 | 2025-05-23 04:29:00 | NOAA-20 | IVINHEMA | MATO GROSSO DO SUL | Brasil | 5004700 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 7055504f-7cb0-3835-a06b-70c5bdc9e874 | -21.71746 | -55.37199 | 2025-05-23 04:29:00 | NOAA-20 | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 7.8 |
| c49783dd-e995-3e3f-a6df-c3c9a579ac42 | -21.4681 | -57.17275 | 2025-05-23 04:29:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 22f19dae-bd2c-33f7-b685-a01ecc42d011 | -21.46713 | -57.17749 | 2025-05-23 04:29:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 44d1b2fa-1b25-378c-bccf-cf95c4836714 | -21.46709 | -56.29608 | 2025-05-23 04:29:00 | NOAA-20 | JARDIM | MATO GROSSO DO SUL | Brasil | 5005004 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 94789026-9122-3316-9e86-6654b010dfdf | -21.7248 | -55.37756 | 2025-05-23 04:29:00 | NOAA-20 | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 05c83d7f-03d5-3de4-93a9-3d3b394dd72a | -21.71819 | -55.36819 | 2025-05-23 04:29:00 | NOAA-20 | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 62e71569-a68f-3b79-898c-688c96c60073 | -21.7215 | -55.37287 | 2025-05-23 04:29:00 | NOAA-20 | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 03a47989-f5d8-381c-9d9a-1998d5f3afa6 | -13.9818 | -56.0151 | 2025-05-23 04:30:00 | GOES-19 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 67.1 |
| d055301b-bc51-3e16-8935-44dfb9afa769 | -6.2224 | -43.3693 | 2025-05-23 04:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 072db013-4809-39cf-8fb9-1c78e610b5ed | -30.66859 | -52.79981 | 2025-05-23 04:32:00 | NOAA-20 | ENCRUZILHADA DO SUL | RIO GRANDE DO SUL | Brasil | 4306908 | 43 | 33 | nan | nan | nan | Pampa | 0.7 |
| b0fb7f83-3f5c-347a-a658-3a6c755cf0a5 | -29.77591 | -51.17572 | 2025-05-23 04:32:00 | NOAA-20 | SÃO LEOPOLDO | RIO GRANDE DO SUL | Brasil | 4318705 | 43 | 33 | nan | nan | nan | Pampa | 1.3 |
| c3b98836-9e81-3ef9-9fe9-fea95e289a36 | -29.77924 | -51.17638 | 2025-05-23 04:32:00 | NOAA-20 | SÃO LEOPOLDO | RIO GRANDE DO SUL | Brasil | 4318705 | 43 | 33 | nan | nan | nan | Pampa | 1.3 |
| 5f0d9a9f-08db-31a2-a878-c0954026dc3c | -29.87358 | -51.15704 | 2025-05-23 04:32:00 | NOAA-20 | CANOAS | RIO GRANDE DO SUL | Brasil | 4304606 | 43 | 33 | nan | nan | nan | Pampa | 0.8 |
| cc6da00a-264d-386b-9f97-c3df7b229c61 | -13.9818 | -56.0151 | 2025-05-23 04:40:00 | GOES-19 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 50.7 |
| 3e3f7db6-0205-394e-907d-d4c12dfe9199 | -6.2224 | -43.3693 | 2025-05-23 04:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 74.2 |
| ba537cea-5a7b-3198-a31d-504889fed0dd | -13.9818 | -56.0151 | 2025-05-23 04:50:00 | GOES-19 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 58.9 |
| f5d776db-1d03-3da9-a2c1-bf1a69daf902 | -7.0695 | -44.9335 | 2025-05-23 04:50:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 59.3 |
| a9d7d923-1410-3ea7-9a6b-04602664516a | -6.2224 | -43.3693 | 2025-05-23 04:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 9ce0a877-fafc-39f3-b855-18978dc5ddd8 | -6.2224 | -43.3693 | 2025-05-23 05:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 8bfed840-8169-331e-bc15-63402d299620 | -13.9818 | -56.0151 | 2025-05-23 05:00:00 | GOES-19 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 66.0 |
| 7b973c69-140d-3fef-ab3a-9428e9145194 | -13.9818 | -56.0151 | 2025-05-23 05:10:00 | GOES-19 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 44.7 |
| 85d491fb-bc96-3783-a45c-dd66894bf2b8 | -8.72272 | -50.2561 | 2025-05-23 05:16:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c2f38314-8922-376a-8690-7e74ef860bb8 | -5.57904 | -45.19896 | 2025-05-23 05:16:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 2339085a-80de-3265-9e75-419efb38c237 | -7.71079 | -45.6652 | 2025-05-23 05:16:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f2dcf95d-447e-37e8-a2fb-d0e4b6f2a68f | -8.48606 | -49.60759 | 2025-05-23 05:16:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6b49a580-1b32-3972-b29e-ed9837a2fe70 | -2.58321 | -51.92427 | 2025-05-23 05:16:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0a13df47-6ed4-373d-b9c7-5c14838475b1 | -7.71164 | -45.65834 | 2025-05-23 05:16:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c9f026c0-63f4-3d23-b3cb-ff32e203e7f9 | -8.48047 | -49.6069 | 2025-05-23 05:16:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| a055c0d1-be2f-3328-9635-3857b4483d0c | -8.48 | -49.61056 | 2025-05-23 05:16:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 4fd32a24-661b-3688-8443-bfa418f7c38b | -7.71868 | -45.65936 | 2025-05-23 05:16:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 644dcb98-896e-3eec-9934-9697fcbf9728 | -2.58818 | -51.92082 | 2025-05-23 05:16:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6219e3eb-ff7c-3c08-8291-a91ff00ccefa | -5.57813 | -45.20578 | 2025-05-23 05:16:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 89a192ca-dbc4-3ec7-9fe2-7e72c64b0703 | -7.71368 | -45.66026 | 2025-05-23 05:16:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 76e5e352-c7a9-3304-9a5e-2e7e0efc0bd3 | -14.04455 | -53.37954 | 2025-05-23 05:18:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8de7d651-f610-33f3-8617-c827058666a2 | -10.31561 | -59.57 | 2025-05-23 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| af1c1076-531c-36f9-b630-e01705deec16 | -10.98834 | -59.15532 | 2025-05-23 05:18:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 17edd787-5eef-32ab-8fbb-fb81bd62200b | -12.30337 | -52.49174 | 2025-05-23 05:18:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 61ed1de0-7a36-395b-975c-3a30bd6eb00e | -8.16721 | -61.47915 | 2025-05-23 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b81ea2d6-7fa7-3cd0-8379-42917a19494c | -11.08919 | -57.27248 | 2025-05-23 05:18:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| c2fadae7-ab30-3624-b9e3-2cd2b70d5515 | -13.24759 | -56.54419 | 2025-05-23 05:18:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 02b595b3-0cf2-357e-a9d6-86f4434b1586 | -13.78631 | -54.30893 | 2025-05-23 05:18:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 3d3920ce-2969-3535-b692-af12ffb68b0e | -10.73162 | -59.32052 | 2025-05-23 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8d1bcee0-8210-3585-9817-bad1cefb812d | -11.30812 | -54.02734 | 2025-05-23 05:18:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0e689b8b-30d2-3d91-b0b1-ec0b40c02f51 | -12.34253 | -49.98256 | 2025-05-23 05:18:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 76949e69-3689-3fd5-b131-d233f7345e5c | -11.5717 | -54.56362 | 2025-05-23 05:18:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c84d7df6-e975-3332-a4ac-e8407c917738 | -13.78139 | -54.31258 | 2025-05-23 05:18:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| b1f63bb6-be18-31bf-95d1-78ec980d8331 | -10.12117 | -58.22261 | 2025-05-23 05:18:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4d526a81-f998-385e-a265-fa873a182ece | -12.13595 | -54.66265 | 2025-05-23 05:18:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2b017cec-4efc-3e4b-aea8-6526600eba26 | -12.32802 | -49.99146 | 2025-05-23 05:18:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 71f31896-bd04-32c1-b016-e8ecfab2f155 | -9.48854 | -57.15882 | 2025-05-23 05:18:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 03634ebd-e52e-3a22-88aa-47ae822314c1 | -12.29232 | -52.50125 | 2025-05-23 05:18:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 60b5d62a-2c46-3855-ac3c-0f191a838c35 | -12.41846 | -49.98031 | 2025-05-23 05:18:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 37133c48-2e8f-39d4-904d-bd02a8c0135e | -11.32718 | -58.62355 | 2025-05-23 05:18:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 52de2762-1a32-319c-ba3a-5f8d9b7b06a3 | -13.18388 | -53.57574 | 2025-05-23 05:18:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c9952aa7-500f-3f75-b3aa-5001793f5501 | -9.11312 | -63.5749 | 2025-05-23 05:18:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9fafae15-e7c2-3b79-ade4-aa47cce9d570 | -10.71293 | -48.82236 | 2025-05-23 05:18:00 | NOAA-21 | OLIVEIRA DE FÁTIMA | TOCANTINS | Brasil | 1715507 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 23d129cf-0b6c-33d7-a803-1d62d0362a11 | -12.41799 | -49.98431 | 2025-05-23 05:18:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c9fc22e3-d3a0-351d-ad8e-5408fd6e48dd | -13.98445 | -56.01361 | 2025-05-23 05:18:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 15.4 |
| b447c3a7-4ae7-3f8b-8731-624ede609500 | -10.29423 | -57.14124 | 2025-05-23 05:18:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8e023cd2-3819-3d98-a01f-dedb68db984f | -13.98514 | -56.00846 | 2025-05-23 05:18:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 15.4 |
| eb23ff21-f91c-384c-b218-766bdf2aa388 | -14.03988 | -53.37889 | 2025-05-23 05:18:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b927565e-65ca-3d13-99de-a5d937de58ee | -11.81031 | -57.36173 | 2025-05-23 05:18:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 81a66b13-ed6a-3f90-91c6-03d5de174909 | -11.30717 | -54.02114 | 2025-05-23 05:18:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4b54464d-080b-38db-8b83-97e864a04c36 | -11.32773 | -58.6199 | 2025-05-23 05:18:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8aee8199-4506-3827-a8fe-5a3a877c7ea7 | -8.16782 | -61.47538 | 2025-05-23 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0eb5ebb2-c66d-31df-9343-b033cedb5da4 | -14.04115 | -53.36884 | 2025-05-23 05:18:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| fc6b41d5-3d49-3bda-815e-2fbafa62e377 | -12.29784 | -52.49651 | 2025-05-23 05:18:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| fd6b8b8e-a9d6-35c1-b034-4dcdd7fe448a | -10.37091 | -57.49842 | 2025-05-23 05:18:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 8e3581e6-14e8-38e6-8744-5fcb7042b875 | -11.30496 | -54.01856 | 2025-05-23 05:18:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fb8b60c2-caf7-3de0-be9b-1a0429d82a95 | -12.72031 | -54.97455 | 2025-05-23 05:18:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |


[Clique aqui para ver as próximas entradas](README17.md)
