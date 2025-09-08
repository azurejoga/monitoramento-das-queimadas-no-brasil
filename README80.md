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

## Dados Diários - Página 80

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 61cfb99f-6eab-3e0a-9f7d-0db8a8213d29 | -9.99527 | -51.67397 | 2025-09-08 05:21:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 16a6a9bf-d81c-33a7-b7f0-024feb02e0dc | -9.95131 | -67.19553 | 2025-09-08 05:21:00 | NPP-375D | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ebbe659f-365a-31c0-ad9d-d3dda3d94772 | -6.25868 | -53.27913 | 2025-09-08 05:21:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9f421ecc-e08e-3ed5-8ea9-f523a7619ddb | -9.98542 | -51.67861 | 2025-09-08 05:21:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a4b7b10d-71b0-3315-84e0-9e4a08fe1723 | -9.71433 | -62.39795 | 2025-09-08 05:21:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9d3e2107-9756-3e63-bf97-7081275a5178 | -9.56382 | -53.59858 | 2025-09-08 05:21:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fb7f6ff5-06b8-315c-ba5c-830a5a2e2fde | -10.16426 | -61.12678 | 2025-09-08 05:21:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 08855fd9-6163-3425-9548-8e1614b14fb0 | -9.20125 | -46.04824 | 2025-09-08 05:21:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| ee4b97ff-b957-3fb7-b714-606eca6c40c4 | -11.23161 | -55.00899 | 2025-09-08 05:21:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 71b8e370-a233-3fc9-bf1c-f918fbb7836f | -7.22372 | -46.19829 | 2025-09-08 05:21:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ed4155a4-522c-37aa-8c92-295e899e81fc | -9.13155 | -65.95168 | 2025-09-08 05:21:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2c4e81a0-1a46-37aa-b283-7bdf17f8753b | -11.21494 | -55.01038 | 2025-09-08 05:21:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6d052c02-dcf7-3604-bb17-b82daee95ac7 | -9.14245 | -46.06207 | 2025-09-08 05:21:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| eb90b0c9-c66f-3662-af8c-8143669779c6 | -12.19973 | -53.91352 | 2025-09-08 05:21:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 86265008-9a87-3f7b-b23d-992479b348fc | -9.93304 | -60.10239 | 2025-09-08 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 13c51c1c-c66b-38ca-9248-1cff65a3385d | -6.28037 | -53.42252 | 2025-09-08 05:21:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 841f899e-cf53-3c74-8e04-e7d767c94cc1 | -7.39568 | -61.6376 | 2025-09-08 05:21:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| cbe5e625-5f28-3a94-89a9-3cfb2b300f6d | -6.83746 | -52.80644 | 2025-09-08 05:21:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5c2962af-e7b7-3721-91fd-2008c65b2fbe | -10.08668 | -59.1838 | 2025-09-08 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ef4004c6-30ca-3523-bc72-d93a5ab19306 | -10.79909 | -47.73411 | 2025-09-08 05:21:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b4075999-f4af-3036-84da-0b05eb1e9551 | -9.67514 | -51.06574 | 2025-09-08 05:21:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fd25911d-dfd6-31b6-b151-415f0fc1ec21 | -12.62494 | -56.96779 | 2025-09-08 05:21:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 0cc0fb30-dc9e-3fa8-a686-10b3b30df739 | -6.63701 | -53.37004 | 2025-09-08 05:21:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fea0dd28-91a2-30bd-bc49-9cdc4e81b56f | -9.94563 | -60.14376 | 2025-09-08 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dd7ffa94-dcd7-31cc-917a-75237d2b7637 | -6.20829 | -53.27346 | 2025-09-08 05:21:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bb8f66c2-653f-3594-87b4-debf949fa330 | -6.63402 | -53.36287 | 2025-09-08 05:21:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 3e25c884-72d6-3b17-bc43-f2fe91104e92 | -9.98476 | -51.6837 | 2025-09-08 05:21:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 7af2c2be-1c8a-3a42-a24c-d86483bc8d33 | -7.77344 | -61.37618 | 2025-09-08 05:21:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ea2f52b0-66b6-3f6d-b1f5-057d6205ec23 | -13.81117 | -46.27917 | 2025-09-08 05:21:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 45037317-4080-3eca-81a4-550f3953698c | -10.14841 | -61.13893 | 2025-09-08 05:21:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 90dadc87-2cf6-37dc-8ae7-fa9ea3bd26de | -11.66269 | -46.88868 | 2025-09-08 05:21:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6f153810-b89e-35b7-b34b-fb4627728b25 | -11.96819 | -55.53426 | 2025-09-08 05:21:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b539fd1a-c7a3-3cef-8a5d-d2561d57fb84 | -10.95778 | -46.82498 | 2025-09-08 05:21:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 8abb324b-45d5-3abe-8486-5b8d8e9f65bc | -12.63769 | -56.98305 | 2025-09-08 05:21:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c131bf90-2038-3430-9a79-575f9bb31a1d | -9.53495 | -59.06436 | 2025-09-08 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| bab57435-5eb4-300d-b29a-93228d77a446 | -6.81488 | -52.80775 | 2025-09-08 05:21:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| cc98b3a4-8ccb-3a4b-a157-413f45f8af6f | -13.32285 | -51.74722 | 2025-09-08 05:21:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3c78aadf-5bd4-33e6-abd4-805c55db1f12 | -12.61208 | -56.97913 | 2025-09-08 05:21:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 13278c6f-4e8e-34e4-b851-6cd78778cd25 | -7.39983 | -61.63425 | 2025-09-08 05:21:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 54c46f36-e171-3c5a-b59c-f1fafc65e440 | -10.41856 | -60.74306 | 2025-09-08 05:21:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8f82d868-82b1-37b4-8fe4-d25fd89c378f | -10.46895 | -53.61055 | 2025-09-08 05:21:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b147f541-df3e-38c2-b410-32ee0a6c251c | -6.63756 | -53.36616 | 2025-09-08 05:21:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 6832ed6f-34dc-361e-9653-808bf09c60dc | -11.02228 | -45.92979 | 2025-09-08 05:21:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 21007e34-d9da-3a94-bea0-38c0755e312f | -9.17166 | -59.37677 | 2025-09-08 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8df7c28f-6fe2-3cf8-9221-5cce7effd6d0 | -11.86283 | -51.06026 | 2025-09-08 05:21:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 86b719c2-f614-3304-8089-2aedd1ce9de6 | -11.20033 | -54.9973 | 2025-09-08 05:21:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5f9e3187-cd04-307e-b428-14efcc58453f | -12.01545 | -50.38066 | 2025-09-08 05:21:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d07169bf-799f-3eac-853f-cc4b435ef7c3 | -10.79973 | -47.72889 | 2025-09-08 05:21:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b02e9284-ed12-3de0-b8a1-2ed1187d26dd | -12.63466 | -56.97815 | 2025-09-08 05:21:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2b8be635-299a-3b8d-a3c8-288f0f725460 | -12.62431 | -56.97216 | 2025-09-08 05:21:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| dd826f62-cba3-3dc9-8065-28a4adf34f6e | -9.16944 | -59.36925 | 2025-09-08 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e61e06c5-a297-3fbe-b0d5-a9061ddff068 | -12.86998 | -47.97868 | 2025-09-08 05:21:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 87a98d72-0aa2-3041-9eae-6c643ccfc16c | -13.70257 | -46.8744 | 2025-09-08 05:21:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e32ae4aa-cab9-33b2-9f21-0805eefc8c8a | -7.18616 | -59.83768 | 2025-09-08 05:21:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| edbb70df-514c-3068-b6c4-0fbf7e58f291 | -6.54062 | -54.99714 | 2025-09-08 05:21:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5582ec67-dee8-31c3-8017-e387724a51db | -9.20645 | -65.90633 | 2025-09-08 05:21:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2cf6ebd5-4f2e-39ae-9bfe-565c15e76ccf | -11.02969 | -52.04142 | 2025-09-08 05:21:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 126ff545-8c2d-3060-9d1e-082bafdc0dc2 | -12.52561 | -53.84718 | 2025-09-08 05:21:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bc479c79-f47b-3542-aafc-14a9f996b891 | -9.99537 | -51.67985 | 2025-09-08 05:21:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 230a2bbd-136b-3770-af64-367ec63d84b8 | -10.51034 | -57.80027 | 2025-09-08 05:21:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 330cd3b6-5027-3898-844f-29c194d065cf | -9.12637 | -65.95522 | 2025-09-08 05:21:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 40013d88-e025-318a-8bb5-7dd0533d6e1b | -6.81051 | -52.80711 | 2025-09-08 05:21:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6b7eabe2-1ff7-3e70-8e02-36830da0b7f9 | -12.94845 | -54.81166 | 2025-09-08 05:21:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 92b34090-edfb-3bbb-92e3-e3a2eb6fba2d | -5.77068 | -56.52165 | 2025-09-08 05:21:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1158a6c3-62f5-3159-ab8d-747aca06c2e9 | -12.6194 | -56.98028 | 2025-09-08 05:21:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| a784819a-73ff-3cfd-9054-d5206c75123c | -12.62243 | -56.98518 | 2025-09-08 05:21:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a6a0f754-8148-3918-b1ca-3f1598656c5c | -11.41046 | -50.39894 | 2025-09-08 05:21:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ea89893c-b68a-3fb8-a9eb-4e6492d506c8 | -13.65075 | -47.91769 | 2025-09-08 05:21:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 22f51ce4-e4d3-3f7f-982b-673767df074c | -11.22251 | -55.01504 | 2025-09-08 05:21:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3496ac87-c120-3f62-a2cc-5ab3f4365296 | -11.21192 | -55.0027 | 2025-09-08 05:21:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 62abe1d5-4dc7-3282-88bb-605d6b0c1f96 | -10.42469 | -60.74771 | 2025-09-08 05:21:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 58607ad2-3da7-37e7-be23-a2e9c80b3d39 | -12.62671 | -56.98141 | 2025-09-08 05:21:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| ac6a1b33-b767-3179-ac27-030702535aea | -9.99471 | -51.68488 | 2025-09-08 05:21:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5c3770d2-a5c9-3d7d-9a35-08bffdc06d77 | -6.62561 | -53.36159 | 2025-09-08 05:21:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 512ad468-3309-3f07-8b41-3e655d2d665d | -11.01864 | -46.02312 | 2025-09-08 05:21:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1af35f7f-a59a-39d9-b172-656eb2fbe5c8 | -11.41232 | -50.38438 | 2025-09-08 05:21:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 56becf1f-35f8-3433-81fb-1f4d98aff5b1 | -9.46048 | -56.04682 | 2025-09-08 05:21:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a04b8b10-8698-3811-93a2-76044c84be57 | -6.16491 | -57.93858 | 2025-09-08 05:21:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| da36c044-a079-3852-ba6c-9c30b4df67c8 | -12.61333 | -56.97047 | 2025-09-08 05:21:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a6092d05-546f-3238-bd2c-5a78905af93e | -10.08723 | -59.18027 | 2025-09-08 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 514d7363-6d13-3e03-bad8-3a44c695800d | -11.20738 | -55.00565 | 2025-09-08 05:21:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bf481388-c334-3c16-9309-1115c16303f4 | -9.12562 | -65.95951 | 2025-09-08 05:21:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6c79e127-8323-3460-9f20-4de6771538ad | -9.95232 | -51.18752 | 2025-09-08 05:21:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1fc3ef8c-74f4-320a-a084-4c3ef9afaf00 | -10.43065 | -59.6066 | 2025-09-08 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a487ff92-75c1-3cdb-ba9b-324b8aa015ec | -12.94585 | -54.7995 | 2025-09-08 05:21:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0489ab78-ecef-3a5c-b30a-f122d82003a9 | -12.82942 | -52.93999 | 2025-09-08 05:21:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| de4f58b0-4755-39da-b357-c4ef25ce15cf | -13.81387 | -46.25354 | 2025-09-08 05:21:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f626ba0b-f21d-3245-832e-1df0c3786dcb | -10.88225 | -55.71788 | 2025-09-08 05:21:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1db784f8-fe3f-3715-8720-8d3222d59c67 | -9.20205 | -65.90551 | 2025-09-08 05:21:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2740259a-ae88-3dbe-9bf1-cfce545b61d0 | -10.41463 | -60.7461 | 2025-09-08 05:21:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 79a6c635-5f8c-3afc-a02a-e777ab6f39ad | -11.21949 | -55.00738 | 2025-09-08 05:21:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1d6b8dce-0920-330b-9f8a-ad50e47ee545 | -12.93119 | -54.78165 | 2025-09-08 05:21:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2c91a7ea-c8b7-3528-af5c-03be6f0d4663 | -8.21097 | -50.14198 | 2025-09-08 05:21:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7dbd15da-c22d-34da-ad48-83b2a9b7480a | -11.40486 | -60.60488 | 2025-09-08 05:21:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 19cdd2cc-f38f-3e30-9b63-bc6e96fd6a51 | -6.63286 | -53.37059 | 2025-09-08 05:21:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3467b38e-b548-3cf5-9c8a-dc1989406f68 | -9.95704 | -51.19146 | 2025-09-08 05:21:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| eb3dd9fb-da83-3e59-bc42-9f729a866b69 | -6.82884 | -52.80426 | 2025-09-08 05:21:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7d1c2a0d-498d-3342-a48c-3590bf6b1f50 | -9.99841 | -51.65653 | 2025-09-08 05:21:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 06639700-cb3d-33ec-9e35-725673d6ee01 | -11.02945 | -45.94161 | 2025-09-08 05:21:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 88cdfe59-d03a-33fe-8a6f-e65f606ca177 | -11.87575 | -50.95964 | 2025-09-08 05:21:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README81.md)
