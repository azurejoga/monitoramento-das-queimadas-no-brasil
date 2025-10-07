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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1b625101-da93-3cd5-ac8a-7db65233419f | -15.17259 | -52.76792 | 2025-10-07 04:10:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7e595839-243b-38c7-88f5-9b19f5d8c4dd | -18.16202 | -53.36846 | 2025-10-07 04:10:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| edd8901f-3948-3f72-8d05-7f80d031a618 | -15.26887 | -48.06656 | 2025-10-07 04:10:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7f990465-d6e8-3d59-af74-5555622950e5 | -19.79477 | -45.84624 | 2025-10-07 04:10:00 | NOAA-21 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1ea1c189-628e-3cca-9908-756f8e11a513 | -18.16354 | -53.36116 | 2025-10-07 04:10:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5d8e43b7-2347-3732-80cf-02b6c9ac2f8e | -15.59329 | -47.26742 | 2025-10-07 04:10:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 574c3f19-d51a-37c0-8125-2247e378f8ec | -15.37517 | -47.3098 | 2025-10-07 04:10:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2af407b8-041f-3733-a2a4-89089e25eb87 | -18.11367 | -53.3576 | 2025-10-07 04:10:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cb3e3251-9e0d-3f0b-97d1-288034a5c545 | -16.54797 | -42.72572 | 2025-10-07 04:10:00 | NOAA-21 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 95ec34c8-9454-3380-a3b0-833b9d7b9cc0 | -11.74264 | -54.71827 | 2025-10-07 04:10:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 1bb3afb5-be3b-3e74-9e6e-35ea96829716 | -13.99206 | -53.91138 | 2025-10-07 04:10:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b2c9c047-6a31-30e9-b8d3-459bb2bfcf92 | -12.25319 | -47.85214 | 2025-10-07 04:10:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ef77b9c8-bd39-3869-94ca-9db56570a5f0 | -15.59204 | -52.55371 | 2025-10-07 04:10:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ee3347ff-f563-3d4b-898a-cd5949681217 | -20.20801 | -43.91206 | 2025-10-07 04:10:00 | NOAA-21 | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 796e5024-067f-30a9-8732-9dcea776a256 | -14.28818 | -45.8368 | 2025-10-07 04:10:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 485201ae-7cb3-34c2-9d63-c4cc473b0301 | -14.90676 | -46.84383 | 2025-10-07 04:10:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f9402625-e78d-3c64-85ef-941744212abd | -15.60918 | -52.57379 | 2025-10-07 04:10:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 93249913-8d33-3ebf-9607-63ff809d73f5 | -15.26675 | -48.05614 | 2025-10-07 04:10:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 60fa911d-4e2c-3ac6-b521-d29f34c56a11 | -13.08035 | -47.83132 | 2025-10-07 04:10:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| aac2060c-d33a-3062-bac7-dc1d3b1c3a55 | -14.75971 | -46.04305 | 2025-10-07 04:10:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 08adf27b-4a34-37ea-a24f-a84e344827d4 | -13.67669 | -47.95362 | 2025-10-07 04:10:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e0ca59ed-9cad-3f70-b45b-e76c6598fdef | -13.2642 | -48.46426 | 2025-10-07 04:10:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3cf1c78a-9a8e-3099-aea6-f155e4e9db8a | -18.57268 | -49.25467 | 2025-10-07 04:10:00 | NOAA-21 | CENTRALINA | MINAS GERAIS | Brasil | 3115805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 805fdeaa-6d26-3b4d-8e0c-222916ae035b | -13.29947 | -48.05447 | 2025-10-07 04:10:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2ae739d7-3518-3417-be46-df9523fc13fe | -12.94494 | -46.78719 | 2025-10-07 04:10:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7c37f352-9a7c-338f-bd3b-7da2bd24537f | -12.06222 | -51.21 | 2025-10-07 04:10:00 | NOAA-21 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 61c00b2c-12ba-334f-858f-362d3a4d1214 | -14.53547 | -46.63747 | 2025-10-07 04:10:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 75e03bd3-7900-303f-8c8b-bfcc318a2847 | -13.04535 | -49.15674 | 2025-10-07 04:10:00 | NOAA-21 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0407395f-6f83-337b-9e11-c795f5e2be82 | -15.98672 | -50.93853 | 2025-10-07 04:10:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 445333dd-e690-3ceb-8af3-3d365801532c | -16.02 | -51.03868 | 2025-10-07 04:10:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 24573f6f-f08d-3f16-b87a-b6dca7061708 | -13.97094 | -53.89133 | 2025-10-07 04:10:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 19334d5e-075a-350a-9de8-2f9efe237e18 | -16.3831 | -48.99383 | 2025-10-07 04:10:00 | NOAA-21 | ANÁPOLIS | GOIÁS | Brasil | 5201108 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a1dff6a6-8358-334f-b66d-0a9bfe52afa3 | -17.9628 | -44.40217 | 2025-10-07 04:10:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c826aa7e-8779-38d6-8851-aea34cce106e | -13.07417 | -47.88913 | 2025-10-07 04:10:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b84b3438-8d41-311d-8a56-b4396ed144c8 | -13.30831 | -48.05063 | 2025-10-07 04:10:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 78182eab-c2cf-395b-af51-53bc83eb00cd | -19.9312 | -46.72149 | 2025-10-07 04:10:00 | NOAA-21 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b1679ce9-cd5c-339f-92fe-3e42dc4bb9b8 | -16.00336 | -50.95035 | 2025-10-07 04:10:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cfdc8c2a-f758-3cfd-b59b-82b4fb55e89a | -13.39449 | -47.58286 | 2025-10-07 04:10:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b8736519-578b-30ff-a428-5a06d49324e3 | -18.60185 | -46.80116 | 2025-10-07 04:10:00 | NOAA-21 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ef1f0d74-b743-38d5-8287-83173dac00a6 | -14.64912 | -48.36872 | 2025-10-07 04:10:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 39623656-ea0f-3d99-b150-62ab26a0ad46 | -15.65447 | -43.6752 | 2025-10-07 04:10:00 | NOAA-21 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 468627ed-8188-31d4-9880-3534d4127c9f | -13.34335 | -47.56794 | 2025-10-07 04:10:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5f1ee399-2fe9-3919-93bf-9ed788c84d83 | -13.23198 | -48.457 | 2025-10-07 04:10:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 68120951-7883-35a5-802d-7fb97eeefcbc | -12.66297 | -45.02801 | 2025-10-07 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 32ab0bf0-378c-3939-b21f-210ded3f8431 | -14.93312 | -46.79881 | 2025-10-07 04:10:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 1b6f849b-390b-3551-97bb-2dee87457b49 | -13.09595 | -47.85768 | 2025-10-07 04:10:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| c1cc7501-6d30-36f9-960c-4bb321df5788 | -14.93245 | -51.40894 | 2025-10-07 04:10:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 462220ec-de2a-3549-9498-efd435a2de14 | -13.08204 | -47.845 | 2025-10-07 04:10:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a428901f-06fb-3a15-a8da-e72ab36fa23c | -18.28859 | -45.41169 | 2025-10-07 04:10:00 | NOAA-21 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 236e9937-e8d5-3e98-9737-019c463baf29 | -14.72082 | -48.3545 | 2025-10-07 04:10:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 32f1ca79-128d-37cf-bfb8-77bab829f30e | -12.41378 | -50.26712 | 2025-10-07 04:10:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1bd993f5-ce64-3349-959b-ce19552e9ed0 | -12.40301 | -51.13227 | 2025-10-07 04:10:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8f39d6ea-26f3-3bf5-ac24-e0dceb0c373e | -19.79144 | -45.84562 | 2025-10-07 04:10:00 | NOAA-21 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 9613dd3c-31d7-389f-b964-eb3409c5ded6 | -13.07001 | -47.89142 | 2025-10-07 04:10:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 733cb5e5-5e0c-3c81-8c57-7978555dd054 | -16.30751 | -42.05523 | 2025-10-07 04:10:00 | NOAA-21 | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| f87d5ea3-eaf1-31a5-8e5d-1b9b7f0a4ca8 | -13.50439 | -43.6702 | 2025-10-07 04:10:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 56.0 |
| c4384d89-5bb0-304b-b643-85f09f8bb540 | -19.74501 | -45.85639 | 2025-10-07 04:10:00 | NOAA-21 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 02a65058-5b77-352b-82bf-13859fd65656 | -12.97677 | -46.77898 | 2025-10-07 04:10:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 28ac1ffd-1306-3e2f-8ad5-f3a269a31c0b | -13.26082 | -47.18589 | 2025-10-07 04:10:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c3f8b7ec-83c0-3267-889a-2b47c87484ac | -15.44414 | -49.09937 | 2025-10-07 04:10:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e15879a6-c246-3f2e-8ead-e3ab9c4ea7f6 | -14.9238 | -51.40367 | 2025-10-07 04:10:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 25660bf3-5ce2-348d-ac77-6f9936b3e0bb | -15.586 | -47.26605 | 2025-10-07 04:10:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2c8bb984-2458-3ebf-8df7-90c4b9066a9a | -14.91549 | -51.44465 | 2025-10-07 04:10:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f462df4d-ebbf-37ba-b218-59839765fa24 | -13.2208 | -47.81391 | 2025-10-07 04:10:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 9d6e73e2-150d-3a21-a11a-601d71a93fab | -15.14698 | -45.80976 | 2025-10-07 04:10:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f16bf1a2-635f-3fac-8a30-477113803ae3 | -20.11835 | -44.40959 | 2025-10-07 04:10:00 | NOAA-21 | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 282a1372-a919-3b86-a810-00c75d18960f | -16.29605 | -45.24009 | 2025-10-07 04:10:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b293d3ee-d92b-3719-a3a1-ec7f3d7d170d | -15.58761 | -52.54947 | 2025-10-07 04:10:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 61819718-2b06-3fb7-9124-652609000cdb | -19.51333 | -43.8333 | 2025-10-07 04:10:00 | NOAA-21 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| baab3e7c-e698-3364-98ae-a8711890fcf7 | -13.21822 | -46.53367 | 2025-10-07 04:10:00 | NOAA-21 | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 66886a45-ba41-375c-a077-d5782fbd6398 | -14.93031 | -51.42171 | 2025-10-07 04:10:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 8.6 |
| fffaa55a-3cea-3dca-9673-0b16a62ed381 | -13.10187 | -47.98478 | 2025-10-07 04:10:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 1f621280-29f2-3511-a249-37382b615322 | -14.99101 | -49.96715 | 2025-10-07 04:10:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 014547e1-82f7-379d-885a-b01346a4b19b | -14.28751 | -47.42051 | 2025-10-07 04:10:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 67516020-aa58-3e1c-a801-f3b95c55b2f5 | -14.24697 | -54.25071 | 2025-10-07 04:10:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| af68cd0b-db86-3885-96bf-34352bdf9789 | -19.13179 | -46.43066 | 2025-10-07 04:10:00 | NOAA-21 | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c2b9c17d-e9be-32d6-a67f-ff0175595b81 | -14.93966 | -46.80395 | 2025-10-07 04:10:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 075bf6af-f0d0-3ee6-a74a-917b73cfe69a | -16.29212 | -50.97844 | 2025-10-07 04:10:00 | NOAA-21 | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 92314a0c-c727-3613-9117-01458d17fa49 | -15.79378 | -43.65424 | 2025-10-07 04:10:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 52279675-b529-3a0d-a17e-afd54087649a | -14.69581 | -48.40409 | 2025-10-07 04:10:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 82aa32a3-66af-314f-8475-3902085eb04d | -20.11448 | -44.41265 | 2025-10-07 04:10:00 | NOAA-21 | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.8 |
| 6a587226-9b62-3d1f-9849-666fccade3d2 | -14.93234 | -51.41096 | 2025-10-07 04:10:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 07fb371b-014d-39b5-98c3-a068d0aa4a01 | -15.36623 | -47.31758 | 2025-10-07 04:10:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 244f4ee9-669b-354c-8459-2cee19fc5456 | -14.28752 | -45.8408 | 2025-10-07 04:10:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 44a0d84f-9df3-355c-894f-71fb3fcf1fe5 | -20.12165 | -44.41018 | 2025-10-07 04:10:00 | NOAA-21 | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| a899703c-1aa6-3da9-a175-ba73f3296315 | -14.70455 | -46.00863 | 2025-10-07 04:10:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cc40a98b-2e8b-3fc5-85c0-4f8de408e55b | -13.78861 | -50.78899 | 2025-10-07 04:10:00 | NOAA-21 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2aead189-0362-30f7-9c1c-23d4b5dfa560 | -19.02668 | -44.73349 | 2025-10-07 04:10:00 | NOAA-21 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a0767c0d-12b6-3368-8f38-b30c0cfab018 | -15.51656 | -46.83673 | 2025-10-07 04:10:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c6e90dfc-2e65-354b-a38a-747d72f79995 | -17.34938 | -46.83508 | 2025-10-07 04:10:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c74a3985-5379-3d9a-a95f-26b9c8ef8666 | -20.2692 | -45.3555 | 2025-10-07 04:10:00 | NOAA-21 | SANTO ANTÔNIO DO MONTE | MINAS GERAIS | Brasil | 3160405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 121096b7-a635-3fa6-bacf-07bb23dd7aa0 | -19.04736 | -48.13647 | 2025-10-07 04:10:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7dcf133d-f0a2-3bfa-ada3-34e12483bcb7 | -12.98337 | -46.78481 | 2025-10-07 04:10:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| c8fa6143-4f80-37a8-b17a-3953e920293f | -20.12439 | -44.41442 | 2025-10-07 04:10:00 | NOAA-21 | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| bb906287-a785-3397-b5c3-7bc480cc8014 | -15.58108 | -52.5677 | 2025-10-07 04:10:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a6458179-3343-391b-846e-4e9c9bf43f19 | -17.61442 | -46.68586 | 2025-10-07 04:10:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f470ebd9-d1d4-3e5b-8e65-686df38463b8 | -12.98154 | -51.02929 | 2025-10-07 04:10:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 67337a1b-5e65-348b-8380-c9b6102038cd | -14.90902 | -46.8308 | 2025-10-07 04:10:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 91fa669a-dc2b-367d-ab8b-621f4f7f1625 | -12.18159 | -47.77831 | 2025-10-07 04:10:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b760ae77-708e-3f52-8791-dbf885b3f4c6 | -14.94795 | -51.45675 | 2025-10-07 04:10:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README38.md)
