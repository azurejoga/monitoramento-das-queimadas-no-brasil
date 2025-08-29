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

## Dados Diários - Página 70

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9090cab2-1471-36cd-af9b-395274f36b2e | -9.01428 | -65.70718 | 2025-08-29 05:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a1af782c-89be-3f18-90e9-2d84656732e1 | -10.97815 | -46.89869 | 2025-08-29 05:08:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1dc0cd77-1eda-3efb-8c87-f5ac67960b25 | -13.36692 | -51.76903 | 2025-08-29 05:08:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 331c675e-47a6-3cf6-8b90-e30715162ee5 | -12.99271 | -56.91943 | 2025-08-29 05:08:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ba828716-d55c-361e-8c9e-b2b73ae2dd62 | -13.56227 | -46.89658 | 2025-08-29 05:08:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 49688506-788c-3f02-b0f3-32d4b82d0928 | -12.86356 | -48.13983 | 2025-08-29 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 868ff60a-0cc4-3818-9064-d47be2111832 | -15.12567 | -48.11938 | 2025-08-29 05:08:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 20c6fc76-7cef-37c0-a64e-15756ee981bd | -8.8846 | -60.74311 | 2025-08-29 05:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 2f90721d-6601-3373-b056-6c84b9364da2 | -13.41825 | -46.96764 | 2025-08-29 05:08:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d6c33c82-2758-33e5-828b-6b98e441118c | -9.45971 | -60.56455 | 2025-08-29 05:08:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| bd06dc54-809c-3b86-83b5-d06c6e4f40c1 | -11.53987 | -47.31136 | 2025-08-29 05:08:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a6ae67f8-4a54-33f0-9141-6893ef8069a9 | -16.2859 | -53.61571 | 2025-08-29 05:08:00 | NPP-375D | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e78d24f7-a49e-3267-a914-fd6ccb16bfe3 | -9.06838 | -60.40979 | 2025-08-29 05:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 59b7de0d-a63b-371f-96b2-a8fd82a2be52 | -13.55231 | -46.93221 | 2025-08-29 05:08:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0992b7c8-e43f-36ed-af1d-ca094341044e | -8.11742 | -61.22066 | 2025-08-29 05:08:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6bab3abc-5b33-3dda-8311-5112a25d40e0 | -13.41301 | -46.97366 | 2025-08-29 05:08:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 2c736208-8616-390e-8ab0-349581331ad9 | -11.30039 | -43.54947 | 2025-08-29 05:08:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ffece937-f9f4-3075-8f02-565bde5f6575 | -15.8175 | -48.16582 | 2025-08-29 05:08:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 824a16e1-fd20-36db-9817-3095b1030cc9 | -9.16106 | -65.79577 | 2025-08-29 05:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 645cf9a0-8bc8-3347-9820-8cc786ce799e | -13.54184 | -46.86996 | 2025-08-29 05:08:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 8.6 |
| e872692f-0ba8-35a9-910d-de8ed9b595a8 | -13.40312 | -46.99654 | 2025-08-29 05:08:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6a2b06cc-9c3a-39d4-a95c-32d880cb9a1c | -9.30967 | -57.69812 | 2025-08-29 05:08:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 84e270de-b49b-33d6-8a40-d80c151b7b6e | -9.41136 | -60.57077 | 2025-08-29 05:08:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ab286709-9dba-3654-b991-cae70e1e34b8 | -9.16609 | -59.5724 | 2025-08-29 05:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 32404bb2-31fa-3abe-9806-8b783156ed0d | -11.57644 | -49.51764 | 2025-08-29 05:08:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3ceb724b-d9bf-320a-bc23-226b0f2f3c1b | -9.16648 | -65.79681 | 2025-08-29 05:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f435f19c-8c6c-3478-8cea-fdddb22c0625 | -9.15592 | -59.58843 | 2025-08-29 05:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a248bafa-fe23-3d34-a27e-55e90b16cef5 | -10.79401 | -46.36119 | 2025-08-29 05:08:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c472fe76-9477-35a9-a24d-c7b5c003eed3 | -13.45645 | -46.95095 | 2025-08-29 05:08:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 927e4a5c-c2be-3055-a9e7-865fc0d76425 | -11.55788 | -46.3659 | 2025-08-29 05:08:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2331cf95-dc20-38ab-8ebc-10a97509080f | -9.15081 | -59.57429 | 2025-08-29 05:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| eb96cecf-4689-32f5-a7fe-40f3606cc945 | -10.36759 | -57.8107 | 2025-08-29 05:08:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 60b3efd4-8be6-3822-abf5-a0c154c5fde0 | -10.49354 | -51.61835 | 2025-08-29 05:08:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 79cbb760-3760-39c6-b162-9ace92090380 | -11.56189 | -46.37869 | 2025-08-29 05:08:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2e08b882-afd5-3052-932e-2cdfd0eff22e | -8.95974 | -65.96841 | 2025-08-29 05:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 27c15bd6-cf58-3d32-8576-8856a5f0d2fb | -13.02921 | -56.91772 | 2025-08-29 05:08:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0bce26bb-3062-3680-99ba-1c2ad1b4188c | -10.9818 | -46.91434 | 2025-08-29 05:08:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| b271d107-93a6-3680-948d-bfa0fc5f807a | -9.1574 | -59.57962 | 2025-08-29 05:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 54edb00f-f3d8-3902-8276-f9e55f69942a | -12.88511 | -48.13907 | 2025-08-29 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 08cef2cf-2a83-39cf-910b-0ccd66f33f6f | -9.93593 | -46.70647 | 2025-08-29 05:08:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6c9badcf-84e5-3786-b34f-29d1d232cf45 | -9.11425 | -65.77602 | 2025-08-29 05:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 446959cc-78ad-39b0-b9c5-8460ac2135a5 | -8.95006 | -65.95905 | 2025-08-29 05:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0dcb421d-5924-3eab-b3dd-299a072b0bee | -9.12029 | -65.77374 | 2025-08-29 05:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 8e3a9eb2-3d3b-3b59-a4b2-07a7c5ff0efa | -9.45508 | -60.5686 | 2025-08-29 05:08:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 6db0762e-cc78-3ad7-9e4a-eea65ea217fb | -12.93001 | -56.97102 | 2025-08-29 05:08:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7b2d9260-7304-32fb-a954-ed2f2a18bbcf | -13.97355 | -46.336 | 2025-08-29 05:08:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e2dd17e4-1a6e-351e-8928-9730655a0d51 | -13.66611 | -46.91718 | 2025-08-29 05:08:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e1536477-6aef-341d-8c1f-470ff106d0fd | -12.70331 | -48.19419 | 2025-08-29 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4b048bf3-53d6-3227-81ae-adaba589eca7 | -13.00381 | -56.91396 | 2025-08-29 05:08:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fb6a9375-4596-3483-9135-14a0513fb35d | -11.59199 | -46.37723 | 2025-08-29 05:08:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9db7d4c4-1f32-3f3f-8963-99273401d102 | -9.77026 | -64.26244 | 2025-08-29 05:08:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 5ec401bf-17f8-39c0-8ac9-107939aa2047 | -10.62163 | -54.9077 | 2025-08-29 05:08:00 | NPP-375D | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9e373e5d-f1fd-30a2-b5e8-972b02797eb7 | -9.11151 | -65.78749 | 2025-08-29 05:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a10f3d82-4620-3225-a756-7317ba3ca431 | -12.8364 | -48.10546 | 2025-08-29 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| adaf7aa1-3f37-3951-a602-7ab145f81c96 | -12.98129 | -54.7626 | 2025-08-29 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0329bff9-40de-3441-b942-c6b5c5759fdb | -8.88069 | -60.74244 | 2025-08-29 05:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 45466636-34d0-3af3-8a1e-45d3c8ad43e6 | -11.87575 | -46.40162 | 2025-08-29 05:08:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 57a60966-5bce-3888-a039-5ca1e47bb8f5 | -14.52075 | -52.99446 | 2025-08-29 05:08:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d7d62dbe-695b-3f17-ba1f-15e2cc585f46 | -9.60715 | -55.38192 | 2025-08-29 05:08:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 57c577f2-19c5-3fb0-b78e-93321828bc62 | -13.53472 | -46.88319 | 2025-08-29 05:08:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4be651f8-f314-331b-92b0-04064bfb8621 | -12.93611 | -56.97565 | 2025-08-29 05:08:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5d8081df-6fcf-3847-8236-fd9f61a28b9d | -11.31621 | -55.22181 | 2025-08-29 05:08:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f49dff53-55f8-325c-b5f4-c2b143dfbd38 | -8.9593 | -65.96837 | 2025-08-29 05:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a937a66d-920b-305a-aeb3-cb499f926883 | -11.57711 | -49.51262 | 2025-08-29 05:08:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 324943de-fe17-3221-a801-beff8fbc4106 | -9.53559 | -65.69748 | 2025-08-29 05:08:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d8adc90c-ba83-341f-b8d4-f27a563c4ffb | -12.70374 | -48.14817 | 2025-08-29 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d9275984-72b8-3758-9241-058d23ef942d | -11.61761 | -47.31269 | 2025-08-29 05:08:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0d881185-8945-32de-97db-38844ac06817 | -14.2901 | -53.30202 | 2025-08-29 05:08:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 4805dd62-6310-3463-bcd9-b68037ed86bb | -12.42541 | -63.92008 | 2025-08-29 05:08:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 8.2 |
| f6ad27a2-c31d-3c64-aae3-add60af81f35 | -11.41262 | -46.91006 | 2025-08-29 05:08:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 39fe3e34-bb27-3b74-aacd-e782cd689114 | -12.8206 | -48.10284 | 2025-08-29 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 487abbc1-8ee6-383e-9daf-9b53fd815732 | -11.6231 | -47.31336 | 2025-08-29 05:08:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 69387563-b812-333a-9bbd-581efc8b9955 | -12.8479 | -48.1362 | 2025-08-29 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 891018bc-99fc-3c9b-b4c8-1c50f9ace240 | -13.54106 | -46.8793 | 2025-08-29 05:08:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 94f79c7f-420a-3543-8831-8dbc7694e912 | -10.79979 | -46.36185 | 2025-08-29 05:08:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 194a3652-1d05-393f-9931-7020df27c765 | -12.91405 | -48.1221 | 2025-08-29 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 84fd4780-b942-3f25-9be8-3573610950b2 | -8.28469 | -61.40707 | 2025-08-29 05:08:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 41de604e-6aea-3575-aa98-05d8f474b1ca | -9.1993 | -59.66599 | 2025-08-29 05:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2b37e129-0752-38be-99d1-6d5026756117 | -17.04928 | -45.88902 | 2025-08-29 05:08:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| eb209710-5cba-36e9-ad6e-40a9d47355cf | -9.46736 | -60.5659 | 2025-08-29 05:08:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 35ce4977-6752-3da3-8b54-f188783d8d19 | -14.4698 | -48.3797 | 2025-08-29 05:08:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e8d34288-dc06-3b74-b99b-ac0f83ac9a5c | -11.61716 | -47.31628 | 2025-08-29 05:08:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f35db6af-b492-3b2c-aaa7-636641117dd6 | -9.66173 | -65.03365 | 2025-08-29 05:08:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| ab8fa477-2426-3987-9a9f-ec97922b395c | -9.10684 | -65.78555 | 2025-08-29 05:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 025e8ac5-0b7f-34af-8755-7bee79dd1d4d | -13.1893 | -45.28645 | 2025-08-29 05:08:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 210af3fd-8c25-313e-9e64-e61ba5f8b821 | -9.93382 | -46.70662 | 2025-08-29 05:08:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| be57ff42-bb81-393d-b947-274267b68a67 | -9.185 | -60.86199 | 2025-08-29 05:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| db6885a1-f84c-3c1d-a324-76ffb9f72983 | -11.32627 | -43.56917 | 2025-08-29 05:08:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8bf6c54d-bdd8-3c96-a513-9e0b26c0679a | -13.51964 | -46.8585 | 2025-08-29 05:08:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d20cf4af-fb09-314e-ae61-ad8722dd9515 | -15.19535 | -52.34072 | 2025-08-29 05:08:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a0a0edba-a8f7-3ac9-90e9-a6dca82466f4 | -9.30115 | -56.81752 | 2025-08-29 05:08:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7c9e890e-4d7c-3004-9add-60ec21ee05ab | -13.1905 | -45.27604 | 2025-08-29 05:08:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 58bd1e69-d7b6-3d22-8d59-99791d7b94a4 | -12.84123 | -48.10217 | 2025-08-29 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f6fdc944-53bb-3715-878c-0527428b58fa | -15.16893 | -52.33437 | 2025-08-29 05:08:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9ddec5c9-579a-3afe-9efe-b1a9c3ee5430 | -12.85323 | -48.09989 | 2025-08-29 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| dd29e0b2-888a-3ac6-beb1-90dbfecf30f0 | -8.29763 | -61.40557 | 2025-08-29 05:08:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e5241392-161c-3e6a-a81e-8464598463fe | -13.41225 | -46.98033 | 2025-08-29 05:08:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 6ba9a93c-fcb1-3611-8b86-13e263563e10 | -12.68637 | -48.15886 | 2025-08-29 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a445ce2c-071d-3ae5-9599-a4527d395656 | -11.16296 | -47.15561 | 2025-08-29 05:08:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 60cb3d6c-4bb3-3de3-bf3c-b68217a7af61 | -12.88015 | -48.13569 | 2025-08-29 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README71.md)
