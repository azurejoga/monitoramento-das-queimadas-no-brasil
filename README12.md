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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6a06327d-8940-3e57-b148-6714fa936c33 | -10.645 | -49.729 | 2026-05-29 13:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 103.7 |
| 380f60b7-0b30-3a12-b349-f3cd838e584e | -6.9982 | -42.878 | 2026-05-29 13:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 80.2 |
| d15ac3dd-a2fb-3ab2-9f04-10f70cd12c9e | -11.9493 | -43.4019 | 2026-05-29 13:30:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 125.7 |
| f0f7fb55-1b44-3180-b802-880271f65242 | -10.8192 | -46.9009 | 2026-05-29 13:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 2b615c35-c11c-3e21-8715-a2f19914058e | -8.8537 | -46.7228 | 2026-05-29 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 39cb2891-6b28-34fa-8404-451231c62a02 | -10.8188 | -46.9233 | 2026-05-29 13:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 94.3 |
| 7c59bc3d-b733-3e83-8d82-d958510e6dea | -8.8351 | -46.7024 | 2026-05-29 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 97.8 |
| 09a05153-52ab-3682-a78e-86028b05ab77 | -8.8348 | -46.7247 | 2026-05-29 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 116.0 |
| e487a2ab-7796-3df5-8c6c-f8590ce5f42c | -11.9493 | -43.4019 | 2026-05-29 13:40:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 160.2 |
| 66985978-de21-3f18-ab0f-5da69e20033d | -6.9982 | -42.878 | 2026-05-29 13:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 76.9 |
| 8395ab7d-59cb-377b-ad87-95d7889d6571 | -8.8537 | -46.7228 | 2026-05-29 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 5a7b5b41-f602-34fa-8848-d143eb4f90d9 | -10.645 | -49.729 | 2026-05-29 13:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 102.1 |
| 0ddc703d-1c85-35ef-a36d-1f63593e1f86 | -8.854 | -46.7005 | 2026-05-29 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 7b5768ac-bc83-3621-99e6-2855b707202e | -8.8351 | -46.7024 | 2026-05-29 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 144.3 |
| cb77a793-d4f5-3b83-9ded-938fbb2d6e54 | -8.8348 | -46.7247 | 2026-05-29 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 132.0 |
| 1354070b-9327-345d-a626-a3dfbcc9368e | -10.645 | -49.729 | 2026-05-29 13:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 107.0 |
| a453a21c-ed1e-3468-8f16-af84cd7438d7 | -8.8348 | -46.7247 | 2026-05-29 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 152.1 |
| 07cbecc0-b0fa-3fae-88fa-ffb37f233e79 | -8.8351 | -46.7024 | 2026-05-29 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 139.5 |
| a708fb17-7137-3168-a4ef-5f2c4093788b | -8.854 | -46.7005 | 2026-05-29 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 17635f22-8501-3811-8839-b40cec4f714a | -11.9493 | -43.4019 | 2026-05-29 13:50:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 193.6 |
| da6e5d6c-be4c-3c96-ab13-74d3e72cd2b2 | -8.8537 | -46.7228 | 2026-05-29 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 6c7823c3-d302-30ac-b199-1f1488ecf4b0 | -10.8192 | -46.9009 | 2026-05-29 13:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 94.2 |
| 5372c30a-8d1b-3d08-9869-0dcc96614b5c | -10.8382 | -46.8985 | 2026-05-29 13:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 2321747c-4d9f-38b4-b3c8-9bf8abab7216 | -8.8351 | -46.7024 | 2026-05-29 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 170.1 |
| 855244d1-1ab9-38fc-9daa-b24bf25ac37a | -8.854 | -46.7005 | 2026-05-29 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 4fdead30-231a-3255-8778-35e55303fa4e | -11.9493 | -43.4019 | 2026-05-29 14:00:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 159.5 |
| 3e2f993e-8f2e-3169-9f53-068da56f6708 | -10.645 | -49.729 | 2026-05-29 14:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 106.6 |
| cb39dc59-9824-378a-a77e-234fc648fce4 | -6.9982 | -42.878 | 2026-05-29 14:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 87.0 |
| fcc1d684-eb8e-3bb0-9698-20cb1aa85bfc | -8.8537 | -46.7228 | 2026-05-29 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 67.7 |
| b613fe51-3aee-38e1-a07c-8b692a65186c | -8.8348 | -46.7247 | 2026-05-29 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 186.5 |
| 3b8fbd6b-030d-355f-9232-2ce0d8609d00 | -8.8351 | -46.7024 | 2026-05-29 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 198.7 |
| 5f8b0541-d606-3f96-8a10-ac6fa17b5d8e | -10.645 | -49.729 | 2026-05-29 14:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 104.6 |
| afdb2bf0-45ac-38ba-93c6-5617f3ccb757 | -11.9493 | -43.4019 | 2026-05-29 14:10:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 163.8 |
| 558ffd64-0a4f-3263-8fe9-5a3b10325d30 | -8.854 | -46.7005 | 2026-05-29 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 109.4 |
| c4d2a820-8505-3818-8f92-bd47e7a4da19 | -8.8348 | -46.7247 | 2026-05-29 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 178.2 |
| f4eaeecb-94e7-3934-a533-755a26f8f3e7 | -6.9982 | -42.878 | 2026-05-29 14:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 85.6 |
| 92ffcf2b-03e4-3587-a632-a587a7ed696b | -8.8537 | -46.7228 | 2026-05-29 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 90.3 |
| 15cfed0e-e923-3e8b-b6f7-f7ce1b57a4e0 | -8.854 | -46.7005 | 2026-05-29 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 126.8 |
| 0390f3ea-28fa-3c5b-b4f7-58845615a01d | -8.8351 | -46.7024 | 2026-05-29 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 130.6 |
| d97497c3-1742-3efe-b5a9-1b1317f6bab8 | -8.8537 | -46.7228 | 2026-05-29 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 135.1 |
| 6cb135ba-f600-3031-bad5-d81e8ff0d755 | -11.9493 | -43.4019 | 2026-05-29 14:20:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 146.9 |
| 9b3cc5d7-c434-3114-9a61-1ba151090cd7 | -10.8192 | -46.9009 | 2026-05-29 14:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 87.1 |
| 10f7f0e6-deb4-3a1b-b398-90ee075e647b | -10.645 | -49.729 | 2026-05-29 14:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 103.8 |
| 0c897566-e9db-3d65-8aaa-c873af138ef0 | -10.8382 | -46.8985 | 2026-05-29 14:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 41918243-f70a-33d7-896a-94bbd6f8c32d | -6.9982 | -42.878 | 2026-05-29 14:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 90.3 |
| 3cc7efe0-8f01-315c-8444-98f05a91c70c | -8.8348 | -46.7247 | 2026-05-29 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 146.1 |
| 81f4d19b-f1ec-31c9-9eb1-2b9f690e9c29 | -11.9493 | -43.4019 | 2026-05-29 14:30:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 130.5 |
| 7646b0f0-03b8-3fd7-a474-783539bb4f79 | -10.8188 | -46.9233 | 2026-05-29 14:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 97.6 |
| 3cfbf621-03da-3f25-bd22-e6cc87140f70 | -10.8382 | -46.8985 | 2026-05-29 14:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 133.5 |
| 407255d9-9134-3e84-94e5-91125c032a34 | -10.8192 | -46.9009 | 2026-05-29 14:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 96.6 |
| ce7ef779-0969-34fe-89c9-e0f95bf0e231 | -10.645 | -49.729 | 2026-05-29 14:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 96.0 |
| ecd7e7db-779f-3012-a38d-0028467f0f7b | -8.8351 | -46.7024 | 2026-05-29 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 142.3 |
| 94c1af07-03a5-3fe3-baeb-8e4915d43a62 | -8.8348 | -46.7247 | 2026-05-29 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 136.7 |
| bd49664d-add3-3487-ab98-57e6d08f7f8a | -8.8537 | -46.7228 | 2026-05-29 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 111.6 |
| 9c144894-2239-3cda-a48f-1376b6032ede | -10.8379 | -46.921 | 2026-05-29 14:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 136.7 |
| ea71de14-f95c-3dcf-ab84-f986f8175364 | -10.8382 | -46.8985 | 2026-05-29 14:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 150.5 |
| 981a8e0f-e1e7-33d4-94a6-52034e4c3ebc | -10.8188 | -46.9233 | 2026-05-29 14:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 203.4 |
| 96e60d5d-b7bd-3847-956c-7d69c4828358 | -8.8351 | -46.7024 | 2026-05-29 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 101.2 |
| f2116802-4dc1-31d3-9852-514e477964b2 | -10.8192 | -46.9009 | 2026-05-29 14:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 165.4 |
| fb6942ca-2e05-3f35-ae89-6143596b2ad7 | -10.645 | -49.729 | 2026-05-29 14:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 93.8 |
| 4d2c84de-686a-3de0-addd-c96afce8c4c6 | -11.9493 | -43.4019 | 2026-05-29 14:40:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 118.5 |
| d040e4ea-d861-3afb-a974-9d83e3680db9 | -10.8379 | -46.921 | 2026-05-29 14:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 140.9 |
| d2249958-33f2-30c1-8cac-d6a16e0c82d4 | -10.6642 | -49.7054 | 2026-05-29 14:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 757ebd97-2b1b-36d1-9dc7-2cd8c762f0a3 | -8.8348 | -46.7247 | 2026-05-29 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 120.6 |
| 12eeefa4-185a-3b4f-aefd-b54df09145d9 | -8.8537 | -46.7228 | 2026-05-29 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 107.9 |
| 3dd5a9d9-a7d1-352f-831c-ae1e25dba95c | -10.8188 | -46.9233 | 2026-05-29 14:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 159.8 |
| eee22c07-7c71-3105-8fe5-34fd0e75dd1c | -10.645 | -49.729 | 2026-05-29 14:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 102.0 |
| bbe23a70-e0a5-3f3e-987f-124da470e100 | -8.8537 | -46.7228 | 2026-05-29 14:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 73.6 |
| b6818674-02cf-3898-96a6-de275db55a8a | -10.8379 | -46.921 | 2026-05-29 14:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 135.4 |
| 1c43c9f7-c508-3fe6-b9f5-193b493f260a | -8.8351 | -46.7024 | 2026-05-29 14:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 113.2 |
| 160ae4eb-514d-329b-ae04-f16a3a1adda5 | -10.8192 | -46.9009 | 2026-05-29 14:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 143.1 |
| fba59ad8-d2e3-30f2-9b14-c6bbbb215066 | -11.9493 | -43.4019 | 2026-05-29 14:50:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 119.9 |
| 45209b5c-6882-31c0-a079-db31a041d17a | -8.8348 | -46.7247 | 2026-05-29 14:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 96.3 |
| 07fc0146-3f86-3c84-b54d-ab88110cdc23 | -10.8382 | -46.8985 | 2026-05-29 14:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 583e1623-124a-341a-b0b6-4bd15181a873 | -10.8188 | -46.9233 | 2026-05-29 15:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 117.5 |
| 51d14d74-e64e-3fa5-bacf-a0a4f548420f | -10.8192 | -46.9009 | 2026-05-29 15:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 114.7 |
| 5ef531be-85cc-353d-9f2e-ec1a8ebba889 | -10.756 | -49.9105 | 2026-05-29 15:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 113.9 |
| 372f3702-7eee-307d-9dc0-47983de2808a | -8.8348 | -46.7247 | 2026-05-29 15:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 106.2 |
| 72edc6f6-08de-36b4-ba9b-e2fbd2d44959 | -10.737 | -49.9126 | 2026-05-29 15:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 92.2 |
| a0d712e4-5310-3ca8-9e00-ba23368b7658 | -8.8351 | -46.7024 | 2026-05-29 15:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 100.2 |
| 992393f0-0cb8-3945-8f78-9f5e641e3213 | -10.8379 | -46.921 | 2026-05-29 15:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 62076741-6d2e-3425-9773-a9529e075710 | -8.8348 | -46.7247 | 2026-05-29 15:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 75.2 |
| dde0098c-881e-32e8-aeb1-ac5626290f51 | -10.1031 | -46.5623 | 2026-05-29 15:10:00 | GOES-19 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 18db4c1b-f9e1-36ad-84bb-3b3eb1d87488 | -8.8351 | -46.7024 | 2026-05-29 15:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 97b93d15-c9f0-3bfb-84c1-70df7cfb0908 | -8.8537 | -46.7228 | 2026-05-29 15:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 66.4 |
| b60310a2-c243-38af-8eab-eca81b8cfdc1 | -10.645 | -49.729 | 2026-05-29 15:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 113.9 |
| 53ecfb83-7228-3477-b7c4-ca87cad4cfd7 | -10.8188 | -46.9233 | 2026-05-29 15:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 122.8 |
| 9cce7fff-5809-30b0-a90a-8d4b3063528d | -10.8192 | -46.9009 | 2026-05-29 15:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 100.5 |
| 780f9f1c-e90b-3d05-a688-991240f7675c | -10.737 | -49.9126 | 2026-05-29 15:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 17b68218-8a5d-3376-8cec-f859ddb16751 | -7.03073 | -38.81156 | 2026-05-29 15:16:00 | NOAA-21 | BARRO | CEARÁ | Brasil | 2302008 | 23 | 33 | nan | nan | nan | Caatinga | 6.6 |
| a4dd4fd7-b043-3c0b-aa26-9991cb75d416 | -9.38728 | -37.81091 | 2026-05-29 15:16:00 | NOAA-21 | OLHO D'ÁGUA DO CASADO | ALAGOAS | Brasil | 2705804 | 27 | 33 | nan | nan | nan | Caatinga | 15.2 |
| b8d6d427-24fd-3ad0-af4a-8d88797a5eb8 | -11.41792 | -37.81725 | 2026-05-29 15:16:00 | NOAA-21 | TOMAR DO GERU | SERGIPE | Brasil | 2807501 | 28 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| f74a667a-095e-399b-a3e3-d4550b8f64a5 | -8.6053 | -37.69649 | 2026-05-29 15:16:00 | NOAA-21 | IBIMIRIM | PERNAMBUCO | Brasil | 2606606 | 26 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 0ff9c0dc-2b7a-3c04-9fdd-826539da3d06 | -8.30586 | -39.38206 | 2026-05-29 15:16:00 | NOAA-21 | CABROBÓ | PERNAMBUCO | Brasil | 2603009 | 26 | 33 | nan | nan | nan | Caatinga | 20.1 |
| b4ca46bf-f83d-391e-bece-70ec22c8f22f | -8.60673 | -37.69591 | 2026-05-29 15:16:00 | NOAA-21 | IBIMIRIM | PERNAMBUCO | Brasil | 2606606 | 26 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 008fb957-3427-322a-8f17-3d4d24c3a608 | -8.8351 | -46.7024 | 2026-05-29 15:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 47ad3013-0c0d-3af9-ac38-5b7355e64914 | -8.8348 | -46.7247 | 2026-05-29 15:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 02d73a13-928c-3cd8-99f5-90340898e3a4 | -6.823 | -43.4104 | 2026-05-29 15:20:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 69.5 |
| aeefd956-ef51-3ed9-81cd-afa95a8e4319 | -10.737 | -49.9126 | 2026-05-29 15:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 109.4 |
| d6f0e2e2-af5a-3407-a708-98de281f6407 | -10.645 | -49.729 | 2026-05-29 15:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 99.1 |


[Clique aqui para ver as próximas entradas](README13.md)
