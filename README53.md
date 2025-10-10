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

## Dados Diários - Página 53

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 45ece772-7329-3b6f-bf13-fc5ba4def640 | -13.2355 | -47.6215 | 2025-10-10 13:50:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 334ae8c7-7b0d-39cd-9b20-d82ca287516e | -12.9183 | -45.0517 | 2025-10-10 13:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 66.0 |
| 6690c6eb-da91-3434-a842-175f8c290132 | -8.2074 | -44.18 | 2025-10-10 13:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 108.3 |
| 3213f670-6a33-3656-9075-0c424bdef579 | -8.5196 | -46.3323 | 2025-10-10 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 6b1461fa-eff6-3770-b965-84ef1bb1b1dd | -10.8922 | -47.093 | 2025-10-10 13:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 84.5 |
| df0c4f6b-5f97-3b06-8f2c-aff17afbe68d | -9.6363 | -46.0995 | 2025-10-10 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 9b58449d-2f8e-32e5-a686-78d844b9adc6 | -12.9841 | -51.0648 | 2025-10-10 13:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 2756eda3-59a2-394a-9c98-f35da480105d | -11.7585 | -43.3374 | 2025-10-10 13:50:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 3b719e5a-cf62-3cc9-8140-a698729f4cce | -8.2071 | -44.2032 | 2025-10-10 13:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 98.1 |
| 057c1347-eba1-3b7c-a295-4020a39698a5 | -8.4844 | -46.134 | 2025-10-10 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 102.6 |
| 59ddcbbf-e175-383a-9c78-b4d40758bb39 | -8.1882 | -44.2052 | 2025-10-10 13:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 98.4 |
| 637aef7b-4dae-307d-a728-2d65b47a6d42 | -10.1898 | -44.5934 | 2025-10-10 13:50:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 142.3 |
| 3ca30dcb-7cd7-3b86-8459-1c0fb7e7ab99 | -13.8496 | -45.8223 | 2025-10-10 13:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 158.2 |
| bdeeee0d-314c-313c-b702-4ed957e053da | -13.3488 | -47.7388 | 2025-10-10 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 146.5 |
| 2ac5a906-2ccc-33e3-957a-b564221757e0 | -12.4705 | -47.4416 | 2025-10-10 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 1f2d55c0-99e6-3a0f-a312-aa77b3f8d879 | -14.8433 | -48.4665 | 2025-10-10 13:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 106.3 |
| c85c4493-58c3-37e5-b47d-b44cf15a0411 | -9.0022 | -45.4693 | 2025-10-10 13:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 75.6 |
| cfa773dc-a01e-3faa-b750-87088c127623 | -13.8311 | -45.7793 | 2025-10-10 13:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 116.3 |
| a06690b8-d7b4-3569-95d8-5b74a39d6ddb | -14.9372 | -46.7591 | 2025-10-10 13:50:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 118.0 |
| 3931d784-0f67-37bc-97b8-a79a27f001c6 | -8.0154 | -44.4539 | 2025-10-10 13:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 69.8 |
| f8dbd97e-4b0a-3cc3-a62a-aef405b27fc9 | -7.7927 | -44.1767 | 2025-10-10 13:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 353d94d6-246a-340b-b9f9-759b57ca0df8 | -8.5055 | -45.9519 | 2025-10-10 13:50:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 101.1 |
| ea3902d1-1fab-3252-8cc2-61a32e148497 | -8.5029 | -46.1545 | 2025-10-10 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 159.3 |
| 42f7c711-1373-3261-9c84-e59bc1990f68 | -14.8884 | -47.2226 | 2025-10-10 13:50:00 | GOES-19 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 112.9 |
| 4bafcc26-8194-3263-8952-70f71e0e6dcc | -14.4258 | -47.9974 | 2025-10-10 13:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 100.4 |
| d0a09344-acf1-319b-a339-9472fabaf7dd | -10.1901 | -44.5703 | 2025-10-10 13:50:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 84.1 |
| a7059585-8ae7-3616-85ff-400dc4a8978e | -13.0036 | -51.041 | 2025-10-10 13:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 99.7 |
| 0fb3a1b8-13a5-30b0-8ef3-fbcc80d7596d | -8.5032 | -46.1321 | 2025-10-10 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 198.6 |
| 9e70ca0f-153f-3e17-a58e-f85bc5f7e56d | -13.2859 | -48.0157 | 2025-10-10 13:50:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 98caa6d7-5d98-30f8-b5e5-c3313b586f94 | -14.4253 | -48.0199 | 2025-10-10 13:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 7287ac1e-207f-3df5-b678-1853e0fb145a | -14.9567 | -46.7556 | 2025-10-10 13:50:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 99.8 |
| bda936e1-526e-3792-92d0-bc4aadcfe563 | -9.1028 | -45.0248 | 2025-10-10 13:50:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 8fd5b109-1b63-30d5-8777-fac6d35d2705 | -7.7924 | -44.1998 | 2025-10-10 13:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 92.8 |
| 73acdf44-7245-3151-86f0-8a6a4cf33b3c | -10.1517 | -44.5984 | 2025-10-10 14:00:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 4483747e-b21c-30ec-bc43-9574721ccbc6 | -13.3215 | -47.137 | 2025-10-10 14:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 64.6 |
| cb0541aa-e077-3a5a-9c3a-ac3b2b9c8845 | -10.1901 | -44.5703 | 2025-10-10 14:00:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 17c2c924-c587-3807-9a41-4f88be20a704 | -8.5599 | -44.6494 | 2025-10-10 14:00:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 95.8 |
| 46d3afc9-12ea-3fcf-a9f4-730d2a859919 | -8.1618 | -43.323 | 2025-10-10 14:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 144.7 |
| 4a3a2a35-f98e-36ad-bdd2-2a0e2fe1f738 | -16.7505 | -44.0129 | 2025-10-10 14:00:00 | GOES-19 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 100.0 |
| 87973c3d-d92e-3c63-a442-81f2d26402fc | -8.5052 | -45.9744 | 2025-10-10 14:00:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 59.5 |
| c9189d3e-a12c-3cd8-b6a8-8aa9a50cd8c4 | -13.8311 | -45.7793 | 2025-10-10 14:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 120.5 |
| 9ca663c3-797c-390a-9b47-1405d4b4c258 | -8.1807 | -43.321 | 2025-10-10 14:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 226.5 |
| 72e38236-1637-3e41-a3b1-b34a9b49b422 | -8.2074 | -44.18 | 2025-10-10 14:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 118.3 |
| 863b2664-d097-3e51-b74a-4b39f70297e4 | -8.6292 | -45.1228 | 2025-10-10 14:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 80.1 |
| c375fbf9-2c77-3725-862e-65abc9d75ff1 | -7.7547 | -44.2036 | 2025-10-10 14:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 112.6 |
| 7f519497-a547-31fb-b676-cc207f9bbc06 | -8.5016 | -46.2669 | 2025-10-10 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 44f1f6a9-d4eb-3670-8de9-570141b00fbd | -13.2864 | -47.9934 | 2025-10-10 14:00:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 760db6c7-c521-354c-a2d7-cb56c0ac30ce | -11.6852 | -47.5263 | 2025-10-10 14:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 53.4 |
| 8c2c8166-4e9a-347a-8c6d-1c5be2a9df73 | -11.6451 | -44.2966 | 2025-10-10 14:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 101.1 |
| 25871377-9fa8-3ed4-8f3c-ce8991ccd7b8 | -10.1707 | -44.5959 | 2025-10-10 14:00:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 80.9 |
| d8455c29-0c02-35cd-8f2b-40ae284c1a93 | -8.4844 | -46.134 | 2025-10-10 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 105.2 |
| 63343b88-5c71-3384-bc0a-0f98dff21089 | -15.9195 | -43.2779 | 2025-10-10 14:00:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 130.8 |
| c29c4f9b-8e9d-3a24-86fc-b8ea6fc6fe52 | -8.6109 | -45.0792 | 2025-10-10 14:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 59.6 |
| 40dc89ae-27ee-3bc1-9236-3b8219ba9f5b | -8.1993 | -43.3424 | 2025-10-10 14:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 353.2 |
| fc29f84d-e39b-3127-931d-0108dc0051cd | -8.5029 | -46.1545 | 2025-10-10 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 161.7 |
| 0cf07e3e-998d-379e-b025-8473401709cb | -16.7306 | -44.0173 | 2025-10-10 14:00:00 | GOES-19 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 118.5 |
| 08d3cd37-39cb-36aa-acf4-123b1f1d707c | -9.6363 | -46.0995 | 2025-10-10 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 9f0f8f28-9a84-3bf8-b393-355ef0ababac | -8.6295 | -45.1 | 2025-10-10 14:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 82.3 |
| f80a9d69-e09c-3fa6-92be-58e92b12b631 | -9.0022 | -45.4693 | 2025-10-10 14:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 61.4 |
| 016909a7-1af7-30ee-b3ff-1e9c68e300cd | -9.4674 | -46.006 | 2025-10-10 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 81.5 |
| a863fd05-4025-33ec-b261-1d1740f057b4 | -7.7924 | -44.1998 | 2025-10-10 14:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 99.8 |
| 3ac6510e-4358-39df-9212-e053995fc464 | -11.7585 | -43.3374 | 2025-10-10 14:00:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 9be8d486-c7f3-3410-b37b-74e9cc1ad0a5 | -8.1804 | -43.3445 | 2025-10-10 14:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 153.0 |
| fcf54834-7c77-3ef0-b6bf-6facdfb2c548 | -8.199 | -43.3659 | 2025-10-10 14:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 138.7 |
| e13f3bfa-cc48-3f77-85e4-43775f9919ac | -8.5055 | -45.9519 | 2025-10-10 14:00:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 5e6508ac-22f3-303b-b499-086e68fa3c8b | -7.8648 | -44.4461 | 2025-10-10 14:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 8f004113-5eac-36d7-8490-63120c78ac18 | -8.2077 | -44.1568 | 2025-10-10 14:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 105.6 |
| cbbb9ebf-583f-33cb-afe4-d0d7c630efb0 | -13.2859 | -48.0157 | 2025-10-10 14:00:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 289dcef2-920f-3d41-85bc-708c39592701 | -12.4705 | -47.4416 | 2025-10-10 14:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 1d540e76-0e5d-3ca0-9a8f-daba11903604 | -14.4258 | -47.9974 | 2025-10-10 14:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 81.0 |
| f5296f59-68c3-3ded-99d9-79af272ee4f1 | -13.8491 | -45.8454 | 2025-10-10 14:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 112.7 |
| 13b727bd-b887-3314-8744-46e8d521d260 | -8.0154 | -44.4539 | 2025-10-10 14:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 36f6c9c2-118a-33bf-9bb0-1f019703b0d5 | -8.4824 | -46.2912 | 2025-10-10 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 66.0 |
| ba93752c-016b-3581-ab0c-175c20ed89d7 | -16.7312 | -43.9931 | 2025-10-10 14:00:00 | GOES-19 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 158.8 |
| 40437cb6-2fb7-3834-937d-59aff0b6aa83 | -8.2071 | -44.2032 | 2025-10-10 14:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 107.2 |
| ef22addd-1319-3780-bf99-6dd0f92fe4bf | -13.2667 | -48.0186 | 2025-10-10 14:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 976ff56d-ab6e-33a1-958a-00a4fe0527a9 | -8.1879 | -44.2283 | 2025-10-10 14:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 98.3 |
| 3c4dc5c5-0089-307b-b650-f6050787ba89 | -13.3026 | -47.1174 | 2025-10-10 14:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 529d2fe4-e571-3b9c-95b0-eab0ce203270 | -8.5602 | -44.6264 | 2025-10-10 14:00:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 5c0c7ca8-e1ad-3b19-bcb8-751ceb1df079 | -7.7927 | -44.1767 | 2025-10-10 14:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 86.2 |
| c38d6e87-af14-3f54-bf40-4c17ebc68962 | -10.1714 | -44.5496 | 2025-10-10 14:00:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 9e93dc7d-baa5-3e63-ab14-a5e35c0b12c2 | -13.3057 | -47.9906 | 2025-10-10 14:00:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 91.8 |
| 477823d6-2e54-335a-b471-dabde95b2e21 | -12.5541 | -48.1419 | 2025-10-10 14:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 68.1 |
| c2e29bf1-462b-3945-9b78-31801821ba7f | -16.7511 | -43.9887 | 2025-10-10 14:00:00 | GOES-19 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 143.3 |
| 66617935-dffa-3b79-920b-f754a1ca7102 | -13.3022 | -47.14 | 2025-10-10 14:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 76.6 |
| fc0aa128-ec7c-3c52-a376-92eb93b2f86d | -8.1882 | -44.2052 | 2025-10-10 14:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 106.5 |
| e206b175-0251-3db5-b979-122256dd44ea | -13.2355 | -47.6215 | 2025-10-10 14:00:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 009fb4cc-d130-3313-82e6-175cee8ef70a | -10.1898 | -44.5934 | 2025-10-10 14:00:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 106.8 |
| dd42ce7d-0d18-30cb-8323-bd606d815535 | -13.8496 | -45.8223 | 2025-10-10 14:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 114.0 |
| 206f0241-64f3-35b6-acd5-ef0b04ef7121 | -12.3592 | -47.2335 | 2025-10-10 14:10:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 75.8 |
| bb4f7a4f-21af-325d-b101-0ca56faa1fee | -13.3215 | -47.137 | 2025-10-10 14:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 87.9 |
| 6bace8ac-bb9b-3fe5-ad49-7fbf17e7cd9e | -8.1804 | -43.3445 | 2025-10-10 14:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 162.4 |
| bb6722a4-5f56-3907-b17c-6512e8f0663d | -15.3933 | -47.3166 | 2025-10-10 14:10:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 118.3 |
| 806d44da-494d-35f1-8052-2dddf2c7613c | -13.3022 | -47.14 | 2025-10-10 14:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 106.4 |
| f2cb8539-17d1-3b7d-817b-72c2f5e093c2 | -8.4844 | -46.134 | 2025-10-10 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 98.3 |
| da00e009-d508-3ec7-9366-c9c006490334 | -13.3963 | -47.2607 | 2025-10-10 14:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 57.6 |
| 61998c05-4ce3-3784-acb2-9226f0110dba | -7.7927 | -44.1767 | 2025-10-10 14:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 40f249bc-0755-32cc-81f3-38b03b75529d | -8.6292 | -45.1228 | 2025-10-10 14:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 82.3 |
| e1c8ca52-c682-3a4e-81b8-c7c266547cc4 | -8.6106 | -45.102 | 2025-10-10 14:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 4ccff9e2-6ba0-396f-abe3-26e9589d9ad9 | -17.9207 | -57.6158 | 2025-10-10 14:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 56.1 |


[Clique aqui para ver as próximas entradas](README54.md)
