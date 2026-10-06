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

## Dados Diários - Página 97

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 869738d0-d2c6-31b0-9f68-96e2b149cdd8 | -8.9875 | -65.4006 | 2026-10-06 18:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 98.0 |
| 73b8de93-9b02-3c0f-beea-cf42ca090b4b | -9.1829 | -67.3861 | 2026-10-06 18:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 102.8 |
| 68bdc927-ae5c-3647-8460-0cce29659ea2 | -11.6374 | -43.664 | 2026-10-06 18:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 106.4 |
| 70d5125b-37f2-3015-bbf9-3a2d80c5e933 | -9.1406 | -68.9219 | 2026-10-06 18:10:00 | GOES-19 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 71.4 |
| ab3cda59-d6a7-38ed-a59e-bc371a246c84 | -9.5468 | -64.8196 | 2026-10-06 18:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 268.4 |
| b72ace4f-67e1-3892-8d1d-b687a307ba3b | -9.9444 | -67.1982 | 2026-10-06 18:10:00 | GOES-19 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 118.6 |
| 05e52d65-2530-3c03-a9ab-ac6e3a04c460 | -11.6946 | -43.6787 | 2026-10-06 18:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 125.3 |
| 4bb21594-2572-39cb-9626-5c5a39d1e06f | -9.8619 | -64.9958 | 2026-10-06 18:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 93.3 |
| a58fe678-3337-3e18-8895-9d81771e4152 | -9.1256 | -67.8507 | 2026-10-06 18:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 98.2 |
| 9e271556-d439-3dc2-8cc7-ef93cc1696a5 | -9.1645 | -67.3495 | 2026-10-06 18:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 123.6 |
| 77c56bd2-e79c-3d00-aa6f-edab1eff9891 | -5.9838 | -40.9123 | 2026-10-06 18:10:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 130.4 |
| 43d90a7b-4c4b-3f9d-96db-aef0fe5984a9 | -9.1068 | -67.9437 | 2026-10-06 18:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 94.2 |
| 6e36afcd-cea2-3230-8dd6-0f917ed5a1d8 | -9.5467 | -64.8384 | 2026-10-06 18:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 96.3 |
| 844d6f0f-5c2c-3ad7-bc8d-7415baae142c | -9.1257 | -67.8322 | 2026-10-06 18:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 115.2 |
| 9edac7a6-8712-368e-ae70-ec8328bbd3bc | -6.0266 | -42.2792 | 2026-10-06 18:10:00 | GOES-19 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 112.4 |
| 3d1721d9-3b3c-37d2-9326-564634213759 | -11.8216 | -47.3521 | 2026-10-06 18:10:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 107.4 |
| ee997914-7db1-3ea8-a304-8ad89279a611 | -6.65 | -43.7749 | 2026-10-06 18:10:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 68.3 |
| e1e90679-1b64-3e31-9673-beb0011ffc11 | -8.537 | -66.9764 | 2026-10-06 18:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 102.9 |
| a9a17dce-77a2-384a-8c22-1c4e74f53452 | -3.292 | -42.2673 | 2026-10-06 18:10:00 | GOES-19 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 169.5 |
| 22be5202-dc36-3823-86b1-0d9a4ebb5772 | -7.8167 | -45.3193 | 2026-10-06 18:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 137.4 |
| 156e92ea-4612-3de1-8474-0e5c7e3c33b1 | -3.9798 | -42.8688 | 2026-10-06 18:10:00 | GOES-19 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Caatinga | 116.0 |
| 030c3387-8087-3df7-9cf8-b76d0f44f077 | 1.8038 | -55.5458 | 2026-10-06 18:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 71f29fd7-ad39-37d0-8eac-89f709321f93 | -15.6055 | -41.6797 | 2026-10-06 18:10:00 | GOES-19 | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 128.9 |
| 88657ab6-1db4-3b1d-89b3-0c25f499c683 | -9.4435 | -67.1008 | 2026-10-06 18:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 142.4 |
| 2f066ff4-996b-3773-81c0-0c1e5bc12df6 | -7.5332 | -70.0148 | 2026-10-06 18:10:00 | GOES-19 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 84.9 |
| f551d7f9-9ec9-3535-97e8-7e0f79394411 | -8.1949 | -70.4634 | 2026-10-06 18:10:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 73.5 |
| c3871a78-8931-37b4-ab9c-402b56490497 | -6.6027 | -37.8944 | 2026-10-06 18:10:00 | GOES-19 | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 90.2 |
| d4e31b14-aced-3e4d-9bb3-0a37b469378b | -6.0078 | -42.2808 | 2026-10-06 18:10:00 | GOES-19 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 89.8 |
| e7aa9d0c-d5d9-31c0-a404-d9faa35c836e | -9.0231 | -65.7169 | 2026-10-06 18:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 96.7 |
| 9ba6d87c-a63a-35c5-882f-1e1e354c3dcd | -9.1333 | -65.9186 | 2026-10-06 18:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 90.4 |
| 882328a2-0211-3875-8c70-f73d28f80323 | -9.0045 | -65.7174 | 2026-10-06 18:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 95.7 |
| 85d9e1f2-b3fb-3253-b26b-93d72a041bdb | -9.0705 | -67.7225 | 2026-10-06 18:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 79.9 |
| de25f959-ed61-319e-8fa7-d164126e7b05 | -8.5367 | -67.032 | 2026-10-06 18:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 106.9 |
| 5554483d-ec51-35bc-ae6d-3793bfbfacfc | 2.4585 | -50.8299 | 2026-10-06 18:10:00 | GOES-19 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 76.6 |
| 6effb7e6-ac0f-3db9-aafc-8a8d75f3b5e9 | -11.7143 | -43.652 | 2026-10-06 18:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 97.3 |
| 74a50ec7-0ca3-3804-98a4-e17f2702acbc | -9.2366 | -67.885 | 2026-10-06 18:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 145.5 |
| ab9400f0-bd17-31ee-9315-d04bdfd0414f | -6.6312 | -43.7765 | 2026-10-06 18:10:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 5d9edf1b-d520-3c7d-9244-b03535e70314 | -6.5985 | -41.5582 | 2026-10-06 18:10:00 | GOES-19 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 102.1 |
| 490caf84-5b1a-33f5-8c18-c8b5c6775061 | -9.8844 | -64.2802 | 2026-10-06 18:10:00 | GOES-19 | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 117.8 |
| a9033c02-48ee-39e1-9966-38d0a74581c7 | -5.7376 | -45.1533 | 2026-10-06 18:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 941.4 |
| 5290f9fd-0d18-3261-aabd-e803f2dc865a | -9.1895 | -65.7863 | 2026-10-06 18:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 88.0 |
| 79f1d5d2-1906-3ba1-ad82-178602fa87e8 | -8.7632 | -72.7808 | 2026-10-06 18:10:00 | GOES-19 | MARECHAL THAUMATURGO | ACRE | Brasil | 1200351 | 12 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 6d5b2378-8fce-36e8-8462-e39235dafee4 | -9.5469 | -64.8008 | 2026-10-06 18:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 125.7 |
| 2b949537-d9a0-37fb-a021-b21e7fbe8dc4 | -9.256 | -67.6438 | 2026-10-06 18:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 101.8 |
| 9bd637be-f4ed-3d55-8ac2-4d3f70643c04 | -9.1055 | -68.3135 | 2026-10-06 18:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 100.4 |
| 5626d83d-0ea1-337d-8656-f34f1191165c | 3.5263 | -51.2778 | 2026-10-06 18:10:00 | GOES-19 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 56.5 |
| d4ca4a68-932d-314b-87bc-090bf83617c9 | -5.7378 | -45.1307 | 2026-10-06 18:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 124.7 |
| cfa508f8-84eb-3252-ba21-c9393e646879 | -8.5368 | -67.0135 | 2026-10-06 18:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 100.3 |
| 38f94a30-fe64-37eb-8005-cea17dd21dcb | -9.4819 | -66.7836 | 2026-10-06 18:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 103.9 |
| c16260e2-2f6c-3e59-a2b6-f8767ecec734 | -9.5151 | -67.7484 | 2026-10-06 18:10:00 | GOES-19 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 133.6 |
| dca2ba72-83eb-3a45-a81a-7768f59836ed | -8.573 | -67.2163 | 2026-10-06 18:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 88.8 |
| 4c0499e3-401b-32b6-9d19-dce26b5d9ea0 | -7.47 | -42.8078 | 2026-10-06 18:10:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 66.4 |
| e68ea285-6cd4-379b-ac9d-60e25528d8d4 | -11.6951 | -43.655 | 2026-10-06 18:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 123.3 |
| 4c0853eb-a414-3d77-9b3b-7c68d0479160 | -9.8071 | -44.7804 | 2026-10-06 18:10:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 89.9 |
| 0bb37c4f-f2e1-3d72-878b-d9806054c21f | -4.4972 | -43.701 | 2026-10-06 18:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 90.5 |
| 193d0631-8eee-38e7-85df-fa14e45c0be7 | -4.2967 | -42.9915 | 2026-10-06 18:10:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 201.8 |
| e8a9c580-d4a0-39f2-9fd2-3d07168055e7 | -6.6217 | -37.8923 | 2026-10-06 18:10:00 | GOES-19 | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 95.3 |
| 29ee1568-87c2-301f-a956-8b4d67905c45 | -9.3431 | -64.7143 | 2026-10-06 18:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 124.0 |
| 4844f1df-171b-3a54-b49e-0c95c98e7449 | -9.1253 | -67.9432 | 2026-10-06 18:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 108.7 |
| 1fdac4d7-7668-3785-90ce-19d83e6d4b10 | -4.8081 | -42.1577 | 2026-10-06 18:10:00 | GOES-19 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 153.7 |
| 98e44c3b-b8e9-36c8-b69c-cc86093b1e7e | -11.8296 | -44.688 | 2026-10-06 18:10:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 282.4 |
| 78c7a287-bbf6-373e-8569-70ae4cf6eb06 | -8.9607 | -67.3733 | 2026-10-06 18:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 80.8 |
| dbc4bf04-5766-3c0a-b534-543445bf51ca | -3.1926 | -43.443 | 2026-10-06 18:10:00 | GOES-19 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 109.1 |
| 7dc920c3-cc1d-3804-b8cd-a3c430b3a79c | 0.7266 | -51.3955 | 2026-10-06 18:10:00 | GOES-19 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 209.2 |
| df67afd4-960b-3007-b826-97440282370c | -3.0077 | -43.1251 | 2026-10-06 18:10:00 | GOES-19 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 91.2 |
| ab128f56-639c-3d65-8c9e-f394e3fa46c2 | -10.9762 | -45.4094 | 2026-10-06 18:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 154.3 |
| bb4aed49-4093-3447-be8c-1f300a42943b | -7.7127 | -73.0611 | 2026-10-06 18:10:00 | GOES-19 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 67.3 |
| bbc655b4-acb4-36ee-a978-9bb0eb7c8590 | -9.0705 | -67.741 | 2026-10-06 18:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 140.0 |
| 91194262-b673-356e-87c2-7b6010f7e8dd | -8.2678 | -70.8836 | 2026-10-06 18:10:00 | GOES-19 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 87.8 |
| 83079c18-a9fa-34a0-8e69-fad06e3b2b07 | -9.3835 | -68.2701 | 2026-10-06 18:10:00 | GOES-19 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 81.0 |
| 724b0295-8374-3602-9638-bf93e68bc807 | -9.5006 | -66.7459 | 2026-10-06 18:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 96.4 |
| a04bcc04-45da-351d-b345-a2dec3b696ec | -11.8315 | -43.5391 | 2026-10-06 18:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 174.9 |
| 54ea1345-254b-3aba-8519-c2687d80dd6d | 1.8767 | -55.7424 | 2026-10-06 18:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 79c717b0-fdae-3e63-852a-0ec7c95b3ab3 | -6.8408 | -41.7994 | 2026-10-06 18:10:00 | GOES-19 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 97.1 |
| 65bb9015-3fd1-39c3-9391-2631a8a7e029 | -9.1072 | -67.8326 | 2026-10-06 18:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 111.2 |
| a841f466-9f01-3167-acc0-400d7e1b21f4 | -8.7324 | -69.4271 | 2026-10-06 18:10:00 | GOES-19 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 3d32a41c-d466-383f-85dc-76fe6834b4fd | -7.86 | -44.21 | 2026-10-06 18:15:00 | MSG-03 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| efd8a598-921f-34f2-b33e-faf6504e22a1 | -9.96 | -43.74 | 2026-10-06 18:15:00 | MSG-03 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 28c695aa-e2f3-3c48-967a-bf3615821c3c | -5.7 | -45.13 | 2026-10-06 18:15:00 | MSG-03 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e69f4fca-946d-351a-8123-e0c40176be21 | -5.73 | -45.18 | 2026-10-06 18:15:00 | MSG-03 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fad33716-e1bf-3bb4-85ba-883a1df0ab03 | -9.95 | -43.56 | 2026-10-06 18:15:00 | MSG-03 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2a85e276-609c-35e1-b924-35f07929b5b2 | -9.95 | -43.47 | 2026-10-06 18:15:00 | MSG-03 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e4b8d089-848c-3d2f-8518-82408e74040d | -3.17 | -50.59 | 2026-10-06 18:15:00 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 08a286b3-be26-3356-b0f9-a2144d3bfd28 | -1.29 | -54.55 | 2026-10-06 18:15:00 | MSG-03 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b09d2c72-e9b1-30f3-bf3b-437ba515fc03 | -5.7 | -45.18 | 2026-10-06 18:15:00 | MSG-03 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f07547c1-b707-3768-8296-9601ceb32644 | -5.72 | -41.75 | 2026-10-06 18:15:00 | MSG-03 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| f2ce9691-3db4-3421-b26f-54602642820f | -7.86 | -44.16 | 2026-10-06 18:15:00 | MSG-03 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 24c0a209-654d-3b66-9df1-ba11a3b6037e | -10.01 | -43.52 | 2026-10-06 18:15:00 | MSG-03 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3bf9c4a5-7da7-3146-b89f-9ca834880d4e | -9.96 | -43.83 | 2026-10-06 18:15:00 | MSG-03 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 1c30e3d3-6244-33e3-b316-e41526d15cbe | -9.95 | -43.6 | 2026-10-06 18:15:00 | MSG-03 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b961e036-8ed7-3601-8fc0-67afae26be6f | -7.43 | -44.46 | 2026-10-06 18:15:00 | MSG-03 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 95ad717d-c0b2-3c98-a391-11438ed3e9d2 | -9.96 | -43.79 | 2026-10-06 18:15:00 | MSG-03 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| f94e44be-afaf-3343-a276-91beceb1acd8 | -3.08 | -53.75 | 2026-10-06 18:15:00 | MSG-03 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ce89889d-a043-337b-a164-efe5a4cc5bfe | -5.73 | -45.14 | 2026-10-06 18:15:00 | MSG-03 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ffbd6b59-6df2-3c34-b895-2f2e9afd9385 | -3.17 | -50.53 | 2026-10-06 18:15:00 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5ce6a2a9-eed8-323b-b2e0-4a7f3906d934 | -9.95 | -43.65 | 2026-10-06 18:15:00 | MSG-03 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 17a2fe34-25ff-36ce-b4f9-c3e47198bbc0 | -9.98 | -43.47 | 2026-10-06 18:15:00 | MSG-03 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 42574342-3e93-3937-b40f-dfca67442c62 | -1.32 | -54.55 | 2026-10-06 18:15:00 | MSG-03 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cba19e25-4675-3820-96b4-f47fbc915de7 | -3.02 | -53.86 | 2026-10-06 18:15:00 | MSG-03 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 263129ef-f3b9-3ffd-b924-1b6b187a4ce9 | -9.95 | -43.69 | 2026-10-06 18:15:00 | MSG-03 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README98.md)
