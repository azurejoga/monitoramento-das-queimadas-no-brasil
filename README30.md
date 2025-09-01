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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 36e6e987-b5ab-30b3-ad2b-8dbca056b40d | -7.95155 | -46.3552 | 2025-09-01 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5951ce97-92a8-38ca-98bb-402aaa979930 | -11.07654 | -52.06259 | 2025-09-01 04:10:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4bbdf606-ebc1-3292-abca-0ca3c27383ce | -6.81658 | -43.33933 | 2025-09-01 04:10:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c28d9439-cb94-30c0-b115-ced0b3be4129 | -7.24357 | -44.05997 | 2025-09-01 04:10:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6df60f55-c1bc-3b24-83ad-36a1c533da08 | -8.15566 | -43.00748 | 2025-09-01 04:10:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 972683bd-2101-30c9-b98a-b18a9bdc01d0 | -7.87714 | -46.97793 | 2025-09-01 04:10:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ff4d0070-f1c5-35dd-aeec-495fdf390f7f | -11.45348 | -46.81585 | 2025-09-01 04:10:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 789d78a3-937f-3e83-a37f-1b3ea3d15f48 | -11.37314 | -43.61703 | 2025-09-01 04:10:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2fdf31b5-b29e-35ed-b248-2833883bad99 | -8.00006 | -44.04806 | 2025-09-01 04:10:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c6da3a99-c636-3437-95e6-9fa1dc427a03 | -7.11505 | -44.76202 | 2025-09-01 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 747490d7-58cc-3899-bb96-0ce66af5a95f | -6.28411 | -43.56678 | 2025-09-01 04:10:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e137bf59-fb05-3fc3-af40-e4096684c6d4 | -6.75818 | -43.78234 | 2025-09-01 04:10:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 55a70d7c-db31-3ab4-a9fe-75b9a159a96a | -8.77137 | -46.10511 | 2025-09-01 04:10:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 059e1ec7-c485-3dfd-b43d-5faed92a284d | -9.01129 | -50.11619 | 2025-09-01 04:10:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 84b65a00-1c06-32f6-a165-fbc66f223356 | -6.75692 | -43.79003 | 2025-09-01 04:10:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| c8e1c4e6-2f17-327f-8ff9-f65a41414f37 | -8.83262 | -47.8086 | 2025-09-01 04:10:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 284dd3eb-0cb8-34cb-bc90-fdca80fe31bc | -6.7528 | -43.79332 | 2025-09-01 04:10:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| f1ef736b-f266-32fb-9cbc-8af75a3bae30 | -6.15353 | -43.34182 | 2025-09-01 04:10:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 99b40669-67ad-3260-9c51-5cdb859ee8cb | -10.47869 | -51.63226 | 2025-09-01 04:10:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b3131d82-3f93-392d-a27d-c311c0a87623 | -12.09834 | -44.72116 | 2025-09-01 04:10:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 66fea277-2f29-355f-b3c9-193980863ff0 | -6.37179 | -43.56101 | 2025-09-01 04:10:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 54fd637e-4c5e-31e7-9dec-54c83b4cd407 | -11.9585 | -45.79782 | 2025-09-01 04:10:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4d51e853-96b0-3c48-b003-1f8bc4d5ebd5 | -11.37164 | -43.58362 | 2025-09-01 04:10:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9ebbd669-c7f9-3d0d-ad90-d4067db20386 | -6.57606 | -43.70233 | 2025-09-01 04:10:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 27302e31-594e-3ec8-8927-351277e30054 | -11.8974 | -46.73454 | 2025-09-01 04:10:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2c4bff82-47e3-3fff-80ed-24e190ef3b44 | -5.36491 | -43.69343 | 2025-09-01 04:10:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 781c5183-b393-3694-bfaa-bb81bbcca67a | -9.67075 | -47.04582 | 2025-09-01 04:10:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 97cf2d2f-64a6-3b02-aa73-de86bb4a5bcc | -11.37578 | -43.64336 | 2025-09-01 04:10:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| db8608c2-3a59-396e-85df-8fc1beebd32e | -7.39237 | -47.43512 | 2025-09-01 04:10:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b0caabb6-91fa-3693-94d9-00ea7b591d2c | -9.6394 | -46.61007 | 2025-09-01 04:10:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4fd608f3-96d3-38fe-b542-299f61215e79 | -6.2426 | -43.39393 | 2025-09-01 04:10:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e05290b4-79d7-3a55-998f-1e37cc039189 | -6.83432 | -44.24426 | 2025-09-01 04:10:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fe84736b-6788-3d1c-a11c-3063ec0fcc94 | -6.81891 | -52.81554 | 2025-09-01 04:10:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ec803514-4255-3eb2-936f-a99674286b3f | -5.98079 | -42.56931 | 2025-09-01 04:10:00 | NPP-375D | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| f023ef2c-0195-388f-af92-0196cce8bbcd | -5.81313 | -43.86703 | 2025-09-01 04:10:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c08d2208-e87b-31da-86c2-7e844d336530 | -9.12636 | -45.19916 | 2025-09-01 04:10:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6588ec5c-1cd4-33db-adec-97b1f5613d68 | -11.08544 | -44.62999 | 2025-09-01 04:10:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e0abb945-c7bd-3b4b-9f01-8d4fa085fe64 | -7.07231 | -44.35908 | 2025-09-01 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 294cd087-7a7c-308f-9fff-61f4f397387b | -6.77595 | -44.62349 | 2025-09-01 04:10:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ca1ff452-d703-3a2a-a8af-7776e1655e67 | -11.37094 | -43.60928 | 2025-09-01 04:10:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 84078a27-8bbd-3872-b4d6-d8cc943828f7 | -6.71547 | -42.25381 | 2025-09-01 04:10:00 | NPP-375D | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 13e7fd09-77bb-3081-9dc1-5e7efb4d3a82 | -8.16764 | -45.0345 | 2025-09-01 04:10:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 16703cdf-9ab4-351c-bf9a-ecc5f0d5776e | -6.09154 | -43.33192 | 2025-09-01 04:10:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4a3290f5-5c7d-3a85-a901-8b65fd437d12 | -8.33329 | -47.44276 | 2025-09-01 04:10:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c793c48b-e791-3573-b758-f03ee398e348 | -7.95075 | -46.36008 | 2025-09-01 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d36fc387-7562-313a-b49f-a6bfb0497548 | -7.10008 | -44.55886 | 2025-09-01 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b33171f6-d6f6-344a-93fe-965a1aaddb19 | -6.19609 | -45.37527 | 2025-09-01 04:10:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cd512f37-71e6-310f-92bf-74cd9ecfd1f2 | -11.04704 | -46.95971 | 2025-09-01 04:10:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7eb80fb3-0ec7-324c-8a59-72926f2b15aa | -6.28462 | -43.28572 | 2025-09-01 04:10:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| aaf53fa7-0bcd-31cb-9de3-8d179f957a63 | -7.50571 | -45.83754 | 2025-09-01 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| ce0debd4-17ef-3b50-b59c-88892e2e850d | -7.46424 | -44.81859 | 2025-09-01 04:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 18c4ba40-fb80-38d7-acda-50c76f5900e4 | -11.47759 | -46.79059 | 2025-09-01 04:10:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 291c32fd-5b07-3e1d-a999-22bf0aee6097 | -7.32929 | -44.08594 | 2025-09-01 04:10:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5eb66987-ca70-37c6-a030-7356ce3c4be0 | -6.32767 | -43.53924 | 2025-09-01 04:10:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2fa9d137-3491-38ac-9ba2-63a86a43bb90 | -11.89327 | -46.69681 | 2025-09-01 04:10:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 98eb6cf7-e329-3094-ae4c-c12ec203b280 | -11.3446 | -43.51663 | 2025-09-01 04:10:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 82ff1068-cdaa-3bc8-a115-8f38c2623026 | -6.4244 | -43.96901 | 2025-09-01 04:10:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d96a17b5-54c0-33f9-af40-5a7f5b362643 | -6.41799 | -43.62722 | 2025-09-01 04:10:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f7a1ea80-9627-333b-b5ed-b1a274197237 | -7.66182 | -42.70892 | 2025-09-01 04:10:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 25965bb6-d0cd-3ab6-b9f9-197968a342ee | -10.23827 | -51.10682 | 2025-09-01 04:10:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a983529c-602f-30ce-9f9b-c617055a163d | -10.02801 | -48.36611 | 2025-09-01 04:10:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7f50cf05-950f-323a-8d11-3eb370879c53 | -11.87398 | -46.74173 | 2025-09-01 04:10:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b170fcdc-54fb-301b-b4b8-c88709eed8cb | -6.80043 | -52.81463 | 2025-09-01 04:10:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 79c2e25f-f1e2-3290-ba5c-4bb5c1c9105d | -8.09319 | -49.93895 | 2025-09-01 04:10:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2e3054a3-f19b-3fc7-bc65-2ff781e71379 | -6.9351 | -42.02023 | 2025-09-01 04:10:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| a658b04a-13d8-3da5-b017-61356a2feff3 | -6.80057 | -52.81211 | 2025-09-01 04:10:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 7bd9f405-f467-34bf-97a7-30839714559c | -11.80859 | -46.41836 | 2025-09-01 04:10:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 68b8526d-c9c3-39ba-9297-cbc8eebd7085 | -6.8185 | -43.33281 | 2025-09-01 04:10:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 55d9ec2b-fd73-3042-970d-fb5a5f707c3f | -9.63633 | -46.60451 | 2025-09-01 04:10:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 91005242-2c1d-38ac-9699-7ec0ae54674c | -6.83835 | -43.3352 | 2025-09-01 04:10:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 67c20d32-8826-380f-b0c6-4e4a0dbfc8c2 | -8.16695 | -45.0388 | 2025-09-01 04:10:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c8b48e28-1a02-3737-8dbd-a22b7cff7e6b | -6.83194 | -52.81348 | 2025-09-01 04:10:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 86fb465e-e64f-3db2-9bf2-2b6b0b8fc337 | -6.84332 | -52.82037 | 2025-09-01 04:10:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| aa9a7530-21f2-3108-b92d-6dd16a353269 | -10.37016 | -52.28868 | 2025-09-01 04:10:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4b59affd-a332-38c9-90c1-c5f466552639 | -6.35242 | -43.92208 | 2025-09-01 04:10:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b2175b65-1c74-3e96-9ecf-b2510d9ac67d | -6.95164 | -44.29923 | 2025-09-01 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3553ee85-baeb-30fd-a736-505a7c951397 | -7.38252 | -47.44165 | 2025-09-01 04:10:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1f40b265-1a96-3b30-859d-b7e6f8949a04 | -7.50188 | -45.83692 | 2025-09-01 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 9dd97cca-e5a4-3af9-82f3-7bc1ef77b5a1 | -7.6256 | -42.65582 | 2025-09-01 04:10:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d9798e4f-1dc5-3e59-ba94-93807090a779 | -11.35569 | -43.53316 | 2025-09-01 04:10:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1a2cb5a5-e9cc-3d95-bb89-41e5cd896acb | -8.44527 | -47.37261 | 2025-09-01 04:10:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b2688f9e-faf7-3d0f-b361-39005858ca35 | -11.02724 | -47.02813 | 2025-09-01 04:10:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 32c9c6ac-5788-353e-a470-523bd075d045 | -7.38745 | -47.43838 | 2025-09-01 04:10:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 45dbf0fa-8292-33f3-bd8a-5f4d0b64cd71 | -6.83633 | -52.82394 | 2025-09-01 04:10:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 659deb3b-ccd8-3ff4-8c00-1f8289c8d5b5 | -7.65903 | -42.70482 | 2025-09-01 04:10:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 1e88c098-ef15-3ac9-a6a0-4e483ada86d2 | -11.04667 | -46.98522 | 2025-09-01 04:10:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a6d76eff-8d79-3d6e-a866-9032df8e942b | -6.51351 | -42.94554 | 2025-09-01 04:10:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e6e71d0b-bc7c-3fa4-99b2-62fe59594c7b | -10.04164 | -48.09001 | 2025-09-01 04:10:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| adf2ebdd-1964-3e50-abc0-f69511ba6420 | -11.03958 | -45.14568 | 2025-09-01 04:10:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 125.8 |
| 9e6e3069-0178-3e3f-b837-477d915e7f43 | -7.97659 | -46.41859 | 2025-09-01 04:10:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 005251b8-484f-3399-a59a-d691838b206f | -6.77163 | -44.6272 | 2025-09-01 04:10:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 004c73ab-3819-32ad-b720-9ebfbb341201 | -6.28709 | -43.30915 | 2025-09-01 04:10:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 583c3bf8-f57f-39c3-a9de-9c5da634d0bd | -9.63641 | -46.60657 | 2025-09-01 04:10:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cf90fd12-a27c-3b5c-8a2f-9c16f52eec3b | -6.94286 | -42.01431 | 2025-09-01 04:10:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b9cd9a92-cfba-39bb-990b-56a17ef582a4 | -6.33094 | -43.56314 | 2025-09-01 04:10:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8dd8573d-0a5a-32ce-bbc9-ee08399857fa | -6.85908 | -52.80337 | 2025-09-01 04:10:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 14d373f6-be6c-3d8b-8d76-5f40d4817698 | -6.74385 | -43.77719 | 2025-09-01 04:10:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a520a58a-166d-35c6-a86d-265cb5ccd3cd | -6.31336 | -43.78429 | 2025-09-01 04:10:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5052b537-fe9e-3361-b662-dbca68347ef2 | -8.88207 | -47.21014 | 2025-09-01 04:10:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 389e680c-c245-304f-9962-db8a62bf0be4 | -6.75343 | -43.78946 | 2025-09-01 04:10:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |


[Clique aqui para ver as próximas entradas](README31.md)
