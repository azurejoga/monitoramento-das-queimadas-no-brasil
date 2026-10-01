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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a247c64b-993c-3341-ac27-0bd8ce3bed0f | -4.29057 | -50.80712 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 2713af4e-7725-379e-8548-8f8e538e6144 | -4.2639 | -50.77779 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 28993fe3-1e23-378f-985d-5debd6a9ffd8 | -11.25917 | -43.52717 | 2026-10-01 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 82cd4457-7a0e-359c-aaee-195305620f9c | -6.3884 | -45.80943 | 2026-10-01 04:14:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f93bc26e-e7c2-33a3-92d3-45eb2e8b707a | -4.29487 | -50.75741 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 0ac5d800-aa9a-3ff2-b34e-c9f723f099c8 | -4.27183 | -50.74343 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 64c50fd7-45da-3e2e-8dd8-7b1fe8be5f67 | -12.20102 | -43.8324 | 2026-10-01 04:14:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7483b291-0f7f-3ba4-8c54-d2487eff3dac | -7.03234 | -50.73199 | 2026-10-01 04:14:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dfabae2e-29a9-3f65-9111-8e4598fcd466 | -8.96496 | -44.17438 | 2026-10-01 04:14:00 | NPP-375D | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 38ecf75e-aef3-3471-bf27-90ceb55c2bed | -11.1461 | -49.05075 | 2026-10-01 04:14:00 | NPP-375D | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b1967abc-425e-372f-861a-f934f3ee02ca | -8.36465 | -45.49924 | 2026-10-01 04:14:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1c322e98-45ad-3eb3-9415-b2cab9ae195c | -11.63048 | -43.48704 | 2026-10-01 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9972972e-0725-3073-9522-e250de9cb4a6 | -8.85095 | -44.3924 | 2026-10-01 04:14:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 02bb6a15-da38-38cb-a70c-07cc65b14799 | -4.28845 | -50.7474 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c903f41f-8612-363f-a05f-645931a22b91 | -11.40586 | -51.0295 | 2026-10-01 04:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ab04d927-2ba9-321f-be09-209b8779b400 | -5.42086 | -44.02916 | 2026-10-01 04:14:00 | NPP-375D | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2c8ae35f-32ce-3eb1-a575-7bde19c21f03 | -11.415 | -50.97268 | 2026-10-01 04:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fac3aef6-0a2a-3595-8ecd-05cd650539b6 | -4.29822 | -50.76408 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 2270e291-eec5-39cd-a72e-6cafb33ee25d | -4.2842 | -50.74542 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 4ef0b18a-564a-33ab-9a63-2bb2283f3767 | -4.29044 | -50.82083 | 2026-10-01 04:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 5104cb9d-8233-3d42-af91-5fe3748de8df | -4.28869 | -50.75634 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 4d461b93-a32d-317f-af44-0bbdf53a5673 | -10.85262 | -48.68645 | 2026-10-01 04:14:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7d64c7db-55bf-3b0d-bbef-85a2638e413b | -8.21039 | -45.47308 | 2026-10-01 04:14:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ddf2f0de-1422-3c49-bc45-3fdc109eff45 | -4.28467 | -50.77987 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1485.3 |
| d0441de0-eddd-309b-845c-56df6354470f | -11.68592 | -43.50365 | 2026-10-01 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d2c5e646-72ad-3aac-95a2-ce8cdabb4a8e | -8.2058 | -45.49918 | 2026-10-01 04:14:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8ac9cedf-7a16-3a7b-bcdf-5b83fd6130ee | -5.44957 | -44.53844 | 2026-10-01 04:14:00 | NPP-375D | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f0fc8c49-aa6e-3d28-9dc7-caada7f5f151 | -7.6078 | -44.55567 | 2026-10-01 04:14:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 249f8fe3-d08c-3aef-9ab5-e594c2c5da0a | -5.08794 | -45.78734 | 2026-10-01 04:14:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ce6d0d78-7cef-33f2-8091-bb7a41e75f21 | -4.31343 | -50.78616 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| adfd61df-1fec-3abd-b2ab-24922647500d | -5.75484 | -45.15564 | 2026-10-01 04:14:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 9307fc8a-9eb3-3f96-b271-7c0c1b418f3a | -8.20714 | -45.49156 | 2026-10-01 04:14:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5203be75-1bc8-3f37-a910-907b77cc3675 | -4.30022 | -50.76336 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 4d7ed279-174a-3078-9de0-509446f9fd6a | -11.44725 | -43.43723 | 2026-10-01 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ea05c635-42e4-3bcd-91f8-9a3bf2da8923 | -8.20657 | -45.50293 | 2026-10-01 04:14:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 13df6075-facb-38bc-a0ca-93bd414db9b6 | -7.6126 | -44.55352 | 2026-10-01 04:14:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f7f93bae-24e8-339b-9952-ea1de3e15610 | -9.78927 | -44.81285 | 2026-10-01 04:14:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bcd298d8-c217-33f7-ae2a-bd63bf08523b | -4.30358 | -50.76978 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 9441d0ee-2994-3912-9427-c07885c058bd | -7.5023 | -45.83335 | 2026-10-01 04:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e689003f-8a59-3b1b-9dfa-c647134313e9 | -5.32577 | -47.47342 | 2026-10-01 04:14:00 | NPP-375D | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 01b0b2d8-765d-35d3-85c0-fdc772dc41f1 | -10.65893 | -50.75895 | 2026-10-01 04:14:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fe82db48-5827-373c-9977-09d4ce4e18a2 | -4.30214 | -50.81392 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| dd934177-6810-3cf7-bea4-aa29f2431cbd | -4.25783 | -50.82468 | 2026-10-01 04:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4f909065-bdc6-3808-9b48-39002de72160 | -8.84438 | -50.50394 | 2026-10-01 04:14:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 857eae34-b708-3559-8ebf-8a6f0924607b | -4.26142 | -50.79161 | 2026-10-01 04:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a0e3cc9a-2986-3b4f-8dd8-5379c79934bf | -11.41622 | -43.40771 | 2026-10-01 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 3e60e2c2-56e6-3c9b-9a4c-7450118c15ea | -8.20517 | -45.50281 | 2026-10-01 04:14:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 99abb8ee-860c-320f-a1b5-ff9f594ce77c | -11.1906 | -45.19202 | 2026-10-01 04:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 843cc371-fbcc-3581-9b14-38149d8c9df9 | -8.32969 | -44.16018 | 2026-10-01 04:14:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 8.2 |
| ed6a0dc0-24c7-33c5-92cd-62a030d3237f | -5.76187 | -45.16473 | 2026-10-01 04:14:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0dd8a541-81c4-3a86-a9c4-19bfda9d4e27 | -8.13968 | -43.43276 | 2026-10-01 04:14:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2a5ea598-faca-321e-92ba-93f978872b03 | -11.61576 | -43.5534 | 2026-10-01 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 50488124-db13-39b0-8652-7c87ffc17b43 | -11.71179 | -43.4356 | 2026-10-01 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e212cc7d-4512-34dc-b1bb-8fb5dd050a70 | -8.37747 | -50.73235 | 2026-10-01 04:14:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0a09c17c-8568-3a62-94cf-ec04cbf4da67 | -4.27571 | -50.81883 | 2026-10-01 04:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| b472cbe4-f5ce-3d27-aaf3-41fcb7886460 | -4.25987 | -50.77586 | 2026-10-01 04:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 17bc700b-11e7-33b3-b1ba-b62dabb45b45 | -11.40658 | -51.02574 | 2026-10-01 04:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e70ec204-a4d2-324f-99f0-ec47305e5227 | -5.42584 | -43.45208 | 2026-10-01 04:14:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 8753d1cb-f975-34dc-9933-ec1b77786a6c | -4.27821 | -50.80481 | 2026-10-01 04:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 772c6e1a-22ac-3fea-b289-03ac5152b0bd | -9.77016 | -44.80949 | 2026-10-01 04:14:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5b1d2c70-46db-327a-8e7e-261efc0247f7 | -11.11405 | -44.59698 | 2026-10-01 04:14:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dbb3a750-8cb4-3830-a0c8-faab4865ae1d | -7.54154 | -47.12475 | 2026-10-01 04:14:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d114357a-a592-3a3a-8a35-f3fb0204dc42 | -9.12345 | -49.92173 | 2026-10-01 04:14:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9bb08d70-9f18-3b02-9dc1-acd144a84a2f | -9.80376 | -44.82022 | 2026-10-01 04:14:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| eafbc914-da80-3564-8e85-7c07504be810 | -11.46849 | -43.46112 | 2026-10-01 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 28df235f-a623-3d9a-8893-4154dd7fd2a8 | -11.19195 | -45.11435 | 2026-10-01 04:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ebab53fc-beb8-3143-a3a9-593997e1cd44 | -11.28512 | -50.97895 | 2026-10-01 04:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5bf2a914-830f-335c-bace-dff96965d8b0 | -11.45709 | -43.44299 | 2026-10-01 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 26.3 |
| 31b6ae0a-86c0-325f-b884-0ad5dbed1adc | -7.0263 | -44.63441 | 2026-10-01 04:14:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 066b393a-bc66-3c17-b116-9aaf955c9c8c | -9.87871 | -44.96787 | 2026-10-01 04:14:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5a55825d-1ed3-3c1b-88b0-15befce9f380 | -9.77781 | -44.81083 | 2026-10-01 04:14:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 34ca6caf-79df-384e-9eb3-be8a9e19ec78 | -11.45295 | -43.44631 | 2026-10-01 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 91e4bff0-29fa-3e79-825e-105d30028f14 | -5.75421 | -45.15939 | 2026-10-01 04:14:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| fdc37993-d99f-312d-87a1-41465e53f761 | -8.76165 | -44.91173 | 2026-10-01 04:14:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c097d3f3-f5e7-3ecf-8eed-6950bd657c30 | -6.91504 | -51.67425 | 2026-10-01 04:14:00 | NPP-375D | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a2ddb30b-f0de-3006-94dc-0a082aa15b47 | -4.29402 | -50.78771 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| a068b697-4e52-38ea-86bf-960b76cfb52e | -4.29635 | -50.73881 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8441024c-eb28-3584-8318-a68143e8a631 | -11.43718 | -43.4113 | 2026-10-01 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c4ebd6b9-1b39-3ac3-8701-22c28dd0d96c | -4.28786 | -50.76122 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| e3afd673-52d8-3897-b52d-2f681b57ee18 | -8.33033 | -44.15801 | 2026-10-01 04:14:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 5dbcb48c-c8b5-3e5a-89cc-8f9ce22d3d57 | -10.72375 | -45.32623 | 2026-10-01 04:14:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9a1acfc9-e4fe-30b4-abfe-50668e3e9ea3 | -12.50607 | -43.10289 | 2026-10-01 04:14:00 | NPP-375D | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 463074dc-7d80-3f0a-aad4-a9374b8b9776 | -11.16745 | -45.11977 | 2026-10-01 04:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 783b8c6b-e542-3660-a11e-d1438d0d6c89 | -8.62422 | -45.36862 | 2026-10-01 04:14:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8829fe52-d987-36ba-9a0e-fd79167ec31a | -4.45881 | -47.92396 | 2026-10-01 04:14:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| ab8c046d-6db5-3ec6-8d74-f969269b2c17 | -10.72459 | -45.32145 | 2026-10-01 04:14:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 781980b1-9e9b-3988-b8d8-26ef4c651468 | -4.30642 | -50.78973 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 83075a90-9c45-390f-be43-7f6873f451ac | -5.17493 | -46.19564 | 2026-10-01 04:14:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 40b036e7-840b-30fc-ada2-3f6e0b9dd233 | -11.44791 | -43.43331 | 2026-10-01 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 90ced9ca-83af-3495-b2ec-21c07d73f599 | -7.06545 | -42.29576 | 2026-10-01 04:14:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 7.2 |
| c7ac0dc1-b77c-360d-b217-1405d1f2364d | -6.01173 | -49.5612 | 2026-10-01 04:14:00 | NPP-375D | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 47835236-89f8-3f84-baff-2b17887d4b0f | -4.27885 | -50.73955 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0b8ea7bc-faa1-3c0e-a037-5d395049599f | -7.47246 | -49.5761 | 2026-10-01 04:14:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 372ec023-6e1e-349c-bbf3-8c92b97e0859 | -5.76436 | -45.14967 | 2026-10-01 04:14:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f93ea107-951f-35a4-955a-74f79d7b70ec | -4.25166 | -50.82338 | 2026-10-01 04:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8f64859f-b4f4-3f99-9507-094520604113 | -11.62501 | -43.49822 | 2026-10-01 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3c5c9a25-9375-3e02-9b94-a2c0623293dc | -7.07562 | -42.32116 | 2026-10-01 04:14:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 0b878cce-d5ec-3d63-a485-2f85c2dbe304 | -4.27973 | -50.80878 | 2026-10-01 04:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 1bbad9c9-0eaf-3419-bb70-9b079fef12b9 | -8.04071 | -42.86137 | 2026-10-01 04:14:00 | NPP-375D | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 68a1eeba-d2da-346c-ad46-c2e799c910c7 | -11.68166 | -43.50392 | 2026-10-01 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README38.md)
