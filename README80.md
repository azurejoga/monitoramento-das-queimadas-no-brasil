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

## Dados Diários - Página 80

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 03119539-5737-38de-b58d-3e339bc46cbd | -18.03371 | -50.94589 | 2026-09-17 05:38:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 13.4 |
| a396f835-fdd0-314e-bd48-ed363ad703e6 | -11.8069 | -58.1759 | 2026-09-17 05:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 100.5 |
| a752cc6c-ca84-3301-a927-296e122cc200 | -11.8069 | -58.1759 | 2026-09-17 05:50:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 82.7 |
| 0ac7c437-0ad8-3bca-85cc-b3f336863e6f | -18.0502 | -50.935 | 2026-09-17 06:00:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 129.8 |
| 1f916306-74e9-3c53-94ce-99ad9a91f5f0 | -18.0497 | -50.9571 | 2026-09-17 06:00:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 124.1 |
| 5bbb4f4d-9945-383b-993b-cf7d6e602a23 | -11.8069 | -58.1759 | 2026-09-17 06:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 89.8 |
| 5a891d1c-3c2e-3e1b-924e-a9ef10875e8a | -18.0298 | -50.9606 | 2026-09-17 06:00:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 242.1 |
| 7ca19bc7-43eb-371b-804f-16c7db3869f7 | -18.0303 | -50.9385 | 2026-09-17 06:00:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 251.6 |
| e41794a1-5763-330c-a5fd-bd5c527dc383 | -4.54613 | -42.94297 | 2026-09-17 06:08:00 | AQUA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 23.9 |
| 6717eda9-af69-38f9-94b7-eabd929a4a7e | -4.55292 | -42.94963 | 2026-09-17 06:08:00 | AQUA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 31.2 |
| 68a95b07-999d-3570-b9af-0cce35649935 | -4.55567 | -42.93284 | 2026-09-17 06:08:00 | AQUA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 29.1 |
| 6f462a83-ddfc-349e-a5be-a4b24a18958b | -4.55801 | -42.9449 | 2026-09-17 06:08:00 | AQUA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 29.1 |
| 6222acea-1f32-3d40-be98-179e6d885525 | -18.0298 | -50.9606 | 2026-09-17 06:10:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 229.1 |
| d1b0de99-a6a8-3bf4-b5cc-8326c35fbfbc | -18.0502 | -50.935 | 2026-09-17 06:10:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 144.4 |
| e3274d7a-be4f-3f02-bfef-239aefc90036 | -11.8069 | -58.1759 | 2026-09-17 06:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 97.1 |
| e9b0f114-cc4e-3e92-a3d1-4fad431f9c98 | -18.0303 | -50.9385 | 2026-09-17 06:10:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 239.3 |
| 7d903b4b-8e3b-35fb-9b5c-c0ae6041be5c | -18.0497 | -50.9571 | 2026-09-17 06:10:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 131.6 |
| a586d63b-e2bd-369b-8901-d1a243f0a6a0 | -10.38975 | -46.62418 | 2026-09-17 06:10:00 | AQUA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 38.9 |
| a9be1f92-118a-3d3a-9aa0-2241b3322d0f | -10.82795 | -46.1419 | 2026-09-17 06:10:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 120.9 |
| eb35bbad-532a-32a5-b115-4f17dcddbc46 | -9.61848 | -45.37309 | 2026-09-17 06:10:00 | AQUA_M-M | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 42.8 |
| 8c716623-6ed1-3000-a8b9-d9e972acf887 | -9.12188 | -45.72099 | 2026-09-17 06:10:00 | AQUA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 21.1 |
| f98ddc3a-1e0c-3da8-82b0-96ba01e44612 | -7.94049 | -44.84258 | 2026-09-17 06:10:00 | AQUA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 35.7 |
| 95edf8c6-818a-3c57-be06-611446d6ce00 | -10.39369 | -46.62968 | 2026-09-17 06:10:00 | AQUA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 37.3 |
| 86096683-38a2-38ca-a277-17ec243cd471 | -14.12957 | -44.01186 | 2026-09-17 06:10:00 | AQUA_M-M | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 523256af-20bb-3c81-b594-d67bdb6afd2b | -6.93602 | -41.69755 | 2026-09-17 06:10:00 | AQUA_M-M | DOM EXPEDITO LOPES | PIAUÍ | Brasil | 2203404 | 22 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 61bed5d9-d61f-3a3d-8504-b7e15689bb50 | -7.94168 | -44.83762 | 2026-09-17 06:10:00 | AQUA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 56.4 |
| 57758284-9d8f-3119-8de9-1a9dadf5e7c2 | -8.57934 | -44.57483 | 2026-09-17 06:10:00 | AQUA_M-M | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 5e914cac-4c45-350f-9dd7-be2ec066af71 | -5.63541 | -44.78938 | 2026-09-17 06:10:00 | AQUA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 21.1 |
| dc420eef-80bd-3d16-bb2a-3de6561211fb | -9.09645 | -45.73551 | 2026-09-17 06:10:00 | AQUA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 23.4 |
| e4d6aed0-cd3e-3a63-80a0-f5b3c4b28728 | -14.55922 | -39.6313 | 2026-09-17 06:10:00 | AQUA_M-M | ITAPITANGA | BAHIA | Brasil | 2916609 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.8 |
| dbee3a8a-fc39-3cba-9edd-1b9181c4351b | -9.1003 | -45.71241 | 2026-09-17 06:10:00 | AQUA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 1e351944-f42b-3f99-9fcd-e5574059ab5d | -5.64152 | -44.79781 | 2026-09-17 06:10:00 | AQUA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 39.4 |
| e1e31fae-2b7b-3a43-8c90-cd767a25a9d5 | -12.3702 | -40.56892 | 2026-09-17 06:10:00 | AQUA_M-M | RUY BARBOSA | BAHIA | Brasil | 2927200 | 29 | 33 | nan | nan | nan | Caatinga | 11.7 |
| 0259c395-4e4a-389f-aa62-ace013b8916f | -5.76746 | -45.11083 | 2026-09-17 06:10:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 199.5 |
| 6eb442ee-5bcf-38c4-95e1-9a0b710c4c47 | -9.61764 | -45.35773 | 2026-09-17 06:10:00 | AQUA_M-M | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 54.4 |
| e363d1d1-b6b0-36a9-b9a3-daf2f2da4bfd | -10.5343 | -44.85059 | 2026-09-17 06:10:00 | AQUA_M-M | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 0f0af45b-62ee-3f8d-99c7-98e859723ced | -9.10423 | -45.74174 | 2026-09-17 06:10:00 | AQUA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 20.5 |
| a310b521-4e68-30fd-816d-37962e4d3793 | -7.02926 | -42.06774 | 2026-09-17 06:10:00 | AQUA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 11.3 |
| fca08ec1-4f52-3ba8-b730-579d97806637 | -5.76175 | -45.09279 | 2026-09-17 06:10:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 51.7 |
| 3d308034-129e-3b10-a841-9e9f91a7d575 | -6.03202 | -44.0336 | 2026-09-17 06:10:00 | AQUA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 17.4 |
| cae74082-0a50-3c4c-8ffa-a4a642ca2723 | -9.10821 | -45.7188 | 2026-09-17 06:10:00 | AQUA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 173.0 |
| 9e8986bc-e003-33f1-b817-9853022518ec | -7.08779 | -41.83854 | 2026-09-17 06:10:00 | AQUA_M-M | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 21.8 |
| 691505d4-f484-34dd-af68-5bc9b7d07838 | -10.8238 | -46.16571 | 2026-09-17 06:10:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 31.3 |
| 188f6d29-2d1e-3eda-a92e-7f65905178ef | -5.77565 | -45.09469 | 2026-09-17 06:10:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 182.4 |
| f618f67a-489f-34d7-8d94-fa0ffde0c5f2 | -10.53751 | -44.85632 | 2026-09-17 06:10:00 | AQUA_M-M | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 3347c445-34ec-3cc1-9c10-91ab7c26539e | -14.54908 | -39.63892 | 2026-09-17 06:10:00 | AQUA_M-M | ITAPITANGA | BAHIA | Brasil | 2916609 | 29 | 33 | nan | nan | nan | Mata Atlântica | 26.2 |
| f7c8b5ac-3b88-370c-9bb9-bbdf2188cd8b | -5.75761 | -45.11704 | 2026-09-17 06:10:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 27.3 |
| 108cae47-95db-3956-b74b-7bcf017cf712 | -6.92372 | -41.70832 | 2026-09-17 06:10:00 | AQUA_M-M | DOM EXPEDITO LOPES | PIAUÍ | Brasil | 2203404 | 22 | 33 | nan | nan | nan | Caatinga | 9.3 |
| ca8f4f14-f339-363b-83fe-7677c89a3340 | -9.62212 | -45.35118 | 2026-09-17 06:10:00 | AQUA_M-M | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 34.4 |
| 7f5b1cc8-4e45-34be-bade-b4e4ec1414f0 | -14.55045 | -39.62992 | 2026-09-17 06:10:00 | AQUA_M-M | ITAPITANGA | BAHIA | Brasil | 2916609 | 29 | 33 | nan | nan | nan | Mata Atlântica | 14.6 |
| 19e89574-9727-3e44-85d3-a327f544f755 | -8.26882 | -42.17353 | 2026-09-17 06:10:00 | AQUA_M-M | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 11.2 |
| f3fb2d27-0d42-3446-803a-6c3b34aff1c3 | -12.37921 | -40.57034 | 2026-09-17 06:10:00 | AQUA_M-M | RUY BARBOSA | BAHIA | Brasil | 2927200 | 29 | 33 | nan | nan | nan | Caatinga | 12.4 |
| 4e54a6fa-355f-3d2f-b589-3987baf7025d | -5.77142 | -45.08635 | 2026-09-17 06:10:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 131.0 |
| 8b530443-cccb-31b3-b011-5286bfc7ec5d | -5.7715 | -45.1192 | 2026-09-17 06:10:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 9db6bcb7-eb66-3877-ba65-2630625f833e | -7.94493 | -44.81781 | 2026-09-17 06:10:00 | AQUA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 31.8 |
| 4d532cad-ba42-32d1-8c4b-d9d9746e2307 | -13.43445 | -43.80945 | 2026-09-17 06:10:00 | AQUA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 32.6 |
| 69c985cb-bb7e-3294-8783-6f7f91f44f39 | -14.55785 | -39.64029 | 2026-09-17 06:10:00 | AQUA_M-M | ITAPITANGA | BAHIA | Brasil | 2916609 | 29 | 33 | nan | nan | nan | Mata Atlântica | 9.6 |
| b88b82e4-fcc9-3d8f-8919-30fd2d6ab6cc | -7.94392 | -44.82261 | 2026-09-17 06:10:00 | AQUA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 53.1 |
| 76218e59-21b1-3b63-b9f8-652c835d6a79 | -18.02645 | -50.94742 | 2026-09-17 06:12:00 | AQUA_M-M | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 523.0 |
| 67d0f93f-55a4-308d-9fbf-c79a29f04284 | -18.03487 | -50.90814 | 2026-09-17 06:12:00 | AQUA_M-M | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 132.8 |
| dbb628e6-689d-33e6-83c0-8ecc3fe84d13 | -18.02954 | -50.90253 | 2026-09-17 06:12:00 | AQUA_M-M | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 53.4 |
| 8ee89872-a81d-3687-a9ac-4baee9d4e839 | -16.98993 | -45.46613 | 2026-09-17 06:12:00 | AQUA_M-M | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 18.1 |
| e07c31b9-5b6d-3d69-94a4-1f02f4f165ba | -18.02135 | -50.94192 | 2026-09-17 06:12:00 | AQUA_M-M | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 660.6 |
| 0958ee3e-1dff-3b81-9416-42c12579b375 | -16.99363 | -45.45978 | 2026-09-17 06:12:00 | AQUA_M-M | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 14.0 |
| f4d4695c-0591-3392-a459-7e087865a0db | -18.03816 | -50.94533 | 2026-09-17 06:12:00 | AQUA_M-M | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 116.7 |
| 6829beb3-8c78-394d-b8f1-97653e4d5b50 | -18.0502 | -50.935 | 2026-09-17 06:20:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 95.5 |
| 706ed2ca-28c7-3391-a912-2a4ec4de5259 | -18.0303 | -50.9385 | 2026-09-17 06:20:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 248.9 |
| 3bb79add-e532-327f-852a-eed565aea802 | -18.0497 | -50.9571 | 2026-09-17 06:20:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 71baba6c-3d95-31e2-a827-7766525a5c06 | -18.0298 | -50.9606 | 2026-09-17 06:20:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 194.4 |
| 298ab754-6a1b-3fd0-a7fe-7670e79176f8 | -11.8069 | -58.1759 | 2026-09-17 06:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 87.0 |
| 99ce58ef-ae17-3896-8513-a56f284ebf48 | -7.30357 | -64.67641 | 2026-09-17 06:20:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b5d0ee10-9bd6-3a9b-97d5-3cda9c0bfc20 | -8.64789 | -66.5794 | 2026-09-17 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b03aee15-a478-380c-a181-51311d6503e2 | -9.05006 | -65.91589 | 2026-09-17 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| da328fc8-ce29-35dd-95d6-8943fe13bce0 | -8.88301 | -62.38971 | 2026-09-17 06:22:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 396a49f2-81bd-365f-bf87-1136646f4a61 | -9.10818 | -65.9462 | 2026-09-17 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d9b0a855-1598-33ba-ac9b-f8d99e613523 | -9.33643 | -68.84937 | 2026-09-17 06:22:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 962a1dea-8b4f-3dd7-bc8c-14e1d12e506d | -9.48111 | -65.65909 | 2026-09-17 06:22:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 155faa96-2964-3230-bfc6-fca80ca9d7c6 | -8.92334 | -62.40165 | 2026-09-17 06:22:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1fe36fb5-f162-30ec-b658-0440f6a45abb | -8.75615 | -66.56945 | 2026-09-17 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d15db3e0-d947-36d7-82fe-86f72b176856 | -7.79644 | -66.91715 | 2026-09-17 06:22:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8603484a-2e7f-3193-84c7-5380ae16ebed | -8.75047 | -66.57195 | 2026-09-17 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e0beb667-6dca-346a-9bef-b47284200fb5 | -8.09273 | -71.28243 | 2026-09-17 06:22:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 180208fb-0606-3fb8-a14a-0d3fb3e9d6ea | -9.10728 | -65.94992 | 2026-09-17 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7214c697-c522-3b1e-aed0-05e14df2516c | -8.65098 | -66.59639 | 2026-09-17 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4d9a5c6a-eb14-3c62-83f3-fdbd58b9272c | -9.11415 | -65.94328 | 2026-09-17 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2ccb6b15-d7cb-3b0b-8b1c-1545d107d2a4 | -7.79603 | -66.92011 | 2026-09-17 06:22:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9ddcc41e-d1de-345e-8653-55cdb274ac3a | -7.56989 | -73.0389 | 2026-09-17 06:22:00 | NOAA-21 | MÂNCIO LIMA | ACRE | Brasil | 1200336 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8008dba4-ce73-3cf5-a7cd-1eb5a5e94252 | -9.34549 | -65.9351 | 2026-09-17 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9209a5d5-aac4-36ea-b7f9-ff15377f4c30 | -9.10775 | -65.94636 | 2026-09-17 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e6314b93-dbfb-3eec-a2f1-35219db25178 | -9.10863 | -65.9426 | 2026-09-17 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 29da6b72-c4bb-3af2-bb70-4a15b22defd8 | -8.91648 | -62.4008 | 2026-09-17 06:22:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e45a1157-2af3-395e-8598-d93c25cd1765 | -9.1092 | -65.93555 | 2026-09-17 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7b1cbc6f-4131-31fe-b3fb-648fb6618be1 | -7.80072 | -66.91495 | 2026-09-17 06:22:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 71730bc3-4a92-3a58-a8f6-aa8ef7b93556 | -9.11552 | -65.93247 | 2026-09-17 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7750c0b7-8940-3138-8d06-7538ea1953c9 | -7.61244 | -67.24615 | 2026-09-17 06:22:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7e589fae-f455-37ec-a611-29a6fa571d98 | -9.10954 | -65.93538 | 2026-09-17 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8d6e5683-cabc-33e9-99bc-a0f6a5656e28 | -9.10823 | -65.94276 | 2026-09-17 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2cc8e15f-cc6b-382e-970b-0fe03be77981 | -8.7509 | -66.5687 | 2026-09-17 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3ae281b6-628d-331c-b390-14c08ad70ef2 | -8.75572 | -66.57269 | 2026-09-17 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 46d43752-e981-3492-969d-ca544b125e1f | -9.1137 | -65.94689 | 2026-09-17 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README81.md)
