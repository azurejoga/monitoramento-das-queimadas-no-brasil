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

## Dados Diários - Página 69

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fbcc4013-890e-33d9-9345-70bab481376a | -15.87543 | -56.48858 | 2026-08-31 05:38:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 06c407fa-5de1-3402-8f82-002fc9abe097 | -14.23158 | -52.8516 | 2026-08-31 05:38:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d41e3320-de2e-3207-b634-0c0d162b2fac | -14.21093 | -52.83844 | 2026-08-31 05:38:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 45d1407a-9c44-3903-bfaa-7f72e6650460 | -15.63342 | -50.09572 | 2026-08-31 05:38:00 | NPP-375D | GUARAÍTA | GOIÁS | Brasil | 5209291 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 93251f6b-a177-34e1-ac99-561b0fc23bb2 | -14.58041 | -54.08706 | 2026-08-31 05:38:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9ce5dc00-744d-3e27-9fd2-fa883c117f55 | -20.2524 | -58.15759 | 2026-08-31 05:38:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.5 |
| eba73e3c-ac8b-3a30-9c09-9158ec234628 | -15.02364 | -48.16835 | 2026-08-31 05:38:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d5d70be9-ef9b-36f4-a3ed-87a1d1b38526 | -14.58075 | -54.11774 | 2026-08-31 05:38:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0b5428c3-ac26-30fb-87ec-98882c947538 | -15.54964 | -56.28438 | 2026-08-31 05:38:00 | NPP-375D | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 06d015ef-9ab6-31be-9834-9eeb05906d45 | -14.46628 | -52.19517 | 2026-08-31 05:38:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0df87d69-6c95-30f7-aa7b-6165a4c45e2f | -14.59291 | -54.10186 | 2026-08-31 05:38:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 13f84f15-f48f-3d2e-b003-5d67bd804616 | -20.2546 | -58.14929 | 2026-08-31 05:38:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 28.0 |
| 1edd9446-eb3b-3911-988d-aff314379e11 | -19.11879 | -57.41226 | 2026-08-31 05:38:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 0051abf9-0890-3a04-ae41-1a0ffc61f090 | -14.29874 | -52.90312 | 2026-08-31 05:38:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 48f9a643-eabe-346d-8819-631ccd1b8843 | -15.87509 | -56.49051 | 2026-08-31 05:38:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b165a0b3-b9f1-3321-88de-abecc7f1087c | -15.24203 | -53.86956 | 2026-08-31 05:38:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 019f4ba5-eb99-30e8-90c0-2ab6034046d7 | -14.29915 | -52.8996 | 2026-08-31 05:38:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f8b36c12-e46d-37c3-b865-10054f952f7d | -14.57665 | -54.11669 | 2026-08-31 05:38:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2aa1c55d-af5f-3805-838c-8f93a7ce2a2d | -15.08875 | -48.10962 | 2026-08-31 05:38:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b6a90c74-05fb-36fb-b983-e8120a197b35 | -14.44797 | -52.52134 | 2026-08-31 05:38:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 68ee187c-c52f-37ec-93dd-1beef529e10b | -15.23647 | -53.87222 | 2026-08-31 05:38:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 72280870-4f3a-39f5-877a-7e97c73180eb | -14.58095 | -54.12322 | 2026-08-31 05:38:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| faf6fd64-4cad-322e-ab66-33d6b0eab62c | -14.38932 | -52.55736 | 2026-08-31 05:38:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0a8d96e6-50c8-34ac-adfa-27db5037c83d | -14.68335 | -54.9076 | 2026-08-31 05:38:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 2a0a073d-a2ca-3ea7-ad94-81365befbf7f | -20.25657 | -58.15819 | 2026-08-31 05:38:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 4705d0a1-b71d-3177-8036-03314972a6ef | -14.14248 | -52.80562 | 2026-08-31 05:38:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d23600ea-86db-3cac-9d1a-9bfabe469dda | -14.59221 | -54.10763 | 2026-08-31 05:38:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 978cfdef-b79b-3f1d-8b36-50adfafcd7e6 | -14.17868 | -52.87794 | 2026-08-31 05:38:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f394cbd8-5374-30c7-b454-91a0a82fb2e4 | -13.97248 | -54.401 | 2026-08-31 05:38:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8564dac9-e8a1-3b38-b8e1-38bc8fb45449 | -15.23934 | -53.87907 | 2026-08-31 05:38:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 16599af4-81a6-3b61-85d3-110374dd652b | -20.25291 | -58.15362 | 2026-08-31 05:38:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 22.1 |
| 052318da-f621-37d8-9a2b-cc6690a439d8 | -15.24092 | -53.87918 | 2026-08-31 05:38:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 55a07730-2b77-3778-983e-b5cab9fb95d9 | -14.44784 | -52.54193 | 2026-08-31 05:38:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b06d9554-d455-345d-a3d2-5a0194166a83 | -20.25878 | -58.14988 | 2026-08-31 05:38:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 28.0 |
| 88e27fe8-c547-3bfb-80c9-19268ce2c21d | -15.61088 | -56.39754 | 2026-08-31 05:38:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 08b77c44-2cf7-3c43-b8f9-60faf14a16ba | -20.25829 | -58.15388 | 2026-08-31 05:38:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 28.0 |
| fcf8f14c-2e90-3f30-8687-110837f77786 | -15.61796 | -56.41178 | 2026-08-31 05:38:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 29403d04-fc1e-3d87-86f9-4f449b8a106c | -14.68297 | -54.91166 | 2026-08-31 05:38:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 12cf8828-014e-3cfc-bdf4-a2da5dcdb4e3 | -14.14207 | -52.80911 | 2026-08-31 05:38:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ab3e2b2c-b407-39e9-8f18-9803ec89b6a2 | -14.44197 | -52.52416 | 2026-08-31 05:38:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 15929b8f-e4fe-3e81-ae48-65cf97b8f1f4 | -15.91327 | -56.2209 | 2026-08-31 05:38:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 913474df-ea6e-3245-be02-91213c58901b | -14.58508 | -54.12431 | 2026-08-31 05:38:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3a770bbe-7d45-3e6f-9909-13ddc745f01c | -14.40959 | -52.5297 | 2026-08-31 05:38:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 16.2 |
| ee5548d4-8caa-3c34-a4d4-3c3af42d181e | -14.60087 | -54.12081 | 2026-08-31 05:38:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8441eb51-bc5a-3b88-9686-ac6ab7445fbb | -14.43599 | -52.52691 | 2026-08-31 05:38:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 449816e5-7e1e-3e22-ad8e-e7c5a7cbfeea | -20.25342 | -58.14964 | 2026-08-31 05:38:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 22.1 |
| ef968430-a915-3c73-addd-6d24de659543 | -15.23726 | -56.39053 | 2026-08-31 05:38:00 | NPP-375D | ACORIZAL | MATO GROSSO | Brasil | 5100102 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 556561b1-0577-315d-abbe-c814c6f8e19c | -14.17838 | -52.87588 | 2026-08-31 05:38:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5e263bbf-e628-34bd-81e4-1e166afee152 | -15.6174 | -56.41614 | 2026-08-31 05:38:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3ba0b0c9-799f-3b34-8bf7-f63ce263f9c1 | -14.59653 | -54.11438 | 2026-08-31 05:38:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 76d59d8e-1946-30c6-9ded-c2a35bfea984 | -14.41003 | -52.52593 | 2026-08-31 05:38:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 16.4 |
| ced69f02-32f5-397d-ab4e-3e5c6961f244 | -16.35833 | -51.0078 | 2026-08-31 05:38:00 | NPP-375D | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 76284bc6-c3ca-3304-8903-0bae0e481d4a | -14.58323 | -54.10526 | 2026-08-31 05:38:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 837dfe04-2922-3a43-bb0c-8894c521b268 | -14.44447 | -52.52287 | 2026-08-31 05:38:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| fad2bb87-9c71-3ddc-8b89-2ea566708d69 | -15.67591 | -56.27711 | 2026-08-31 05:38:00 | NPP-375D | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 07f4ef2e-ad28-3987-a013-a35eb67277fa | -15.55021 | -56.28 | 2026-08-31 05:38:00 | NPP-375D | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1710b711-3009-3dba-8bbc-0c17676538fe | -14.40353 | -52.53296 | 2026-08-31 05:38:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 7e9a938b-a710-3620-b0c0-4e229899ee63 | -14.60375 | -54.09706 | 2026-08-31 05:38:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 91d84fd7-73b8-31e1-bb70-ff091748ea2f | -14.44493 | -52.51899 | 2026-08-31 05:38:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| fe585d50-af9b-32ba-a0bf-2885ad91d73e | -14.23665 | -52.85558 | 2026-08-31 05:38:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 73ff118a-991c-384c-bbd7-21828ed78a16 | -15.24647 | -53.87656 | 2026-08-31 05:38:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1c8c7ea2-c89c-3f66-be0b-f0ef1e83bda4 | -14.16147 | -52.78623 | 2026-08-31 05:38:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5549a1e4-0f23-3f26-80fd-1c8cf41e9517 | -15.24166 | -53.87278 | 2026-08-31 05:38:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c3f4b3a3-3433-305f-961c-039748c1778e | -14.22649 | -52.84774 | 2026-08-31 05:38:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2f2eb039-2853-30f8-a6c3-34ea9c7a936b | -14.17796 | -52.87934 | 2026-08-31 05:38:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 36761d58-4853-380c-b46c-83b6c2e7790b | -14.58789 | -54.10091 | 2026-08-31 05:38:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7cef1d27-ee60-35d8-8fd0-44ee21f98049 | -14.42733 | -52.52373 | 2026-08-31 05:38:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8dddabb5-190b-347d-aff1-0cd160477611 | -15.23973 | -53.87591 | 2026-08-31 05:38:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b464f7b8-be97-371e-a90b-232b72c48c0c | -15.62121 | -56.42113 | 2026-08-31 05:38:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 57c6ba5f-1bf5-3b57-81f3-69b53264363c | -14.44742 | -52.54548 | 2026-08-31 05:38:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a4f2d701-3e17-3cc6-8a61-ea403d0d1cae | -20.25364 | -58.15727 | 2026-08-31 05:38:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.3 |
| 2079d5c4-b835-3ecc-87a4-a7e2623b8da6 | -15.24012 | -53.87272 | 2026-08-31 05:38:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6e207595-5c45-31a8-8c84-44050b517e33 | -15.67916 | -56.27502 | 2026-08-31 05:38:00 | NPP-375D | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 366e93c4-5d61-3fc3-b1b8-340ab71c267e | -14.40442 | -52.52539 | 2026-08-31 05:38:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 5f26324f-332e-317a-b49c-a7e649413ff9 | -20.26125 | -58.1548 | 2026-08-31 05:38:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 17.9 |
| 42c6909c-971b-3f75-ab27-1884c08d4ef9 | -20.24873 | -58.15304 | 2026-08-31 05:38:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 22.1 |
| cc8cffdb-cf11-3d9b-8ea0-9f8286260211 | -14.23197 | -52.84826 | 2026-08-31 05:38:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c00cd73d-0a71-3a94-90f8-afa9777c4416 | -13.46374 | -57.04122 | 2026-08-31 05:38:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1c6d0078-b5a6-3b18-8054-58d4590f3184 | -16.35212 | -51.00618 | 2026-08-31 05:38:00 | NPP-375D | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 07520b91-4d09-3d94-bdac-b983ceb9c856 | -14.17284 | -52.88065 | 2026-08-31 05:38:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 99dc3a92-b823-308d-ab5e-007e245e63d3 | -15.03095 | -48.16932 | 2026-08-31 05:38:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 581720ae-fdc9-30c0-ab36-83fb19b16885 | -14.44754 | -52.52518 | 2026-08-31 05:38:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 13cf186a-59a2-3075-ae1b-2c629bdca914 | -15.24129 | -53.87599 | 2026-08-31 05:38:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 49beaf66-87b5-3e8f-82d1-762eee15eaab | -19.08054 | -57.40262 | 2026-08-31 05:38:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 463c04f0-a436-3088-9a1b-7c0f9ff5e731 | -14.57568 | -54.11727 | 2026-08-31 05:38:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 29cdf1f3-7552-3b47-b4ee-d27fd8d8c886 | -15.24609 | -53.87979 | 2026-08-31 05:38:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6471f645-5297-3132-8e8e-d528d2017a7e | -15.92163 | -56.22657 | 2026-08-31 05:38:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| a1a3475f-074a-3189-ba35-ead49519eab2 | -14.39531 | -52.55463 | 2026-08-31 05:38:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a8e1422e-12b9-3334-9777-552ae4d9d143 | -14.29955 | -52.89609 | 2026-08-31 05:38:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b5db1f67-d90d-36c6-9611-9ac1cc54f82f | -14.44546 | -52.54345 | 2026-08-31 05:38:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5e951383-5415-3b30-ad80-8661412f8b5d | -13.48263 | -57.05511 | 2026-08-31 05:38:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c374b5df-899b-3e08-9358-f839f64204e9 | -14.23118 | -52.85494 | 2026-08-31 05:38:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0ada08f5-bdce-333f-b1f8-96d167680343 | -14.58494 | -54.08271 | 2026-08-31 05:38:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e4d19ff9-e510-3da4-a1ab-81cd20d40095 | -14.40397 | -52.52919 | 2026-08-31 05:38:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 1355786e-2457-39ac-8d0a-02316c98bf7d | -20.25759 | -58.15023 | 2026-08-31 05:38:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 17.9 |
| d5d891a6-363b-360f-a706-2b1695b04648 | -14.44155 | -52.52795 | 2026-08-31 05:38:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e22a2f35-c61a-3436-9fbb-24e5297994d3 | -14.30923 | -52.90808 | 2026-08-31 05:38:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 06f49d4b-9144-3c5d-bed1-6b0d15cc0fa4 | -14.39796 | -52.53203 | 2026-08-31 05:38:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 92a66c51-d29f-35bf-8574-c8e8a31d5675 | -14.15558 | -52.78902 | 2026-08-31 05:38:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bdf7e005-aa35-3cb7-b861-d0b38db7df26 | -14.17324 | -52.8771 | 2026-08-31 05:38:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README70.md)
