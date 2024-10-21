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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e89beebc-b482-3d72-bb4b-192cb4a121de | -3.03951 | -51.0225 | 2024-10-21 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 84a6214c-7098-3f0a-9ad9-ecc0f3e86c9e | -3.03899 | -51.02564 | 2024-10-21 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| af6c395e-8622-3875-addd-b6e12dc0121a | -3.03014 | -50.39273 | 2024-10-21 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 21a9ddc2-2078-3914-8e0e-e1d3a576f418 | -3.0292 | -50.39847 | 2024-10-21 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ce005bf2-65a7-3fd8-9920-add9f1a0d50b | -3.02556 | -54.34723 | 2024-10-21 04:12:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a9fa9919-f218-304e-8205-94fc3326303e | -3.02462 | -54.35281 | 2024-10-21 04:12:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cabeeda5-2d62-38a2-ab36-9c1745360dcd | -3.01912 | -54.34587 | 2024-10-21 04:12:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3e3f5374-3a39-327c-8cbb-ce46f448aa06 | -3.01815 | -54.35162 | 2024-10-21 04:12:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bdcccc9a-370a-32d3-8acc-7be1151e3027 | -3.01721 | -54.35719 | 2024-10-21 04:12:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 605acf81-04d1-3540-b0eb-e2e2c786e362 | -2.99945 | -53.04957 | 2024-10-21 04:12:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 6aea91dc-e6cd-38d6-afe0-8c8215723021 | -2.99869 | -53.0541 | 2024-10-21 04:12:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 7409fb90-83c4-3b95-9a6c-174b5569e188 | -2.99864 | -51.0417 | 2024-10-21 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a1dc83fc-0799-3914-b296-1ee8dcaf0674 | -2.99811 | -51.0449 | 2024-10-21 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c5e03b7e-6791-37a8-8354-1df0d44f048f | -2.99425 | -53.04392 | 2024-10-21 04:12:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| e6dc3c19-ef97-3e37-9381-de9aba4184e0 | -2.99349 | -53.04844 | 2024-10-21 04:12:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| f27746e0-0c7e-35ce-8ee5-6c1316d5672d | -2.99272 | -53.05297 | 2024-10-21 04:12:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 7eafe159-d0d1-3d46-b9a9-5276e9dc72c2 | -2.99019 | -51.05999 | 2024-10-21 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d318c329-c961-3203-be02-ce182c005a05 | -2.98601 | -51.05271 | 2024-10-21 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| db8570d8-812c-3e9b-9b18-8015d8d4af95 | -2.98548 | -51.05591 | 2024-10-21 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dd8554e0-97ff-3ef7-9a61-cb4434b1c47e | -2.98489 | -50.29575 | 2024-10-21 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7f55193e-4a21-3ef2-8efd-f6dc04f803f4 | -2.97273 | -47.99294 | 2024-10-21 04:12:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e6def062-de3b-372d-ad97-616ef9640625 | -2.96848 | -47.99224 | 2024-10-21 04:12:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a1470a91-6de1-3dcb-aabd-6e74777d6481 | -2.96783 | -47.99621 | 2024-10-21 04:12:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| eeb44208-659a-3331-a364-829899694ad5 | -2.96422 | -47.99154 | 2024-10-21 04:12:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c1918854-4b52-32a4-ad18-eac7e1d6850a | -2.96357 | -47.99553 | 2024-10-21 04:12:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0e0f05ca-25c3-3a48-a357-69889f1a708a | -2.96193 | -50.52296 | 2024-10-21 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0ef9dff9-d6bb-3c97-86f7-cf5f234fc421 | -2.96144 | -50.52591 | 2024-10-21 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a6241163-e28b-3c01-8c4e-4a28da346898 | -2.95997 | -47.99085 | 2024-10-21 04:12:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cb5342b4-1086-3309-b18a-0ef115c75975 | -2.95932 | -47.99482 | 2024-10-21 04:12:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9f3e4673-6bb3-31f1-9361-cd7c8a5571ca | -2.95838 | -47.36731 | 2024-10-21 04:12:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 53689c9b-f6b5-3a7a-b930-e3a3d5e3e65e | -2.95736 | -50.51921 | 2024-10-21 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 78ae1ec3-0498-3263-93f0-c65bf2370daf | -2.95687 | -50.52213 | 2024-10-21 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7164f3bf-4c46-3fe0-ab3c-4498f2ab7e07 | -2.95359 | -52.90787 | 2024-10-21 04:12:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d0407beb-3337-3ac4-93fc-d3348d3359d3 | -2.9529 | -52.91199 | 2024-10-21 04:12:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7c6cbf25-fa56-33fc-85b1-ccf4b39d743b | -2.95066 | -51.03987 | 2024-10-21 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2da2a4ab-aca2-3736-bec5-49b8b98eb455 | -2.94763 | -52.90702 | 2024-10-21 04:12:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2cc329e0-264a-329e-a2de-89aa3a135f1c | -2.94665 | -49.55873 | 2024-10-21 04:12:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e774a198-f6d0-39e6-a0bb-d0c517a05641 | -2.94583 | -49.56374 | 2024-10-21 04:12:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fe718f95-79d0-3238-9dd8-2995533f386b | -2.94542 | -51.03897 | 2024-10-21 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 95982167-8de0-3ddc-992e-9c2fcaf5b89d | -2.93396 | -49.343 | 2024-10-21 04:12:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 048729d3-fb90-3a87-a1f8-4923f7b7a160 | -2.90891 | -45.20719 | 2024-10-21 04:12:00 | NPP-375D | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 12.6 |
| eb274767-53b3-3d5f-b1ad-86cd0a6ab66a | -2.90825 | -45.2113 | 2024-10-21 04:12:00 | NPP-375D | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 12.6 |
| fbe50d24-0863-336b-a74a-167fde7d57f2 | -2.90596 | -45.20251 | 2024-10-21 04:12:00 | NPP-375D | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 06d7cff2-30be-3681-b86e-ce460d44d083 | -2.90531 | -45.20662 | 2024-10-21 04:12:00 | NPP-375D | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 5291f598-37bf-3ff9-9052-06d4f4004d71 | -2.90466 | -45.21072 | 2024-10-21 04:12:00 | NPP-375D | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 12.6 |
| ea2ec932-8888-3956-b76a-23cd54b888f3 | -2.904 | -45.21483 | 2024-10-21 04:12:00 | NPP-375D | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 7a90b843-fd77-30dd-a4b4-a34ce88046ee | -2.90237 | -45.20195 | 2024-10-21 04:12:00 | NPP-375D | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 320b6920-4dbd-3b43-9ce2-d6031f090f54 | -2.90171 | -45.20605 | 2024-10-21 04:12:00 | NPP-375D | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 8.2 |
| c5ff2387-d087-3b61-acc0-114586a8d272 | -2.90106 | -45.21015 | 2024-10-21 04:12:00 | NPP-375D | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 8.2 |
| d522466e-17d1-3fff-8d70-4ba7e257e505 | -2.89942 | -45.19727 | 2024-10-21 04:12:00 | NPP-375D | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 68c1cdaf-924a-371b-b8d9-50a8f152843f | -2.89877 | -45.20138 | 2024-10-21 04:12:00 | NPP-375D | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8d5369d2-4ba6-3384-a22a-07697a66eaad | -2.89811 | -45.20548 | 2024-10-21 04:12:00 | NPP-375D | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 38fe316d-fedf-3706-90d5-8086bfcf8261 | -2.89746 | -45.20959 | 2024-10-21 04:12:00 | NPP-375D | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 9d64b3c8-3cd5-3aa4-8628-b42c80793394 | -2.89583 | -45.19671 | 2024-10-21 04:12:00 | NPP-375D | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 157a37b4-455e-3ccf-8477-7c67bea6d09c | -2.89517 | -45.20081 | 2024-10-21 04:12:00 | NPP-375D | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ae6e31f4-a5b7-350c-bcf3-55384826876b | -2.89452 | -45.20491 | 2024-10-21 04:12:00 | NPP-375D | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f8415364-60ed-3228-ba23-df8e1fcaf75c | -2.86063 | -45.46394 | 2024-10-21 04:12:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 46ca2bef-0ae2-36d4-a7d3-9b52ab826f71 | -2.85996 | -45.46817 | 2024-10-21 04:12:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 11.0 |
| c702bd6b-7c5f-3fbc-ba22-6428ebf33bc2 | -2.85928 | -45.4724 | 2024-10-21 04:12:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2717fa7a-59e1-3d2e-b59f-3670f4bdf9ea | -2.85631 | -45.46758 | 2024-10-21 04:12:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 54c22717-317d-3e72-85e9-76347eda0621 | -2.85563 | -45.47182 | 2024-10-21 04:12:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e192ed33-c72c-393b-af4c-bba091d739f2 | -2.85527 | -51.28857 | 2024-10-21 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cadfa765-110e-36d8-8f69-28ee0718d54e | -2.85142 | -53.33434 | 2024-10-21 04:12:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d4152bb6-0fdc-3151-8cbf-27e2326f9745 | -2.85064 | -53.33898 | 2024-10-21 04:12:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0f444fcc-6e8f-3815-9077-4e76b436ad9a | -2.84992 | -51.2877 | 2024-10-21 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 28c3db09-49ec-354e-92b9-b1dcd8ed8903 | -2.84583 | -50.45919 | 2024-10-21 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c0bec294-84d2-3f31-b806-e681de75546a | -2.84536 | -50.46214 | 2024-10-21 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 485c4ee3-82a8-3108-9c9f-2936068879ab | -2.84531 | -53.33334 | 2024-10-21 04:12:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8cf8a753-b805-39d7-be18-18cef8219049 | -2.84495 | -50.45689 | 2024-10-21 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 410a268e-82ea-3853-bded-d9011c857794 | -2.84453 | -53.33796 | 2024-10-21 04:12:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e9b6e292-ee2b-3534-8dad-e5f06a376ee6 | -2.84445 | -50.45983 | 2024-10-21 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 01d55441-262c-30b2-a922-0c86c3533207 | -2.84395 | -50.46277 | 2024-10-21 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6cebea5b-334b-3206-8696-157e61ff7c32 | -2.84373 | -53.3427 | 2024-10-21 04:12:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4f37dfcd-e89b-3cb6-91cd-f4b892c45e1e | -2.84079 | -50.45832 | 2024-10-21 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e8d1804e-a0b2-3c1c-9aa4-34ffc92e7f70 | -2.84031 | -50.46125 | 2024-10-21 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ca92a75b-410a-3f7b-beed-f36e3d8a6faf | -2.83921 | -53.33231 | 2024-10-21 04:12:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fdde3d7e-cc38-3175-aa78-60710164b47b | -2.83843 | -53.33691 | 2024-10-21 04:12:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 67d711b2-b0f0-3f65-b6c1-08bc6d778f02 | -2.82442 | -53.00472 | 2024-10-21 04:12:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8e5804b6-4426-3230-8055-510902573896 | -2.82372 | -53.00893 | 2024-10-21 04:12:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9a62ae05-bf84-3520-837c-be9e48e4968f | -2.8184 | -51.34426 | 2024-10-21 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 57c342af-a4ce-37a2-b13c-882d1c83abd1 | -2.81783 | -51.34764 | 2024-10-21 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d80d9a62-3c33-3369-ae9d-d6d5926780ea | -2.81726 | -51.35102 | 2024-10-21 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f9fba978-9843-32ca-884d-3785ee6094f6 | -2.81635 | -51.34325 | 2024-10-21 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 93db7377-c615-3a01-8c16-a2917e3b4174 | -2.8158 | -51.34662 | 2024-10-21 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c2004f9f-3780-318d-99e9-9adb438036ff | -2.81526 | -51.35 | 2024-10-21 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9c3b5fcf-10f8-3638-bc2a-c67dd5b16a1d | -2.8136 | -51.34002 | 2024-10-21 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1863ef0e-aa61-3316-b346-5befc1064e1a | -2.81303 | -51.34338 | 2024-10-21 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 89ecacf3-7ea7-30e8-b2cf-47eaecb78006 | -2.81246 | -51.34676 | 2024-10-21 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cd294f7d-f3dd-3e5c-8a22-401bdb5b01d6 | -2.81189 | -51.35012 | 2024-10-21 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e58624ca-6850-33d6-86c3-ebdbe596cbc2 | -2.81132 | -51.3535 | 2024-10-21 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 72081342-7024-3df6-9386-b3341f925e21 | -2.81098 | -51.34236 | 2024-10-21 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6f8d6f55-38ba-3713-8f63-31caf5428390 | -2.81044 | -51.34573 | 2024-10-21 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e12da2f2-ac46-3122-8b49-6d5e0d2c3cc4 | -2.80989 | -51.3491 | 2024-10-21 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7a1bcb03-269c-33f5-89d2-1deb48be1bf6 | -2.80935 | -51.35247 | 2024-10-21 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a20e3fab-0d6e-3972-a3a0-a1264f6a5c4d | -2.80235 | -45.36053 | 2024-10-21 04:12:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 09ad41fb-7429-3ca1-b326-22a68c0f2c5b | -2.80233 | -51.36172 | 2024-10-21 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| a725294e-2d08-3c64-a8bf-b2b9cf56dd52 | -2.80178 | -51.36511 | 2024-10-21 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 9fc1b1b5-1a6f-3acb-a563-fe7fcaedbacf | -2.80123 | -51.36851 | 2024-10-21 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 874e86e4-e36a-3ee9-90a7-49e80c7c479f | -2.80028 | -48.67181 | 2024-10-21 04:12:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f49fa711-af9a-3a23-b8ac-5686f00d3e1a | -2.79943 | -51.35847 | 2024-10-21 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README30.md)
