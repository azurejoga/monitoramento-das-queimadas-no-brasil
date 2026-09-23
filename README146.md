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

## Dados Diários - Página 146

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2857e6d1-491c-3f9b-aa00-ea32810d8419 | -2.9525 | -57.72 | 2026-09-23 15:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 755545af-76a6-3770-91ff-99a03f0c6665 | -5.809 | -47.7692 | 2026-09-23 15:10:00 | GOES-19 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 49754474-25b5-3c79-99ee-d6db223ff5be | 1.7846 | -56.0393 | 2026-09-23 15:10:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 4e80fdce-e1ce-323d-aacf-dacca3516a74 | -6.2767 | -47.5631 | 2026-09-23 15:10:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 93.4 |
| f5a86d68-93ac-39a0-ac46-9b8cab69169a | -10.5561 | -46.7095 | 2026-09-23 15:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 229.0 |
| 067b43e7-7b28-3215-8039-ff3e4428a32a | -1.6041 | -54.455 | 2026-09-23 15:10:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 2c72685d-f59e-3c22-8073-b7c5d65d126f | -7.9798 | -47.4711 | 2026-09-23 15:10:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 113.7 |
| 036e6191-e910-3d7f-8a58-a16bba76d3df | 1.5102 | -55.885 | 2026-09-23 15:10:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 1265e860-2bdd-3246-aa7b-148951406c7d | -8.4983 | -57.6271 | 2026-09-23 15:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 117.1 |
| 9a84475e-bb4e-3361-a60a-a5911381bb87 | -8.0279 | -61.3626 | 2026-09-23 15:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 69.4 |
| bf6631f1-42f6-32e7-b069-3bdfb8f884b8 | -7.8811 | -61.1779 | 2026-09-23 15:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 1fb3bdde-f4e7-36e9-988a-fc3b6323b364 | -8.4985 | -57.6075 | 2026-09-23 15:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 199.9 |
| 176d38fd-93d5-3423-a7b1-0f09e9a02dae | -9.5731 | -47.9529 | 2026-09-23 15:10:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 121.8 |
| 0fad8b14-3da9-3095-aa1d-801bdb849e24 | -2.8609 | -57.78 | 2026-09-23 15:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 8b9e87a3-0534-3bce-8f9c-6bcab4a5ca74 | -6.4486 | -59.9717 | 2026-09-23 15:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 104.6 |
| e34e237f-24bf-327b-8712-9bf817bf4225 | -13.5 | -40.74 | 2026-09-23 15:15:00 | MSG-03 | IRAMAIA | BAHIA | Brasil | 2914307 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| eef5202e-0ba8-33b7-8ec4-d04f7e10a06b | -13.53 | -40.75 | 2026-09-23 15:15:00 | MSG-03 | IRAMAIA | BAHIA | Brasil | 2914307 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| dbececb8-115f-3322-9c2f-af7ce70a1943 | -6.61 | -43.7 | 2026-09-23 15:15:00 | MSG-03 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8c22ea53-a8d6-3161-ae62-f45f37daeaf9 | -6.61 | -43.74 | 2026-09-23 15:15:00 | MSG-03 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ef9f74a1-b4de-311c-825d-3a45a7d4e73b | -13.53 | -40.71 | 2026-09-23 15:15:00 | MSG-03 | IRAMAIA | BAHIA | Brasil | 2914307 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 9a3ffba6-6f1a-30f9-a0d3-f17c6a33a1fb | -8.746 | -44.8586 | 2026-09-23 15:20:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 105.0 |
| 5409baa3-d44f-3dcd-9a03-a0a20f4f56b4 | -6.4302 | -59.9724 | 2026-09-23 15:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 81.6 |
| 25ca7c76-592a-3896-b208-2b3df962ce4d | -1.5859 | -54.4153 | 2026-09-23 15:20:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 5d67f1cf-098c-37fa-94e6-7561a45d1375 | -6.5963 | -59.9087 | 2026-09-23 15:20:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 84.0 |
| 712df684-992b-3d68-a1a6-be5d0139af8d | -6.3383 | -59.9374 | 2026-09-23 15:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 72.1 |
| a71b0edb-1bd2-3ea8-bce5-3e707ad33cf3 | -1.8218 | -55.7037 | 2026-09-23 15:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 2406aa6d-6472-35f5-a842-1b2f19f7fc0f | -1.2189 | -54.5592 | 2026-09-23 15:20:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 1489cb47-b8fa-35b3-a71b-191b813d6600 | -2.9525 | -57.7394 | 2026-09-23 15:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 911613fc-9cac-3a3a-a717-38f64ba94a93 | -6.9029 | -46.5456 | 2026-09-23 15:20:00 | GOES-19 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 101.9 |
| e6c36778-bce4-3c46-966e-83a2ceda948e | -6.9225 | -42.9088 | 2026-09-23 15:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 82.2 |
| 899079b3-201d-3270-adac-7c7e2bf51f1a | -8.9016 | -45.933 | 2026-09-23 15:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 8256cf3a-b3c3-3169-ad22-17d55f0ba967 | -6.8152 | -47.8735 | 2026-09-23 15:20:00 | GOES-19 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 91.3 |
| fdf02253-bb38-3191-8370-ff7798beb87b | -1.0244 | -48.8087 | 2026-09-23 15:20:00 | GOES-19 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 858554df-2e3c-35c0-8aad-dc71cb392d5a | -6.6148 | -59.908 | 2026-09-23 15:20:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 142.7 |
| 64d5bba3-55df-3234-ae93-511a86d927a3 | 1.224 | -50.9764 | 2026-09-23 15:20:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 5d050f93-17cf-3f9b-bdbf-96a31a955109 | -6.1849 | -45.3241 | 2026-09-23 15:20:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 68.9 |
| f58e4a94-ef9c-3676-a692-5b7c30eb9f15 | 1.5102 | -55.885 | 2026-09-23 15:20:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 52.6 |
| c2974384-fcc9-337e-9852-9dc1d607bc91 | -2.9525 | -57.72 | 2026-09-23 15:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 73e2d93e-49d5-3e02-a64c-e72f3ca5dc59 | -7.3564 | -44.4726 | 2026-09-23 15:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 74.9 |
| ec9ad419-5a54-36de-9d29-5dc26c49c54a | -6.3382 | -59.9566 | 2026-09-23 15:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 110.2 |
| dc7f1ccd-bdd3-31b4-97d3-6d59b36e54f8 | -5.6567 | -60.2092 | 2026-09-23 15:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 4e151292-7156-3624-a2b4-99e927f38560 | -2.7713 | -57.0229 | 2026-09-23 15:20:00 | GOES-19 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 3c5e7089-8869-3334-b685-1120c518e665 | -6.5763 | -45.4968 | 2026-09-23 15:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 106.3 |
| ccb9171e-feed-3429-ae94-d983c4e48e0e | -6.2026 | -47.5026 | 2026-09-23 15:20:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 97b0db1c-c965-3824-9d14-4eccb1d1259c | -8.8735 | -49.7328 | 2026-09-23 15:20:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 116.9 |
| 07570169-75f6-304d-8e4c-4ae3ca23ffb0 | -1.4303 | -48.9316 | 2026-09-23 15:20:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 56.5 |
| d8109703-f2e4-3872-87ed-9ab8f1461c67 | -11.4588 | -47.3777 | 2026-09-23 15:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 136.1 |
| eac61c94-1408-3d2d-a183-0bf637f3b2bb | -7.8811 | -61.1779 | 2026-09-23 15:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 67.5 |
| bba07a61-7d3d-3e28-b650-12fd3b3651de | -2.5687 | -57.5135 | 2026-09-23 15:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 1d574a82-c5aa-34ba-afcb-d1c69d5dc636 | -5.2895 | -60.2014 | 2026-09-23 15:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 79.7 |
| e9351a14-8ba5-3e04-a566-def2a51267ed | -6.9228 | -42.8852 | 2026-09-23 15:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 74.1 |
| a8c90301-27d7-3085-998a-c38d0016ab2d | -11.4209 | -47.3603 | 2026-09-23 15:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 154.0 |
| 64d09129-7b4e-31e7-aae0-386cddaf9197 | -1.9271 | -58.2587 | 2026-09-23 15:20:00 | GOES-19 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 108.8 |
| 9736039b-3610-30a9-b558-97c6293c88c8 | 1.4453 | -50.7655 | 2026-09-23 15:20:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 72.5 |
| fc9156e9-fd39-3fba-bdbf-a0a56a469d59 | -7.2994 | -59.5343 | 2026-09-23 15:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 69.7 |
| d2e59f08-b421-3dde-b7c5-33e594978838 | -1.5674 | -54.4555 | 2026-09-23 15:20:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 60.7 |
| b1a19832-5c90-377e-a33c-726c0c9d35c0 | -9.406 | -47.7507 | 2026-09-23 15:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 94.4 |
| ca4682cc-1fbb-30c0-bb1c-117b72813a96 | -1.6042 | -54.435 | 2026-09-23 15:20:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 59.9 |
| ccd6239a-7b92-33cc-b215-56473435c175 | -6.4487 | -59.9526 | 2026-09-23 15:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 3d25f92a-acdf-337d-9a5f-73af3ae187c1 | 1.5652 | -55.845 | 2026-09-23 15:20:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 57.9 |
| d3d83c51-9adc-3b6c-8172-febd5e1ff09d | -8.4985 | -57.6075 | 2026-09-23 15:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 224.5 |
| 6ca17294-2be4-334d-8e3b-a17148f44bc5 | -6.5442 | -44.9555 | 2026-09-23 15:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 59.4 |
| fefc196e-ca0c-3b9f-996b-5bd165485f7a | -1.9088 | -58.2589 | 2026-09-23 15:20:00 | GOES-19 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 80.9 |
| 0e3440c8-24ab-3392-b9be-41f1261ed6c6 | -8.7069 | -49.5336 | 2026-09-23 15:20:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 101.2 |
| 65d4e9bf-6c80-3e23-b319-874feda4d64e | -3.7167 | -54.1896 | 2026-09-23 15:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 125.9 |
| 2fa1db58-55bb-317a-b4ef-fcf17fbabaa9 | 1.2425 | -50.893 | 2026-09-23 15:20:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 26fe7116-4d0f-37d4-8879-5b03a128a66a | -8.4983 | -57.6271 | 2026-09-23 15:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 107.6 |
| 23c7a3af-0e94-3acd-aaa6-ba1c39e82669 | -6.3199 | -59.9381 | 2026-09-23 15:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 107.9 |
| 7ed56fbe-cbf7-36c0-a928-b052a57e052e | -2.7713 | -57.0229 | 2026-09-23 15:30:00 | GOES-19 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 75.5 |
| a7347e97-b0e7-37ee-8b33-536c91d3cc26 | -1.9271 | -58.2587 | 2026-09-23 15:30:00 | GOES-19 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 176.4 |
| 8b97dcf6-f3fc-377c-a147-8dde98e6f273 | -8.8735 | -49.7328 | 2026-09-23 15:30:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 76.5 |
| 328cbd28-0ea4-382a-8354-ac68389e69f0 | -8.0279 | -61.3626 | 2026-09-23 15:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 97292921-6ca8-3b4e-a673-76cca970fc42 | 1.5469 | -55.8255 | 2026-09-23 15:30:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 57.9 |
| fd5cb1d9-078d-3312-ba9f-76b4691f8082 | -7.6448 | -57.6337 | 2026-09-23 15:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 0c8cf2d5-8aaf-3998-b111-d7c2bff26842 | -6.6148 | -59.908 | 2026-09-23 15:30:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 136.8 |
| a942652e-5323-3ab7-9308-f72a72640f3b | -2.6993 | -56.5353 | 2026-09-23 15:30:00 | GOES-19 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 7fa3b44c-501a-3b7d-a426-5f66a1d87c55 | -6.4487 | -59.9526 | 2026-09-23 15:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 86.6 |
| 2ec0b59c-cf05-3ab9-93d1-1f1aacade8c6 | -6.3383 | -59.9374 | 2026-09-23 15:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 78.2 |
| 224d27ae-ae3f-3756-a880-ba3499b6359a | -9.5731 | -47.9529 | 2026-09-23 15:30:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 109.1 |
| 1ecc7f4e-7241-35bf-928e-93d688450d7e | -6.6357 | -45.1752 | 2026-09-23 15:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 5527cfd7-b77f-32cc-96d2-a988a6befa91 | -6.5442 | -44.9555 | 2026-09-23 15:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 56.0 |
| afd91c39-863a-3860-8887-ca7e0bddbb1e | -1.4303 | -48.9316 | 2026-09-23 15:30:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| f933e2c9-bde7-3ecb-8f78-a8fcf0476aa0 | 1.5285 | -55.8454 | 2026-09-23 15:30:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 75.3 |
| dd57b766-5552-3e1d-9a4d-12e980d98115 | -5.2895 | -60.2014 | 2026-09-23 15:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 79.8 |
| faad59cf-5c1f-30d2-b1ae-453b93979e56 | 1.5651 | -55.8647 | 2026-09-23 15:30:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 80674f02-09dd-30e4-b4e6-f5979826e5e3 | 1.5286 | -55.8257 | 2026-09-23 15:30:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 62.4 |
| fc96c354-f916-323b-b251-81ff3a07ae54 | -9.3797 | -48.3232 | 2026-09-23 15:30:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 90.7 |
| 2ce1c8bd-e5f1-3ff7-8783-f3b0c62270d7 | -5.2711 | -60.2019 | 2026-09-23 15:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 91fcc652-e5c1-37c3-8305-48c7ad0d0e7d | -8.4983 | -57.6271 | 2026-09-23 15:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 120.1 |
| 266bdc75-130f-39e3-8525-0beddd7cb795 | -1.6042 | -54.435 | 2026-09-23 15:30:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 5f725341-c8e5-306c-9344-9ab25f112da2 | -1.8218 | -55.7037 | 2026-09-23 15:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 49.6 |
| da75b9ed-0edb-37f3-9314-76e8ed9b037c | -6.3199 | -59.9381 | 2026-09-23 15:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 104.1 |
| c54649f2-91a0-3fd4-aef7-02d395eda56e | -1.5674 | -54.4555 | 2026-09-23 15:30:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 62.8 |
| ff9a1de0-d8cd-32cf-9649-733e993baa57 | -6.6332 | -59.9073 | 2026-09-23 15:30:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 66.6 |
| c3742e7d-bc02-3bdd-9677-a7d0c510f47f | 1.4453 | -50.7655 | 2026-09-23 15:30:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 68044d86-f2ae-3b70-ae93-fadff1bd4cfa | -3.8096 | -58.8802 | 2026-09-23 15:30:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 77.0 |
| 0d62f43b-5ac8-36c1-98a3-32c61f93be41 | -2.9158 | -57.7789 | 2026-09-23 15:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 36336558-f6fe-3e6a-8055-661f1df4ad01 | -8.4985 | -57.6075 | 2026-09-23 15:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 260.9 |
| fc44efe6-3086-3070-a6fa-6412d8d8c2ad | -6.5963 | -59.9087 | 2026-09-23 15:30:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 78.6 |
| 1733e04a-c267-314b-98a4-032449b9c019 | 1.5102 | -55.8456 | 2026-09-23 15:30:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 68.3 |


[Clique aqui para ver as próximas entradas](README147.md)
