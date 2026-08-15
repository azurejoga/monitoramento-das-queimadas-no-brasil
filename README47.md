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

## Dados Diários - Página 47

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5cae5296-7c9e-3ada-8772-5aa4c0f6b7bd | -11.59117 | -54.66809 | 2026-08-15 05:55:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3e08f567-068c-322a-88bb-d78d7375a2dc | -11.49707 | -54.63667 | 2026-08-15 05:55:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| af85b001-1679-3994-923b-0b42ccd59b44 | -6.53389 | -55.17783 | 2026-08-15 05:55:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f9832289-3a8e-37a8-89c2-908e18c01664 | -11.59218 | -54.67518 | 2026-08-15 05:55:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c4056ea1-efde-3b42-86cd-09fbf9aaa879 | -9.70835 | -69.06727 | 2026-08-15 05:55:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 694abd25-d770-38a9-bd64-a041ed01bc0c | -11.49874 | -54.63547 | 2026-08-15 05:55:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a82b161d-ab58-3409-b3fc-02a1880879a3 | -6.02045 | -57.83847 | 2026-08-15 05:55:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 00f032c4-20e8-369f-b178-cb4212bb763d | -6.20815 | -57.7714 | 2026-08-15 05:55:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| eef44090-2128-376f-871c-fc38bd44cf2b | -6.2471 | -55.62381 | 2026-08-15 05:55:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 4e5c6306-67a3-38f4-9d71-b572072ec125 | -11.58824 | -54.69468 | 2026-08-15 05:55:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 07ed0a0a-b565-3b52-bbee-cd2462062e55 | -13.4226 | -57.05252 | 2026-08-15 05:55:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 69677e2f-747b-34dc-ad8f-21276d6345d9 | -11.58896 | -54.68818 | 2026-08-15 05:55:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 46ab85c0-921f-3a66-b1bb-6f6afd58b45d | -11.59044 | -54.67479 | 2026-08-15 05:55:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2ea0091b-7a29-3941-a87a-6cfcc286fb80 | -3.94767 | -59.62824 | 2026-08-15 05:55:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a3ea3c37-2712-3def-907a-74e19f6daec3 | -6.02767 | -57.82603 | 2026-08-15 05:55:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9a1dcc73-f4b0-3291-b60f-6cd32dfa375e | -13.42879 | -57.05346 | 2026-08-15 05:55:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 504fcb26-9831-3aa3-a598-ad08fe4a7ee6 | -11.11368 | -62.89471 | 2026-08-15 05:55:00 | NOAA-20 | MIRANTE DA SERRA | RONDÔNIA | Brasil | 1101302 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1ffc5538-07c1-3ca2-84ef-6097fa693b73 | -11.50485 | -54.63073 | 2026-08-15 05:55:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 3db43cf6-884a-3379-b40b-070644c78077 | -6.20274 | -57.7708 | 2026-08-15 05:55:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| c2172c5b-e026-3ee6-a085-6d43c8a55dbd | -6.20865 | -57.76792 | 2026-08-15 05:55:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| ad0d0636-ea62-33bd-b4fd-cb98173a055c | -6.016 | -57.83131 | 2026-08-15 05:55:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ccf1977b-e02a-3b95-a5a6-efa2a9bb437f | -9.71505 | -69.06836 | 2026-08-15 05:55:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1b926324-ae75-3399-be7e-f7698d31ec60 | -13.42317 | -57.04771 | 2026-08-15 05:55:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cf00d0cb-c5ad-34fb-8a93-61c80dd5c47b | -14.4309 | -51.8816 | 2026-08-15 06:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 1131b027-c9d0-32ed-b51d-11d2f774fa3c | -11.4367 | -46.3934 | 2026-08-15 06:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 267.5 |
| 2b3910b8-3c85-325f-acec-a3f15d7a2965 | -6.9334 | -43.6333 | 2026-08-15 06:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 62.7 |
| 42437657-5050-3d9f-97f9-9dca089dab33 | -11.4562 | -46.3681 | 2026-08-15 06:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 47.7 |
| 5ef7ec40-5b56-3120-ac60-3c8e33506bb9 | -11.4176 | -46.3959 | 2026-08-15 06:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 62.3 |
| 0cd92351-965b-374f-a2c4-f2872dfea8f5 | -14.4302 | -51.9243 | 2026-08-15 06:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 161.7 |
| e523a33a-5569-3362-9f16-75b7fb6a4a9d | -14.4112 | -51.9055 | 2026-08-15 06:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 97.4 |
| 3d2ec7cd-a0a7-3a2e-8cc7-17a3061a10cf | -6.6194 | -59.0609 | 2026-08-15 06:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 51.9 |
| d8b743b8-d0f4-3387-be1c-a6ca52842537 | -14.4499 | -51.9004 | 2026-08-15 06:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 154.8 |
| 69d5d56c-378b-34c1-a858-3312bd5816a4 | -14.4495 | -51.9217 | 2026-08-15 06:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 72.3 |
| e7ebe190-3e4d-33d9-96a7-018684fae70c | -14.4306 | -51.9029 | 2026-08-15 06:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 402.2 |
| b39069e8-c10c-3f21-afaa-ad553d8584fc | -11.4559 | -46.3908 | 2026-08-15 06:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 87.9 |
| 1591ece1-5688-35cd-873f-957727f458f7 | -11.418 | -46.3733 | 2026-08-15 06:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 67.1 |
| c59bfcf5-f42b-32d5-b16a-491738b12e43 | -11.4371 | -46.3707 | 2026-08-15 06:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 171.7 |
| 6e78fb81-a6d6-370c-9cc0-2c44accaffec | -6.9334 | -43.6333 | 2026-08-15 06:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 57.0 |
| c57e886b-924e-3cc1-8022-5375d54f5f32 | -11.4367 | -46.3934 | 2026-08-15 06:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 186.5 |
| 97669bd8-de1b-3b15-8b17-d7350e23069d | -14.4302 | -51.9243 | 2026-08-15 06:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 87.9 |
| c5eb46c2-30bd-3771-a186-2dab4c439ef3 | -11.4371 | -46.3707 | 2026-08-15 06:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 91.7 |
| d66b46a2-e474-3ae0-b3b1-837d7c7396e9 | -14.4112 | -51.9055 | 2026-08-15 06:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 77.0 |
| e482cb9f-e9af-39a2-a41a-bd4be26beeaf | -14.4499 | -51.9004 | 2026-08-15 06:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 88.0 |
| ccb25dd5-8232-3c1a-99bf-a2af14fa961f | -14.4306 | -51.9029 | 2026-08-15 06:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 205.4 |
| 5cd169f8-dd67-30f1-ba5b-1d21c86e9766 | -14.4309 | -51.8816 | 2026-08-15 06:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 52.8 |
| 70639e39-5ca2-3726-89da-3b735833a8cf | -11.43 | -46.4 | 2026-08-15 06:15:00 | MSG-03 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e101ddd0-a29f-3429-8327-a81b324b4581 | -14.43 | -51.9 | 2026-08-15 06:15:00 | MSG-03 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a83023c6-d086-3d52-b802-e1a9daea6599 | -14.4306 | -51.9029 | 2026-08-15 06:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 155.9 |
| 0ddbeb34-b2f3-36b0-9649-2d1eb5ee9d66 | -14.4499 | -51.9004 | 2026-08-15 06:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 79ed3b1b-af02-3df5-921c-d050e9ac2f44 | -14.4302 | -51.9243 | 2026-08-15 06:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 1c4fd1ff-e247-3601-8706-6f89ee4ae19d | -11.4367 | -46.3934 | 2026-08-15 06:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 160.6 |
| 81bf123d-9487-3bea-a689-6602cb0a97ca | -14.4112 | -51.9055 | 2026-08-15 06:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 51.5 |
| 4024e9a8-a63b-352c-ab3d-3bd51920ad15 | -11.4371 | -46.3707 | 2026-08-15 06:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 43.9 |
| 292d3981-b045-366b-885b-9ad5980d3a0d | -11.4559 | -46.3908 | 2026-08-15 06:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 85.5 |
| 633714e2-24ec-3f71-ac91-a32dfd928f17 | -4.11049 | -42.50418 | 2026-08-15 06:29:00 | AQUA_M-M | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 26d037a5-6ff4-34f5-8cf4-8832ebf87e20 | -4.10241 | -42.49728 | 2026-08-15 06:29:00 | AQUA_M-M | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 9.2 |
| 4e70610c-88be-36ea-aeef-7c2a87d397b7 | -4.10098 | -42.50677 | 2026-08-15 06:29:00 | AQUA_M-M | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 74acea45-6ace-3484-b03b-02d5566899e1 | -11.4371 | -46.3707 | 2026-08-15 06:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 47.4 |
| 0e175a46-eced-35ad-8090-84245bec69f5 | -11.4559 | -46.3908 | 2026-08-15 06:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 119.3 |
| 3e14a6c3-7402-3f76-bb07-864222cf70be | -14.4302 | -51.9243 | 2026-08-15 06:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 4e024b9b-2a74-3841-924b-f79a2cf790b7 | -14.4499 | -51.9004 | 2026-08-15 06:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 59.1 |
| b0043976-f5dc-344e-b529-ea92b829750d | -14.4306 | -51.9029 | 2026-08-15 06:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 154.2 |
| 8f78404f-0805-37af-aa7f-9fcdc994fa9a | -11.4367 | -46.3934 | 2026-08-15 06:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 269.0 |
| 75a5e451-63f0-3771-8835-0ab7392fdc12 | -11.4364 | -46.416 | 2026-08-15 06:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 161.1 |
| d324f60b-d069-3414-b989-4217347814f8 | -11.4555 | -46.4134 | 2026-08-15 06:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 74.5 |
| e46578ec-bf42-3c02-8e04-1063cb301262 | -9.11715 | -46.40012 | 2026-08-15 06:31:00 | AQUA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 94587e5d-ef48-3446-8110-986da560ca3f | -11.43971 | -46.38951 | 2026-08-15 06:31:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 4ea26fce-42af-3189-9b9c-aefd220d4700 | -6.26818 | -43.28275 | 2026-08-15 06:31:00 | AQUA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| b2ad4da5-9b1e-3f60-89ae-8d99e26a0e05 | -11.43834 | -46.39845 | 2026-08-15 06:31:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 266.7 |
| d2b766e5-6168-323c-b92b-3935f72c4e83 | -6.11943 | -44.03682 | 2026-08-15 06:31:00 | AQUA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 9cedeeed-e201-3bea-bca5-20ad324620f7 | -6.92631 | -43.64452 | 2026-08-15 06:31:00 | AQUA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 31.3 |
| 7811f109-b186-3e18-9df5-10494cf0f4e2 | -11.4235 | -46.37792 | 2026-08-15 06:31:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 24.7 |
| fec784c1-5040-3cfe-8812-c0eaa86eefee | -6.3351 | -44.07193 | 2026-08-15 06:31:00 | AQUA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 58cab2da-e66f-390a-ad87-b65d055ee8cf | -11.43092 | -46.3882 | 2026-08-15 06:31:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 38.1 |
| b2daba55-bc86-3fb1-b505-890f18e38ce2 | -6.92902 | -43.62627 | 2026-08-15 06:31:00 | AQUA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 5c3b3db0-d722-320c-b806-34751e908135 | -10.41355 | -47.98211 | 2026-08-15 06:31:00 | AQUA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 2f941daf-085f-383e-8d88-3470f98416b4 | -6.33644 | -44.06305 | 2026-08-15 06:31:00 | AQUA_M-M | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 0add59c0-bcdd-3294-8c84-a15a96a049df | -6.91872 | -43.6341 | 2026-08-15 06:31:00 | AQUA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 11.7 |
| bbfc5945-78b9-34d9-9240-9706815ac22c | -11.41883 | -46.34975 | 2026-08-15 06:31:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 2132a742-4dc4-3c04-b281-90e2c62e8ba4 | -11.43697 | -46.4074 | 2026-08-15 06:31:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 143.0 |
| 5a6a8104-ce57-3281-bfbd-dcf704250f43 | -6.99344 | -45.89 | 2026-08-15 06:31:00 | AQUA_M-M | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| ebc26f29-61b0-352d-be63-91be4766aa09 | -7.26858 | -44.68367 | 2026-08-15 06:31:00 | AQUA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 3960c8ba-c7a9-3797-bcc7-994510a71607 | -8.49228 | -44.73641 | 2026-08-15 06:31:00 | AQUA_M-M | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 5234a60f-5c72-3292-bc79-da6d0263d02d | -6.92008 | -43.62495 | 2026-08-15 06:31:00 | AQUA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ff494ab1-a581-3515-809b-a01018e4b24b | -10.16149 | -48.25358 | 2026-08-15 06:31:00 | AQUA_M-M | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 3f3a6565-1628-3988-a7a0-224c726d27b1 | -6.26955 | -43.27351 | 2026-08-15 06:31:00 | AQUA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 44fd7462-c953-36ae-949d-b55386842a17 | -8.49096 | -44.74525 | 2026-08-15 06:31:00 | AQUA_M-M | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 11.9 |
| b8bf02f7-a862-34a2-a373-ea97ad8d5a36 | -11.41141 | -46.3395 | 2026-08-15 06:31:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 1db4f915-6571-3db4-b99f-4221102c7716 | -6.92766 | -43.63543 | 2026-08-15 06:31:00 | AQUA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 39.6 |
| 6d2d2190-114e-355a-9056-54911c6529ac | -6.99207 | -45.89895 | 2026-08-15 06:31:00 | AQUA_M-M | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 15.5 |
| d6f04ed3-86c9-302b-a5be-554f08424ea4 | -6.12076 | -44.02792 | 2026-08-15 06:31:00 | AQUA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 37.5 |
| 611919c6-35d1-3ca2-84d9-b584caa00bc7 | -12.37872 | -46.41451 | 2026-08-15 06:31:00 | AQUA_M-M | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 07eda422-6423-3f71-9e68-9500fbca1cd7 | -11.42955 | -46.39717 | 2026-08-15 06:31:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 98.2 |
| f1f8e972-8a79-34b4-ac86-80c9cec7a99b | -9.10827 | -46.39874 | 2026-08-15 06:31:00 | AQUA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| bcfd77c9-c9cf-336f-8ea9-5ae1f919eac9 | -16.10895 | -49.85094 | 2026-08-15 06:33:00 | AQUA_M-M | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| ad20d375-b7e0-3909-ab1f-5795a0931ae3 | -14.2913 | -42.70811 | 2026-08-15 06:33:00 | AQUA_M-M | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 15908c5e-fdc8-3f6b-82d0-94e0f93f9329 | -13.68806 | -46.25666 | 2026-08-15 06:33:00 | AQUA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b2e7972d-0e12-37b9-b686-36acb00b9f03 | -18.51657 | -48.25 | 2026-08-15 06:33:00 | AQUA_M-M | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 23.0 |
| cb5d3134-250c-36a3-ba14-281203bcf528 | -14.41908 | -51.91432 | 2026-08-15 06:33:00 | AQUA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 54.1 |
| d5420367-0878-33f3-b9b5-1269d2319a94 | -14.95615 | -46.63002 | 2026-08-15 06:33:00 | AQUA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 11.9 |


[Clique aqui para ver as próximas entradas](README48.md)
