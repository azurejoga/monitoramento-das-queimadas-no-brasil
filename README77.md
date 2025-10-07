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

## Dados Diários - Página 77

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5de93c39-772c-3c36-b037-21b12f9e785d | -10.85247 | -51.02987 | 2025-10-07 04:38:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bf437e93-7c75-3f30-ba5f-9797598a8bac | -16.29295 | -50.98646 | 2025-10-07 04:38:00 | NPP-375D | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f1fe0924-1f46-39f6-9528-c81a3f394eee | -18.27559 | -45.46114 | 2025-10-07 04:38:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 30db188c-9e25-38e7-aba2-e9b3bf028287 | -13.26783 | -47.59216 | 2025-10-07 04:38:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ab7b8ca4-803b-3690-b897-ee386725420f | -14.90749 | -46.85668 | 2025-10-07 04:38:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d7ca49f9-6972-312d-9195-14b3d7b389db | -11.80633 | -45.0539 | 2025-10-07 04:38:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 59efde58-9f9b-37ec-92f2-dc8917251ae1 | -14.70116 | -48.34203 | 2025-10-07 04:38:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ef8b39f9-8506-3c7b-b7e2-a8231533d5ad | -10.42211 | -50.31078 | 2025-10-07 04:38:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 063c6a88-8bd1-3f15-a478-6e7f2bdd1396 | -13.30207 | -48.05249 | 2025-10-07 04:38:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3e116ea2-9edc-3f0b-875d-3b8e596dd023 | -16.03178 | -51.0276 | 2025-10-07 04:38:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e42264fd-644f-351c-952d-9e56605d6d19 | -15.50268 | -47.92443 | 2025-10-07 04:38:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 976d5c34-4fc0-3fcb-a3e5-48970940c369 | -10.94973 | -51.18467 | 2025-10-07 04:38:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c6ab4cb9-8a91-3928-9e64-d388bc7ee624 | -10.41752 | -50.31755 | 2025-10-07 04:38:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 65226d68-f32f-3fef-9a49-3a3b36ea3b4a | -13.26145 | -47.79145 | 2025-10-07 04:38:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f560b3b2-06ba-3e71-b6b6-b258d6746f61 | -12.91993 | -54.7213 | 2025-10-07 04:38:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 76df970c-2283-35b2-9955-113b384ff5ce | -10.43147 | -51.63318 | 2025-10-07 04:38:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 84942e9b-4725-370f-b3c5-a21fe1930638 | -13.32864 | -48.03783 | 2025-10-07 04:38:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b7f173ed-7b7a-3ce8-9ea5-42077d8e8f3c | -14.91775 | -51.40719 | 2025-10-07 04:38:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d6a41f82-21a2-3b32-be94-af03e6c59187 | -13.9702 | -53.89035 | 2025-10-07 04:38:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 0242c637-b6d6-3111-9009-c6a135308b97 | -12.89623 | -54.75903 | 2025-10-07 04:38:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ef3a6741-5c21-346f-a08e-598cd28e89a9 | -14.70749 | -48.39215 | 2025-10-07 04:38:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bafd3b8c-efd4-36c3-ba63-df494614ba7c | -13.83565 | -48.02862 | 2025-10-07 04:38:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3ddf56f2-4659-3126-998f-d2217bc3e5b1 | -11.2983 | -48.26909 | 2025-10-07 04:38:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| dfa6b7f4-ff15-39db-ae94-6770bc851454 | -15.5013 | -46.8317 | 2025-10-07 04:38:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b80fa803-36f2-3d0c-8ed0-6c0ad26defcc | -14.90401 | -46.84862 | 2025-10-07 04:38:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 403c86c4-6d5c-3a01-87d1-d3bcf5ce4f2c | -11.0459 | -50.91315 | 2025-10-07 04:38:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b1ecec6a-0c6a-329e-aa12-4abdb335cb0b | -12.38099 | -51.08649 | 2025-10-07 04:38:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 86c502fb-ed12-39a1-87b3-f5e21ae0bfe8 | -11.1613 | -47.95848 | 2025-10-07 04:38:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 68b1f67a-c0b2-3bd1-90ab-5f3cb86aee00 | -11.12532 | -47.21951 | 2025-10-07 04:38:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 39e5afe3-ff0b-3bc9-914b-8d7d744175fe | -13.25784 | -47.1851 | 2025-10-07 04:38:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 743fa2c7-5386-34de-8c4e-69201c4b8836 | -10.4327 | -50.33138 | 2025-10-07 04:38:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 73018356-cd1a-3e84-a5b0-8e33a1f7e258 | -11.49181 | -44.97195 | 2025-10-07 04:38:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6fc30826-2d9e-3d2a-903c-5bfe568ee435 | -13.2778 | -48.07496 | 2025-10-07 04:38:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| aef80609-270f-30f8-b200-55b9338e7bd0 | -15.37449 | -47.31275 | 2025-10-07 04:38:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7eb70280-cdd1-358b-b81a-d875a1616c09 | -13.51511 | -48.62036 | 2025-10-07 04:38:00 | NPP-375D | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5ad6d8ca-9547-3acc-9700-c28b8dad86ea | -10.41872 | -50.31021 | 2025-10-07 04:38:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| abd5f048-aa67-3f3d-9104-151f70dc2791 | -10.91863 | -47.06514 | 2025-10-07 04:38:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| bb6f6199-891a-3c87-b04d-05daf05646c6 | -11.12932 | -47.21625 | 2025-10-07 04:38:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e2bd8696-d072-3acd-b3ef-53fde4e484be | -10.50161 | -51.49574 | 2025-10-07 04:38:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6328638b-f3c8-3568-bcf9-dadda872a5e6 | -11.7916 | -45.12861 | 2025-10-07 04:38:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fcec240c-1625-3e81-8488-39959981447d | -12.95528 | -46.82135 | 2025-10-07 04:38:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 01d960eb-0e43-3556-97db-f177a0bb831d | -13.6007 | -43.66715 | 2025-10-07 04:38:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3c9321d8-240d-3012-bebb-d7532f757952 | -14.75956 | -46.04449 | 2025-10-07 04:38:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 7.3 |
| e920831b-171a-3bc7-8e19-70623749e714 | -16.05169 | -50.98979 | 2025-10-07 04:38:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 33f76ed7-8d7c-3d13-ad45-6302b922e9c3 | -10.72386 | -46.6315 | 2025-10-07 04:38:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d2e8b02d-fb3a-3d78-88e4-aad9779f61de | -13.38055 | -44.30758 | 2025-10-07 04:38:00 | NPP-375D | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 438a23c5-1d8a-3c5c-88d6-933fb35adcfd | -10.23284 | -52.69818 | 2025-10-07 04:38:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0aed3cec-c24e-3a3d-aedf-ae20e1b790a0 | -13.22937 | -51.68246 | 2025-10-07 04:38:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ffda8b5e-96ce-37bc-91cc-c986ed11370b | -13.27166 | -47.79331 | 2025-10-07 04:38:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d2b7ff6c-3076-351f-81e8-07137f178531 | -13.07037 | -47.9498 | 2025-10-07 04:38:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6e670dae-0fcd-3dae-a540-5af51887883c | -10.81558 | -48.82924 | 2025-10-07 04:38:00 | NPP-375D | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4367fffd-4c2c-313d-8617-9bdaf5ff47f3 | -12.54498 | -48.14498 | 2025-10-07 04:38:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 40eeb356-831d-3956-b225-9b6b1b722f9e | -11.64774 | -46.87803 | 2025-10-07 04:38:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 1a032202-61cb-3d05-a58d-4348ba4c045c | -12.34762 | -47.05832 | 2025-10-07 04:38:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 188a6a89-84f2-3ef0-b68b-540662a01181 | -10.45816 | -50.41116 | 2025-10-07 04:38:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b9446742-9930-3828-8ee5-641c1ce365d2 | -14.77695 | -46.05644 | 2025-10-07 04:38:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 61.9 |
| 4720b83d-803d-3a84-8259-712647e83339 | -14.70059 | -48.34582 | 2025-10-07 04:38:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 385a92b2-cd5e-3401-a48f-1889b700a465 | -10.61929 | -48.70081 | 2025-10-07 04:38:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| af378db4-61f1-3b72-bad5-a306121f30e1 | -9.61782 | -57.20021 | 2025-10-07 04:38:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6581c974-bd51-3a91-9b27-92d1b374d1c9 | -11.94894 | -46.43155 | 2025-10-07 04:38:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7e5cccee-83dc-32c0-b9dd-4a205ee7cfb5 | -11.40429 | -55.08929 | 2025-10-07 04:38:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 73adeae7-3b31-36ca-8e53-a5fe465122e7 | -10.11112 | -58.53151 | 2025-10-07 04:38:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2521916b-1693-3161-959b-9308376e0fe7 | -13.00555 | -51.02835 | 2025-10-07 04:38:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f3146e56-d3e8-3425-9732-4e206a4c28d6 | -13.71806 | -48.06722 | 2025-10-07 04:38:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4f2548a5-ced1-3941-8e9d-a6e034519913 | -14.91166 | -46.85316 | 2025-10-07 04:38:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 72445cf8-978f-3fc1-9490-bb33be88e89b | -9.16985 | -59.56103 | 2025-10-07 04:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 38fa212e-e634-3d96-9d4a-8c242cfc6d4f | -16.02151 | -51.04839 | 2025-10-07 04:38:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8e78027f-740b-37ce-b583-5bd5e7b5cb21 | -13.27762 | -48.46811 | 2025-10-07 04:38:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a3e41304-ec4a-387f-8ad2-b5c9dadbce93 | -12.40039 | -51.1402 | 2025-10-07 04:38:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dfa85d92-aeb3-3983-a81e-ae58d2fe3c7b | -10.74579 | -50.48838 | 2025-10-07 04:38:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 5d2c15a7-bc6d-3f11-8438-4e5d770ca7e0 | -17.71329 | -40.24507 | 2025-10-07 04:38:00 | NPP-375D | LAJEDÃO | BAHIA | Brasil | 2918902 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 400c3b7d-18ed-335c-86a9-177f9230100b | -12.34385 | -50.26803 | 2025-10-07 04:38:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ba956f0b-5c01-3f1f-9f0f-3b738576213c | -15.57701 | -52.56522 | 2025-10-07 04:38:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| cb4de1ee-71c0-3da9-8b30-4a1c0097d28d | -12.91387 | -54.73154 | 2025-10-07 04:38:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6722694c-dda0-3cea-a44e-3815ddf9a3e6 | -13.68728 | -47.94808 | 2025-10-07 04:38:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ffa49aa4-61cc-30b2-b6bf-ad4ec4fea6fa | -14.91127 | -46.82415 | 2025-10-07 04:38:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| db68a422-fcb7-389c-8fa1-ff487308dfc1 | -8.22596 | -61.17276 | 2025-10-07 04:38:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6aa79aa8-6aed-364e-b0dd-23363ddc9992 | -12.14237 | -50.87725 | 2025-10-07 04:38:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 37658d7f-eab4-3a2c-a7e7-58978e96c443 | -18.01343 | -44.96825 | 2025-10-07 04:38:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cb6875fd-4d91-35bc-ba07-103911314e97 | -15.59244 | -52.55951 | 2025-10-07 04:38:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7f599754-dad6-3db4-9437-1f08dc682c2e | -15.18831 | -56.82391 | 2025-10-07 04:38:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 31d6c413-32cc-3a4c-b7ac-76b5f9f36b47 | -18.67305 | -44.04239 | 2025-10-07 04:38:00 | NPP-375D | PRESIDENTE JUSCELINO | MINAS GERAIS | Brasil | 3153202 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 21ece488-4f63-3579-9dd0-51746c8340e6 | -14.7732 | -46.05592 | 2025-10-07 04:38:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 61.9 |
| e8166370-c864-3bf8-bfbd-598c49b3523b | -10.80513 | -56.23697 | 2025-10-07 04:38:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 23ff3a0c-5de3-3d37-9f0e-39b3e4b5eb50 | -9.61493 | -57.20075 | 2025-10-07 04:38:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2fc6b781-a3b0-37a6-b7f9-951b936c2f48 | -10.74395 | -47.86048 | 2025-10-07 04:38:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 76f425be-4928-3a29-8bc1-f6e9463c9bdf | -15.38397 | -47.99769 | 2025-10-07 04:38:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 32076f34-0f28-3c09-b4e0-8fae941c7a6c | -13.34774 | -48.02976 | 2025-10-07 04:38:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 57907d09-cca1-37fa-b52b-cd0f556c5df3 | -14.65251 | -48.3643 | 2025-10-07 04:38:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 771c377f-35ba-3bac-9852-789babb8c874 | -13.01198 | -46.65165 | 2025-10-07 04:38:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4d901ad5-e339-3ac4-8d04-00e7f05774a4 | -10.7348 | -49.29593 | 2025-10-07 04:38:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 600b44e2-a736-3765-a786-f4bb5e307f0c | -13.24708 | -47.79775 | 2025-10-07 04:38:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4a3a735c-b00f-361a-bb6b-424a1d40caf9 | -23.37826 | -47.19404 | 2025-10-07 04:40:00 | NPP-375D | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 2362c29d-e07e-355e-8504-015aa02ab024 | -19.28459 | -44.35183 | 2025-10-07 04:40:00 | NPP-375D | PARAOPEBA | MINAS GERAIS | Brasil | 3147402 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ab19c701-2d9e-3e74-9899-9ee518c5c852 | -20.98304 | -45.58135 | 2025-10-07 04:40:00 | NPP-375D | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 271fc723-1847-3991-a7fc-d142c70f2b99 | -22.36713 | -47.7084 | 2025-10-07 04:40:00 | NPP-375D | IPEÚNA | SÃO PAULO | Brasil | 3521101 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 77f5cf78-e4dc-31d3-9b26-18ffa7e4b17b | -18.10476 | -53.36507 | 2025-10-07 04:40:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 590f5333-e904-365c-8908-95170c6bb823 | -22.54743 | -44.98956 | 2025-10-07 04:40:00 | NPP-375D | CRUZEIRO | SÃO PAULO | Brasil | 3513405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| d1330b2a-f6a0-39ca-8b1b-a00a9c1e3fb6 | -18.16367 | -53.37901 | 2025-10-07 04:40:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7fda06d7-6124-3173-9358-5ff02f117705 | -23.20033 | -46.77797 | 2025-10-07 04:40:00 | NPP-375D | CAMPO LIMPO PAULISTA | SÃO PAULO | Brasil | 3509601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |


[Clique aqui para ver as próximas entradas](README78.md)
