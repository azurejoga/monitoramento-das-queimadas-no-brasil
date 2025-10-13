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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 69d8401e-6f48-3ef5-bc34-3a02d4c02b9d | -5.91798 | -45.42703 | 2025-10-13 04:44:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 86273a94-8c3d-313a-9556-8e5525e313ef | -7.49766 | -44.63118 | 2025-10-13 04:44:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.2 |
| f9d760a9-2d6c-344c-ac94-4a29f78ad257 | -3.26154 | -50.13747 | 2025-10-13 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 406ae53b-6776-3245-9df7-6c5d78f55c0e | -3.89347 | -47.18018 | 2025-10-13 04:44:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f26c3efd-48fa-3657-b82d-764d04caaa5c | -4.47856 | -44.93793 | 2025-10-13 04:44:00 | NOAA-20 | LAGO DO JUNCO | MARANHÃO | Brasil | 2105807 | 21 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 18bf01a3-23c5-3808-ae8b-0858da7d50b2 | -2.89155 | -50.73653 | 2025-10-13 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cf4cd8be-d3ef-3dff-a345-f5cd8748b6a4 | -7.67218 | -42.38391 | 2025-10-13 04:44:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| e55825bb-7625-31c1-85d9-f9ae2771326e | -3.41711 | -52.04145 | 2025-10-13 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4439be1f-1e6d-3047-8e37-56bd6ab42da9 | -3.41231 | -52.88137 | 2025-10-13 04:44:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| df14ff64-e513-3657-8787-fb893984b959 | -7.50976 | -42.16046 | 2025-10-13 04:44:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 7e832634-8490-388a-ab76-3565ca8c7e7d | -5.11019 | -43.20148 | 2025-10-13 04:44:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b7003c66-2a88-355c-9590-325b202e0ea8 | -7.55931 | -43.83955 | 2025-10-13 04:44:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 03ab8604-811a-3df3-b0aa-e3d5326fb4ae | -4.66192 | -45.70067 | 2025-10-13 04:44:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c375960c-cd08-3753-886f-eb989808232e | -7.51546 | -42.15799 | 2025-10-13 04:44:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 0ed12ff0-b04b-318b-a246-34e984d8efdc | -6.7326 | -42.08895 | 2025-10-13 04:44:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c0c4e7ca-76fa-3179-9da2-7874592124ba | -6.27227 | -43.90342 | 2025-10-13 04:44:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 89ed8349-d710-32d5-9609-178a481b37be | -3.09347 | -50.38248 | 2025-10-13 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e8c88490-e298-385a-be94-a51cf245c6c0 | -7.34382 | -43.86175 | 2025-10-13 04:44:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1e50c93d-f464-35b0-a18a-d78a378c4902 | -3.8104 | -51.17712 | 2025-10-13 04:44:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ebf5596b-6991-371b-85b7-1c8abed2a921 | -7.5021 | -44.63184 | 2025-10-13 04:44:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 23e2ac61-fc67-39d5-8c69-dca1c540335b | -7.75434 | -44.20677 | 2025-10-13 04:44:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 226f1d43-dbd3-37b5-aeed-0bc8b9fabfcd | -7.51502 | -42.16119 | 2025-10-13 04:44:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 0268ca1f-b36b-31e6-b440-ae0c6a51b551 | -7.14501 | -42.51714 | 2025-10-13 04:44:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| ef4c9648-ea58-3e05-9501-26fb38827a76 | -7.80837 | -42.44282 | 2025-10-13 04:44:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 5054b331-e313-360b-b4da-570b080f7e0f | -7.777 | -44.04397 | 2025-10-13 04:44:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 11c9da46-b917-338f-acbb-b9e01112a5b1 | -3.25878 | -50.13351 | 2025-10-13 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 72c6a498-5ea9-34ce-8ade-70ff342387ed | -10.79666 | -43.97036 | 2025-10-13 04:44:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a97c24ef-37cb-3804-bb1c-644965f38cee | -4.86898 | -45.73571 | 2025-10-13 04:44:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9d9802c3-bf37-33c9-82d1-95937a9fe864 | -3.14735 | -50.45129 | 2025-10-13 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bbabe9e6-3819-32af-94f4-0f07c1020d33 | -8.23762 | -43.36246 | 2025-10-13 04:44:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 42fda144-2c59-312f-a892-44a4174d9364 | -4.28329 | -48.57355 | 2025-10-13 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f5eee7ac-7816-39a4-a3e8-ce916b0f2720 | -4.53515 | -42.8862 | 2025-10-13 04:44:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| e596824e-bb27-39a7-a5e8-92f4ea154511 | -7.48433 | -42.75888 | 2025-10-13 04:44:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 3886fdee-b169-343f-b443-994e95892956 | -2.98564 | -50.29153 | 2025-10-13 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 465bdd27-804d-3d3b-a116-ef3c1e825255 | -10.80222 | -43.96575 | 2025-10-13 04:44:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| f56f082f-99fa-3a11-a44b-8e3dad363c03 | -3.02251 | -50.44547 | 2025-10-13 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 55209f12-8e72-3fc4-8751-e79251ea90ae | -5.81179 | -44.04974 | 2025-10-13 04:44:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6731f2f6-141d-3141-ac2f-f9e23108ebf1 | -3.06656 | -49.4116 | 2025-10-13 04:44:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c775294b-dde2-308b-a747-5682f9175914 | -3.87056 | -44.12154 | 2025-10-13 04:44:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1084ac17-5e55-3210-a241-324f8b688610 | -5.24756 | -45.59595 | 2025-10-13 04:44:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4fe60c8e-6749-37b3-8615-346549b486ec | -6.73861 | -42.08422 | 2025-10-13 04:44:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| dc028070-63d9-3d1f-b7b4-acc762f59f89 | -7.51667 | -44.59332 | 2025-10-13 04:44:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bbc67c8a-6d99-3df5-86a2-cfddfd3d0454 | -3.29003 | -53.01094 | 2025-10-13 04:44:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f0f9de2a-1e12-3fff-bf62-9caf39c11b2f | -7.49191 | -44.60796 | 2025-10-13 04:44:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 49fe9c69-3818-300f-a781-bcb897538590 | -6.93726 | -42.04414 | 2025-10-13 04:44:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 5ac1ac25-bc70-3605-b10c-b8d8adc6609b | -6.33752 | -44.33025 | 2025-10-13 04:44:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1580b1b9-77c8-312a-afda-54cc601835cc | -3.82426 | -47.74241 | 2025-10-13 04:44:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8e61c928-d6c1-3424-9641-66c694377924 | -3.43733 | -49.84117 | 2025-10-13 04:44:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| efb7eaa1-8402-360b-ab62-1b986ed4885b | -6.70088 | -45.97331 | 2025-10-13 04:44:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e7ec7c68-c53a-379e-8f90-f4c26de82142 | -3.24577 | -50.81675 | 2025-10-13 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f4c4a9c8-8ab3-3a95-ac71-eac4e9961955 | -6.42047 | -42.55114 | 2025-10-13 04:44:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| ff95d816-f617-3cc4-8479-eb4df578bb90 | -3.9198 | -50.012 | 2025-10-13 04:44:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a23fb833-6924-3dd7-a2f9-a17b8fbce837 | -7.13946 | -42.51962 | 2025-10-13 04:44:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e45ab3cf-2c05-3b98-8195-000cd919ce6c | -3.06324 | -49.41108 | 2025-10-13 04:44:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8576c939-4f9b-3661-b727-07492c1ff5bc | -10.81129 | -43.97222 | 2025-10-13 04:44:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 7c1f80ad-dafd-369b-b9e8-a7c946870406 | -3.61266 | -48.91803 | 2025-10-13 04:44:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 63deb769-d2a3-320d-9385-c1585fc2fb97 | -7.64674 | -42.57243 | 2025-10-13 04:44:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 9a910d04-702f-3cb0-8089-4f7136e9a5f1 | -7.51415 | -42.16756 | 2025-10-13 04:44:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 7cf94b5b-63ac-381f-9110-be06210be785 | -3.1375 | -50.21362 | 2025-10-13 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 912621fb-1d5a-311b-8195-433684dc9e27 | -7.49467 | -44.65223 | 2025-10-13 04:44:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 99171c6d-e8a7-30ea-895a-61954ffa280c | -7.54855 | -46.08958 | 2025-10-13 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| c6faa777-283e-3bba-b4b1-9d8a85c4445e | -7.48942 | -44.62553 | 2025-10-13 04:44:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 05026ef7-8bc6-36be-95a7-28355c6c2a00 | -7.35113 | -44.08067 | 2025-10-13 04:44:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| eb434940-a10a-3924-99af-37ffb21eb919 | -7.552 | -43.84092 | 2025-10-13 04:44:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ed2fe82f-cb69-3be1-8755-dd7937313c26 | -10.81618 | -43.97281 | 2025-10-13 04:44:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 44255e5e-375a-34ce-be7b-d80dc39e2974 | -7.92454 | -47.21851 | 2025-10-13 04:44:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b7fce9bc-e7c8-3a89-a336-3cf793d8be88 | -5.92965 | -40.88335 | 2025-10-13 04:44:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e9429b2b-1105-387d-a744-40c245870e6e | -3.60486 | -51.33982 | 2025-10-13 04:44:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a5238301-6a2c-3024-9aaa-eda632e824b5 | -7.48684 | -44.61176 | 2025-10-13 04:44:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4e6bacfc-1052-39c7-b633-d548795ce6d3 | -8.53827 | -44.59167 | 2025-10-13 04:44:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 4cd4ee04-0776-3a12-8a91-6ea530498c0d | -4.53438 | -42.89139 | 2025-10-13 04:44:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| fe49b6ca-b1c4-307a-88a9-6abb0225d02d | -10.8071 | -43.96638 | 2025-10-13 04:44:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 027e4b4a-40dc-3a9d-9d21-29eaaf9d86d0 | -7.5492 | -47.32591 | 2025-10-13 04:44:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4cd6d61a-93fe-31d6-9b53-d886d36f93f6 | -3.07042 | -49.40865 | 2025-10-13 04:44:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| b1cc3116-1ac1-34e0-9bc3-476c246a9563 | -10.81894 | -43.98944 | 2025-10-13 04:44:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 36cb8395-ac55-3156-bd5d-e501ee6d9090 | -7.28125 | -41.96082 | 2025-10-13 04:44:00 | NOAA-20 | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 069d397d-145d-3332-8f8d-d6f8ce4acf08 | -7.77634 | -44.04875 | 2025-10-13 04:44:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 683a154e-0787-36c7-abdf-b1e790963ca1 | -2.88933 | -50.72906 | 2025-10-13 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 660249e4-78b8-3d50-96db-76d0461bd1fc | -4.31818 | -48.07855 | 2025-10-13 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 00f2ae45-adad-3555-a87c-442622452623 | -3.09787 | -50.37612 | 2025-10-13 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 3ae9eebe-7aa4-3d60-bb29-d7e2f54e4844 | -3.72459 | -44.40782 | 2025-10-13 04:44:00 | NOAA-20 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d3d42b45-9a39-3537-8ff0-9f3cfb6d66e2 | -2.88104 | -50.73844 | 2025-10-13 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 2168a821-8855-3230-bc1d-19d26c903974 | -6.22859 | -41.56542 | 2025-10-13 04:44:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 3aa3d8cb-2426-3a8b-b8ef-64a2190b281a | -4.18275 | -46.22855 | 2025-10-13 04:44:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e38f5a51-adcc-34bb-a054-e930c832c0c0 | -3.14134 | -50.21069 | 2025-10-13 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 9f6dc278-fde8-393c-a22d-305577b8cfd1 | -6.7156 | -46.79536 | 2025-10-13 04:44:00 | NOAA-20 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e3c6cf07-e481-3e1b-af1c-319542d526c1 | -3.92257 | -50.01596 | 2025-10-13 04:44:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4e2f19f2-68b6-30dd-8499-ad603fb578e3 | -4.84474 | -43.20271 | 2025-10-13 04:44:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 936fb119-1ae8-318c-bc7d-8b08aaace6a5 | -7.64594 | -42.57837 | 2025-10-13 04:44:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 43e4bea7-4247-3101-8c9e-76162c72886d | -7.50273 | -44.59558 | 2025-10-13 04:44:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b2f62cfd-b496-31fb-90ce-89eb365a75d8 | -6.76277 | -44.65145 | 2025-10-13 04:44:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 78870df1-7b87-3020-be63-ef8167bf0f6d | -3.12775 | -50.20814 | 2025-10-13 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 588d54b5-0bdf-3e77-ba6e-438ec27f9f66 | -6.22319 | -41.56491 | 2025-10-13 04:44:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 1ee88877-3351-3706-ad61-8c5dbe58ace0 | -7.83976 | -44.52826 | 2025-10-13 04:44:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e348d229-b58b-32a1-a7be-bf315fa58c2a | -5.57899 | -41.10669 | 2025-10-13 04:44:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 1e1eca3c-796b-37d7-a14d-01ae9e723cad | -3.09402 | -50.37904 | 2025-10-13 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| a5861c63-4aee-34d0-8f03-8dc5a4a40f9d | -7.78096 | -44.04951 | 2025-10-13 04:44:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c55025ac-e805-312f-8d77-66f031593f73 | -7.49828 | -44.62684 | 2025-10-13 04:44:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 795e0544-891f-3354-9cd8-8ed661991269 | -5.56605 | -45.27402 | 2025-10-13 04:44:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6141b133-8a83-3470-a819-4a5fff690ce4 | -4.02577 | -46.97708 | 2025-10-13 04:44:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |


[Clique aqui para ver as próximas entradas](README29.md)
