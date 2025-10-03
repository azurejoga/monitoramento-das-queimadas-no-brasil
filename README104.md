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

## Dados Diários - Página 104

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 33134ab8-43db-3427-8f1e-2253616d498e | -11.90701 | -46.29017 | 2025-10-03 04:32:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| dffa0e89-ba06-39ea-b8e5-d863ab36ace7 | -11.80917 | -47.93153 | 2025-10-03 04:32:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e968cc3c-76a6-391c-bfc2-70f9b3fd82e7 | -5.63743 | -44.51478 | 2025-10-03 04:32:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 252c892e-8cb2-306e-87fc-6be9db61d6f5 | -7.74091 | -42.59803 | 2025-10-03 04:32:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 9a9c8721-da8f-35c3-844c-f6f56dd1ec3b | -5.7317 | -45.51052 | 2025-10-03 04:32:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c0d2e969-312d-38c8-afb3-3f7f10626da0 | -10.943 | -46.70396 | 2025-10-03 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8ebc0eef-ead2-358f-8484-0fabbc527700 | -7.90208 | -43.53402 | 2025-10-03 04:32:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 82cb2363-d8ec-321b-a33b-13e4a901f5ef | -11.2176 | -49.95544 | 2025-10-03 04:32:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 772696e0-fa80-331f-bbc9-5b2940b8da05 | -11.09789 | -47.83099 | 2025-10-03 04:32:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 56d963eb-9d0e-3042-a4a5-91058cd575de | -9.92245 | -43.73283 | 2025-10-03 04:32:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 46017b73-6a6e-3584-b423-7df8327f3d2a | -6.22518 | -45.35477 | 2025-10-03 04:32:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6f7fd9e6-62f4-3cd1-ad02-c7b15e3cb0e8 | -6.6441 | -43.59423 | 2025-10-03 04:32:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 67ed7235-8821-3d69-8fb8-0fa6d7a44ad9 | -10.94874 | -46.71264 | 2025-10-03 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fda9e9a9-d5db-3a75-89cf-9521fe08b362 | -5.74461 | -44.81237 | 2025-10-03 04:32:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f257796d-a902-31a0-a903-df7b395cfbcb | -7.81645 | -46.97736 | 2025-10-03 04:32:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3e96f658-f935-3486-8686-335a2200f706 | -9.3788 | -45.85085 | 2025-10-03 04:32:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 113b3c5b-9f00-3846-8542-84f2d15006fc | -11.37423 | -48.99778 | 2025-10-03 04:32:00 | NOAA-20 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 31193be6-9dbe-32d9-b32f-1426759e6319 | -7.77125 | -42.57951 | 2025-10-03 04:32:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 7.8 |
| acb2e421-d0b4-3129-a416-6e17dbf00d58 | -9.92318 | -43.72773 | 2025-10-03 04:32:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| bbac331a-78f4-37ae-aa09-851085d8569f | -9.91404 | -47.71758 | 2025-10-03 04:32:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 92dac11e-f487-3f56-ade4-99fde0a68bcf | -9.87872 | -47.81689 | 2025-10-03 04:32:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 732644e7-eeb8-326c-83db-1abb05ab6b63 | -11.48903 | -45.01722 | 2025-10-03 04:32:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7c59e5fa-696d-3848-bba1-ebae98e5d77b | -7.7911 | -42.55925 | 2025-10-03 04:32:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 1f1a4d0a-4f18-3a5e-a5f9-93937bdec89a | -10.8966 | -46.73618 | 2025-10-03 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 57386d93-b12f-3d80-9999-ac64d0e3cf25 | -6.30212 | -43.11253 | 2025-10-03 04:32:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 87a2a585-6cef-372d-aef3-c2d36c26af19 | -7.90451 | -43.54451 | 2025-10-03 04:32:00 | NOAA-20 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| fa9c59f0-c1cf-3127-a5b9-7953e804d64a | -8.61878 | -54.97659 | 2025-10-03 04:32:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 814b2dcc-a084-3d2f-b618-81fe9501fa19 | -6.66574 | -42.78909 | 2025-10-03 04:32:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| a3127a8e-4cb2-3795-936c-a8703b9f4d26 | -11.58955 | -47.63518 | 2025-10-03 04:32:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 22aa590a-e94c-3cf7-a284-fbd6830d3f4c | -8.69016 | -47.68729 | 2025-10-03 04:32:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0f699398-2236-36ad-8422-a509ea8d3683 | -11.49142 | -43.50208 | 2025-10-03 04:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 376721ab-9ad9-3e41-95cf-4433c7fe879f | -11.0552 | -47.80227 | 2025-10-03 04:32:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2eb74768-ca2e-3723-9ff4-8b29c9d75973 | -5.97576 | -44.15364 | 2025-10-03 04:32:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5fa350bb-ff30-3db9-b90c-f2d062450705 | -11.93235 | -47.88088 | 2025-10-03 04:32:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ce56e9f2-3200-3192-a200-ee3a5f9a4b3f | -10.89375 | -46.73184 | 2025-10-03 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 05794cee-8656-3ce7-883d-fd789dced0ef | -9.76728 | -46.22158 | 2025-10-03 04:32:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 307e5e51-f8cf-39cc-bd01-1bfbc0ac668f | -10.59755 | -48.7109 | 2025-10-03 04:32:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 194e40bb-5e40-3925-bd96-a0803bc35592 | -7.79098 | -42.50065 | 2025-10-03 04:32:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ee8332ba-293f-30ff-bcb3-c53334b3a840 | -5.90132 | -43.90708 | 2025-10-03 04:32:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 457222f2-db56-338c-9c4f-d4f7e3e70385 | -10.83743 | -46.59079 | 2025-10-03 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f7ddb7c9-8c9e-3882-aab2-00416e9879c8 | -11.55099 | -47.66244 | 2025-10-03 04:32:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 14d97cff-16e7-353d-8a1a-c6ddb936397d | -4.65698 | -45.79745 | 2025-10-03 04:32:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ccfe9b5d-5929-306e-a68e-defbb591a46f | -11.08355 | -47.70766 | 2025-10-03 04:32:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7e397ef9-d474-3127-9a23-d0855a3ea643 | -6.22985 | -45.34758 | 2025-10-03 04:32:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 15.9 |
| eecaf773-763c-3aa5-a2e6-5ad323c25832 | -7.74311 | -42.58318 | 2025-10-03 04:32:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| b2ede76a-f8b3-32f2-82db-60819e0e1758 | -8.83867 | -48.85687 | 2025-10-03 04:32:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8bb7c0ec-9281-3313-b8ae-941301eaec6b | -11.57336 | -47.65108 | 2025-10-03 04:32:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 04ffe8f9-5723-3d72-80b3-f5ca730dd8a8 | -7.25403 | -49.41012 | 2025-10-03 04:32:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1eef3fbf-dcb2-3dd7-ad01-daf28808123d | -8.8847 | -46.59115 | 2025-10-03 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7e6ae7ed-76ba-3f9d-beb3-799da93bb867 | -4.66317 | -45.80213 | 2025-10-03 04:32:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8faa6a2c-57d0-3a4c-a9c5-620906048463 | -10.87601 | -46.70969 | 2025-10-03 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 736d047d-14cd-39a7-9190-f7cd07baf1f6 | -11.91056 | -46.29059 | 2025-10-03 04:32:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4d7946f4-17b1-321b-886c-f7a92642ff87 | -10.33824 | -48.17755 | 2025-10-03 04:32:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 242ba9f6-2def-3996-92bd-d1e3685f10c4 | -8.48293 | -44.59475 | 2025-10-03 04:32:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7e5b81e7-939f-3f55-91cb-98a796555740 | -11.62693 | -48.53501 | 2025-10-03 04:32:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7314a8a4-78cb-370f-9243-a161bfebe670 | -7.86687 | -47.30656 | 2025-10-03 04:32:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0eef72ee-c7a4-330a-9906-c18588e28372 | -11.62988 | -45.06266 | 2025-10-03 04:32:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ae14b67d-9c45-316a-b046-9872352b3a82 | -10.87276 | -51.26064 | 2025-10-03 04:32:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8fb0fc58-3fb2-334f-b5e3-72e1b3a7c40e | -11.49554 | -43.50267 | 2025-10-03 04:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3eca6157-cfb1-38df-9f4b-97b60d09ca73 | -10.01234 | -48.502 | 2025-10-03 04:32:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a7b48aa8-e3ce-381b-9ff1-b1a66badfc5e | -6.45233 | -43.12732 | 2025-10-03 04:32:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 64e7cd91-2876-3a9b-b4f8-53586fc05988 | -6.3627 | -43.30124 | 2025-10-03 04:32:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 71ba5b01-a2a2-35d9-80c1-72b04ef0fdb3 | -11.35407 | -44.93859 | 2025-10-03 04:32:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 41c31543-07e0-3248-b59a-2f28ab18590d | -11.11408 | -47.8591 | 2025-10-03 04:32:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 82f87f7d-94f3-3955-83a1-25164ab485d7 | -10.54143 | -43.64797 | 2025-10-03 04:32:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9dedc039-9e53-3eaa-bcba-5334b3fe3cf9 | -7.66637 | -47.28624 | 2025-10-03 04:32:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 91edc7ee-56cc-3a7b-82ec-667965ed51a2 | -8.02182 | -55.42034 | 2025-10-03 04:32:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c70f4704-2f30-394c-aecf-31766bac5168 | -10.4404 | -49.35777 | 2025-10-03 04:32:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| dcb69bde-cc85-375a-8647-ec038c06f60a | -10.12365 | -52.34601 | 2025-10-03 04:32:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 67908156-f400-3b76-a3d0-a1cea4e77090 | -9.91936 | -50.90259 | 2025-10-03 04:32:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3be9d954-ddbc-382e-9dc6-0667ff62424e | -11.11523 | -47.87378 | 2025-10-03 04:32:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f935c499-e35a-3389-91c5-5c312576f72a | -11.06356 | -47.79251 | 2025-10-03 04:32:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8b0c39d7-f339-331b-a78f-5218048793b2 | -7.2945 | -45.26925 | 2025-10-03 04:32:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d22ea7ef-e6cd-3315-b6cf-f96a24fb7d0b | -11.06244 | -47.79971 | 2025-10-03 04:32:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 64683159-805d-306a-8adf-f70e1b691794 | -11.89233 | -42.82411 | 2025-10-03 04:32:00 | NOAA-20 | BROTAS DE MACAÚBAS | BAHIA | Brasil | 2904506 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| dfb856a2-c487-3234-a4bb-d9e1e6ff36aa | -6.36522 | -43.96639 | 2025-10-03 04:32:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 00555d15-ce25-3e40-a2c4-21e2c5682c7e | -9.92125 | -43.7691 | 2025-10-03 04:32:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| cdfe1743-aa37-3af4-b287-207f9ba4ac52 | -6.70742 | -42.81321 | 2025-10-03 04:32:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 1bc8a853-a18a-3224-adce-4faaef9cd2b1 | -6.48166 | -44.21749 | 2025-10-03 04:32:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9ac5e190-abeb-3205-9680-ba98f08ebd14 | -7.76482 | -46.27127 | 2025-10-03 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 43.1 |
| faf03c67-6f7c-3d87-a01b-042fd552b24e | -5.71445 | -49.25199 | 2025-10-03 04:32:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ba3255af-eadf-3c1a-a331-0dcf891c1e3e | -6.59689 | -44.32038 | 2025-10-03 04:32:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 909df6dd-ab82-391e-abc8-34aa703350f0 | -5.2252 | -44.49445 | 2025-10-03 04:32:00 | NOAA-20 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a743228e-e649-3b25-bb97-a63b00dc64b0 | -7.7665 | -42.61282 | 2025-10-03 04:32:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| ac04f953-1556-31b6-a319-6686e166036a | -6.55261 | -43.87316 | 2025-10-03 04:32:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 86b13811-1c7d-3845-a358-3ec779eed36d | -11.62919 | -47.99445 | 2025-10-03 04:32:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 5876f7a5-e2d2-3a5f-9050-b425461c7b4f | -9.92506 | -43.62984 | 2025-10-03 04:32:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 92289312-9c0e-3f7a-af47-e43918da0ac3 | -11.47703 | -44.96812 | 2025-10-03 04:32:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6181f7a5-015b-3c5d-802a-b9997293d197 | -11.08465 | -47.87261 | 2025-10-03 04:32:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 1df50c04-9fb7-3548-b957-64f60117c05e | -10.89089 | -46.72751 | 2025-10-03 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5bf324de-404f-39a8-ad5f-193396868040 | -7.75797 | -46.24755 | 2025-10-03 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 22.2 |
| 7d26e72c-d1c7-347b-b968-6cfcbedf9dda | -11.08853 | -47.8696 | 2025-10-03 04:32:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| e6d90b97-9afb-3f1b-a604-c903eaa83969 | -6.03341 | -44.62965 | 2025-10-03 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 90e49dc8-e578-3db1-bd39-0e0765b20849 | -6.99961 | -47.20687 | 2025-10-03 04:32:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 86328121-7b63-386b-9fe8-4d755077f153 | -11.9022 | -46.74301 | 2025-10-03 04:32:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3a089aad-08a4-309c-95fe-7cd8d6ceaa86 | -7.75571 | -46.26245 | 2025-10-03 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 24.5 |
| 1aa928df-7660-32a7-be9d-6cf68ac02303 | -8.81011 | -46.66955 | 2025-10-03 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c54fa79c-c494-32da-88dc-8074c32ffbff | -11.92009 | -46.27498 | 2025-10-03 04:32:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8ecaed67-a474-385d-a2ae-a4245bad0f76 | -7.29525 | -44.18881 | 2025-10-03 04:32:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3586bb6c-50ae-3357-a31b-a176f8f0721d | -7.75211 | -42.56509 | 2025-10-03 04:32:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 74.1 |


[Clique aqui para ver as próximas entradas](README105.md)
