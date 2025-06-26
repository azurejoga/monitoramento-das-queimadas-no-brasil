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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 17afa7da-68d3-3aa1-8b48-17fc50665260 | -11.07091 | -55.38091 | 2025-06-26 05:08:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| cb767f44-8b14-3b1f-ad3d-c5cb8330bd20 | -10.87732 | -56.45816 | 2025-06-26 05:08:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| c6546c2e-8268-3783-8bbd-cb93fbb4cc73 | -11.88315 | -54.6701 | 2025-06-26 05:08:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 05afac76-5b52-3731-988e-e01a0d2ef26e | -12.79786 | -48.7349 | 2025-06-26 05:08:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 59beb6c4-d9c5-327c-82f6-6b6d3609dd4d | -12.21619 | -51.46429 | 2025-06-26 05:08:00 | NPP-375D | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c78dad16-4b4b-3d89-a5f2-f5b0ec17af60 | -11.06185 | -55.37197 | 2025-06-26 05:08:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 336ac8c2-b8f3-3c42-8224-54131b2239b6 | -11.13225 | -58.61209 | 2025-06-26 05:08:00 | NPP-375D | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 84de11a0-3325-33b4-a8df-76d61b8ad447 | -10.29785 | -57.13151 | 2025-06-26 05:08:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| bf6c4ecc-d6ed-321c-89f2-eaf644638359 | -11.57366 | -54.52459 | 2025-06-26 05:08:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b116cc8e-bcd0-3350-9623-a3a7b835a177 | -11.2375 | -49.50171 | 2025-06-26 05:08:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4be3ec4d-93bb-38a6-b195-617ccb514716 | -11.35997 | -48.71194 | 2025-06-26 05:08:00 | NPP-375D | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 52d3ce07-460e-31ff-8247-046589a9ee28 | -12.65635 | -54.10466 | 2025-06-26 05:08:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| edb45dd1-21e2-34da-b351-c79325764b85 | -11.83374 | -51.25243 | 2025-06-26 05:08:00 | NPP-375D | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 222f6537-d9c9-3009-abce-dc691f20be57 | -11.95824 | -47.01557 | 2025-06-26 05:08:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5c21fbe5-2f84-3568-b6f9-02cb27b9c18b | -10.02843 | -54.32023 | 2025-06-26 05:08:00 | NPP-375D | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7b86c3d5-2945-3e25-8020-1d48ae86fc0b | -13.10001 | -52.29888 | 2025-06-26 05:08:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 5c2e7232-631a-39bf-9685-b3933384dda0 | -11.58845 | -44.63793 | 2025-06-26 05:08:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f6bfe138-3cb6-3b0f-bdef-3f6064d3671b | -11.61554 | -58.28341 | 2025-06-26 05:08:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6802300e-e544-3e67-90ca-23167e01490e | -11.57129 | -47.42931 | 2025-06-26 05:08:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 79cdffbe-6a3d-3db0-9b2d-552b5c0851f6 | -11.61891 | -58.28397 | 2025-06-26 05:08:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8c1f97aa-c9b5-3578-9b8e-c0a0ac7c3e0c | -9.7943 | -57.42284 | 2025-06-26 05:08:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 89a7234e-a11e-302e-b634-1a61c2f98f18 | -11.07203 | -55.37355 | 2025-06-26 05:08:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3d00d63f-53cf-3bf9-82af-37fb3d099092 | -12.04562 | -48.07978 | 2025-06-26 05:08:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 50564788-9eaf-3331-be3b-99233bcbd300 | -11.07147 | -55.37724 | 2025-06-26 05:08:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| a6a18db2-ac49-36d3-99d0-5f719ce1256f | -11.12937 | -46.88616 | 2025-06-26 05:08:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6564c942-3a7f-396a-854b-7d1b53b7e375 | -11.07712 | -46.6317 | 2025-06-26 05:08:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3383045a-274c-31ea-b4a5-b29e3a0aac51 | -10.8286 | -53.73533 | 2025-06-26 05:08:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 44781a23-5fe2-3afe-8359-984252b9dc23 | -12.79277 | -48.73409 | 2025-06-26 05:08:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8133f523-f73d-35c6-9c78-cda722bdf06c | -9.39277 | -63.26521 | 2025-06-26 05:08:00 | NPP-375D | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a9469b48-6dae-337f-bd91-42e8857120af | -11.58779 | -44.64354 | 2025-06-26 05:08:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 613710f2-a965-3515-a0e2-7ab30b384d34 | -12.1315 | -50.16974 | 2025-06-26 05:08:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 62ae4c10-9abd-34b1-b6db-15e92f1db69e | -11.86657 | -52.25218 | 2025-06-26 05:08:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ffead3b6-f37f-3f2d-bc74-c3b40988de4a | -11.06478 | -55.07715 | 2025-06-26 05:08:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 8e731727-dbf9-35c2-8b32-e49573031a93 | -11.12892 | -46.88988 | 2025-06-26 05:08:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 626fd47b-e6f0-3500-92e4-dbbd3561100b | -12.04641 | -48.07995 | 2025-06-26 05:08:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6926da1c-8e04-36c3-b6f4-26405f9dddf5 | -9.24772 | -63.28851 | 2025-06-26 05:08:00 | NPP-375D | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 58104fe6-4761-319c-9349-28b5071a3b00 | -10.30338 | -57.13962 | 2025-06-26 05:08:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fd2c44ac-e351-3cd1-a618-747501598350 | -11.79199 | -47.54145 | 2025-06-26 05:08:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fdf4fa22-486b-3670-9a31-0bcb7e81c6cb | -10.50129 | -53.58774 | 2025-06-26 05:08:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e3d1a984-5d6a-37bb-9ad1-b0ba8493fbf2 | -12.76294 | -44.40279 | 2025-06-26 05:08:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4c205866-2ddd-363a-9348-beb54b311311 | -13.03819 | -48.83063 | 2025-06-26 05:08:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 03321dbc-efcb-3d72-b78f-55bdb414c28e | -11.5695 | -52.10284 | 2025-06-26 05:08:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 8aafd631-b474-34fb-b322-3d09b8c89a17 | -13.78041 | -54.30133 | 2025-06-26 05:08:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f87dd0cb-00d2-3253-a71d-9734fb9842f0 | -11.91986 | -54.81047 | 2025-06-26 05:08:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 95b1b8f6-7724-3683-86fc-1a30234a8cbe | -11.80803 | -57.35566 | 2025-06-26 05:08:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 2a6e1486-0782-3a84-897a-7deeb3606e14 | -13.29176 | -57.0856 | 2025-06-26 05:08:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ace09d44-fecf-3a13-8cf9-312cbe3d92cf | -11.81136 | -57.3562 | 2025-06-26 05:08:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 4ba1c1b7-c41f-3c7b-99a0-ccbd9174a674 | -9.58174 | -63.20675 | 2025-06-26 05:08:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8d480173-55f9-380b-9e1e-712af26d37ae | -11.81176 | -47.56134 | 2025-06-26 05:08:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3c50c944-3d31-3d60-b519-e3b61f622e74 | -11.95441 | -47.02142 | 2025-06-26 05:08:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0b3aacc6-c049-374c-9d51-0cc109f67171 | -10.06516 | -55.5488 | 2025-06-26 05:08:00 | NPP-375D | NOVA GUARITA | MATO GROSSO | Brasil | 5108808 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7e1c5829-644e-3017-a926-d916d4e5797e | -11.13622 | -53.91822 | 2025-06-26 05:08:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 08f88639-0964-3a91-b63c-6086125ba0b8 | -12.02235 | -57.09381 | 2025-06-26 05:08:00 | NPP-375D | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 04a2d823-3d0f-3cad-bd61-c13c979f4a82 | -11.808 | -55.07304 | 2025-06-26 05:08:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 67041b00-0ef0-358d-8585-d47038c1d3c4 | -9.39271 | -63.26807 | 2025-06-26 05:08:00 | NPP-375D | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 58bccba6-6752-39ce-b265-d757e491ae34 | -12.53138 | -57.19081 | 2025-06-26 05:08:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 93c0d3f8-1a25-3b33-a4d0-b51372abd4f9 | -12.52805 | -57.19026 | 2025-06-26 05:08:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eb03f4d2-737c-353e-80f2-c27a4139fe88 | -11.44081 | -54.47706 | 2025-06-26 05:08:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 096cb830-b1aa-3142-8c92-4f38d97548af | -11.82838 | -51.2598 | 2025-06-26 05:08:00 | NPP-375D | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 79f4f393-d5e0-38c6-aa77-8d660a5e553c | -12.02623 | -57.09082 | 2025-06-26 05:08:00 | NPP-375D | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f4751811-c696-3d82-9ed5-5ebb809c99a9 | -14.38309 | -50.32876 | 2025-06-26 05:08:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e3dbf94e-0a8b-33a6-84e2-fc1d8542ebc5 | -11.91117 | -54.82102 | 2025-06-26 05:08:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f50f559f-de96-3028-b5ed-3dec75a91069 | -11.36573 | -48.70688 | 2025-06-26 05:08:00 | NPP-375D | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 18ee42ee-10c9-322d-b561-65dc84146c60 | -12.02678 | -57.0873 | 2025-06-26 05:08:00 | NPP-375D | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e07090bd-5136-3754-9e88-8c2ff8f35659 | -12.02346 | -57.08675 | 2025-06-26 05:08:00 | NPP-375D | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fe52f77f-0e4b-3dea-87ee-78c1e8a3fe84 | -11.1398 | -53.91879 | 2025-06-26 05:08:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c93a2a38-99a1-3e54-a685-53d894f6cbdf | -12.61842 | -57.87684 | 2025-06-26 05:08:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6ced561e-43fe-3daa-b16f-b183da08c090 | -11.06879 | -55.07389 | 2025-06-26 05:08:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9e26c564-15a3-3dd1-bea7-7757d1915aa3 | -11.95351 | -47.02913 | 2025-06-26 05:08:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6211618f-b695-35ad-86ec-3cf788b44585 | -10.16299 | -53.92794 | 2025-06-26 05:08:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 653fbfe6-4256-373f-afa8-1a52b102a131 | -8.72465 | -64.1605 | 2025-06-26 05:08:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e0f22884-1c8f-3db0-9e97-ae67306105bd | -11.4373 | -54.47651 | 2025-06-26 05:08:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c7be91fb-ea5c-3034-8625-a7bc3f151319 | -11.79714 | -47.54185 | 2025-06-26 05:08:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 388a6702-ba58-3a49-8aee-c18e709cd398 | -13.52026 | -56.57675 | 2025-06-26 05:08:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6d95daba-f25c-3ef8-8e4b-ee490640dd91 | -11.06808 | -55.37671 | 2025-06-26 05:08:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 04d8c88d-58aa-3836-a50f-a6c1084a8d15 | -17.14331 | -52.49099 | 2025-06-26 05:08:00 | NPP-375D | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9c52f5d6-95d1-3090-8343-d9c2ca06c2e5 | -11.23889 | -49.49155 | 2025-06-26 05:08:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| debf503f-b889-3269-a60b-a275552e001e | -11.0943 | -46.6343 | 2025-06-26 05:08:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c34e46d9-3c8c-3309-a5c4-6ac60089eb4a | -11.10949 | -46.65302 | 2025-06-26 05:08:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ecf3e1b3-fdee-3d98-8991-4ce2c5358cb7 | -9.25224 | -63.2894 | 2025-06-26 05:08:00 | NPP-375D | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fd4d59e0-1444-37af-b9d3-89d33dd61dd3 | -10.82139 | -53.73421 | 2025-06-26 05:08:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b348cdf3-0c90-310b-be6c-a415e8577ce2 | -11.43671 | -54.48047 | 2025-06-26 05:08:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2c6c1bbe-74d1-3c06-8b19-21f867b9a5d6 | -13.78024 | -54.29882 | 2025-06-26 05:08:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 615becd5-a795-34f9-8c18-b3a97ba53e61 | -11.80297 | -47.5397 | 2025-06-26 05:08:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d472f7e1-92b4-34c6-9299-c5dfef877a88 | -13.0491 | -48.82613 | 2025-06-26 05:08:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d8eff212-c291-3f7d-9541-bed30f231d90 | -11.60388 | -55.54199 | 2025-06-26 05:08:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 45b70ab3-45c0-3cd9-9435-fb778959b79c | -11.06422 | -46.64188 | 2025-06-26 05:08:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b373c7e0-7c66-338a-a853-18d82bf838fb | -10.29729 | -57.13502 | 2025-06-26 05:08:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6b3edbd1-9e02-3f14-bd4b-9b70c8336753 | -9.79374 | -57.42637 | 2025-06-26 05:08:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ea8cec86-5dd0-3031-b2dc-eadcb2fdf521 | -12.80807 | -48.73632 | 2025-06-26 05:08:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d8db05bb-e343-3e61-a98a-e503614b12ca | -15.07988 | -48.94666 | 2025-06-26 05:08:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ff800547-0f22-3ce3-976a-8184d810c751 | -11.95487 | -47.01756 | 2025-06-26 05:08:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 885ad400-26d8-3eb7-b9e1-4c76ed7aada3 | -11.60444 | -55.53831 | 2025-06-26 05:08:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 478d7bdb-7665-3a1e-a995-e6bd7d005dee | -11.0579 | -55.37511 | 2025-06-26 05:08:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 14e143af-c558-33cb-9583-66442f1a35a5 | -11.82359 | -51.26315 | 2025-06-26 05:08:00 | NPP-375D | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1d3a94b6-4626-33d8-a884-b16e5b62b2e5 | -10.06461 | -55.55239 | 2025-06-26 05:08:00 | NPP-375D | NOVA GUARITA | MATO GROSSO | Brasil | 5108808 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0e2b6d6a-c71f-3f67-9c6c-54c4d2db0797 | -10.82374 | -53.74318 | 2025-06-26 05:08:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 035fffec-8050-3729-909d-77e56648c87e | -11.07043 | -46.63873 | 2025-06-26 05:08:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8cff608b-83db-3b5b-bcf3-6c155731d337 | -10.86773 | -53.77811 | 2025-06-26 05:08:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 897f5325-fa0e-3df4-be7e-876dd78bf849 | -12.9051 | -56.98653 | 2025-06-26 05:08:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README19.md)
