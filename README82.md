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

## Dados Diários - Página 82

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d359ee80-ae4b-390e-8c87-2e6073bd841a | -11.0485 | -45.6511 | 2026-10-06 13:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 313.8 |
| 8f9b1802-a807-3e37-af0f-8b1c7787f95a | -11.6946 | -43.6787 | 2026-10-06 13:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 128.8 |
| 260df4b1-9dab-3089-8b3f-b7b81663030b | -7.8496 | -44.1478 | 2026-10-06 13:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 111.9 |
| 15b94fd5-7d10-323d-8b10-818d5e2ee42a | -10.9758 | -45.4324 | 2026-10-06 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 181.1 |
| 256928ff-c94f-3739-adbd-51a9259926ce | -9.1519 | -65.8994 | 2026-10-06 13:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 61.3 |
| ff88d135-ceb8-317a-86d2-557c02c1a0ea | -7.8684 | -44.1459 | 2026-10-06 13:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 64.9 |
| abcf5269-387b-3aed-b71e-faf7d249d9bd | -11.6946 | -43.6787 | 2026-10-06 13:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 129.0 |
| 73797e2b-271c-3f67-98c2-dc06ea9ee32f | -11.6575 | -43.6136 | 2026-10-06 13:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 212.0 |
| dabfbac2-9b18-386a-8869-4e33f99974f5 | 3.055 | -60.5952 | 2026-10-06 13:30:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 105.8 |
| 4a7f71f6-4c43-38a3-a8c1-9a39f4d14a95 | -7.8682 | -44.169 | 2026-10-06 13:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 136.0 |
| 57674cb8-a2b7-3cea-a830-f3e4d0e0b14b | -11.6951 | -43.655 | 2026-10-06 13:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 122.1 |
| 52410188-64b9-3ee3-a8a8-218c601d4919 | 3.0733 | -60.576 | 2026-10-06 13:30:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 3fa41a62-259c-39fe-83ad-bc1fcb4ccbb8 | -11.657 | -43.6373 | 2026-10-06 13:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 203.4 |
| 1ce135bd-40e6-32f5-86fc-2417ceeba946 | 1.8038 | -55.5458 | 2026-10-06 13:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 3b182d2d-0d95-33d5-b1df-3dd4f14d6fb2 | -7.2077 | -44.3255 | 2026-10-06 13:30:00 | GOES-19 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 112.5 |
| eb51d80d-9e81-341f-ab21-95b242d0df75 | -7.2079 | -44.3024 | 2026-10-06 13:30:00 | GOES-19 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 103.3 |
| 0a3591fa-c0a4-3fb5-9cc3-7e032dfecaba | -11.6763 | -43.6343 | 2026-10-06 13:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 142.6 |
| d56dcd0a-ba81-3269-a5ba-65f4115f0283 | -11.0485 | -45.6511 | 2026-10-06 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 156.2 |
| e2064d90-f20d-3a5d-98c8-acae3104da3b | -11.8315 | -43.5391 | 2026-10-06 13:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 124.0 |
| 3541eabf-cc08-33d8-9929-23335bb3d1f1 | -10.9762 | -45.4094 | 2026-10-06 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 183.8 |
| 01e10b2d-3c99-35f5-beb1-b6aca273a4a8 | -10.491 | -47.2533 | 2026-10-06 13:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 87.5 |
| d1c3da68-728c-36cf-ba55-7763cd3a9698 | 3.0732 | -60.5949 | 2026-10-06 13:30:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 1fdc2671-f8a8-3ccb-b301-eede254cd455 | 1.7304 | -55.6259 | 2026-10-06 13:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 139433fd-6434-383a-a610-e38c12ea24e6 | -7.8682 | -44.169 | 2026-10-06 13:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 181.8 |
| 95d5178e-de03-32a5-a2cf-904052fba719 | -11.6951 | -43.655 | 2026-10-06 13:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 144.3 |
| 3516cd6d-b45d-38bf-b70c-fcc69e07d0d1 | -9.8071 | -44.7804 | 2026-10-06 13:40:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 90.8 |
| 6c16d88d-d256-3926-a147-033381ec8dec | -6.8957 | -43.6368 | 2026-10-06 13:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 170.5 |
| 8af87e6c-3d45-34ed-8534-2feda3c9ac98 | -11.0485 | -45.6511 | 2026-10-06 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 150.2 |
| 21e3bcff-b0ee-306a-ae5e-2c3bb4af31b8 | -11.657 | -43.6373 | 2026-10-06 13:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 141.2 |
| edbb111c-9542-3293-8e80-cebe93ed1d91 | -9.1519 | -65.8994 | 2026-10-06 13:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 79.7 |
| ccf78a77-7533-361b-bcb5-fcb27abb756c | 3.055 | -60.5952 | 2026-10-06 13:40:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 5fb80fca-f051-36cc-a13f-f7935689862e | -7.4001 | -45.6072 | 2026-10-06 13:40:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 110.0 |
| ee813132-dea7-3926-a92b-df687ff2d5dd | -11.8315 | -43.5391 | 2026-10-06 13:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 144.2 |
| c62e552a-e755-3e93-8210-61343eee674e | 1.7855 | -55.5461 | 2026-10-06 13:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 362cd9d6-50c1-3696-a1fd-677e96e74846 | -7.8496 | -44.1478 | 2026-10-06 13:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 142.5 |
| 0e9cb8b8-4518-365e-b4ce-3d210c0c7a51 | -7.2077 | -44.3255 | 2026-10-06 13:40:00 | GOES-19 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 89.4 |
| 963dc7e3-53cf-3f04-ab0c-e46d4dfd364f | -7.2079 | -44.3024 | 2026-10-06 13:40:00 | GOES-19 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 93.9 |
| cb0702c7-7687-3f45-aeda-1dde5375f811 | -10.491 | -47.2533 | 2026-10-06 13:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 84.8 |
| db331b34-b710-32f5-af99-aaa771f7f39e | -11.6946 | -43.6787 | 2026-10-06 13:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 116.7 |
| 48c8765b-d5a9-3715-a0ae-0934e966b884 | -7.8684 | -44.1459 | 2026-10-06 13:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 89.9 |
| b3a2de2a-ac44-349b-8a1c-de10a1e0614d | 1.8038 | -55.5458 | 2026-10-06 13:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 36b2d63b-429e-38aa-a664-807dea65d35f | -11.8296 | -44.688 | 2026-10-06 13:40:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 112.0 |
| a451728f-9692-3b95-b3a2-e41dbbe1fd71 | -9.1334 | -65.9 | 2026-10-06 13:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 57.5 |
| eb48bd98-e9ae-3a91-8f1d-2260114322d5 | 1.7304 | -55.6259 | 2026-10-06 13:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 791ebf79-7bfd-38ec-aa3c-b282e6380df2 | 3.0733 | -60.576 | 2026-10-06 13:40:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 2819f317-fb30-34f6-92dc-ce7de5e1bff4 | -10.7493 | -45.3024 | 2026-10-06 13:40:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 135.0 |
| f942bc43-d42a-32e9-8785-83854283b225 | 1.7854 | -55.5658 | 2026-10-06 13:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 09b637da-7f53-39aa-9b4e-ad54949c9bac | -9.8828 | -44.794 | 2026-10-06 13:40:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 91.3 |
| b619d4ff-963b-34d8-8e7b-cedc8ae7d936 | -10.9758 | -45.4324 | 2026-10-06 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 155.9 |
| 8cd06a73-bf21-3550-8311-ff97f10b9d2b | -10.9762 | -45.4094 | 2026-10-06 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 122.7 |
| 47bcfa89-b8d6-3636-b5c9-3a070060040d | -11.6575 | -43.6136 | 2026-10-06 13:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 189.9 |
| 2e5633a1-3a15-381b-802a-8371f493d7d8 | -7.2079 | -44.3024 | 2026-10-06 13:50:00 | GOES-19 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 2bed08fe-8ac3-3aae-9426-01addd90985b | -7.8496 | -44.1478 | 2026-10-06 13:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 134.4 |
| 30dd3ce7-81bf-331c-8e6f-a9f645327179 | 1.4922 | -55.688 | 2026-10-06 13:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 69.6 |
| b9dd373e-d9f8-3392-a8fe-cd8ad9085719 | 3.1281 | -60.575 | 2026-10-06 13:50:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 75f71191-5852-3e13-8b39-1a8001e90f97 | -6.7228 | -44.0001 | 2026-10-06 13:50:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 92.2 |
| 73f99daf-4d9a-3beb-ae16-8d5e0814a398 | -10.9946 | -45.4527 | 2026-10-06 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 81.1 |
| a36de7b7-29ee-361d-a53f-a170c4b8b1d6 | -7.4001 | -45.6072 | 2026-10-06 13:50:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 161.0 |
| ea191eef-5a11-3248-897e-16455f833a7e | -11.1197 | -45.9602 | 2026-10-06 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 58.3 |
| cbb65631-cb97-3a37-b055-f3ddd4a87d83 | -11.6763 | -43.6343 | 2026-10-06 13:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 155.7 |
| 11131b20-db2b-3cb8-91bc-288dfb439686 | 1.7855 | -55.5461 | 2026-10-06 13:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 67.1 |
| c06d2c4d-e815-354d-8bab-fbe241358c54 | -7.4889 | -42.8059 | 2026-10-06 13:50:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 67.4 |
| d9c2687f-9923-3aef-8a87-6f7c88e6686f | -11.8315 | -43.5391 | 2026-10-06 13:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 159.1 |
| 4663ed6f-89a9-33f6-b1f5-99bab658a4cf | 3.0733 | -60.576 | 2026-10-06 13:50:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 67.2 |
| e8646a35-2ad6-3d12-bced-6dc0b1ba598e | -6.8957 | -43.6368 | 2026-10-06 13:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 194.2 |
| 494f74e0-ab8f-3ffe-8dea-dde6e786d930 | -9.7312 | -65.0944 | 2026-10-06 13:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 55294830-c2c3-3258-865b-8ddf639724b3 | -10.9762 | -45.4094 | 2026-10-06 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 229.2 |
| 72bf49b3-6604-34dc-93f5-8a0b363754c9 | -10.9755 | -45.4553 | 2026-10-06 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 93.5 |
| 88324037-91f1-3b0f-9aa1-556568d1378b | -10.9758 | -45.4324 | 2026-10-06 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 368.5 |
| d6e6e38c-cb97-325b-a4c3-a54e5cacdc52 | 1.7671 | -55.5859 | 2026-10-06 13:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 75c27865-33b8-331c-bb79-776f93cf608a | 3.0732 | -60.5949 | 2026-10-06 13:50:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 0236dd8a-8800-3bca-9c08-ddf10dd368e7 | -9.8071 | -44.7804 | 2026-10-06 13:50:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 95.1 |
| 0c038abb-3180-3967-9629-c0191256c1cb | -11.657 | -43.6373 | 2026-10-06 13:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 220.4 |
| 71fe6f1f-6351-3a58-b523-1176e19b2c98 | -10.491 | -47.2533 | 2026-10-06 13:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 61.0 |
| 984dc6d1-4259-3b68-a0b8-91833e91b442 | -11.0856 | -45.7145 | 2026-10-06 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 286.5 |
| 8168e3c9-a2f8-3b2b-90de-f9adfb3458e0 | 1.7854 | -55.5856 | 2026-10-06 13:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 97.0 |
| 6f3918a7-be14-31e6-b085-a44f10d0cdd8 | 1.8038 | -55.5458 | 2026-10-06 13:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 69267cc0-6fd4-33f3-89d3-5eef274cb39c | -7.2077 | -44.3255 | 2026-10-06 13:50:00 | GOES-19 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 87.4 |
| b7b0e073-cd8d-33e3-ad56-368803545939 | -7.8682 | -44.169 | 2026-10-06 13:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 154.4 |
| 5bb6a4e4-274e-3971-867c-72a2fa3c4050 | 1.7854 | -55.5658 | 2026-10-06 13:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 122.4 |
| 13e6ef33-0ed5-35d6-8ac2-1069105756b0 | 1.7671 | -55.5859 | 2026-10-06 14:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 8f8aeb5a-3896-3e19-baa8-574867a77949 | -6.8957 | -43.6368 | 2026-10-06 14:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 168.7 |
| 8eaa6bc8-6c07-3992-8d58-7dd99590197b | -11.8315 | -43.5391 | 2026-10-06 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 157.6 |
| 4f4dd726-b8bd-320f-88af-1cb73fc21219 | -10.9762 | -45.4094 | 2026-10-06 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 306.6 |
| e7c0828c-a0a6-36a0-9c5c-9f6efafd9554 | 1.7854 | -55.5658 | 2026-10-06 14:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 187.6 |
| bff94fcd-73d8-3de7-b5b6-c96298d7e8a3 | -7.8496 | -44.1478 | 2026-10-06 14:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 119.0 |
| 9000da50-825c-344c-8b63-ba9497e347c9 | -7.4889 | -42.8059 | 2026-10-06 14:00:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 64.0 |
| 55238285-c326-3cb1-b739-6f7d3d725eb6 | -6.3623 | -42.5349 | 2026-10-06 14:00:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 65.0 |
| 9d941ba0-6f1c-3124-8fd7-b96f864d8680 | 3.0732 | -60.5949 | 2026-10-06 14:00:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 85a9d680-69b4-3f9e-bc0e-9ecd970f8d5c | -10.9946 | -45.4527 | 2026-10-06 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 73.9 |
| c1ba7a6c-355c-31f1-a10e-3d4d83343c21 | -11.6575 | -43.6136 | 2026-10-06 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 160.7 |
| 40f59241-7c6f-3237-a485-8a3172e898bc | -7.8684 | -44.1459 | 2026-10-06 14:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 86.1 |
| a60ed830-77ef-3a76-8b64-3e6f1a00f779 | -10.9755 | -45.4553 | 2026-10-06 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 147.1 |
| b926f621-ecc8-3384-b4e0-cff638f2baca | -11.6946 | -43.6787 | 2026-10-06 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 172.8 |
| 51dd15ec-01f5-3cb1-adb9-2ddaf3efbc71 | -10.9758 | -45.4324 | 2026-10-06 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 542.2 |
| c1189f83-8daa-387d-9033-debba7a677a3 | 1.7855 | -55.5461 | 2026-10-06 14:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 78.9 |
| 82a5102b-eeed-388a-aa9d-c2518c339971 | 3.1281 | -60.575 | 2026-10-06 14:00:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 56.5 |
| d95173f5-c6c2-3635-bdf6-af44ff5b37c5 | -7.2077 | -44.3255 | 2026-10-06 14:00:00 | GOES-19 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 92.0 |
| 11b2576d-22c9-3b54-a2b9-7b84b2f1e13a | 1.4922 | -55.688 | 2026-10-06 14:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 117.9 |
| 36d39dab-1fa3-3867-a7ef-5c271fb8b272 | -11.6763 | -43.6343 | 2026-10-06 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 153.5 |


[Clique aqui para ver as próximas entradas](README83.md)
