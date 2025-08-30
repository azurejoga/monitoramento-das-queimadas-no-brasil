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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 55709253-0ca5-3d9d-afbe-c7b2b18db971 | -9.69311 | -47.06213 | 2025-08-30 03:30:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b815dd97-23c5-371e-8fd1-2d8d28e4ee1c | -7.59538 | -42.69436 | 2025-08-30 03:30:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 2c35e173-1050-3026-a43b-b2fe538b5fa2 | -11.9183 | -44.86412 | 2025-08-30 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 109f7f2a-2878-3628-a8d0-4e8bca8a95fb | -7.60102 | -42.72831 | 2025-08-30 03:30:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f8afd69b-e614-349f-afca-cb476cf2dd3c | -11.5647 | -46.35191 | 2025-08-30 03:30:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2a3f12d7-2e2e-3361-bd7d-6d89c0e18a1d | -8.44843 | -43.64824 | 2025-08-30 03:30:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 26b883d2-5c82-39d6-a3d3-2269aba0c607 | -11.84295 | -46.4498 | 2025-08-30 03:30:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 42d962eb-d29c-3044-9c1b-a3adc7779c77 | -11.35545 | -43.55861 | 2025-08-30 03:30:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 57069896-1643-33b5-9d47-3e517c36fbb3 | -13.31499 | -43.01691 | 2025-08-30 03:30:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 92a9f03e-d1e8-3e25-889e-95706a1a7f54 | -11.31409 | -43.46864 | 2025-08-30 03:30:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bc54c1f8-41f9-3787-a229-cc43295ddcba | -7.58742 | -42.70534 | 2025-08-30 03:30:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 6ebca49e-95ed-384c-928c-52aed6ca518a | -11.30743 | -43.62324 | 2025-08-30 03:30:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cbb9e371-b93b-3aad-a380-3da4962c2eee | -11.86785 | -46.43053 | 2025-08-30 03:30:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 84a9c206-dd50-3ab4-b8e0-ff19b3ce16bd | -11.57253 | -46.34785 | 2025-08-30 03:30:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f9acc0ca-ca2d-38ea-80f7-f01a5750bba4 | -11.07757 | -45.13043 | 2025-08-30 03:30:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6cc8a4ed-c739-336c-bcfa-d4a1964be0ed | -11.30266 | -43.64766 | 2025-08-30 03:30:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ea2abb3e-532d-38dc-b5ce-55cd9c4dbdeb | -7.11914 | -44.60592 | 2025-08-30 03:30:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| d1dde28e-cffc-3493-a666-a6f30c6b37ea | -11.87244 | -46.38875 | 2025-08-30 03:30:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 616d9648-e417-3d59-8646-507f79276260 | -11.29693 | -43.64661 | 2025-08-30 03:30:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dc69032b-083f-3779-8161-6517a33d32a1 | -7.16843 | -44.87585 | 2025-08-30 03:30:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9137e909-90c5-3418-8d06-09b661ad8066 | -11.33579 | -43.59923 | 2025-08-30 03:30:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bded6de1-fdd4-3876-a76e-6778567cc063 | -11.29175 | -43.58234 | 2025-08-30 03:30:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| eee8ad1b-2272-39bb-bd5f-a36e7c02d36d | -7.60531 | -42.7374 | 2025-08-30 03:30:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 08c3f5e5-cf1b-35c3-8e78-8ef7bd66b341 | -11.30819 | -43.61937 | 2025-08-30 03:30:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9b1246c7-60f8-376b-b975-9777fab2723c | -11.82833 | -46.45293 | 2025-08-30 03:30:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 7e032a65-deae-33e9-80d0-7daa276b16c4 | -9.10776 | -46.05466 | 2025-08-30 03:30:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2987d130-b180-3608-bbcc-d2f251754ada | -7.39621 | -45.92598 | 2025-08-30 03:30:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| ac26804b-e2de-3e21-a831-d39966323dc5 | -11.30691 | -43.47527 | 2025-08-30 03:30:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1d9e8afc-f6ef-37bb-8e05-bd3d28672adb | -11.84076 | -46.39291 | 2025-08-30 03:30:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| b3fb10bc-0ae3-371e-9fb8-6d8c6ce677d5 | -9.21471 | -46.75368 | 2025-08-30 03:30:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| dbb48c43-ec6a-3c73-9005-e18b92992738 | -11.85095 | -46.44485 | 2025-08-30 03:30:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bbc802e0-4ee4-3764-a3be-d0650bcd6771 | -8.10306 | -45.0014 | 2025-08-30 03:30:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4521b20c-eca3-3a83-8643-4f17495d033f | -11.88194 | -46.39575 | 2025-08-30 03:30:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d5eaed9f-3f56-3fc4-8b52-1271c0b11c20 | -7.62419 | -42.66643 | 2025-08-30 03:30:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 20df2744-7354-308f-9ee7-a94958a2a6e7 | -11.85237 | -46.43798 | 2025-08-30 03:30:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d2ddc326-65b1-3753-a124-290a8baf2b43 | -10.99468 | -46.95833 | 2025-08-30 03:30:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1f5c3d43-1806-3bd6-9ec7-71fcd6ad31af | -7.59097 | -42.71832 | 2025-08-30 03:30:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| a71c717a-ae7f-3f91-b1b8-0a8d1b9fed6f | -11.31574 | -43.64147 | 2025-08-30 03:30:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a242f9af-9011-30ec-804d-4b1dcfc7f6a8 | -8.44457 | -43.6461 | 2025-08-30 03:30:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f8130404-2f0d-3b64-a66f-2143ecae28a1 | -8.10854 | -45.00839 | 2025-08-30 03:30:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 930b9055-445e-3b17-bf0b-a1af44db35f0 | -10.0263 | -46.0356 | 2025-08-30 03:30:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| f1fe6e4a-f0fa-3463-af6f-74d0ee8cc8f5 | -9.31269 | -40.21722 | 2025-08-30 03:30:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 1a283561-1443-3dde-96b3-7cf9f4532ca0 | -11.31001 | -43.64045 | 2025-08-30 03:30:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e0df7ce9-8274-3c5b-944a-5c1bf22f558b | -11.86296 | -46.38648 | 2025-08-30 03:30:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 496cf5e0-6cc0-3ceb-9452-e014ee9eb05a | -12.00891 | -43.99201 | 2025-08-30 03:30:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 8cdf4d37-16b2-3bb5-86c6-4c57406f056f | -7.59823 | -42.71116 | 2025-08-30 03:30:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| f049dfb1-b078-389f-bc4e-6d40e31e3c43 | -7.60605 | -42.73335 | 2025-08-30 03:30:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 6542073a-8d14-3683-ba1d-cf6af2cf2ece | -7.60324 | -42.71619 | 2025-08-30 03:30:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| dd82733d-cd73-394e-abc4-d294c9067d86 | -11.8363 | -46.44818 | 2025-08-30 03:30:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 15.8 |
| def11356-e194-34fe-8c57-c5b20e7ea0ab | -11.77828 | -47.55843 | 2025-08-30 03:30:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cd05786c-cc5e-3eaa-92be-5b0d34a1cb8f | -11.32928 | -43.60227 | 2025-08-30 03:30:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b128ec99-24aa-348d-b700-322c192e3ee6 | -7.63062 | -42.66359 | 2025-08-30 03:30:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| ea54c90e-7440-3242-9dee-6831fa3b864c | -11.3059 | -43.63111 | 2025-08-30 03:30:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 670ace9e-1c61-3dee-b3c9-7012048b1454 | -11.87738 | -46.45215 | 2025-08-30 03:30:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 8e4ff578-5aec-3550-b050-687ae74d28e2 | -7.59451 | -42.73144 | 2025-08-30 03:30:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 3313f525-1e07-38ab-8ca4-1fe682bc4e10 | -11.31493 | -43.64565 | 2025-08-30 03:30:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 78324765-748d-3cd5-8dbc-ca86e2bf82f1 | -7.16338 | -44.16214 | 2025-08-30 03:30:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| bd7de6ac-07f6-3306-b91c-8308d9b39125 | -9.6946 | -47.05498 | 2025-08-30 03:30:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a8ef3cb5-84b8-34f2-901c-d815a32e5c97 | -11.91924 | -44.85945 | 2025-08-30 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4b7be936-9d92-3ea5-bc34-f6710e01c7af | -7.95222 | -46.38511 | 2025-08-30 03:30:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9c42472f-9e0a-34ef-993e-2e1238b1033a | -11.31338 | -43.65363 | 2025-08-30 03:30:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b8b3e506-773d-366a-8bed-08aab74a2112 | -11.85372 | -46.39759 | 2025-08-30 03:30:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 1ad437da-8735-388f-849f-e8d7fe2571ae | -11.08389 | -45.13152 | 2025-08-30 03:30:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b7cf08c3-8049-307f-a4eb-7d993df61593 | -11.30096 | -43.626 | 2025-08-30 03:30:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7155866f-4039-332b-bb92-655d9c878ce1 | -7.41127 | -42.05701 | 2025-08-30 03:30:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b4fa340d-1f22-3259-a530-ca032be726f2 | -11.35661 | -43.5832 | 2025-08-30 03:30:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2a8f320e-47df-302f-bc94-f0786443bf83 | -11.2199 | -45.0246 | 2025-08-30 03:30:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 32eb607c-d011-32f3-bf12-eb7d38c80d1e | -11.22071 | -45.03273 | 2025-08-30 03:30:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b2160845-6d28-3815-9390-2c79da561234 | -11.569 | -46.35078 | 2025-08-30 03:30:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 13642c0f-3606-380f-bd0a-59d2ce70d3ef | -11.34376 | -43.52754 | 2025-08-30 03:30:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 620d180c-42eb-3fde-9f14-045a667061c9 | -7.39407 | -45.92747 | 2025-08-30 03:30:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 539154b5-9be3-3770-9d02-a1286786db35 | -7.59246 | -42.71022 | 2025-08-30 03:30:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| ce3091f6-89e0-3f40-9738-27c98459199f | -11.34301 | -43.59247 | 2025-08-30 03:30:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| efcc087e-df6a-3b37-9e52-63da3401f278 | -11.82708 | -46.45898 | 2025-08-30 03:30:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 20.2 |
| e82863bd-6895-3d09-b5c2-d8693f1dfedb | -7.59675 | -42.71923 | 2025-08-30 03:30:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 632d88c6-67e5-36c8-88fe-a40902308a9e | -11.33809 | -43.52645 | 2025-08-30 03:30:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 152d5e85-96d0-39ec-96ef-0ab56e5c8031 | -11.3047 | -43.57662 | 2025-08-30 03:30:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1b0d77f8-6035-3652-b818-72c007d8f9c2 | -11.32036 | -43.61773 | 2025-08-30 03:30:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 30b4a59a-fc2e-3275-b944-894caa54665b | -11.29903 | -43.57543 | 2025-08-30 03:30:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7c5e9206-5c0d-3b1f-8890-e67ef3802e66 | -12.32162 | -42.85775 | 2025-08-30 03:30:00 | NOAA-20 | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 16c72528-9723-3c72-9559-a9814c23a286 | -7.08788 | -44.30888 | 2025-08-30 03:30:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 8749cdd4-919e-335b-bdcb-609984018e44 | -11.14679 | -47.15181 | 2025-08-30 03:30:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0b300b02-4d9f-3923-bf21-88450a83f339 | -11.31237 | -43.62831 | 2025-08-30 03:30:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3d143f8a-9b65-3364-b73a-0899d3842191 | -7.61827 | -42.7315 | 2025-08-30 03:30:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| bddcb858-f483-31d3-a9ee-33e7a7670445 | -11.87544 | -46.39352 | 2025-08-30 03:30:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| eb7d5f5d-7cbf-3664-a7d8-458c06f0e27c | -11.29937 | -43.63416 | 2025-08-30 03:30:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f0307402-469d-395e-b728-3e923f740727 | -7.206 | -43.70735 | 2025-08-30 03:30:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| dbf88ebf-21c0-3b6f-8636-97a2e4aea41a | -9.50046 | -45.39331 | 2025-08-30 03:30:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 93e51837-5833-3021-85b0-9aea0a6e13a4 | -7.16951 | -44.87014 | 2025-08-30 03:30:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ee9377f1-74ad-31d1-ad0d-6ad3e2da79e3 | -11.92171 | -46.69647 | 2025-08-30 03:30:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| eadc547d-45e5-31fc-83a6-f5d489e74387 | -7.5889 | -42.69733 | 2025-08-30 03:30:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 840d8ac0-84cb-3fae-ac96-5e21f91e6b61 | -11.31178 | -43.66183 | 2025-08-30 03:30:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| dbbf70d4-e84f-3aaa-96a1-74daa4c7dc70 | -7.09227 | -44.32084 | 2025-08-30 03:30:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 17.4 |
| b025733a-e344-3266-8d38-4897ad833811 | -11.32147 | -43.64252 | 2025-08-30 03:30:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4ebfa880-f0b2-3b49-a73f-03959434ef00 | -11.21881 | -45.02996 | 2025-08-30 03:30:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5bcf4929-8ae2-3a57-a9da-a2b8adaa1bde | -7.64273 | -42.66203 | 2025-08-30 03:30:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 9cebd367-21ff-3ca1-86d7-8795b5aaafb6 | -11.34306 | -43.29111 | 2025-08-30 03:30:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f0e69a13-2d8e-3fc9-b7f4-972370008380 | -11.29773 | -43.64251 | 2025-08-30 03:30:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2c8760a1-424b-395e-8303-a139cf45c2f8 | -11.33449 | -43.28595 | 2025-08-30 03:30:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d0796b00-7f95-3b54-81ab-d1d70337bac1 | -11.40887 | -44.68451 | 2025-08-30 03:30:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |


[Clique aqui para ver as próximas entradas](README13.md)
