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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0fafb983-5e50-33fe-8c77-9669aebb80ed | -11.54404 | -52.77296 | 2026-06-17 05:40:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 20ced610-8cf3-3569-9303-f764e731d679 | -12.18999 | -52.77362 | 2026-06-17 05:40:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f053c970-d2f2-378d-9579-345c28c2aae8 | -11.53812 | -52.77212 | 2026-06-17 05:40:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1d3cc61b-e43b-3a2f-842e-26fe702cafe7 | -12.06128 | -58.04076 | 2026-06-17 05:40:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 428c390e-3529-3015-902c-e18511fc0366 | -10.7779 | -54.10228 | 2026-06-17 05:40:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ba499fa4-7085-3568-87d0-0a61191cc2c9 | -12.07798 | -54.60312 | 2026-06-17 05:40:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 514463cc-d205-3c32-b376-3e153d56350b | -11.71962 | -54.49283 | 2026-06-17 05:40:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3b575dc6-7de2-3282-bedb-79ad4c714a73 | -12.21767 | -52.79533 | 2026-06-17 05:40:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 99e831a7-cc4a-3a1b-b53d-2557d52b4214 | -9.19028 | -58.05217 | 2026-06-17 05:40:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a3680afa-6c62-3391-9003-fd5a6727a755 | -12.21931 | -52.78209 | 2026-06-17 05:40:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 4498f32e-0ffd-3b77-84d9-43f23ba08660 | -10.15248 | -56.60541 | 2026-06-17 05:40:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a2581f1e-c67c-3967-969d-f73328cc7674 | -7.86287 | -61.49133 | 2026-06-17 05:40:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0038a6a7-8d28-3477-81e0-50ce2182b684 | -12.20736 | -52.78048 | 2026-06-17 05:40:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 17.0 |
| f5b0d561-dc57-3766-b890-80f06a36757f | -12.22365 | -52.79608 | 2026-06-17 05:40:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 11.4 |
| b4d38800-6c6e-383d-a1e3-b6af79c41247 | -12.08199 | -54.61378 | 2026-06-17 05:40:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 0ea36ec6-01b9-366c-a94b-522e20f79503 | -11.91464 | -55.91451 | 2026-06-17 05:40:00 | NPP-375D | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 967d6d29-353b-3b86-8584-69746f1c043b | -11.48497 | -57.10611 | 2026-06-17 05:40:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fd37b887-d038-3680-9326-59bf12f46a74 | -11.5435 | -52.77732 | 2026-06-17 05:40:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| be75a8f9-4678-31c9-ba4c-c3eb79f8d3f7 | -12.21446 | -52.78795 | 2026-06-17 05:40:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 44.1 |
| 75bbfcc1-7409-33d5-a797-2d4ef6515e5a | -12.19005 | -52.7892 | 2026-06-17 05:40:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 9b4a3837-4695-321b-9416-9fb0a1f8e483 | -10.77971 | -54.1025 | 2026-06-17 05:40:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d0497dcb-f30e-3262-8f86-d455c5b46ec7 | -11.58644 | -55.33921 | 2026-06-17 05:40:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d9db80fd-5fdf-39b7-837b-0200f97e06e9 | -11.53706 | -52.78073 | 2026-06-17 05:40:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 008926c9-45ce-3bf2-8a65-63bafce8fc2d | -12.2117 | -52.79458 | 2026-06-17 05:40:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 74.1 |
| fe639685-9e68-38a3-8994-766d413a9038 | -12.18782 | -52.79149 | 2026-06-17 05:40:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| dc90f7cf-c366-378d-865d-b2c29e03402d | -12.19597 | -52.77439 | 2026-06-17 05:40:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 99403d42-0f35-35c1-acb1-7fb94a26fd55 | -12.20139 | -52.77968 | 2026-06-17 05:40:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 7ec20e7c-294c-3131-84ea-6c738f1e2cae | -12.22474 | -52.78727 | 2026-06-17 05:40:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 10.9 |
| af11b897-a578-350f-a01a-3fb600c7f763 | -12.22095 | -52.7843 | 2026-06-17 05:40:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 3013c60a-326e-3342-a82a-b3dfb6966cc1 | -12.21394 | -52.79237 | 2026-06-17 05:40:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 44.1 |
| 76304036-8d83-3b4b-9a66-c5d932372bf4 | -10.27369 | -60.55195 | 2026-06-17 05:40:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e583988f-1c9b-3dac-9be7-5729703e7799 | -12.06043 | -58.0419 | 2026-06-17 05:40:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f2483778-5b69-3132-abf2-65dd17b1209c | -10.77161 | -54.1084 | 2026-06-17 05:40:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8769cff6-f9fd-38fd-a162-7a6574a449a0 | -12.20303 | -52.78186 | 2026-06-17 05:40:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| efdce13c-9f20-3c9d-8546-a0d3ea4a2fd3 | -12.19211 | -52.77123 | 2026-06-17 05:40:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 081fbd04-6b33-3bcd-b957-7bf885deb654 | -11.59109 | -55.34213 | 2026-06-17 05:40:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 4f54efdf-3c20-35ba-90fe-6ee777cbce94 | -12.21889 | -52.80195 | 2026-06-17 05:40:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 17.7 |
| 5c50e846-a7e4-3e79-b86c-4a985c7d757d | -10.63719 | -51.8012 | 2026-06-17 05:40:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a2c19f98-2cee-3de4-89e3-afd3781a04ae | -12.21497 | -52.78352 | 2026-06-17 05:40:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 8f1db68b-184b-3f25-95c4-285a84e82549 | -12.21224 | -52.79017 | 2026-06-17 05:40:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 74.1 |
| a63a7cce-a72d-3bd6-aa09-012538db9d44 | -11.54942 | -52.77816 | 2026-06-17 05:40:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3fc1e535-bf7a-3419-8db2-252b98bf09d5 | -12.20848 | -52.78715 | 2026-06-17 05:40:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 43.6 |
| f6f242cc-6507-3776-b505-a77d9f4d17b0 | -12.19379 | -52.79227 | 2026-06-17 05:40:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 9c1faa60-4e50-3abf-9514-034fc8e51c26 | -10.15187 | -56.60985 | 2026-06-17 05:40:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| ff992497-cf85-3060-aaa8-c3f3fce82d5e | -12.66988 | -54.57962 | 2026-06-17 05:40:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1c35df15-e407-3639-9c06-736eb42bfd9a | -12.21279 | -52.78575 | 2026-06-17 05:40:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 17.0 |
| ae847f66-a3ca-37b2-8e6f-d1fc6220fa81 | -12.0819 | -54.60647 | 2026-06-17 05:40:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7cc8185b-2044-3409-9faf-1833c6c0f0f5 | -12.17804 | -52.77206 | 2026-06-17 05:40:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ea356016-b37d-3ed9-9dad-6daed307bc56 | -12.18401 | -52.77285 | 2026-06-17 05:40:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 719041c8-8fdf-3751-90f1-fbe3f346197e | -12.18347 | -52.77735 | 2026-06-17 05:40:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| f789f032-5cc5-3a89-b523-c7b405247ed7 | -12.19552 | -52.79444 | 2026-06-17 05:40:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 4d057190-5570-3cb8-a33b-a7f9bb99f122 | -7.32238 | -64.70596 | 2026-06-17 05:40:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 76411825-8c72-3f46-a653-8779c33d8445 | -12.08231 | -54.6031 | 2026-06-17 05:40:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 50b35acc-a439-300c-b1fd-d781145bccb8 | -12.22043 | -52.78873 | 2026-06-17 05:40:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 44.1 |
| 7d6bf353-4d28-356d-939a-53b0fc18c855 | -12.20085 | -52.78415 | 2026-06-17 05:40:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 8.3 |
| d34cf4e6-8017-35aa-b21e-abbe447b3311 | -11.59183 | -55.33636 | 2026-06-17 05:40:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4cbb83dc-2a11-3531-a773-87b16c0ccde1 | -12.08116 | -54.62021 | 2026-06-17 05:40:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 85f29f06-73ed-3e96-af95-3bbc06d8dc70 | -12.20797 | -52.79158 | 2026-06-17 05:40:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 43.6 |
| de7a6d2e-8f96-3c2f-ae79-cb5751871406 | -10.77927 | -54.10598 | 2026-06-17 05:40:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0cfd8673-ac9d-34b6-afd8-cf149f96973c | -12.21822 | -52.79092 | 2026-06-17 05:40:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 21bfa342-772f-366a-94a6-44b7b1d83b5a | -9.88126 | -52.44328 | 2026-06-17 05:40:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 82a3bfb3-56d5-3d0d-abc3-4541a18b0692 | -12.17695 | -52.78104 | 2026-06-17 05:40:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| e6119ae2-a1d2-3f10-9d25-06dfdaa9a169 | -10.64341 | -51.80206 | 2026-06-17 05:40:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ea9626a0-8e5b-316d-a95d-2d5ac3d19f3d | -12.21116 | -52.79897 | 2026-06-17 05:40:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 27.8 |
| a1f71003-0e6f-3d97-a087-a10c21a321c8 | -12.17152 | -52.77576 | 2026-06-17 05:40:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| ee8609b3-c087-360d-bc4e-c00e9d12c72c | -11.3557 | -55.81987 | 2026-06-17 05:40:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a8f9c3ba-95f3-3248-8f63-009cacc61597 | -10.58652 | -53.51337 | 2026-06-17 05:40:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2adea53c-0633-36ec-9e6f-ee61879476d3 | -9.85408 | -62.37494 | 2026-06-17 05:40:00 | NPP-375D | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| a47e0048-8d5e-332e-896e-32bfb18f3eae | -7.63412 | -50.0249 | 2026-06-17 05:40:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9f32436b-237d-3418-a0f9-b62ed777c622 | -12.20519 | -52.7982 | 2026-06-17 05:40:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 27.8 |
| 5798e77a-9bfa-3ed1-aee0-774a6721d9ef | -12.19705 | -52.78105 | 2026-06-17 05:40:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| c88e45c1-0bfa-37b7-afa6-f480a7153a0e | -12.19976 | -52.79304 | 2026-06-17 05:40:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 3bdc9902-4763-321a-a08d-d8e94b89fdf9 | -11.55535 | -52.77893 | 2026-06-17 05:40:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d500b9fa-0376-3bd9-be20-f211317d7e5b | -9.20435 | -58.06864 | 2026-06-17 05:40:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| db58c18b-5f5d-31e0-b5a6-247a2899cb47 | -10.76625 | -54.10755 | 2026-06-17 05:40:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e3470dd3-b44c-3b89-9f48-59603e1e5dd6 | -12.46994 | -55.12569 | 2026-06-17 05:40:00 | NPP-375D | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3593973f-5d93-331c-b554-4997baf42529 | -12.2329 | -52.78583 | 2026-06-17 05:40:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f791616f-cbfd-384b-91c4-6a687183b627 | -12.20746 | -52.796 | 2026-06-17 05:40:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 29.0 |
| 2dbe1fd6-3811-3fe9-9af5-74f26f764fe8 | -12.0815 | -54.60979 | 2026-06-17 05:40:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 206c2eeb-2769-3a3a-b10b-e3525b3ffcaf | -12.47033 | -55.12257 | 2026-06-17 05:40:00 | NPP-375D | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6a009729-47f3-3c4a-b6a3-1f7078b4178e | -12.67522 | -54.58032 | 2026-06-17 05:40:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 24eda248-131c-385e-bf2a-0b36bc73b61e | -12.19757 | -52.77656 | 2026-06-17 05:40:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 0f67870d-e450-3538-9787-2dfb7bc3562e | -12.2231 | -52.80049 | 2026-06-17 05:40:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 10.1 |
| ce56d3da-fddf-38ff-aa78-3491d8e4ca9b | -11.47994 | -57.10991 | 2026-06-17 05:40:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 76db7c7d-ffda-34f0-b034-355f319ab76e | -10.12566 | -52.18367 | 2026-06-17 05:40:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6ad3116a-20af-3b49-b2aa-27a221716522 | -12.21292 | -52.80117 | 2026-06-17 05:40:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 17.7 |
| b4c30894-4f5b-3b88-aaba-bec9b95b2499 | -10.2743 | -60.5479 | 2026-06-17 05:40:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b0b62022-2c6f-33b5-a900-664ca701fa61 | -10.77116 | -54.11179 | 2026-06-17 05:40:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8de0cb06-88de-35af-a495-4c663a1fec0f | -12.0807 | -54.61631 | 2026-06-17 05:40:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 7747f930-b05e-32b3-83a0-179ca4762e3f | -10.27491 | -60.54385 | 2026-06-17 05:40:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 26093a72-c651-3a1e-aea1-060dd30f676e | -12.07755 | -54.60646 | 2026-06-17 05:40:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d76360a2-ada7-312e-8077-4388b7fea58b | -12.19433 | -52.78784 | 2026-06-17 05:40:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 58a36360-4ef9-3fb2-a490-f0e55ea813c6 | -9.46496 | -57.83668 | 2026-06-17 05:40:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| efe4e213-0e15-37bf-ba2d-c3cceabcd55d | -12.20573 | -52.79381 | 2026-06-17 05:40:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 74.1 |
| f61c71c4-4c30-3b93-9edb-6db79ee9a85d | -12.22589 | -52.79391 | 2026-06-17 05:40:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 692086a7-a91a-3893-8279-02f5c455a222 | -12.20627 | -52.78939 | 2026-06-17 05:40:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 5a20e498-32a1-35b2-a7b2-e7863032add3 | -9.18576 | -58.05508 | 2026-06-17 05:40:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2e35d16d-b382-3e84-a79e-ece934252c1e | -12.20194 | -52.77521 | 2026-06-17 05:40:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 72206a7f-7a00-3c06-90b9-0e388d9009f5 | -12.4295 | -58.40974 | 2026-06-17 05:42:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5319a50d-d4f7-3760-b903-e05c404b9bca | -14.09977 | -59.46348 | 2026-06-17 05:42:00 | NPP-375D | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README16.md)
