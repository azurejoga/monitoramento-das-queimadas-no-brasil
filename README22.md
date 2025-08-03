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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 15f26e4f-516a-3301-8c30-30eef3265ba5 | -12.62651 | -44.51023 | 2025-08-03 04:53:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c5a98383-0f4e-3143-b140-e344d27c3ab3 | -7.96105 | -45.10959 | 2025-08-03 04:53:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5fb3a9ae-456a-3f09-a932-2885c416ad1c | -6.62151 | -59.95148 | 2025-08-03 04:53:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 18b1ff7a-bcb4-3c95-8e41-3bba139aceaa | -10.4668 | -47.22506 | 2025-08-03 04:53:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 81bf4814-2f7a-3d7f-a830-9f05e67173b9 | -12.65576 | -44.49631 | 2025-08-03 04:53:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ffe27427-ac97-3a96-9ce0-da753e022a17 | -10.35691 | -45.18309 | 2025-08-03 04:53:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c874a2ba-9621-3aca-8ddf-4690925934ad | -7.50518 | -49.74864 | 2025-08-03 04:53:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7bd8c957-7349-395c-9f8c-19afee15eade | -8.00726 | -43.16881 | 2025-08-03 04:53:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 76448af3-cea2-356b-90e2-9cac10bbb858 | -7.41204 | -47.00726 | 2025-08-03 04:53:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 033843f2-c9a3-3a12-9d24-47de1263a6a2 | -8.01132 | -43.18058 | 2025-08-03 04:53:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| d741b669-044c-35cf-8445-460d1717e4ea | -6.61743 | -59.96961 | 2025-08-03 04:53:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 108b4323-0748-3f58-ad40-6f3680eea21e | -6.72906 | -59.17016 | 2025-08-03 04:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 982d6b4b-456f-361d-96fe-276cb3adb5ba | -7.60009 | -55.20275 | 2025-08-03 04:53:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c037cd0d-b2f1-3d84-86d8-6aaba9f9bd0b | -7.99871 | -43.18987 | 2025-08-03 04:53:00 | NPP-375D | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 8.3 |
| a1cba074-df8e-3990-bfa1-71738b79eced | -6.61794 | -59.97166 | 2025-08-03 04:53:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3b427c7c-6c26-39af-89ea-e05b02463a00 | -12.64603 | -44.51714 | 2025-08-03 04:53:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bbd3dcc5-191b-3489-b299-d64954f0c3ae | -12.03783 | -44.02079 | 2025-08-03 04:53:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f7f2acb3-ade8-39e5-9936-95962e0d7ce6 | -7.43601 | -43.82877 | 2025-08-03 04:53:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6e5f703b-669a-3ec2-b1c9-17c6ae581da8 | -11.93421 | -46.67523 | 2025-08-03 04:53:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 09c5bf90-49ef-3634-bae5-7573dce04988 | -7.96515 | -45.11578 | 2025-08-03 04:53:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 61a92aed-1a59-392d-bba3-7b38fb6f983c | -8.34163 | -46.91409 | 2025-08-03 04:53:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7502b511-ed26-3151-8d71-b003c69b841f | -12.64947 | -44.50267 | 2025-08-03 04:53:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| e68b4f1e-f12a-3cbf-ae44-46b5acc99d9f | -12.64325 | -44.49549 | 2025-08-03 04:53:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c184f092-2202-3c00-8846-69415533d4eb | -12.67378 | -44.4843 | 2025-08-03 04:53:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 02e9c0ed-5777-3b41-bbe1-2b962d379948 | -12.66283 | -44.52927 | 2025-08-03 04:53:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 857b6c9f-d803-3e75-9660-08b9574b8b5f | -12.63649 | -44.50529 | 2025-08-03 04:53:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 78a07ef3-7d1b-3a21-9c1f-98d9172db091 | -11.93485 | -46.67026 | 2025-08-03 04:53:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 873599fd-afa0-3615-a1e1-5c49d58fefe9 | -7.53539 | -44.88127 | 2025-08-03 04:53:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cc0f24ea-a5a9-39a9-bbd3-960b3a1adf9f | -8.4368 | -45.59485 | 2025-08-03 04:53:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e89c9ec0-5a52-39da-80a4-05d51093c78a | -7.52551 | -61.36319 | 2025-08-03 04:53:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 17c8dfeb-b93a-3d6e-a3ad-70b2c83c822a | -8.04186 | -43.1063 | 2025-08-03 04:53:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.4 |
| e4748efb-cbf1-3cc5-8f88-63db073ae339 | -12.44798 | -44.8596 | 2025-08-03 04:53:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 14aece59-bcf8-30d3-aab4-863e1fb1fa02 | -10.47663 | -46.96228 | 2025-08-03 04:53:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 041681aa-0fb5-3859-ad07-0bfd0af7d621 | -12.41229 | -47.07526 | 2025-08-03 04:53:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 28b8ca8f-4377-36d8-9145-eb89f929a399 | -12.48815 | -47.16603 | 2025-08-03 04:53:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 907ee647-2347-33fa-8fb1-5c1b2cdf15ed | -12.63238 | -44.49406 | 2025-08-03 04:53:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ead405b8-c4d4-3592-98bc-e20e100e3780 | -12.50047 | -47.1772 | 2025-08-03 04:53:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dd1495cd-f761-3d0b-b84e-3463c8ba0d55 | -7.92395 | -45.12597 | 2025-08-03 04:53:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6a805f52-5e5e-3585-8f95-092672a879de | -9.39854 | -45.50199 | 2025-08-03 04:53:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 93c7429c-c8fc-399d-9953-c3c8b75f4760 | -7.13659 | -48.19616 | 2025-08-03 04:53:00 | NPP-375D | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 75e46c6e-a925-335f-ad3a-ce3949d5c8d7 | -6.8307 | -59.26313 | 2025-08-03 04:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 70aa1619-46a4-38ee-8cec-9f9677be4f88 | -10.95395 | -45.17123 | 2025-08-03 04:53:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 19d57a87-4d4b-3d3f-9383-6994ec7d4e10 | -7.5266 | -61.35703 | 2025-08-03 04:53:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 349bfc07-bf96-393d-9ef6-0033f0f95ead | -7.96924 | -45.10073 | 2025-08-03 04:53:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 703b268c-b47f-3576-a74b-112ddac5b145 | -12.42186 | -43.48898 | 2025-08-03 04:53:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| edf77189-d4b5-305d-89fe-008c37862a80 | -12.61424 | -44.66019 | 2025-08-03 04:53:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| fad7bd69-0def-3154-a2a2-578c1a2bf5f4 | -12.63062 | -44.50805 | 2025-08-03 04:53:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| de9106b2-1a9c-3564-b446-e910c63ac066 | -12.43593 | -47.03569 | 2025-08-03 04:53:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c068cb43-3d69-3290-8239-ae992de7cb8d | -7.51663 | -61.32392 | 2025-08-03 04:53:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3de48975-cb9a-338a-95a5-297a1f81fe09 | -10.78733 | -48.81051 | 2025-08-03 04:53:00 | NPP-375D | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 96da948a-a793-3228-85bd-b62911524a4b | -9.58556 | -43.83746 | 2025-08-03 04:53:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| ea9a200c-b1af-305b-adc9-656c42259887 | -8.01684 | -43.14029 | 2025-08-03 04:53:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 5a808b1f-132b-3c23-a8a6-8aecac05bdc3 | -8.01532 | -43.15143 | 2025-08-03 04:53:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| b727307f-ef50-3cbc-bdba-3df40d4cbe4a | -8.0012 | -43.1716 | 2025-08-03 04:53:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 60d29edb-3870-306c-98a5-91c83b2f269d | -12.63693 | -44.50178 | 2025-08-03 04:53:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 77907a94-561a-3e75-889d-a29a7d560ae6 | -11.23457 | -48.44358 | 2025-08-03 04:53:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e43b0446-9e97-37c7-9a24-8a5d50bc06eb | -6.67844 | -59.16998 | 2025-08-03 04:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 46fd0867-c355-3699-97b8-2b0c9fa3d3ae | -8.00625 | -43.1762 | 2025-08-03 04:53:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 28.1 |
| 9e056516-f68e-305a-9f3c-14ea543de4a9 | -12.67335 | -44.48783 | 2025-08-03 04:53:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cdb08495-8565-3a59-8f85-1196eaa51ce5 | -12.65618 | -44.49279 | 2025-08-03 04:53:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a766564f-8db0-3df8-8bee-754817990c68 | -9.39928 | -45.49667 | 2025-08-03 04:53:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6fe6ffe5-06d6-38d1-bb1e-ffd1a8e701fb | -7.31548 | -44.67089 | 2025-08-03 04:53:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a6dea548-43bc-39f4-a02e-8221456bd6ea | -8.01025 | -43.14693 | 2025-08-03 04:53:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 38.5 |
| c7eb36fc-522e-39f8-b4e7-71021cc4ab3f | -6.67022 | -59.16419 | 2025-08-03 04:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| aa65f624-daf4-300a-9769-4e3697f5c939 | -12.63276 | -44.504 | 2025-08-03 04:53:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| db15787b-d5b2-3925-b6eb-ce3af0740af8 | -8.00424 | -43.19085 | 2025-08-03 04:53:00 | NPP-375D | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 085677e3-fb4b-3cce-83e0-8e55f285053a | -7.96668 | -45.10499 | 2025-08-03 04:53:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 71c63b56-7a76-31f4-bc23-a0a8e9ea7f99 | -6.72755 | -59.17905 | 2025-08-03 04:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0b412b0c-9724-302b-8994-3c232ff0cb32 | -6.65192 | -59.11096 | 2025-08-03 04:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| b6bf6992-4840-315e-b24f-5f705ed87176 | -11.04947 | -49.54441 | 2025-08-03 04:53:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3b02160d-b3c8-3c1a-8f1f-01ab245109fe | -6.82095 | -59.26608 | 2025-08-03 04:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2cad8fd3-363e-3e84-9923-09e6ff8fd5aa | -7.12572 | -44.38532 | 2025-08-03 04:53:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bae38de6-d735-3801-8cec-ea8189935605 | -7.09882 | -44.36577 | 2025-08-03 04:53:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 67ccb205-1247-3f35-892b-ce6392f522c8 | -8.03159 | -43.11582 | 2025-08-03 04:53:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 7438931e-7261-39db-a864-6dd972c6af73 | -8.00417 | -43.14983 | 2025-08-03 04:53:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 38.5 |
| 9aefdcc7-6de0-34a8-b2c8-51f5614f4c42 | -6.73203 | -59.17983 | 2025-08-03 04:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 496b85e3-1fc7-3d9b-8bb3-cc818223c49f | -8.01738 | -43.16324 | 2025-08-03 04:53:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| dbfb2959-0992-340c-b255-3e31c821caa1 | -7.52203 | -61.35299 | 2025-08-03 04:53:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d3019844-8e4d-377f-8cad-45ccd20c9593 | -6.62773 | -59.96632 | 2025-08-03 04:53:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e6be9000-97f2-347e-8244-aa89f0b27cfb | -8.93779 | -46.74552 | 2025-08-03 04:53:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 27dc6c51-c7aa-3703-911f-af0a154f0965 | -10.95903 | -45.17185 | 2025-08-03 04:53:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 90174f17-9f33-33d0-8813-007526feed37 | -7.59946 | -55.20663 | 2025-08-03 04:53:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d660e55a-605f-3b5f-a92a-d42eb3f836af | -12.6202 | -44.50309 | 2025-08-03 04:53:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 78d0a16c-8b04-3fcb-877a-55301136bc62 | -12.62694 | -44.49334 | 2025-08-03 04:53:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1f5794c8-b393-3865-9160-917a3c4bc1d9 | -12.6524 | -44.52433 | 2025-08-03 04:53:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 253fa3e6-ef22-3931-aa91-c69663e9eb3c | -12.63317 | -44.50049 | 2025-08-03 04:53:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| ac4fc4d3-a357-3c3c-a2ff-c28bfe766489 | -10.02935 | -45.57911 | 2025-08-03 04:53:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2f677802-2511-3017-bd47-034d599165cb | -6.81194 | -59.26466 | 2025-08-03 04:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 272474e1-18df-3ac4-83e7-02f64db6e05e | -8.3373 | -46.91343 | 2025-08-03 04:53:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 448d3e34-90af-3f75-be5e-b5ba32cc671e | -12.44229 | -44.86205 | 2025-08-03 04:53:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2f2ca930-392e-385a-a296-d25c5c677b93 | -6.73428 | -59.16649 | 2025-08-03 04:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| aa65dee8-f887-344b-a6c7-c964d42e0386 | -8.0438 | -43.10995 | 2025-08-03 04:53:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 9c5071b9-14be-3d1b-88b0-6f2e9479243c | -8.02169 | -43.13005 | 2025-08-03 04:53:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| af4d422f-fdae-3e76-a969-8e4cc8820a37 | -7.12266 | -43.48459 | 2025-08-03 04:53:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| bc1b3ac8-f802-341b-9da7-e0654df8ac43 | -8.00924 | -43.15433 | 2025-08-03 04:53:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 96.9 |
| 67126819-14a5-38b6-a074-dad52b877990 | -6.63115 | -59.94601 | 2025-08-03 04:53:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7f6d76f5-ac31-3382-a2ce-55cb37c82edb | -6.62356 | -59.96745 | 2025-08-03 04:53:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| e017660e-7a4b-314a-802a-66b29a1d5415 | -12.63944 | -44.49419 | 2025-08-03 04:53:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 791b2136-bcad-3bf0-b73a-668747bf9eb8 | -8.00474 | -43.18723 | 2025-08-03 04:53:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 29.3 |
| a0d0eb44-23f3-3ac2-b9e3-48d171a6cfb3 | -8.01786 | -43.13285 | 2025-08-03 04:53:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |


[Clique aqui para ver as próximas entradas](README23.md)
