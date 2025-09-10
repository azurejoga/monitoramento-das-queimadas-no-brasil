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
| 4e2b89a8-0c84-3384-99a5-3441c0514391 | -5.76268 | -45.5245 | 2025-09-10 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8c5f096b-cecf-349d-98f2-d6315519b797 | -7.93931 | -44.85235 | 2025-09-10 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 022e4d3d-cb1b-3f8a-bdc6-5ba9e1428a48 | -5.53123 | -44.33037 | 2025-09-10 04:14:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cf1a70dc-5abb-3cbf-bb92-674da55a8af6 | -7.66347 | -50.29346 | 2025-09-10 04:14:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 173eb6ca-4a66-39cf-82a7-eb4c126eb929 | -8.21704 | -45.7927 | 2025-09-10 04:14:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f4d2d53e-d772-3b45-b397-af396d97b60e | -9.44671 | -46.71427 | 2025-09-10 04:14:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e9616809-3999-3611-93ec-b62d16b10984 | -5.80691 | -45.29253 | 2025-09-10 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 26c76661-be9b-32f2-83ce-3e524e32d552 | -6.20935 | -43.50302 | 2025-09-10 04:14:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e17d9f5d-a697-3319-bd0d-c86e792d574f | -5.90463 | -45.79432 | 2025-09-10 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 35e91283-e661-304c-8540-07fd516db7cd | -5.67086 | -43.35784 | 2025-09-10 04:14:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8eb1f8a8-a136-35f6-b5da-a7d0ae76883d | -7.56171 | -48.22943 | 2025-09-10 04:14:00 | NOAA-21 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1ca675c0-8266-3585-b29a-3cd2563d7760 | -6.29912 | -42.20773 | 2025-09-10 04:14:00 | NOAA-21 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| ad9f0816-c4be-3aa3-b896-edbf14e1244f | -8.46813 | -48.9502 | 2025-09-10 04:14:00 | NOAA-21 | PEQUIZEIRO | TOCANTINS | Brasil | 1716653 | 17 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 82382a3f-ecd5-30c2-9552-aba572b508a8 | -7.25374 | -44.45541 | 2025-09-10 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cd5b4186-ed46-3739-ad33-dbba5b686f44 | -9.80766 | -47.76316 | 2025-09-10 04:14:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 87d390fc-cf43-37ba-a5c7-0bbb80cc4121 | -5.73496 | -43.09976 | 2025-09-10 04:14:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 0.6 |
| ab01c066-adc2-3a8c-bd95-1f172a64f487 | -9.44588 | -46.69747 | 2025-09-10 04:14:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| dc3681df-96e6-346f-a8bd-7847cb21e531 | -8.06904 | -48.66379 | 2025-09-10 04:14:00 | NOAA-21 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 435df3c5-a269-3273-9b2e-56e290049e2c | -6.5211 | -42.92358 | 2025-09-10 04:14:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c4fdd4fa-db72-3998-baf7-36667da3005d | -9.45374 | -46.71558 | 2025-09-10 04:14:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0da538ee-b2dd-329d-afef-53be16db6dd8 | -9.44035 | -46.70891 | 2025-09-10 04:14:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 9581397c-f186-336c-b21d-e0e5944917d3 | -5.72734 | -45.41248 | 2025-09-10 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 856af1f9-a21f-30eb-8d1f-35c8444a329c | -9.31604 | -46.71339 | 2025-09-10 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5e0f0909-7f2e-3ff1-9abe-81a6e6a65859 | -8.0448 | -48.68495 | 2025-09-10 04:14:00 | NOAA-21 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 15.5 |
| f9879071-170d-32ea-b3d5-e0935a0ea646 | -6.20469 | -43.40335 | 2025-09-10 04:14:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d3787c9e-cd25-31ce-9236-738f37575034 | -9.14457 | -46.2061 | 2025-09-10 04:14:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| aeb600c4-be2f-3094-a4f2-1c6abaf3f3df | -9.67532 | -46.89133 | 2025-09-10 04:14:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6a9daf22-2c00-3bbc-a9af-d1bd903ec7c6 | -5.72453 | -45.60598 | 2025-09-10 04:14:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 148f4cef-7bd3-3441-bdb1-84868d377950 | -6.25704 | -43.41924 | 2025-09-10 04:14:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 41292b4f-4f85-33d7-ad59-19900058fc5d | -7.18459 | -44.93458 | 2025-09-10 04:14:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 18.7 |
| f51a3a12-8c81-361a-b208-e457e25919c8 | -7.84248 | -45.4139 | 2025-09-10 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6987e78c-3a56-36ed-8dc8-84aaf5672521 | -6.18179 | -41.05557 | 2025-09-10 04:14:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| f635c5c9-cfb4-3df6-839d-ea5b213151a4 | -9.43831 | -46.72116 | 2025-09-10 04:14:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| bca35a3a-86e0-3b12-a9c6-23689882e772 | -6.87761 | -47.88778 | 2025-09-10 04:14:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ebd3b997-48d7-3bdb-ac2e-6fcd9f9bcdb6 | -6.18953 | -43.49994 | 2025-09-10 04:14:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 06eb7f5b-44e2-30f6-9c65-bc613548e39a | -8.86029 | -47.23189 | 2025-09-10 04:14:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 503d8e56-c2f9-3a06-9d7d-49179ed7898d | -5.48357 | -42.66137 | 2025-09-10 04:14:00 | NOAA-21 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 989604ce-ecfc-375a-a612-d6c42421f2b3 | -8.96685 | -44.93795 | 2025-09-10 04:14:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5e253b09-a878-322e-8755-2aee4e07ff28 | -9.8258 | -46.05742 | 2025-09-10 04:14:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ec87721b-e0bd-39ce-82aa-17e19d1f8f51 | -6.41458 | -44.40456 | 2025-09-10 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fe3bc618-176c-3546-808f-7aff13e53c8f | -5.85452 | -44.17842 | 2025-09-10 04:14:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3653f1aa-2c26-3d64-a465-870b5cac9d91 | -9.21851 | -50.54488 | 2025-09-10 04:14:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 40b1e09c-592c-38fb-a8a8-41e233e38b21 | -6.89952 | -43.91855 | 2025-09-10 04:14:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 13c8c9ed-5dac-3bd5-83c4-80dce2f9791e | -9.52719 | -48.26711 | 2025-09-10 04:14:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 52af50b9-2031-3013-bf6f-17e7af4e49f8 | -6.99944 | -45.65046 | 2025-09-10 04:14:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b4136a9a-0aa3-3204-bead-9bdccaa5a56b | -7.07923 | -45.20216 | 2025-09-10 04:14:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| f0cc8e3e-7093-30ff-a208-b2f8b3fb7af8 | -6.2039 | -41.02348 | 2025-09-10 04:14:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 03385952-d896-3098-b90d-54e27b77f8d8 | -7.66884 | -50.26254 | 2025-09-10 04:14:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 49f4693c-9a38-38f3-bd85-68e97e7461e6 | -8.02217 | -44.50252 | 2025-09-10 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 50c5992e-e2e2-3bf4-bc28-906b059ae988 | -3.96426 | -43.23941 | 2025-09-10 04:14:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d4e7ecd6-9d79-3bae-9db7-b77158f007bd | -5.63867 | -45.41883 | 2025-09-10 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 588d3bcc-e65a-3a99-b8ff-2ee86893bc39 | -5.58066 | -45.03792 | 2025-09-10 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 35.5 |
| 124ab1a5-0ec2-3a2b-bf5e-d8aeb535dedf | -4.97028 | -43.63678 | 2025-09-10 04:14:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e091c832-0d61-35d7-9bd7-7bcd034448a1 | -8.47026 | -47.29574 | 2025-09-10 04:14:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e840a187-0138-332b-90a4-f71024d282de | -5.407 | -43.45735 | 2025-09-10 04:14:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5164ef78-d7b1-3efa-bdff-8ac2c4d95d2b | -5.65015 | -42.62011 | 2025-09-10 04:14:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 6536f0b3-fc38-30cb-8605-cc576613ac3d | -8.05219 | -48.69009 | 2025-09-10 04:14:00 | NOAA-21 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 33.4 |
| e96bf26d-e648-34ef-a300-4468a599d514 | -6.18407 | -42.66502 | 2025-09-10 04:14:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 27e2ce4d-1323-3413-8c22-1509ab9bf53f | -6.05961 | -43.13356 | 2025-09-10 04:14:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 02b283a0-1009-3e9d-b40c-75ba486aeed4 | -7.18516 | -44.93095 | 2025-09-10 04:14:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 28344276-1907-37eb-8faf-cda57165ad1d | -6.06291 | -43.13408 | 2025-09-10 04:14:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 0a612ebe-af2a-311c-9ce7-8ef84a5a29d3 | -8.04111 | -43.82356 | 2025-09-10 04:14:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| ef2968c6-45f4-3f63-9980-bc1e722012c7 | -5.68184 | -43.35249 | 2025-09-10 04:14:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bd1083a1-5b72-3fb5-ac25-8a555f146aec | -5.25411 | -45.10197 | 2025-09-10 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7ce4fd68-2224-3c57-8c25-45719070edc1 | -7.23417 | -46.1904 | 2025-09-10 04:14:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1a86e402-375c-3cd2-b967-e198abbf3202 | -6.98241 | -43.15248 | 2025-09-10 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 216a803c-b806-3fdf-a676-b586c06de9c0 | -6.55421 | -42.93233 | 2025-09-10 04:14:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c1c926e6-f5b7-3cf5-81a0-e531438bb1ed | -5.66123 | -51.63582 | 2025-09-10 04:14:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b9ac3436-7dc6-3bf1-a37b-13db2540af12 | -5.40945 | -42.8545 | 2025-09-10 04:14:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 4d90ad0f-8ec2-33a1-9021-e791f18c478e | -6.26028 | -43.39856 | 2025-09-10 04:14:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 611626be-c2d3-3adf-a2ea-a5670b3781a2 | -4.08941 | -50.69118 | 2025-09-10 04:14:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9bf45c0c-17f9-3f56-93dd-cc43929db84d | -6.34625 | -42.60498 | 2025-09-10 04:14:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b87ba2ec-5eda-38b2-b52b-d5d4603490b3 | -7.81609 | -47.50505 | 2025-09-10 04:14:00 | NOAA-21 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 71035d38-1a12-3748-9fa1-48237aa77401 | -6.23792 | -43.49336 | 2025-09-10 04:14:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c3204e5d-e2d5-3cb9-88b6-2fd89be027f2 | -8.74714 | -47.10011 | 2025-09-10 04:14:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| d22be26a-79d7-394d-84e7-710c57653c6b | -5.71743 | -45.41553 | 2025-09-10 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c32566a9-7ae0-37c0-a38e-6808a7695eda | -9.67465 | -46.89544 | 2025-09-10 04:14:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 672e6c16-2139-348f-ae58-eece22587de8 | -7.07982 | -45.19849 | 2025-09-10 04:14:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 3620e1d9-45f8-3889-99ea-1062c6412f88 | -8.01092 | -45.52501 | 2025-09-10 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e82bbe69-9f49-3ff8-8abd-98954db52ea9 | -8.32792 | -44.86777 | 2025-09-10 04:14:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4bb6fe9e-4d10-3e64-a3ac-1f83bc9f4cd0 | -5.9155 | -45.81631 | 2025-09-10 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fcab79e5-eccc-3296-b814-47a487c1db62 | -9.09637 | -46.96495 | 2025-09-10 04:14:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e24d3f01-06fc-3bd1-8f4e-ec57a657d9e4 | -6.87596 | -47.89768 | 2025-09-10 04:14:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 302c1fca-5647-34f3-bc06-5dc3008f32ab | -8.07046 | -48.631 | 2025-09-10 04:14:00 | NOAA-21 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 8cb7cf2d-3074-374a-8288-5454ad05d1eb | -5.418 | -43.45198 | 2025-09-10 04:14:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 2233b528-b4ec-3b1f-aa95-7f7d856f1145 | -5.6747 | -43.35491 | 2025-09-10 04:14:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 58517126-9214-3ebd-8769-b2e458c8e92d | -5.5836 | -42.91698 | 2025-09-10 04:14:00 | NOAA-21 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 4c468018-60a0-367b-bd88-875f8768060a | -5.42473 | -42.82161 | 2025-09-10 04:14:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 8a344360-25ad-3ad1-b926-89b2b6bd9bfb | -5.71853 | -45.4229 | 2025-09-10 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 81d054b5-fe8d-37cc-b42a-bd1dccdb89ad | -5.67764 | -45.46437 | 2025-09-10 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ddd613e6-6885-3ffa-beb3-f8d823744386 | -4.49859 | -43.93108 | 2025-09-10 04:14:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e7fb7a73-792e-3839-b610-102b66b60c9d | -5.71396 | -45.41499 | 2025-09-10 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 19b37287-3629-34a6-8874-6013c9e78f25 | -6.35213 | -43.04923 | 2025-09-10 04:14:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 736e7b3f-ce33-3c1b-88d4-1ecfd5af2482 | -5.96214 | -45.79543 | 2025-09-10 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1c2591ea-244e-3915-9a1d-57b78592e85a | -6.1856 | -41.05149 | 2025-09-10 04:14:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 0b4ed034-0e65-341c-92c5-6cb506c83b52 | -9.66524 | -46.64568 | 2025-09-10 04:14:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 73893f1b-f2ac-3168-b5c5-43203984089d | -5.41329 | -42.85157 | 2025-09-10 04:14:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a398c6bc-efd4-334a-ab1d-330239eb200e | -7.35181 | -46.16003 | 2025-09-10 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e1a8f497-fa80-345e-bfb5-14d8731fecd4 | -9.69376 | -46.8235 | 2025-09-10 04:14:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 60e20a5c-ae3a-3783-974d-1229c6ce7b43 | -6.26526 | -43.40993 | 2025-09-10 04:14:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |


[Clique aqui para ver as próximas entradas](README31.md)
