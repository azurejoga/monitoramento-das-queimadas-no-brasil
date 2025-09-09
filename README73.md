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

## Dados Diários - Página 73

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 72b23745-63f9-3ae1-baf0-21b28f94adfa | -21.8717 | -47.3167 | 2025-09-09 06:50:00 | GOES-19 | PIRASSUNUNGA | SÃO PAULO | Brasil | 3539301 | 35 | 33 | nan | nan | nan | Mata Atlântica | 81.1 |
| 4dff4ef5-3b08-32b3-8687-c4a97f77873b | -10.962 | -45.113 | 2025-09-09 06:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 46.2 |
| 40c183ad-d33d-3dfe-b329-2f73c71db693 | -21.4348 | -48.8503 | 2025-09-09 06:50:00 | GOES-19 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 129.1 |
| 186dfcb6-aebe-3971-b652-e50f48127cae | -12.1991 | -53.8817 | 2025-09-09 06:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 99b64c64-486f-3dd0-95ea-341288ebce84 | -21.4562 | -48.8222 | 2025-09-09 06:50:00 | GOES-19 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 82.1 |
| e9c31c7c-7acf-376d-82ad-688063623346 | -21.4355 | -48.827 | 2025-09-09 06:50:00 | GOES-19 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 669cfa1c-c532-3a08-a8b9-a59299cf340f | -21.4555 | -48.8455 | 2025-09-09 06:50:00 | GOES-19 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 170.7 |
| d2bddc13-649d-33a7-be00-b43f4cb26b34 | -10.9815 | -45.0874 | 2025-09-09 06:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 46.8 |
| 36db204e-8cd1-3211-b4c0-30f152147b18 | -21.4562 | -48.8222 | 2025-09-09 07:00:00 | GOES-19 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 137.2 |
| d31bae05-b452-3ee6-839b-1bc30c54880c | -21.8717 | -47.3167 | 2025-09-09 07:00:00 | GOES-19 | PIRASSUNUNGA | SÃO PAULO | Brasil | 3539301 | 35 | 33 | nan | nan | nan | Mata Atlântica | 238.6 |
| 5727646d-78cb-35bc-b271-b86bba36183c | -10.9811 | -45.1104 | 2025-09-09 07:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 74.3 |
| bb53767c-52bc-376b-a237-6f249503b878 | -21.8925 | -47.3114 | 2025-09-09 07:00:00 | GOES-19 | PIRASSUNUNGA | SÃO PAULO | Brasil | 3539301 | 35 | 33 | nan | nan | nan | Mata Atlântica | 113.7 |
| ae1d2eea-7820-3780-93a7-ec3ef34127e2 | -21.4548 | -48.8687 | 2025-09-09 07:00:00 | GOES-19 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 101.8 |
| 93573558-52ff-3d79-abb4-ae11a1746784 | -21.871 | -47.3406 | 2025-09-09 07:00:00 | GOES-19 | PIRASSUNUNGA | SÃO PAULO | Brasil | 3539301 | 35 | 33 | nan | nan | nan | Mata Atlântica | 126.3 |
| b05e9a14-85d6-3fda-bd0d-bcdbb04ebed0 | -21.4355 | -48.827 | 2025-09-09 07:00:00 | GOES-19 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 100.7 |
| dd42defc-a1a1-3fba-9bd6-8c3f1dbd0578 | -12.1991 | -53.8817 | 2025-09-09 07:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 7b7b14e2-0842-3c84-8cdb-424398a0518d | -15.8205 | -52.2444 | 2025-09-09 07:00:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 87.7 |
| 78c3a38e-436a-3c87-bb16-3b879e1c83f1 | -21.4555 | -48.8455 | 2025-09-09 07:00:00 | GOES-19 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 452.0 |
| c955caf6-c7ca-3f65-a638-85f2ba71378b | -12.1988 | -53.9024 | 2025-09-09 07:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 78.1 |
| 7e25bb87-c6c1-3060-8dcf-4fe0ac96631e | -21.4348 | -48.8503 | 2025-09-09 07:00:00 | GOES-19 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 255.6 |
| fed275f0-7b08-338d-8bdf-a1c5281cfeca | -10.962 | -45.113 | 2025-09-09 07:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 44.9 |
| 2f2ea429-1c37-3b40-a3d0-c118febbfda0 | -10.9815 | -45.0874 | 2025-09-09 07:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 45.0 |
| 81014c28-a5c9-31d2-9b57-86edfea3053d | -10.962 | -45.113 | 2025-09-09 07:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 47.6 |
| fe5079a3-ea89-33da-959b-f1ff986159f1 | -10.9811 | -45.1104 | 2025-09-09 07:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 57.4 |
| 6accc3b7-f70b-3dc8-832c-ea36c6df3a31 | -21.4555 | -48.8455 | 2025-09-09 07:10:00 | GOES-19 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 139.7 |
| 528718cc-5180-3e9c-b2d7-70a552a5b3c7 | -12.1991 | -53.8817 | 2025-09-09 07:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 91a79802-31d7-36d0-b65a-9a92d88afaf3 | -21.871 | -47.3406 | 2025-09-09 07:10:00 | GOES-19 | PIRASSUNUNGA | SÃO PAULO | Brasil | 3539301 | 35 | 33 | nan | nan | nan | Mata Atlântica | 154.7 |
| c6c5c6cf-a4c6-3348-8987-30d2248aebfb | -21.8925 | -47.3114 | 2025-09-09 07:10:00 | GOES-19 | PIRASSUNUNGA | SÃO PAULO | Brasil | 3539301 | 35 | 33 | nan | nan | nan | Mata Atlântica | 157.9 |
| 00a3709a-5005-3f05-9bee-b9372e32b518 | -12.0298 | -51.0722 | 2025-09-09 07:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 55.7 |
| 8fc5dd3f-94f9-37dc-9ff3-07bbf7449992 | -21.8918 | -47.3353 | 2025-09-09 07:10:00 | GOES-19 | PIRASSUNUNGA | SÃO PAULO | Brasil | 3539301 | 35 | 33 | nan | nan | nan | Mata Atlântica | 121.1 |
| 021af3b7-778c-38dc-8bea-bb20716796c8 | -21.8717 | -47.3167 | 2025-09-09 07:10:00 | GOES-19 | PIRASSUNUNGA | SÃO PAULO | Brasil | 3539301 | 35 | 33 | nan | nan | nan | Mata Atlântica | 225.7 |
| 30d13b9d-3dea-3b05-a9fa-7754ceb0bbb7 | -12.1988 | -53.9024 | 2025-09-09 07:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 9452a272-acd8-3797-b991-008e1adfb686 | -14.3421 | -47.3365 | 2025-09-09 07:20:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 41.1 |
| 281e3485-10c3-36dd-aa38-d9de1ee7b83e | -14.3615 | -47.3333 | 2025-09-09 07:20:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 128.0 |
| 72d62558-9ab7-3055-ba64-3df594478817 | -21.8717 | -47.3167 | 2025-09-09 07:20:00 | GOES-19 | PIRASSUNUNGA | SÃO PAULO | Brasil | 3539301 | 35 | 33 | nan | nan | nan | Mata Atlântica | 169.8 |
| 05b8fd37-c6b0-39f6-8ddb-4172396f9395 | -12.1988 | -53.9024 | 2025-09-09 07:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 8ab88b07-f98e-3bf9-9cb1-e78123816d35 | -14.362 | -47.3107 | 2025-09-09 07:20:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 66.6 |
| ef578c35-1855-3785-92e8-15c5de14ab60 | -9.7206 | -46.8302 | 2025-09-09 07:20:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 64.2 |
| f29421f2-7dea-30e3-97bd-dfbb07e34080 | -21.871 | -47.3406 | 2025-09-09 07:20:00 | GOES-19 | PIRASSUNUNGA | SÃO PAULO | Brasil | 3539301 | 35 | 33 | nan | nan | nan | Mata Atlântica | 105.5 |
| 9a30023a-28ee-3b03-b21c-b4d872359c40 | -12.0298 | -51.0722 | 2025-09-09 07:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 65.8 |
| e4fa6d3b-a436-35f7-ab46-e43b2af4cd65 | -21.8925 | -47.3114 | 2025-09-09 07:20:00 | GOES-19 | PIRASSUNUNGA | SÃO PAULO | Brasil | 3539301 | 35 | 33 | nan | nan | nan | Mata Atlântica | 91.6 |
| b4d3efa9-1dc6-31e9-8c39-ba4f1972e403 | -10.9811 | -45.1104 | 2025-09-09 07:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 57.4 |
| c70dc952-82ff-3163-b918-d972539bcbb5 | -12.1991 | -53.8817 | 2025-09-09 07:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 70.7 |
| f20279d8-0bb2-39b8-9ed9-47448e601970 | -21.871 | -47.3406 | 2025-09-09 07:30:00 | GOES-19 | PIRASSUNUNGA | SÃO PAULO | Brasil | 3539301 | 35 | 33 | nan | nan | nan | Mata Atlântica | 161.7 |
| eb483fe3-0671-3ee5-bc56-f646c78946e6 | -21.8925 | -47.3114 | 2025-09-09 07:30:00 | GOES-19 | PIRASSUNUNGA | SÃO PAULO | Brasil | 3539301 | 35 | 33 | nan | nan | nan | Mata Atlântica | 135.3 |
| 0aa6760a-1ef4-348b-8681-3f85226206b9 | -21.8918 | -47.3353 | 2025-09-09 07:30:00 | GOES-19 | PIRASSUNUNGA | SÃO PAULO | Brasil | 3539301 | 35 | 33 | nan | nan | nan | Mata Atlântica | 101.3 |
| 53f5249c-c364-39d4-9d68-d76737881a25 | -10.9811 | -45.1104 | 2025-09-09 07:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 52.4 |
| 41535f70-c28d-3942-901e-9623f13783a9 | -21.8717 | -47.3167 | 2025-09-09 07:30:00 | GOES-19 | PIRASSUNUNGA | SÃO PAULO | Brasil | 3539301 | 35 | 33 | nan | nan | nan | Mata Atlântica | 245.9 |
| b61a011d-1b5a-337d-9b44-d5ad5e7f47f0 | -14.362 | -47.3107 | 2025-09-09 07:30:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 57.1 |
| 9784db85-2d50-3a96-99be-aef12d421026 | -14.3615 | -47.3333 | 2025-09-09 07:30:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 106.8 |
| 32f8269f-cb5f-345a-82db-20785669b131 | -12.1991 | -53.8817 | 2025-09-09 07:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 75.2 |
| 3e828676-9460-3097-a30a-2cc8410c54d5 | -14.3421 | -47.3365 | 2025-09-09 07:30:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 34.5 |
| cdc5a805-5c83-3967-af94-858d92f3fb94 | -12.1988 | -53.9024 | 2025-09-09 07:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 57.8 |
| ff473568-c863-3afc-a4de-0033195234e4 | -7.5407 | -48.2303 | 2025-09-09 07:30:00 | GOES-19 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 0d77f0a8-0796-331d-90b6-282d10e9df40 | -12.0298 | -51.0722 | 2025-09-09 07:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 93d375cc-f511-3471-83df-b650e3b2ab3a | -12.1988 | -53.9024 | 2025-09-09 07:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 7d550a0d-03af-3096-a1ad-88120d32114d | -21.8918 | -47.3353 | 2025-09-09 07:40:00 | GOES-19 | PIRASSUNUNGA | SÃO PAULO | Brasil | 3539301 | 35 | 33 | nan | nan | nan | Mata Atlântica | 202.3 |
| c480819f-a515-3053-97bb-ab8a19e8c933 | -21.8925 | -47.3114 | 2025-09-09 07:40:00 | GOES-19 | PIRASSUNUNGA | SÃO PAULO | Brasil | 3539301 | 35 | 33 | nan | nan | nan | Mata Atlântica | 254.9 |
| 7b4bdfe1-20a3-328c-96ae-436ee300476a | -21.8717 | -47.3167 | 2025-09-09 07:40:00 | GOES-19 | PIRASSUNUNGA | SÃO PAULO | Brasil | 3539301 | 35 | 33 | nan | nan | nan | Mata Atlântica | 273.0 |
| 38d25641-4749-30e2-b3ad-340bdee2727d | -21.871 | -47.3406 | 2025-09-09 07:40:00 | GOES-19 | PIRASSUNUNGA | SÃO PAULO | Brasil | 3539301 | 35 | 33 | nan | nan | nan | Mata Atlântica | 201.3 |
| 349bba95-f86d-3224-96ed-6f36075a3218 | -10.9811 | -45.1104 | 2025-09-09 07:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 54.7 |
| c58637e7-d687-388b-97bc-91a4a16fac18 | -15.8205 | -52.2444 | 2025-09-09 07:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 86f6e12d-1211-3c82-b1cc-e11e354e2014 | -21.4355 | -48.827 | 2025-09-09 07:40:00 | GOES-19 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 117.2 |
| ae59c65f-dd70-3b24-a547-ffec4c290588 | -12.1991 | -53.8817 | 2025-09-09 07:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 66.2 |
| f66686fd-6acb-37f4-a88a-640db25fa2a1 | -14.3615 | -47.3333 | 2025-09-09 07:40:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 53.9 |
| 8c25fc30-c193-30d9-a44f-1fba73cd9368 | -21.871 | -47.3406 | 2025-09-09 07:50:00 | GOES-19 | PIRASSUNUNGA | SÃO PAULO | Brasil | 3539301 | 35 | 33 | nan | nan | nan | Mata Atlântica | 292.9 |
| 589a87ea-d089-3bd1-904d-ae6d13496364 | -21.8925 | -47.3114 | 2025-09-09 07:50:00 | GOES-19 | PIRASSUNUNGA | SÃO PAULO | Brasil | 3539301 | 35 | 33 | nan | nan | nan | Mata Atlântica | 362.1 |
| d580351d-3ba3-3094-9c6a-3d0a55552e0a | -15.8275 | -48.9505 | 2025-09-09 07:50:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 55.7 |
| d05a6ad8-6102-3a99-9b2e-f9229e052a81 | -21.8918 | -47.3353 | 2025-09-09 07:50:00 | GOES-19 | PIRASSUNUNGA | SÃO PAULO | Brasil | 3539301 | 35 | 33 | nan | nan | nan | Mata Atlântica | 356.3 |
| 9b244bfe-ade4-3a33-9f43-f1c0783d0c0f | -14.3615 | -47.3333 | 2025-09-09 07:50:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 52.5 |
| b8730c7d-a276-382e-86de-6abf8bd6e43e | -12.1988 | -53.9024 | 2025-09-09 07:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 63.4 |
| e47d06d4-6954-35bc-8bf2-e435e5098053 | -15.8205 | -52.2444 | 2025-09-09 07:50:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 115.0 |
| ef9b3477-4c09-3418-9713-e4750e9d975c | -12.1991 | -53.8817 | 2025-09-09 07:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 328763b5-2df9-3c1b-ba12-d9d9435cb10e | -10.9811 | -45.1104 | 2025-09-09 07:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 52.7 |
| ba80f398-cc85-36c3-81b4-83f03e9a9af0 | -21.8717 | -47.3167 | 2025-09-09 07:50:00 | GOES-19 | PIRASSUNUNGA | SÃO PAULO | Brasil | 3539301 | 35 | 33 | nan | nan | nan | Mata Atlântica | 307.2 |
| 60da40de-7fb9-3b72-a3fb-9f721da64e6a | -21.871 | -47.3406 | 2025-09-09 08:00:00 | GOES-19 | PIRASSUNUNGA | SÃO PAULO | Brasil | 3539301 | 35 | 33 | nan | nan | nan | Mata Atlântica | 286.7 |
| 5726dacc-ccfd-3dd2-9848-476eaa6ddc91 | -21.8918 | -47.3353 | 2025-09-09 08:00:00 | GOES-19 | PIRASSUNUNGA | SÃO PAULO | Brasil | 3539301 | 35 | 33 | nan | nan | nan | Mata Atlântica | 381.0 |
| baebff99-8fca-3cd3-b4e2-24310f26d3a0 | -21.8717 | -47.3167 | 2025-09-09 08:00:00 | GOES-19 | PIRASSUNUNGA | SÃO PAULO | Brasil | 3539301 | 35 | 33 | nan | nan | nan | Mata Atlântica | 196.6 |
| 2aefaaf7-a85c-3ee0-9243-77fa73663de5 | -12.1991 | -53.8817 | 2025-09-09 08:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 64.3 |
| feb78807-498a-3033-9303-9a6b657de0e9 | -12.1988 | -53.9024 | 2025-09-09 08:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 60.4 |
| d9dcde14-58fc-3cf3-bde6-793b0370ea1f | -14.3615 | -47.3333 | 2025-09-09 08:00:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 20548f16-5634-340a-b68b-f7d8784d9ca3 | -21.8911 | -47.3591 | 2025-09-09 08:00:00 | GOES-19 | PIRASSUNUNGA | SÃO PAULO | Brasil | 3539301 | 35 | 33 | nan | nan | nan | Mata Atlântica | 77.4 |
| 4b2e8128-fec9-38ee-ac2d-c56a9c0f6daf | -21.8925 | -47.3114 | 2025-09-09 08:00:00 | GOES-19 | PIRASSUNUNGA | SÃO PAULO | Brasil | 3539301 | 35 | 33 | nan | nan | nan | Mata Atlântica | 232.4 |
| d6d311d2-909a-3f10-bc6d-c75780a013b0 | -21.8911 | -47.3591 | 2025-09-09 08:10:00 | GOES-19 | PIRASSUNUNGA | SÃO PAULO | Brasil | 3539301 | 35 | 33 | nan | nan | nan | Mata Atlântica | 93.1 |
| df1d2fb4-cf91-3e8d-89ca-5a9d39fa8624 | -21.8702 | -47.3644 | 2025-09-09 08:10:00 | GOES-19 | PIRASSUNUNGA | SÃO PAULO | Brasil | 3539301 | 35 | 33 | nan | nan | nan | Mata Atlântica | 82.8 |
| d2fa587e-bae7-3143-9f4b-d78a5f3a0380 | -21.8918 | -47.3353 | 2025-09-09 08:10:00 | GOES-19 | PIRASSUNUNGA | SÃO PAULO | Brasil | 3539301 | 35 | 33 | nan | nan | nan | Mata Atlântica | 400.2 |
| c271ef87-65d3-3346-a0b3-780b01764d62 | -21.8925 | -47.3114 | 2025-09-09 08:10:00 | GOES-19 | PIRASSUNUNGA | SÃO PAULO | Brasil | 3539301 | 35 | 33 | nan | nan | nan | Mata Atlântica | 233.9 |
| a8d2143a-55b8-3897-ad33-aab29c73e6a1 | -21.8717 | -47.3167 | 2025-09-09 08:10:00 | GOES-19 | PIRASSUNUNGA | SÃO PAULO | Brasil | 3539301 | 35 | 33 | nan | nan | nan | Mata Atlântica | 223.2 |
| 004737ed-aec7-3e6d-9da2-d5c2d4a4c6c6 | -12.1988 | -53.9024 | 2025-09-09 08:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 0b63a789-5ea0-38f4-a65a-b5d5438e4b07 | -15.8205 | -52.2444 | 2025-09-09 08:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 3eaa24e5-3758-3cf1-8d69-c7265651a6ad | -10.9811 | -45.1104 | 2025-09-09 08:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 50.4 |
| e338009b-c65e-38c5-ae6e-b010fb5e23a3 | -21.871 | -47.3406 | 2025-09-09 08:10:00 | GOES-19 | PIRASSUNUNGA | SÃO PAULO | Brasil | 3539301 | 35 | 33 | nan | nan | nan | Mata Atlântica | 363.0 |
| bf241c29-b7cc-3dc4-af97-95e723f2e0f0 | -12.1991 | -53.8817 | 2025-09-09 08:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 1399dec7-d06e-3709-8050-6d4d9263f5e6 | -21.871 | -47.3406 | 2025-09-09 08:20:00 | GOES-19 | PIRASSUNUNGA | SÃO PAULO | Brasil | 3539301 | 35 | 33 | nan | nan | nan | Mata Atlântica | 168.7 |
| 3e1cc7b7-9a3d-3ebb-a3a7-2a1f4c036811 | -21.8918 | -47.3353 | 2025-09-09 08:20:00 | GOES-19 | PIRASSUNUNGA | SÃO PAULO | Brasil | 3539301 | 35 | 33 | nan | nan | nan | Mata Atlântica | 340.1 |
| 7dbc18e9-81c6-346e-bbc3-f3ab45962a3a | -12.1988 | -53.9024 | 2025-09-09 08:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 416d7288-d9e0-30d4-8c72-311c77cfac21 | -12.1991 | -53.8817 | 2025-09-09 08:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 60.5 |
| a48389ed-ecea-3b25-9918-3bedb2c615eb | -21.8717 | -47.3167 | 2025-09-09 08:20:00 | GOES-19 | PIRASSUNUNGA | SÃO PAULO | Brasil | 3539301 | 35 | 33 | nan | nan | nan | Mata Atlântica | 117.5 |
| 10ec4c02-dc66-349e-903b-06b001ac6ad9 | -21.8925 | -47.3114 | 2025-09-09 08:20:00 | GOES-19 | PIRASSUNUNGA | SÃO PAULO | Brasil | 3539301 | 35 | 33 | nan | nan | nan | Mata Atlântica | 173.4 |
| 5476cd04-a51c-3e75-b80e-7b5bb84d868d | -21.8918 | -47.3353 | 2025-09-09 08:30:00 | GOES-19 | PIRASSUNUNGA | SÃO PAULO | Brasil | 3539301 | 35 | 33 | nan | nan | nan | Mata Atlântica | 172.0 |


[Clique aqui para ver as próximas entradas](README74.md)
