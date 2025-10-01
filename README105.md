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

## Dados Diários - Página 105

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c47b8963-58ba-3bb1-8bea-92e9868f8238 | -11.5698 | -50.18528 | 2025-10-01 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 1783349f-1c47-36d7-8b2b-a74c9c928f95 | -14.71744 | -48.13967 | 2025-10-01 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 53194a7c-2705-379c-8d14-cb8268e3be33 | -10.6243 | -48.59956 | 2025-10-01 04:51:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c94f18b2-cd6d-3234-ae15-ba1ac10d6e3f | -13.28188 | -47.23102 | 2025-10-01 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fe57fa94-3e68-31d8-9ff4-bfe7b7bdbc19 | -14.5262 | -48.37429 | 2025-10-01 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3b53eb8a-ae96-3c7b-866e-f7d8881ee592 | -10.9071 | -46.53159 | 2025-10-01 04:51:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 2d48fb56-2bd6-361a-8fbc-4590d111fbe2 | -11.12809 | -49.78886 | 2025-10-01 04:51:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1c995916-5891-3239-a184-9053f9771e9b | -11.68725 | -46.84775 | 2025-10-01 04:51:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7f604037-1762-3ba8-8d38-0bdc93931354 | -15.35524 | -47.07835 | 2025-10-01 04:51:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 113cd4f6-88c2-3c42-922c-abd2d527d5fb | -12.37718 | -49.92832 | 2025-10-01 04:51:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 79c0fe50-6064-349a-9d84-945417abc9ec | -13.45652 | -47.24557 | 2025-10-01 04:51:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| afdd0328-c3e3-3df1-8d8a-26e78a81e47b | -12.37777 | -49.92432 | 2025-10-01 04:51:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 90425c9d-2b16-3b14-896d-128d8a2e1183 | -14.00082 | -45.02214 | 2025-10-01 04:51:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 86964603-c0c2-3a16-9aef-0d895cbd87fd | -11.96745 | -46.59228 | 2025-10-01 04:51:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5ad77ab3-8a9d-3242-93e5-cc8a5de48ef6 | -13.73613 | -48.81786 | 2025-10-01 04:51:00 | NPP-375D | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 57aefb1e-95ac-3488-a385-8dd628f24b11 | -14.68773 | -48.11923 | 2025-10-01 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| c0131fb0-d6b7-3bbf-984b-f9789c0112c5 | -12.95166 | -46.42181 | 2025-10-01 04:51:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 1e84f3c7-54ed-31c7-8392-9e5fcc98087d | -12.08831 | -47.25887 | 2025-10-01 04:51:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| ec0dca8a-3f32-3c3e-a4ff-8f25795407c2 | -10.28455 | -50.46283 | 2025-10-01 04:51:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| afefd0da-5f40-32c6-a8a9-98fcf81df820 | -11.81507 | -44.97739 | 2025-10-01 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3e8b5b10-cda9-325b-944f-7fa79354180f | -9.39384 | -54.69881 | 2025-10-01 04:51:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 469702ad-e4ff-33d5-926a-7b2dcac10fe2 | -11.82992 | -44.97395 | 2025-10-01 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 48c91922-4a48-35e2-bd0a-fe73a203d01c | -14.52618 | -48.37053 | 2025-10-01 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 558be953-0c26-3fa9-88ef-c0845ebb3c35 | -11.19933 | -47.73552 | 2025-10-01 04:51:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2e173323-fe09-31df-9761-dfbc76f18b51 | -14.39148 | -54.91029 | 2025-10-01 04:51:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6e4f6a2e-1725-339b-b301-f504bff04415 | -11.96323 | -46.59161 | 2025-10-01 04:51:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 03150996-1ceb-3232-8eeb-fb1994229012 | -13.77289 | -48.3245 | 2025-10-01 04:51:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b2b21c6c-7917-34bc-bc17-a71ecaf2bbf9 | -13.81681 | -47.50432 | 2025-10-01 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ab204073-e90d-3e7e-909b-f5d3b65ead2b | -16.01331 | -50.89959 | 2025-10-01 04:51:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6a2408e5-c518-3d2e-8f33-9a30bca9f63a | -11.02272 | -49.82104 | 2025-10-01 04:51:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7f161e33-7754-39b3-b788-eaf985174234 | -15.44611 | -43.64295 | 2025-10-01 04:51:00 | NPP-375D | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 1d2a6256-151e-3a12-addb-2f4a69cfe257 | -10.48591 | -55.58424 | 2025-10-01 04:51:00 | NPP-375D | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2779b158-caaf-34d9-931b-795f43afb6af | -14.89477 | -48.11554 | 2025-10-01 04:51:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 7de3faa5-209d-3fbd-a1d2-3138d4fb0d7b | -14.88262 | -48.3264 | 2025-10-01 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 00923c4f-5d82-32af-af25-79fefc489b2e | -15.764 | -43.67762 | 2025-10-01 04:51:00 | NPP-375D | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d25ec145-aadc-3edf-ad36-84a7c0aee601 | -13.80989 | -47.49378 | 2025-10-01 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 61d48aea-ded0-30ff-b0c6-f78567db8095 | -14.90604 | -47.20944 | 2025-10-01 04:51:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 486312d5-9a89-38a1-b81b-0e25c7131739 | -12.00103 | -46.59209 | 2025-10-01 04:51:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4f649ce3-4e9a-3250-a377-616620a73fe9 | -14.04265 | -47.99036 | 2025-10-01 04:51:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d95acd25-344e-3443-b8d1-fac105060647 | -14.3461 | -45.909 | 2025-10-01 04:51:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5c69036b-ceaf-3ca4-8f22-3d1589d6b43f | -14.20774 | -44.92804 | 2025-10-01 04:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bf1cc338-66de-3ad1-8c57-accf97d90f04 | -12.84705 | -47.02682 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| eee8ac94-2907-3e32-a854-f96542f17312 | -14.83697 | -51.74119 | 2025-10-01 04:51:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| df2c48cc-7b1a-3123-be12-84ec509b404b | -14.79282 | -45.78924 | 2025-10-01 04:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 909b3464-3801-3a24-8fe4-e9df8b39f596 | -9.4471 | -47.9222 | 2025-10-01 04:51:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 68bdb470-875a-39ee-a51b-c80792d61ccc | -16.37049 | -47.04791 | 2025-10-01 04:51:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0aecdeed-2d62-306a-9727-5b283cedcdef | -11.20052 | -47.75519 | 2025-10-01 04:51:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0b858e3f-e93b-3661-b0d5-9f491ebf2afd | -14.68709 | -48.12394 | 2025-10-01 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 84f7dca4-8dab-31f6-b1f3-bbf76f9b5557 | -13.76091 | -48.40451 | 2025-10-01 04:51:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3a683910-280d-3c56-96eb-d5073b6440c3 | -15.36209 | -44.15126 | 2025-10-01 04:51:00 | NPP-375D | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6a6c2bfc-8107-304f-a30f-787d757ee983 | -15.34345 | -47.84529 | 2025-10-01 04:51:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cf8f58de-5227-3b8f-b794-5db00ee86ce0 | -13.98587 | -44.91894 | 2025-10-01 04:51:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 74be5ef6-b027-3b43-ab60-3a60fb836030 | -15.06273 | -45.04241 | 2025-10-01 04:51:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| de62a4c8-5513-3195-a109-798ed13916a9 | -11.33243 | -56.20835 | 2025-10-01 04:51:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3cf40982-1e45-33a1-a45b-ae5670360095 | -11.04744 | -47.81903 | 2025-10-01 04:51:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e3d23cc8-38eb-37d6-b6d3-85e37d69bbf4 | -14.10189 | -44.30797 | 2025-10-01 04:51:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8aab2d57-4093-31ed-b23d-90485156ddc2 | -11.81375 | -44.98742 | 2025-10-01 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 235bb477-9732-33b8-a10b-b541b93caee1 | -13.66178 | -48.03573 | 2025-10-01 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e18927db-b49e-3a7f-9ff2-c4705390f109 | -11.8131 | -44.99236 | 2025-10-01 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 36ce25c1-157c-3d90-86f2-95afd7379970 | -9.9408 | -43.59256 | 2025-10-01 04:51:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c7d25096-1871-3326-bad0-9c11613edf60 | -11.93837 | -47.08442 | 2025-10-01 04:51:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5c8ef5bc-1801-3128-a270-265d38bdaca3 | -13.37743 | -48.10395 | 2025-10-01 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| aaf384e7-0ce8-3b17-8d38-0484efe6944f | -11.46766 | -45.00432 | 2025-10-01 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| bd8d7cc2-34fe-3b82-95fe-4cb7e72bd2bf | -10.64058 | -48.52864 | 2025-10-01 04:51:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 33f51eba-d36d-3ad5-9bc6-ac08358a795c | -11.43511 | -55.03833 | 2025-10-01 04:51:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e0c23436-6507-37c0-a15f-a3e7826fd045 | -14.50424 | -48.41692 | 2025-10-01 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 655e3569-abbe-3dd6-98c9-f49a127e86e0 | -16.02732 | -50.90173 | 2025-10-01 04:51:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 67b3c531-4c1a-316a-8582-f6a0381e66db | -10.79403 | -45.35367 | 2025-10-01 04:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8b075e8d-684c-304d-b7c8-2257984cf774 | -11.38932 | -44.89368 | 2025-10-01 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d17f16cf-0a42-3419-8437-aff8645bbfc6 | -12.75984 | -46.88294 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 13.8 |
| b77e011f-e9d4-3008-aa21-fbd000b4c45a | -10.82718 | -45.38099 | 2025-10-01 04:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.8 |
| fc20af0b-a0f6-3912-a8ac-77432ba3061c | -14.70686 | -48.2171 | 2025-10-01 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 165fa60c-92a9-3ea9-b460-fab1ad5f547d | -10.8161 | -46.63456 | 2025-10-01 04:51:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a6c8a55e-af53-33bf-ba14-40ee1383b557 | -13.32746 | -47.85798 | 2025-10-01 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1c85002f-2a39-3bfd-b265-4f96121c4d0f | -14.7869 | -45.79878 | 2025-10-01 04:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| c88b8f46-a2f8-3cb4-bbe2-1426cf4215e1 | -11.45967 | -44.97575 | 2025-10-01 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8ef60650-46fa-375d-9956-a9c710a95dfb | -9.27567 | -45.68045 | 2025-10-01 04:51:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| aeddbc27-0445-3d43-a796-829a473f46db | -10.03519 | -52.10527 | 2025-10-01 04:51:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 36c48e09-1f85-3766-b6c7-1009fb9efea9 | -12.45982 | -50.22147 | 2025-10-01 04:51:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 66c56e0d-a392-333b-8c17-d780e17041ee | -14.19042 | -46.10396 | 2025-10-01 04:51:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9d9aef3d-f812-3259-9c05-41ffc8c398be | -11.84211 | -48.05922 | 2025-10-01 04:51:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 99b5dadd-faa4-35a8-984f-a685a8c7588c | -8.97259 | -50.26613 | 2025-10-01 04:51:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dcb4241e-9c28-312e-9b4c-95b365e1bc43 | -14.19255 | -46.12236 | 2025-10-01 04:51:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b8ce894b-2d21-3ac9-a5ea-bd83e5ac790e | -13.97759 | -45.06145 | 2025-10-01 04:51:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 71a9e066-5031-32c9-8a02-a31a4b01dd42 | -9.92915 | -43.67484 | 2025-10-01 04:51:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cb293c2a-2538-3c81-b206-d3640e23d5a1 | -11.43904 | -44.95179 | 2025-10-01 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a53dba3b-6633-38a9-a897-c40369048bd6 | -16.19733 | -50.00095 | 2025-10-01 04:51:00 | NPP-375D | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 498283f7-2966-30da-8ac9-b403a39c5009 | -14.41385 | -47.14296 | 2025-10-01 04:51:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 12390f05-03ba-3c13-97f9-c8eed7e89b91 | -13.16308 | -42.3556 | 2025-10-01 04:51:00 | NPP-375D | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| b5dcb558-0cb6-39c8-8b47-735a7b8bc685 | -14.68359 | -48.23978 | 2025-10-01 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5881982a-35fc-3c68-883c-0d14a83fc672 | -12.83355 | -47.03245 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1a4b2259-f9ac-3a5f-83e7-1297aa72a611 | -9.92694 | -43.65581 | 2025-10-01 04:51:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a0cf2b21-3b45-3d9b-b779-9f9552c0f74e | -12.82313 | -47.0154 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| da51df75-6700-35a3-8af5-a1c8af4899d3 | -14.6801 | -45.29235 | 2025-10-01 04:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 496e3cdd-1e2d-366a-afce-155011b8332b | -12.90532 | -46.82174 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b1a95a93-dc2a-33e7-9f1c-ee2e2c10730b | -12.77513 | -46.86526 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 319d984a-7e6b-3e7c-9686-7761e8ce5660 | -15.24187 | -50.08107 | 2025-10-01 04:51:00 | NPP-375D | MORRO AGUDO DE GOIÁS | GOIÁS | Brasil | 5213855 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 12c967a6-27cc-34be-a451-75e4239e58dd | -14.17563 | -46.11151 | 2025-10-01 04:51:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6336156e-46f5-31b9-9304-3dfdcba7de88 | -16.37564 | -47.07695 | 2025-10-01 04:51:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 31426fd2-a515-3850-ade6-346a056a0d64 | -14.44016 | -46.36317 | 2025-10-01 04:51:00 | NPP-375D | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README106.md)
