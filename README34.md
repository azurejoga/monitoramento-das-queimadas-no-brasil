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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 515827f4-5bc9-39cc-8edb-b155565f7eac | -11.63386 | -47.76874 | 2026-09-20 04:19:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| cc6a1d5d-c1c5-39dd-a073-97ebb8e5923a | -8.38407 | -45.63474 | 2026-09-20 04:19:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 4bea82e1-135c-354b-8ec2-78ab03f4743e | -7.51857 | -47.33469 | 2026-09-20 04:19:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f845dc0b-9c7e-3361-8b77-d247022744dd | -11.09261 | -48.29706 | 2026-09-20 04:19:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b64bb1d9-3bfa-3bf0-9cc6-290a5632c3aa | -10.18917 | -44.13931 | 2026-09-20 04:19:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 91f0a709-2c84-30a4-b250-563c305bb737 | -5.40102 | -42.94934 | 2026-09-20 04:19:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 6630fa52-f19e-3f82-8764-75e5e2090285 | -7.16607 | -47.44596 | 2026-09-20 04:19:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 78340648-998c-3999-b2ea-b515a9fc5e03 | -9.59275 | -45.3741 | 2026-09-20 04:19:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e6d3b549-b750-3bb0-a6d9-cf80ccb683bd | -11.41382 | -44.21499 | 2026-09-20 04:19:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 08bab5fe-c0a0-3246-a15d-e7765a7bb16c | -8.65595 | -45.43828 | 2026-09-20 04:19:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8d6272ef-f4c3-32fb-b2ce-51526334a12a | -11.45525 | -45.40154 | 2026-09-20 04:19:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c1f1a9fc-7404-3a86-93a5-a158c31ca970 | -8.6323 | -47.62003 | 2026-09-20 04:19:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 35bf8baf-185f-3261-9384-0b967a3fbc5e | -5.22542 | -47.58335 | 2026-09-20 04:19:00 | NPP-375D | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Amazônia | 8.8 |
| bff3a3d5-76b2-34f1-a347-6e234fdad5ca | -11.44697 | -45.34232 | 2026-09-20 04:19:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c5aa1197-d3b2-32de-824a-ba3791dd37e2 | -8.17655 | -54.7552 | 2026-09-20 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b7b9e6c7-3880-3a6c-87fe-5513706104eb | -8.41766 | -45.87403 | 2026-09-20 04:19:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 853ec0b0-a49f-3648-92fc-fe01fdfd44e8 | -6.26059 | -42.72895 | 2026-09-20 04:19:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| f52081f4-5261-3096-908b-625b1a877168 | -7.9604 | -44.02817 | 2026-09-20 04:19:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 67d5bc0e-3c5c-3ce5-863e-88e21887159e | -7.59756 | -46.73094 | 2026-09-20 04:19:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 23978f2a-d373-3852-b083-2b6692e50915 | -11.48105 | -47.78436 | 2026-09-20 04:19:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| ae428b9b-3736-38ae-9632-c21625d1e981 | -5.83356 | -53.52601 | 2026-09-20 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1c9375a7-1e5f-3f29-b050-0308b8db65ef | -10.30762 | -50.27491 | 2026-09-20 04:19:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 102998d4-fc62-30cc-bd1e-dac6ce8df0fe | -8.47647 | -44.51117 | 2026-09-20 04:19:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6c1effdf-8fe4-397a-87e8-f1f075df51b0 | -10.41674 | -48.3278 | 2026-09-20 04:19:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d5018ee6-7938-327f-bbf2-5f5b8e8b4143 | -5.84818 | -53.55609 | 2026-09-20 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| dfc4c52c-24b6-3741-939a-6412cde0f672 | -8.13773 | -46.80618 | 2026-09-20 04:19:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 42138776-94ef-385b-b4a5-7cab6c96b986 | -7.01511 | -45.24646 | 2026-09-20 04:19:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 27.0 |
| c8328630-d2a0-3f1d-ab30-f13b0a6dafa1 | -5.45206 | -44.31424 | 2026-09-20 04:19:00 | NPP-375D | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 86d20865-07e7-3180-b985-b3a13e02209c | -9.11942 | -45.72356 | 2026-09-20 04:19:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| dde420fd-4db8-3843-ad8c-662eba4e6955 | -8.76601 | -48.66649 | 2026-09-20 04:19:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 7.2 |
| bce5ddf0-d953-34cf-a2fb-5912a22c4e29 | -7.53722 | -44.93524 | 2026-09-20 04:19:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8fa08609-1f65-3e03-93a2-4b5dbd31b75c | -4.89197 | -45.62785 | 2026-09-20 04:19:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 99c65315-cbe2-386d-b493-3a8b52844c3c | -5.83529 | -53.55353 | 2026-09-20 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3d62490e-956f-3bd8-bb72-d4ea68e8f315 | -2.63909 | -54.69238 | 2026-09-20 04:19:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 75218877-bfa9-3297-90f8-103377b9416f | -5.40042 | -42.953 | 2026-09-20 04:19:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 2.0 |
| c2bf3a0b-0bd8-3989-bde5-216540c51ed1 | -10.32569 | -48.00709 | 2026-09-20 04:19:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 827791a5-3ccf-3c07-8469-f1f99f816b01 | -7.43508 | -44.76154 | 2026-09-20 04:19:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 03bba083-d0fe-39e8-a958-89101ba6d09f | -10.30075 | -45.42929 | 2026-09-20 04:19:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| edcfacc0-642c-3495-88df-0102c2aa9e2e | -7.29556 | -46.74263 | 2026-09-20 04:19:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 10ae472e-4987-3c17-bd08-440ecaa1451c | -6.30199 | -47.62564 | 2026-09-20 04:19:00 | NPP-375D | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 03626346-d1ea-3d9a-b5ad-e1d78a96ae3c | -7.58806 | -46.73308 | 2026-09-20 04:19:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b6dd6256-5f8b-3db8-8e8d-1eb8ff60d74f | -9.88876 | -46.53883 | 2026-09-20 04:19:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| fced7c7f-df7c-3fe2-bbdd-b78f40c800e9 | -2.98017 | -54.76921 | 2026-09-20 04:19:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 047e4814-3755-3e0b-9266-d663834b6c13 | -7.30738 | -48.71049 | 2026-09-20 04:19:00 | NPP-375D | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fc947e3a-60f6-34a2-aac1-4b072d4df075 | -7.01584 | -45.24207 | 2026-09-20 04:19:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 15ba1ecc-4f28-3c5b-8a62-ca2637f895b9 | -10.78759 | -50.86832 | 2026-09-20 04:19:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| d04a7546-edd5-3c0f-9440-1e3aa5f65adc | -11.44411 | -45.33768 | 2026-09-20 04:19:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9ce37ee7-6d5a-3a0b-a638-8c93c506bfdb | -7.52755 | -45.44093 | 2026-09-20 04:19:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 9106e995-7fea-3af5-81c1-8fb9b37f1a2b | -5.6614 | -42.6302 | 2026-09-20 04:19:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 9b2d0934-19e9-3925-a919-7a633fe1cf2a | -7.10734 | -42.09069 | 2026-09-20 04:19:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.2 |
| 4e409c80-3ac9-3b67-86ac-678454e82d86 | -3.00948 | -54.16696 | 2026-09-20 04:19:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 126a897f-ef8b-353b-8dca-0a8a4240e72e | -10.41133 | -48.94407 | 2026-09-20 04:19:00 | NPP-375D | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| bcc6ff21-696a-337f-a7fd-6314d2edc2db | -8.48095 | -46.86686 | 2026-09-20 04:19:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d8d1f016-9189-38fc-9323-50ac0cde0ee3 | -7.54168 | -45.42502 | 2026-09-20 04:19:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 29.2 |
| 659862b4-398c-3f52-bfac-fa2835714a86 | -10.49153 | -48.09791 | 2026-09-20 04:19:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| af8d4d44-d34d-39c9-93b5-f1667598e026 | -7.55941 | -45.69016 | 2026-09-20 04:19:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c0db1f64-2294-374d-843e-a0ce34f23d08 | -10.23454 | -45.35643 | 2026-09-20 04:19:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5f6e346a-3d9d-320d-bc3f-74fef7ccc342 | -10.83331 | -50.93023 | 2026-09-20 04:19:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| badcd3ce-366f-3079-9b24-73f5bc913f7f | -11.65669 | -43.43102 | 2026-09-20 04:19:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 94cd3f5f-66e9-331c-a508-0ce07f5a2793 | -7.97085 | -44.07298 | 2026-09-20 04:19:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f95ea358-152b-3845-9de5-b86b072dfcc6 | -8.05387 | -46.29025 | 2026-09-20 04:19:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| b8146e58-59d9-3e89-a8d8-ca146d097de2 | -6.29694 | -47.62906 | 2026-09-20 04:19:00 | NPP-375D | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d9207c0d-36a3-37f7-9a97-771c8e1ee904 | -8.38352 | -47.18956 | 2026-09-20 04:19:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0ed6926c-69f7-388d-8b0d-39928b2bebb3 | -11.44816 | -45.40035 | 2026-09-20 04:19:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1a5daeeb-8aa8-3092-a179-cc9e8e3a96c4 | -9.94803 | -45.54793 | 2026-09-20 04:19:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 859ec6d0-063a-3106-85e1-e758de30fc41 | -8.18431 | -54.75084 | 2026-09-20 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f34eed29-1dc3-3158-bd2a-113e592cc500 | -10.49032 | -46.26448 | 2026-09-20 04:19:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 84f12c4b-bc20-311b-bfd1-1702be154e00 | -5.83623 | -53.5483 | 2026-09-20 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e4d3c204-82e4-3050-bc96-2121a9406671 | -11.66509 | -43.42146 | 2026-09-20 04:19:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5572d810-f935-3db8-8681-40f6fc1ee16c | -11.4817 | -47.78066 | 2026-09-20 04:19:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8df2969b-af12-35a2-b0a2-13eb1cbf32e5 | -5.84249 | -53.54743 | 2026-09-20 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b6e13db9-60b8-3e47-8fd1-95647effaeeb | -11.24129 | -48.38531 | 2026-09-20 04:19:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 4adb4526-e722-31f9-ac02-540a4d1278d0 | -5.89156 | -53.64449 | 2026-09-20 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4c819f92-95f4-3798-b9b1-13def6f4383e | -6.28414 | -41.77726 | 2026-09-20 04:19:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d05e6a6e-79af-3908-a2ce-3d8be7f75e7b | -11.07769 | -49.50072 | 2026-09-20 04:19:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4e885a4a-65ca-3db2-81e2-76428c64e6a4 | -9.70314 | -45.8681 | 2026-09-20 04:19:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1ce2a7a8-1b34-3405-9ebd-9fe59805e459 | -6.31865 | -47.633 | 2026-09-20 04:19:00 | NPP-375D | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 536a9b4d-616e-3fa8-8c8d-172f76520372 | -10.27237 | -45.43922 | 2026-09-20 04:19:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b9a21789-790c-386a-b5b0-732bc781108c | -5.22101 | -47.58259 | 2026-09-20 04:19:00 | NPP-375D | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 7367dfc5-f934-3794-b0c6-b22955900688 | -6.32484 | -44.4305 | 2026-09-20 04:19:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 03d096c4-6f26-3213-8104-5b1e89548076 | -8.17318 | -54.77296 | 2026-09-20 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ffa159d3-f309-35ef-b97b-c526751225c4 | -9.03993 | -49.83774 | 2026-09-20 04:19:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c19adbc5-8cd8-3708-a226-08a09bb290e6 | 1.22559 | -50.98836 | 2026-09-20 04:19:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dff20c17-aa66-3123-a051-44641367808d | -9.79512 | -45.07369 | 2026-09-20 04:19:00 | NPP-375D | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d382d82f-17c6-3c26-82e1-887d7b64b083 | -10.48799 | -46.27792 | 2026-09-20 04:19:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| eb33d940-f732-3b07-a8c2-7d407bde53f2 | -7.01808 | -45.25151 | 2026-09-20 04:19:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 98ff36c0-f222-3304-91f6-86f10157cbde | -10.29995 | -50.26227 | 2026-09-20 04:19:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 60ca0a84-64be-3646-b9d4-b422f030268e | -9.23922 | -46.18229 | 2026-09-20 04:19:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 38bfeda1-d847-36fe-911f-e7ff4e4375c2 | -7.54904 | -45.3808 | 2026-09-20 04:19:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| bb6d936d-6e8e-3ebf-958b-d04523c99569 | -10.2967 | -45.42627 | 2026-09-20 04:19:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0ca62d19-ca6a-3c3e-a1ad-cf0c06a2b0f2 | -5.51098 | -45.66325 | 2026-09-20 04:19:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5f780060-0a4a-31d6-8174-14918ea216cd | -10.41287 | -48.93537 | 2026-09-20 04:19:00 | NPP-375D | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| acf8d3b9-1647-3b5f-9a80-4571d8ca8904 | -4.8959 | -45.62833 | 2026-09-20 04:19:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 0ee6d7a6-6df4-3109-89b3-0bb7a124cad1 | -8.7311 | -44.87077 | 2026-09-20 04:19:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f8ca5846-ad90-382e-875d-e64af8b1d7d8 | -10.30964 | -50.22403 | 2026-09-20 04:19:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| cd11eeb0-86af-3e24-abcd-1b5663775051 | -5.84743 | -53.52093 | 2026-09-20 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| fb348077-d97c-3c4a-abf4-d1ea7cef174f | -6.30044 | -47.60852 | 2026-09-20 04:19:00 | NPP-375D | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 632063fc-7f9f-30f3-a96a-7b7cf5330ea0 | -8.45459 | -48.45143 | 2026-09-20 04:19:00 | NPP-375D | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 66f71cff-f037-3909-b453-3baeda06c548 | -9.23808 | -46.23492 | 2026-09-20 04:19:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| f8a3476e-9814-3814-968c-51c7295f0163 | -8.42424 | -54.73251 | 2026-09-20 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README35.md)
