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

## Dados Diários - Página 146

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b3709496-4832-3a78-859f-6084ab6ad9ac | -15.6929 | -47.0354 | 2025-09-11 14:10:00 | GOES-19 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 100.2 |
| 0f7bd2cf-692e-321e-b1da-628906390127 | -11.0959 | -51.3443 | 2025-09-11 14:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 273.8 |
| 2f167f99-85cb-3b26-b3fb-321088f32b63 | -15.6732 | -47.0389 | 2025-09-11 14:10:00 | GOES-19 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 263.2 |
| bc314653-1553-3b5c-8690-3eed4274a4c5 | -13.2609 | -51.7122 | 2025-09-11 14:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 154.2 |
| 046158f0-b144-313f-bf64-110721ae6163 | -9.0793 | -49.7997 | 2025-09-11 14:10:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 91.3 |
| cfb504c3-584f-3257-aba1-64ed02792f58 | -13.2794 | -51.7524 | 2025-09-11 14:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 98.6 |
| 84569514-e460-35e9-a309-a892c5d25323 | -5.7337 | -45.605 | 2025-09-11 14:10:00 | GOES-19 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 2845482e-2997-347e-b7ec-cfd286c1264f | -7.8711 | -45.4955 | 2025-09-11 14:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 61b50580-49c9-3df3-adfd-26cf3378c492 | -7.8708 | -45.5181 | 2025-09-11 14:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 169.5 |
| 782837e1-42a7-3c2d-b076-ae344d4f3889 | -9.7634 | -47.8447 | 2025-09-11 14:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 206.2 |
| b0375d40-5b0c-3142-8a77-8da2d7159858 | -12.1658 | -48.4811 | 2025-09-11 14:10:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 89.7 |
| e70061f4-8eec-3ea3-9531-dae5b4a20718 | -9.7631 | -47.8667 | 2025-09-11 14:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 35a9179f-08c8-39e2-a275-118b1ee14e2e | -9.0942 | -47.076 | 2025-09-11 14:10:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 113.1 |
| 4efca26b-75ff-31bf-879d-14da157642ef | -11.391 | -43.5128 | 2025-09-11 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 157.7 |
| aeac6c2b-61ed-31c0-97f7-7ac48a62a22e | -6.6652 | -44.1205 | 2025-09-11 14:10:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 76e2f8c1-3847-3399-bd3f-b2d443b71cda | -13.49 | -51.7688 | 2025-09-11 14:10:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 163.5 |
| a80a61d3-a696-30d3-85b7-d246e5a4f9fb | -11.4097 | -43.5336 | 2025-09-11 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 153.4 |
| ad675a7a-3d3e-31ae-892d-45be33f40e5d | -10.8594 | -45.5622 | 2025-09-11 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 153.3 |
| 1cf3027b-bfa6-368f-bd7e-fbeee345552b | -9.0791 | -49.8211 | 2025-09-11 14:10:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 163.6 |
| dfa69e22-0634-3890-b534-f848ed5033c0 | -10.7362 | -46.1238 | 2025-09-11 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 91.9 |
| fd71fd2f-291e-35af-98a7-6e4760356081 | -6.1705 | -41.0658 | 2025-09-11 14:10:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 96.5 |
| 0cf34231-3e4c-3635-82d2-a680c934e5a2 | -13.2798 | -51.7312 | 2025-09-11 14:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 162.7 |
| 0051b397-de69-3874-919e-fccedd6e24bd | -14.4461 | -53.2755 | 2025-09-11 14:10:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 87.2 |
| a1561eaf-07c2-37c8-909b-fcae1f45487b | -10.203 | -46.213 | 2025-09-11 14:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 130.7 |
| 3c45b2d9-88cb-3fb4-814a-4fc4ca1856c7 | -5.7339 | -45.5825 | 2025-09-11 14:10:00 | GOES-19 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 55e69738-632b-30f6-b7eb-e62aa62d2bba | -19.9994 | -47.6271 | 2025-09-11 14:10:00 | GOES-19 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 176.6 |
| ece2041d-2b7b-34bb-8c70-0bbb5cf55ae9 | -16.6335 | -49.7683 | 2025-09-11 14:10:00 | GOES-19 | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 808fa95e-205a-346d-8506-6201a53eec5e | -15.8006 | -52.2687 | 2025-09-11 14:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 195.3 |
| 6b37c341-aff5-3322-9728-8472fe6816fe | -5.5389 | -44.3471 | 2025-09-11 14:10:00 | GOES-19 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 4ea4c87f-ae24-3cdd-b4d5-cd427552abb0 | -9.9398 | -46.064 | 2025-09-11 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 173.3 |
| e937911a-af05-3545-8af4-ac38de9840df | -6.4848 | -45.2781 | 2025-09-11 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 136.3 |
| d50a703d-7281-3225-a67b-0e273318adcf | -10.7557 | -46.0987 | 2025-09-11 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 213.9 |
| d20b92e4-c6b3-3ad1-a21d-e72bb70497bc | -9.057 | -47.0355 | 2025-09-11 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 86.9 |
| adfae5a2-619d-3b3a-b0d4-3c09e31fab84 | -8.1649 | -46.0983 | 2025-09-11 14:10:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 117.4 |
| 035e9e5e-d200-3fea-b346-06bc9fd90441 | -11.429 | -43.5307 | 2025-09-11 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 143.8 |
| 6411df1a-fdab-3c90-afa2-89079519ae24 | -4.5717 | -43.7428 | 2025-09-11 14:10:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 8d781e9c-fbc5-3d6e-8a96-9b1ec40a3562 | -10.6603 | -48.6436 | 2025-09-11 14:10:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 75.7 |
| d2d307d8-7b04-3897-97ab-9e0ec1198af3 | -14.4323 | -52.9408 | 2025-09-11 14:10:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 22e3b867-7d79-3c98-8ae0-9a6d9b8232b4 | -14.3127 | -45.0226 | 2025-09-11 14:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 101.6 |
| 79cde1dc-3a3b-3d86-80e9-b5a22cd8508d | -15.6536 | -47.0425 | 2025-09-11 14:10:00 | GOES-19 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 1775bf1a-26fe-3cf5-9725-8d59db556b8f | -15.1697 | -56.3576 | 2025-09-11 14:10:00 | GOES-19 | ACORIZAL | MATO GROSSO | Brasil | 5100102 | 51 | 33 | nan | nan | nan | Cerrado | 84.6 |
| b2a41a58-2fe6-380c-9748-32f3b05f456a | -12.9292 | -54.7538 | 2025-09-11 14:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 118.6 |
| 39138756-47ea-314a-817e-37e70d201f6b | -6.9319 | -45.5352 | 2025-09-11 14:20:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 75.8 |
| e882bfea-2cde-3295-8493-bd5e2d4d1fa3 | -8.9752 | -46.0829 | 2025-09-11 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 187.9 |
| cbc6f348-074f-3c10-9c5e-de60d93a87f2 | -9.9026 | -50.17 | 2025-09-11 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 124.8 |
| 89a87482-47e3-332d-a623-cb90826ee252 | -14.2881 | -54.7514 | 2025-09-11 14:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 101.2 |
| 3b490a0b-89ec-31ef-bd39-130530cd9895 | -9.0129 | -46.0788 | 2025-09-11 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 137.3 |
| 11807ecc-756e-365f-9599-4a0bb3af0951 | -10.5482 | -49.8899 | 2025-09-11 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 132.4 |
| 9433e8b1-3593-32ab-8f71-48270e0503f7 | -7.4161 | -45.8536 | 2025-09-11 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 138.1 |
| 5018a754-9d4f-3bb6-89ab-8addb79d5736 | -9.7445 | -47.8468 | 2025-09-11 14:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 124.9 |
| 61daca2a-9962-3c41-82cc-380d8564cbd8 | -17.3372 | -46.6718 | 2025-09-11 14:20:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 135.4 |
| 1610ec0b-dfa7-3395-93bc-19bb202dac09 | -16.6335 | -49.7683 | 2025-09-11 14:20:00 | GOES-19 | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 92.7 |
| 48701d83-f45f-32f6-9691-5306dc64ddfa | -9.0127 | -46.1014 | 2025-09-11 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 120.9 |
| e4869fe8-4e93-37e3-a1f3-b87e9505d98f | -8.8755 | -49.5613 | 2025-09-11 14:20:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 141.3 |
| 3c07222a-3ef0-32b6-a005-b9f5d12b18b6 | -15.6732 | -47.0389 | 2025-09-11 14:20:00 | GOES-19 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 178.0 |
| b78fb905-72e2-3b9d-ae4c-c8220332ef5b | -12.1335 | -44.8508 | 2025-09-11 14:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 97.6 |
| 3aedb2fd-9654-30e3-a709-547372fc7bbc | -5.9193 | -45.7492 | 2025-09-11 14:20:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 60.5 |
| a93be1d8-a0c4-3f26-a0b9-d2c972892379 | -14.3074 | -54.7492 | 2025-09-11 14:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 138.6 |
| 59c12902-e56c-3732-a5ff-109e3def04cc | -15.1211 | -50.1438 | 2025-09-11 14:20:00 | GOES-19 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 84.2 |
| cb0c6f9a-fd7c-3642-8ab3-49f5d77ac375 | -6.3158 | -43.4081 | 2025-09-11 14:20:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 74.5 |
| c5bd1cfa-4fc1-3a0e-97ed-5ef4428211a7 | -15.801 | -52.2472 | 2025-09-11 14:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 103.9 |
| eecc3a68-da34-38c5-89b8-b36dff656e4b | -13.49 | -51.7688 | 2025-09-11 14:20:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 120.2 |
| 4edc7346-e5cf-3cc1-8a19-2af8f5cca723 | -6.4836 | -41.7373 | 2025-09-11 14:20:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 100.2 |
| 1b757089-c157-3210-b160-2955aa22cafe | -11.077 | -51.3462 | 2025-09-11 14:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 128.3 |
| e6b17343-09f4-3178-8de6-850a57d55a53 | -9.7634 | -47.8447 | 2025-09-11 14:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 208.9 |
| 667bee46-2e53-3c01-9916-57e196815a01 | -6.8374 | -45.6108 | 2025-09-11 14:20:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 69.0 |
| a22c5974-2245-334a-b0b0-f08ce4b2ec75 | -4.5717 | -43.7428 | 2025-09-11 14:20:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 74.0 |
| f71abe67-4d1e-3126-a37f-3a3bdc841de4 | -11.7115 | -48.2536 | 2025-09-11 14:20:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 151.5 |
| 529a3141-3ea5-38d4-8339-1bc0b7df3eec | -9.0567 | -47.0577 | 2025-09-11 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 94.6 |
| 63b7a4cf-1e44-3db7-9b51-8114b850e6ca | -9.9004 | -51.8811 | 2025-09-11 14:20:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 7581da25-e2e3-3005-87ff-d871529df732 | -9.0753 | -47.078 | 2025-09-11 14:20:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 171.2 |
| b1e119bc-9b70-36d5-9b7b-7588e7d6b65c | -15.1367 | -52.4466 | 2025-09-11 14:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 148.4 |
| b83eb2fc-0ab6-3fc1-9570-9ec049f7cc46 | -12.1658 | -48.4811 | 2025-09-11 14:20:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 127.4 |
| c1b2d670-4d52-3ff8-9710-f4a3304dc271 | -10.8594 | -45.5622 | 2025-09-11 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 147.4 |
| 139bfc96-8bf5-3d61-8ee3-8e56f680e377 | -9.9059 | -49.9132 | 2025-09-11 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 4a2fb5da-a425-3148-90f7-b3c9150db6ef | -8.1101 | -49.2634 | 2025-09-11 14:20:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 92.3 |
| 8deb9bf6-04be-3a00-81a4-037e80a1af86 | -14.7527 | -60.2321 | 2025-09-11 14:20:00 | GOES-19 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 35847dcd-4d94-36df-906a-3365d7a2a4bc | -14.7524 | -60.2519 | 2025-09-11 14:20:00 | GOES-19 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 7abdaa5e-bdb0-34e2-9799-5b9a649aba9f | -5.7339 | -45.5825 | 2025-09-11 14:20:00 | GOES-19 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 2328861d-5d31-3037-90c2-9d73722a670a | -6.5038 | -45.2539 | 2025-09-11 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 106.3 |
| 71ff18c6-6c1e-346b-96bf-c89f3d06a16e | -11.1689 | -45.2914 | 2025-09-11 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 92.6 |
| d27a3cd2-3ef3-38ad-81d1-613bf8d6c872 | -11.0962 | -51.3231 | 2025-09-11 14:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 122.6 |
| 92e20211-f091-3841-a6d0-cd9dd59899ca | -8.1103 | -49.2419 | 2025-09-11 14:20:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 106.0 |
| f9339f2e-bb2a-33fd-a241-246f2827af7c | -13.2798 | -51.7312 | 2025-09-11 14:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 113.5 |
| 3ab470b0-8d04-3430-81f1-59f8ad461152 | -10.6793 | -48.6415 | 2025-09-11 14:20:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 81.6 |
| afc89df5-cffb-38b7-924d-7b1609db95a7 | -15.5628 | -54.7453 | 2025-09-11 14:20:00 | GOES-19 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 89.7 |
| b11e4e74-fadc-3e7e-99cc-4bee342dc540 | -9.1514 | -47.0257 | 2025-09-11 14:20:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 07b497a2-0579-36a1-a1b1-6c15edd4c9ba | -14.5612 | -52.1623 | 2025-09-11 14:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 97.2 |
| 32494dcf-d84e-31f5-a8e7-92f7f3071199 | -19.2016 | -47.9889 | 2025-09-11 14:20:00 | GOES-19 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 151.7 |
| f9e598f6-9842-3ff7-a788-b29ae58959f7 | -11.1 | -48.4172 | 2025-09-11 14:20:00 | GOES-19 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 156.0 |
| bb275fc5-0023-318c-98aa-971fdc28bd81 | -7.8708 | -45.5181 | 2025-09-11 14:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 104.9 |
| 5c0d8ff5-4e06-36b6-8d0d-58caf516e166 | -10.6603 | -48.6436 | 2025-09-11 14:20:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 2588c35c-f7cd-34ea-b46f-95d0cae772da | -14.381 | -47.3302 | 2025-09-11 14:20:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 89.8 |
| a9e44628-450a-3c61-b975-6e469c0d2ea7 | -10.6413 | -48.6458 | 2025-09-11 14:20:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 103.6 |
| 441ca253-cdfb-3219-8861-010779ed4da4 | -11.0997 | -48.4392 | 2025-09-11 14:20:00 | GOES-19 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 147.2 |
| c29fbdd4-0cf8-3051-b544-7330b7c70892 | -8.1651 | -46.0758 | 2025-09-11 14:20:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 108.7 |
| 7d94cd12-741d-339a-ba62-704c399639b3 | -6.3226 | -53.4553 | 2025-09-11 14:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 93.0 |
| c05903aa-9dc3-3f7a-b7e2-9f31c6311e66 | -7.4159 | -45.8761 | 2025-09-11 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 148.3 |
| ace48b63-1701-3f3a-91f5-1acec39920a9 | -9.4617 | -46.4117 | 2025-09-11 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 103.5 |
| 7152d68c-645b-34ad-928b-ac09e989143a | -15.6929 | -47.0354 | 2025-09-11 14:20:00 | GOES-19 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 108.6 |


[Clique aqui para ver as próximas entradas](README147.md)
