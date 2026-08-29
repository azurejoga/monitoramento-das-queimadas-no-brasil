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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bacc7af9-5e10-36fe-9b8d-82d17e4419b7 | -14.21081 | -45.30544 | 2026-08-29 04:34:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 72dc6585-1158-3e64-b25d-a1652316fafa | -11.03736 | -57.22237 | 2026-08-29 04:34:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1efec901-c9bb-3bbb-9b9b-b8da08b8ab60 | -10.75633 | -50.64368 | 2026-08-29 04:34:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 26878019-a85a-37e0-8ee6-51a8facc6703 | -16.51202 | -49.25321 | 2026-08-29 04:34:00 | NPP-375D | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 330bd18c-beca-3418-82a1-92521e114f0b | -10.75589 | -54.04316 | 2026-08-29 04:34:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9bcc80d1-81ed-3cd6-8bd2-5e14264caa81 | -17.05779 | -39.86758 | 2026-08-29 04:34:00 | NPP-375D | ITAMARAJU | BAHIA | Brasil | 2915601 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 7b3b71bf-b47a-34c1-867b-9ec7f8a47c9f | -9.97404 | -53.93335 | 2026-08-29 04:34:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 9.7 |
| c460778d-a6b6-3e73-a8e4-45cabff77e68 | -13.4258 | -54.02171 | 2026-08-29 04:34:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8b7c145b-b8a8-3b39-adc7-8409fed58f54 | -11.18128 | -51.28733 | 2026-08-29 04:34:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 06197161-8511-316e-8307-386d1ea83828 | -11.02513 | -57.24985 | 2026-08-29 04:34:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| abbb962f-fc22-32b3-b7bc-e47ba30085d7 | -14.41304 | -51.73862 | 2026-08-29 04:34:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 11566f75-49ac-33c4-829b-0164156aa21a | -15.57142 | -42.71518 | 2026-08-29 04:34:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 2e717588-cf5c-39bd-9454-8fde41c48f3e | -11.24194 | -53.99684 | 2026-08-29 04:34:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0e944472-87b3-3781-8f79-875bfb9cc5bf | -14.17694 | -48.76221 | 2026-08-29 04:34:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6df7d910-167b-3b24-a410-fa18ad85fe5c | -10.50816 | -59.62613 | 2026-08-29 04:34:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9279e207-9b39-3a44-b4a9-ebed6faf3a69 | -13.66974 | -47.75027 | 2026-08-29 04:34:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 37f5d7d0-ed84-38d6-831f-d29819b6106b | -15.65026 | -45.9309 | 2026-08-29 04:34:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 5cc136b1-35d7-3ef0-8a0d-8759207eefa5 | -14.76242 | -48.7489 | 2026-08-29 04:34:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9d29c0a0-025f-3ff6-b3de-9bf16ec9e416 | -12.43128 | -43.41012 | 2026-08-29 04:34:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 04c72a44-9eb0-366b-bce1-51507b55cf0d | -12.24924 | -50.53468 | 2026-08-29 04:34:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1fbe5818-3615-37c0-9974-ecf78741c58c | -11.26561 | -54.0374 | 2026-08-29 04:34:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9113c7b0-ce07-31b4-a48c-99b5fd630730 | -17.76987 | -48.60577 | 2026-08-29 04:34:00 | NPP-375D | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a40a469e-2dde-31fa-90cc-9f8ce8b56317 | -15.65802 | -48.3727 | 2026-08-29 04:34:00 | NPP-375D | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 322c992b-8ce9-3add-8ffa-eb14ed4ffba3 | -13.66202 | -47.73397 | 2026-08-29 04:34:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 55037b39-b6ba-35c4-8fcd-0cd4fa1d9bff | -15.12605 | -53.5791 | 2026-08-29 04:34:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 29.9 |
| a645b839-c1b0-3edb-b3c0-5aa323a15152 | -14.18927 | -48.75236 | 2026-08-29 04:34:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e7ef3fe9-a9a7-32ec-8d42-c4d7d0e32ee8 | -11.48056 | -46.94748 | 2026-08-29 04:34:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8cf7c381-87c5-3d14-911d-4bb3aafab8a7 | -12.69024 | -48.42857 | 2026-08-29 04:34:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6ddfb2b1-def6-34e2-a96a-c5e8ed78b2e1 | -17.59742 | -51.61186 | 2026-08-29 04:34:00 | NPP-375D | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 97b1ba60-f741-3e51-a599-351a3f0679af | -12.77292 | -46.4491 | 2026-08-29 04:34:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 39c0c2e7-ef26-3617-8c97-bd704a7ef921 | -11.04573 | -57.21051 | 2026-08-29 04:34:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3f95c666-bf3d-3cf8-9dc1-360616a8207e | -11.71159 | -54.53733 | 2026-08-29 04:34:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c4321d1e-665f-310d-aa14-bd3722747089 | -14.16478 | -52.83224 | 2026-08-29 04:34:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f88400c4-4c1a-3703-8403-4a64cac7fad1 | -14.92509 | -41.30635 | 2026-08-29 04:34:00 | NPP-375D | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| f9901483-9858-3100-9f58-c75b10f2870e | -11.48666 | -46.95225 | 2026-08-29 04:34:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 61deb560-962a-356f-91bf-ccc0ae41470a | -16.51712 | -47.73316 | 2026-08-29 04:34:00 | NPP-375D | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 572976fa-20db-3dc1-83f2-d4d072f01e05 | -12.78621 | -46.45131 | 2026-08-29 04:34:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 02c72536-28b6-38fc-b5d2-e599667aa11c | -12.37987 | -48.19209 | 2026-08-29 04:34:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f3d6633d-1b0c-3e35-8489-cbd915eff3c9 | -11.2667 | -54.03163 | 2026-08-29 04:34:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b310f7cb-1db0-3177-beca-fbe9f9eaada8 | -10.82912 | -50.50824 | 2026-08-29 04:34:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 44b49336-829f-3830-b25a-b713d7bd48ba | -14.4047 | -52.57385 | 2026-08-29 04:34:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a251fe16-6477-308d-ae71-61a5589f71b9 | -14.20292 | -52.84402 | 2026-08-29 04:34:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b5384065-47e6-39f7-beff-eaf3c5b39eac | -11.03873 | -57.21389 | 2026-08-29 04:34:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| dac3d965-e8f9-362b-9ee6-3b581c393297 | -11.18359 | -51.28705 | 2026-08-29 04:34:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 915109df-472e-3031-922d-a46091f4940f | -11.17975 | -51.27162 | 2026-08-29 04:34:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 47b83ec6-f186-3003-adae-4913b97ed3d3 | -11.03279 | -57.24583 | 2026-08-29 04:34:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4dbce874-9fc8-3012-be2d-f421bd16ddfe | -14.2045 | -52.83543 | 2026-08-29 04:34:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c5c15afc-eff2-3265-a1be-4f11d95c3d6b | -11.72169 | -54.53936 | 2026-08-29 04:34:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c5a8dcd8-b10e-35e0-9517-52f1be66360e | -16.47894 | -49.4295 | 2026-08-29 04:34:00 | NPP-375D | GOIANIRA | GOIÁS | Brasil | 5208806 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 33d04739-0a1d-30c9-874b-8843a73151cd | -11.61509 | -46.73139 | 2026-08-29 04:34:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1ed3195e-5b3d-304e-91b3-93182af8311e | -15.10306 | -48.1556 | 2026-08-29 04:34:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fb7874de-49fb-3569-9353-60eb1712a012 | -12.78897 | -46.4554 | 2026-08-29 04:34:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1d7a35c9-4495-365b-be0b-e33e696dd0bb | -12.76509 | -44.26594 | 2026-08-29 04:34:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8c757b69-df05-3a71-aaca-94830702835b | -14.18452 | -48.75951 | 2026-08-29 04:34:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 05adcc7f-317f-3db1-9054-db1a12d08ebf | -13.64796 | -47.73528 | 2026-08-29 04:34:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| bb68a298-7b9f-35c2-9a9b-ff0f5eca91ff | -14.41386 | -52.57169 | 2026-08-29 04:34:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 192d0209-d9fa-37b9-bbb1-a6137121a987 | -11.03499 | -57.23238 | 2026-08-29 04:34:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 780dd61f-6a46-3602-947f-56967f737539 | -11.65937 | -46.72423 | 2026-08-29 04:34:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 76eb5d7f-02ff-325b-9b56-68dfddd4afcc | -11.17805 | -51.27062 | 2026-08-29 04:34:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 96223c41-4260-3562-ada4-b983327f6db3 | -14.17266 | -52.83803 | 2026-08-29 04:34:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fc001176-2843-3ba5-a36f-25183f2f2b64 | -15.6538 | -46.56947 | 2026-08-29 04:34:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| d54cb760-982a-3e59-a144-052aa24e233e | -11.03265 | -57.21275 | 2026-08-29 04:34:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d8c17da6-3533-3afc-a0e5-a460c8d2312d | -14.59474 | -53.14176 | 2026-08-29 04:34:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 126d286f-d3fa-37b5-9027-00d7bce510ed | -16.4754 | -49.23847 | 2026-08-29 04:34:00 | NPP-375D | SANTO ANTÔNIO DE GOIÁS | GOIÁS | Brasil | 5219738 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 168e0d9f-9657-3911-b20d-c6c3c57ea8a8 | -11.83705 | -46.77509 | 2026-08-29 04:34:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c55f115f-25da-3a61-aa94-90f986971b66 | -14.76651 | -48.7457 | 2026-08-29 04:34:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c2506bdc-fd2e-364e-8c9c-faf0d2b6d087 | -14.30246 | -51.70287 | 2026-08-29 04:34:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f31e972f-f7da-3a2a-83f4-3d95974e39ed | -14.20211 | -52.84836 | 2026-08-29 04:34:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4d1709d2-98dc-3616-8c8f-893cbe865ced | -17.08768 | -47.18853 | 2026-08-29 04:34:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9430667f-d150-3879-8085-e40f1da8a244 | -14.91261 | -56.30952 | 2026-08-29 04:34:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c38dfc39-67f0-3751-b432-431ddcd40e41 | -11.03034 | -49.67976 | 2026-08-29 04:34:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d60e5fd5-d73c-3d32-ab02-5f96c49ae1e8 | -13.31697 | -48.1958 | 2026-08-29 04:34:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 153608d3-ce9a-36c6-899e-619969c61728 | -14.177 | -52.83881 | 2026-08-29 04:34:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 33349dd3-567f-33ea-9469-af045401f82b | -14.20371 | -52.8397 | 2026-08-29 04:34:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ccd1b403-74da-3654-a670-c45bf6f9f127 | -12.78232 | -46.45429 | 2026-08-29 04:34:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 1b6dd531-8b5d-315d-b15b-2f3e6b8663bd | -12.79229 | -46.45595 | 2026-08-29 04:34:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2245f064-cdd6-3dcb-a01e-912ed6985703 | -12.91566 | -45.87006 | 2026-08-29 04:34:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 44be03af-4215-347e-9c38-4b601be44390 | -14.16124 | -52.82722 | 2026-08-29 04:34:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 352235a4-980f-34c0-b8b8-695316958615 | -12.25611 | -50.54099 | 2026-08-29 04:34:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 73b9159a-6316-33dd-acae-4c873f65fd92 | -15.1216 | -53.57818 | 2026-08-29 04:34:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 29.9 |
| 96b6bdab-be9e-3c2c-aeda-0e06093c943b | -12.21661 | -50.53886 | 2026-08-29 04:34:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 54ed6ee7-c13e-3b02-92e5-5cea4cf34c22 | -12.77349 | -46.44556 | 2026-08-29 04:34:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 639dba1e-3a7b-38d0-9e55-8440c0e08b8c | -11.24233 | -47.04879 | 2026-08-29 04:34:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0eca7393-fb46-382e-8b2a-0207efc09d85 | -14.92096 | -41.30575 | 2026-08-29 04:34:00 | NPP-375D | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 67d62f5b-dbf1-3eee-bf92-b4265976f7c5 | -11.0382 | -57.24786 | 2026-08-29 04:34:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 81a25255-dd37-3fda-b415-6728dcb852df | -11.02605 | -57.24531 | 2026-08-29 04:34:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2b8c1d4c-f4c3-35dc-8121-c9944de9aab1 | -11.49514 | -46.94249 | 2026-08-29 04:34:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 25e2999c-b963-3215-af98-76d5f0c9f0e7 | -11.48707 | -45.09871 | 2026-08-29 04:34:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8f08f08e-e016-3df2-9120-e91efac57f09 | -11.17694 | -51.26337 | 2026-08-29 04:34:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3c48f423-953b-32fd-9f89-05a76085e52a | -11.69019 | -47.62972 | 2026-08-29 04:34:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bf1e7116-568b-33a4-9c36-9623fb558828 | -11.19396 | -55.10419 | 2026-08-29 04:34:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 94300f9d-a054-3dd4-a15c-a3ab9a277ba2 | -11.60738 | -46.93925 | 2026-08-29 04:34:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 850696e7-8cd2-373a-b3dd-887ae4b0d698 | -11.48331 | -46.95168 | 2026-08-29 04:34:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c341dda4-7932-34be-9e5a-7f86dd41190a | -11.23213 | -53.9947 | 2026-08-29 04:34:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 88059bfd-6f64-3ba8-ab9a-873129c202bb | -15.57644 | -56.29136 | 2026-08-29 04:34:00 | NPP-375D | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1890c438-dc22-39a6-a074-a73237232b8d | -11.02874 | -49.68611 | 2026-08-29 04:34:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 88243efe-75aa-358f-b1a3-999da6c1d9a0 | -17.79378 | -39.70691 | 2026-08-29 04:34:00 | NPP-375D | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| a6483776-2ddd-31b1-99da-a202453ff85e | -10.80196 | -54.01645 | 2026-08-29 04:34:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e6fb6b93-9241-347d-a1dd-902f4c5d7371 | -11.60507 | -46.72975 | 2026-08-29 04:34:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4aefb27d-db44-30c4-a0d1-ce212017a966 | -17.79296 | -39.70761 | 2026-08-29 04:34:00 | NPP-375D | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |


[Clique aqui para ver as próximas entradas](README36.md)
