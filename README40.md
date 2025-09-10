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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d0051037-96dc-3725-84be-6ee62a24efbf | -13.56191 | -43.60657 | 2025-09-10 04:17:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c4e25073-7a7f-3fb0-a9fa-565457edfb25 | -11.95698 | -46.65047 | 2025-09-10 04:17:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a81abd28-f87d-31c5-9b27-6c21844b806a | -13.97772 | -48.22294 | 2025-09-10 04:17:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 26cf21ff-de65-31c4-a2dc-40c5eac5b5ac | -21.31227 | -43.88466 | 2025-09-10 04:17:00 | NOAA-21 | BARBACENA | MINAS GERAIS | Brasil | 3105608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.4 |
| fc2a52cf-c0eb-3f0a-938f-2dd83d449fba | -22.57217 | -48.55963 | 2025-09-10 04:17:00 | NOAA-21 | IGARAÇU DO TIETÊ | SÃO PAULO | Brasil | 3520004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 31c35b74-3377-3f70-8d34-5b59f2809d09 | -10.01791 | -51.68304 | 2025-09-10 04:17:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f426e1c0-ba0d-30f6-abce-31d9e2781d26 | -15.84572 | -52.27244 | 2025-09-10 04:17:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f2acc9fe-3c66-386a-bf02-c86cfc11030d | -11.45719 | -43.66037 | 2025-09-10 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 855efa47-ad7a-3e34-ae59-60f32337840e | -10.27503 | -48.82247 | 2025-09-10 04:17:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0c7751fd-0e0a-32cb-92d4-0cafb6632850 | -10.72207 | -48.28753 | 2025-09-10 04:17:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| af3d77b0-c798-3283-8715-825f18f962cb | -10.3863 | -50.5427 | 2025-09-10 04:17:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b4c1e113-4ad4-3e46-b1a8-a02ee1f3c56d | -13.94425 | -48.25803 | 2025-09-10 04:17:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b4750502-b223-3220-90ca-d97b17e93f24 | -14.3748 | -47.31768 | 2025-09-10 04:17:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f52c53fa-71e7-3a71-b599-f6d6c47520e6 | -16.45662 | -51.97391 | 2025-09-10 04:17:00 | NOAA-21 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 23ab3031-464b-3a30-92b5-ba3717601ad0 | -23.18536 | -46.11848 | 2025-09-10 04:17:00 | NOAA-21 | IGARATÁ | SÃO PAULO | Brasil | 3520202 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 7d8e6e27-6cc4-364e-9207-d74d9674754a | -11.11931 | -48.44493 | 2025-09-10 04:17:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b1b5b560-248a-3fbb-9ca2-0ba6a809f16b | -15.80655 | -52.25981 | 2025-09-10 04:17:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| d2e1c409-214a-361f-be28-7ec81c9fc27b | -20.56798 | -47.67556 | 2025-09-10 04:17:00 | NOAA-21 | SÃO JOSÉ DA BELA VISTA | SÃO PAULO | Brasil | 3549508 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 67cb39ea-9594-35a7-b30b-c1dfc8375e40 | -16.45802 | -50.66655 | 2025-09-10 04:17:00 | NOAA-21 | MOIPORÁ | GOIÁS | Brasil | 5213400 | 52 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 0bd8160e-b377-3726-a437-62aed317e565 | -11.68149 | -46.89951 | 2025-09-10 04:17:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 76f512d3-8577-32cb-b1c3-7ab25493629f | -12.02238 | -51.027 | 2025-09-10 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b3914fde-900d-307c-acd2-1d63479c1be0 | -20.08537 | -47.813 | 2025-09-10 04:17:00 | NOAA-21 | ARAMINA | SÃO PAULO | Brasil | 3503000 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0b8695df-4b68-35ec-a0a0-1dabac6a8134 | -23.45948 | -46.97553 | 2025-09-10 04:17:00 | NOAA-21 | SANTANA DE PARNAÍBA | SÃO PAULO | Brasil | 3547304 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 3f7f2df0-0f50-3e9f-9e30-e5c7c4ef6d9c | -9.95846 | -51.17786 | 2025-09-10 04:17:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 61b2dcbe-bca5-3ccd-88b9-d7387ba82447 | -17.31092 | -46.73901 | 2025-09-10 04:17:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c72469f1-f3f8-374f-ab05-8a09d5e79653 | -14.32783 | -47.30653 | 2025-09-10 04:17:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e4de9ece-c58f-3f09-8a95-b956f62d0688 | -13.81027 | -46.30008 | 2025-09-10 04:17:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 41aa108c-9790-3944-a9d6-c2f3048e97eb | -15.10882 | -50.07695 | 2025-09-10 04:17:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 5e83cfd4-c57c-3c63-b15e-ac93cfe378d5 | -15.13993 | -52.40125 | 2025-09-10 04:17:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 37.0 |
| 9b651020-4a78-3f14-a963-3cf1df847e9d | -10.27195 | -48.81679 | 2025-09-10 04:17:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 9be95c76-9c5f-3251-b000-c6fdb89dbf23 | -11.38152 | -43.53261 | 2025-09-10 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2cada6ab-edc2-30bc-9cf8-815e4de7e159 | -14.36099 | -47.31544 | 2025-09-10 04:17:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a2de71e4-ba86-3809-b845-5b256a2fa4d2 | -10.26845 | -48.81353 | 2025-09-10 04:17:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bf777960-5f86-35d1-8d2b-5feef303d5b7 | -11.44255 | -43.60038 | 2025-09-10 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 20db3f9c-7106-3846-9fb9-73ec1e4f0946 | -11.81693 | -46.75801 | 2025-09-10 04:17:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 125a3976-6ba8-3526-ab09-b8f436414a47 | -12.44472 | -44.74538 | 2025-09-10 04:17:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4c484eae-aa0a-39a9-9485-15f082ae0736 | -12.41502 | -44.71897 | 2025-09-10 04:17:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 704380d1-528a-3bb1-89e6-8d40827cbf6f | -13.75863 | -47.1745 | 2025-09-10 04:17:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d371d9a2-5b5a-3f6a-8ff8-9a932b8c08fc | -17.30641 | -46.74576 | 2025-09-10 04:17:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 2c5e109f-9ac5-34f9-bcde-ab72251edbc0 | -15.1315 | -52.39593 | 2025-09-10 04:17:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 1928e8b4-7a44-3f41-84d9-08b2f9aed5f5 | -11.045 | -46.05624 | 2025-09-10 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| de53e114-0a3d-353b-93be-ea28bf235b81 | -15.01423 | -48.03144 | 2025-09-10 04:17:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5c72143d-eecc-3f3f-a14e-66052f1e0618 | -20.54071 | -47.6743 | 2025-09-10 04:17:00 | NOAA-21 | SÃO JOSÉ DA BELA VISTA | SÃO PAULO | Brasil | 3549508 | 35 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0e161ad4-304d-3847-8889-2a4a902224d8 | -12.85577 | -52.94653 | 2025-09-10 04:17:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 81c689e8-e3fb-370d-8e15-6f3eb884fbcb | -16.14613 | -47.89397 | 2025-09-10 04:17:00 | NOAA-21 | CIDADE OCIDENTAL | GOIÁS | Brasil | 5205497 | 52 | 33 | nan | nan | nan | Cerrado | 8.8 |
| fdd13c86-b6b6-35e8-94d5-3757de5d1ae9 | -19.93412 | -49.24838 | 2025-09-10 04:17:00 | NOAA-21 | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6a5e77af-0f42-3266-92c8-89124791bb42 | -12.93931 | -54.79693 | 2025-09-10 04:17:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| bb97ad83-5164-375d-b0a2-d0dc855da313 | -13.93271 | -48.2604 | 2025-09-10 04:17:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 1629ba5f-010a-3420-895e-f7d7cd4bf365 | -9.97611 | -50.29871 | 2025-09-10 04:17:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7edd741f-bb13-300a-9c8f-d6ebd01fa0cb | -17.24921 | -46.08124 | 2025-09-10 04:17:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 746b236b-48a3-3987-8b2a-feda05f1a191 | -14.78421 | -48.23016 | 2025-09-10 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d95856ab-124f-369b-8a11-cb70cdd47879 | -21.40226 | -44.27266 | 2025-09-10 04:17:00 | NOAA-21 | MADRE DE DEUS DE MINAS | MINAS GERAIS | Brasil | 3139102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| e7ea8ea3-b52d-31f0-bc1d-52ab388df964 | -15.9513 | -50.22386 | 2025-09-10 04:17:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| eba4908e-3375-33f0-aca9-8bd9483737e9 | -11.6752 | -46.8943 | 2025-09-10 04:17:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b7822ac6-2819-33aa-aa1f-63dbe4f93b92 | -11.57028 | -44.66013 | 2025-09-10 04:17:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 017f01d1-5427-34a0-bf1e-b86a24be7c10 | -16.67219 | -48.52245 | 2025-09-10 04:17:00 | NOAA-21 | SILVÂNIA | GOIÁS | Brasil | 5220603 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 1b9072dc-ead8-34d7-bd4a-9beb0ed3841f | -21.026 | -48.41729 | 2025-09-10 04:17:00 | NOAA-21 | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d19d6c9e-232f-3942-8384-6bf6bc637000 | -17.5706 | -44.54716 | 2025-09-10 04:17:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f9967aa7-d8bb-3637-a765-aa8137cd1cce | -15.28407 | -53.78647 | 2025-09-10 04:17:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b305b8c2-f41f-38e5-b3fe-a1c55fb7ff13 | -13.97233 | -48.22324 | 2025-09-10 04:17:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 929f928d-febf-36cc-ace5-065348b250bb | -17.74133 | -44.49055 | 2025-09-10 04:17:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c9da1f61-2e6b-3d09-9b70-4fe6c6d9bde4 | -12.18451 | -53.87542 | 2025-09-10 04:17:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 45918365-6c34-3dce-bef9-b1f4101d7ce1 | -13.15284 | -45.28402 | 2025-09-10 04:17:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 5daf3244-83d9-3781-8a76-bdb0526c7b19 | -15.48152 | -49.37971 | 2025-09-10 04:17:00 | NOAA-21 | RIANÁPOLIS | GOIÁS | Brasil | 5218706 | 52 | 33 | nan | nan | nan | Cerrado | 8.4 |
| a0821f43-f830-3659-b610-090d2a1aea98 | -13.98378 | -46.65917 | 2025-09-10 04:17:00 | NOAA-21 | IACIARA | GOIÁS | Brasil | 5209903 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1e4ea34b-84c6-317f-9006-f20ca0cc07e2 | -13.17938 | -47.25085 | 2025-09-10 04:17:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 23e9112e-0cd0-353e-a4e6-b0b6985cda88 | -11.44181 | -43.69412 | 2025-09-10 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ab767e23-1c01-3b24-a3fc-b3aaf233fdc5 | -15.86022 | -51.83157 | 2025-09-10 04:17:00 | NOAA-21 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| a8f77025-0d32-3c68-9626-ab719f0bcb5e | -12.878 | -47.96367 | 2025-09-10 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b8d695ec-e1cd-3e24-98e3-495ad060cdbd | -12.18841 | -53.86164 | 2025-09-10 04:17:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| b3e59189-5dc0-3e61-8f5f-07f51916ced3 | -12.68865 | -44.96919 | 2025-09-10 04:17:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c0808516-9c78-3aed-9ad7-8f4cafd0f6d0 | -10.59807 | -43.30048 | 2025-09-10 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| fd95f8a9-ffac-38d0-95c6-f824b823eea3 | -21.50624 | -44.79346 | 2025-09-10 04:17:00 | NOAA-21 | LUMINÁRIAS | MINAS GERAIS | Brasil | 3138708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| 71307f9d-d5ea-307b-93b2-336b930a5a1b | -13.64428 | -46.99345 | 2025-09-10 04:17:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c85ac919-f3fc-32e0-872c-7bec937813c4 | -15.01281 | -48.01847 | 2025-09-10 04:17:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6eefc084-4ccd-38c6-8d49-2e83d29570c1 | -10.69422 | -50.46767 | 2025-09-10 04:17:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c5a5260a-4cb7-3618-9e59-f01dddd7677a | -20.98429 | -48.00739 | 2025-09-10 04:17:00 | NOAA-21 | PONTAL | SÃO PAULO | Brasil | 3540200 | 35 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 20e4c75f-2567-3aef-899e-ada2e4c4d7bb | -17.72259 | -44.44208 | 2025-09-10 04:17:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0ffdf127-beaf-3357-9798-320626999bc9 | -20.75415 | -45.34445 | 2025-09-10 04:17:00 | NOAA-21 | CANDEIAS | MINAS GERAIS | Brasil | 3112000 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c46e4908-1025-3daa-9bc1-162ba37c21c0 | -20.52166 | -47.6438 | 2025-09-10 04:17:00 | NOAA-21 | SÃO JOSÉ DA BELA VISTA | SÃO PAULO | Brasil | 3549508 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 358e72dc-92e7-3cf4-bfc0-966e11a6683b | -14.89416 | -55.8641 | 2025-09-10 04:17:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0ee76f40-5fd1-3699-99b1-5be4ebc0263c | -17.71586 | -44.44102 | 2025-09-10 04:17:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 54aa7f00-37f6-3d68-b5a4-924cfab7d059 | -10.19377 | -46.80877 | 2025-09-10 04:17:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8d9cca11-6f58-3550-a143-bb3683063257 | -10.56401 | -49.44262 | 2025-09-10 04:17:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e384181d-2589-35e2-826b-edcc63fc0506 | -12.88159 | -47.96436 | 2025-09-10 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 49941a99-b851-33d6-ab65-e62a2c78a451 | -15.3339 | -52.89713 | 2025-09-10 04:17:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c4060793-014f-3654-af54-d465b06da00f | -16.8853 | -45.75786 | 2025-09-10 04:17:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cc5de746-2d7c-3f1f-80d8-40d9ee81fb41 | -11.39427 | -43.53826 | 2025-09-10 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 0ad932f6-fc21-33ba-afe5-854fe03127d7 | -12.83612 | -52.94274 | 2025-09-10 04:17:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0370f3de-1be3-35ca-974f-79d82081b6fd | -20.57132 | -47.67616 | 2025-09-10 04:17:00 | NOAA-21 | SÃO JOSÉ DA BELA VISTA | SÃO PAULO | Brasil | 3549508 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bbd76fb4-a786-380c-b26b-517c67ad5990 | -12.93016 | -54.75595 | 2025-09-10 04:17:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 10.9 |
| cab10d4e-01e1-3408-b168-72c43e1bb449 | -13.64754 | -46.97395 | 2025-09-10 04:17:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bfbca104-85dd-3220-b547-ca24b30ce6af | -11.67392 | -46.90211 | 2025-09-10 04:17:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f310d680-e1f8-30a9-99b6-9d975b99a74b | -16.44916 | -51.98167 | 2025-09-10 04:17:00 | NOAA-21 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 23eb9cfa-2a3c-360b-b445-cb60df4b5a92 | -11.43478 | -43.58464 | 2025-09-10 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| fe3a79e4-080a-34a9-a4f3-7eda8fbf0271 | -11.45265 | -43.62346 | 2025-09-10 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| b0aac704-c17f-3cbe-931e-754bf93cd5bd | -15.56369 | -42.72004 | 2025-09-10 04:17:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 97b9332a-f4f0-32b9-890e-54af1ddc0cd3 | -10.00816 | -48.09226 | 2025-09-10 04:17:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 20.4 |
| ee830de2-26fb-3488-a7ed-f669b19fca36 | -15.94968 | -48.10752 | 2025-09-10 04:17:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e261abc2-a6f4-3809-8148-712db1c36711 | -12.99549 | -48.02345 | 2025-09-10 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README41.md)
