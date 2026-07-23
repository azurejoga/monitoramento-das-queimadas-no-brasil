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
| 485e2d0b-a88a-3dd9-97ef-28e7155232f2 | -5.7613 | -49.0895 | 2026-07-23 00:00:00 | GOES-19 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 84.5 |
| 86d6e75a-b431-39ad-a9ad-3ab1ee9bba87 | -18.7999 | -51.2638 | 2026-07-23 00:00:00 | GOES-19 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 69.4 |
| e2305103-bfc1-35f7-8cec-4ea2c2f90c8e | -11.9069 | -50.3815 | 2026-07-23 00:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 89.1 |
| 92b5f410-15fd-3a97-bc4e-4a11c69bfb41 | -11.807 | -47.0858 | 2026-07-23 00:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 87.0 |
| d78932af-28e1-3a58-b478-d8d4d2c7d0c4 | -11.7875 | -47.1108 | 2026-07-23 00:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 320.0 |
| 01510767-7b53-3f79-b190-ccc097be2929 | -11.9072 | -50.36 | 2026-07-23 00:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 9de5be17-99fc-3126-a403-3535043e01f1 | -18.7804 | -51.2453 | 2026-07-23 00:00:00 | GOES-19 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 79.2 |
| eeb72767-eb7c-32fa-ab61-995f5b8224d3 | -11.8879 | -50.3837 | 2026-07-23 00:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 85.7 |
| f6d9e7d9-14ac-39e9-9563-e12376f0e364 | -18.8004 | -51.2417 | 2026-07-23 00:00:00 | GOES-19 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 192.7 |
| 2b5dcbed-34d1-35a5-9518-cca1c86da0a5 | -11.8066 | -47.1082 | 2026-07-23 00:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 151.0 |
| 03a1d292-5612-3963-8eb9-af9bbdc5c335 | -11.7879 | -47.0884 | 2026-07-23 00:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 249.3 |
| bf67b3f9-a0dd-3447-a557-f159d3c6645b | -11.7687 | -47.0909 | 2026-07-23 00:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 1847d5ae-4872-3eff-bd6d-b4cc0e2b1eff | -11.7875 | -47.1108 | 2026-07-23 00:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 313.9 |
| a3f60d3a-c1b8-3aac-a589-9147533fd3eb | -11.807 | -47.0858 | 2026-07-23 00:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 81.2 |
| bfc867a6-a021-39ec-bda3-52eeead6ec7f | -11.698 | -50.3629 | 2026-07-23 00:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 5eae61ee-d7e6-376b-8377-019add0679f8 | -18.8004 | -51.2417 | 2026-07-23 00:10:00 | GOES-19 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 143.5 |
| efe25ede-2fa1-3733-a1cd-8e20cc779a52 | -11.7879 | -47.0884 | 2026-07-23 00:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 240.1 |
| 5bfcc1f3-e981-30ff-aee0-c8aaeeed4621 | -11.7683 | -47.1134 | 2026-07-23 00:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 84ec25ac-c064-3d4d-9fb1-82beb205f917 | -11.9072 | -50.36 | 2026-07-23 00:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 56.9 |
| cd428372-1f13-34d6-8914-d50261afc35b | -11.8882 | -50.3622 | 2026-07-23 00:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 52.3 |
| 2f0c4082-40cb-37d5-848a-fad8da399549 | -5.7613 | -49.0895 | 2026-07-23 00:10:00 | GOES-19 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 7ac1eea8-a7f0-372d-a6f6-dec591e1c36c | -11.6792 | -50.3437 | 2026-07-23 00:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 61c18334-ec57-3fb0-9025-c1efd519e5f6 | -11.6983 | -50.3415 | 2026-07-23 00:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 4e03c34d-f95b-3b1d-9920-82d3e933a760 | -11.8879 | -50.3837 | 2026-07-23 00:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 86.1 |
| b016d41e-b52e-3040-974a-fff8b7092042 | -11.9069 | -50.3815 | 2026-07-23 00:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 73.8 |
| b5be879c-d3fe-3fe0-ad63-ca245fc14e1a | -11.8066 | -47.1082 | 2026-07-23 00:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 137.7 |
| a9137cfe-6339-3be5-a7e9-e3716cf30b3b | -11.78 | -47.14 | 2026-07-23 00:15:00 | MSG-03 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 125a71ab-50cd-34e4-8144-e05634beb3c8 | -11.78 | -47.09 | 2026-07-23 00:15:00 | MSG-03 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 630f2621-79d5-3123-8e4c-f6b863d54d86 | -8.0534 | -48.4594 | 2026-07-23 00:17:00 | METOP-B | COLINAS DO TOCANTINS | TOCANTINS | Brasil | 1705508 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 88e11b6d-bb17-336a-a0d3-eb2e9883c20f | -11.6863 | -50.339401 | 2026-07-23 00:17:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 144453b7-8d00-3f5a-a82f-a2e9a21348c1 | -11.6084 | -50.313202 | 2026-07-23 00:17:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f0fc1d35-c8db-309b-875e-5c30885a9d23 | -11.7642 | -50.365799 | 2026-07-23 00:17:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c9fbdce4-15c1-303a-a4d0-88c1c196a53d | -11.8977 | -50.364799 | 2026-07-23 00:17:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1459629d-fa7e-38ac-b7ed-f800cc32e9bf | -12.5215 | -48.240898 | 2026-07-23 00:17:00 | METOP-B | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 502f20eb-4681-3be9-b19a-88e1b9734df2 | -12.6585 | -48.2085 | 2026-07-23 00:17:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bfb10cd2-297a-3fc8-8dcb-60e5317d57c9 | -11.6992 | -50.3512 | 2026-07-23 00:17:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8ab87b1a-ce29-35f1-a566-afcd4d6a52f6 | -11.7105 | -50.355999 | 2026-07-23 00:17:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2275636e-144f-351b-b859-7ca059315b24 | -11.662 | -50.323002 | 2026-07-23 00:17:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b99fc32d-f5e9-315b-8b22-cae6bc1303b8 | -12.4531 | -49.576698 | 2026-07-23 00:17:00 | METOP-B | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 76c84ed9-f703-3447-8c1e-5ac07f92422f | -11.6636 | -50.330002 | 2026-07-23 00:17:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c8dab211-0ec6-34d9-95c5-51c0f0c8dea7 | -5.3564 | -43.128799 | 2026-07-23 00:17:00 | METOP-B | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 085c03d6-484a-3a58-a538-75d1acbe01a7 | -11.7363 | -50.379501 | 2026-07-23 00:17:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 97282c1e-8167-32ed-8568-729c0db61dd0 | -11.8993 | -50.371799 | 2026-07-23 00:17:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1a71cf52-02af-32fc-bb2a-37bd0a940d28 | -20.112801 | -50.467201 | 2026-07-23 00:17:00 | METOP-B | TURMALINA | SÃO PAULO | Brasil | 3555307 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 3da0b8e6-fe63-3d54-b7a0-3fda1302a6a2 | -12.0266 | -50.342899 | 2026-07-23 00:17:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6cf9f8be-c217-3267-bd28-d9f9b5bb3539 | -7.8838 | -46.892601 | 2026-07-23 00:17:00 | METOP-B | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6363c651-4580-3680-a1e0-68071cb41513 | -21.0436 | -47.770699 | 2026-07-23 00:17:00 | METOP-B | JARDINÓPOLIS | SÃO PAULO | Brasil | 3525102 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 54304fd1-927b-3fdd-adaf-a170d47138a8 | -12.0282 | -50.349899 | 2026-07-23 00:17:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 767cc804-e1f9-3081-8bf7-78ecc982b175 | -20.5159 | -48.856701 | 2026-07-23 00:17:00 | METOP-B | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 13903123-1090-3907-888b-81d9f12b7dfe | -11.6961 | -50.3372 | 2026-07-23 00:17:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| eccc2f8f-077b-3103-af7b-340f110df0b0 | -11.906 | -50.355598 | 2026-07-23 00:17:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 643baefe-f4b7-38a0-baaa-717bfcf5818a | -12.0199 | -50.3591 | 2026-07-23 00:17:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 17fa469f-dfd3-3c12-b760-8aa3a79e3229 | -10.8038 | -50.444801 | 2026-07-23 00:17:00 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2979d04c-752b-3e06-89a6-4874015ee040 | -11.709 | -50.348999 | 2026-07-23 00:17:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2e0bb0b1-f47b-3473-aa9b-2f0b2f2bf422 | -11.7332 | -50.365501 | 2026-07-23 00:17:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4a2fb73a-b0d4-3807-bb4b-231a4bb2142b | -11.6182 | -50.311001 | 2026-07-23 00:17:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6a42643e-4ae1-3edd-ac78-ccd775feac74 | -10.8945 | -51.085499 | 2026-07-23 00:17:00 | METOP-B | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a96ae66e-dc6d-36c4-8939-bb4c890ff841 | -11.9158 | -50.353298 | 2026-07-23 00:17:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9dd2c272-8af8-328f-b4e2-a3ad2f21ebfa | -2.8541 | -54.479599 | 2026-07-23 00:17:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2ad08186-cb12-3126-ac14-d165f579b389 | -12.0184 | -50.3521 | 2026-07-23 00:17:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b2a52451-5a13-3e11-96df-1d3c791d8b46 | -11.7815 | -47.096298 | 2026-07-23 00:17:00 | METOP-B | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a40eb3af-512b-3959-a4da-8e06c05189c2 | -7.0084 | -45.419102 | 2026-07-23 00:17:00 | METOP-B | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bedd76a2-05c3-3c6b-b6b3-133ef670acbb | -12.8447 | -44.373299 | 2026-07-23 00:17:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 210267c0-5252-3813-a83f-c8248ba8c544 | -11.6264 | -50.3018 | 2026-07-23 00:17:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 33826cea-51b9-3f55-a37b-dde8622dada9 | -12.4156 | -50.3797 | 2026-07-23 00:17:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 13a88317-d650-3878-b037-8be91a229fee | -11.6295 | -50.315701 | 2026-07-23 00:17:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0a629bcb-9009-3435-b2b1-ca9791cf2825 | -11.841 | -50.341 | 2026-07-23 00:17:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| aa489260-5b6c-3278-a7f1-66b5ec78a39a | -11.7611 | -50.351799 | 2026-07-23 00:17:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 31524ade-b279-3ac2-9dc5-dc1e5a09bb33 | -11.9467 | -50.353699 | 2026-07-23 00:17:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b78f2d95-2a69-3602-830a-82972be13ab7 | -12.6683 | -48.2062 | 2026-07-23 00:17:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 870b1eba-855f-3565-a5f2-ac31824bd5e2 | -8.8097 | -49.372101 | 2026-07-23 00:17:00 | METOP-B | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b773e9da-94af-3c28-a34b-15c0ea59169a | -8.0517 | -48.451698 | 2026-07-23 00:17:00 | METOP-B | COLINAS DO TOCANTINS | TOCANTINS | Brasil | 1705508 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 54fbb685-6453-3e9a-ab74-724292202141 | -12.0117 | -50.368301 | 2026-07-23 00:17:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 371418e2-b8ff-3045-ae46-bf9f626ce395 | -11.7317 | -50.358501 | 2026-07-23 00:17:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f206f3a5-a3dc-3b46-be02-69b1a9cfb67b | -5.7618 | -49.075199 | 2026-07-23 00:17:00 | METOP-B | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f9f48593-348b-3e51-b368-ab6a36ab9130 | -19.707899 | -48.065601 | 2026-07-23 00:17:00 | METOP-B | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| f39979fa-3eac-3abf-9c0b-95b91ee78f9a | -21.065399 | -45.926601 | 2026-07-23 00:17:00 | METOP-B | CAMPO DO MEIO | MINAS GERAIS | Brasil | 3111309 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 9de395ea-9c98-3385-b772-53722a45a432 | -11.5766 | -48.394199 | 2026-07-23 00:17:00 | METOP-B | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 501c4054-1f93-3a48-910e-8b2e9db74ea4 | -8.8373 | -48.325699 | 2026-07-23 00:17:00 | METOP-B | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7eb1d8db-fead-3fad-a5bb-972b49a75058 | -11.7497 | -50.347099 | 2026-07-23 00:17:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d591a7f6-1bb0-3f5c-9d46-47270e4b3e2c | -4.833 | -44.066502 | 2026-07-23 00:17:00 | METOP-B | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 769d9d27-2058-3776-b93c-3b7e14593d91 | -12.0168 | -50.3451 | 2026-07-23 00:17:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 77695a10-499f-3a9b-afb2-e17248abc7a7 | -11.5668 | -48.3965 | 2026-07-23 00:17:00 | METOP-B | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a7239d02-1eac-33ba-b6af-15bfb2a17298 | -11.7853 | -50.368401 | 2026-07-23 00:17:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2f543685-2112-3b00-bcaa-70775fc7fb8d | -20.163601 | -43.901001 | 2026-07-23 00:17:00 | METOP-B | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 7c06085d-7a12-333b-83f3-64556c64568f | -11.7121 | -50.362999 | 2026-07-23 00:17:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a87cb631-e84c-3100-a44b-50bbe8b3df0d | -7.0067 | -45.844101 | 2026-07-23 00:17:00 | METOP-B | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3478985f-8590-3936-8925-de8c32a4ae63 | -11.5942 | -48.022202 | 2026-07-23 00:17:00 | METOP-B | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1e7514f4-0255-3f7a-8dcf-9c7d1df6ed66 | -11.9008 | -50.378799 | 2026-07-23 00:17:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 98886cbb-cc2f-354c-b4cf-b0ddef800dbf | -9.1109 | -49.653 | 2026-07-23 00:17:00 | METOP-B | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a65453e4-9e6d-38a6-a3e5-91b519f62e71 | -18.7943 | -51.226898 | 2026-07-23 00:17:00 | METOP-B | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 5995f102-bd1b-311a-9839-ede69d931961 | -11.7528 | -50.361099 | 2026-07-23 00:17:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 88327244-613b-3723-b0ac-12d64096e3e4 | -19.17 | -46.5812 | 2026-07-23 00:17:00 | METOP-B | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 6c4301f9-f2a3-3912-b7be-ad65a2fd919c | -7.8306 | -47.105202 | 2026-07-23 00:17:00 | METOP-B | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 64e1fdef-d55f-3dba-9b33-5d04de53987d | -6.2337 | -48.975201 | 2026-07-23 00:17:00 | METOP-B | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 308f0864-cb1b-364a-8b8b-757acd5c3615 | -11.6734 | -50.327801 | 2026-07-23 00:17:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b52b2c54-2a01-3379-9507-45a73e7b3392 | -11.774 | -50.363602 | 2026-07-23 00:17:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9d541bc4-a1b4-37dd-9dbb-37b61933de93 | -10.6328 | -47.481899 | 2026-07-23 00:17:00 | METOP-B | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 52c24d24-da74-3d03-92a3-54a40e702571 | -12.0251 | -50.335899 | 2026-07-23 00:17:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d4a9df3a-88ca-3dd8-9426-5b91afb760e3 | -11.9091 | -50.369598 | 2026-07-23 00:17:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README2.md)
