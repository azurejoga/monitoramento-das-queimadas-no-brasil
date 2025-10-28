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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 54b00b22-a3b7-3f7e-8bd5-4cd204f2f931 | -3.5831 | -43.634 | 2025-10-28 00:00:00 | GOES-19 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 92.8 |
| c669cced-4e2a-3159-bab3-58995bd9bdc5 | -4.3814 | -44.2603 | 2025-10-28 00:00:00 | GOES-19 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 1cfc3204-0f7a-30d5-94d0-b7855ac59175 | -2.737 | -45.4002 | 2025-10-28 00:00:00 | GOES-19 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 45.0 |
| 7da837e1-2a92-3ecb-b90a-61b127051a73 | -5.2773 | -44.3193 | 2025-10-28 00:00:00 | GOES-19 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 60.3 |
| da488fa5-b959-3bc5-953d-af10fca26211 | -6.7061 | -42.0517 | 2025-10-28 00:00:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 181.1 |
| 0e0ece5f-5d51-32d7-bf68-c2c4f16a277a | -10.5683 | -49.8018 | 2025-10-28 00:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 6ddb74a3-32d3-34ac-8996-5b15a05a9cb7 | -13.5655 | -49.5845 | 2025-10-28 00:00:00 | GOES-19 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 112.6 |
| bd68a922-b2a6-386c-b9b1-990b6da42932 | -10.9216 | -50.2571 | 2025-10-28 00:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 65.6 |
| ded4807a-b134-3fd2-acb2-c6e78fbde275 | -6.0974 | -44.6718 | 2025-10-28 00:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 51.1 |
| 6069a2ba-812c-3d5f-a5dd-b50d9e1e4b9e | -4.381 | -44.3061 | 2025-10-28 00:00:00 | GOES-19 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 79.5 |
| d119e0bb-8e8b-30b7-9ae1-5d71d42d8516 | -10.9402 | -50.2764 | 2025-10-28 00:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 7e0d6b96-8766-3271-82cf-10648f681fb4 | -12.629 | -45.0749 | 2025-10-28 00:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 97.9 |
| f0a77306-bacc-3c98-b5de-8d7d8689c0d7 | -3.914 | -60.598 | 2025-10-28 00:00:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 45.5 |
| 848e9eb6-7d91-338d-bb40-85534845ec2c | -4.3625 | -44.2842 | 2025-10-28 00:00:00 | GOES-19 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 569.1 |
| 641f6cb7-ed98-37de-a8a6-5fe327917297 | -10.9213 | -50.2785 | 2025-10-28 00:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 29d665f1-4721-3836-9e1f-0bc84053a8f1 | -11.2798 | -45.5052 | 2025-10-28 00:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 50.6 |
| e4d95122-16bb-35e2-9a1d-ff20c7514002 | -5.8572 | -46.4459 | 2025-10-28 00:00:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 85.5 |
| 16e48746-e463-3d86-a32c-8d4185df83ea | -14.1545 | -44.2527 | 2025-10-28 00:00:00 | GOES-19 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 0586e347-3c39-3918-a2fb-f4ff81290150 | -6.6875 | -42.0296 | 2025-10-28 00:00:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 255.8 |
| 300f5512-927c-3ea5-be2b-14dd61abdb47 | -8.6343 | -47.7181 | 2025-10-28 00:00:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 34.7 |
| 93e9cb80-a33c-3363-bc72-fbce17ebaf77 | -4.3627 | -44.2613 | 2025-10-28 00:00:00 | GOES-19 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 109.6 |
| 6fa7f56c-ec25-3f34-8b34-8ec9b5a448f6 | -10.9405 | -50.255 | 2025-10-28 00:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 55.0 |
| 29c21ece-1531-32ca-8a51-6d9bb925699c | -9.1371 | -51.299 | 2025-10-28 00:00:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 3152d188-2d9f-3052-86a8-7ec35b051d80 | -12.0808 | -45.6425 | 2025-10-28 00:00:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 73.3 |
| ee36b009-1e1c-3fed-bbcd-fe93738ec9f5 | -7.9835 | -45.5298 | 2025-10-28 00:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 49.9 |
| 597c711e-1cfb-3a40-8bd4-b65f594daf62 | -7.4541 | -49.4018 | 2025-10-28 00:00:00 | GOES-19 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 43.4 |
| 35f595e5-a66e-3035-9cb8-06a81eca25df | -6.7064 | -42.0278 | 2025-10-28 00:00:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 187.0 |
| adf40599-7018-3b08-a1b5-44c538516e86 | -4.7206 | -46.4276 | 2025-10-28 00:00:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 297b5369-4a45-3b2b-8815-28694388f9c6 | -10.5686 | -49.7803 | 2025-10-28 00:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 58.1 |
| b3dd253c-04a3-395a-99bc-c515514b79e6 | -2.7555 | -45.422 | 2025-10-28 00:00:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 59a4fe29-e74c-339b-b221-4e47ba98bc8f | -1.8608 | -54.5314 | 2025-10-28 00:00:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 20.2 |
| deb0e5e3-b861-3f62-9961-79a51acb2fe1 | -7.4539 | -49.4232 | 2025-10-28 00:00:00 | GOES-19 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 30.2 |
| ccfdd8ab-d55e-3674-83f9-39e5aad0ff46 | -1.8608 | -54.5114 | 2025-10-28 00:00:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 27.6 |
| 8cf1384e-0cfd-3fce-8237-9fdae001e9de | -2.7556 | -45.3995 | 2025-10-28 00:00:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 91.6 |
| 97e3efca-7eba-3f86-8629-62ac545c0744 | -5.794 | -35.6028 | 2025-10-28 00:00:00 | GOES-19 | IELMO MARINHO | RIO GRANDE DO NORTE | Brasil | 2404606 | 24 | 33 | nan | nan | nan | Caatinga | 68.5 |
| b73929cc-3b1f-336e-b04c-7750c82c2362 | -7.9882 | -46.7406 | 2025-10-28 00:00:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 104.7 |
| 13c2c962-4569-3d2c-b10e-7e80b6bc9948 | -10.568 | -49.8233 | 2025-10-28 00:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 43.4 |
| fc6b3b5b-1297-3a83-8174-e79e2b6369dd | -10.5872 | -49.7998 | 2025-10-28 00:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 39.7 |
| 61de7e58-0392-3c17-bd04-3d4cd6c81408 | -6.6873 | -42.0535 | 2025-10-28 00:00:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 230.3 |
| aeece464-c668-3f0d-bf2f-f8a0824dc163 | -7.9693 | -46.7423 | 2025-10-28 00:00:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 56.5 |
| 3224c482-c68a-3c12-a551-3992ef87cb33 | -4.3624 | -44.3072 | 2025-10-28 00:00:00 | GOES-19 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 123.7 |
| 5e9884e3-900e-3941-88f4-f4891449d263 | -4.3812 | -44.2832 | 2025-10-28 00:00:00 | GOES-19 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 332.7 |
| 016cbdec-ec0c-3a90-83c2-4f1f68224703 | -14.155 | -44.2289 | 2025-10-28 00:00:00 | GOES-19 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 103.3 |
| a86fc7ed-961a-3b0b-8aa9-1f6e1cd8f83f | -3.5833 | -43.6108 | 2025-10-28 00:00:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 767b8291-0525-3804-9e30-0b878c5a72f2 | -14.155 | -44.2289 | 2025-10-28 00:10:00 | GOES-19 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 102.0 |
| 63d27a7e-5705-3b86-9d8d-8ce08ae29f2d | -3.7205 | -45.7203 | 2025-10-28 00:10:00 | GOES-19 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 62.5 |
| b3211ba0-ae1e-36ee-b640-2dc07aca91f8 | -12.0996 | -45.6626 | 2025-10-28 00:10:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 89.2 |
| fcb431de-c113-304d-a78f-56d3fc7a1251 | -6.0974 | -44.6718 | 2025-10-28 00:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 55.3 |
| b43fc36d-16fc-3a3d-934d-0136d1d18fbb | -5.8572 | -46.4459 | 2025-10-28 00:10:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 2c5de2ac-a2ee-3f00-8096-6a2e5ad56b63 | -11.2798 | -45.5052 | 2025-10-28 00:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 72.1 |
| ea33af8a-1014-30f4-bb61-8c95809558a0 | -4.3625 | -44.2842 | 2025-10-28 00:10:00 | GOES-19 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 178.4 |
| 69d7ce4c-86df-3a68-943d-32eba8dbd4c9 | -14.3673 | -49.0068 | 2025-10-28 00:10:00 | GOES-19 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 97.1 |
| 03f6c592-569a-3aed-a1f1-a03a57e5ed11 | -7.9882 | -46.7406 | 2025-10-28 00:10:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 98.9 |
| 5b65836b-0530-3e79-91ee-b48611b33658 | -7.9368 | -49.7271 | 2025-10-28 00:10:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 31.6 |
| 6771b694-8071-3c66-84df-ab079cfb3525 | -7.9464 | -45.4882 | 2025-10-28 00:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 45.4 |
| c8a83d97-b06b-3106-b0bf-4526daa23106 | -2.7556 | -45.3995 | 2025-10-28 00:10:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 92.1 |
| bace5583-57cd-3d62-9f24-aaa974af946f | -14.1545 | -44.2527 | 2025-10-28 00:10:00 | GOES-19 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 73.9 |
| ccf33479-7a3a-35b3-a995-d68ec0ad7c97 | -1.8608 | -54.5114 | 2025-10-28 00:10:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 31.9 |
| 76444064-c581-3eff-b2f7-0b31f6ce40cf | -6.6873 | -42.0535 | 2025-10-28 00:10:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 163.4 |
| da46b9f9-da04-3ab8-ad73-da7ca7d84862 | -7.4541 | -49.4018 | 2025-10-28 00:10:00 | GOES-19 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 837165b0-f4cd-38a6-9299-35c1c2c835a2 | -9.1371 | -51.299 | 2025-10-28 00:10:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 2481bca6-16af-3331-abc8-7c9f88c6968e | -5.8386 | -46.4472 | 2025-10-28 00:10:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 8e80df50-b377-3c23-bfa0-1c9658bc5b5d | -10.9213 | -50.2785 | 2025-10-28 00:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 55.3 |
| ebcab262-2b94-3843-b2a8-22e74c1bc864 | -4.4602 | -43.6569 | 2025-10-28 00:10:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 42.1 |
| 7e788339-8c6e-3776-9873-6dc3497bb763 | -7.4539 | -49.4232 | 2025-10-28 00:10:00 | GOES-19 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 44.5 |
| df6fb393-27ae-347e-bd07-5866f034c7a5 | -10.5686 | -49.7803 | 2025-10-28 00:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 45.2 |
| 75dd26bb-e455-3ea6-b5b8-a5558ab3cb36 | -6.7061 | -42.0517 | 2025-10-28 00:10:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 168.3 |
| 9bcd401f-87ea-371c-925d-0b8feeae6a2d | -10.9405 | -50.255 | 2025-10-28 00:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 48.2 |
| fafea11c-2176-33d0-8e3c-460c4d40464d | -4.3812 | -44.2832 | 2025-10-28 00:10:00 | GOES-19 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 238.9 |
| 7413272d-2b96-3578-b58e-9d99a69150b6 | -10.5683 | -49.8018 | 2025-10-28 00:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 2e7f6639-cb30-3e59-858b-8eb1c04a57dd | -4.3814 | -44.2603 | 2025-10-28 00:10:00 | GOES-19 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 65.3 |
| 19b63b13-c879-38c9-aab8-0d24b39735fb | -10.5872 | -49.7998 | 2025-10-28 00:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 39.3 |
| 7a7d350f-483d-3535-bf83-b177c454c57a | -10.9216 | -50.2571 | 2025-10-28 00:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 53.0 |
| c3571b8e-447f-31fd-a9b5-1cc8919b4c0d | -12.0804 | -45.6655 | 2025-10-28 00:10:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 103.4 |
| fc8c9ea5-5b4a-3ac9-9f0f-3a92bd82a3af | -8.6343 | -47.7181 | 2025-10-28 00:10:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 23.9 |
| 948902cc-bfb1-3b5e-b3d1-6ed2cff6b7b9 | -6.6875 | -42.0296 | 2025-10-28 00:10:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 203.8 |
| ca3ba793-77b5-3a8c-9f83-b89f4fe6d657 | -8.646 | -45.2806 | 2025-10-28 00:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 69.5 |
| fc1d83c3-be99-3824-a801-2c6c2c07fb3e | -10.9402 | -50.2764 | 2025-10-28 00:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 49d66e49-9b7c-3ebd-87d8-119887c7db11 | -1.8608 | -54.5314 | 2025-10-28 00:10:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 19.8 |
| 16487c5b-4d6d-34c8-aa7f-f7f827ea96ab | -12.629 | -45.0749 | 2025-10-28 00:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 65.3 |
| 1c78c8a2-2343-3c1a-87a2-656a566b8a45 | -7.965 | -45.509 | 2025-10-28 00:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 36.8 |
| 6f393adb-3b01-3f4f-b805-6b6734380ec8 | -3.5833 | -43.6108 | 2025-10-28 00:10:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 29.5 |
| 5176f829-b74e-320a-9b1c-23b8033ecdab | -2.7555 | -45.422 | 2025-10-28 00:10:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 88.9 |
| 53e513df-0812-3639-bd22-45d9b2f84d14 | -7.9647 | -45.5317 | 2025-10-28 00:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 29.2 |
| a0518ccc-d8d7-3cfd-9811-39cbe721c775 | -6.7064 | -42.0278 | 2025-10-28 00:10:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 198.8 |
| f8566bcc-0c0f-3374-8e07-b095c5e1146f | -10.568 | -49.8233 | 2025-10-28 00:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 40.7 |
| a0a1024e-d53f-3e26-a691-cbf7707b933f | -4.381 | -44.3061 | 2025-10-28 00:10:00 | GOES-19 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 58.0 |
| 9dd2b6b4-dec4-3687-9270-7f563403b515 | -3.5831 | -43.634 | 2025-10-28 00:10:00 | GOES-19 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 64.4 |
| c6598fd9-aa6b-3bc3-88b6-68ccb00d519f | -6.7061 | -42.0517 | 2025-10-28 00:20:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 148.7 |
| d89ad436-4fd8-3074-9033-e5ecff9466c0 | -5.8572 | -46.4459 | 2025-10-28 00:20:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 0b676a45-4e1b-3b50-aee2-2615edd21aa0 | -6.6873 | -42.0535 | 2025-10-28 00:20:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 183.0 |
| e2982236-d5e3-3020-9e11-4a03a15507f9 | -10.9213 | -50.2785 | 2025-10-28 00:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 2ddc33cd-17b9-32b5-8340-55dd4a8f5c24 | -10.5686 | -49.7803 | 2025-10-28 00:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 37.4 |
| e46e5b7d-2468-3d7b-91af-f514452db66b | -14.3673 | -49.0068 | 2025-10-28 00:20:00 | GOES-19 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 210d5c72-a04d-3967-9e15-8df43c781bb9 | -7.4539 | -49.4232 | 2025-10-28 00:20:00 | GOES-19 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 81.8 |
| 6f8c26dc-a0e6-3366-8a5f-b763c18bb813 | -6.6875 | -42.0296 | 2025-10-28 00:20:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 172.7 |
| e07c8369-b677-360d-955c-a14a2964aa8e | -7.4541 | -49.4018 | 2025-10-28 00:20:00 | GOES-19 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 122.2 |
| 71fba479-3b1b-3953-90e4-e1b63ab2dbab | -2.7556 | -45.3995 | 2025-10-28 00:20:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 89.0 |
| a58aeb89-3e92-39ea-97cc-5322d7b4b1f3 | -7.9647 | -45.5317 | 2025-10-28 00:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 81.1 |
| b30db454-a00f-3ecc-a985-2e5d4fe897af | -11.2798 | -45.5052 | 2025-10-28 00:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 87.4 |


[Clique aqui para ver as próximas entradas](README2.md)
