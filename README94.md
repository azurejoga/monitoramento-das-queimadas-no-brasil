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

## Dados Diários - Página 94

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0fb42ed8-80c4-331d-ba57-9b6e8153e592 | -8.0259 | -45.1397 | 2025-10-28 14:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 52.3 |
| 5a75ad0e-94a3-3c14-ba5b-cf95f563157f | -13.9469 | -47.7371 | 2025-10-28 14:30:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 57.3 |
| 433a5c6b-b34a-3028-be5f-b8faebd2bde2 | -13.9275 | -47.7401 | 2025-10-28 14:30:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 69.4 |
| e8cd4ad8-8eea-3944-bc24-40e28325c210 | -8.1106 | -44.3749 | 2025-10-28 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 53.1 |
| beff0203-0c93-3a58-97f3-4ff5dff4df8a | -7.1227 | -47.0154 | 2025-10-28 14:30:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 42.5 |
| b24e8ee0-ee61-32a8-be7f-cd954f03a5ce | -7.8035 | -46.4681 | 2025-10-28 14:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 116.8 |
| 23edad4a-8327-31ab-a72d-a007c5ba7b8e | -4.2457 | -42.2408 | 2025-10-28 14:40:00 | GOES-19 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 71.0 |
| 8299460a-bfad-3b80-ad33-4fa2d44c52ab | -7.8225 | -46.444 | 2025-10-28 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 73.1 |
| dc712dd1-061f-3f81-8c45-04e0b5496a59 | -8.0447 | -45.1378 | 2025-10-28 14:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 50.0 |
| 0dcae844-fa66-3bfc-967d-a3826e2b94ed | -14.4285 | -47.8626 | 2025-10-28 14:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 105.3 |
| 0671d7e8-11f8-37a7-a8b8-fc1af73cf041 | -13.9337 | -48.4305 | 2025-10-28 14:40:00 | GOES-19 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 135.0 |
| a7c3a76d-78c0-37f9-a88e-0a53ecc94ec4 | -7.6675 | -46.8806 | 2025-10-28 14:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 83.6 |
| ac76efbf-26ff-3dd4-b6ae-12b4321aa9dc | -10.0188 | -47.1528 | 2025-10-28 14:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 97.0 |
| 9814c4d0-ff13-3be7-8d3d-9698bb94c349 | -9.7939 | -47.0003 | 2025-10-28 14:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 154.4 |
| 48e148ef-a00c-3a85-a93a-3d66f6f7f30c | -7.7489 | -44.6873 | 2025-10-28 14:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 9bc246d1-d0c8-300c-b3e7-2f63fd3256ba | -10.9224 | -47.6009 | 2025-10-28 14:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 71.0 |
| e8d790dc-8264-3304-82e0-80ce10422bc0 | -10.9418 | -47.5763 | 2025-10-28 14:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 35.6 |
| b2284c53-98ef-39a3-b099-1d06354bfee0 | -9.4929 | -46.9001 | 2025-10-28 14:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 114.6 |
| db021923-644b-3153-bac4-dd136120efee | -9.9629 | -47.0925 | 2025-10-28 14:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 130.6 |
| 2f583a67-3dcc-380b-86c5-fa9ea72bcafa | -10.3027 | -47.1644 | 2025-10-28 14:40:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 93.2 |
| d84d6593-030f-3384-b57f-bc8e875440b7 | -13.9143 | -48.4335 | 2025-10-28 14:40:00 | GOES-19 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 94.0 |
| e3578f5a-3a05-3447-abdd-5c170306d9d7 | -9.5298 | -46.9628 | 2025-10-28 14:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 320.2 |
| 3a4ffcb3-4485-3a00-8f0d-1b8f91e15bfa | -10.3208 | -47.229 | 2025-10-28 14:40:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 62.0 |
| fe450343-d82e-3359-97e9-8f017672f940 | -7.686 | -46.9011 | 2025-10-28 14:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 125.0 |
| eacea3e8-c7da-3268-89a8-867d46bb42b1 | -7.5242 | -46.27 | 2025-10-28 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 44.5 |
| d901489f-1d9e-3135-9081-c507c883afc1 | -13.2691 | -47.8846 | 2025-10-28 14:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 849d6507-fbbc-3563-a70b-c27d6356b932 | -13.2258 | -47.1066 | 2025-10-28 14:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 66.9 |
| 7a01d23b-4c3c-3864-aa29-f36c4f3c0787 | -3.9993 | -49.0295 | 2025-10-28 14:40:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 77.1 |
| 3ccbe84f-b27f-360e-ad5c-7e7a077aa33a | -9.9809 | -47.1571 | 2025-10-28 14:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 0e9649fc-de39-36a9-a1f4-d6912e857c69 | -9.7942 | -46.978 | 2025-10-28 14:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 120.7 |
| cbada622-1c2f-33d2-af5a-2a879f895fc2 | -8.0444 | -45.1606 | 2025-10-28 14:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 51.7 |
| 09ad3548-8769-3ec2-b1ad-4be5d470d0e4 | -7.0745 | -44.4756 | 2025-10-28 14:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 39.5 |
| 8d6c90fd-2aaa-3c66-8240-f53f06906b21 | -13.6435 | -46.4519 | 2025-10-28 14:40:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 92.7 |
| fde7b643-f4aa-3a71-878c-24fbe07ab1cb | -8.0256 | -45.1625 | 2025-10-28 14:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 43.0 |
| 6c385119-6d9c-3d0b-84c4-483815a81a38 | -7.8418 | -46.3976 | 2025-10-28 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 60.7 |
| 32803094-b4f8-3d41-9ef5-fb92b8a59d9c | -9.9 | -44.9069 | 2025-10-28 14:40:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 354.7 |
| 0f586ccd-9506-3be2-b6e5-c53e2cdef47b | -7.9691 | -46.7646 | 2025-10-28 14:40:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 59.6 |
| 7368a972-237e-33ed-b0c2-d1795b4377f6 | -14.374 | -51.8252 | 2025-10-28 14:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 87.1 |
| 76694304-3b05-3c03-bba2-9c6ae12184b8 | -6.5065 | -44.9813 | 2025-10-28 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 60.3 |
| a628977d-1ca3-3c5d-aff8-667e50da1388 | -8.5036 | -47.6426 | 2025-10-28 14:40:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 113.0 |
| f513e8b5-85e5-316d-bff2-1588fe2398b0 | -7.9652 | -45.4863 | 2025-10-28 14:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 49.7 |
| e4161594-2db2-3942-ad83-273bbca76af6 | 1.6203 | -55.7062 | 2025-10-28 14:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 0aa879f8-f343-374c-b6b9-35a263baf824 | -9.546 | -45.7935 | 2025-10-28 14:40:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 112.3 |
| 7351823a-949a-3f00-b9d4-e27509021e73 | -9.3491 | -49.2589 | 2025-10-28 14:40:00 | GOES-19 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 49b70509-bdfc-3874-9ac5-de4bf1b78841 | -7.1227 | -47.0154 | 2025-10-28 14:40:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 49.3 |
| 9e4edb3a-7539-37ba-8d5c-10fc8c864e93 | -8.1883 | -47.2979 | 2025-10-28 14:40:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 49d0fcf7-ac29-350f-8217-84e3dea760ff | -11.1141 | -44.0244 | 2025-10-28 14:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 92.5 |
| ef881fe7-638f-3464-8e6d-870350c6063f | -9.4739 | -46.9021 | 2025-10-28 14:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 110.4 |
| 87f5a8cd-f165-3b63-8f80-157c9f3d555d | -6.6894 | -45.4198 | 2025-10-28 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 53.0 |
| 98ba9f09-d1cc-31c4-b85c-96edf3dd8056 | -3.0148 | -41.6851 | 2025-10-28 14:40:00 | GOES-19 | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Caatinga | 85.8 |
| 2818f66f-a7b6-3e30-aa1a-4f1b240d16af | -10.3507 | -47.7793 | 2025-10-28 14:40:00 | GOES-19 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 56.8 |
| 18881371-9a78-3fc2-8fd2-b403499d79f7 | -15.2003 | -47.2142 | 2025-10-28 14:40:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 54.4 |
| 9a1a7a7b-25b1-3ffc-bef7-2194592b6489 | -8.5588 | -47.7472 | 2025-10-28 14:40:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 70.3 |
| d27b16ec-2ac6-3226-98d3-53581c69dacf | -10.3401 | -47.2045 | 2025-10-28 14:40:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 62.9 |
| ce683597-9bc7-3847-9662-0deb0b86d6c8 | -14.6698 | -48.4052 | 2025-10-28 14:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 4db710de-f6d5-33db-8c5d-585f9d285e4a | -9.9815 | -47.1126 | 2025-10-28 14:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 135.3 |
| ac035ac3-75cf-3e89-8abc-153cddab30b3 | -9.9626 | -47.1147 | 2025-10-28 14:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 142.8 |
| 0b0a1292-141d-3a18-9a9a-2fc3610d2fe8 | -8.1454 | -47.7636 | 2025-10-28 14:40:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 56.7 |
| 5f46038d-7f87-3cb6-9f83-f995ab3d6393 | -10.3021 | -47.209 | 2025-10-28 14:40:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 80.8 |
| a605fdd6-3d87-3147-9066-f346a742568d | -9.9818 | -47.0903 | 2025-10-28 14:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 114.5 |
| 6ba41303-1444-3126-899d-a33d23ebceaa | -3.9992 | -49.0508 | 2025-10-28 14:40:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 0d0c8ec3-747f-303f-b74a-fbfe6e90cecb | -9.549 | -46.9385 | 2025-10-28 14:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 115.1 |
| 23bb795a-6f2b-3672-a3b9-bebd1ecdb45d | -14.9045 | -52.4354 | 2025-10-28 14:40:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 85.9 |
| ab84132a-26c7-35d2-8518-e5bc4f51d2c2 | -9.3488 | -49.2805 | 2025-10-28 14:40:00 | GOES-19 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 83.7 |
| b746c384-c4d5-36f7-9ddd-d4fe25517bad | -13.6846 | -48.3347 | 2025-10-28 14:40:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 56.2 |
| 07213d90-405f-3f15-98b9-ba590b596458 | -7.369 | -45.0204 | 2025-10-28 14:40:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 50.9 |
| ccc34c49-d5e4-3a05-9593-0c26d08100a2 | -4.6121 | -43.3227 | 2025-10-28 14:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 66.1 |
| facd4537-1c71-37b2-b9dc-e6dac959f12b | -10.3024 | -47.1867 | 2025-10-28 14:40:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 82.4 |
| ef1cb6e7-4f0b-3e2e-b288-06afd246a31f | -9.1846 | -44.579 | 2025-10-28 14:40:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 106.3 |
| 86fab55c-5ab3-340a-9ce2-640e560620b2 | -8.3245 | -45.3597 | 2025-10-28 14:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 52.2 |
| 5fc0e667-904b-31cd-b437-b575abd804c0 | -10.9221 | -47.6231 | 2025-10-28 14:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 44.6 |
| cde985cc-83e4-3b2c-9d90-4d2acf9d6b0f | -13.2262 | -47.084 | 2025-10-28 14:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 810f1464-0295-3c89-b74f-444db8c5b412 | -14.3982 | -51.5443 | 2025-10-28 14:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 401ee0cc-2c8b-3fcf-a050-79cb7b77d2fa | -13.2695 | -47.8622 | 2025-10-28 14:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 47.0 |
| d2cf1f8d-3d6d-325b-9d4b-3c6bdbd38f37 | -8.4689 | -45.8655 | 2025-10-28 14:40:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 78.0 |
| ac8ff420-7977-382f-969b-1b788339137c | -8.1352 | -47.0154 | 2025-10-28 14:40:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 3948584d-d642-386f-ab2f-cf7f8219c926 | -10.3018 | -47.2312 | 2025-10-28 14:40:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 6d4873ea-40e0-37f1-807b-f9fae798b053 | -4.227 | -42.2419 | 2025-10-28 14:40:00 | GOES-19 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 73.7 |
| 8f87f165-bf6f-3616-8f75-ac7b48ff875e | -13.6842 | -48.357 | 2025-10-28 14:40:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 93.0 |
| cdfa7769-da9f-35d3-b88a-3ca503c7cc94 | -8.646 | -45.2806 | 2025-10-28 14:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 44929cde-680a-39c9-86cf-c67eb20b8541 | -4.9138 | -42.9998 | 2025-10-28 14:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 441aa5e1-d3a3-3b56-aaf8-43a81d83a97d | -13.9465 | -47.7595 | 2025-10-28 14:40:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 249.2 |
| 8dd0fee4-b78e-37b7-a00a-3e0138f9e5ec | -13.9275 | -47.7401 | 2025-10-28 14:40:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 71.7 |
| ec2e2a2c-ad9f-32d0-a5f7-87e350787fec | -7.8223 | -46.4664 | 2025-10-28 14:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 75.9 |
| b9e919ef-705e-33df-8ba3-183b9582a750 | -8.6062 | -45.4439 | 2025-10-28 14:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 116.8 |
| 0b17ee2c-fe83-3a54-af74-efb1d682b702 | -14.6304 | -48.4337 | 2025-10-28 14:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 053d8f5b-0ea4-3b34-9463-155bee2816c0 | -8.6065 | -45.4212 | 2025-10-28 14:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 6b1f7b0e-5633-3695-94db-43875b95ed51 | -10.3317 | -47.7814 | 2025-10-28 14:40:00 | GOES-19 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 118.6 |
| e5eb2656-8f3a-378f-8791-f02987d9c189 | -14.9041 | -52.4566 | 2025-10-28 14:40:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 97.5 |
| 70bb30a9-ebe2-36c9-87f2-155a81095b46 | -10.0378 | -47.1506 | 2025-10-28 14:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 70271eb8-67bb-33d3-b70b-d90787f647e0 | -7.7678 | -44.6855 | 2025-10-28 14:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 53.3 |
| 75d34462-90f2-3d4e-acb9-bdbd1eb4a002 | -9.4854 | -46.0717 | 2025-10-28 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 124.8 |
| 518ac078-97ea-3d9c-be86-bd45893ee1e1 | -4.4431 | -43.4259 | 2025-10-28 14:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 96.4 |
| 7ab8982e-2507-3e17-95c1-b0c6746a9b70 | -10.9609 | -47.574 | 2025-10-28 14:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 39.4 |
| b8efc0a3-2488-39df-8cb3-26453c7b005f | -10.3217 | -47.1621 | 2025-10-28 14:40:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 94.7 |
| 0335457e-8751-3768-bf48-1cd6a5433922 | -6.0974 | -44.6718 | 2025-10-28 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 167.4 |
| 0d322108-c205-3e44-8bc2-59fef6d2b800 | -2.95 | -43.4993 | 2025-10-28 14:40:00 | GOES-19 | HUMBERTO DE CAMPOS | MARANHÃO | Brasil | 2105005 | 21 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 47b24809-5cca-318a-912c-5fee8a58e8e1 | -4.3424 | -41.8067 | 2025-10-28 14:40:00 | GOES-19 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 74.5 |
| fd5852ee-9fe1-3eb3-a953-d7aa30296919 | -14.2975 | -52.9366 | 2025-10-28 14:40:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 97.7 |
| 17e92e78-6d96-38dc-ae16-b8450dfb70ec | -9.9632 | -47.0702 | 2025-10-28 14:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 87.8 |


[Clique aqui para ver as próximas entradas](README95.md)
