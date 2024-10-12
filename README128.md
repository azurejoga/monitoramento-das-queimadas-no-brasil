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

## Dados Diários - Página 128

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4eee1d2e-36ec-39e7-a7c5-35891f6c7da0 | -10.16846 | -60.89561 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a45aa2a5-724f-3704-979c-724f46e0d1c8 | -10.16791 | -60.89911 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 674fa055-c0c5-33f7-8896-8cc4c90af874 | -10.16737 | -60.90263 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 58ec2a8d-b475-3002-a6f2-ca34972e1756 | -10.06207 | -61.12245 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| eb9d25da-3819-3100-ac4c-e3c96435de14 | -10.06151 | -61.12595 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 94f983fd-8748-3b73-b9db-60d276a7d3a7 | -10.06039 | -61.1114 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0a662cf2-817a-3742-be49-6cc499081459 | -10.05929 | -61.11841 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a178028a-84ed-3cd1-86fb-8f996423cf78 | -10.05874 | -61.12191 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 92ce10c7-4a1f-3cb8-8e2c-7072cbb5861c | -10.05707 | -61.11088 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2de53d2f-01f9-32e1-bf70-be4485dc2196 | -10.05652 | -61.11438 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 82559b24-3fe2-3357-8a1d-7cdd0deeaa82 | -10.05597 | -61.11788 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b1deacca-d633-3f3c-82fc-b12c627c79b4 | -10.05542 | -61.12138 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a834c259-a134-3984-bb88-a58ad77219cd | -10.05264 | -61.11734 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2c7c036a-f24f-3ae4-aebc-0bb64a0b0d43 | -10.75249 | -60.74935 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 659dd88f-be87-3b5d-a0da-381d06c80251 | -10.75025 | -60.74174 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a7e86155-d8f2-370f-ac0c-edf207cb72e0 | -10.7497 | -60.74528 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e3eb42c8-8089-3112-abc2-70f45ea8a71f | -10.74915 | -60.74882 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 325702bc-d925-301b-b6af-757dc743be83 | -10.74861 | -60.75237 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 737b44e6-4f08-3b36-bc52-1d0633b77f19 | -10.74691 | -60.74121 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 06995f48-d4cf-3e7b-bb0b-6c30d81e7748 | -10.74637 | -60.74476 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 67fc23c7-7e3d-3cbe-a979-720938afc78a | -10.74582 | -60.74829 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4fc0466f-0566-393d-b500-e9e5d492fda5 | -10.47172 | -61.24915 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 25cf8931-270b-3f15-aadd-6cdb852a52c8 | -10.46839 | -61.24862 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| fb356475-1fb7-3da7-8f15-c95fb571f848 | -10.40673 | -61.23536 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 170d16bf-0631-39b6-b884-ef08c8229b7c | -10.40618 | -61.23887 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 486ad85d-fade-3718-966c-fc72c0401510 | -10.40396 | -61.23132 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0e98b821-570b-33d0-97cd-b47f533a6e92 | -10.40341 | -61.23483 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8b742bba-f056-3287-b529-adc435767681 | -10.40286 | -61.23833 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b38f3b14-a221-3649-9482-104aa4b78de6 | -10.40284 | -61.21677 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b28eb339-c431-332a-9c57-cc478eba51ce | -10.40008 | -61.2343 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f608e828-f1e4-3d40-b8b3-8c59ca03335a | -10.40006 | -61.21273 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9a1c236a-5d09-35dd-8986-0432a1b80292 | -10.39953 | -61.2378 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 46bf0d8b-295c-3406-bae3-34e55c065a5a | -10.39951 | -61.21623 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 54999365-85c0-349d-8642-390b98a32ab9 | -10.39619 | -61.2157 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9fadfd16-6aa8-3666-9622-06c0f7c65c95 | -10.38842 | -61.20008 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 188b23a5-7b8e-36e5-bfe2-fc06a965556b | -10.38787 | -61.20358 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 479201dc-71c0-37d2-aaa8-3c7d7325dc44 | -10.38677 | -61.2106 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b3ae34ed-7f53-3e42-b9ea-1d131b06c378 | -10.3851 | -61.19955 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c19b4322-dcee-3250-8b4e-0446995be8aa | -10.38454 | -61.20305 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f70497a8-faa0-3348-b880-f7e5c0146fee | -10.38399 | -61.20655 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 194da25d-c806-3088-a7bd-051dcd5bfa4a | -10.38346 | -61.23163 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 266893f6-38d2-3ec3-b9f8-9101ad4312d2 | -10.38344 | -61.21006 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ff43bf8c-98db-315c-9db7-815c8e18b1d1 | -10.38291 | -61.23514 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c2b7eb34-c6bb-3644-b579-23d48a066f51 | -10.38232 | -61.1955 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d894aaae-090f-3b49-b550-167978dfd31a | -10.38177 | -61.19901 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7a901d7c-8bc8-3eba-adbb-5e701439813c | -10.38122 | -61.20252 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7a526a81-93cc-3196-bc8c-c836d963c05b | -10.38067 | -61.20602 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 159d6586-28dd-3c2f-9ba3-6900b2a57fcf | -10.38014 | -61.23109 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a4ad1592-1838-3f97-8fa5-94afe6ba790e | -10.37959 | -61.23461 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c996d196-9ae6-3a49-bfe2-4f1e51269287 | -10.37904 | -61.23811 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a9f1b014-0f50-3369-80ce-e84422cb2f70 | -10.37848 | -61.24162 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 065525d2-22f2-33a8-93f9-0007a68eccc9 | -10.37793 | -61.24512 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 36300cfa-1327-34d7-b9cf-0299e6446446 | -10.37735 | -61.20549 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a7b7bfb6-79d4-3391-89e1-75a3d7dee21a | -10.37681 | -61.23056 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5271582c-0c0e-3dd1-b7e8-b30e8ba3527e | -10.37626 | -61.23407 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 37f9ceb8-d140-3dc8-a7d2-d7a79995b9e8 | -10.37571 | -61.23758 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5b98cf80-6609-3401-9a5a-45aa20d92e27 | -10.37516 | -61.24108 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 27fa6e05-2842-33d9-a3c1-b342c0069d37 | -10.3751 | -61.17637 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8ee59d5f-6ddf-3736-a056-643cf640bca8 | -10.37349 | -61.23003 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6c2a4984-4b2b-3eab-b53a-df4e0e8049d5 | -10.37294 | -61.23354 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d645230e-d2ff-38e5-b7a6-d3640f1be443 | -10.37239 | -61.23705 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 62a18808-1f65-31ae-89b0-6f08bd03bde2 | -10.37233 | -61.17233 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 61c36035-e481-3be9-a825-6f7de51347ea | -10.37184 | -61.24055 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e74cd651-75d9-30ce-82f0-fa105aaa3699 | -10.37178 | -61.17584 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 04473d4b-b404-3ff9-94c2-45be197c57d1 | -10.37016 | -61.2295 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f3961265-c34f-34c1-b62c-bad1b7c385a9 | -10.36961 | -61.23301 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a6636496-c59e-37af-bdc7-f5689fefa891 | -10.36906 | -61.23651 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 56279b44-b786-35bd-80b0-7ce6b2aa4b32 | -10.369 | -61.17179 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 236b9ebb-1e36-3e61-81ac-ed7a25041c4e | -10.36845 | -61.17531 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4312c840-0ab1-3270-8b68-9136558c9e63 | -10.36574 | -61.23598 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 097fc816-f238-39a5-9091-7fefdee34efd | -10.36409 | -61.2465 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2b591429-5596-302b-b163-d83c05c71a5e | -10.36241 | -61.23545 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7e0b0558-e1d6-3fd3-9d48-cd9b641b60bd | -10.36186 | -61.23895 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| df719367-8ab0-36e9-b405-5a51836513be | -10.36131 | -61.24246 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 29cd0357-e7b6-30c3-8e55-5c16cbb219d4 | -10.36076 | -61.24596 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 444bc8e8-f6f2-3481-8711-f90286311962 | -10.35854 | -61.23842 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b32264b7-2cfb-35be-a4ce-e0e3a6150ed2 | -10.47117 | -61.25266 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1836beeb-81c3-3c2d-a1d9-98e4c183f7cb | -10.46784 | -61.25212 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| fe5e2355-d130-3529-8000-009e922a2ba5 | -10.42298 | -61.25571 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7cfad46f-efae-3d3f-8caf-c3471554eebb | -10.42243 | -61.25922 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8222aa2f-fb4e-30e4-a355-ee26b515826a | -10.41965 | -61.25518 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b0ce3e9a-83b1-32e7-a8e9-5c851bdc710b | -10.4191 | -61.25868 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| afdc8ad6-3b72-3d29-b854-98ea6ab86a52 | -10.41855 | -61.26219 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6a4eaca0-562b-38ca-aa62-271dfd1b8fa4 | -10.41284 | -61.26151 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a75ccf53-1f8c-333c-bf6e-55cfb42aa6ef | -10.41064 | -61.27554 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 47535bde-f3d2-3e42-8068-314516c87908 | -10.40787 | -61.2715 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 51738e6e-15bf-307c-a36d-c4547bdfb80f | -10.40731 | -61.27501 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 99182ca7-ded7-38f3-a50a-80b963bfd4a8 | -10.40509 | -61.26746 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c0a05b78-0c7c-350e-83e5-13788f4e557a | -10.40454 | -61.27096 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2d89fd7f-7de1-32ad-83b1-86f9f5104ad2 | -10.40399 | -61.27448 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ebac9dca-fba9-3a80-b661-2d4f2e29307f | -10.40344 | -61.27798 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1a2da629-9eaa-309d-974d-46627571f814 | -10.40289 | -61.28148 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| e29524a5-e1c0-3d31-b707-06fb4f02db9d | -10.40234 | -61.28498 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 49f9e94e-2e25-3c75-ac1d-1d9d4a2a9c87 | -10.40178 | -61.2885 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f71abcc4-543b-3f73-b3ab-ba79bd1e593f | -10.40177 | -61.26693 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 20c0704a-b005-3e25-a514-5ad6eaee333c | -10.40122 | -61.27043 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 931ff8e5-a756-3f84-938b-23492cf635bd | -10.40067 | -61.27393 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bbffd1d6-a1a4-322f-8ba7-faaf31132e5a | -10.40012 | -61.27745 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d1c91894-4ff8-38cd-a8c2-313e1b995e1e | -10.39956 | -61.28095 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| b642c622-972e-31bb-a6d3-c5bae3fd926c | -10.39955 | -61.25938 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README129.md)
