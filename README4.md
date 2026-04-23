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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e3da8424-ba06-31e3-ba46-aa181505ea54 | -12.09262 | -51.22774 | 2026-04-23 04:29:00 | NPP-375D | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| af707450-a3f7-3c39-bc93-0f674bc9b82c | -11.78198 | -43.6172 | 2026-04-23 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| eea69b20-4266-37a8-92a6-23105e5a6b2a | -16.58594 | -46.96817 | 2026-04-23 04:29:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1e0f125c-d47d-3bfd-b5c0-7b1b93d88de8 | -14.90437 | -45.17824 | 2026-04-23 04:29:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 84807dd0-d3c1-34ff-b006-adcfc17fbc82 | -13.37998 | -45.32113 | 2026-04-23 04:29:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f79e40b1-f692-380f-977c-b404286f29d5 | -11.76627 | -43.64819 | 2026-04-23 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b2699461-fbe6-3be5-a30b-d73d825131f7 | -11.97537 | -43.84165 | 2026-04-23 04:29:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8eb8fa32-ce33-3702-8710-898467bbea30 | -13.37662 | -45.32059 | 2026-04-23 04:29:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 345b7aab-f981-3a6e-98f9-6947fabcf3f0 | -12.28057 | -44.61833 | 2026-04-23 04:29:00 | NPP-375D | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fd733461-bdd2-3bc3-a782-d7e8f9a83780 | -11.77967 | -43.65717 | 2026-04-23 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0af85f45-8063-3e65-a43f-d7e73b8bd1cc | -12.01031 | -49.27819 | 2026-04-23 04:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3523accd-762f-3fd5-89dc-9301db4b9f9f | -11.05958 | -49.49994 | 2026-04-23 04:29:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 07d37e99-289b-3a12-9ee2-87feef85ec98 | -12.85197 | -43.77685 | 2026-04-23 04:29:00 | NPP-375D | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1885db7e-2ec3-3353-9af2-7ea001736282 | -11.79248 | -43.61884 | 2026-04-23 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b8eacc94-eeb4-3f6d-9be7-0b5b2a85d023 | -13.38614 | -45.32584 | 2026-04-23 04:29:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6d27e483-75a8-3ba5-8434-af551cd31d3b | -11.76746 | -43.64033 | 2026-04-23 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5235836b-e63b-3fe8-9072-bbf9fff2d9aa | -13.02751 | -43.58862 | 2026-04-23 04:29:00 | NPP-375D | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5f892ac1-c5d8-3baf-84c6-7f29042ded1e | -11.76686 | -43.64426 | 2026-04-23 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b24936ac-a3c5-3889-8615-0c81930ae9e7 | -12.27691 | -44.61839 | 2026-04-23 04:29:00 | NPP-375D | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5ebbf5bb-532f-3ee5-9ac0-0d70636e7df4 | -11.782 | -43.66561 | 2026-04-23 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 8ef5dc4a-9d64-36d8-ad59-eb485774a4aa | -12.2834 | -44.62255 | 2026-04-23 04:29:00 | NPP-375D | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| e84f3777-7bcc-3065-9e23-23f78013dfc0 | -12.28031 | -44.61892 | 2026-04-23 04:29:00 | NPP-375D | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 57b6aeb2-b08c-3ac3-94c4-b4b34c66c3ab | -15.15804 | -41.28968 | 2026-04-23 04:29:00 | NPP-375D | BELO CAMPO | BAHIA | Brasil | 2903508 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 33011fc2-0893-390f-a4a4-b9c9d7688b9e | -11.77385 | -43.64535 | 2026-04-23 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0f1e12d9-bd74-3604-85da-90df026b3545 | -11.7849 | -43.62169 | 2026-04-23 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7b2976a2-d641-3246-a89a-c34148fbef88 | -13.38669 | -45.32221 | 2026-04-23 04:29:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2baff22a-5adf-33c3-be4d-e5deac1eae6d | -12.57025 | -45.47271 | 2026-04-23 04:29:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e793ed2f-9dd8-39e7-b447-418ab9c2b126 | -11.76976 | -43.64874 | 2026-04-23 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3334d81a-ef8f-3d8b-8205-479f5160fcb0 | -16.71076 | -44.95376 | 2026-04-23 04:29:00 | NPP-375D | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 095c221e-47fc-3724-9334-01c07a0e00e2 | -12.24148 | -44.18402 | 2026-04-23 04:29:00 | NPP-375D | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| abb2c41e-9ef3-3f0d-a457-baa8c6c59c8e | -11.79132 | -43.62672 | 2026-04-23 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 828538fa-b665-3937-b527-fca522677073 | -11.78563 | -43.61494 | 2026-04-23 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| cc309e17-67bf-3abf-8181-53631ff0bd06 | -11.77036 | -43.64481 | 2026-04-23 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 540179ed-7f78-3f35-a856-6240fa3e10f6 | -12.3064 | -57.18106 | 2026-04-23 04:29:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0980e7ec-7551-3b69-b28e-9a5479590b2e | -12.58204 | -45.47479 | 2026-04-23 04:29:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ba5e3c67-b574-347a-88a4-40d6c0623714 | -13.38333 | -45.32167 | 2026-04-23 04:29:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ec8be6ba-b051-3493-b24a-f002c45e8985 | -11.78548 | -43.61775 | 2026-04-23 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 617763f5-24c8-3180-83c4-61e2367f3d6b | -11.77904 | -43.65824 | 2026-04-23 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| c443b39e-c2fa-3e70-bd52-69cb7a35b837 | -13.00454 | -55.977 | 2026-04-23 04:29:00 | NPP-375D | LUCAS DO RIO VERDE | MATO GROSSO | Brasil | 5105259 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d06517ea-1146-3e2a-b72e-44d08ba87513 | -12.58538 | -45.47532 | 2026-04-23 04:29:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5ad29ee6-f19b-338d-ba1a-f98776fbcff1 | -11.77445 | -43.64142 | 2026-04-23 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0d754c04-7b3e-36bc-b70b-76607ac8be65 | -13.37887 | -45.32839 | 2026-04-23 04:29:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3449221e-c87d-30ee-8b23-179c85de5474 | -12.58082 | -45.47075 | 2026-04-23 04:29:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f2bbb6c9-323d-37a2-9dd3-e3a3fcca8bb1 | -12.58648 | -45.46818 | 2026-04-23 04:29:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ffb87eb9-181b-3248-bf79-4f5f98bf1e8c | -11.77785 | -43.6661 | 2026-04-23 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2df69f48-93fb-3087-a2a6-3fc564b79d2d | -11.7919 | -43.62278 | 2026-04-23 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 3f7c24e5-bdd6-3d0d-906a-1a3d889e5fe8 | -13.38389 | -45.31805 | 2026-04-23 04:29:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6ee4459c-66ae-3c10-b7a6-974dbccda7b1 | -11.78898 | -43.61829 | 2026-04-23 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c60f5a54-df83-308e-b1d5-21ffe725ac11 | -11.77555 | -43.65769 | 2026-04-23 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 47077ef7-9651-3ba8-b559-36d1da997e63 | -12.05262 | -45.3427 | 2026-04-23 04:29:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3f8f23b3-e312-3794-984b-d9577c7fb325 | -11.78154 | -43.61834 | 2026-04-23 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d9e1202a-9ad5-32ed-929d-8135e6216324 | -11.77495 | -43.66162 | 2026-04-23 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8edcd678-b4d3-3b85-921c-a4531ab79b30 | -13.38558 | -45.32946 | 2026-04-23 04:29:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 19e58097-d3a7-334f-9ad1-57d415596453 | -13.38222 | -45.32892 | 2026-04-23 04:29:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dd32c6b7-2472-3c18-94c1-23fd39fbd428 | -13.37942 | -45.32476 | 2026-04-23 04:29:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cb46a01c-77e3-35e4-88f7-5daea5d5b488 | -11.7954 | -43.62333 | 2026-04-23 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dae698bb-04e6-3764-bdae-45eb0ec8d1fa | -12.56635 | -45.47574 | 2026-04-23 04:29:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1a4be07a-93ed-3725-a129-22f7a9a4fdd7 | -12.28001 | -44.62203 | 2026-04-23 04:29:00 | NPP-375D | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 0c0e78e7-df48-33a0-8288-1b51ebaab42d | -11.79598 | -43.61939 | 2026-04-23 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f72438a0-14f8-39d3-84fa-f2f39ea58316 | -15.15754 | -41.2935 | 2026-04-23 04:29:00 | NPP-375D | BELO CAMPO | BAHIA | Brasil | 2903508 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| ccfe3dae-be42-37a8-abf0-76268fa49700 | -11.78504 | -43.61888 | 2026-04-23 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5f824939-c6ed-33f8-b460-f03c1743d636 | -11.78782 | -43.62617 | 2026-04-23 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 9acfc3d9-25ea-38e7-b7a9-d4058b1f0cfe | -11.06328 | -49.50057 | 2026-04-23 04:29:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b6a7c11e-b257-3bbf-b494-4e65e1fbf979 | -11.06155 | -49.50237 | 2026-04-23 04:29:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 82ea0823-5c10-396e-af3f-432bfc9ef3c0 | -11.77618 | -43.65662 | 2026-04-23 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e91621d4-16c2-345e-8a86-321a68389b36 | -11.77851 | -43.66504 | 2026-04-23 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 039bd665-00dc-3c25-bec1-987a37a7fd71 | -11.77845 | -43.66216 | 2026-04-23 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c6bbcd28-5ccf-3900-b8f9-81e1fa2b0e73 | -12.58259 | -45.47121 | 2026-04-23 04:29:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bf9581d4-1210-36a4-a64c-3a030b98a97b | -12.30048 | -57.17988 | 2026-04-23 04:29:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2b89dc12-3821-3069-a0c5-079101cdae22 | -13.44085 | -44.0495 | 2026-04-23 04:29:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 226a3f59-959a-30fc-88fc-d83cc1292da7 | -11.77266 | -43.65321 | 2026-04-23 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d6f0932a-db80-31ae-8d2d-e6fa656923b3 | -12.58314 | -45.46764 | 2026-04-23 04:29:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b99f17d4-8332-3e48-b553-9db0921a7e37 | -11.77206 | -43.65714 | 2026-04-23 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1be94083-cc66-32e0-98cc-c449bb7e5f86 | -13.37606 | -45.32422 | 2026-04-23 04:29:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 01022cf9-9dd5-3a40-839e-300957b8c33d | -11.78258 | -43.66167 | 2026-04-23 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 9f8194c2-3018-317a-a441-9d50b3a47574 | -13.38278 | -45.3253 | 2026-04-23 04:29:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2cc1f8be-a4b9-3e1e-a71d-7981e28fcb0a | -20.20909 | -46.74347 | 2026-04-23 04:32:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| eebbef53-ad3c-3922-8858-0708a522af3a | -20.23654 | -46.76783 | 2026-04-23 04:32:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 672ee06d-a486-3721-9db2-fe31517ffaf8 | -20.19017 | -46.89169 | 2026-04-23 04:32:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7135303c-958b-3119-adf9-eed3b320d8d5 | -20.17884 | -46.94366 | 2026-04-23 04:32:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e26e267f-042f-3a67-bcc3-0a38be906af5 | -16.43143 | -54.91818 | 2026-04-23 04:32:00 | NPP-375D | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f7eaf91e-c746-35c1-9e01-3c4fb3a44c07 | -20.23252 | -46.79442 | 2026-04-23 04:32:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dc87d446-8ad6-34df-ac60-53cc3197e30d | -18.58517 | -55.93308 | 2026-04-23 04:32:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 767034bd-6e9f-3e12-b029-c7fba0755b10 | -19.97654 | -44.85823 | 2026-04-23 04:32:00 | NPP-375D | SÃO GONÇALO DO PARÁ | MINAS GERAIS | Brasil | 3161809 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 687ec973-f6d7-313b-b07b-728bc2dd0a1c | -22.1082 | -48.45274 | 2026-04-23 04:32:00 | NPP-375D | BOCAINA | SÃO PAULO | Brasil | 3506805 | 35 | 33 | nan | nan | nan | Cerrado | 35.4 |
| 89df88b5-3338-3d09-80c0-35ad152dbef4 | -22.11212 | -48.44962 | 2026-04-23 04:32:00 | NPP-375D | BOCAINA | SÃO PAULO | Brasil | 3506805 | 35 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 94073ade-38ca-3ee9-a1be-4aa4d6123fc9 | -18.50562 | -55.4988 | 2026-04-23 04:32:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 3d203cc8-34f2-3c92-b6cd-f4b6425d1caf | -20.71819 | -55.17377 | 2026-04-23 04:32:00 | NPP-375D | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4173bf7e-c2d4-3e27-9b67-3f369c416f0b | -20.23758 | -46.80666 | 2026-04-23 04:32:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 42481d1d-daaf-3ada-b152-c09a725c0e99 | -20.18681 | -46.89108 | 2026-04-23 04:32:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cd8fbd22-6600-3a95-ae08-906fbaeaf329 | -21.70593 | -48.43164 | 2026-04-23 04:32:00 | NPP-375D | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d617e3af-8fe6-33d2-92d1-29a649dd3d71 | -18.58633 | -55.9274 | 2026-04-23 04:32:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 1ad5d128-77ec-3003-a0ad-a78c1fb3a4e0 | -20.23533 | -46.79871 | 2026-04-23 04:32:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7d693ab8-90da-3369-b6d1-18316ad016e4 | -19.44398 | -56.6097 | 2026-04-23 04:32:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 6b217a5a-3853-30e7-a6f5-e5ac10cd1f40 | -21.7026 | -48.43104 | 2026-04-23 04:32:00 | NPP-375D | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b24f70ae-8914-37c0-8f52-54458c449411 | -20.19672 | -46.73367 | 2026-04-23 04:32:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c485fd2f-dccd-3114-a572-eb33cc19218a | -20.1879 | -46.90662 | 2026-04-23 04:32:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fe97c371-3bd6-3e04-bd56-8524637353d0 | -20.23815 | -46.80291 | 2026-04-23 04:32:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6710ee7a-2ae9-3131-b77a-54ce76df1723 | -20.16146 | -46.94465 | 2026-04-23 04:32:00 | NPP-375D | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 169fd718-fe03-39d1-9b2d-7a92db763bbd | -17.48609 | -51.09383 | 2026-04-23 04:32:00 | NPP-375D | MONTIVIDIU | GOIÁS | Brasil | 5213756 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README5.md)
