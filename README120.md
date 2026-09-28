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

## Dados Diários - Página 120

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3457224e-3a01-3536-ad2c-403878461275 | -8.38918 | -45.47123 | 2026-09-28 16:26:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 70b0903c-ab51-3855-86bb-b7dc0c213c5d | -9.83426 | -49.1417 | 2026-09-28 16:26:00 | NOAA-20 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 08e92cae-55f5-3d64-b36b-55ba21c2e444 | -7.45686 | -45.81 | 2026-09-28 16:26:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 16.0 |
| d7bca980-d73f-3f15-9434-67131ceaeb31 | -7.45073 | -44.5956 | 2026-09-28 16:26:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2cc4cf6c-5f4a-31ff-ab5b-74d559f818f5 | -9.96672 | -50.13902 | 2026-09-28 16:26:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 6d95e061-5e43-3c4a-9b24-809491f0e689 | -9.97473 | -50.1613 | 2026-09-28 16:26:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 2652bf2c-b3bf-3100-b65f-888bb0729599 | -8.09877 | -44.0099 | 2026-09-28 16:26:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 91e1081c-0339-3697-ad87-7fd2e71c6296 | -9.22935 | -47.32735 | 2026-09-28 16:26:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 46ec2aa1-8ede-3f8a-87a4-1530cd6d2ca6 | -9.0715 | -47.18279 | 2026-09-28 16:26:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 35fa73f7-4f0d-3f9e-abe8-c6d8f0008db1 | -6.36613 | -45.78685 | 2026-09-28 16:26:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| df303761-a257-3e63-9c77-7b3d7b88ee88 | -3.88561 | -38.73047 | 2026-09-28 16:26:00 | NOAA-20 | CAUCAIA | CEARÁ | Brasil | 2303709 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| bbe5e40d-966b-36d6-b059-b8a225c4b92c | -7.71129 | -44.9162 | 2026-09-28 16:26:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 9.0 |
| b079a4f0-9744-3036-927f-cdb50a10ddcf | -10.92205 | -50.65899 | 2026-09-28 16:26:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 1a52c3cd-59f2-309f-bb2a-bdef50741662 | -11.15955 | -50.05957 | 2026-09-28 16:26:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 7341363f-1166-3e10-9f04-60c6e5ad3f5c | -6.81484 | -45.05471 | 2026-09-28 16:26:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 250e5f71-c2e0-379a-8885-e5926f4ae87f | -10.92192 | -50.66245 | 2026-09-28 16:26:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 90e5e9a6-b938-3643-afe4-578200f7c56b | -11.1177 | -47.71969 | 2026-09-28 16:26:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 4ef6cbec-73a6-3128-bed8-5cbe0eb69baa | -9.7819 | -46.44165 | 2026-09-28 16:26:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 1cff218f-19fe-3701-bc29-1df7e56a12b4 | -7.25844 | -43.35485 | 2026-09-28 16:26:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 031466de-8948-3c87-af3e-86c017b42e2f | -10.95141 | -50.68144 | 2026-09-28 16:26:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 9.0 |
| d6185cae-0c7d-3b17-80ff-3f51a160f60f | -11.30163 | -48.73071 | 2026-09-28 16:26:00 | NOAA-20 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 8a01fa3e-0612-3735-b7a5-0838604622b1 | -7.32169 | -55.00544 | 2026-09-28 16:26:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| b095eba6-86db-3fda-b126-2d1113967196 | -9.7657 | -44.83969 | 2026-09-28 16:26:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 160.4 |
| 12c80e1a-181c-3b46-9d6b-7bc52b7975db | -10.55051 | -51.44015 | 2026-09-28 16:26:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| d5fdb25a-71f8-345f-acd7-307758ca76a3 | -9.96973 | -50.16194 | 2026-09-28 16:26:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 19.9 |
| df3236a8-5033-34cd-a22c-26bffe06d9b9 | -7.43243 | -55.63122 | 2026-09-28 16:26:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 23.4 |
| f8613d6f-68f9-3f47-b696-ba7efc8595cb | -9.3155 | -46.56323 | 2026-09-28 16:26:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 7db000c7-9889-33c3-b96c-e68f622819cc | -10.12211 | -50.19521 | 2026-09-28 16:26:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 29.4 |
| ae54f997-6b28-34bb-9496-fed8c21af1fc | -7.70545 | -44.92495 | 2026-09-28 16:26:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 234f0221-bab2-318e-ad9a-d51ebce25812 | -9.93388 | -50.23864 | 2026-09-28 16:26:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 36.2 |
| 4da2dd29-2151-36b5-a1ff-629cc95676b3 | -9.07946 | -49.87841 | 2026-09-28 16:26:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 37.3 |
| b6d10ef1-e0a0-3938-bfae-49bed8d0b9c1 | -4.37334 | -43.05899 | 2026-09-28 16:26:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 7b54e8e0-3c73-3f73-8846-0a957391150a | -9.39328 | -46.38937 | 2026-09-28 16:26:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 28.5 |
| 13f65942-e324-391e-aa1b-224799e9af23 | -9.65971 | -42.31982 | 2026-09-28 16:26:00 | NOAA-20 | REMANSO | BAHIA | Brasil | 2926004 | 29 | 33 | nan | nan | nan | Caatinga | 8.0 |
| e3a1ee14-a57c-3889-b0b6-7f7abc99a61d | -10.59937 | -50.56581 | 2026-09-28 16:26:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 6b6db8b9-d90e-3c72-ba4c-c7841ab0920f | -8.6651 | -47.23713 | 2026-09-28 16:26:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 51ed7b51-cf95-35f9-8b57-f06b04bc824e | -9.83093 | -44.93811 | 2026-09-28 16:26:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 22.6 |
| e8a05816-a655-3ae3-8690-0a753f69542f | -10.92796 | -50.70752 | 2026-09-28 16:26:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8a24d6c1-f8f2-3524-8553-055bd9877245 | -7.30822 | -44.60182 | 2026-09-28 16:26:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 2a40fc9c-1fd9-32de-b397-b755a6b72f16 | -10.96791 | -43.68895 | 2026-09-28 16:26:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 72.6 |
| ae3cf8a1-e13a-3e3b-9fa2-51d07ee33000 | -6.00504 | -48.37648 | 2026-09-28 16:26:00 | NOAA-20 | PALESTINA DO PARÁ | PARÁ | Brasil | 1505494 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 3f679d23-9468-339e-b49f-bb5bfb3315d7 | -8.94206 | -38.22535 | 2026-09-28 16:26:00 | NOAA-20 | PETROLÂNDIA | PERNAMBUCO | Brasil | 2611002 | 26 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 70e57b8e-ff02-3ce0-a0f5-e45a6224d5b6 | -6.69284 | -45.67422 | 2026-09-28 16:26:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 658f140a-2aae-3f7d-a75a-79a7b10eddc3 | -3.56021 | -39.0329 | 2026-09-28 16:26:00 | NOAA-20 | SÃO GONÇALO DO AMARANTE | CEARÁ | Brasil | 2312403 | 23 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 918bed01-ead6-3349-9c1a-a2c3fcb4088f | -3.80333 | -44.10741 | 2026-09-28 16:26:00 | NOAA-20 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| acf02a46-2d97-39cb-a4ac-2f98911dd7e6 | -7.40955 | -42.11806 | 2026-09-28 16:26:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 12.7 |
| eb1ff23a-01f7-32f6-8aaa-ae3d40222171 | -9.9843 | -45.34837 | 2026-09-28 16:26:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 54.0 |
| 3c7aa847-8b81-3bc0-91f5-ea11c9485037 | -8.52346 | -47.53246 | 2026-09-28 16:26:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 9c8781c0-7f50-3d8d-8e37-8e71cd7e5f1c | -7.68764 | -44.87631 | 2026-09-28 16:26:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 2d1b0b21-8f8a-3d95-a6ba-f207c69c651a | -7.21453 | -45.07657 | 2026-09-28 16:26:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| e00d4284-5d36-38f5-998b-cb369947f253 | -6.87551 | -42.84266 | 2026-09-28 16:26:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 16.2 |
| 043f8269-e3ac-3337-96e6-7c42c2fca6b4 | -8.38436 | -45.46351 | 2026-09-28 16:26:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 69.6 |
| f3d72155-0e56-35c5-a952-1a983a03e0e8 | -8.91779 | -37.21022 | 2026-09-28 16:26:00 | NOAA-20 | ITAÍBA | PERNAMBUCO | Brasil | 2607505 | 26 | 33 | nan | nan | nan | Caatinga | 10.7 |
| 5ccb0538-7fdd-3d22-aab4-8f5267624626 | -6.04314 | -45.17246 | 2026-09-28 16:26:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 5174e40d-df09-3e31-b824-80f62fea2825 | -7.28252 | -44.30941 | 2026-09-28 16:26:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 91d0e4fb-0590-3c7d-b344-55548b20308a | -5.63814 | -45.53286 | 2026-09-28 16:26:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 36.4 |
| f0b86af2-b4f9-3c98-9c38-53d1f41555f3 | -6.35128 | -45.81001 | 2026-09-28 16:26:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 6cb3ca99-3b91-3d95-8183-ba86fe5bcd4e | -7.26282 | -43.36134 | 2026-09-28 16:26:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 20.2 |
| fac2aee0-58e6-3562-82ff-9c6147fa9eb1 | -9.50966 | -46.37717 | 2026-09-28 16:26:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| c2d709bb-88e5-3e90-b527-b7adcc6d3187 | -7.29689 | -43.31676 | 2026-09-28 16:26:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 95cd9306-3fdd-304a-9549-8590afd810b6 | -8.66543 | -45.36572 | 2026-09-28 16:26:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 25.9 |
| 293f41c3-3bed-3248-9661-05148a4771d3 | -10.89421 | -50.69551 | 2026-09-28 16:26:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 4d372187-9011-3303-8c3c-b3aa1845217a | -9.96738 | -50.2609 | 2026-09-28 16:26:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0b910641-bfec-33c8-802d-a2c1b2d4341b | -10.59957 | -49.98792 | 2026-09-28 16:26:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 20d25b1a-70ba-3605-8f0e-891faf6ab1fc | -11.18679 | -50.03795 | 2026-09-28 16:26:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c3e6e34f-8a71-3143-9a81-37a50b5f1303 | -11.14908 | -50.0579 | 2026-09-28 16:26:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| f56861bd-bf3c-3f9b-b27d-ddbcbae7c44a | -10.98328 | -50.68063 | 2026-09-28 16:26:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 2e1470f7-f1ca-341c-a23e-dc22c016725e | -6.69829 | -45.66995 | 2026-09-28 16:26:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 24c18a78-ae7e-3b71-b274-f57096d7ee9e | -6.36255 | -45.78737 | 2026-09-28 16:26:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| aada0216-772d-348b-9b73-0c57677f83e3 | -5.72463 | -53.45974 | 2026-09-28 16:26:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| e5bc0571-1afc-3844-ac45-a5bf2d4eb6b6 | -11.18716 | -50.0409 | 2026-09-28 16:26:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| f83fe7b2-ee49-3ff9-a098-65e0934025cb | -9.75686 | -48.20051 | 2026-09-28 16:26:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 7ba06be6-6d61-31bd-aaa6-0c64e08728af | -7.52301 | -44.89235 | 2026-09-28 16:26:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 7626167d-1173-3a74-8b9d-be7e8f66af9d | -6.89705 | -52.47537 | 2026-09-28 16:26:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| cef41527-815f-376f-ac0d-58ae2b675de8 | -9.32258 | -46.55722 | 2026-09-28 16:26:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 30b673f7-eaad-3705-b01c-f490700cb9fb | -8.73459 | -44.90056 | 2026-09-28 16:26:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 18.3 |
| f3d4d6d9-58e7-3303-9faf-2af373d81412 | -10.10724 | -43.94534 | 2026-09-28 16:26:00 | NOAA-20 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 21.8 |
| 7ccaf282-73dd-399a-aff7-56dd22e2156e | -9.516 | -46.36635 | 2026-09-28 16:26:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 24.0 |
| 90c15017-3405-31e8-834b-daa74a34cfa7 | -7.34413 | -42.06763 | 2026-09-28 16:26:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 9.7 |
| 1ecea404-a7f1-3811-9e70-4f2c3c49c97a | -11.15452 | -48.33039 | 2026-09-28 16:26:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c7934135-6e9e-3f9e-a20f-584807c9ecbe | -10.96351 | -50.69304 | 2026-09-28 16:26:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 29.1 |
| e2000f48-f6c6-36f9-9cc2-944bcac0205f | -11.1351 | -50.06868 | 2026-09-28 16:26:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 66f7857d-0bb2-3371-ba79-5ab9726fbe15 | -7.83234 | -55.13113 | 2026-09-28 16:26:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 5e82a797-d877-3661-af5f-50da61ac1eef | -7.9004 | -45.44272 | 2026-09-28 16:26:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 228b08eb-a14e-3a3b-89ec-4f6b4759dfe3 | -10.9627 | -50.68657 | 2026-09-28 16:26:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 14.1 |
| d512314d-e650-3cbd-97a6-4fb6e4fde067 | -7.26124 | -43.35083 | 2026-09-28 16:26:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 2cfbab1e-a327-3ba9-b02b-e27df5eb2075 | -11.46985 | -49.74445 | 2026-09-28 16:26:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| c0789e8e-4170-32a6-aacc-c5fc7a652ca1 | -9.44637 | -41.81171 | 2026-09-28 16:26:00 | NOAA-20 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 142.7 |
| a14feea1-f6e0-3232-ad9f-93f4844b2b35 | -9.51149 | -46.3621 | 2026-09-28 16:26:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 24.0 |
| 661457ad-4c46-393c-95f1-0ff9d6dd2522 | -7.33248 | -42.08107 | 2026-09-28 16:26:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 15.3 |
| ad0c3767-fcb1-39aa-9fa9-f0134f44defd | -10.92245 | -50.66222 | 2026-09-28 16:26:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 1ad1232b-0f01-3c73-b9f5-2e9fcaa34c4b | -9.78592 | -45.81527 | 2026-09-28 16:26:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 28.8 |
| 16d966d3-110c-3287-be7c-7b380cbe4b9c | -7.27626 | -44.31406 | 2026-09-28 16:26:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 495fb7f0-0903-3b57-9d2d-17eb8bc24bc7 | -3.3113 | -42.55317 | 2026-09-28 16:26:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 0be750d1-a928-3dd7-84db-e18a346906fc | -10.71481 | -44.44078 | 2026-09-28 16:26:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 9.4 |
| cf8ecdea-9b23-39b2-9c02-7acaac99cc31 | -3.81118 | -44.092 | 2026-09-28 16:26:00 | NOAA-20 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| f0aa5652-de34-3c74-a8cc-770a44327118 | -7.6237 | -39.98806 | 2026-09-28 16:26:00 | NOAA-20 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 15.7 |
| 947c53ba-7565-3d4d-9b26-c1a7dcf6e1e2 | -8.38138 | -45.46823 | 2026-09-28 16:26:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 7a999efc-3e2a-3057-836f-aa87ee752abb | -3.22115 | -42.80616 | 2026-09-28 16:26:00 | NOAA-20 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 2fcb04b2-5728-3fea-ba3f-aa50fc94ea7f | -5.51341 | -45.54293 | 2026-09-28 16:26:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |


[Clique aqui para ver as próximas entradas](README121.md)
