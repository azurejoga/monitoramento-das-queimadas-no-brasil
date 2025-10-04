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
| 8e01ab2a-9ce4-32ab-94f6-eb9c86e8b44e | -8.9171 | -46.06431 | 2025-10-04 03:51:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 65e17c08-ca06-36d6-9b16-9df6a1c5ca48 | -6.04785 | -42.51875 | 2025-10-04 03:51:00 | NPP-375D | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 1f9d0aef-60ca-372e-be76-3483cfd8d22d | -7.54932 | -42.40396 | 2025-10-04 03:51:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e4b66f1f-b18c-38c5-b19b-d93fcf725b53 | -9.91134 | -43.71596 | 2025-10-04 03:51:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f413aa7d-d155-3fbb-a2bd-33508c9c7162 | -8.95554 | -48.69035 | 2025-10-04 03:51:00 | NPP-375D | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0cecf6ea-982f-370a-baf7-1e1680f32176 | -7.77468 | -42.60044 | 2025-10-04 03:51:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 6f773e01-e0f8-35a3-858f-db867e0375ab | -7.86387 | -48.1989 | 2025-10-04 03:51:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b5edcf2a-1842-3200-af86-873dfcfd6dbd | -5.24891 | -45.55311 | 2025-10-04 03:51:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4acc15e0-6d9f-3f0f-85d7-774f721e4d71 | -5.84366 | -42.88068 | 2025-10-04 03:51:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| b568dcd2-cf60-3338-a339-076af807b39c | -5.61114 | -43.22436 | 2025-10-04 03:51:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0c704dbe-fd30-3c23-907c-a1b57d5e154d | -6.94314 | -37.96378 | 2025-10-04 03:51:00 | NPP-375D | POMBAL | PARAÍBA | Brasil | 2512101 | 25 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 43ed8453-4ee9-3c3a-abeb-47b06708984f | -11.72399 | -44.44061 | 2025-10-04 03:51:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 10ce684c-8810-3fb9-aa68-8edb3e8949cb | -6.28489 | -45.07983 | 2025-10-04 03:51:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 86e2e88c-3cd7-3b1d-9e03-c3bab8181381 | -8.91114 | -46.05923 | 2025-10-04 03:51:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 76134dee-45c8-3dc3-9f4c-f2b4ffb3d55b | -8.17905 | -44.13954 | 2025-10-04 03:51:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6a229f9b-92d7-38cb-926c-ffcb056416a9 | -8.22835 | -46.8124 | 2025-10-04 03:51:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 92465fc5-5fc3-37e8-b5ca-b2063bf6783f | -6.64903 | -41.95247 | 2025-10-04 03:51:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 5dc6e09c-71fb-35b0-ac0d-d082f27496a9 | -7.80498 | -42.53136 | 2025-10-04 03:51:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| e37e9cae-cf9f-3169-aa2d-e116ccaaafaa | -6.27881 | -45.08473 | 2025-10-04 03:51:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b230a8b4-014b-36dd-a5dc-ab10fe583f45 | -7.71905 | -42.57518 | 2025-10-04 03:51:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 5e19ca13-264a-3188-bf23-8fc934686474 | -7.04884 | -43.22274 | 2025-10-04 03:51:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| ac0b7516-c77e-340a-a14d-dacc239e8e8f | -6.65165 | -42.80655 | 2025-10-04 03:51:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| ea204c43-8247-3be3-8aef-968fda9b8716 | -10.29639 | -45.18289 | 2025-10-04 03:51:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 4e8560ee-431c-37d2-a5ad-e207755507e6 | -5.85358 | -42.20798 | 2025-10-04 03:51:00 | NPP-375D | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 24985dd0-9da0-3aeb-b353-1e9ee55cc16c | -5.77113 | -43.61219 | 2025-10-04 03:51:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7987eb9c-84c7-3dfa-98ae-3c0fa994dc0c | -8.1994 | -46.99584 | 2025-10-04 03:51:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| baf9ba8c-f068-310f-9293-8ed6d4413258 | -5.84644 | -42.78529 | 2025-10-04 03:51:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 94bea411-5d04-3b41-9d9c-beb298acb75b | -9.76756 | -46.21226 | 2025-10-04 03:51:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6fff5d08-46c0-3a17-8224-7e661486f233 | -5.83423 | -42.88322 | 2025-10-04 03:51:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| acc2c08f-1fc0-3231-807f-c9a5ec2085ec | -9.94801 | -43.73581 | 2025-10-04 03:51:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 304df8fa-8744-3ff4-aa42-9b510ac96bb1 | -11.07705 | -47.88166 | 2025-10-04 03:51:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b5a34b23-7613-30dc-a435-5db51909c609 | -8.06013 | -44.79774 | 2025-10-04 03:51:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 92232cfd-82d1-3eb2-8763-bb639e53daa2 | -5.66613 | -42.70731 | 2025-10-04 03:51:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| a2f09f83-caf6-39a5-b3dd-f74c32c2f2db | -9.89818 | -43.73983 | 2025-10-04 03:51:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| cecf8099-796b-3372-9ae6-51f590ece8b6 | -6.34069 | -43.46232 | 2025-10-04 03:51:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c268a203-3358-3962-9739-ef3c721fe1d4 | -7.24528 | -48.48602 | 2025-10-04 03:51:00 | NPP-375D | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 01c07482-4501-3a50-9ecd-736379b88831 | -5.25817 | -39.26592 | 2025-10-04 03:51:00 | NPP-375D | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| bf1e718c-670b-3280-9d2a-11c1667feae5 | -7.55533 | -42.39356 | 2025-10-04 03:51:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 5e8f6c02-a025-3753-b794-310357fb6feb | -8.92227 | -46.61369 | 2025-10-04 03:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6b13f85a-e048-3ee8-8245-6d5af6468e7b | -8.89342 | -45.02493 | 2025-10-04 03:51:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9c4ceba0-1584-36cc-9ed7-c497cf1c3c0a | -7.77481 | -46.25135 | 2025-10-04 03:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bcd2aa60-4853-378a-b5ba-bcd62e44a946 | -9.11993 | -44.38894 | 2025-10-04 03:51:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e7b34480-a714-3715-8218-3a69cd2e0a31 | -6.88257 | -44.50482 | 2025-10-04 03:51:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2f2b7ec5-3973-32df-a83e-60ee6547092b | -6.19754 | -44.64387 | 2025-10-04 03:51:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b71543ab-55ca-390d-b3ff-4c60c565d306 | -6.29774 | -42.49401 | 2025-10-04 03:51:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 3501a34c-7d55-301c-91ef-5748b0d6e3c0 | -9.11871 | -40.13107 | 2025-10-04 03:51:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 22b651c8-6810-352b-a9d1-f949fb089440 | -11.08051 | -47.89374 | 2025-10-04 03:51:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 1c54c863-376c-3231-aa03-38c2d271bc17 | -5.71333 | -44.24286 | 2025-10-04 03:51:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3d7e8101-b08e-3c13-98de-bda4073ccc47 | -5.95949 | -43.49511 | 2025-10-04 03:51:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 43485f99-1d6c-3343-8c9c-36a75e6b0559 | -8.17524 | -44.13417 | 2025-10-04 03:51:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6907a479-2143-3263-aa66-3114887db992 | -11.45052 | -45.14569 | 2025-10-04 03:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 87fb009d-2afd-32f5-b1ff-83a941d62824 | -6.74952 | -42.17123 | 2025-10-04 03:51:00 | NPP-375D | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 681d3537-336e-3196-9233-08571804e1e6 | -4.82138 | -42.75911 | 2025-10-04 03:51:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 71374a9b-3695-3203-a46b-243bacdb0714 | -5.23892 | -45.54783 | 2025-10-04 03:51:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 845066d4-0266-3760-a59c-93628bd89507 | -5.19169 | -45.07591 | 2025-10-04 03:51:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 22.0 |
| 5ab3cdeb-e44b-304d-842f-6990a1993855 | -6.20107 | -44.33767 | 2025-10-04 03:51:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ba8f96d1-8a79-31b2-92c3-1d2da41ef174 | -5.77801 | -42.92339 | 2025-10-04 03:51:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 6075fdca-7815-3d95-8885-1dfd15d9120a | -6.18814 | -43.25782 | 2025-10-04 03:51:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.8 |
| db007f2d-24ab-3c08-b4ec-539f3c9cb786 | -9.9153 | -50.50106 | 2025-10-04 03:51:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| c2e0e9f8-a0bc-3e74-853c-4f377c27116e | -9.93467 | -50.90035 | 2025-10-04 03:51:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 74a347a6-35ca-3118-8b90-46fe0caf9956 | -5.69053 | -42.69467 | 2025-10-04 03:51:00 | NPP-375D | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| f049b9ed-a4e6-3e9e-8da9-a2d02f5d0b5e | -5.96857 | -43.4968 | 2025-10-04 03:51:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8cce6f62-b9fe-34f3-8208-6e5e18961712 | -8.22993 | -46.80231 | 2025-10-04 03:51:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 927d4905-7129-35f6-b59d-c8a34e9dfb54 | -10.04746 | -49.20394 | 2025-10-04 03:51:00 | NPP-375D | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 364b9009-6675-3c54-a8b1-78697736c9fc | -10.5396 | -44.516 | 2025-10-04 03:51:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 53abbd51-5af0-31c8-9406-20b3900d5ea5 | -11.11737 | -47.88285 | 2025-10-04 03:51:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1e826f09-23d2-3a48-8e88-99aff2b05852 | -6.37715 | -43.89433 | 2025-10-04 03:51:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5e0313c5-7b4e-3dec-a272-3e24627274a8 | -11.42784 | -43.48494 | 2025-10-04 03:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e62cc7d6-647d-344d-8fd4-abb0f41bd7d3 | -6.71398 | -42.81598 | 2025-10-04 03:51:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| a020f59d-df17-32a2-95b9-0516b0b4f61c | -6.31032 | -44.27629 | 2025-10-04 03:51:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| da48e4f1-6a6d-3867-b3b7-1dea8ef32620 | -5.01867 | -43.66026 | 2025-10-04 03:51:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2e5d4dd2-ce64-326d-a386-2216361be935 | -7.71709 | -42.58654 | 2025-10-04 03:51:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 4a69e57c-a889-3b67-a648-fef06ae9a912 | -9.34038 | -45.77472 | 2025-10-04 03:51:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a890e1c4-2962-3bc3-b0ec-6fb42ccfc143 | -8.38783 | -47.99622 | 2025-10-04 03:51:00 | NPP-375D | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6cc76884-9b7e-387f-a630-6c3e0b725cd5 | -6.87771 | -47.2399 | 2025-10-04 03:51:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 263575ef-600b-3c57-920a-1b435f285ed2 | -5.73631 | -42.92949 | 2025-10-04 03:51:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 8abe3193-af46-3f30-9d67-6f28217356a6 | -4.44085 | -43.24805 | 2025-10-04 03:51:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| b16d1ef0-6201-3a87-901e-fc63ee990bab | -6.09185 | -43.48695 | 2025-10-04 03:51:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 8f6a601c-02dc-3eff-9574-4be30f056722 | -6.24786 | -45.34653 | 2025-10-04 03:51:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ac4b6be5-a4de-3608-98ee-6d954c5cf25a | -7.79414 | -42.56093 | 2025-10-04 03:51:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 3ada31b2-29e1-393c-bf38-036abc35ecf2 | -5.24304 | -45.55539 | 2025-10-04 03:51:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 80e2517f-d2dc-3fe4-aa4b-6dfde17fb8a2 | -11.62311 | -45.0698 | 2025-10-04 03:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4a37cbc0-781e-3d82-b124-cb50285e29c8 | -8.17067 | -44.13332 | 2025-10-04 03:51:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c943b96f-304b-3883-bc0b-8379728f000f | -6.67439 | -44.20987 | 2025-10-04 03:51:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| dd12adb0-042c-3f96-8a66-cdacf7a1ba77 | -8.1943 | -47.00191 | 2025-10-04 03:51:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 0c71cd9c-ebd3-3502-890f-994352c78871 | -5.9098 | -49.29753 | 2025-10-04 03:51:00 | NPP-375D | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6cafeb86-7950-324b-93ae-a1547dc421b1 | -10.99538 | -46.67817 | 2025-10-04 03:51:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 69994a5e-dc3f-3953-88e6-e228bd5aacfa | -8.22964 | -46.80518 | 2025-10-04 03:51:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a203db83-448f-3a51-912d-4b99420d9156 | -6.07046 | -42.51434 | 2025-10-04 03:51:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 39.2 |
| 57d8a846-6463-348a-8c0c-253b4922658d | -6.87786 | -47.23757 | 2025-10-04 03:51:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 16.9 |
| b7c09fee-bc92-32fa-850f-f5d2d45339f0 | -6.24428 | -45.35744 | 2025-10-04 03:51:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| d1823b52-02f8-3f91-81cb-609ef74c2ad1 | -4.71843 | -46.12744 | 2025-10-04 03:51:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7e5a37ef-9e67-32ac-8302-7ebcb81a067f | -5.93773 | -42.88198 | 2025-10-04 03:51:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 8db01bf7-85d0-38c6-91b2-1ce4769ff322 | -8.38866 | -47.99178 | 2025-10-04 03:51:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 69f5bdb2-b32a-36dd-815c-1f55438156fe | -6.44587 | -44.80493 | 2025-10-04 03:51:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| d131c1b3-29b6-36f8-a768-23ff8d9940c0 | -9.33679 | -45.65295 | 2025-10-04 03:51:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7785b399-ad39-34cc-ae00-62e74b5d53cd | -4.43625 | -43.2473 | 2025-10-04 03:51:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 91d9814d-5ceb-3f16-968e-96286b4fd27a | -5.82112 | -42.88089 | 2025-10-04 03:51:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 23575df1-5f01-3149-a02a-fa0575f5a2fc | -4.31587 | -48.09272 | 2025-10-04 03:51:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| f19fd39b-71c4-3476-9a0c-607adaf3cab4 | -5.45808 | -43.16217 | 2025-10-04 03:51:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |


[Clique aqui para ver as próximas entradas](README31.md)
