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

## Dados Diários - Página 57

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 92853bf3-d2da-366c-8cdb-b8fbf3e70b7d | -12.7294 | -47.9845 | 2025-09-21 14:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 3ce7db50-0f34-3ad5-ae19-cb11bbd12444 | -8.8801 | -46.138 | 2025-09-21 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 65.8 |
| dd7bdace-6515-3865-a098-bfce966e8434 | -16.8727 | -43.8894 | 2025-09-21 14:40:00 | GOES-19 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 8d680e22-f7de-3f48-9f7c-e76756f753b3 | -14.7682 | -51.3863 | 2025-09-21 14:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 53.9 |
| 7882674c-e7c3-3d55-bd01-a77223c7739d | -6.704 | -44.0017 | 2025-09-21 14:40:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 100.7 |
| e1a51979-b5ec-3c77-8114-34f90d24e5b2 | -12.451 | -49.7328 | 2025-09-21 14:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 8032bc04-af3e-36a9-b67f-28ec1b754406 | -14.8071 | -51.3809 | 2025-09-21 14:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 3136c531-b1dd-3150-924b-b90d65068326 | -15.0508 | -55.283 | 2025-09-21 14:40:00 | GOES-19 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 150.8 |
| b4275d75-14db-350b-9bd2-ed0f7d9dd973 | -4.4084 | -43.0551 | 2025-09-21 14:40:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 3871177a-c2d3-3419-bf95-4cba51611803 | -9.8822 | -46.116 | 2025-09-21 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 462.4 |
| fdf798ff-16c3-3957-9459-8bcc930ba956 | -12.8969 | -50.5398 | 2025-09-21 14:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 926fcb2e-d595-3b7c-bdda-d7042a2fc7ae | -14.788 | -51.3621 | 2025-09-21 14:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 56.8 |
| eb12b522-4d16-3e0d-b3a1-8aea57d340ab | -12.9161 | -50.5374 | 2025-09-21 14:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 62.8 |
| 15ced95f-bbb7-3194-a152-87d8593f800c | -15.4653 | -55.9966 | 2025-09-21 14:40:00 | GOES-19 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 6aeba5d4-8453-3e39-ab1d-fb5f87cb0dfa | -12.1156 | -44.7839 | 2025-09-21 14:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 103.6 |
| f5bf0ed1-6d81-31b9-b88f-e6f9c26932f1 | -17.1173 | -45.9491 | 2025-09-21 14:40:00 | GOES-19 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 158.3 |
| dde8aa66-f813-3550-ad1f-86f4f63628c3 | -10.7571 | -46.0079 | 2025-09-21 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 60.7 |
| 972504e3-7a4f-3528-9ddd-0e45da4b1ce8 | -10.0317 | -46.2561 | 2025-09-21 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 107.3 |
| 4f6ced2d-2b68-30b6-8476-b95b646765fb | -15.0511 | -55.2624 | 2025-09-21 14:40:00 | GOES-19 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 8bf42070-28fe-3702-aff6-ba98070ef6b6 | -9.1744 | -45.3135 | 2025-09-21 14:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 96.2 |
| 25940105-a364-35e2-aa57-f9c9bbbfb746 | -7.5272 | -44.3413 | 2025-09-21 14:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 119.3 |
| 318a403d-b5f6-35e8-a77b-3cbee0a5039d | -12.9049 | -46.7713 | 2025-09-21 14:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 80.5 |
| f0ccc19c-94f9-3100-973a-9f6f6831dbda | -2.9528 | -42.8938 | 2025-09-21 14:40:00 | GOES-19 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 94.4 |
| cbaa3af0-a764-3197-af80-1b1812ab4f92 | -11.3681 | -50.8486 | 2025-09-21 14:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 91.0 |
| 25e6312e-f963-3e20-9576-b38e867750e7 | -8.8993 | -46.1135 | 2025-09-21 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 69.0 |
| bc41e45a-5577-3cd0-bafc-234dfe831b45 | -12.0767 | -44.8131 | 2025-09-21 14:40:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 98.5 |
| d2724dd3-4605-3e27-9a9f-32817049bb1d | -7.6007 | -44.4952 | 2025-09-21 14:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 7f06a08b-6219-33bd-b66b-dd460d84b208 | -12.3399 | -44.0946 | 2025-09-21 14:40:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 9946833f-7113-376f-8fd5-42c088b5685c | -10.2621 | -46.0703 | 2025-09-21 14:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 83.8 |
| 6461633b-c913-3f50-9da7-44ec689533ca | -14.2666 | -51.3479 | 2025-09-21 14:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 58.8 |
| 2ee478cb-a468-3e0a-8080-8d47bd59f694 | -12.9157 | -50.5589 | 2025-09-21 14:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 34cb6d1d-1e5c-3d2c-bd61-eb70bda937a9 | -12.2794 | -45.2679 | 2025-09-21 14:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 98.1 |
| 45d53b4b-4938-3c6c-a038-e6a428584831 | -10.6741 | -46.4477 | 2025-09-21 14:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 72.5 |
| bb776d63-dfe2-3313-978e-b209ad990ab7 | -16.0011 | -47.2757 | 2025-09-21 14:40:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 106.6 |
| 0da1e964-e137-3837-9c27-cd66f2b368d2 | -8.8615 | -46.1175 | 2025-09-21 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 60.8 |
| d1995886-dc3d-3f66-9987-6ef5932cf4b3 | -9.8632 | -46.1182 | 2025-09-21 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 112.5 |
| b2249483-244c-3cbd-a008-3d0e2c471b2a | -7.5275 | -44.3182 | 2025-09-21 14:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 105.1 |
| e6e6974f-6698-3697-81d7-752e37f9e3a7 | -10.0314 | -46.2786 | 2025-09-21 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 90.0 |
| aaa458b3-06f1-3a1c-817f-db877d4807c0 | 4.3344 | -60.7406 | 2025-09-21 14:40:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 73.4 |
| f45b81be-a317-3c40-a7cc-560d37815e33 | -4.6658 | -43.6445 | 2025-09-21 14:40:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 8093c905-e392-3699-be03-eaee27a09b08 | -12.1344 | -44.8042 | 2025-09-21 14:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 114.8 |
| 94aacaf2-a275-3c97-8466-bde7ba7d75ad | -9.8442 | -46.1205 | 2025-09-21 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 110.5 |
| a95de293-20a8-337a-968b-7ddaa3b1fe89 | -12.6088 | -45.1244 | 2025-09-21 14:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 136.3 |
| 104fcf11-432a-3907-ae3b-4e2830a2251a | -12.4056 | -51.4113 | 2025-09-21 14:40:00 | GOES-19 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 77.1 |
| b015418b-8fe2-3a31-92a7-79ff1df47522 | -12.3112 | -50.1178 | 2025-09-21 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 9447f8b8-4811-36a1-8192-d6279ced0177 | -12.9349 | -50.5565 | 2025-09-21 14:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 74.3 |
| ac1409cf-94d2-3d91-8db2-47133a39e714 | -3.8228 | -44.1063 | 2025-09-21 14:40:00 | GOES-19 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 101.6 |
| 065f34ef-7274-3144-8137-b12cd7280c6a | -9.0078 | -45.0584 | 2025-09-21 14:40:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 163716dc-21a0-39e3-9401-aede7e02a6dd | -10.0128 | -46.2583 | 2025-09-21 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 0a6d8933-7d4f-365f-a1b1-6cd71edb96a5 | -22.7055 | -51.4221 | 2025-09-21 14:40:00 | GOES-19 | PORECATU | PARANÁ | Brasil | 4120002 | 41 | 33 | nan | nan | nan | Mata Atlântica | 117.0 |
| 30d7628e-56f8-3591-a86d-96c11c95f44b | -7.7336 | -44.3902 | 2025-09-21 14:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 90.0 |
| 523b9b15-6b1e-372f-b846-92cddb534528 | -12.711 | -46.868 | 2025-09-21 14:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 86.5 |
| f2beae21-946a-36db-92fb-54d67cfd5ac4 | -12.8965 | -50.5614 | 2025-09-21 14:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 68.2 |
| aa058c6e-d263-34eb-9b75-e24389aeb12c | -16.8926 | -43.8849 | 2025-09-21 14:40:00 | GOES-19 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 203.4 |
| 7e609d3b-6329-305d-8211-708b40dcd862 | -12.144 | -44.2899 | 2025-09-21 14:40:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 339.5 |
| 95c5f205-19ce-3ef3-9ea6-90ed930da394 | -9.2616 | -45.8485 | 2025-09-21 14:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 49.8 |
| e7d27406-2892-3062-b340-14e1afb2509e | -17.1179 | -45.9256 | 2025-09-21 14:40:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 101.9 |
| db353909-cc39-37bf-a642-239ec71e5f29 | -7.9471 | -43.8828 | 2025-09-21 14:40:00 | GOES-19 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 7dd6d604-f130-31ca-b0ff-1454d9e7da91 | -12.2941 | -49.9904 | 2025-09-21 14:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 6a3465d4-3e3c-38a3-add8-c667d6661bcd | -12.7302 | -46.8651 | 2025-09-21 14:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 74.7 |
| e99f3b01-166f-3c76-afa8-7cd9fd932247 | -12.2983 | -45.2881 | 2025-09-21 14:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 123.3 |
| 81d1a18b-2c7c-3c28-8d3f-1f5f3b8b4e09 | -5.5583 | -42.1507 | 2025-09-21 14:40:00 | GOES-19 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 117.8 |
| 069dcd92-7bbf-3f0d-bd7e-dd3c93170422 | -7.9282 | -43.8848 | 2025-09-21 14:40:00 | GOES-19 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 31b25767-24fd-34c2-9710-d81ba99320c2 | -9.1933 | -45.3114 | 2025-09-21 14:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 98.5 |
| bd3d9e9e-ac87-338d-9bb1-73f584ee49a9 | -4.388 | -43.2896 | 2025-09-21 14:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 87.5 |
| af8d539c-6387-37cd-89c7-5fe1a13552ab | -8.8612 | -46.14 | 2025-09-21 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 53.8 |


