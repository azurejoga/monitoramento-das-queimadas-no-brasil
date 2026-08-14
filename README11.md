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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3e8ae58b-a563-333e-a451-b326bfee0580 | -6.91186 | -43.63385 | 2026-08-14 04:12:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 2a4a7451-d61e-330d-9a07-914d413cef19 | -2.57373 | -47.24931 | 2026-08-14 04:12:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| acaa7ed8-0b9c-3d4c-8cad-3cdb2e34da93 | -4.48898 | -42.55713 | 2026-08-14 04:12:00 | NPP-375D | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 1a891f48-d44f-3a23-9704-f1e9238d59f0 | -6.91921 | -43.63504 | 2026-08-14 04:12:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 2cb0ea40-bb27-31a3-b4d8-53e9471d3fe2 | -4.72094 | -42.76805 | 2026-08-14 04:12:00 | NPP-375D | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d2809516-cb0b-3361-b36c-13cbef09b00e | -4.50368 | -42.54654 | 2026-08-14 04:12:00 | NPP-375D | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 15b25352-c84f-3cd2-99ff-4de92a48200d | -7.00153 | -44.83099 | 2026-08-14 04:12:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b6050257-1cfe-32f6-9443-6fe700126fc4 | -2.69675 | -48.21643 | 2026-08-14 04:12:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 500e30cc-cb66-3ed1-b538-ecd51a3f1e6e | -6.8494 | -42.90942 | 2026-08-14 04:12:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 71ee6c07-4cc2-3a7c-99eb-f8a68b8f815e | -4.49586 | -42.54946 | 2026-08-14 04:12:00 | NPP-375D | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 7a22cf46-7cf3-3c01-80cc-534f503f0cc4 | -4.50144 | -42.53786 | 2026-08-14 04:12:00 | NPP-375D | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 13.8 |
| 75f57143-773d-3fa3-b0c1-d029620176ea | -2.69215 | -48.22041 | 2026-08-14 04:12:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 199e63b0-62c3-3fa4-978b-96b1a76189f9 | -2.69034 | -48.22205 | 2026-08-14 04:12:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 01084728-37d4-32b3-9ecb-0a41338da4bb | -6.86062 | -38.35168 | 2026-08-14 04:12:00 | NPP-375D | MARIZÓPOLIS | PARAÍBA | Brasil | 2509156 | 25 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 21bb1615-7560-351a-a27d-0d7ae6166d2a | -6.9976 | -44.8303 | 2026-08-14 04:12:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| af2d91de-0dcd-3138-b4d0-60a95a7b712b | -6.19188 | -45.24551 | 2026-08-14 04:12:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fa689fb9-94d0-3033-b515-41aef07a3ec5 | -4.50077 | -42.54191 | 2026-08-14 04:12:00 | NPP-375D | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 13.7 |
| 1c4c10e7-8e4d-3408-ba92-866a634f8eee | -6.59407 | -44.55879 | 2026-08-14 04:12:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7b97570d-8a5d-374b-9f98-298b7fde0f4f | -2.79625 | -49.58559 | 2026-08-14 04:12:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| be134e1b-18fd-3fc0-8d58-50a832395b5d | -5.31822 | -43.55912 | 2026-08-14 04:12:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 806bfc15-0b9f-317a-be92-089b5ec49266 | -2.64995 | -47.98509 | 2026-08-14 04:12:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 66e392b4-eaca-3a34-9db3-38fb0db5c171 | -2.69145 | -48.21556 | 2026-08-14 04:12:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ae115be1-4757-3969-8cb0-fdeb6ea513f7 | -4.50658 | -42.55118 | 2026-08-14 04:12:00 | NPP-375D | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| a97110f2-5810-32c1-adf2-c46f977c2503 | -6.24522 | -47.69716 | 2026-08-14 04:12:00 | NPP-375D | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 6eafe146-088a-3091-b8dd-f540c9645435 | -6.41046 | -39.26446 | 2026-08-14 04:12:00 | NPP-375D | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | 5.9 |
| ebc29547-a9b5-3687-836d-63d3f7099924 | -7.60743 | -42.73718 | 2026-08-14 04:12:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d19dc48e-ca7d-33eb-aae4-46a376eefdf7 | -4.79392 | -40.0434 | 2026-08-14 04:12:00 | NPP-375D | MONSENHOR TABOSA | CEARÁ | Brasil | 2308609 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 27ce7414-710e-35e4-8550-4316f5ce6c75 | -7.45361 | -46.15272 | 2026-08-14 04:12:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 02ab798e-aa3c-3f26-94c8-da9479615427 | -4.50501 | -42.53844 | 2026-08-14 04:12:00 | NPP-375D | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 21.4 |
| 10e97439-56d1-3638-bc9d-f79abe1d9a94 | -2.90662 | -40.39259 | 2026-08-14 04:12:00 | NPP-375D | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 375bd0a1-d9b2-3fde-88e2-b9da5856db79 | -2.64528 | -47.98098 | 2026-08-14 04:12:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 487690c0-2a38-39a7-a161-8f3d30d31bc6 | -6.9257 | -41.9967 | 2026-08-14 04:12:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 703cda89-01d7-3386-8377-71f38523ceca | -4.49228 | -42.54888 | 2026-08-14 04:12:00 | NPP-375D | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| f9cb55c5-de1f-3ccd-9907-cb761e2152d8 | -4.49093 | -42.54493 | 2026-08-14 04:12:00 | NPP-375D | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| c394324e-462e-31ca-a77a-927f97772bb9 | -6.6774 | -43.40583 | 2026-08-14 04:12:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e8bffcaa-ed14-38b7-a228-4f73efb5406a | -4.49161 | -42.55294 | 2026-08-14 04:12:00 | NPP-375D | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 2ae706a2-6b8f-38ff-9644-aea448a6565e | -6.2623 | -43.27337 | 2026-08-14 04:12:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cbf54fc7-1e34-3627-bf84-a9940ad1da0d | -6.90745 | -43.63762 | 2026-08-14 04:12:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 12522300-df32-3085-86c7-3331f3b84da4 | -4.74329 | -48.02062 | 2026-08-14 04:12:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 280d6236-8db4-37bd-a0be-4e01fe831d73 | -4.49719 | -42.54135 | 2026-08-14 04:12:00 | NPP-375D | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 13.7 |
| 99c7202a-24d0-3e3d-a98b-3e6a22db16c9 | -6.3463 | -40.96992 | 2026-08-14 04:12:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| a8d16538-fcb4-3988-a960-12d75df20648 | -6.91614 | -43.63627 | 2026-08-14 04:12:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| dea01a6b-7e08-3594-9b36-818967b156ed | -5.78276 | -45.05505 | 2026-08-14 04:12:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8d8acb91-65ce-3608-b376-c58c882a1815 | -4.49321 | -42.55363 | 2026-08-14 04:12:00 | NPP-375D | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 1eb4bd13-1aa1-369f-b148-9b2ea20ceefd | -4.52597 | -38.54926 | 2026-08-14 04:12:00 | NPP-375D | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 10e644c1-b4fd-339b-808c-a2f39a2e9820 | -4.50301 | -42.55059 | 2026-08-14 04:12:00 | NPP-375D | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 3591e6bc-6151-3962-9676-04973788351a | -8.07127 | -35.61211 | 2026-08-14 04:12:00 | NPP-375D | PASSIRA | PERNAMBUCO | Brasil | 2610509 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| adb0732e-2704-3214-85c0-bc8c4b0c7c65 | -6.41824 | -39.25852 | 2026-08-14 04:12:00 | NPP-375D | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 6ced1217-9f17-3215-9b23-2c5a65f8f93f | -6.11416 | -44.02691 | 2026-08-14 04:12:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 8d721427-376e-349f-86c0-bd00dc8130fb | -8.07041 | -35.60952 | 2026-08-14 04:12:00 | NPP-375D | PASSIRA | PERNAMBUCO | Brasil | 2610509 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 4982f7ee-8a50-3522-90eb-433dd7587db1 | -2.6962 | -48.21967 | 2026-08-14 04:12:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ecc13291-0177-30d6-bdc7-0d3b0c27fb41 | -6.88502 | -43.71129 | 2026-08-14 04:12:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8c2082f3-1051-328f-9200-833267905099 | -6.92288 | -43.63564 | 2026-08-14 04:12:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5b2aa3aa-86be-3f0a-8f2f-ec7f4fa5e06b | -5.788 | -45.0486 | 2026-08-14 04:12:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 19b2fab5-98b3-3794-8e03-55b89f0fa885 | -5.48799 | -43.67688 | 2026-08-14 04:12:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9416f1a4-976b-3c8c-a0ad-d7d0f5a2b2a8 | -6.91176 | -43.64003 | 2026-08-14 04:12:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| a69c8f2c-56a3-31ef-b9f2-802d20d5d780 | -4.49385 | -42.54957 | 2026-08-14 04:12:00 | NPP-375D | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| dbcc70f6-a4c5-335e-8734-b45e1be7a4bf | -4.50725 | -42.54712 | 2026-08-14 04:12:00 | NPP-375D | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 032e791f-c7af-345a-811e-0550007d3c1c | -4.27164 | -49.3695 | 2026-08-14 04:12:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6d436283-d5bc-30d4-a88f-d0e423f723aa | -6.26594 | -43.27396 | 2026-08-14 04:12:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 88f364cc-ef0c-3408-8504-c7d24695ee17 | -2.6909 | -48.2188 | 2026-08-14 04:12:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d21e66e8-97f4-3a16-ad3b-44a8fc5f8df0 | -4.1048 | -50.44375 | 2026-08-14 04:12:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 3c244967-c49f-37f0-af68-a26929c0ab21 | -4.25077 | -48.54656 | 2026-08-14 04:12:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1774636d-34ff-3e02-a8f9-fa09d17efd3c | -6.97653 | -41.46738 | 2026-08-14 04:12:00 | NPP-375D | SANTANA DO PIAUÍ | PIAUÍ | Brasil | 2209351 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 231ad18c-cd35-389e-b077-79902ed3d801 | -6.86869 | -42.92498 | 2026-08-14 04:12:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 63e873dd-20e1-34bb-98a7-33ae0ac57e63 | -6.83876 | -42.90775 | 2026-08-14 04:12:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| ee9d3680-ad5b-341b-b3af-cb25170ea37c | -4.25135 | -48.54323 | 2026-08-14 04:12:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e832e144-b5e2-38b9-9922-c8467b5646c0 | -2.65049 | -47.98187 | 2026-08-14 04:12:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b1bcdbf1-0c3b-31a6-ae03-ef2291e3b8f4 | -7.00237 | -44.82598 | 2026-08-14 04:12:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e482b024-4ae4-37c6-be0d-6793f239f4cc | -5.59385 | -37.74025 | 2026-08-14 04:12:00 | NPP-375D | FELIPE GUERRA | RIO GRANDE DO NORTE | Brasil | 2403707 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b96dfb91-b206-3161-be94-7a57bb672797 | -4.11077 | -50.44491 | 2026-08-14 04:12:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ebe21687-2db0-3d81-875b-92086de997ab | -6.92913 | -41.99722 | 2026-08-14 04:12:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 2841bdd8-3e0d-36b7-b680-7829ab3e510b | -6.91039 | -43.64254 | 2026-08-14 04:12:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ee38cc11-b7a8-3e08-b80f-ee02d3aa349b | -5.55574 | -43.96605 | 2026-08-14 04:12:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2fe0c756-cf2c-30bc-b4ef-b08deaf512c1 | -4.64222 | -50.92937 | 2026-08-14 04:12:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 15cb1029-97f8-3cfc-9304-02106f1f7f61 | -4.40717 | -42.14443 | 2026-08-14 04:12:00 | NPP-375D | BOA HORA | PIAUÍ | Brasil | 2201770 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| d6dbeb26-b01c-3f6c-bdd2-61a058ee798c | -6.80714 | -44.88294 | 2026-08-14 04:12:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6040b5fa-cd19-3d2f-81e3-a4d7a1859617 | -4.19714 | -46.81243 | 2026-08-14 04:12:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b42b9a88-9ad2-331c-80fa-d4771c9a2f4b | -2.69798 | -48.21805 | 2026-08-14 04:12:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 614015c6-795c-3601-aa88-939ba7dfa4e8 | -6.86005 | -38.3554 | 2026-08-14 04:12:00 | NPP-375D | MARIZÓPOLIS | PARAÍBA | Brasil | 2509156 | 25 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 404bd4a2-9f6f-327d-8e6a-7fad83a771c8 | -4.19243 | -46.8117 | 2026-08-14 04:12:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f6fdb2fc-7af8-3f05-b3b4-eeee4a55d2b1 | -4.49028 | -42.549 | 2026-08-14 04:12:00 | NPP-375D | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 539d0aae-6877-366e-a711-c7a1bd02adfa | -5.48726 | -43.68138 | 2026-08-14 04:12:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 56ddaf43-3416-3107-9d1b-049d27b00ffb | -6.85663 | -38.35487 | 2026-08-14 04:12:00 | NPP-375D | MARIZÓPOLIS | PARAÍBA | Brasil | 2509156 | 25 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 46790dac-b551-3b05-9671-905e0d7a3dd9 | -6.90879 | -43.63508 | 2026-08-14 04:12:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 793e856a-28b8-32df-ab54-54652d39963f | -6.84652 | -42.90481 | 2026-08-14 04:12:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a0611f19-45ad-3cfa-a576-444b05cef273 | -4.49256 | -42.5577 | 2026-08-14 04:12:00 | NPP-375D | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 7.8 |
| f6c68753-6769-3414-a793-235a853ab692 | -6.99844 | -44.82527 | 2026-08-14 04:12:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 05c50734-54cd-3401-88d9-42be0def3c38 | -7.61157 | -42.73387 | 2026-08-14 04:12:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 25f28d1b-2ca6-3f9a-9c1a-c745fbea4a0c | -6.26524 | -43.27818 | 2026-08-14 04:12:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ac601ef7-a4bb-327c-9c46-a90b18769f2e | -3.33971 | -50.14872 | 2026-08-14 04:12:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0c858bf6-3435-3eb4-a7cd-bee1a1a693cc | -4.4945 | -42.54551 | 2026-08-14 04:12:00 | NPP-375D | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 3bc64e8a-525e-382b-9115-02a4f67b0333 | -4.10402 | -50.44827 | 2026-08-14 04:12:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| d1883ef3-297c-36dc-af44-de8d6f152018 | -5.59732 | -37.74079 | 2026-08-14 04:12:00 | NPP-375D | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 33404882-99f1-35c2-b371-c1b1d6da173e | -2.64581 | -47.97779 | 2026-08-14 04:12:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f439e15c-6369-38c0-bc6e-7cf7fdeb67b3 | -3.34046 | -50.14442 | 2026-08-14 04:12:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b875fe93-e374-3f26-9186-bfc1746155a5 | -2.69268 | -48.21715 | 2026-08-14 04:12:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2d2bbc64-8b38-38b1-a64a-1f8487f49df3 | -6.91904 | -45.73454 | 2026-08-14 04:12:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d6b821c1-e057-34ae-9143-134bf625f2de | -6.44909 | -41.91689 | 2026-08-14 04:12:00 | NPP-375D | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| f3e3ed77-ef22-3660-bcdc-50afb866402b | -6.98459 | -41.2896 | 2026-08-14 04:12:00 | NPP-375D | SANTO ANTÔNIO DE LISBOA | PIAUÍ | Brasil | 2209401 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |


[Clique aqui para ver as próximas entradas](README12.md)
