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

## Dados Diários - Página 141

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b382d08e-f72b-3a31-94d0-c85d07f355a7 | -11.7211 | -46.5127 | 2025-09-11 13:20:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 445.4 |
| 0e3aca51-1aae-3790-a742-7a11ecef1f61 | -9.0579 | -46.9688 | 2025-09-11 13:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 76a1f856-7448-38ee-8558-4209430cad2b | -8.9368 | -46.132 | 2025-09-11 13:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 110.6 |
| 7f439ff1-60dc-30b5-92ba-8401b26fbcbd | -6.2228 | -43.3226 | 2025-09-11 13:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 90.3 |
| 462786d9-d0b8-308d-b1dd-15a76503fe20 | -15.8014 | -52.2258 | 2025-09-11 13:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 829d08bf-1073-332f-a6d8-932fc5e03c8f | -15.1016 | -50.1468 | 2025-09-11 13:20:00 | GOES-19 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 153.7 |
| ad1e9639-a6be-3fce-ae28-b7729f0865e1 | -15.1021 | -50.1249 | 2025-09-11 13:20:00 | GOES-19 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 82.9 |
| e5864e69-9e90-329b-8975-8a107847eddb | -10.184 | -46.2153 | 2025-09-11 13:20:00 | GOES-19 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 131.8 |
| 289218a5-ac0e-3909-8721-ffaf6c9e9359 | -6.3041 | -53.4562 | 2025-09-11 13:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 62.6 |
| e1aaedcc-836a-34a2-b2b8-685c12b27784 | -8.7411 | -45.2248 | 2025-09-11 13:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 126.4 |
| 468e0a30-ccd6-35ca-a031-db4204e09a26 | -6.0784 | -44.6961 | 2025-09-11 13:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 532923d1-9fee-3662-aa59-caae1a2d189d | -16.6335 | -49.7683 | 2025-09-11 13:20:00 | GOES-19 | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 192.4 |
| d0d0bbc4-c986-351a-94c8-43e82f1f45c3 | -9.0265 | -49.5046 | 2025-09-11 13:20:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 117.3 |
| 9424b3e8-23e0-35f8-be7a-08618f9060a7 | -15.801 | -52.2472 | 2025-09-11 13:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 77.0 |
| e3b9d80a-d00c-39a5-bce3-9fee8d478051 | -15.1759 | -52.4199 | 2025-09-11 13:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 86.2 |
| adb1f604-a571-3ca2-bcae-4f6f08f994d3 | -15.1211 | -50.1438 | 2025-09-11 13:20:00 | GOES-19 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 85.6 |
| 828c5c72-cab7-3579-bcec-253645283eec | -10.5671 | -47.2442 | 2025-09-11 13:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 295.5 |
| ea586ad3-d101-348a-ab65-5422de806b23 | -12.6829 | -45.2746 | 2025-09-11 13:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 87.9 |
| ec8b2f3c-d1e4-3a92-9898-d32a06674550 | -10.7366 | -46.1011 | 2025-09-11 13:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 173.0 |
| 4137c951-270e-30f7-9bb1-76594f9f97bd | -9.1514 | -47.0257 | 2025-09-11 13:20:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 108.0 |
| 42890d45-4daa-36ea-90a7-09e454b078a8 | -8.0772 | -45.5659 | 2025-09-11 13:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 95.4 |
| df9cbaa1-e604-3db8-8a2f-a323e003b26b | -6.4364 | -44.4847 | 2025-09-11 13:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 90.1 |
| 7f9a5996-4a6f-3dc2-a767-ed63bc09b5b5 | -14.5128 | -53.9158 | 2025-09-11 13:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 2f834806-d004-30d7-a575-5f47fdf75ec0 | -7.559 | -48.2723 | 2025-09-11 13:20:00 | GOES-19 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 7d1b9b46-8e09-38c5-80ef-80c119fb288b | -8.1103 | -49.2419 | 2025-09-11 13:20:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 77.5 |
| ed760ed6-c5a0-39b4-ab60-f64c0ef59c8c | -9.0262 | -49.5261 | 2025-09-11 13:20:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 86.2 |
| b92107cc-e094-3ffc-a9e0-6506dc57745b | -11.7115 | -48.2536 | 2025-09-11 13:20:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 160.1 |
| 9244efbd-5440-3add-8538-dc4640000f71 | -8.1649 | -46.0983 | 2025-09-11 13:20:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 104.5 |
| d1039317-0927-3235-97e0-2683ec845a6c | -15.6737 | -47.016 | 2025-09-11 13:20:00 | GOES-19 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 100.9 |
| db544db3-0b0d-3fba-8ff4-dd8698d03a01 | -9.7634 | -47.8447 | 2025-09-11 13:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 98.3 |
| 0bd6706b-c3c3-3191-b3f4-8bb0a4dc3bbd | -10.7369 | -46.0785 | 2025-09-11 13:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 105.3 |
| 05a7923b-0bac-3cbf-b77a-41dba42998bf | -9.0358 | -45.783 | 2025-09-11 13:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 46.9 |
| 591a0e46-ad25-3bca-b31c-57f036de5202 | -6.0784 | -44.6961 | 2025-09-11 13:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 7641d81d-fe60-3fd7-95b0-6416291ef606 | -13.2798 | -51.7312 | 2025-09-11 13:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 107.3 |
| 9bfcfd8a-7b16-3fc8-9c63-7619fd0c42d3 | -8.994 | -46.0808 | 2025-09-11 13:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 103.1 |
| 5e60d023-3684-32fb-a444-af985c619c59 | -9.7634 | -47.8447 | 2025-09-11 13:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 82.3 |
| b2a761ab-4177-3efb-85f4-264258a9d321 | -10.7557 | -46.0987 | 2025-09-11 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 699.0 |
| 02ddec3c-4ec1-3d06-985e-7e913e107593 | -15.6732 | -47.0389 | 2025-09-11 13:30:00 | GOES-19 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 244.5 |
| ee6cb897-fd7a-3b8c-95e2-3bf10f5ccf37 | -15.8014 | -52.2258 | 2025-09-11 13:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 71.3 |
| a305a722-492d-35e9-9464-596133f4be12 | -16.6335 | -49.7683 | 2025-09-11 13:30:00 | GOES-19 | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 138.7 |
| 4f8373fa-dd01-33ad-8837-703dfd52528f | -9.1331 | -46.9831 | 2025-09-11 13:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 75.6 |
| b5ae8923-fda8-3698-aeb1-fed239aa53c6 | -4.553 | -43.7439 | 2025-09-11 13:30:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 76.8 |
| badbfa91-ccda-3612-8c36-3cb99cd2f3a3 | -15.6737 | -47.016 | 2025-09-11 13:30:00 | GOES-19 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 94.8 |
| e0efae54-68a6-31bd-ba5f-cf551bd5d719 | -15.1016 | -50.1468 | 2025-09-11 13:30:00 | GOES-19 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 127.3 |
| f85c192d-a041-3689-9e1d-31cb1f4b4e59 | -9.7445 | -47.8468 | 2025-09-11 13:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 171.9 |
| 55f3447b-59ca-3150-8c36-dca069764259 | -11.4093 | -43.5573 | 2025-09-11 13:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 144.6 |
| 55e21f7b-fef2-3c79-b187-ef80a10b6a34 | -8.9368 | -46.132 | 2025-09-11 13:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 79.1 |
| fe126d2f-fe03-35e8-9296-0fa4a6b95086 | -9.0567 | -47.0577 | 2025-09-11 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 79.0 |
| b38b4670-f0b8-356e-a696-a98c80b8b934 | -8.7411 | -45.2248 | 2025-09-11 13:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 91.8 |
| 6a9f4d78-4127-3251-b430-3746af015669 | -11.7112 | -48.2757 | 2025-09-11 13:30:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 270.2 |
| f7d47650-cbf1-34be-8ba5-081460b808eb | -13.2599 | -51.7761 | 2025-09-11 13:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 111.9 |
| 50a25ca3-b1f6-3250-9488-6e1ec4014080 | -6.8525 | -47.8707 | 2025-09-11 13:30:00 | GOES-19 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 89bf8755-b8e0-34d0-9fb7-e072cd616aa5 | -11.9898 | -47.5748 | 2025-09-11 13:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 100.6 |
| 39335d76-63d0-3359-90a5-aab41b7888b1 | -14.3122 | -45.046 | 2025-09-11 13:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 102.1 |
| 37788d68-325f-3ef7-8d68-b38f5a80ac9e | -11.7782 | -46.5274 | 2025-09-11 13:30:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 90.1 |
| 8e08a51b-a825-3937-a918-cc34cfc3d337 | -9.976 | -50.3334 | 2025-09-11 13:30:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 58.4 |
| c04a3f6d-3c6b-3003-951d-2df84946f9e0 | -8.9365 | -46.1545 | 2025-09-11 13:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 148.5 |
| e7bc11f0-2a00-34a7-826a-92a6e7ac9e47 | -7.8708 | -45.5181 | 2025-09-11 13:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 137.3 |
| 819bd438-5dd4-339b-b8fb-22d6c25f549a | -9.9951 | -50.3102 | 2025-09-11 13:30:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 84.8 |
| ae4490d9-3bcb-3294-9b61-f17c40cf7d09 | -6.1705 | -41.0658 | 2025-09-11 13:30:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 95.5 |
| 21df9b83-e850-38d9-a451-ab38366212da | -6.8187 | -45.6123 | 2025-09-11 13:30:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 47080bca-5c50-3590-a089-442061b8c06b | -9.4804 | -46.4321 | 2025-09-11 13:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 126.9 |
| 026da840-0630-3b08-b530-bd7b71464ead | -6.3158 | -43.4081 | 2025-09-11 13:30:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 9935c316-221c-3f8b-bb9d-0d8d06d3a33c | -13.2602 | -51.7548 | 2025-09-11 13:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 285.1 |
| 544d2887-dd39-3360-87c0-4207ae7f073a | -11.0959 | -51.3443 | 2025-09-11 13:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 101.3 |
| 6e29b085-b141-3174-a20b-faa307c0caff | -11.391 | -43.5128 | 2025-09-11 13:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 94.1 |
| 170362f4-4e39-3696-b0d7-9b3c64af6a28 | -15.8006 | -52.2687 | 2025-09-11 13:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 869ac80f-206b-30ee-ad21-f519f2803ca2 | -15.1759 | -52.4199 | 2025-09-11 13:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 4c124871-3cba-333b-a06a-e94d2a8fbc9c | -9.0074 | -49.5278 | 2025-09-11 13:30:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 30f78d4e-1bed-32b0-bc97-0059e3fb5ca9 | -10.7366 | -46.1011 | 2025-09-11 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 277.1 |
| 58695580-2778-35b5-b4c2-d1f950ceb6c0 | -9.0942 | -47.076 | 2025-09-11 13:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 96.3 |
| 9717a4d5-8aa9-3205-9cc2-a4fd379373e4 | -11.7115 | -48.2536 | 2025-09-11 13:30:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 230.4 |
| df1cf96b-17df-31a3-9524-27656a476da0 | -9.4797 | -46.477 | 2025-09-11 13:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 102.1 |
| 47ede131-e56e-3cb5-a76c-cd1092bb3065 | -10.5671 | -47.2442 | 2025-09-11 13:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 160.6 |
| bfcaa73b-74fd-385b-a0f5-caa42003192d | -9.0753 | -47.078 | 2025-09-11 13:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 103.4 |
| 5f01c779-31c7-3e84-8220-7ccf7b400596 | -11.0997 | -48.4392 | 2025-09-11 13:30:00 | GOES-19 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 88.8 |
| d6e9c2cb-0727-328b-8a7f-1ad7349f7944 | -9.0262 | -49.5261 | 2025-09-11 13:30:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 96.6 |
| f2d8d036-ae59-355f-bcee-f4c8363809e4 | -9.0565 | -47.08 | 2025-09-11 13:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 5a1e1725-854f-3bc7-9811-747cd3b9a86f | -7.1721 | -44.1444 | 2025-09-11 13:30:00 | GOES-19 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 89.8 |
| 5bdf898c-640d-3aad-bc63-b85a7cc5a26f | -9.0939 | -47.0983 | 2025-09-11 13:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 173.6 |
| 5ff443f0-57fa-3cea-a1f6-807d00c7572e | -11.4285 | -43.5544 | 2025-09-11 13:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 197.1 |
| 35a93e4d-30d3-3b31-9de8-7b7bb98d5149 | -11.1 | -48.4172 | 2025-09-11 13:30:00 | GOES-19 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 993ea1ad-87f2-3ae7-b789-a65d1e4dbc13 | -11.7316 | -50.6587 | 2025-09-11 13:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 652b3fda-dd96-31d7-91ff-979b48de9406 | -8.8758 | -49.5399 | 2025-09-11 13:30:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 73.0 |
| bdf836d8-a05b-31b9-956c-3cfad32765e1 | -9.0265 | -49.5046 | 2025-09-11 13:30:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 94.7 |
| 0c6111b6-8383-3834-a2e7-16475b519998 | -13.2407 | -51.7784 | 2025-09-11 13:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 89.6 |
| f926a69a-1b1b-3974-81c5-f46c64b1af74 | -9.9004 | -51.8811 | 2025-09-11 13:30:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 4b01b450-7706-3c2d-8ca5-80e500c22a20 | -11.4281 | -43.578 | 2025-09-11 13:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 126.7 |
| 425eea27-3208-308e-a6c2-8cd4b0326c01 | -9.9762 | -50.3121 | 2025-09-11 13:30:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 120.4 |
| 0ad34946-89d9-3ff1-a0ae-194609cc0def | -6.2226 | -43.3459 | 2025-09-11 13:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 102.7 |
| fc710638-446a-33ad-939b-856e98c61d40 | -6.4174 | -44.5092 | 2025-09-11 13:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 76.5 |
| f4f6ddf7-5d66-306b-baad-4a692ad35d0a | -10.7362 | -46.1238 | 2025-09-11 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 111c9ee7-592f-3b23-a75c-a329735c40dc | -9.0129 | -46.0788 | 2025-09-11 13:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 438d37d3-fb92-30c0-9f21-6497913fd2f5 | -6.8374 | -45.6108 | 2025-09-11 13:30:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 166.5 |
| 08aabf6d-92bb-3170-ae8a-fc1e0dc8ac77 | -22.6809 | -53.1309 | 2025-09-11 13:30:00 | GOES-19 | SÃO PEDRO DO PARANÁ | PARANÁ | Brasil | 4125902 | 41 | 33 | nan | nan | nan | Mata Atlântica | 95.0 |
| 3b3b621a-fceb-3550-a0ee-377e59f55fd7 | -9.4801 | -46.4545 | 2025-09-11 13:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 349.2 |
| 566a5861-9115-340e-ab87-074563b78179 | -11.7786 | -46.5047 | 2025-09-11 13:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 522.9 |
| 0dbbda3c-1bf3-3d95-812b-b7038997ae2d | -5.4719 | -43.4278 | 2025-09-11 13:30:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 69.1 |
| e94b7889-3d61-3915-81b5-69fc194907bb | -8.5667 | -45.5842 | 2025-09-11 13:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 219.0 |
| a4ac3dd2-d7e2-3e4d-888a-e245648921ea | -9.0547 | -45.7809 | 2025-09-11 13:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 52.9 |


[Clique aqui para ver as próximas entradas](README142.md)
