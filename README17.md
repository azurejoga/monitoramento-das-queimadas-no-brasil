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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 657fa7fa-fc88-34da-a223-53735c89e0ec | -13.53159 | -44.85069 | 2025-10-01 03:30:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 391681bf-1f37-3992-bfd8-b086c0fb0823 | -11.38787 | -44.89646 | 2025-10-01 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 57078553-8e51-3a2a-b61a-85a22cb485df | -14.17735 | -46.12704 | 2025-10-01 03:30:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e0bb482e-96fd-3b4b-92cc-edfaf6d4c894 | -12.35699 | -43.21371 | 2025-10-01 03:30:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3155c6db-1fee-3c75-916e-1581d7337c88 | -11.98996 | -46.65841 | 2025-10-01 03:30:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4624a6a1-0c74-32b4-8dfc-43def2326189 | -11.98947 | -46.65845 | 2025-10-01 03:30:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9a248105-ef9f-368d-8f70-1b57ef3f3f17 | -12.77453 | -46.87735 | 2025-10-01 03:30:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0e9da0d0-7da8-3ac5-863c-b4dc42062550 | -13.37543 | -47.31207 | 2025-10-01 03:30:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 62977644-532e-36f3-a413-b4b694808fb5 | -8.53538 | -44.70673 | 2025-10-01 03:30:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 92bd8e0d-ab42-381e-949a-c03d14914060 | -8.57921 | -44.75756 | 2025-10-01 03:30:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2f05dbdc-a831-38aa-af04-dd5b5f859dc6 | -14.17872 | -46.12061 | 2025-10-01 03:30:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d9ea15f3-d486-381b-970e-5e388890b519 | -9.94852 | -43.58467 | 2025-10-01 03:30:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 171dfa82-5e1c-3785-ad3e-259c1d97339c | -11.43802 | -43.50403 | 2025-10-01 03:30:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f12521e0-3cc6-3792-b594-7fee56da8934 | -10.90921 | -46.56034 | 2025-10-01 03:30:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 15.2 |
| b2015dfe-1769-32aa-9f6e-f9e02fbc80af | -13.77519 | -47.97081 | 2025-10-01 03:30:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| a0427eca-915c-30f1-a729-53764aa6d671 | -11.42799 | -43.5018 | 2025-10-01 03:30:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6de30e6f-7487-38df-a0d2-ded72997e022 | -11.80769 | -44.9837 | 2025-10-01 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3307b91e-4ef3-3fa1-b706-9b469703a693 | -11.19347 | -47.20174 | 2025-10-01 03:30:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c788d59b-efca-35e7-93ef-273d90e7ae73 | -14.53783 | -41.66744 | 2025-10-01 03:30:00 | NOAA-20 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| c0db3993-85cb-3787-8de7-2c075f23a5e6 | -10.90719 | -46.53167 | 2025-10-01 03:30:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 045d1317-6256-3b6b-8afb-35480b481380 | -13.31139 | -47.21209 | 2025-10-01 03:30:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 23844415-15f0-3845-a212-fdfbb6beffa3 | -10.82566 | -45.37749 | 2025-10-01 03:30:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 537ac402-1765-3e09-9f8f-8c3805aa6ecc | -11.46266 | -45.00911 | 2025-10-01 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8f6354ce-13a4-3127-899f-dbffa0c9bd07 | -10.9269 | -46.50876 | 2025-10-01 03:30:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f5257d1d-718d-314f-b28a-7f876494dd6e | -13.65502 | -47.31229 | 2025-10-01 03:30:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 208c882e-e477-32fe-a62d-96f350e4a088 | -11.59792 | -45.05111 | 2025-10-01 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3b570bae-c2da-35d4-af3e-2d6c61c463b3 | -11.45407 | -45.08561 | 2025-10-01 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 20b50b3c-8f4c-3d80-ab0d-42327d898b5a | -9.93003 | -43.64864 | 2025-10-01 03:30:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0f413b23-2084-3bcd-9882-d95a65f3fbb8 | -11.13198 | -43.38129 | 2025-10-01 03:30:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 426ef054-3e9a-3b66-8aa8-107fe9acde69 | -11.45491 | -43.51566 | 2025-10-01 03:30:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ce34f370-261f-34d7-8c9c-305d81f0d3a1 | -12.75865 | -46.9175 | 2025-10-01 03:30:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3f802956-d2f4-3950-926b-f97576448efa | -13.21869 | -47.33879 | 2025-10-01 03:30:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 1cfebb61-0cf7-32ff-8886-44256711e15f | -10.81412 | -46.64298 | 2025-10-01 03:30:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| aa92960f-8e9b-338c-9778-bd6875161a1d | -13.77103 | -47.97527 | 2025-10-01 03:30:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 4fdac6eb-d066-3502-acd5-7d489273f4ca | -10.92642 | -46.50854 | 2025-10-01 03:30:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 412b1d50-1b41-3058-a46e-7bf1353ea072 | -14.19487 | -46.10728 | 2025-10-01 03:30:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e87e9e15-0427-396e-8b21-9d2d860696ba | -9.93676 | -43.64557 | 2025-10-01 03:30:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fa53ceb8-d812-3f13-9d92-363a63c2456c | -14.06497 | -44.37131 | 2025-10-01 03:30:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0adfabc2-4d01-392d-bc59-3aaac9a919d7 | -11.39413 | -44.89755 | 2025-10-01 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2e28be09-f42f-3d2a-b59d-25ed6248dc81 | -11.84577 | -44.98714 | 2025-10-01 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 8d56a728-6437-3037-a544-3566b5779b5c | -11.36697 | -45.06336 | 2025-10-01 03:30:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ce3d8a02-26ba-3c2f-ae06-b48001344f0f | -12.18219 | -40.41192 | 2025-10-01 03:30:00 | NOAA-20 | RUY BARBOSA | BAHIA | Brasil | 2927200 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| af52c28d-691c-333c-85e5-7919eb5fcf1b | -11.45692 | -44.97243 | 2025-10-01 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 75bc25f4-6fe8-3f88-958c-fd2e8a673543 | -11.28086 | -39.2229 | 2025-10-01 03:30:00 | NOAA-20 | SANTALUZ | BAHIA | Brasil | 2928000 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| be09b42e-b7b2-362f-b920-8916393f946e | -11.74272 | -46.87903 | 2025-10-01 03:30:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 66e41f5c-6520-38cc-ac9d-71a89083a0d9 | -14.05832 | -45.03711 | 2025-10-01 03:30:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 510859b4-9fed-3b6e-8ae1-e2413f534ee5 | -13.64782 | -47.31345 | 2025-10-01 03:30:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 54aa8e45-19c0-3755-b1d5-2381f7838637 | -13.76654 | -47.97619 | 2025-10-01 03:30:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 2e8ec602-2fe9-39c8-ab1b-bcd624387152 | -10.91133 | -46.51207 | 2025-10-01 03:30:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7cafe3a1-1335-3ae7-a373-9f9557b1fba8 | -13.37279 | -47.32972 | 2025-10-01 03:30:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 77c8409b-7044-3619-b39b-833a8f28d7f9 | -13.13946 | -47.41843 | 2025-10-01 03:30:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d6a89765-282a-3f00-b100-756c77a845e7 | -12.01527 | -46.63654 | 2025-10-01 03:30:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 546d2336-678c-35fa-8ef9-dde80c5634f6 | -11.81789 | -44.9654 | 2025-10-01 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 65039606-d827-331a-be9c-52b2a433b1a0 | -11.81888 | -44.9289 | 2025-10-01 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f81f2add-5e88-3055-a35b-9b7118a51154 | -11.51981 | -43.55313 | 2025-10-01 03:30:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 62439a8f-d98c-3c3a-8575-5a0dfa93bb1b | -12.84038 | -47.03638 | 2025-10-01 03:30:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0994abbe-65f0-32ef-a1aa-2307030dca26 | -11.80819 | -44.9915 | 2025-10-01 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b15f6897-ff53-37d0-aee1-5ca479c49b90 | -8.5536 | -44.71637 | 2025-10-01 03:30:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 3a5ab9a9-cc17-3e86-a323-5319dbbed482 | -11.19211 | -47.20805 | 2025-10-01 03:30:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5f3c29da-7e04-3236-a648-718a4ce29197 | -11.82802 | -44.97909 | 2025-10-01 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5204e846-d41e-3b41-887d-e8ff91a8bd0d | -9.93261 | -43.66706 | 2025-10-01 03:30:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 01811db4-c8ed-32b8-880c-dbd9b39f21ad | -10.90643 | -46.50363 | 2025-10-01 03:30:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8a9c1e9b-993b-3b93-a043-aa2c7f6ad61e | -11.38413 | -45.07553 | 2025-10-01 03:30:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e4dd9e86-6906-3688-9b62-ff67070ef24b | -10.77949 | -45.37284 | 2025-10-01 03:30:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e8afd535-1c51-3ad1-82b7-85f52554d6f3 | -13.15962 | -42.35759 | 2025-10-01 03:30:00 | NOAA-20 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 3ef0011e-9278-3d04-a035-a7891631f188 | -13.64632 | -48.03316 | 2025-10-01 03:30:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 97870abc-8bb3-3a33-b402-4415a8aad3c4 | -9.925 | -43.67461 | 2025-10-01 03:30:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c6e5e971-59f3-37d1-a9d0-5a7d060d2a8c | -11.44843 | -43.5184 | 2025-10-01 03:30:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6c6c9fcf-7d14-3077-8fe4-26324d46ebdc | -12.35174 | -43.21405 | 2025-10-01 03:30:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f81c5b8f-ebcf-3c61-b089-7bf6ce9d0d29 | -11.46229 | -45.09145 | 2025-10-01 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 943546c1-86e8-36ce-a28d-09272ecb5cff | -9.93177 | -43.67139 | 2025-10-01 03:30:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e3e409ff-259d-33fb-a55c-9ac3d2fd21ba | -10.9161 | -44.34159 | 2025-10-01 03:30:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b81e43d9-0637-33a8-8bd3-a11ab63de617 | -14.1915 | -46.1231 | 2025-10-01 03:30:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 12.1 |
| f2eac5bc-069b-3d81-819c-a20c3b743137 | -11.82505 | -44.99374 | 2025-10-01 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8e2ed583-92a4-369e-b344-821f299a462a | -11.8467 | -45.0146 | 2025-10-01 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9ba85435-20d4-3d4a-ac3f-aff24e3efe41 | -11.81898 | -44.99178 | 2025-10-01 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8500a2a2-a26f-3c98-9116-3b921b946a1c | -11.44979 | -45.02484 | 2025-10-01 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 826017b9-5450-3788-a8ea-b3559de7d6f4 | -11.81787 | -44.93384 | 2025-10-01 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b9f58127-45cd-31cd-9f84-9bfaa233299c | -13.76643 | -47.96217 | 2025-10-01 03:30:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 11.3 |
| dc64ad3b-c443-3bb1-a6d4-d1613d2d5fe3 | -13.32961 | -47.82626 | 2025-10-01 03:30:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2469fb83-315a-3886-8fa4-9b64faf40736 | -11.93955 | -43.9166 | 2025-10-01 03:30:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6f7dd3e7-2890-37a6-a137-e647e3b48636 | -13.33139 | -47.81806 | 2025-10-01 03:30:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 750e49ba-5a32-379c-87b3-dd6f5bde7227 | -11.81686 | -44.97046 | 2025-10-01 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 59cb0c79-e9f5-3065-8ca0-f5c9b73ac359 | -11.4636 | -45.10363 | 2025-10-01 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 13582ca1-428d-373e-8b46-cf0190016076 | -12.74469 | -41.82085 | 2025-10-01 03:30:00 | NOAA-20 | BONINAL | BAHIA | Brasil | 2904001 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| d0baf1aa-6568-3e1b-95a0-7e2368a77742 | -13.64402 | -48.03314 | 2025-10-01 03:30:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c2fcebd0-d830-3925-9c9b-a96c0cd876c4 | -13.765 | -47.9831 | 2025-10-01 03:30:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 4a342eaf-f469-37db-91a2-f7d7bacd72b5 | -14.16594 | -46.07897 | 2025-10-01 03:30:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ca395a4d-9350-3a13-a3c8-1f2a706ca167 | -11.09989 | -40.95834 | 2025-10-01 03:30:00 | NOAA-20 | VÁRZEA NOVA | BAHIA | Brasil | 2933158 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 25e8e8a5-9519-32c3-8afa-d3fd09056f99 | -15.46554 | -39.47712 | 2025-10-01 03:30:00 | NOAA-20 | CAMACAN | BAHIA | Brasil | 2905602 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| a9b5d4f7-4bb2-304c-b8ea-7925325e469b | -11.46327 | -45.08665 | 2025-10-01 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| e6fd604a-b678-37c7-95e8-f416625b94c6 | -11.20485 | -47.20423 | 2025-10-01 03:30:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 95f659e8-f5e2-3522-af78-7abc11673cd0 | -11.46323 | -44.97334 | 2025-10-01 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e50d1e51-fa5d-3ac6-9297-579826753233 | -11.46745 | -45.08408 | 2025-10-01 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 00a426da-5970-3dc8-99b6-645c0c20b0a6 | -11.47044 | -45.08354 | 2025-10-01 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| b8aa8164-5326-380c-939d-98f9c1d636ed | -10.90923 | -46.52504 | 2025-10-01 03:30:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fcd22c2f-fa93-36f4-94d5-bd7852766fb5 | -9.92753 | -43.66156 | 2025-10-01 03:30:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 11480927-e2e6-3324-bf3a-68747c037ac5 | -14.70068 | -42.3185 | 2025-10-01 03:30:00 | NOAA-20 | JACARACI | BAHIA | Brasil | 2917409 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 9512f4a2-c855-36fd-8847-16a1098ff9d2 | -9.93592 | -43.61823 | 2025-10-01 03:30:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 407d4008-1678-3ed7-a16f-34dc7046664d | -11.82098 | -44.98193 | 2025-10-01 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |


[Clique aqui para ver as próximas entradas](README18.md)
