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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 10190959-62b1-3e57-b35c-d3435b88ac87 | -16.45496 | -51.98256 | 2025-09-10 04:17:00 | NOAA-21 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1fd26f5a-9870-344b-9acc-f010738e5bdf | -10.19335 | -46.67497 | 2025-09-10 04:17:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 493f3115-da34-34da-8f71-d4a59b6dfff7 | -10.1939 | -46.67829 | 2025-09-10 04:17:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 405bde49-5df8-3954-9de7-02982ffc6204 | -13.94498 | -48.25364 | 2025-09-10 04:17:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 09997f85-d6b0-33f6-b359-00701292e164 | -21.40013 | -43.87589 | 2025-09-10 04:17:00 | NOAA-21 | ANTÔNIO CARLOS | MINAS GERAIS | Brasil | 3102902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| b538107c-77a5-3e1f-ba58-80648d064036 | -20.28743 | -46.25087 | 2025-09-10 04:17:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5cc427ad-0083-3d06-82e4-f0ebf6dc2be0 | -14.35534 | -47.30682 | 2025-09-10 04:17:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| bdb7ddcd-f508-3aa3-aa4d-7bdb40f94709 | -13.02287 | -48.03738 | 2025-09-10 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8d4da2c6-85fe-3dfb-9b3e-823e5f1ce943 | -14.2515 | -47.10787 | 2025-09-10 04:17:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 22e089c5-8e7d-39ee-bf9d-046d1dffd252 | -13.04355 | -47.16475 | 2025-09-10 04:17:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 489825b6-82ec-356c-89fb-68824ad4ecf6 | -15.15275 | -44.0279 | 2025-09-10 04:17:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e2f3c59d-0441-3cec-bf45-e2e426ab608a | -20.7575 | -45.34503 | 2025-09-10 04:17:00 | NOAA-21 | CANDEIAS | MINAS GERAIS | Brasil | 3112000 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1e252132-73e4-3a26-be43-bcf3bfcef50a | -10.27546 | -48.81959 | 2025-09-10 04:17:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e829b8c6-45bc-3eda-b1d1-02556a3401f9 | -10.30861 | -48.81444 | 2025-09-10 04:17:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3ea10af4-1d27-328a-bfcd-0ca74ffa20b2 | -15.22758 | -44.02453 | 2025-09-10 04:17:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 81eb7580-c089-34c1-bf7a-a5dbde01ad91 | -22.1569 | -47.66217 | 2025-09-10 04:17:00 | NOAA-21 | ANALÂNDIA | SÃO PAULO | Brasil | 3502002 | 35 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c1a5779d-cb18-354c-abd4-4310250d6175 | -11.45597 | -43.62398 | 2025-09-10 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 02fa6c2e-c43a-3dab-9e8d-cae19fde3458 | -15.10546 | -48.03005 | 2025-09-10 04:17:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e2d96965-f7e7-3f4e-a429-fa862c6b61b8 | -11.18579 | -48.37405 | 2025-09-10 04:17:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f415f1db-a6c9-3284-9495-37f9526a77d5 | -15.78701 | -43.12965 | 2025-09-10 04:17:00 | NOAA-21 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 756931de-5821-3c61-9f5d-f56b00badd18 | -14.33189 | -47.30338 | 2025-09-10 04:17:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 43b2144d-5414-330f-acf2-ff397760f15c | -15.11871 | -47.02887 | 2025-09-10 04:17:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 87910943-1526-3354-9d01-ffb6c66a2987 | -10.00896 | -48.08757 | 2025-09-10 04:17:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 21.0 |
| 4c834b6d-6b57-39f6-adeb-0124fdbbfdd9 | -15.80915 | -52.24606 | 2025-09-10 04:17:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 57dff797-bead-3bf5-8d36-4cc3ae41de4b | -11.44166 | -49.26143 | 2025-09-10 04:17:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e93f8f2c-8a9e-3c13-86e1-03ecc1b90495 | -13.20007 | -43.37438 | 2025-09-10 04:17:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| c03a59fb-726c-34d5-9a89-15a6737cc96e | -21.30815 | -43.88834 | 2025-09-10 04:17:00 | NOAA-21 | BARBACENA | MINAS GERAIS | Brasil | 3105608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 572caf23-0837-35bb-9608-16e034f75afe | -11.10901 | -48.36702 | 2025-09-10 04:17:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 925b1260-d470-3166-81e7-65a1c8c49861 | -13.19421 | -45.27991 | 2025-09-10 04:17:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6046104b-4863-3b62-ba60-720f445ec82e | -20.09941 | -47.81163 | 2025-09-10 04:17:00 | NOAA-21 | ARAMINA | SÃO PAULO | Brasil | 3503000 | 35 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 68c76785-8436-3208-bbfb-2c71ae20b7b5 | -10.72127 | -48.29221 | 2025-09-10 04:17:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e9fc6207-2448-3c0d-b9b6-65cf828149e3 | -10.00942 | -51.67581 | 2025-09-10 04:17:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 21fe7f2f-d9f7-362c-9808-a405d9f05a84 | -11.34292 | -46.53715 | 2025-09-10 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d7aeca3f-8895-3cd4-80e3-05a33ad6fb3d | -15.02246 | -50.08646 | 2025-09-10 04:17:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 37.0 |
| f82dcd41-6c15-3d99-af6f-ed0ca09c7869 | -17.56389 | -44.5461 | 2025-09-10 04:17:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| efa56947-92af-32ca-8b02-ead041055bf6 | -20.09667 | -47.80727 | 2025-09-10 04:17:00 | NOAA-21 | ARAMINA | SÃO PAULO | Brasil | 3503000 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| add7985a-0f7c-3d37-a52b-8365ae8648b8 | -15.22482 | -44.04284 | 2025-09-10 04:17:00 | NOAA-21 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 10aa26c1-8d08-3698-9afd-75934d288511 | -15.94254 | -50.22763 | 2025-09-10 04:17:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4039b2f7-3904-327f-af36-5a6d62611fcc | -15.48953 | -49.49142 | 2025-09-10 04:17:00 | NOAA-21 | RIANÁPOLIS | GOIÁS | Brasil | 5218706 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 85cb85d0-3ef2-3e26-98c1-bafea5306900 | -15.87574 | -52.20993 | 2025-09-10 04:17:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| effe9b31-f4d4-3ce6-89e7-1d192d88f7a7 | -22.87292 | -51.23417 | 2025-09-10 04:17:00 | NOAA-21 | ALVORADA DO SUL | PARANÁ | Brasil | 4100806 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 3d0aa975-db5d-3594-b494-1d80d6f8e867 | -23.28805 | -45.95047 | 2025-09-10 04:17:00 | NOAA-21 | JACAREÍ | SÃO PAULO | Brasil | 3524402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 98dae286-8a02-3e6d-a662-23af0ca5afc4 | -16.57213 | -49.22809 | 2025-09-10 04:17:00 | NOAA-21 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e08be1ca-e4e5-3216-9166-325555dbfbfa | -14.93066 | -55.91887 | 2025-09-10 04:17:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e4ffc298-34b9-3d93-978b-6234efa062a7 | -11.37853 | -45.5869 | 2025-09-10 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c5c4eda8-fb72-31ee-beeb-8c7c1b2da186 | -20.53286 | -47.63826 | 2025-09-10 04:17:00 | NOAA-21 | SÃO JOSÉ DA BELA VISTA | SÃO PAULO | Brasil | 3549508 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ed357e5a-170e-3174-928c-570536b93f2d | -23.02794 | -50.10708 | 2025-09-10 04:17:00 | NOAA-21 | CAMBARÁ | PARANÁ | Brasil | 4103602 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 262602ee-6c3f-3b01-88af-5c38e3f9f43f | -23.14236 | -48.26293 | 2025-09-10 04:17:00 | NOAA-21 | BOFETE | SÃO PAULO | Brasil | 3506904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| a911ebc1-9d88-30da-9348-5301076a8e23 | -13.17874 | -47.25471 | 2025-09-10 04:17:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2727c92d-52a2-36bd-ba85-3325f5e16ac7 | -10.02627 | -51.66405 | 2025-09-10 04:17:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 16.1 |
| bbe43605-f35a-34af-86e4-5f891c369091 | -20.93455 | -45.79737 | 2025-09-10 04:17:00 | NOAA-21 | ILICÍNEA | MINAS GERAIS | Brasil | 3130507 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 42e0fd96-a95a-3e5f-9530-8bf70fe399cd | -17.75026 | -44.47681 | 2025-09-10 04:17:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 956604df-aaa0-39f6-bf3b-a005a0733f10 | -11.32077 | -46.52158 | 2025-09-10 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 39a65363-b1a7-32f6-92c7-03b272c4aa0e | -12.042 | -51.04416 | 2025-09-10 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0986e868-35e7-37e2-af1a-8f7974728d94 | -11.68314 | -46.89981 | 2025-09-10 04:17:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e0ae69ea-ba5f-3ee6-af95-b5c4905d2ce9 | -11.43764 | -43.6322 | 2025-09-10 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2fb05692-8977-326b-b476-6215f9e67d1a | -14.74778 | -45.33062 | 2025-09-10 04:17:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2c48067f-d372-31e7-8cfa-5807aed60a31 | -15.96183 | -49.6194 | 2025-09-10 04:17:00 | NOAA-21 | ITAGUARI | GOIÁS | Brasil | 5210562 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b44b5836-df87-3eae-9cc4-346b08840eb5 | -17.71642 | -44.43728 | 2025-09-10 04:17:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| aa186ef0-db10-3d3a-8e58-84abc3784892 | -12.92867 | -54.7635 | 2025-09-10 04:17:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 0bde240b-da7d-37c6-b8e8-cd9899171efe | -23.35942 | -47.20416 | 2025-09-10 04:17:00 | NOAA-21 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| b6466ef1-d0b8-3aeb-8e45-506e4cc42d96 | -15.87497 | -52.20762 | 2025-09-10 04:17:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2b904799-f78b-3874-9b32-40635dce4bc8 | -16.6729 | -48.51833 | 2025-09-10 04:17:00 | NOAA-21 | VIANÓPOLIS | GOIÁS | Brasil | 5222005 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bb6a48c0-3ac9-37e8-9057-736a63747891 | -20.99224 | -47.99253 | 2025-09-10 04:17:00 | NOAA-21 | PONTAL | SÃO PAULO | Brasil | 3540200 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f9de9b08-41d3-3bf5-a8ed-ede6eacf3942 | -11.03882 | -46.05138 | 2025-09-10 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cb1b9584-4ee7-3267-adf3-adcb1827f526 | -10.47194 | -47.9485 | 2025-09-10 04:17:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bfa2f833-5fd0-3140-a797-b12e7563a011 | -20.70789 | -46.05898 | 2025-09-10 04:17:00 | NOAA-21 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f766d8ed-7921-3317-bd42-85fa11c7135f | -15.64481 | -48.087 | 2025-09-10 04:17:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5c97a83b-b16b-30c2-8319-5e38a0e8466e | -10.27154 | -48.81897 | 2025-09-10 04:17:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| eaef7c15-cac1-3aac-99e8-2c2924940db9 | -12.0147 | -50.99414 | 2025-09-10 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 19132015-866d-364b-b35b-cd794d7f7c66 | -13.54279 | -44.13445 | 2025-09-10 04:17:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| a52f1e0c-5415-3e67-9835-91c95f2b7045 | -15.14606 | -44.02682 | 2025-09-10 04:17:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6b9e80f6-cd91-3fe4-88f7-c6c2789e3bf1 | -11.43709 | -43.63573 | 2025-09-10 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2c84e0b3-e9dd-31c1-bded-ccd7d7598d40 | -10.27633 | -48.81459 | 2025-09-10 04:17:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f6722097-d1d5-37ff-988e-571c78cade82 | -15.69869 | -49.89556 | 2025-09-10 04:17:00 | NOAA-21 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8119a1af-b3d9-350b-82f7-973f85e8c390 | -16.46094 | -51.97477 | 2025-09-10 04:17:00 | NOAA-21 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7cd026b1-bbb8-38ee-bd23-caf5378a215d | -13.96699 | -48.2207 | 2025-09-10 04:17:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 6b356e70-17d3-3cf0-becd-e22270d4f0d2 | -13.92705 | -48.24994 | 2025-09-10 04:17:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 84541c3f-69df-38c7-b604-fb48038711fb | -13.01637 | -48.03912 | 2025-09-10 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2e4b4982-6192-34f5-b3e1-196b678e2baa | -15.27472 | -53.78156 | 2025-09-10 04:17:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0ae9dd3a-8636-3c2b-ad54-6e3a0edcb78f | -13.95716 | -48.24743 | 2025-09-10 04:17:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 26fa1470-5be8-38e9-8468-37722211a72d | -11.87117 | -47.53465 | 2025-09-10 04:17:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 364fc9fd-8090-3021-95ee-635c15664b94 | -16.46136 | -50.67087 | 2025-09-10 04:17:00 | NOAA-21 | MOIPORÁ | GOIÁS | Brasil | 5213400 | 52 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 1df54da3-8420-3e0f-b2a2-1d57c566efba | -17.32739 | -46.70058 | 2025-09-10 04:17:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e85b8082-6c1c-3d38-b47e-bb91bd4aa056 | -15.47984 | -49.38938 | 2025-09-10 04:17:00 | NOAA-21 | RIANÁPOLIS | GOIÁS | Brasil | 5218706 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 32918780-89d5-32f2-bf2f-39b36021155b | -10.72881 | -48.29353 | 2025-09-10 04:17:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4900260e-8ef6-3796-8b40-05b0809ccd1f | -11.29895 | -53.96542 | 2025-09-10 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 519ee64d-a9c3-3fda-b6e1-a0fa13852827 | -17.16059 | -50.15399 | 2025-09-10 04:17:00 | NOAA-21 | JANDAIA | GOIÁS | Brasil | 5211701 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b7b8d883-7d56-3da3-a046-0eb0e2f76fbd | -11.75429 | -50.62526 | 2025-09-10 04:17:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3505bb94-f107-3144-8c85-4e81d5a7402b | -12.99336 | -48.03616 | 2025-09-10 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fc806bde-4979-3e73-8dfe-b6a18cd3cb73 | -22.58475 | -46.71806 | 2025-09-10 04:17:00 | NOAA-21 | SERRA NEGRA | SÃO PAULO | Brasil | 3551603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| ecca5ae8-9ac9-3809-8d34-816343d5f189 | -13.97476 | -48.24007 | 2025-09-10 04:17:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 67deed08-1e66-3d8c-9adb-d3112ff04b9c | -16.05548 | -49.97514 | 2025-09-10 04:17:00 | NOAA-21 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5eb6ac49-e1d6-3ff4-b3b1-e3373058ddab | -14.92269 | -50.10269 | 2025-09-10 04:17:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 45f3732e-19b5-3f9b-b9b1-b787685cf52e | -23.03121 | -50.10939 | 2025-09-10 04:17:00 | NOAA-21 | CAMBARÁ | PARANÁ | Brasil | 4103602 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 922e70dc-057d-34d6-b6ec-6e0f55b96678 | -21.58154 | -43.97239 | 2025-09-10 04:17:00 | NOAA-21 | SANTA RITA DE IBITIPOCA | MINAS GERAIS | Brasil | 3159407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 988c11eb-85a7-327c-a5a7-5cd5c0b8d188 | -16.28133 | -45.68198 | 2025-09-10 04:17:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a7b1acc3-1d39-3b52-b70b-3b4febed3a18 | -23.09473 | -46.673 | 2025-09-10 04:17:00 | NOAA-21 | ATIBAIA | SÃO PAULO | Brasil | 3504107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 6f52a585-343d-3cc1-a305-691aec707504 | -21.59854 | -43.97955 | 2025-09-10 04:17:00 | NOAA-21 | SANTA RITA DE IBITIPOCA | MINAS GERAIS | Brasil | 3159407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 0e733e9a-d941-3179-b9e9-6e4c244a39b7 | -15.77791 | -53.64511 | 2025-09-10 04:17:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README42.md)
