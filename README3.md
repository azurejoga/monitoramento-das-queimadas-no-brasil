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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ab4ece8a-5078-3aaa-b572-1505455fd7b3 | -28.87569 | -51.36219 | 2025-03-06 04:46:00 | NOAA-21 | ANTÔNIO PRADO | RIO GRANDE DO SUL | Brasil | 4300802 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| a19893d5-5cfa-36a7-92cc-ec6c620ac9b6 | -30.29951 | -54.6731 | 2025-03-06 04:46:00 | NOAA-21 | SÃO GABRIEL | RIO GRANDE DO SUL | Brasil | 4318309 | 43 | 33 | nan | nan | nan | Pampa | 0.7 |
| 642bdbe4-f4a6-353c-ac34-4b1be1959639 | -30.29618 | -54.67242 | 2025-03-06 04:46:00 | NOAA-21 | SÃO GABRIEL | RIO GRANDE DO SUL | Brasil | 4318309 | 43 | 33 | nan | nan | nan | Pampa | 1.1 |
| 3145b1de-46b9-3881-a162-6ba50e37d01a | -29.58324 | -51.98636 | 2025-03-06 04:46:00 | NOAA-21 | ESTRELA | RIO GRANDE DO SUL | Brasil | 4307807 | 43 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 3804aa52-ddbf-3194-aea5-6c9cd9c53bbf | 3.32252 | -61.24015 | 2025-03-06 05:01:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7c6a49d9-e017-32b7-a56d-2e9304ec80ad | 3.32737 | -61.23947 | 2025-03-06 05:01:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f18a132a-eaae-3309-9e68-b63f133d6a7a | 2.84535 | -60.85886 | 2025-03-06 05:01:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bd68fab8-e4e1-3dc6-ac42-b3c9a6ebee7f | 2.2684 | -60.25322 | 2025-03-06 05:01:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3cc6fa87-0101-3f24-857c-d058a4ad2198 | 0.89304 | -60.43196 | 2025-03-06 05:01:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 76ce6b78-8963-326f-9452-a4060926f701 | 2.85151 | -60.86792 | 2025-03-06 05:01:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 19f42cac-b33c-31a0-af55-5af44a03236c | 2.35559 | -61.00823 | 2025-03-06 05:01:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ab170c7e-2fe7-3880-91c9-4ed29e20a208 | 2.84758 | -60.87353 | 2025-03-06 05:01:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 32d36770-76c5-34c8-babc-771118c74610 | 1.79677 | -60.26901 | 2025-03-06 05:01:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 65506ddb-7b1e-3288-90b4-014b093a403f | 2.84609 | -60.86375 | 2025-03-06 05:01:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d59f14a0-afcf-3c5e-91ec-6618e826edf0 | 2.30747 | -60.21123 | 2025-03-06 05:01:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b184739a-1019-3631-9119-fdc0207d7f30 | 2.37833 | -60.23783 | 2025-03-06 05:01:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2e7659b7-706e-356e-be04-6d47c3bf79bc | 2.30682 | -60.20699 | 2025-03-06 05:01:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| aff155c1-6a0d-3b58-b77e-978a8e15409e | 0.77282 | -60.40975 | 2025-03-06 05:01:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 203fa2c6-8f38-3971-9929-f98c19475ac7 | 2.30304 | -60.21196 | 2025-03-06 05:01:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6aeb6610-a9b8-3c12-b2da-146b6f55a579 | 3.32656 | -61.23409 | 2025-03-06 05:01:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 148238aa-94ed-31f9-ad34-7ef49fd6055c | 2.26904 | -60.25748 | 2025-03-06 05:01:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c53de01d-bc9b-3f83-8dd1-a374e49ba016 | 2.36818 | -60.70094 | 2025-03-06 05:01:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c2e03243-5f9e-3d79-bdd7-d189e0da13c9 | 2.37385 | -60.23833 | 2025-03-06 05:01:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2e55f249-e732-3f51-be20-3279ccca6847 | 0.8938 | -60.43463 | 2025-03-06 05:01:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fbdc6092-d809-3721-822c-3e4d26200ef2 | 2.62936 | -60.41772 | 2025-03-06 05:01:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 74bfbf77-1aab-3321-940e-8ecad4f0c1c3 | 3.32171 | -61.23471 | 2025-03-06 05:01:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 25702daf-764d-3e43-aead-35e7f79957c1 | -13.35144 | -47.01419 | 2025-03-06 05:05:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 7e204fe9-6211-36bc-b56f-e503aad21e3c | -10.53413 | -44.66895 | 2025-03-06 05:05:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 17a9a7af-7a19-3e3b-98bd-4b9b8c89c141 | -10.53479 | -44.66349 | 2025-03-06 05:05:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a1f0b50d-2ef6-38d9-9d88-2fad4a1d27d1 | -13.35079 | -47.01228 | 2025-03-06 05:05:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 8c0630dd-f6bf-3a97-bc42-d996cda2d2b2 | -13.35191 | -47.00999 | 2025-03-06 05:05:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fdf897d3-ad11-35da-ada4-6853c95c220f | -13.35031 | -47.01636 | 2025-03-06 05:05:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 01eee85b-9308-3234-b06e-7f4a336e92e8 | -20.91147 | -56.53334 | 2025-03-06 05:08:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| be7e2397-8e8b-3ef2-bfec-d3e0b955e790 | -21.69214 | -50.35312 | 2025-03-06 05:08:00 | NPP-375D | LUIZIÂNIA | SÃO PAULO | Brasil | 3527702 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 3f8c5290-51f0-38f3-ad56-b00b38d36b82 | -21.69181 | -50.35643 | 2025-03-06 05:08:00 | NPP-375D | LUIZIÂNIA | SÃO PAULO | Brasil | 3527702 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 8f5ba8e3-85dc-39b3-951b-48f34259c710 | -20.72017 | -49.43533 | 2025-03-06 05:08:00 | NPP-375D | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Cerrado | 9.1 |
| a1327c2d-cdce-3fd2-9c8a-e0786fd617ce | -20.7259 | -49.43256 | 2025-03-06 05:08:00 | NPP-375D | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 45b0055b-e930-3cb1-b030-75c1366e1817 | -20.72382 | -49.43351 | 2025-03-06 05:08:00 | NPP-375D | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 96bbc587-1664-3fc5-ad4f-d46cf98d8117 | -20.91499 | -56.53392 | 2025-03-06 05:08:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| da837fb6-7927-33b8-a1df-84338fb1a9fe | -20.72345 | -49.43702 | 2025-03-06 05:08:00 | NPP-375D | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Cerrado | 10.0 |
| e789bd32-efb0-3ecd-87aa-b5f8939d970f | -21.58319 | -57.58143 | 2025-03-06 05:08:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9b91351b-3b1b-32e4-a6d3-ab55c177a81d | -20.7205 | -49.43185 | 2025-03-06 05:08:00 | NPP-375D | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Cerrado | 5.0 |
| db87375e-e3f3-3c61-9481-689b8d4c147d | -20.72556 | -49.43607 | 2025-03-06 05:08:00 | NPP-375D | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2bed4e46-699b-3f43-8f7d-eb670c8dd7c7 | -15.31423 | -60.01816 | 2025-03-06 05:08:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fb1e6e54-fd56-3d08-bd52-1103c478869e | -29.58161 | -51.98804 | 2025-03-06 05:10:00 | NPP-375D | ESTRELA | RIO GRANDE DO SUL | Brasil | 4307807 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 0eb1286c-a55b-3b81-be47-844e3b80e2a9 | -23.29581 | -49.37434 | 2025-03-06 05:10:00 | NPP-375D | TEJUPÁ | SÃO PAULO | Brasil | 3554201 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 5bc42747-fa0f-3879-8941-ecbbfbebe150 | -29.58189 | -51.98466 | 2025-03-06 05:10:00 | NPP-375D | ESTRELA | RIO GRANDE DO SUL | Brasil | 4307807 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| ab695276-90c8-3323-9016-15c8125c56e2 | -30.29487 | -54.67268 | 2025-03-06 05:12:00 | NPP-375D | SÃO GABRIEL | RIO GRANDE DO SUL | Brasil | 4318309 | 43 | 33 | nan | nan | nan | Pampa | 5.1 |
| 0812c2f4-a7ea-3330-81ef-80ec2a3a5df3 | 3.73119 | -59.73005 | 2025-03-06 05:25:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 74c63c30-48c4-30b1-8655-1da91ce89477 | 3.87979 | -59.61885 | 2025-03-06 05:25:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e5051afe-3fe5-3ab8-aff2-7f71833e7215 | 4.23291 | -60.69848 | 2025-03-06 05:25:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4d763e8c-4e55-3d34-aa17-4db2c971fff6 | 4.98067 | -60.4164 | 2025-03-06 05:25:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 0a4b1891-c3b4-3409-977f-9f6c1ccda8d2 | 2.11779 | -61.81691 | 2025-03-06 05:27:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1fb68e2f-d234-3acd-9c9b-d08e0527633a | 0.86134 | -59.35794 | 2025-03-06 05:27:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c2f08165-cf1b-3beb-9404-0a9ad9ca397f | 1.8525 | -60.58041 | 2025-03-06 05:27:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 17071464-d5aa-3faf-b3b7-dad4c1776387 | 2.62639 | -60.42054 | 2025-03-06 05:27:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 26c4c3c1-8a6b-3110-b3b5-92be2f6c69d4 | 2.11723 | -61.81332 | 2025-03-06 05:27:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1d6e2146-efed-3e92-9279-9424896bf61d | 2.62585 | -60.41711 | 2025-03-06 05:27:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 9460bfca-64d9-34e2-bf01-d9751f213ea1 | 1.8558 | -60.5799 | 2025-03-06 05:27:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 5.0 |
| d7d37188-c139-3ea1-861e-b144eb390b06 | 2.11497 | -61.82105 | 2025-03-06 05:27:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5a5ee3c6-a04b-33dc-8e45-311e993da15d | 2.62969 | -60.42004 | 2025-03-06 05:27:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 35da6641-2ab4-3d5b-8cde-2527c3f4a255 | 2.3242 | -60.20765 | 2025-03-06 05:27:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6d70239c-ae99-32ea-ba63-1a2eba0cfa75 | 1.13833 | -60.44663 | 2025-03-06 05:27:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 56129c05-a227-36a8-a081-c564eb037096 | 1.12824 | -60.51136 | 2025-03-06 05:27:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 23ba1bd4-2d42-3013-9237-f9b3c70667a3 | 0.95658 | -60.00432 | 2025-03-06 05:27:00 | NOAA-20 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 53db94c5-6e65-34f9-870e-8ad1a0637fce | 2.35425 | -61.00439 | 2025-03-06 05:27:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9f273b76-b628-31d1-827f-e0324fb00a0b | 0.83841 | -59.96671 | 2025-03-06 05:27:00 | NOAA-20 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 193e29cf-e1fd-3aa5-b0af-46a361c9c980 | 2.85475 | -60.85869 | 2025-03-06 05:27:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 4.5 |
| d85b695a-4f2a-3e1e-b7ad-844d30d13019 | 1.94113 | -60.3876 | 2025-03-06 05:27:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d0fbcd8c-7fcd-3bb6-b483-a61c48c30b7a | 2.36729 | -60.69698 | 2025-03-06 05:27:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8ae37f25-51bb-3304-9af6-bdc124d24576 | 0.75088 | -60.59859 | 2025-03-06 05:27:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 134e7b64-f5e2-365f-96ef-1d4b327fd99e | 3.23468 | -61.20248 | 2025-03-06 05:27:00 | NOAA-20 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0da2f990-7a0c-3b08-91c2-f7b1002ba2ec | 1.85304 | -60.58385 | 2025-03-06 05:27:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9759ead3-3738-338f-9eda-d8ec1d3d93db | 3.32127 | -61.23612 | 2025-03-06 05:27:00 | NOAA-20 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 4.7 |
| bb7161d1-6251-347e-b44c-86c3c3a306c0 | 1.85196 | -60.57698 | 2025-03-06 05:27:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 5.0 |
| b376e5a1-babe-38d2-81c8-31464168063d | 1.8591 | -60.57939 | 2025-03-06 05:27:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 560193b5-4412-3233-bff9-8ab8b6664002 | 1.04045 | -60.06159 | 2025-03-06 05:27:00 | NOAA-20 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b3353642-dba0-3332-88e8-5bca8f9f629d | 1.85964 | -60.58281 | 2025-03-06 05:27:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6e53d210-5c70-3e70-91ca-ef239f23c554 | 3.32463 | -61.23562 | 2025-03-06 05:27:00 | NOAA-20 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 4.7 |
| ef7dd7d5-2d4b-3542-b3d3-64b9a4ac046f | 3.32518 | -61.23919 | 2025-03-06 05:27:00 | NOAA-20 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f978143c-f0fe-3bf0-a05b-407c2e9fc714 | 1.13538 | -60.51376 | 2025-03-06 05:27:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cf920c56-724a-3f58-9d82-82178b3b91be | 2.84757 | -60.85624 | 2025-03-06 05:27:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e2273d49-912e-34c4-b8e5-2e366c67783b | 1.94941 | -60.37579 | 2025-03-06 05:27:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 23c8a844-4d82-3221-aa3f-2544a91d2d0e | 1.13484 | -60.51033 | 2025-03-06 05:27:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 844f6e40-7140-3d0d-92e9-e48f5c76e05d | 2.62861 | -60.41316 | 2025-03-06 05:27:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 455eff18-22da-38c0-856c-1f01eb5668c0 | 2.30771 | -60.21021 | 2025-03-06 05:27:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9c69e818-a816-3029-a0f1-ccf64a35fbf3 | 2.62531 | -60.41367 | 2025-03-06 05:27:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ab0f6ea5-1e09-3def-851f-f1c477d90ce7 | 2.35147 | -61.00836 | 2025-03-06 05:27:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 92da8d59-11c1-399f-ac6a-e96d17b910e7 | 2.37638 | -60.23507 | 2025-03-06 05:27:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 646f91d5-ac21-3146-9bf4-5cbe9e46e598 | 2.11385 | -61.81385 | 2025-03-06 05:27:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bd33fba1-1628-3221-94c3-001acc3b5436 | 2.10153 | -60.23931 | 2025-03-06 05:27:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c16aec33-3780-3c09-b5aa-1be9a8140400 | 0.89492 | -60.43239 | 2025-03-06 05:27:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ee69c2c0-1ad0-37bd-92e8-8dbb90e08953 | 3.32183 | -61.2397 | 2025-03-06 05:27:00 | NOAA-20 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7b1af09b-9fba-3a07-b36a-d46231f787e1 | 1.27115 | -60.34135 | 2025-03-06 05:27:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1f39d271-b1b5-31d5-8a30-64f31c1c588a | 2.10483 | -60.2388 | 2025-03-06 05:27:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 22dacfbc-8a88-3e60-9168-e2ddd8d2698a | 2.62693 | -60.42398 | 2025-03-06 05:27:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 6f50f214-28a4-3844-b403-bd50b0524906 | 2.10877 | -61.82574 | 2025-03-06 05:27:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0bb2bbd6-836d-36b1-b0c6-4943709a8506 | 0.95712 | -60.00775 | 2025-03-06 05:27:00 | NOAA-20 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fa40e62e-c82b-38e6-955b-f4dc2c8bbc26 | 1.94611 | -60.3763 | 2025-03-06 05:27:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c80b7cbc-4c0d-3d5a-8135-6bc6a965503f | 2.62915 | -60.4166 | 2025-03-06 05:27:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 6.5 |


[Clique aqui para ver as próximas entradas](README4.md)
