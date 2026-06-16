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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fde1e847-9938-310c-8dad-5faa902fdea6 | -13.54694 | -47.86901 | 2026-06-16 04:19:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 76703465-a5b5-3d60-a271-d752fc04f042 | -7.72014 | -44.16213 | 2026-06-16 04:19:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| cff5d43b-b212-3b7b-be61-2e8073502bf6 | -11.54809 | -52.79489 | 2026-06-16 04:19:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b7d061d9-1272-301a-90b9-2b6c5d3adef1 | -15.07214 | -55.81709 | 2026-06-16 04:19:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2530d13e-4675-3507-b611-711d5be75932 | -11.54766 | -48.26778 | 2026-06-16 04:19:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f3ac2ee8-16bd-3455-90b1-725caa2b218b | -13.21061 | -45.48806 | 2026-06-16 04:19:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a3987170-42c1-32a4-a075-21af1fb2d8a4 | -12.13521 | -48.26289 | 2026-06-16 04:19:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 2481e232-cb25-36f0-ac0d-424d57607fc5 | -11.53918 | -52.78167 | 2026-06-16 04:19:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| e3f12a68-d414-3eff-b2a1-dca844499e15 | -11.35029 | -51.40747 | 2026-06-16 04:19:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 87ddcc0e-447f-3242-9ca7-826d6ed01691 | -13.81458 | -43.64754 | 2026-06-16 04:19:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c752b9f9-1e0e-391d-bd83-c41469c51aae | -6.15699 | -48.48356 | 2026-06-16 04:19:00 | NPP-375D | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 32b64162-3225-325c-aa9d-137c2ad40eff | -17.80813 | -46.70183 | 2026-06-16 04:19:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a117a8a7-1fe3-30e9-9201-154daa451bc9 | -17.80465 | -46.70119 | 2026-06-16 04:19:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6243567b-c733-3508-974b-5cf9fe533a86 | -11.91317 | -57.04557 | 2026-06-16 04:19:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cb08d355-583f-3ee2-94a1-f60db6e0934f | -10.80315 | -54.18011 | 2026-06-16 04:19:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c222866d-0565-3a35-930a-2cf28099f7e8 | -6.30548 | -43.64031 | 2026-06-16 04:19:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4348b733-1960-31d6-959a-e48e54b88fbe | -6.97783 | -42.87629 | 2026-06-16 04:19:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| dfb99ef1-d5f6-3991-9b43-1a16bb0db995 | -11.47591 | -57.12606 | 2026-06-16 04:19:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 86a50dca-d34c-391b-83a3-0cf5747bfb97 | -17.94008 | -42.84369 | 2026-06-16 04:19:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| e14a0d48-8019-3bb9-b9d9-e1500e18b622 | -17.80398 | -46.70516 | 2026-06-16 04:19:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1424b482-7f49-3654-8d55-502c2138718e | -6.18148 | -48.50468 | 2026-06-16 04:19:00 | NPP-375D | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5370debb-a5d8-3c14-bf0e-8bf3da58bead | -13.56197 | -47.85178 | 2026-06-16 04:19:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9971e482-4f35-38fb-bcab-f4f1f98e3a76 | -6.3943 | -44.17413 | 2026-06-16 04:19:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| dbba5ae8-0f41-30f1-b74d-4989350ee4cc | -6.11453 | -48.48339 | 2026-06-16 04:19:00 | NPP-375D | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3f247e5c-6ac9-3df0-a94f-9f1d69390a9c | -11.26924 | -53.96453 | 2026-06-16 04:19:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dd760bbf-534f-32a8-8762-679e8d88bd39 | -11.71898 | -54.49308 | 2026-06-16 04:19:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7f3a3983-b123-3e6f-ad2b-7b55baa4e48d | -12.14509 | -48.46762 | 2026-06-16 04:19:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 493a8d9e-8798-327b-ba01-142385ad5573 | -12.7994 | -54.86347 | 2026-06-16 04:19:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a05fbfe4-bef2-35bc-801e-d7d857246d3c | -12.91968 | -54.22536 | 2026-06-16 04:19:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 76f7d051-74bc-3d95-9d00-fe3613411472 | -10.15264 | -56.60043 | 2026-06-16 04:19:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 3e24455e-6deb-35fe-9015-e6b72d5791c6 | -11.55648 | -52.78119 | 2026-06-16 04:19:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 09ee5469-c74e-3058-ba5c-4976c3c4675b | -6.13932 | -48.53111 | 2026-06-16 04:19:00 | NPP-375D | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0ac63139-a42a-3767-b377-4c1b203653da | -6.1352 | -48.52804 | 2026-06-16 04:19:00 | NPP-375D | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5467fb96-160b-3bb9-beb0-5851112adb65 | -6.14011 | -48.5266 | 2026-06-16 04:19:00 | NPP-375D | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f9e458dc-3f21-3fa9-a423-f59c05d8c340 | -6.97947 | -42.88745 | 2026-06-16 04:19:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 15.6 |
| f6245c13-2841-3eec-9616-adae36747860 | -11.26303 | -53.95703 | 2026-06-16 04:19:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fa358f98-4e42-33ed-899b-fd68140bb8f8 | -6.98118 | -42.87683 | 2026-06-16 04:19:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| d1a7337f-fef0-32bd-a323-b7c58e24db58 | -11.47751 | -57.11861 | 2026-06-16 04:19:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 65a04ed0-664e-3e3b-a115-d7eea55086cd | -11.78685 | -57.00064 | 2026-06-16 04:19:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 37367001-b7e4-3553-9f48-1fecfe035a56 | -14.15413 | -41.96019 | 2026-06-16 04:19:00 | NPP-375D | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| eba4e3ab-7630-3684-a899-670a739a3f6d | -13.95116 | -41.31567 | 2026-06-16 04:19:00 | NPP-375D | ITUAÇU | BAHIA | Brasil | 2917201 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 91ab37ba-0265-31a8-aee4-2e88b41aa799 | -5.80442 | -45.07113 | 2026-06-16 04:19:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 54286851-7b7e-3d12-9090-9cb4f488d003 | -5.79932 | -45.07916 | 2026-06-16 04:19:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ec6d87ae-321f-38c0-b71f-a0b5e0eddc94 | -13.54096 | -47.85754 | 2026-06-16 04:19:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4ed17e30-c044-3865-89ea-86231dd1bc8a | -7.7208 | -44.16932 | 2026-06-16 04:19:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b3da72fb-7c6b-3114-9f1b-f54a9d64d2cd | -13.54394 | -47.86329 | 2026-06-16 04:19:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b5dc01fe-859d-31de-a05f-18467ceddea5 | -6.83254 | -47.90462 | 2026-06-16 04:19:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 25c720cf-8496-3779-8134-8cc4fbd0ef9b | -17.6034 | -46.67664 | 2026-06-16 04:19:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5b01a69e-a45d-3369-8c90-ea08b0f905d8 | -5.80371 | -45.07547 | 2026-06-16 04:19:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 82d50164-18fc-36d1-a5cd-b73335f9fe11 | -14.85287 | -43.37217 | 2026-06-16 04:19:00 | NPP-375D | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 35498640-dd44-33a8-aeac-5b6306372d1d | -12.85253 | -44.37062 | 2026-06-16 04:19:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 563b019e-059f-3e4a-998b-4c211c150298 | -11.79032 | -57.00144 | 2026-06-16 04:19:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 074349f2-e6af-380b-8ab3-8b6ff0201415 | -12.59687 | -52.91493 | 2026-06-16 04:19:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f4987f62-6368-3758-bcdd-da7098451098 | -7.72206 | -44.16172 | 2026-06-16 04:19:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 12bbe739-cda3-3156-b436-da1859eb39e3 | -6.30769 | -43.64836 | 2026-06-16 04:19:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| a82beca8-2848-3fb1-8f4d-7ea95f8d666a | -11.78883 | -57.00854 | 2026-06-16 04:19:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 536db695-826f-3f6a-8cd8-d423d8bf1f9d | -6.39843 | -44.17081 | 2026-06-16 04:19:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 299c2fac-961e-3eaa-be9b-9bcf00e8f93e | -13.54782 | -47.86401 | 2026-06-16 04:19:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 792498f6-6a12-37fe-b791-c1a4f6f53563 | -7.34698 | -46.21108 | 2026-06-16 04:19:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 96b70d5e-d94e-3f56-9b07-d4988789af65 | -13.56412 | -47.86234 | 2026-06-16 04:19:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 16a44209-29bb-3808-b312-138471cd2430 | -13.54183 | -47.85258 | 2026-06-16 04:19:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f18b9687-c42c-37e5-9967-1f22a0bc2a95 | -14.71707 | -42.94531 | 2026-06-16 04:19:00 | NPP-375D | ESPINOSA | MINAS GERAIS | Brasil | 3124302 | 31 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 941eb99f-194e-3f33-8851-07b89aed7663 | -11.58587 | -55.34013 | 2026-06-16 04:19:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4e4d65b7-da41-392c-a6d2-353d91934268 | -11.48313 | -57.11896 | 2026-06-16 04:19:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ab45780f-86a2-363f-91c6-7f57567862dc | -12.80126 | -54.86253 | 2026-06-16 04:19:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ab750fa5-e083-3395-8e22-a1bd0f943ad8 | -12.13115 | -48.26213 | 2026-06-16 04:19:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 68407ceb-de18-33b8-a3da-7614020f7b8d | -12.9096 | -54.23039 | 2026-06-16 04:19:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5ddd2227-edc1-3812-9c07-0bfccabbe62c | -5.98048 | -47.07183 | 2026-06-16 04:19:00 | NPP-375D | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c963d5f8-0e27-30a8-8f81-3be0abcbd0f9 | -11.48158 | -57.12646 | 2026-06-16 04:19:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 16c556a0-debf-32df-b525-c99858613abe | -12.15121 | -48.45712 | 2026-06-16 04:19:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dc005e8b-5533-3a64-8158-633021cc1335 | -13.55117 | -47.84499 | 2026-06-16 04:19:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 38266d88-c56a-3a12-960a-13b613bfccf6 | -6.97611 | -42.88691 | 2026-06-16 04:19:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 15.6 |
| 5f2d4465-57b3-3682-a467-5a5ab42cfbba | -15.06574 | -55.81644 | 2026-06-16 04:19:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bed4c91f-489f-3012-8374-92327fb6049c | -13.81402 | -43.6511 | 2026-06-16 04:19:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d93c7d77-613e-3522-bf34-be7567000cc3 | -6.13556 | -48.5257 | 2026-06-16 04:19:00 | NPP-375D | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 67949c96-dde2-3562-80f9-5353f11af203 | -5.80003 | -45.07481 | 2026-06-16 04:19:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 50541e59-30b9-39f1-833c-a62e209f1a79 | -5.80228 | -45.08418 | 2026-06-16 04:19:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9bdff085-d5b6-33fd-84cb-8dd88ff63e48 | -11.91469 | -57.0385 | 2026-06-16 04:19:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 834dd7ee-ac8d-3796-aa88-4dbc614299be | -12.14988 | -48.46463 | 2026-06-16 04:19:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f1db787d-d241-3427-a23c-34452613d6a9 | -12.92904 | -54.22537 | 2026-06-16 04:19:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4e6486b2-0cbd-31b9-84be-60899d5ee4ed | -12.80553 | -54.86479 | 2026-06-16 04:19:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 723177e4-6b43-3a43-9484-0a424f1f496a | -6.46315 | -46.89806 | 2026-06-16 04:19:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| edb3a647-8703-3fb6-87ad-5635882a8722 | -12.79838 | -54.86834 | 2026-06-16 04:19:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 66c6463c-14eb-38d7-b4b3-f06efd9660b1 | -12.84917 | -44.37005 | 2026-06-16 04:19:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 9.4 |
| ae4d020c-396a-39dc-8060-907c3bf63457 | -11.48464 | -57.11173 | 2026-06-16 04:19:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 99733be7-45f7-38ca-9b8c-7cf4f25d0a1d | -12.84858 | -44.37369 | 2026-06-16 04:19:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 38.7 |
| 2ad0442e-e5c1-3724-a707-098f96000556 | -7.72299 | -44.1665 | 2026-06-16 04:19:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2f403d56-7abd-3f41-9a15-a3406dab5a8c | -11.20796 | -49.68152 | 2026-06-16 04:19:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0117d5e6-8ff8-39e6-a7c4-178a65cf0acf | -12.85194 | -44.37426 | 2026-06-16 04:19:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 38.7 |
| 67d1bc4f-193f-352f-83ae-61c9f1f3e333 | -6.53855 | -44.68676 | 2026-06-16 04:19:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 75ed4f3d-8cec-3ad4-8e8c-5d00b6a0af95 | -11.91584 | -55.92086 | 2026-06-16 04:19:00 | NPP-375D | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ed1900ab-5ed8-3412-90c6-40af8aad1af7 | -13.55642 | -47.86061 | 2026-06-16 04:19:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 23cac9bb-c065-3f16-a329-67f180f30e87 | -12.91048 | -54.22599 | 2026-06-16 04:19:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0663a81f-977b-3c2b-841a-40670cfebacb | -11.55025 | -52.78375 | 2026-06-16 04:19:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 27fe4faf-1c1b-304e-a01a-3a2013a95a3f | -12.92647 | -54.22226 | 2026-06-16 04:19:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 504f33b3-4b79-302e-a07d-e35363cf7a8f | -11.476 | -57.11741 | 2026-06-16 04:19:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| a25e325b-5fe4-3202-b8c4-bf536577318d | -13.55555 | -47.86558 | 2026-06-16 04:19:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7279946c-b002-30ed-b2ce-b026bfece1d9 | -6.30204 | -43.63974 | 2026-06-16 04:19:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a80d8448-15fa-3f53-a56f-adf4fb1293cc | -6.39016 | -44.17746 | 2026-06-16 04:19:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 492e9779-46d0-33c1-8605-606dba37dd74 | -6.39367 | -44.17802 | 2026-06-16 04:19:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |


[Clique aqui para ver as próximas entradas](README8.md)
