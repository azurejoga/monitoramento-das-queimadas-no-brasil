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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a6d5030f-f0c5-34ee-ac4e-b68b7bf5ef92 | -11.18272 | -54.91315 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 9a9bbac9-0d2f-3ea7-b4e5-2b50db8a4a5a | -11.17633 | -54.90792 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4aa12fe8-7ffb-3867-becc-c22023240fe9 | -11.19795 | -54.88674 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fad7dafe-9a81-3b6d-b44f-5f9c6081d978 | -15.70078 | -56.13164 | 2026-08-05 04:49:00 | NOAA-21 | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9b2c15a3-70d9-3a45-b28b-f2eab610a43b | -11.21577 | -54.91049 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 7cb04327-c9b1-3e0b-abec-bfd7fb90f070 | -12.60174 | -46.9225 | 2026-08-05 04:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| caa9b59f-81f5-3995-9233-a7a1661805a3 | -11.20586 | -54.8387 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b886891c-b08d-3d72-bb01-6b11519cefc1 | -11.91684 | -55.91526 | 2026-08-05 04:49:00 | NOAA-21 | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a25be20b-f764-3c30-93b2-5bf51ad182bf | -13.43653 | -43.8591 | 2026-08-05 04:49:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6c2cc686-ca50-38f7-b46d-f453ab5bb155 | -11.92564 | -55.9078 | 2026-08-05 04:49:00 | NOAA-21 | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 59a8ee26-7aa3-30f5-bb00-f2b39698a5db | -12.1402 | -48.26224 | 2026-08-05 04:49:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c83f09f6-adb1-3815-9bbc-71e54f5d648c | -11.17919 | -54.91256 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| a1cfdf16-0274-3b86-a4ff-7ae169733581 | -12.89636 | -52.83651 | 2026-08-05 04:49:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0e406232-301d-34f3-a9e8-729ddc9a35cf | -12.00535 | -49.26845 | 2026-08-05 04:49:00 | NOAA-21 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 4ed382af-4ddd-3f2d-9231-0471a17dcf18 | -17.94782 | -43.88833 | 2026-08-05 04:49:00 | NOAA-21 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| d9a0c9f9-0815-3abc-a48b-b362a1add2aa | -14.16632 | -54.40202 | 2026-08-05 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8ad19dbd-cf6a-3add-a9dc-de339e9cf860 | -12.00382 | -49.26717 | 2026-08-05 04:49:00 | NOAA-21 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 68b2dcdc-fc19-337a-9b4a-9c10fa55f144 | -11.17784 | -54.92067 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| a4c55179-61b1-327a-ac80-750c0d34cabf | -11.16187 | -54.86415 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b8bcf250-8628-302e-adc3-c04f5f49654a | -11.33907 | -62.21331 | 2026-08-05 04:49:00 | NOAA-21 | ALVORADA D'OESTE | RONDÔNIA | Brasil | 1100346 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| de8a172a-963d-3a13-8c56-9ecab99f32f1 | -12.85693 | -52.82652 | 2026-08-05 04:49:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a766dd60-8b50-352d-97b1-11e60246a119 | -11.17331 | -54.88247 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7ed391c3-dc52-3cfb-b4eb-3c485bd3bedb | -12.58619 | -46.94386 | 2026-08-05 04:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 29b37b3a-d0c0-32b2-b952-38068022f05a | -12.86079 | -52.82353 | 2026-08-05 04:49:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4911086e-8102-37ca-938d-2d8a22d4715d | -11.20168 | -54.90807 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5a3800a6-e2a3-37a7-b4a0-800f9fb357c8 | -11.16927 | -54.90675 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 23ede4c5-baa3-360e-b4e2-8202ec98026e | -11.19972 | -54.85405 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d011ef4b-b881-39b6-adbb-b547e5dfcc77 | -14.16295 | -54.40142 | 2026-08-05 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5f35e210-3e21-3622-a4ef-b3ae466f6172 | -12.59506 | -44.15882 | 2026-08-05 04:49:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0a8e3a83-62a6-35cf-a906-79284f996c9a | -11.33836 | -62.21708 | 2026-08-05 04:49:00 | NOAA-21 | ALVORADA D'OESTE | RONDÔNIA | Brasil | 1100346 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 7f687434-c00f-3b9e-af95-3cbae5dc2f57 | -12.85086 | -52.82192 | 2026-08-05 04:49:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3203e770-5074-3876-ab4f-79180c76a5f0 | -14.18198 | -54.41233 | 2026-08-05 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 72c5728f-328e-3c44-8805-bc463ce66787 | -11.22369 | -54.86216 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a6245202-10ba-3bf0-9fd4-14c6a970020c | -11.17683 | -54.88307 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 12ea3aea-899c-38c2-8bd3-8b5e5a849e9a | -11.25147 | -54.82911 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| df65c80b-2115-3c9f-9914-5294ba3bf62a | -11.19682 | -54.91558 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ab1da9e1-108a-3133-94e1-64f04e66bfa2 | -14.23292 | -48.51562 | 2026-08-05 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 37744a52-060f-3d34-9ec1-7bd0a55d0880 | -14.26828 | -45.29536 | 2026-08-05 04:49:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1663200b-3a17-37a8-8c08-bb282b5b4f7e | -11.18253 | -54.89236 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7ba6aa27-d26e-346c-830b-79b8821cccc5 | -11.91464 | -55.90581 | 2026-08-05 04:49:00 | NOAA-21 | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 243c7b33-b5ec-346b-a7bd-0afeae141c87 | -12.49321 | -45.54175 | 2026-08-05 04:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 04d0f8cb-a8fa-3c46-972c-73325bed3d8c | -12.144 | -48.26278 | 2026-08-05 04:49:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a6054df0-16c1-3392-b2b6-59dd1ec7f86f | -15.43917 | -41.38342 | 2026-08-05 04:49:00 | NOAA-21 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| a29f7dcd-4486-3b80-a6e0-7442c973846f | -11.16121 | -54.86814 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b37dc28c-1a2f-3176-b84f-384ccef108c6 | -14.16909 | -54.40628 | 2026-08-05 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ea0ee3b9-1764-32d6-9ecd-879cc75345bd | -11.19529 | -54.90286 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| dd7f3494-e8c2-3a18-bc91-200d39983d16 | -12.60016 | -46.93429 | 2026-08-05 04:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 035e45af-94a3-3b75-be63-0ba110d473eb | -11.17767 | -54.89985 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e05cb82f-7110-3c14-9f6c-c2f433ce6612 | -11.20652 | -54.83471 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 59178432-13cd-38ca-893a-5eb61f077f89 | -14.02885 | -54.07761 | 2026-08-05 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 50a229d0-d3da-3584-8ae8-c3d56cfec064 | -11.1728 | -54.90734 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 10e11c10-5212-32d1-b0bc-0fcd129cda32 | -11.18691 | -54.9097 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| bd1d48d3-40f2-3fb3-b0d8-40f3ef186bb7 | -12.59657 | -46.92953 | 2026-08-05 04:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3ec7bdfc-fef7-3ee9-ac59-73a469195f37 | -12.14263 | -48.26994 | 2026-08-05 04:49:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8fe34b34-631f-361b-8548-4d02ae73e153 | -11.19091 | -54.88552 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 25121e37-1032-316e-853e-80a33a8636dc | -12.86023 | -52.82706 | 2026-08-05 04:49:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8d686ac4-43fe-34bc-9577-d53a7de64b7f | -11.20719 | -54.89658 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5794c6a9-1fb5-3580-bc22-0c872afc20bd | -11.20192 | -54.86261 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 77079ce3-a92d-3454-83e5-28d0ee314b57 | -12.31856 | -53.17711 | 2026-08-05 04:49:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| ba6595bf-9f04-3dc0-ac37-af75303a1670 | -11.20389 | -54.85063 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| decd6266-3e3e-31e0-ad5b-f3e933a661fc | -14.19245 | -54.43324 | 2026-08-05 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 20.4 |
| cc097f4e-b2ad-331f-8bfa-ec3dcb49d768 | -11.25599 | -54.86687 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 83738082-fb04-3d41-8154-57af0c1729bf | -17.9931 | -47.14893 | 2026-08-05 04:49:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3051010e-743c-35f9-96cf-920d3ad99cf4 | -17.33198 | -42.63556 | 2026-08-05 04:49:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 4ae8dbe5-3539-37cd-9c0c-f2d16e8a5e45 | -11.17264 | -54.88649 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bdafbae6-6bf9-3c22-8353-6045cf72a650 | -14.13856 | -55.24744 | 2026-08-05 04:49:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 46f575e6-53d4-3083-bff2-8c6fe0be49c1 | -12.43575 | -50.51773 | 2026-08-05 04:49:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 275f1f1e-7b90-3bdb-b162-30f3c4e3e76c | -12.45324 | -50.37664 | 2026-08-05 04:49:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 60f337e4-7936-3d31-bf0c-ea986bc7ea48 | -12.58105 | -46.95072 | 2026-08-05 04:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a0f34362-b6ad-3a03-8f67-362bbe1ce37a | -11.19662 | -54.89479 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4765455b-183e-3e57-a068-b86bdc301042 | -16.43388 | -51.77976 | 2026-08-05 04:49:00 | NOAA-21 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0c8925ae-b3a5-3a80-8785-a3bd041a6042 | -11.18758 | -54.90566 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e9091e20-6b21-3293-93c0-d06c4ca545b7 | -13.24594 | -54.26742 | 2026-08-05 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 7ade767f-b677-3c04-9c32-44faa4c5c321 | -11.18784 | -54.86029 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 00484ba1-5661-3981-90a5-76200e6d73c1 | -11.21092 | -54.91797 | 2026-08-05 04:49:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fe7b2409-137b-332f-a31a-a38a8c7f8926 | -12.87678 | -52.82975 | 2026-08-05 04:49:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 79a25063-9e28-3d79-bef2-bdb297da9c63 | -12.31902 | -48.56048 | 2026-08-05 04:49:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1049ed0d-b5ca-3896-8a74-f86ba6f45beb | -11.20037 | -54.85006 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cd79c2f3-8354-3a2c-af20-50ac9398499a | -14.26765 | -45.30058 | 2026-08-05 04:49:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5fc49059-eb5e-3737-ae49-c5d012625bfb | -15.4409 | -41.37925 | 2026-08-05 04:49:00 | NOAA-21 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| a1928374-5365-3ff2-810c-5c87d9b93847 | -11.18539 | -54.897 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f63f97c1-c5c1-3bce-867d-ab6d5480c19c | -12.32965 | -48.53876 | 2026-08-05 04:49:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bec9ae3e-c44e-3f55-a249-d71a9f931afb | -12.58984 | -46.94818 | 2026-08-05 04:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| f5991ded-984d-3d3f-89c8-f39a240c42e9 | -14.1986 | -54.4381 | 2026-08-05 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 86463002-f619-38cf-b8c8-334e42f754fa | -11.183 | -54.86765 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0957b216-211b-34ed-bbcb-be128d90e34f | -11.21003 | -54.83528 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 84064aad-59b4-377b-8180-2a0594e7a619 | -11.18387 | -54.88429 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 28c29ed3-3984-34f7-8f9b-e8205b13b888 | -11.19309 | -54.89419 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0a9e932d-763a-3fba-97df-564b658b5429 | -11.17901 | -54.89175 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9d60f00f-bfb0-3449-8c5f-7338ec5b7403 | -12.60694 | -46.91533 | 2026-08-05 04:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 824398af-9c3d-32bb-bec0-10476a7eee4f | -14.16355 | -54.39774 | 2026-08-05 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 311f942a-c320-37ef-bdb0-26f780fc5255 | -11.91757 | -55.91086 | 2026-08-05 04:49:00 | NOAA-21 | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| afc47606-bd08-3036-a942-69807438ba0c | -11.19728 | -54.89077 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f99bdbe9-cce1-33e5-a789-760d26232188 | -12.5987 | -46.91357 | 2026-08-05 04:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 32805fd9-5ad1-3427-9a01-3da10123df3f | -11.16626 | -54.8813 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b6e3fd10-7d43-382c-847f-52f98a00dd78 | -11.20873 | -54.90926 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8c844d02-b755-3b5a-8ce4-c64f339aceb6 | -11.18119 | -54.90044 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 87678984-f7f6-3452-a8a9-db3d19c9311d | -11.20587 | -54.90462 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 812b6faf-34b4-3ad3-bf8d-739e9210625d | -12.92766 | -49.48387 | 2026-08-05 04:49:00 | NOAA-21 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a4487a79-6e7f-335c-a76d-c71365bf5d8c | -14.02944 | -54.07395 | 2026-08-05 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |


[Clique aqui para ver as próximas entradas](README17.md)
