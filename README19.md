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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8c669b13-137e-369d-b6c8-1f56ebb3a62b | -6.7799 | -44.08607 | 2025-09-04 03:36:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 22.2 |
| ba8bab07-381d-39ce-80ad-552daaa1113b | -7.72169 | -44.62343 | 2025-09-04 03:36:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 247deda4-4702-3bd7-9c43-2c1c085f167d | -6.25999 | -45.09164 | 2025-09-04 03:36:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| bd885f49-6059-3661-be9e-e9919c8855a0 | -6.77839 | -44.09019 | 2025-09-04 03:36:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| db145f7d-67aa-349e-99d1-ad50d979bc42 | -6.70863 | -44.1804 | 2025-09-04 03:36:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fe25212f-1587-37a8-9f58-b7a8c1c26246 | -8.02857 | -44.05823 | 2025-09-04 03:36:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 968eb2a8-45d3-3d50-bf50-3dad7431c008 | -6.77918 | -44.09 | 2025-09-04 03:36:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 12e36913-1519-3126-ae86-578d15043fd8 | -7.92617 | -44.93153 | 2025-09-04 03:36:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9871b0b0-179b-333e-8be8-fe39646e28d3 | -6.27635 | -43.85577 | 2025-09-04 03:36:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9011dd1d-2675-3da7-a683-ab6e2157bc1b | -7.92315 | -44.93202 | 2025-09-04 03:36:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f949059d-d711-33fb-b762-5e69f49fe856 | -8.66609 | -36.22676 | 2025-09-04 03:36:00 | NOAA-20 | IBIRAJUBA | PERNAMBUCO | Brasil | 2606705 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| add260cc-6e36-36cc-bf59-43283d0204dd | -6.88289 | -44.24072 | 2025-09-04 03:36:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 17199093-93e8-3c74-b7d8-0626ec266279 | -8.36837 | -39.38707 | 2025-09-04 03:36:00 | NOAA-20 | CABROBÓ | PERNAMBUCO | Brasil | 2603009 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| afec9e1b-c34d-3b21-8bfb-88c2a9bca797 | -8.61113 | -40.31005 | 2025-09-04 03:36:00 | NOAA-20 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 2.9 |
| b1b7aa7d-4767-3d1c-854f-f91d647d8af7 | -10.97557 | -46.83387 | 2025-09-04 03:36:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 59dc03c0-e51f-382f-810e-7739edf945e0 | -11.03639 | -45.1411 | 2025-09-04 03:36:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 4fd49f03-1fdf-3e14-bb5a-c4c214980aea | -10.97574 | -46.84317 | 2025-09-04 03:36:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 639d53ad-6204-3792-a6e9-3925614014d9 | -11.04699 | -45.14764 | 2025-09-04 03:36:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 376bc0e2-bedc-3e1d-9a5f-bfe4446f3a2b | -9.43233 | -48.09604 | 2025-09-04 03:36:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 110e5067-3986-3637-8dcc-e0672417e375 | -8.03722 | -44.1386 | 2025-09-04 03:36:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f7e3bdd8-d15a-39b3-80f4-191c881ea1bd | -8.0747 | -45.34798 | 2025-09-04 03:36:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ea0ffa25-483a-302f-8326-643004a3369e | -8.43521 | -45.05233 | 2025-09-04 03:36:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f5617664-f9e6-391b-af7c-68a75979f1aa | -8.09216 | -42.42619 | 2025-09-04 03:36:00 | NOAA-20 | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 456de105-4c23-3f7e-9567-0eabbabe321d | -8.01822 | -44.14668 | 2025-09-04 03:36:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 48a7d947-329e-37cf-8ce4-73c56a8af698 | -8.03031 | -45.38366 | 2025-09-04 03:36:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| b445ff27-ac64-36e8-854e-47923f837fbe | -10.14482 | -46.25585 | 2025-09-04 03:36:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a5f83e53-2af4-3929-9367-f327528e0c9e | -6.54605 | -42.95825 | 2025-09-04 03:36:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 971234fb-ae03-3a67-96a7-5f84bc3c02dd | -11.0568 | -45.40711 | 2025-09-04 03:36:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2e026910-94b6-3eb2-9f7a-687228bfe5d5 | -6.86977 | -45.57935 | 2025-09-04 03:36:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 80cd4e49-d5c4-320b-8b89-bf73f9c0b669 | -6.88221 | -44.24441 | 2025-09-04 03:36:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 18001052-9f6d-38e4-aad0-9df828429680 | -7.07548 | -46.20013 | 2025-09-04 03:36:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9880207d-3ffc-3b2b-8dca-68d5c48ab9a4 | -11.05711 | -45.40245 | 2025-09-04 03:36:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5b94ff12-ec2f-3f0d-a191-eb31dd41944b | -9.52722 | -40.32653 | 2025-09-04 03:36:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 40b3734e-7190-38ed-8b42-494045cb4952 | -11.0576 | -45.40294 | 2025-09-04 03:36:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1159cdee-97e9-38cf-88e2-1597b1d0c477 | -8.02435 | -44.04956 | 2025-09-04 03:36:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 95c41fad-45c8-3edc-a03b-5cbdeb006f26 | -8.03043 | -45.38277 | 2025-09-04 03:36:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| fd4d0f02-ca3e-3c87-9ef9-4ec3ae0ef50b | -10.05516 | -46.23101 | 2025-09-04 03:36:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ecf7edf0-737b-31e6-9b56-df83677f32a5 | -9.05904 | -46.99152 | 2025-09-04 03:36:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2ba4da20-d8b3-3761-b2f9-b68686cbc8cd | -5.89665 | -45.96233 | 2025-09-04 03:36:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8de859ad-61fa-342a-aef1-8b845433b391 | -10.98453 | -46.83246 | 2025-09-04 03:36:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a99ab09f-1be9-3af6-98cd-15784b0bb78a | -6.77769 | -44.09417 | 2025-09-04 03:36:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 19f3cd92-bcd8-35b5-92ba-2701f4e3b93e | -8.07561 | -45.34299 | 2025-09-04 03:36:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 76221502-38d6-3ae8-9451-0e8cfb171f2c | -10.05735 | -46.23071 | 2025-09-04 03:36:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 63bce974-5b14-38e5-9624-63b8e8024caf | -8.88976 | -45.78598 | 2025-09-04 03:36:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| be581eaf-2dec-3891-ae80-dfb93347a354 | -9.52866 | -40.31841 | 2025-09-04 03:36:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 50a67327-a4ea-3bc9-9ebc-997e98e73a0c | -8.08494 | -45.36234 | 2025-09-04 03:36:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c6f3df54-8b52-306c-89c0-4378358f6eb1 | -6.77059 | -44.50028 | 2025-09-04 03:36:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3fb69432-28c7-3d68-8d7a-c37f9829c2b2 | -11.95923 | -45.78262 | 2025-09-04 03:36:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 777202dc-706c-3a63-8f7b-00f7ee95aca1 | -6.54663 | -42.9549 | 2025-09-04 03:36:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| aaa1b10c-07a0-3926-ac60-e41a9ee9df23 | -6.25831 | -45.09335 | 2025-09-04 03:36:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 2cb54ac7-1096-3fc0-9e17-df9e895cfb57 | -8.86917 | -37.0299 | 2025-09-04 03:36:00 | NOAA-20 | BUÍQUE | PERNAMBUCO | Brasil | 2602803 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| de035657-af3b-32ee-ae63-8bdbe0eeb89c | -8.02387 | -44.14773 | 2025-09-04 03:36:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 50dc190a-a5af-3195-a767-e6bd9f38bdc8 | -10.99181 | -45.9169 | 2025-09-04 03:36:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 76c75363-1176-3eab-9041-6a69289bc38d | -11.97504 | -45.79487 | 2025-09-04 03:36:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e3a8f549-2aaa-3bb6-be00-4904137bf072 | -11.05268 | -45.14895 | 2025-09-04 03:36:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 65a81fec-a42e-3c52-a466-78198be3a9a2 | -7.93646 | -44.94234 | 2025-09-04 03:36:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| b27229c4-bdb3-3e22-bb15-8c710db984f9 | -9.04114 | -47.0126 | 2025-09-04 03:36:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c98b97cc-3c55-3577-8ccb-b56bec3b0de3 | -6.48929 | -44.10432 | 2025-09-04 03:36:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 2e062b4a-d0b5-31d4-b4c2-247c895742d6 | -7.63556 | -46.56267 | 2025-09-04 03:36:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6536514e-e53a-3ddb-a789-13718a0906b6 | -7.04756 | -43.26831 | 2025-09-04 03:36:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 57c536ff-887a-3acb-a004-e888227c7dc2 | -10.13951 | -46.25008 | 2025-09-04 03:36:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c4d39533-188c-36ce-82a4-2866e9a5e26e | -9.61339 | -47.03745 | 2025-09-04 03:36:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ad82fce9-cebe-3fad-be64-0a9c706ca111 | -8.07485 | -45.34893 | 2025-09-04 03:36:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 196f3ed4-a591-3276-8580-848d862e1bd5 | -12.15823 | -43.70779 | 2025-09-04 03:36:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6c3f9c30-0db9-3979-8a7e-28af72915a40 | -7.93218 | -44.93233 | 2025-09-04 03:36:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8506eeb7-08cf-391b-a131-28774f2890b5 | -9.47884 | -47.61037 | 2025-09-04 03:36:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6ce6c7f7-2ea0-364b-a049-6e31854f0308 | -9.6424 | -46.11988 | 2025-09-04 03:36:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 44268f52-a1ae-3615-9adc-82544b64856b | -9.4912 | -47.61937 | 2025-09-04 03:36:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9e90c771-83f3-32d5-8d23-642c264e9d2b | -6.72957 | -42.2775 | 2025-09-04 03:36:00 | NOAA-20 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| cecfa7ba-0c09-39e8-a1f2-bb3e0e58d887 | -6.70797 | -44.18404 | 2025-09-04 03:36:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 62b9fc9c-dfeb-370b-a569-7413ff3fe9c5 | -6.81152 | -44.464 | 2025-09-04 03:36:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3698d0bf-8a7a-3112-83e4-2bdfa103fa18 | -10.97685 | -46.83772 | 2025-09-04 03:36:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 26fff7c4-b807-32ed-8aee-32b1921dbc61 | -6.70728 | -44.18784 | 2025-09-04 03:36:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cf97000b-edaf-32c5-be3f-75b1c634fe51 | -8.47523 | -45.06863 | 2025-09-04 03:36:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ff2aac00-a3e4-3f19-a61f-4fca27aabd1f | -6.78601 | -44.44854 | 2025-09-04 03:36:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b3989af0-9a62-395b-a93e-25ebd5850d7a | -11.02987 | -45.14409 | 2025-09-04 03:36:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 36.5 |
| 207a84da-ab19-3de7-b3ac-e9295cdfadc4 | -6.72982 | -42.24609 | 2025-09-04 03:36:00 | NOAA-20 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 08f0e438-fd3c-3842-805c-44d4eb22fef0 | -6.78345 | -44.09515 | 2025-09-04 03:36:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| e1e7056c-2e60-3432-a15a-8be6647ff36c | -6.72935 | -42.24874 | 2025-09-04 03:36:00 | NOAA-20 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 8719afd7-d913-38e4-afd4-83056b5fd5ee | -8.02456 | -44.14392 | 2025-09-04 03:36:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| adb1c84a-3e8e-36e6-8a0c-dacdaa93ca85 | -6.40741 | -43.26764 | 2025-09-04 03:36:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6de7a881-2f59-31f3-b624-20683a355ee3 | -8.90232 | -45.87815 | 2025-09-04 03:36:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 00595c0e-fc38-3fe2-b30c-abaac95ee774 | -7.04152 | -43.27086 | 2025-09-04 03:36:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 7d0e1c2c-6e47-3a1f-afce-47b8f9259a3e | -5.90424 | -45.9577 | 2025-09-04 03:36:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c63801ec-f1ad-316e-9927-b32de73829ef | -9.53293 | -40.31918 | 2025-09-04 03:36:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| f9a2df3c-7fa8-37eb-b876-d16ff7624c87 | -9.06566 | -46.9928 | 2025-09-04 03:36:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d6cde628-c56c-30fc-9ad3-7c012aad80d8 | -6.73015 | -42.27417 | 2025-09-04 03:36:00 | NOAA-20 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| b6c520e9-fef2-3423-9943-2f3777d96500 | -9.39168 | -40.31392 | 2025-09-04 03:36:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| f8f48573-1610-3902-a404-5c1d943cbe78 | -10.64986 | -44.84675 | 2025-09-04 03:36:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5ce89dec-69a6-3406-9fce-c21c43111fa9 | -11.96009 | -45.77834 | 2025-09-04 03:36:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8abf09c5-5aca-324b-b70b-fea00b9a6686 | -11.90909 | -46.65407 | 2025-09-04 03:36:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4ed21e20-ec12-3307-a346-39946c52498c | -8.36741 | -39.38641 | 2025-09-04 03:36:00 | NOAA-20 | CABROBÓ | PERNAMBUCO | Brasil | 2603009 | 26 | 33 | nan | nan | nan | Caatinga | 0.6 |
| df962e98-af43-3467-bd7f-1e21751e5a40 | -6.84921 | -44.26077 | 2025-09-04 03:36:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 226be64a-746e-3579-a911-d79261a13f86 | -6.30093 | -44.15601 | 2025-09-04 03:36:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 64a1bde4-ba21-3638-9028-51b3084f93db | -7.72239 | -44.61963 | 2025-09-04 03:36:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f894b292-cadb-373f-a7cb-73c7683777bf | -8.89597 | -45.85458 | 2025-09-04 03:36:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ed5ca4ef-da83-34fa-a7f3-11e94818fdeb | -8.07894 | -45.36065 | 2025-09-04 03:36:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c5fb6a06-5456-3aef-b601-4091f65e1d22 | -8.03129 | -45.37816 | 2025-09-04 03:36:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 7.5 |
| a230367e-3002-3796-b72d-e14f41fa857b | -11.13408 | -44.63849 | 2025-09-04 03:36:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 09141134-3eef-3c52-95c1-c75149d4a441 | -11.13337 | -44.64213 | 2025-09-04 03:36:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README20.md)
