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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5192eb85-5564-3ed5-b66f-1e737c6d24c1 | -11.6597 | -44.5508 | 2026-07-07 06:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 81.2 |
| f6f44fb3-00ac-30ae-b2ff-b93ceae97c7c | -11.6592 | -44.5741 | 2026-07-07 06:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 83.1 |
| b86f7995-a85e-36b4-b3af-8c4a57d7115b | -11.6789 | -44.5479 | 2026-07-07 06:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 106.3 |
| 532ec6c9-5731-32fd-9695-8b0ae4673c5b | -10.9393 | -43.0832 | 2026-07-07 06:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 0b03c725-375b-3ecc-a855-6c83c826be23 | -11.6785 | -44.5712 | 2026-07-07 06:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 91.5 |
| 1cf7ddb4-4348-39ae-8a22-190f458d6413 | -10.9397 | -43.0593 | 2026-07-07 06:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 206.5 |
| 62ed2df0-7b47-3905-a02f-3ea77c03cbeb | -9.21398 | -67.39363 | 2026-07-07 06:05:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d61d507a-6b14-3c43-a4f7-a7e24153efb6 | -9.21684 | -67.39793 | 2026-07-07 06:05:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 249d8064-4cdd-3027-8c1a-22a4d8e1b09c | -8.99034 | -71.26959 | 2026-07-07 06:05:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 84529d93-a48b-301d-8836-a7aa670fbaaf | -10.20636 | -61.48832 | 2026-07-07 06:05:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| af87f417-e30c-3afa-aabf-14f063a6b47b | -9.2134 | -67.39739 | 2026-07-07 06:05:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8525bb94-c294-3b60-b6b2-971918c600f9 | -11.6592 | -44.5741 | 2026-07-07 06:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 81108344-d6d7-3f8f-a16c-cf1bc61f1efb | -10.9397 | -43.0593 | 2026-07-07 06:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 279.8 |
| 02de9da6-afc8-334f-ae3b-924fdc57e4d1 | -10.9401 | -43.0355 | 2026-07-07 06:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 65.7 |
| 40b9bed9-8e25-3fd2-a538-242de5dcc61d | -11.6789 | -44.5479 | 2026-07-07 06:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 4fcec1ec-277a-3f36-a2d6-9e490a67c666 | -11.6785 | -44.5712 | 2026-07-07 06:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 83.6 |
| 5635ddaf-4d03-3eba-b1d2-237a76b93284 | -11.6597 | -44.5508 | 2026-07-07 06:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 60.7 |
| a03a6345-0b40-3b1a-962b-19826ff345d4 | -10.9205 | -43.0622 | 2026-07-07 06:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 181.5 |
| cf2e5b4f-03cd-3d84-b8a1-307dab924982 | -10.9397 | -43.0593 | 2026-07-07 06:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 299.2 |
| 53d9777b-f8eb-3aa0-a279-ef75184075a8 | -12.7944 | -44.4895 | 2026-07-07 06:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 71.2 |
| c525584f-8595-347e-b819-5c33df19929b | -11.6592 | -44.5741 | 2026-07-07 06:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 60.4 |
| c66f4ec6-7598-3e9f-96ec-4b287d2ea4b0 | -11.6789 | -44.5479 | 2026-07-07 06:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 37ea5b08-3ab5-3f35-8e31-234adcafbcc2 | -10.9205 | -43.0622 | 2026-07-07 06:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 128.7 |
| a9a90965-a4bf-3420-b33d-17821b7c9d2b | -10.9393 | -43.0832 | 2026-07-07 06:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 73553c3a-d0f7-3b64-a1f6-f76dab46f829 | -10.9401 | -43.0355 | 2026-07-07 06:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 109.1 |
| 3fca8f26-19f7-34d0-ab45-551b17d59b45 | -11.6785 | -44.5712 | 2026-07-07 06:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 5a3a3d03-1387-3ac9-8315-a8207cd09dc8 | -6.92918 | -43.70225 | 2026-07-07 06:22:00 | AQUA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 29.1 |
| 1a8c154e-bd5e-33fb-beb6-e240a1ff5b17 | -6.92786 | -43.71101 | 2026-07-07 06:22:00 | AQUA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 4fcd981c-cf6d-3177-8bf3-52bfc6bfc86c | -6.9016 | -43.70712 | 2026-07-07 06:22:00 | AQUA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 19d68c2d-bca7-3cdf-b731-5026a7926eb5 | -6.49389 | -42.22886 | 2026-07-07 06:22:00 | AQUA_M-M | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 3d6ef7e3-974a-3f31-a95c-f79cad5e0a2d | -9.40423 | -48.02073 | 2026-07-07 06:22:00 | AQUA_M-M | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 5a8272b7-4d5c-3c37-846f-4e4ff46ffbf5 | -6.91911 | -43.70972 | 2026-07-07 06:22:00 | AQUA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 14.6 |
| f7b83d86-e4cd-36ed-9206-ce3a4f293ad9 | -6.91168 | -43.69966 | 2026-07-07 06:22:00 | AQUA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 3dabab4d-e7d8-39dd-ad67-eb3628b2db4c | -4.28307 | -48.35152 | 2026-07-07 06:22:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 17.3 |
| 6ebbb4f5-0229-34dd-90e3-e606cb84160a | -4.34115 | -47.76171 | 2026-07-07 06:22:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 32a0d292-c84e-33ae-b223-9209b8405384 | -4.83243 | -44.05097 | 2026-07-07 06:22:00 | AQUA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| c91d8023-cc50-3f93-a869-932e393205d3 | -6.93051 | -43.69349 | 2026-07-07 06:22:00 | AQUA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 9.4 |
| f3a752a0-bf17-394c-998d-29e74eb95cb6 | -4.83108 | -44.0598 | 2026-07-07 06:22:00 | AQUA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 38307139-1a19-31c9-80e3-2996152bf06f | -6.91035 | -43.70842 | 2026-07-07 06:22:00 | AQUA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 29.8 |
| 7357afa7-406b-3212-bdb1-a1e9b1ed9dbf | -11.68404 | -44.55415 | 2026-07-07 06:25:00 | AQUA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 422cb54d-308d-3f56-96d2-6006239ec000 | -11.66383 | -44.56931 | 2026-07-07 06:25:00 | AQUA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 54.2 |
| 89207cf0-65c7-3299-99a5-9e2f2d8a85c7 | -11.6726 | -44.57064 | 2026-07-07 06:25:00 | AQUA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 1ff84450-80a0-36a9-87a2-e1a231379db5 | -11.67127 | -44.57954 | 2026-07-07 06:25:00 | AQUA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 73a9b9f0-0bd0-310d-9820-6ff512ebdb8a | -11.65639 | -44.55907 | 2026-07-07 06:25:00 | AQUA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 4127b06e-ed77-3835-adea-4ee858d87a81 | -11.67527 | -44.55281 | 2026-07-07 06:25:00 | AQUA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 51.1 |
| f3cc367b-5551-3eca-95cd-5feb3c92ff5a | -11.6665 | -44.55149 | 2026-07-07 06:25:00 | AQUA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 33.8 |
| a6747adf-1b94-3b28-b040-d5a26cd79010 | -11.67393 | -44.56173 | 2026-07-07 06:25:00 | AQUA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 39.9 |
| 1d51875c-ba4b-3cd0-b56a-9136378e4820 | -10.9351 | -43.05387 | 2026-07-07 06:25:00 | AQUA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 7269d4bd-b159-398c-b823-03b0bd0a0880 | -10.9246 | -43.06212 | 2026-07-07 06:25:00 | AQUA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 153.9 |
| d4b0a66d-dbf8-3518-93f5-ba945c67dad1 | -11.68271 | -44.56306 | 2026-07-07 06:25:00 | AQUA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 71f16aa4-9902-3e8b-997a-ebd15bce3ed6 | -11.65506 | -44.56797 | 2026-07-07 06:25:00 | AQUA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 6686e516-cd72-33fc-8330-8380b999c914 | -10.92601 | -43.05255 | 2026-07-07 06:25:00 | AQUA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 232.5 |
| aa693232-70f5-35d3-a30e-5de1ad047ff4 | -12.78553 | -44.4841 | 2026-07-07 06:25:00 | AQUA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 30.5 |
| ae3e87f9-0d2f-394e-a5b5-54a9050fbdc5 | -10.93369 | -43.06345 | 2026-07-07 06:25:00 | AQUA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 228.4 |
| 59f6a214-37a9-3a8f-ab91-4844e1f14ddd | -12.79434 | -44.48543 | 2026-07-07 06:25:00 | AQUA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 18.5 |
| edb16f0d-095e-3168-aa2f-4fd3f488cc1b | -10.93228 | -43.07302 | 2026-07-07 06:25:00 | AQUA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 88946181-58ba-3bb7-8250-592df2a47243 | -11.66516 | -44.56039 | 2026-07-07 06:25:00 | AQUA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 23.1 |
| 6edc1dec-01c8-3532-be85-6e965ba489cc | -8.98963 | -71.26776 | 2026-07-07 06:27:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9aad8de3-e26c-3c0c-9309-5aa21f8c3d3b | -9.21531 | -67.39159 | 2026-07-07 06:27:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 52664853-9432-37b9-8149-254adadba0c1 | -9.21455 | -67.39732 | 2026-07-07 06:27:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cd92cd08-1719-3b5c-877f-0a218eeb4a94 | -9.20957 | -67.39662 | 2026-07-07 06:27:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 08f9b644-edf8-3074-bda6-65568295d252 | -9.21415 | -67.39547 | 2026-07-07 06:27:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7b82b21c-96ac-3295-90ec-04c3f4756743 | -9.21335 | -67.40118 | 2026-07-07 06:27:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 87b12c33-6245-302b-8b7f-7ab09f565eb8 | -8.99162 | -71.27023 | 2026-07-07 06:27:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a045a586-616a-3dd7-ac73-327de21453cb | -10.9205 | -43.0622 | 2026-07-07 06:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 151.5 |
| 87210685-d231-3707-866a-e9f98fd0cafc | -11.6789 | -44.5479 | 2026-07-07 06:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 66.9 |
| 2420072c-3e86-3b19-ac98-4fa6a7f4ece9 | -11.6785 | -44.5712 | 2026-07-07 06:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 4a5ee572-43e3-30df-bfdf-2468ff8f0543 | -10.9401 | -43.0355 | 2026-07-07 06:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 73.9 |
| d7d9c252-f501-3392-875c-b617cf5454e9 | -10.9397 | -43.0593 | 2026-07-07 06:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 277.5 |
| 501aad4a-d8fa-3be9-976d-c08fda714d3e | -11.6592 | -44.5741 | 2026-07-07 06:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 67.6 |
| bc029641-d8f5-33aa-90a3-130b8e964479 | -11.6789 | -44.5479 | 2026-07-07 06:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 67.2 |
| cf908c37-9692-33cf-baf9-cfb2fe18c566 | -11.6592 | -44.5741 | 2026-07-07 06:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 68.8 |
| a8840f87-84d2-361c-b510-5615060b75cc | -10.9205 | -43.0622 | 2026-07-07 06:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 111.8 |
| 8b71921d-85eb-3401-aa72-a62f2d6b07d2 | -10.9397 | -43.0593 | 2026-07-07 06:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 232.0 |
| 3d6be222-6ec6-3ca7-9c76-818f2d659283 | -11.6785 | -44.5712 | 2026-07-07 06:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 79.6 |
| be998934-3c22-385e-952e-c2d58db89687 | -10.9401 | -43.0355 | 2026-07-07 06:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 93.0 |
| 7a72e4e7-fe1a-375c-8214-f45365def8aa | -10.9205 | -43.0622 | 2026-07-07 06:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 101.3 |
| 74d0e72e-a389-36f6-bb0e-08b3d2ef71db | -10.9401 | -43.0355 | 2026-07-07 06:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 71.8 |
| e323900b-25e2-31bf-8881-ae67ad820e07 | -10.9397 | -43.0593 | 2026-07-07 06:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 188.9 |
| bac7e6c2-4845-3f23-a7a9-f62b7ff82855 | -11.6785 | -44.5712 | 2026-07-07 06:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 3e0de59f-ef71-3efb-afe6-56ac37ba375f | -11.6789 | -44.5479 | 2026-07-07 06:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 61.1 |
| 55a8708b-7867-3248-ad78-d49c54fab643 | -10.9205 | -43.0622 | 2026-07-07 07:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 97.8 |
| 4d975bde-f07c-3691-b33a-0d12ed7f3e74 | -10.9397 | -43.0593 | 2026-07-07 07:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 192.4 |
| 866ad7ef-56da-31c1-9fe6-c50a372f5a7e | -11.6785 | -44.5712 | 2026-07-07 07:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 60.8 |
| ea545a20-b4c9-31d6-9c83-81cb3568af33 | -10.9205 | -43.0622 | 2026-07-07 07:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 82305545-c3d9-32ae-9a0d-6fb589f91898 | -10.9397 | -43.0593 | 2026-07-07 07:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 168.7 |
| adba9e7e-eb4e-348a-9aca-ee43b02ea893 | -10.9397 | -43.0593 | 2026-07-07 07:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 121.6 |
| 45fd1f07-2252-3885-bfe9-403c1e8a048c | -10.9205 | -43.0622 | 2026-07-07 07:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 71.4 |
| c0cff0d5-c27e-332d-89ae-6b5c3380ef06 | -10.9397 | -43.0593 | 2026-07-07 07:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 123.3 |
| 7900e699-0f62-37bc-a3cb-33637c08e044 | -10.9205 | -43.0622 | 2026-07-07 07:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 0b12533b-c78e-3257-8b98-85023318d3fe | -10.9397 | -43.0593 | 2026-07-07 07:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 109.8 |
| 7cc96c7b-aa22-31bf-ba0c-170006590571 | -10.9205 | -43.0622 | 2026-07-07 07:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 0fcb6b38-a560-365e-8ee4-5832a9f6d093 | -10.9397 | -43.0593 | 2026-07-07 07:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 103.6 |
| d22ca044-36dd-3075-bf22-de38cd6cc8d4 | -10.9205 | -43.0622 | 2026-07-07 08:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 65.6 |
| a5b22718-ebe2-3e74-9237-6e1b81b0c2a7 | -10.9397 | -43.0593 | 2026-07-07 08:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 76.2 |
| db0d3f50-879d-326e-abfa-cf05fe8421d6 | -6.9138 | -43.7049 | 2026-07-07 11:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 62b9a37d-b294-363d-8505-7b94f87bc1c3 | -15.5135 | -42.1948 | 2026-07-07 12:00:00 | GOES-19 | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Cerrado | 99.1 |
| 9329caad-bbe0-3ec2-a510-bfded5259f38 | -6.9326 | -43.7032 | 2026-07-07 12:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 04ac8ba8-e8f8-3402-9eeb-de5bde038917 | -15.5135 | -42.1948 | 2026-07-07 12:10:00 | GOES-19 | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Cerrado | 96.9 |
| 630bfe27-a3b2-3495-91e7-b48e785c0e9a | -6.9326 | -43.7032 | 2026-07-07 12:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 83.8 |


[Clique aqui para ver as próximas entradas](README23.md)
