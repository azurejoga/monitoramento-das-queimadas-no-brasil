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

## Dados Diários - Página 47

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7bd10693-9ced-3830-b6d8-06c38ea9dcce | -7.43679 | -46.17459 | 2025-09-16 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 76c4d227-0d50-3ca4-a5a9-d976e260a1c6 | -8.9277 | -45.52293 | 2025-09-16 04:29:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 00f297a9-b1a1-3347-a0dc-71b35b70e3fb | -11.44194 | -47.30465 | 2025-09-16 04:29:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ba591e9c-85d2-302d-8715-d46276b4678d | -10.71961 | -44.74788 | 2025-09-16 04:29:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| d23aa956-3594-3132-a5ac-a7941f247714 | -12.80045 | -47.24756 | 2025-09-16 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a0f1445d-3473-394a-921d-80e4797f145f | -13.18415 | -47.29817 | 2025-09-16 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 520bc91c-b44b-36ef-bcc3-5d45c9fc563c | -8.97627 | -44.18979 | 2025-09-16 04:29:00 | NPP-375D | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 95b4fbc8-8387-3402-a166-f2c71859b37b | -12.77752 | -47.92696 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 0011b621-5d03-3451-bd47-00e6606d3aeb | -8.44958 | -47.67492 | 2025-09-16 04:29:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e512630c-95a9-3ad8-865c-f6d01c165210 | -9.86847 | -46.45122 | 2025-09-16 04:29:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d9a92fb1-fdae-3a70-b8d3-408d6c3953be | -10.71138 | -46.5074 | 2025-09-16 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 3845e04b-c9c2-372c-97e5-76a1516438c2 | -12.66702 | -48.00732 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2f006704-09c7-30c9-8ceb-6b013962e1c2 | -9.073 | -50.30701 | 2025-09-16 04:29:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| de81efbf-31a5-3fed-a5ac-f753259d2ca4 | -7.46225 | -46.14286 | 2025-09-16 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| aa361e51-a665-3126-a9fc-845d7b908a7f | -8.12722 | -48.26323 | 2025-09-16 04:29:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d775ea38-04de-3b62-89ea-d18cceb6f315 | -10.71134 | -46.48561 | 2025-09-16 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 3145f48f-a89a-34b5-a1c0-8efd2ca79c45 | -8.17806 | -47.13593 | 2025-09-16 04:29:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8a074ac4-46c2-351e-a1ac-73c6f40ede45 | -12.83404 | -47.21973 | 2025-09-16 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 01240677-0a3b-3fc3-83fd-f1eb86e11d0c | -12.66999 | -47.92416 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5f59671a-38a6-3966-854c-8aadcb47c7b7 | -12.84218 | -47.13374 | 2025-09-16 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 03acc723-adae-39cd-9ed5-e86b19ca6f81 | -11.63337 | -46.58376 | 2025-09-16 04:29:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2e5d3ad4-0ff8-3174-b393-c450060869e8 | -9.22754 | -45.65768 | 2025-09-16 04:29:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 46de2d80-40a5-3853-b3a1-b35c3f8ef7c2 | -10.23225 | -46.73978 | 2025-09-16 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6508de43-60b6-3d7b-8e78-aa0b575b009f | -7.44012 | -46.17512 | 2025-09-16 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ccb9f2ce-7d11-3709-be75-b59c45c8bbe9 | -11.23567 | -49.4026 | 2025-09-16 04:29:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ffa3646b-b261-39ab-8567-46f6780b4330 | -8.91949 | -46.11729 | 2025-09-16 04:29:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 989a77b9-1d0b-3ed6-9d90-2929ba21a352 | -11.43206 | -46.93788 | 2025-09-16 04:29:00 | NPP-375D | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3b7e1643-8664-3c15-8c2d-7bdf31f83d19 | -11.12313 | -45.34444 | 2025-09-16 04:29:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e8b4a4f0-4284-3990-a189-d55834bd918c | -8.60797 | -46.40657 | 2025-09-16 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2ee42e0c-5dc0-3e3a-95db-6cfe96fccd03 | -9.85414 | -43.12378 | 2025-09-16 04:29:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| d65d4d97-cbc6-34b4-84dd-074cd3f9b101 | -12.67819 | -47.98005 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| debc73d0-57f5-373e-ad0d-18bf1ab924c0 | -12.26028 | -45.29858 | 2025-09-16 04:29:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8df298d8-4d10-3332-b180-13770985cdba | -9.08984 | -44.84505 | 2025-09-16 04:29:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 86f3bfae-ba48-3d6d-a2d9-80f0fc423295 | -10.43649 | -45.1412 | 2025-09-16 04:29:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dc0b49eb-928a-3f0e-9ffc-00e0b638570a | -7.5289 | -46.72479 | 2025-09-16 04:29:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c4e8ec30-9c5a-3fef-8718-3880ef759a16 | -12.81268 | -47.23494 | 2025-09-16 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c5da79df-492d-3fa7-9913-d2bcc8fa3f74 | -11.12533 | -45.11747 | 2025-09-16 04:29:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 87731e3c-a816-39fb-9a3e-8b2f9bcc6c9b | -8.12202 | -48.27364 | 2025-09-16 04:29:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d999f52f-3986-3623-88dc-6442a6db756e | -8.96796 | -44.19674 | 2025-09-16 04:29:00 | NPP-375D | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 327756da-05e4-34cb-aac8-929a70a6ddb9 | -8.97346 | -45.04189 | 2025-09-16 04:29:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 48a393e1-c874-3683-8e0c-a5bf5fa2ef17 | -11.13117 | -45.33796 | 2025-09-16 04:29:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 05f846a2-44a5-3c8e-be4d-d299b1749c74 | -12.05503 | -46.54303 | 2025-09-16 04:29:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a1d055f7-7bad-3a49-82f1-40397ad8ea3a | -12.78878 | -47.25661 | 2025-09-16 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| e97fe680-c289-35a9-b227-99e83e7eb0e3 | -8.96441 | -45.76072 | 2025-09-16 04:29:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 698992f4-b65d-3eec-addf-3b1ec5d3f61a | -12.44296 | -49.70601 | 2025-09-16 04:29:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| de4445b6-029d-37c8-af1e-3e8c39a8bbaf | -11.12025 | -45.34013 | 2025-09-16 04:29:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9f5455b2-270a-3362-814c-e1c26deceeee | -12.69804 | -47.74713 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ab7e772d-7786-34c2-a7f3-26f7dd047d0b | -13.21527 | -47.29607 | 2025-09-16 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f70a0727-d65c-3832-aa8c-1d964428b655 | -12.66533 | -47.71633 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6ea2ab05-6453-3806-92a2-bfcff5a3bfce | -12.9646 | -47.98322 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3cbb80aa-0656-3410-a2b4-90914c5781eb | -7.40884 | -49.99165 | 2025-09-16 04:29:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 20c29829-bc92-335d-8eb2-4f42e933af9c | -10.72544 | -44.75683 | 2025-09-16 04:29:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 1816ae45-5ccb-34b9-9806-7b3492d3ebda | -9.17763 | -47.06298 | 2025-09-16 04:29:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4d39c885-9078-39f3-8da4-771bc4618384 | -13.16968 | -47.28134 | 2025-09-16 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f4b99300-f3c8-3d48-8957-32fdbaf1e2f8 | -12.61158 | -47.96909 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b8d57f5c-f922-39c7-a70b-98d8ce50527c | -12.66922 | -48.01497 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| df067403-51fc-374c-bb51-47dddb94cb34 | -10.79346 | -50.68568 | 2025-09-16 04:29:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cce905a0-7e1e-360e-8217-be3b9bb92051 | -13.20414 | -47.27967 | 2025-09-16 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f0c2d148-8c0b-3a5f-aaee-b68233b1e91b | -10.71024 | -46.49267 | 2025-09-16 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| b4d0e89f-5ed6-3e5f-81da-645455031e4d | -8.87887 | -46.19014 | 2025-09-16 04:29:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| d56596dd-4bf9-3fcc-8f91-11c230f3939f | -12.62912 | -47.51821 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fde6c5c9-274f-38dc-ae56-c6beba4e2636 | -10.73922 | -44.7623 | 2025-09-16 04:29:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 23f0c6ff-ed23-3c94-9b76-3016f1d067e1 | -8.66612 | -46.37611 | 2025-09-16 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| c5e5710e-c600-3701-84c2-b45e6eb4ada4 | -12.69705 | -47.99043 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d3505cc5-a780-34e4-8734-4891f7c73785 | -10.04923 | -44.34458 | 2025-09-16 04:29:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6d835503-c7ea-36c3-90f2-8082a0bc7717 | -7.67467 | -46.29827 | 2025-09-16 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 921dbd7a-9a99-3e75-991a-1bd39fb469c6 | -7.40373 | -49.99976 | 2025-09-16 04:29:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| e41c30ca-866e-351a-bdbb-0fd5d9670cde | -13.2097 | -47.28788 | 2025-09-16 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5b53a1e2-598c-326e-88f0-4131380593f4 | -11.50085 | -43.7276 | 2025-09-16 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f7554aab-1c27-30ee-b845-8ab3b6be5055 | -12.6986 | -47.74359 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 35407b0f-89c2-342d-a094-34c25cd84bab | -7.99235 | -45.65345 | 2025-09-16 04:29:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4f4f888f-93d2-3185-92ad-39a9db827a7a | -10.89415 | -47.79763 | 2025-09-16 04:29:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bccef289-9101-32b7-ba67-0225f7d09655 | -11.07224 | -49.73707 | 2025-09-16 04:29:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f8c561dc-114d-3cb6-a99d-0b483fcbe72a | -12.84677 | -47.13775 | 2025-09-16 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b1264c17-e73b-375e-abae-58d952a213ea | -12.97519 | -47.95951 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fa41231b-10bf-3cf8-9220-e890a6570e91 | -8.21078 | -45.55254 | 2025-09-16 04:29:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bca8887b-166a-342f-a2ee-469048fec1f8 | -11.46951 | -48.70021 | 2025-09-16 04:29:00 | NPP-375D | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c32e5807-bdcb-3766-a764-425c79a0751b | -12.78085 | -47.92751 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c905fd29-d92c-30aa-a1ea-f97844dec94f | -8.1724 | -46.76268 | 2025-09-16 04:29:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3f5643ba-b0e6-34a4-8a7b-17d280f2a9c7 | -7.57358 | -49.84725 | 2025-09-16 04:29:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2437a78a-f343-390b-a1b1-93d544bcbc8d | -7.39772 | -50.00105 | 2025-09-16 04:29:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| c06d9e0c-c6a9-3036-9dcf-609aef8e8e41 | -11.29533 | -50.85381 | 2025-09-16 04:29:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 51818804-d111-33e1-9098-074d9e50b0e1 | -11.65272 | -46.6015 | 2025-09-16 04:29:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a338a3ca-b458-3d66-81d6-bc64107a340f | -10.71079 | -46.48913 | 2025-09-16 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 60fcc0e2-db52-3ab8-bb9e-4e268ff9b538 | -10.65062 | -46.46538 | 2025-09-16 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 223c7e59-3723-354a-9c4d-f32b46d4124d | -8.13197 | -43.65203 | 2025-09-16 04:29:00 | NPP-375D | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8a20e2c0-a22c-3f25-8937-8a9ab7b02522 | -7.71986 | -44.78216 | 2025-09-16 04:29:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c50ed844-870f-384b-9355-8b4cc16cbb89 | -8.10089 | -50.15727 | 2025-09-16 04:29:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 575e24c0-b53a-3d5e-888a-801420ffe90e | -12.11357 | -44.82692 | 2025-09-16 04:29:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8dad20ef-eb82-30c7-93c9-452e9a846251 | -11.24232 | -49.95171 | 2025-09-16 04:29:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c6fc2600-68d4-36c3-ba4f-edca43f92117 | -12.79935 | -47.18891 | 2025-09-16 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2850d4c5-eacc-391b-98a4-371f61054a54 | -8.11921 | -48.26942 | 2025-09-16 04:29:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8c274956-20ad-3380-ba23-6e0cdcc1c273 | -8.22497 | -49.49228 | 2025-09-16 04:29:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b3426644-373f-3b3b-bc09-651219a199fd | -12.77912 | -47.95993 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e11e99e1-95d7-3c28-a0e2-90527e79125e | -8.65331 | -46.34894 | 2025-09-16 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 057d8f46-348f-30ff-9415-af97f3899df3 | -7.85663 | -46.10483 | 2025-09-16 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2c5694cb-c0a0-3d80-b3c9-541acae2f7ea | -8.97866 | -46.24229 | 2025-09-16 04:29:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f5d5a109-da86-3d6d-86f8-b4c3594e83c1 | -7.8376 | -43.85944 | 2025-09-16 04:29:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2357291b-b116-3a0b-af14-802a38750a3a | -10.62933 | -44.21879 | 2025-09-16 04:29:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| acca9674-e56c-3a81-9e35-fb3aa94318f9 | -10.72871 | -44.7604 | 2025-09-16 04:29:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |


[Clique aqui para ver as próximas entradas](README48.md)
