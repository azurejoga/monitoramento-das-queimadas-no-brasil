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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3585928b-dfbd-37dc-9e61-429faaf7f158 | -11.5455 | -47.86686 | 2025-07-04 04:17:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f586d22b-2428-3826-9c28-d24b11835694 | -6.88885 | -43.22068 | 2025-07-04 04:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| c600f2d0-1e57-3146-8a4c-b68f7f38894a | -7.94244 | -43.34119 | 2025-07-04 04:17:00 | NPP-375D | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 726d74c4-a934-3f35-b656-5bd38c3fe792 | -6.73529 | -43.13954 | 2025-07-04 04:17:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4efef767-f254-3d8e-a74a-d716ddf6d9bd | -7.22955 | -43.09692 | 2025-07-04 04:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 8429a957-4a3d-3b82-a486-0602850678bf | -9.58969 | -46.75988 | 2025-07-04 04:17:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d473909d-8e70-34be-a755-8576f2174ce5 | -11.54506 | -47.31252 | 2025-07-04 04:17:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 15307794-1333-384b-b46a-39c9229f986d | -7.07845 | -43.21907 | 2025-07-04 04:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 67a38d34-4e47-3304-8800-7ca7f5aabf80 | -9.84543 | -46.47704 | 2025-07-04 04:17:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0c328bdf-1c6e-3cb3-b44f-022d3899d247 | -7.17935 | -44.01294 | 2025-07-04 04:17:00 | NPP-375D | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 98580d53-886e-363e-b926-310dbbc8342a | -11.45033 | -45.11565 | 2025-07-04 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 8293c04c-c82c-30b8-8ed8-eebacdd74f83 | -7.22346 | -43.0924 | 2025-07-04 04:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| bd87cef3-eeb3-35ec-8f25-6f3cfff1bf98 | -9.08809 | -48.33231 | 2025-07-04 04:17:00 | NPP-375D | TUPIRAMA | TOCANTINS | Brasil | 1721257 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ba9b1314-7e3f-307f-ac01-6340422bad22 | -7.19413 | -43.42939 | 2025-07-04 04:17:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 4c908634-4c7f-36df-b235-e2fa8cda54f6 | -10.6495 | -44.49148 | 2025-07-04 04:17:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9881d458-7d25-30d9-b3a1-040e183f8adb | -9.51156 | -45.43777 | 2025-07-04 04:17:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 059ddea6-db80-3846-804f-23ac9222fe08 | -18.0431 | -46.04922 | 2025-07-04 04:17:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e0deddeb-1632-3bf3-a463-ed1b01162cda | -10.5922 | -49.46149 | 2025-07-04 04:17:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 9f51d6fe-b718-3a5f-93dd-35bfe3c5dde0 | -9.90804 | -55.52581 | 2025-07-04 04:17:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e4a51d9b-018a-3d02-a0b4-0d8530ca5a20 | -7.87378 | -47.13282 | 2025-07-04 04:17:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 017c12d2-2a62-3875-b79d-5ba84a5854c1 | -6.91296 | -44.00318 | 2025-07-04 04:17:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b64ee817-eae2-339d-967f-660761be979a | -9.85598 | -46.47882 | 2025-07-04 04:17:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d79a0e14-309f-3a5c-9fc2-bf3ad1e91d08 | -9.74601 | -48.35289 | 2025-07-04 04:17:00 | NPP-375D | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 23dd031a-d072-35e6-9c72-bdbc4b88d5d9 | -11.93152 | -45.38569 | 2025-07-04 04:17:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 006bf28a-8923-3cd6-bc4a-932b97e8d113 | -7.65401 | -44.34495 | 2025-07-04 04:17:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f0a58178-0914-3481-878d-5263779ed7d6 | -10.59285 | -49.45778 | 2025-07-04 04:17:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 552ae8d7-b2e4-3973-a39a-fa28e46b0b52 | -11.91973 | -45.39479 | 2025-07-04 04:17:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 7dff249b-d373-3954-adc9-3fc0e6ea903c | -7.23065 | -43.08997 | 2025-07-04 04:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 75f2bc8f-0eb9-33c9-80a3-0d7ef1ed040f | -7.96615 | -45.93697 | 2025-07-04 04:17:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ca7c499e-76d9-3709-b7c4-1df192ffcd35 | -11.92134 | -45.40612 | 2025-07-04 04:17:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fe819cd0-d5c1-3526-99f8-cd573ee0556d | -15.08067 | -48.94548 | 2025-07-04 04:17:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1f64a46b-b04f-3a5f-8ebf-66f930edd31b | -6.00957 | -44.53174 | 2025-07-04 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fb0773a3-722f-3449-a748-b2b741cef128 | -9.8034 | -48.25223 | 2025-07-04 04:17:00 | NPP-375D | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 000f7e69-8a2c-37c8-9278-7d6001387214 | -11.92483 | -45.38457 | 2025-07-04 04:17:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d1217122-6e21-3ee9-9853-f366adf59cca | -16.68269 | -43.88412 | 2025-07-04 04:17:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9fe20d7a-f009-3983-94de-9124ebae7adc | -7.09877 | -49.17263 | 2025-07-04 04:17:00 | NPP-375D | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 7.5 |
| d8e5b511-b594-35af-94a3-ba29c98baac6 | -11.01589 | -56.25977 | 2025-07-04 04:17:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b9922656-0857-3b1d-972d-1eb91c024ad3 | -17.50617 | -49.43779 | 2025-07-04 04:17:00 | NPP-375D | PONTALINA | GOIÁS | Brasil | 5217708 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 691fa8d1-4106-37d4-92ec-2d59b862f671 | -11.85591 | -44.86939 | 2025-07-04 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fc1c73c2-21db-3658-acce-1a63167be5cc | -7.94693 | -44.84669 | 2025-07-04 04:17:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 872b4c0e-9751-33e9-9fcc-79eb0f1e283d | -11.91754 | -45.38708 | 2025-07-04 04:17:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3a1102ab-8de0-30fa-8cf3-d4887f2632a3 | -8.53326 | -54.77353 | 2025-07-04 04:17:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 076a7ffe-29b8-31c4-8ff1-0bcb0ff3bf4e | -5.28547 | -45.17002 | 2025-07-04 04:17:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9508eb4f-d539-34fa-910d-339aa83ee7c5 | -9.18335 | -48.84885 | 2025-07-04 04:17:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b3d92bc7-cb65-3a3d-9c9a-ff3cd004a44c | -7.95031 | -44.84726 | 2025-07-04 04:17:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 82c8b23c-c64c-39b7-afce-926c177bc4f9 | -11.49408 | -48.07924 | 2025-07-04 04:17:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a17eebea-8d93-3d32-ad04-1c9933d5388f | -6.60031 | -43.05381 | 2025-07-04 04:17:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 51ad036e-47d7-3925-b850-e034eea4dc50 | -10.23158 | -56.76713 | 2025-07-04 04:17:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9dc3ff3c-a684-3dab-8fab-8f45af8ea083 | -10.24752 | -47.67302 | 2025-07-04 04:17:00 | NPP-375D | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 03d01455-12bf-3035-adf0-af52ef701ed2 | -10.65117 | -44.48095 | 2025-07-04 04:17:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 678f3af4-8665-32d4-b668-220e730b143e | -7.35915 | -44.831 | 2025-07-04 04:17:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c8d393f3-4556-3b80-a505-6cf8e1fa7475 | -7.09807 | -49.17672 | 2025-07-04 04:17:00 | NPP-375D | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 4e2153bc-1922-3c04-bf1e-e27a0ebef567 | -8.2406 | -43.74556 | 2025-07-04 04:17:00 | NPP-375D | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b3bbd56c-2023-30a0-942b-490880b9927e | -11.93095 | -45.38927 | 2025-07-04 04:17:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 146b1aed-8c9b-3331-b781-80453b8a13fe | -7.90216 | -44.53439 | 2025-07-04 04:17:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a41d1bbf-4287-3b41-8123-cc2e301bfad5 | -10.64397 | -44.48338 | 2025-07-04 04:17:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7dec1802-cf14-3adf-be2d-8c1797faa4fd | -11.92862 | -45.40363 | 2025-07-04 04:17:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6422b257-20b5-3211-86dd-78888682d4dc | -7.02838 | -44.043 | 2025-07-04 04:17:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1d414d0e-0f7c-3b80-9dfb-b7d7f7f7603f | -15.98717 | -43.61757 | 2025-07-04 04:17:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 170d7ee0-88ea-33b1-85b4-b81cf853c7ee | -6.88994 | -43.21374 | 2025-07-04 04:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ecd9cea0-2f9e-36cc-a362-d87e6c28e788 | -10.98375 | -45.10904 | 2025-07-04 04:17:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 573a82fe-6c61-3ce5-81b7-4d2269ed496c | -6.38921 | -45.31375 | 2025-07-04 04:17:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d087051c-bb24-37ad-b420-e3eb470e8a8c | -7.2301 | -43.09344 | 2025-07-04 04:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 4106ff1d-a269-3815-b84b-8b6d4787494e | -6.75536 | -44.63057 | 2025-07-04 04:17:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 23cbe7be-2839-3d60-b326-cea76ba598ca | -11.86644 | -44.85999 | 2025-07-04 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e0d0932c-5576-3336-9c22-374a86db7bd7 | -11.84155 | -43.7964 | 2025-07-04 04:17:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| e29a982d-beac-3fd8-8f4b-32b3c11268f4 | -12.42846 | -43.72213 | 2025-07-04 04:17:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| e8865118-e54c-3de5-8396-4c675c8903a6 | -10.98433 | -45.10546 | 2025-07-04 04:17:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 38c15d74-4bce-3233-b0f5-70aae6d57e4c | -11.77349 | -47.39729 | 2025-07-04 04:17:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ae16731e-a31c-38e1-bcaf-c6ea520ce1da | -6.7431 | -43.17632 | 2025-07-04 04:17:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 48eac935-95ce-3ae1-aa9c-4bb17b31b287 | -10.64729 | -44.48392 | 2025-07-04 04:17:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 34c660b3-8630-3fa6-8fc7-681aa3402de8 | -11.91857 | -45.40199 | 2025-07-04 04:17:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2cac49c1-a7c6-3afc-a3e2-89b0002aee9a | -6.75594 | -44.62694 | 2025-07-04 04:17:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 58c16a20-1b9f-33f3-a2d2-3631bd4cdcab | -6.58312 | -43.03333 | 2025-07-04 04:17:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 080acb62-f709-3c38-829b-cd47dc723a46 | -6.88553 | -43.22015 | 2025-07-04 04:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| ba6d2bc3-db36-3fdc-9305-cd240d6d433d | -7.00142 | -45.61016 | 2025-07-04 04:17:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 70372a22-19c8-3cd8-8467-407c2c66562b | -6.72225 | -44.3347 | 2025-07-04 04:17:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e889ca79-7bc2-30c8-aeb9-477fdf19d44e | -9.18273 | -48.85245 | 2025-07-04 04:17:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4afff173-593d-31b2-88ad-fe386ac6d97d | -11.46482 | -47.30042 | 2025-07-04 04:17:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f2223256-bfdb-3522-a61e-5d5d4376df8a | -6.66365 | -43.16743 | 2025-07-04 04:17:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 91ecd173-bc7b-3618-a4d6-e1ad031de213 | -7.07954 | -43.21212 | 2025-07-04 04:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| cab7352f-3908-32c8-b9fc-ac1b4ea5ea0f | -7.23288 | -43.09745 | 2025-07-04 04:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 012a11f5-610a-3b0b-80bf-2f8e203e7a00 | -10.71082 | -49.6694 | 2025-07-04 04:17:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e9fa41c3-2859-3b68-aba8-f00c5491be25 | -6.93112 | -43.03888 | 2025-07-04 04:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 6aca6218-bd60-34d1-b5f0-9be8498bb427 | -6.7735 | -45.54345 | 2025-07-04 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c63b2c71-4e8f-353d-a278-19accc762f2e | -6.27791 | -43.67928 | 2025-07-04 04:17:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| a7637068-cf6a-3a80-a30b-24cb1588a8b5 | -11.91812 | -45.38349 | 2025-07-04 04:17:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 021ac707-d50e-3116-af9e-92c468a793ea | -6.59644 | -43.05676 | 2025-07-04 04:17:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| a50f6e25-440a-3a08-ba60-9538d835d256 | -16.54349 | -45.13352 | 2025-07-04 04:17:00 | NPP-375D | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| be83d6ad-f1f1-397d-b9be-72dd57d53c62 | -10.61994 | -48.07616 | 2025-07-04 04:17:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e8023179-22fb-33ae-b7ef-527d28a6c7cc | -9.00133 | -47.44555 | 2025-07-04 04:17:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6dae48b1-709e-3245-8ead-33b0dfec4425 | -11.02231 | -56.26064 | 2025-07-04 04:17:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 66f3a3bd-faa0-3fea-a898-72fe04ec047b | -6.99641 | -43.54411 | 2025-07-04 04:17:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d00c6e8f-28df-30da-9e56-d485abf78253 | -6.606 | -43.88923 | 2025-07-04 04:17:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 29.5 |
| 8dda7fab-dbb9-3108-a8d9-c7c2466d5ea1 | -6.7342 | -43.14648 | 2025-07-04 04:17:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a3220359-8f52-34b6-b51e-8cdc1525de1a | -12.16314 | -45.52781 | 2025-07-04 04:17:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 11c39af7-0fc0-3914-81d6-75653de7500e | -12.42512 | -43.7216 | 2025-07-04 04:17:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| ebe568e9-b3ad-378e-bf03-b7c19ceaaa95 | -18.03587 | -46.05169 | 2025-07-04 04:17:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7f828f44-a1a5-3556-aff0-a3db5e79a927 | -5.28608 | -45.16621 | 2025-07-04 04:17:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 486e2127-8b6d-3095-bb4c-8cc9fd60220c | -11.86701 | -44.85646 | 2025-07-04 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README11.md)
