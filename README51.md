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

## Dados Diários - Página 51

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 467b590e-5de6-3fe4-8944-ecd2214d2ca2 | -10.2487 | -44.0322 | 2025-10-18 04:29:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c4e6cbbd-4cf3-397d-839f-d55456a7bf55 | -5.16251 | -46.26763 | 2025-10-18 04:29:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d11cc0a8-0eca-3267-8ed6-aa3466f49b5c | -8.11861 | -55.08827 | 2025-10-18 04:29:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 57228abe-38af-344f-a13f-251eced4a5f5 | -5.5636 | -46.3669 | 2025-10-18 04:29:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a97f30b4-596d-362e-86c5-eb0370bddd27 | -5.36172 | -45.56722 | 2025-10-18 04:29:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a3d9f45c-25b1-3fc2-8286-b5d8e1492699 | -5.36436 | -44.93744 | 2025-10-18 04:29:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 54bd114f-3c1b-3187-b012-c125ac294f16 | -6.237 | -44.14854 | 2025-10-18 04:29:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 12464e3d-a8dc-38bd-a4d9-8a4631a0c37c | -6.60878 | -44.21844 | 2025-10-18 04:29:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e6cbb3b7-ea79-3a11-b8ac-d2680ef028d1 | -6.64377 | -48.80782 | 2025-10-18 04:29:00 | NPP-375D | PIÇARRA | PARÁ | Brasil | 1505635 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7f534a25-48d5-38fb-b7f2-e0a43d9defee | -4.99009 | -43.8581 | 2025-10-18 04:29:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6d7b7c08-6cd7-3049-a895-3f2c23b8922e | -8.27882 | -41.44998 | 2025-10-18 04:29:00 | NPP-375D | SÃO FRANCISCO DE ASSIS DO PIAUÍ | PIAUÍ | Brasil | 2209658 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| cacca51a-af65-3b66-8cac-57e2e54f219d | -10.68781 | -44.5521 | 2025-10-18 04:29:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 167d51ca-9579-31e3-8e80-7c3d76d62c86 | -6.87568 | -44.68291 | 2025-10-18 04:29:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1f1188c5-d41f-33a1-8e08-dcc51abca845 | -9.85541 | -51.39676 | 2025-10-18 04:29:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c97e85f4-e442-3828-b0f8-e34fca5023d2 | -6.87236 | -44.38428 | 2025-10-18 04:29:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e87231ff-a784-3e58-818d-0ee97d24e105 | -8.86019 | -46.01025 | 2025-10-18 04:29:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| df4dd4d3-1d94-358a-9d80-f4dc91c3a484 | -8.36398 | -46.2392 | 2025-10-18 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cb5f4bb6-e990-3be3-b0b8-e462ca8bb54a | -7.70994 | -47.85451 | 2025-10-18 04:29:00 | NPP-375D | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 952fb351-342b-3a42-bc2b-99be72bf5437 | -8.09734 | -45.44592 | 2025-10-18 04:29:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a962910d-a57a-3b5c-b010-60c715bb6b29 | -6.5932 | -44.15778 | 2025-10-18 04:29:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e297ed4b-b44e-346a-b77d-0bbea8dee945 | -10.17932 | -44.53145 | 2025-10-18 04:29:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 946c274e-d487-3e28-9957-63108b44887a | -5.92972 | -47.31849 | 2025-10-18 04:29:00 | NPP-375D | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 88f1fb8f-b691-342c-9edc-59f4fca9f946 | -6.24506 | -44.97045 | 2025-10-18 04:29:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 63ac34a6-ed1e-3f52-a4c3-3f5a52d89bb8 | -7.99505 | -45.15639 | 2025-10-18 04:29:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9c3583c8-eab0-3c70-8732-01058adc9c3d | -6.52683 | -41.49311 | 2025-10-18 04:29:00 | NPP-375D | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 4058eb66-ab33-37f3-8667-528fc30cb15e | -7.11912 | -44.79816 | 2025-10-18 04:29:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 463cba98-c3d3-35b7-b2f5-fdb96ef0b0d1 | -8.38894 | -46.23244 | 2025-10-18 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| f2c9de2b-9ed1-3bdc-9ae8-72b87ae1f390 | -6.23067 | -44.14365 | 2025-10-18 04:29:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bdb72bd8-1fd3-3abc-a494-35471b435e0b | -10.26221 | -44.06689 | 2025-10-18 04:29:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 47614c39-d29b-35df-bb9a-70652e7f1bf1 | -9.28744 | -46.88012 | 2025-10-18 04:29:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d60c23d2-3230-3322-bde1-4e2b50e90708 | -6.13428 | -44.21731 | 2025-10-18 04:29:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a78254da-ed1f-3b9d-b0e1-886d35d498f8 | -10.71393 | -44.54769 | 2025-10-18 04:29:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 08cd025c-0534-3d48-9699-c582bf9e1706 | -6.52762 | -41.48792 | 2025-10-18 04:29:00 | NPP-375D | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| bc7e04d8-d898-335b-8caa-f8cda1e5481c | -10.24804 | -44.03656 | 2025-10-18 04:29:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 064cfff4-bad8-3125-9467-6b5970fec786 | -5.92355 | -45.43712 | 2025-10-18 04:29:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 28e05f4d-c599-36c0-a8c0-3d9ff3735aab | -10.23592 | -44.0432 | 2025-10-18 04:29:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| f9a9430e-1223-3c3e-a287-1483f9949eb3 | -5.92689 | -45.43764 | 2025-10-18 04:29:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2724f021-1d74-3773-b591-dfa26f07cdd4 | -5.69332 | -44.4332 | 2025-10-18 04:29:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dbfe0e1e-0d96-35ea-afa8-531417fabec3 | -6.59493 | -46.6904 | 2025-10-18 04:29:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c15916de-2362-3dd4-ad95-0a658d8d97f7 | -8.55519 | -50.08175 | 2025-10-18 04:29:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bbc910a9-ad97-31b5-8df5-c7c8e5055997 | -10.43186 | -45.01406 | 2025-10-18 04:29:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ea186434-67b3-3490-946b-903d2e6517bf | -6.11206 | -44.85847 | 2025-10-18 04:29:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 86e6301c-5ef2-3988-9954-59fcb16f6142 | -10.14682 | -44.58507 | 2025-10-18 04:29:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3bf8a8fe-4566-3e0f-875f-6391fb3ac961 | -10.25676 | -44.07878 | 2025-10-18 04:29:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e3e6ee7d-ff40-307e-a99f-9d97916da790 | -9.72155 | -44.56467 | 2025-10-18 04:29:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 352e7326-1dae-3c83-aa3b-465c599df1e8 | -7.76188 | -42.48454 | 2025-10-18 04:29:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 794a1b13-1980-3b54-a703-fdc21993cec2 | -10.98402 | -44.31939 | 2025-10-18 04:29:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 686b8135-96d2-3305-932b-8c397c57edc6 | -10.16172 | -44.53447 | 2025-10-18 04:29:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| ec7368c6-157a-3561-9bfe-e94eeb25b7ee | -4.43679 | -50.55056 | 2025-10-18 04:29:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| df653751-7796-379f-a02d-e8fa3c349590 | -7.47262 | -42.74366 | 2025-10-18 04:29:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 2f737111-97e9-339c-86d4-8423841a9871 | -4.57018 | -48.40033 | 2025-10-18 04:29:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4bb188e4-a6d3-3892-9b4b-69226e437eed | -10.48066 | -47.74098 | 2025-10-18 04:29:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3206ff79-a6ef-3dda-8065-55e3830fea21 | -10.80835 | -44.01968 | 2025-10-18 04:29:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 523add8f-039b-3855-91db-66d9a70ed830 | -10.80978 | -43.93227 | 2025-10-18 04:29:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e049865c-b8ec-3e59-9a2e-e913c1af6a2a | -8.23328 | -44.00249 | 2025-10-18 04:29:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2df5beea-4fcd-3768-abd1-69375efbd9ae | -10.36571 | -48.66975 | 2025-10-18 04:29:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 52ce16e1-c753-3eb7-8aa9-404afb6acc2d | -8.7933 | -40.43556 | 2025-10-18 04:29:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 390a4c14-f6cc-3d51-b57f-980c88710ca4 | -6.3811 | -43.32621 | 2025-10-18 04:29:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9a0146b1-7109-307a-a423-e9fdd2fbea85 | -6.5961 | -44.16208 | 2025-10-18 04:29:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5ba507b0-f6cc-3666-88df-1423774f8144 | -8.09398 | -45.44536 | 2025-10-18 04:29:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 0c8bdcfc-74cb-3578-9fcf-59e7fff536ea | -6.36898 | -45.78265 | 2025-10-18 04:29:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 81eac26a-962a-30eb-ace3-1fd4617d627b | -10.10797 | -44.55513 | 2025-10-18 04:29:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fc0aae1b-9a32-31b8-b74f-9a31f0d1003d | -9.61245 | -49.02344 | 2025-10-18 04:29:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f24d0f2b-27c6-330e-ae11-adbaeb530799 | -8.44902 | -44.1728 | 2025-10-18 04:29:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 860cc659-251e-33b4-a6e2-1ff9b88262ac | -10.17613 | -43.89455 | 2025-10-18 04:29:00 | NPP-375D | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c97a3138-3274-3b93-95e6-17b667a69198 | -7.7657 | -42.48515 | 2025-10-18 04:29:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| e593e3fb-204a-3c00-bb13-f55f33e67e24 | -9.91821 | -47.65722 | 2025-10-18 04:29:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 9ccf9c18-dead-3ceb-a3d1-859add0586dc | -9.64774 | -48.72276 | 2025-10-18 04:29:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8f583697-11bc-3684-abfa-f6db2231467b | -9.90393 | -47.62626 | 2025-10-18 04:29:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4168509f-1b9b-32ae-a34e-b7f4801306fb | -8.82483 | -50.05444 | 2025-10-18 04:29:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1ee10c1a-35c6-345c-b2a1-7bfc7fc50654 | -4.97312 | -48.36262 | 2025-10-18 04:29:00 | NPP-375D | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 51e4fa7a-ef6d-33e1-a2df-6b419151bf7e | -5.01793 | -46.02859 | 2025-10-18 04:29:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 50d62422-a225-3e00-a388-17e27351f298 | -4.81151 | -45.70559 | 2025-10-18 04:29:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3068037e-fa06-38b5-a3c2-067ee9bb6c68 | -8.94364 | -46.57457 | 2025-10-18 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 82038fb7-f9dc-3c99-a286-49005df1c05d | -10.24314 | -44.04446 | 2025-10-18 04:29:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 7e886121-af25-3ddb-b474-f130fb08937f | -5.30817 | -44.84868 | 2025-10-18 04:29:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 435ece52-b2d7-31c2-8660-ce36d0d9448f | -8.82718 | -49.68611 | 2025-10-18 04:29:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| da841e02-6728-3a06-9b6e-cb1099c6ad10 | -4.93457 | -49.76401 | 2025-10-18 04:29:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1352526c-d66a-3cf2-843e-7b898146d358 | -5.01571 | -46.02115 | 2025-10-18 04:29:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 31.4 |
| 1cf85cd6-fc0a-3b8f-bfd9-aa4f33f26eed | -8.04484 | -41.10257 | 2025-10-18 04:29:00 | NPP-375D | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| cabdcab3-a0d1-3e1d-91a7-1009f6a079a3 | -6.30461 | -44.72035 | 2025-10-18 04:29:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d74efff2-f864-36b5-9d05-c30e65cf65d8 | -8.20737 | -46.92965 | 2025-10-18 04:29:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f7f880e4-179a-3e12-89c7-aa4f69925384 | -7.71052 | -47.85093 | 2025-10-18 04:29:00 | NPP-375D | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 020f5fb6-e0a0-36ce-a191-82a92c2fd17b | -8.54673 | -44.57698 | 2025-10-18 04:29:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 336292c1-d215-37c2-a2b2-16924839f9c8 | -9.13873 | -46.66689 | 2025-10-18 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f73b34ec-7884-3246-a56b-7a1bb69697ba | -9.72215 | -44.56073 | 2025-10-18 04:29:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| c2787a96-aaaa-3888-8184-dba912bba668 | -7.08309 | -44.2561 | 2025-10-18 04:29:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e05b2b28-5c87-3717-8ea7-4f8a0aeb25b5 | -5.89999 | -44.24345 | 2025-10-18 04:29:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4ed6b225-3877-35a7-8480-bad103c324d1 | -10.70203 | -44.55423 | 2025-10-18 04:29:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| aec8fbeb-7e15-3f96-b5c6-81e8bdae9c99 | -5.75238 | -45.85648 | 2025-10-18 04:29:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 34dc28b4-9705-3a08-bf99-afb147b38877 | -10.4993 | -47.53832 | 2025-10-18 04:29:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d2abe272-4da1-3f3f-9587-fee54c66ac0e | -6.3348 | -44.00998 | 2025-10-18 04:29:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 71635612-86d7-31cb-a8dc-86ab9dcf3400 | -6.83476 | -42.42291 | 2025-10-18 04:29:00 | NPP-375D | CAJAZEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202075 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 1c48f8ce-a3b6-366f-b2e4-bea24f659954 | -6.40796 | -41.48342 | 2025-10-18 04:29:00 | NPP-375D | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| e28e429e-cb38-3c74-b326-e93128d0e351 | -7.89501 | -55.4272 | 2025-10-18 04:29:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 144aea2c-cba6-38be-906e-d88cedf79802 | -4.99414 | -43.85487 | 2025-10-18 04:29:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 089a93de-0bc9-3b6d-9371-2568ba6eb2d9 | -9.66939 | -48.5266 | 2025-10-18 04:29:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1a8c1eeb-de42-394e-8881-a8e7e60967bb | -5.33972 | -44.99945 | 2025-10-18 04:29:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e136d07d-ddb9-3eaf-8d12-dcae33079642 | -8.16534 | -47.02675 | 2025-10-18 04:29:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4d05fa0a-5d80-3eef-9326-1b2fdb84a65b | -6.52997 | -44.90785 | 2025-10-18 04:29:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README52.md)
