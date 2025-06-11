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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e4f88ec1-c390-32bc-bcd4-9082f05e04c4 | -10.6492 | -49.4267 | 2025-06-11 02:40:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 39.6 |
| 39c9c765-892d-318f-a6ed-19f030fd77d6 | -10.6681 | -49.4246 | 2025-06-11 02:40:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 39.0 |
| 0c2392ab-b04f-3e89-bf96-bf28b3580fb7 | -10.6492 | -49.4267 | 2025-06-11 02:50:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 42.7 |
| 04c5caa2-79b1-3850-b63d-15d0aaef6433 | -7.4763 | -45.5099 | 2025-06-11 02:50:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 43.9 |
| dc1aef71-2376-33be-862d-a6de86e7bc5e | -7.4575 | -45.5116 | 2025-06-11 02:50:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 6d411f07-335e-312e-b0ac-bee9b35b1277 | -4.89498 | -37.36152 | 2025-06-11 03:06:00 | NPP-375D | TIBAU | RIO GRANDE DO NORTE | Brasil | 2411056 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 33eaf125-46b8-3c9a-bb02-de96a47a2037 | -4.89402 | -37.36681 | 2025-06-11 03:06:00 | NPP-375D | TIBAU | RIO GRANDE DO NORTE | Brasil | 2411056 | 24 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 5ed01110-91b1-33e6-8293-465465c19d48 | -15.8383 | -42.59535 | 2025-06-11 03:08:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 7fa4856d-fa2a-3654-a134-e2aa80aacd96 | -15.83646 | -42.60348 | 2025-06-11 03:08:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| f3136939-ed07-30f6-8365-0f13b2f37f4d | -10.6492 | -49.4267 | 2025-06-11 03:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 37.4 |
| 2553a911-9781-3db9-8ad7-d5c117747489 | -10.6681 | -49.4246 | 2025-06-11 03:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 35.2 |
| 7a16de58-5d96-3535-93b5-af960957299e | -10.6681 | -49.4246 | 2025-06-11 03:20:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 35.2 |
| 14d61604-158d-3485-bfea-80b5f8409cb1 | -7.4575 | -45.5116 | 2025-06-11 03:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 52.3 |
| 2f306276-cc28-33a1-8bb4-559534cd7124 | -6.95013 | -44.55641 | 2025-06-11 03:28:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ddfa61c2-88bf-317c-b794-8fafc88c926a | -8.27245 | -44.9602 | 2025-06-11 03:28:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 96647a3a-93b6-3bfd-b5f0-de2db7f9189b | -5.47641 | -35.57908 | 2025-06-11 03:28:00 | NOAA-20 | PUREZA | RIO GRANDE DO NORTE | Brasil | 2410405 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 0d4650dc-52b0-33a9-90f8-047bc291210c | -10.69583 | -37.04807 | 2025-06-11 03:28:00 | NOAA-20 | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| ce1cb344-0a0f-31b0-8361-07967ae0fd76 | -4.89632 | -37.3619 | 2025-06-11 03:28:00 | NOAA-20 | TIBAU | RIO GRANDE DO NORTE | Brasil | 2411056 | 24 | 33 | nan | nan | nan | Caatinga | 1.6 |
| ab0993f5-f9ab-3b7b-9951-4189ced56cfa | -9.66466 | -37.04347 | 2025-06-11 03:28:00 | NOAA-20 | JARAMATAIA | ALAGOAS | Brasil | 2703700 | 27 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 28d0dde2-9d63-34f8-bfe7-e7b929de6510 | -7.22786 | -44.78648 | 2025-06-11 03:28:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| af86eba8-b616-3c6c-b0de-14f51844feed | -8.2855 | -44.96296 | 2025-06-11 03:28:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ee8ed87f-3e13-3306-b791-bc7a3d229150 | -4.49233 | -43.77473 | 2025-06-11 03:28:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 4ac60249-324c-396a-be22-d4531a90e323 | -4.48541 | -43.77639 | 2025-06-11 03:28:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c6258c9b-a486-3fc4-ab7c-f124ec362d12 | -5.64045 | -43.59739 | 2025-06-11 03:28:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4437b924-c1ac-3a07-bb1f-10bec86f0ae6 | -4.89083 | -37.52765 | 2025-06-11 03:28:00 | NOAA-20 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 2c26c6e2-231b-3184-9e99-082fe8756fc6 | -8.27898 | -44.96154 | 2025-06-11 03:28:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 850c1abe-b84d-3e84-8424-16a24db003f8 | -7.00994 | -44.62686 | 2025-06-11 03:28:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2a12a784-7e77-3730-b78a-7a6e65556026 | -8.28655 | -44.95744 | 2025-06-11 03:28:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7bc95c5e-9f2b-38cb-aa2e-3dccf675be3e | -4.57134 | -43.09264 | 2025-06-11 03:28:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 68d57465-5247-3cf9-8118-de753e84c11b | -6.94912 | -44.56181 | 2025-06-11 03:28:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 155f415f-d342-36f7-95d8-989993ce8ec1 | -4.48489 | -43.77915 | 2025-06-11 03:28:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 21073260-47b8-3428-9e4c-17d34a69f8b2 | -4.5705 | -43.09749 | 2025-06-11 03:28:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 14f231f0-e570-33e8-978b-111085bc6cf6 | -9.66315 | -37.04037 | 2025-06-11 03:28:00 | NOAA-20 | JARAMATAIA | ALAGOAS | Brasil | 2703700 | 27 | 33 | nan | nan | nan | Caatinga | 0.9 |
| a6c2b7ec-3e93-3e56-b584-2a663a740b81 | -5.64675 | -43.59853 | 2025-06-11 03:28:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7b87fb17-ee5b-3d2e-9857-25e22688bc95 | -4.49189 | -43.77754 | 2025-06-11 03:28:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| f25b6f48-ebbd-369f-8825-2e2cad59f0b6 | -5.44987 | -44.81354 | 2025-06-11 03:28:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a73712d2-0b31-3a8e-ae1c-5c9422692f8f | -5.44874 | -44.81956 | 2025-06-11 03:28:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 70ef4e00-3162-331a-99ee-c04492cd4a4f | -5.51229 | -35.59432 | 2025-06-11 03:28:00 | NOAA-20 | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| cfdb61b8-653e-351a-b217-95001f69d0b0 | -8.28002 | -44.95612 | 2025-06-11 03:28:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f6002ba7-6159-3d3f-af82-4189556f33be | -7.01101 | -44.6212 | 2025-06-11 03:28:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3d9c5cdb-4aa2-35b9-844e-b51306cf5e86 | -7.22676 | -44.7923 | 2025-06-11 03:28:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0321048d-cd1f-3fb5-b77e-5c7c515b2896 | -5.64583 | -43.60362 | 2025-06-11 03:28:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 214a21ae-7f48-3966-bd7c-1510596b6dc3 | -9.63256 | -36.92973 | 2025-06-11 03:28:00 | NOAA-20 | GIRAU DO PONCIANO | ALAGOAS | Brasil | 2702900 | 27 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 8e1a283e-1ced-37e4-8def-94da18909853 | -4.49137 | -43.78028 | 2025-06-11 03:28:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| dbad7ffd-57be-3924-8112-666c9de6afe4 | -4.89567 | -37.36582 | 2025-06-11 03:28:00 | NOAA-20 | TIBAU | RIO GRANDE DO NORTE | Brasil | 2411056 | 24 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 317b27c3-9d9c-3c79-9471-330abac08fff | -10.6492 | -49.4267 | 2025-06-11 03:30:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 38.2 |
| 0746c7e3-3a87-3fe9-b245-7b451cc26a61 | -7.4575 | -45.5116 | 2025-06-11 03:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 50.3 |
| e07f94f1-4c3b-36ea-a5b5-31b279a900d2 | -15.72165 | -43.49234 | 2025-06-11 03:30:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dee9df39-e04c-3261-8f45-4778ccdffb45 | -12.27042 | -47.00758 | 2025-06-11 03:30:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ff93dfae-8c6d-3476-99cb-1373f9d8ce34 | -14.24814 | -45.49944 | 2025-06-11 03:30:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f2746810-d3a6-3535-995b-0a95777b94ea | -14.24933 | -45.49305 | 2025-06-11 03:30:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3be0d616-13d1-39aa-b268-60c07ffe801e | -10.89892 | -42.24327 | 2025-06-11 03:30:00 | NOAA-20 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 5f3fdf92-05b8-322d-af35-2c96ae96e56c | -14.49986 | -43.80698 | 2025-06-11 03:30:00 | NOAA-20 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4cec6cdc-c8c6-37e6-9b40-856d70934962 | -14.25519 | -45.49615 | 2025-06-11 03:30:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fb2a1263-d337-3272-86c3-aeea108c033e | -11.34305 | -45.21781 | 2025-06-11 03:30:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 46fb9ce3-58d0-3e4f-a19e-0ccbd2a23176 | -15.83584 | -42.60201 | 2025-06-11 03:30:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| ff3d5b7c-0bfc-3bdf-8448-ef8085dd260e | -10.8968 | -42.24636 | 2025-06-11 03:30:00 | NOAA-20 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 4ae06c18-71df-3f39-b696-df99e56e452a | -15.62682 | -39.16926 | 2025-06-11 03:30:00 | NOAA-20 | CANAVIEIRAS | BAHIA | Brasil | 2906303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| c8b9a230-f257-30d2-ab52-a0265d357096 | -12.15663 | -43.20691 | 2025-06-11 03:30:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4679bd7c-667d-3be9-bb3f-714dfb30b8af | -15.37399 | -47.90235 | 2025-06-11 03:30:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3503bb24-d9ac-3218-9fae-a6db1586c842 | -14.25422 | -45.50088 | 2025-06-11 03:30:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 02c9e8b9-abe5-3395-998c-27577e2683a4 | -12.16969 | -43.48265 | 2025-06-11 03:30:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 40a0e5c0-74d4-3e5c-9e74-a245eacad7ac | -11.62877 | -41.8347 | 2025-06-11 03:30:00 | NOAA-20 | IBITITÁ | BAHIA | Brasil | 2913101 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| acb4c41b-a24e-3470-aa67-5852a12cffd7 | -15.83644 | -42.60145 | 2025-06-11 03:30:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| db3d526e-23e3-3144-8587-422f32c24f6b | -12.17045 | -43.47885 | 2025-06-11 03:30:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 38bc84c1-53f7-301b-a834-4d3484ba5203 | -14.24832 | -45.49779 | 2025-06-11 03:30:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d265c008-d839-34a1-aaff-7ef95351c1f0 | -15.83765 | -42.59541 | 2025-06-11 03:30:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 1c98c330-b309-336b-a3db-7830547d878d | -14.50024 | -43.80581 | 2025-06-11 03:30:00 | NOAA-20 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f52d6266-3fb9-3793-a09b-2b413cb25607 | -11.62669 | -41.83334 | 2025-06-11 03:30:00 | NOAA-20 | IBITITÁ | BAHIA | Brasil | 2913101 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 0bc9a7bc-b4d0-3deb-bd8d-ed1c173059d4 | -15.69778 | -43.42108 | 2025-06-11 03:30:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2fcc90f2-ee56-3745-bb91-12698f07d777 | -10.89745 | -42.24299 | 2025-06-11 03:30:00 | NOAA-20 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 5f829ea0-1058-3405-9707-67aaacdcfc24 | -14.24913 | -45.49467 | 2025-06-11 03:30:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 70f9202f-40e9-3c61-976a-9d90473a0805 | -14.24729 | -45.50259 | 2025-06-11 03:30:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3aaec486-0909-359a-8aa7-dff7bb69a941 | -14.25439 | -45.49922 | 2025-06-11 03:30:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ba12f801-a156-3f0a-b9f4-8923091a5006 | -10.8983 | -42.24665 | 2025-06-11 03:30:00 | NOAA-20 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| d1aa57e5-92eb-3ce6-900c-12e2b9e3b115 | -15.83701 | -42.59594 | 2025-06-11 03:30:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| b44b6e7f-a1b6-37cb-8b24-51647737996d | -11.33683 | -45.21605 | 2025-06-11 03:30:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 243cdadc-fb0a-3b76-ad07-e22e616501cb | -14.25011 | -45.48994 | 2025-06-11 03:30:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0c4724b1-3d4b-3988-b1f9-071465c84f4d | -12.2636 | -47.00582 | 2025-06-11 03:30:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5536df4e-9784-3bb3-b5ee-ecaea918108c | -14.25539 | -45.49451 | 2025-06-11 03:30:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| af97f447-0dc3-328b-b6e5-57bdec3718cf | -13.56659 | -44.27392 | 2025-06-11 03:30:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e67443e9-fd9a-33fd-a52c-5b53476e2755 | -11.77535 | -47.40587 | 2025-06-11 03:30:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 51524d3e-9a67-3f5c-bdbf-391172586a7b | -15.71641 | -43.49118 | 2025-06-11 03:30:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d4e8ff4c-01d1-3f49-ad00-bcd67b2ec495 | -14.25338 | -45.50397 | 2025-06-11 03:30:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 13fed996-f36a-34a3-b3c3-9cd6746fe67e | -15.3756 | -47.89502 | 2025-06-11 03:30:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 68924501-429e-370d-bf67-be0fdc359174 | -11.82539 | -43.78967 | 2025-06-11 03:30:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c5b10692-3496-3b68-8526-721441f826f7 | -13.56743 | -44.26979 | 2025-06-11 03:30:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1145dd71-7ec5-39c8-8e52-e957f349d229 | -15.38081 | -47.90408 | 2025-06-11 03:30:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fd75fc11-2810-301a-a4a5-8b85666285ae | -14.50062 | -43.80327 | 2025-06-11 03:30:00 | NOAA-20 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ff3ef83a-500c-3de6-b740-57448a9f322f | -15.69711 | -43.42441 | 2025-06-11 03:30:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3d10aa96-9e21-38fe-93bf-65f8466f6b5a | -21.17859 | -43.97985 | 2025-06-11 03:32:00 | NOAA-20 | BARROSO | MINAS GERAIS | Brasil | 3105905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 5b01b951-9f14-3845-8e2c-21e3fc26d122 | -18.16331 | -46.95054 | 2025-06-11 03:32:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cb44c6e1-396e-3209-a0bc-afbbe030b149 | -15.37531 | -47.89479 | 2025-06-11 03:32:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fb2b50bf-d285-3a09-bfdb-459055061a62 | -22.40928 | -45.95538 | 2025-06-11 03:32:00 | NOAA-20 | POUSO ALEGRE | MINAS GERAIS | Brasil | 3152501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 61f3eb84-a6f5-3bad-a810-b61cecbee67a | -22.78017 | -49.3489 | 2025-06-11 03:32:00 | NOAA-20 | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8ea7bae4-84db-37f3-bd8c-60bf788fec18 | -17.09239 | -43.80383 | 2025-06-11 03:32:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8e68ff64-aed8-302c-a72c-a7fa23d147b3 | -22.53659 | -48.81566 | 2025-06-11 03:32:00 | NOAA-20 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ea09da02-73a6-3aa9-ab54-f2d9e81f5997 | -17.09236 | -43.80552 | 2025-06-11 03:32:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1066fdb6-0e66-3f1d-bb6e-2f6478e7340f | -16.57587 | -43.64583 | 2025-06-11 03:32:00 | NOAA-20 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 79ae471b-4b0a-3752-8bfa-b714d4af1cd2 | -22.41109 | -45.95615 | 2025-06-11 03:32:00 | NOAA-20 | ESTIVA | MINAS GERAIS | Brasil | 3124500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |


[Clique aqui para ver as próximas entradas](README5.md)
