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
| ff33fdd7-ddbb-34fc-b1d7-1041200ff876 | -2.7369 | -45.4226 | 2025-10-28 01:00:00 | GOES-19 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 38.6 |
| 87fde941-f90b-3c5b-b2be-5dcb810db125 | -2.737 | -45.4002 | 2025-10-28 01:00:00 | GOES-19 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 40.8 |
| 7eb5f43d-909c-3564-9f54-586311e37700 | -12.629 | -45.0749 | 2025-10-28 01:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 92.9 |
| eeabef64-12f6-31e7-a938-1b8301387a3a | -4.4604 | -43.6337 | 2025-10-28 01:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 59.5 |
| 27779aca-fd26-3d70-9a61-c16b9e6c756b | -7.965 | -45.509 | 2025-10-28 01:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 90.8 |
| 2ddbeeb9-baf8-335e-aeb4-711c175d22de | -6.6873 | -42.0535 | 2025-10-28 01:00:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 127.8 |
| 880912af-116e-35f4-8c06-798da1befb25 | -10.568 | -49.8233 | 2025-10-28 01:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 32.8 |
| 461c5631-520a-3563-afdb-4cd460f3fbc1 | -7.9459 | -45.5335 | 2025-10-28 01:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 93.4 |
| 4cd9a556-7825-3ed5-8c3d-26db9ef5907f | -5.8386 | -46.4472 | 2025-10-28 01:00:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 75.5 |
| f686a6fc-0645-32de-b3ac-60bd702deecb | -6.7064 | -42.0278 | 2025-10-28 01:00:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 97.0 |
| 9189ba1b-567e-3783-a516-de84593c26ef | -6.6875 | -42.0296 | 2025-10-28 01:00:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 126.7 |
| 53222b92-a042-30c2-bf03-fb9af3499471 | -4.3812 | -44.2832 | 2025-10-28 01:00:00 | GOES-19 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 59.1 |
| 0a9c303b-17ab-3117-a21e-2d2ee8e41b20 | -6.6873 | -42.0535 | 2025-10-28 01:10:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 105.3 |
| fdc82f4c-87da-3b33-99a7-274fcfea06d4 | -7.9647 | -45.5317 | 2025-10-28 01:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 129.5 |
| e300e521-ad86-3941-a798-df5ebf004748 | -11.2802 | -45.4823 | 2025-10-28 01:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 63.7 |
| d30ddf37-40ae-3cf0-8158-d278ea3faf88 | -11.2798 | -45.5052 | 2025-10-28 01:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 158.7 |
| 01a5c42a-9df9-37e4-b3c7-6eb83fe264f2 | -7.4539 | -49.4232 | 2025-10-28 01:10:00 | GOES-19 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 57.4 |
| ade42778-2b34-3831-841f-07d3a5e00c4c | -2.7556 | -45.3995 | 2025-10-28 01:10:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 101.9 |
| ef74a129-732f-3117-ab3f-3a0fd98ebd24 | -6.7061 | -42.0517 | 2025-10-28 01:10:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 91.6 |
| d55cc982-020d-395e-8ca0-61427b31dd21 | -7.9459 | -45.5335 | 2025-10-28 01:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 82.1 |
| ef6479e0-c547-31c3-91a9-0e72cd0385f4 | -6.6875 | -42.0296 | 2025-10-28 01:10:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 122.7 |
| b49ab7fb-4437-38db-8194-81b499450468 | -2.7555 | -45.422 | 2025-10-28 01:10:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 113.2 |
| 919d3efd-e302-39dd-b437-9601d28c0745 | -10.5683 | -49.8018 | 2025-10-28 01:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 49.6 |
| 731484fc-5820-38f2-a781-a7c892427727 | -4.4602 | -43.6569 | 2025-10-28 01:10:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 58.4 |
| de11c8bd-0030-3c33-ac84-685ba1eaf0f5 | -7.9461 | -45.5108 | 2025-10-28 01:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 94977d27-5b72-387e-9789-fd76f00c0b3d | -7.9464 | -45.4882 | 2025-10-28 01:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 68.2 |
| dce3840b-1d9b-325d-810f-dea86ae166bf | -10.9405 | -50.255 | 2025-10-28 01:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 33.9 |
| d1ce2f97-4c96-382e-84d1-ec5b91defb6c | -4.4604 | -43.6337 | 2025-10-28 01:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 65.2 |
| e9ef3714-665d-3913-a504-ee157facc668 | -10.9402 | -50.2764 | 2025-10-28 01:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 41.3 |
| 325d0e5d-4292-3f4e-98f2-4aee8622e1f9 | -3.5833 | -43.6108 | 2025-10-28 01:10:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 57.3 |
| 2c1b3951-a33c-366d-83b1-3150d6d9bfd9 | -7.9644 | -45.5543 | 2025-10-28 01:10:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 39.7 |
| 022a9007-bd76-3d6d-b286-d1deb3f83f6d | -6.7064 | -42.0278 | 2025-10-28 01:10:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 104.7 |
| ad6d8d8c-2646-33ad-a830-b478a7105cdf | -3.5831 | -43.634 | 2025-10-28 01:10:00 | GOES-19 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 4fe88613-d44e-348a-9582-19f2ac037343 | -7.4541 | -49.4018 | 2025-10-28 01:10:00 | GOES-19 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 78.9 |
| 6e3ba957-d470-3831-8b3f-32439dcebb5d | -7.965 | -45.509 | 2025-10-28 01:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 77.0 |
| db71a6c7-de08-3cba-bdd3-d19b8c1d90a8 | -7.9647 | -45.5317 | 2025-10-28 01:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 165.0 |
| e41eb15a-0914-3e3f-95a3-4e0b3515aff9 | -10.568 | -49.8233 | 2025-10-28 01:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 34.0 |
| adab2a5b-16dc-3842-aca3-0208e7842d04 | -7.9464 | -45.4882 | 2025-10-28 01:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 89.3 |
| f5e9bf80-0134-39bb-90f1-02ae680797b8 | -10.5872 | -49.7998 | 2025-10-28 01:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 34.6 |
| e04861fe-f8e6-3c16-9173-7ee6183c86dc | -6.7064 | -42.0278 | 2025-10-28 01:20:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 100.7 |
| cfb682f4-1a8f-34ff-a113-b2e7e800f0c1 | -4.4602 | -43.6569 | 2025-10-28 01:20:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 94.6 |
| 5fd7328b-e8e5-34bc-8eb4-db2209f6d1d8 | -5.8386 | -46.4472 | 2025-10-28 01:20:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 58.1 |
| 9d792000-2aed-35a1-b4b3-20ccf194e160 | -7.9652 | -45.4863 | 2025-10-28 01:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 907c73e7-9a03-372a-9281-4148143e4487 | -2.7556 | -45.3995 | 2025-10-28 01:20:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 101.8 |
| 216e5544-5365-33ed-872b-77059782055f | -4.3812 | -44.2832 | 2025-10-28 01:20:00 | GOES-19 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 54.6 |
| 6c19dccb-62f7-390a-9df0-8a1b7cd69ef4 | -3.5833 | -43.6108 | 2025-10-28 01:20:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 51.6 |
| 5ec14d7f-a300-31be-9eee-6fe0d723a6b2 | -4.4604 | -43.6337 | 2025-10-28 01:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 29025e81-2395-3107-8193-ea89b3123e5b | -10.5686 | -49.7803 | 2025-10-28 01:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 32.2 |
| 024cdc1c-b8bb-34ef-a305-b34bb72cab16 | -7.965 | -45.509 | 2025-10-28 01:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 109.4 |
| e0ec3e54-46f6-3fc8-be9d-26b6a68c85ef | -11.2798 | -45.5052 | 2025-10-28 01:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 159.1 |
| 3fc97339-67c5-378b-92fc-ed1c13959a81 | -7.9459 | -45.5335 | 2025-10-28 01:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 141.4 |
| c091ed5f-45f9-310e-b8a8-d5aed343c8f8 | -6.6875 | -42.0296 | 2025-10-28 01:20:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 104.1 |
| c6a9fe85-282d-3bd9-8ae4-996057b89401 | -7.4541 | -49.4018 | 2025-10-28 01:20:00 | GOES-19 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 88.5 |
| 4bf5c8ec-dbfc-3ec7-b00d-d072317f4b80 | -6.6873 | -42.0535 | 2025-10-28 01:20:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 87.9 |
| bbf5ff68-1f0f-3d38-b958-cf1be99be9ed | -3.5831 | -43.634 | 2025-10-28 01:20:00 | GOES-19 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 65.8 |
| f4112eac-88c4-3e05-a77a-5550356df9f1 | -6.7061 | -42.0517 | 2025-10-28 01:20:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 86.5 |
| 4803fcc2-4bed-391a-9b79-e990f44ad602 | -2.7555 | -45.422 | 2025-10-28 01:20:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 99.0 |
| 3af41098-ea6f-3c85-bceb-640f48dc1ad0 | -10.5683 | -49.8018 | 2025-10-28 01:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 54.4 |
| cd5ef6bd-6eac-37b3-b348-82c923621596 | -5.8572 | -46.4459 | 2025-10-28 01:20:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 61.2 |
| d4e09f25-4a71-39ec-8adb-47fd167ff4fb | -11.2802 | -45.4823 | 2025-10-28 01:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 69b8adc1-dfea-3956-b680-c7c0dba45fe0 | -7.9461 | -45.5108 | 2025-10-28 01:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 111.7 |
| cf302415-516e-3dbb-beea-5cadf07260fd | -2.7555 | -45.422 | 2025-10-28 01:30:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 76.5 |
| c2ac6688-5691-3990-b082-da44bb668ce2 | -3.5833 | -43.6108 | 2025-10-28 01:30:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 50.7 |
| b9757d85-b5e2-394d-99f7-3eb5f6eb07da | -11.2802 | -45.4823 | 2025-10-28 01:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 106.4 |
| ef98c6b4-7125-3133-8db0-7e22c664e0c7 | -6.6873 | -42.0535 | 2025-10-28 01:30:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 88.8 |
| 071ca5eb-0695-35ab-af1e-08492decdf62 | -6.7061 | -42.0517 | 2025-10-28 01:30:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 83.1 |
| 7d10d270-61e6-3991-aa97-07c5df848cbb | -3.5831 | -43.634 | 2025-10-28 01:30:00 | GOES-19 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 61.5 |
| d5598123-11e8-3813-a785-9a0030bdb1e8 | -7.9459 | -45.5335 | 2025-10-28 01:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 104.7 |
| 2d512617-7de9-368c-a36d-99f0489673ed | -11.2798 | -45.5052 | 2025-10-28 01:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 245.2 |
| fe4dbfe8-7b4a-31f4-bf21-77e97a57a0a7 | -4.4604 | -43.6337 | 2025-10-28 01:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 101.9 |
| 5468220a-7dac-3547-9859-a4b5df003097 | -9.217 | -46.3489 | 2025-10-28 01:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 8cb449f7-c90a-335e-adc5-c86ed82d4968 | -4.4602 | -43.6569 | 2025-10-28 01:30:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 80.6 |
| f3b117a8-a498-3f57-80a4-4aef991658a8 | -6.6875 | -42.0296 | 2025-10-28 01:30:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 105.6 |
| 39331d27-bf43-39da-956f-7083b5924134 | -7.9647 | -45.5317 | 2025-10-28 01:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 104.3 |
| 7b96d222-54d7-3afd-9714-beed132f496c | -9.2167 | -46.3714 | 2025-10-28 01:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 44ae5f93-9967-38f5-8a0f-a643ff2953af | -7.9464 | -45.4882 | 2025-10-28 01:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 75.4 |
| c79331fb-6af2-3cc4-87e0-3dbcf6e10868 | -10.5683 | -49.8018 | 2025-10-28 01:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 53.9 |
| eb243f9b-ffd7-3c38-ab84-d0029c1a2cb1 | -10.5686 | -49.7803 | 2025-10-28 01:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 34.1 |
| 9750a94f-edc9-3e62-bdd6-e4987c3779f2 | -14.3673 | -49.0068 | 2025-10-28 01:30:00 | GOES-19 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 116.3 |
| 8d362896-a21b-3ec6-8e21-6142ef38fa67 | -2.7556 | -45.3995 | 2025-10-28 01:30:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 83.9 |
| d09c38d9-4ddf-3b33-bb94-b26e681069ce | -7.965 | -45.509 | 2025-10-28 01:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 94.1 |
| 5f992e0a-c2cf-3ce9-b4f0-5381a38c2294 | -7.4541 | -49.4018 | 2025-10-28 01:30:00 | GOES-19 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 945d5000-d585-334d-b997-eb8c9072738d | -7.9461 | -45.5108 | 2025-10-28 01:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 109.9 |
| 8250e3a3-fc25-36d2-99de-7ba2757be76d | -6.7064 | -42.0278 | 2025-10-28 01:30:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 96.0 |
| 3cad0c71-26f4-38a5-953a-892b415ca8a0 | -7.965 | -45.509 | 2025-10-28 01:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 96.2 |
| 6829e805-06fb-3727-a706-1b3baf797fa5 | -2.7556 | -45.3995 | 2025-10-28 01:40:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 58.2 |
| d610d365-da58-3025-996e-38eb13c9858e | -4.4632 | -43.2386 | 2025-10-28 01:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 24f4049b-b1b7-32b2-beb2-9efa288d623b | -4.4604 | -43.6337 | 2025-10-28 01:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 94.8 |
| f32aeeaf-b41d-34d5-9de9-b343a3e9c280 | -6.6875 | -42.0296 | 2025-10-28 01:40:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 90.5 |
| 037370d6-09f6-30fb-bd80-e5d25ba3c874 | -11.2802 | -45.4823 | 2025-10-28 01:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 120.2 |
| e35f85ea-363d-3b00-a9aa-1b2519f01f50 | -4.2206 | -43.1828 | 2025-10-28 01:40:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 26.7 |
| 36d6ee1d-e22f-3e8d-ad6f-502cc07dc599 | -7.4541 | -49.4018 | 2025-10-28 01:40:00 | GOES-19 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 80.6 |
| 4a7c4e2b-d707-3b22-9343-b174ab4f3b54 | -7.9461 | -45.5108 | 2025-10-28 01:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 116.8 |
| b5eafcbf-25d5-37fe-a3cd-111e3af34915 | -6.7061 | -42.0517 | 2025-10-28 01:40:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 75.2 |
| 72fa5ea0-20b2-39ac-94f3-ef16314f815a | -10.5683 | -49.8018 | 2025-10-28 01:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 55.0 |
| 88bc3452-7296-378f-abae-ed119cce1291 | -7.9459 | -45.5335 | 2025-10-28 01:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 119.7 |
| 9d20167a-4881-3a3a-b0bf-86a99f032010 | -7.9464 | -45.4882 | 2025-10-28 01:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 101.7 |
| 0e488014-bc0d-3dd9-99e2-dcaea94605ea | -3.5831 | -43.634 | 2025-10-28 01:40:00 | GOES-19 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 58.3 |
| 9abaec74-6d46-3ca3-b90d-be863ebf8386 | -6.7064 | -42.0278 | 2025-10-28 01:40:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 81.1 |
| 3f1bdf04-9908-3b7f-b12b-e402f75e75c5 | -11.2798 | -45.5052 | 2025-10-28 01:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 245.5 |


[Clique aqui para ver as próximas entradas](README7.md)
