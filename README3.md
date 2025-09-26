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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3970e086-0ecd-3221-9c81-c4a5f54c8018 | -9.6922 | -48.9438 | 2025-09-26 01:10:00 | GOES-19 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 76.7 |
| f229547f-cb24-3f5f-a8dd-eed709c2f54d | -16.8538 | -50.5026 | 2025-09-26 01:10:00 | GOES-19 | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 56708e28-9318-36d2-b6ff-e85e5e27fb79 | -11.4225 | -44.9794 | 2025-09-26 01:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 42.5 |
| 83a5f976-b9cc-33ce-bb0e-ed16484e7a19 | -5.475 | -43.0774 | 2025-09-26 01:10:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 41.7 |
| 336ac26b-afc0-3e5d-8bad-6c1748493d6a | -5.4565 | -43.0554 | 2025-09-26 01:10:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 64.6 |
| f88978d7-1760-3c90-a53d-6fa2a5af6f4f | -5.4562 | -43.0788 | 2025-09-26 01:10:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 45.9 |
| 3f144a8a-1bef-337b-9242-20e8bd7c26ec | -12.7377 | -43.4614 | 2025-09-26 01:10:00 | GOES-19 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 76.5 |
| f0de679a-31c0-3f33-b9bf-b25f5074513d | -5.6361 | -43.9258 | 2025-09-26 01:10:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 0a9c842c-3025-31c6-9c5a-f943a6641548 | -8.08634 | -55.22309 | 2025-09-26 01:11:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 8c7ad656-68f9-3891-9664-23ed95682a21 | -10.62939 | -53.88399 | 2025-09-26 01:11:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 4fbff954-136f-33f5-a291-fe06aca7ed51 | -10.92305 | -51.1189 | 2025-09-26 01:11:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 13.4 |
| b41351de-c430-3556-a2b3-5bf91e9081e1 | -10.92341 | -51.13472 | 2025-09-26 01:11:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 746401da-7e93-3512-8662-84c924ee9bd3 | -10.17088 | -55.39599 | 2025-09-26 01:11:00 | TERRA_M-M | NOVA GUARITA | MATO GROSSO | Brasil | 5108808 | 51 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 2fabf5af-c33e-33c8-8104-5ff292e39038 | -10.1805 | -55.39455 | 2025-09-26 01:11:00 | TERRA_M-M | NOVA GUARITA | MATO GROSSO | Brasil | 5108808 | 51 | 33 | nan | nan | nan | Amazônia | 9.1 |
| f8c6b721-a81b-39e5-ae22-227dbc1028ae | -9.6944 | -48.93708 | 2025-09-26 01:11:00 | TERRA_M-M | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 50.3 |
| ab37c135-6174-30ca-8104-fde6f1c0f26d | -10.92641 | -51.14004 | 2025-09-26 01:11:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 22.8 |
| 547bbb61-fc4a-3cce-8e24-30d3c66e5a5d | -10.62494 | -53.89056 | 2025-09-26 01:11:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 15.8 |
| a1c576c8-7caf-3edd-8bed-873ab91eefdc | -6.57766 | -51.1157 | 2025-09-26 01:11:00 | TERRA_M-M | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 42.7 |
| be1bce47-2c9b-36e1-9222-cb2dc8f1a5ec | 1.00394 | -59.50521 | 2025-09-26 01:13:00 | TERRA_M-M | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 5.5 |
| c58a0a85-fdad-3105-b841-909b050d9173 | 1.0027 | -59.51416 | 2025-09-26 01:13:00 | TERRA_M-M | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 4782a90d-e026-3ca5-b0ea-e46c9b654fd6 | -2.69128 | -54.95523 | 2025-09-26 01:13:00 | TERRA_M-M | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 5cb8e3a6-0781-3345-9f43-febdecf51b11 | -2.70243 | -54.95361 | 2025-09-26 01:13:00 | TERRA_M-M | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| ce02e317-fe7e-32cc-b37a-9839d7fa2bc9 | 2.63809 | -60.03153 | 2025-09-26 01:15:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 3245b7bb-7ec2-36b0-8d79-e77782f3c745 | -6.5631 | -51.1126 | 2025-09-26 01:20:00 | GOES-19 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 5100f8b7-6189-313a-bd9c-6c02771bd301 | -5.6361 | -43.9258 | 2025-09-26 01:20:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 0329ddc4-addc-3803-9945-dbdafe12e5ab | -5.6548 | -43.9244 | 2025-09-26 01:20:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 42.8 |
| 060fb291-e98f-3b74-90fc-36a205c3510d | -15.0585 | -42.3178 | 2025-09-26 01:20:00 | GOES-19 | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 74.7 |
| 7fbbeafb-5b97-381e-910c-edb00b035e18 | -9.6922 | -48.9438 | 2025-09-26 01:20:00 | GOES-19 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 7bd50bc8-afdf-3568-b1c1-37a734e560b3 | -5.4752 | -43.054 | 2025-09-26 01:20:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 88.1 |
| e50e3add-65ba-30c7-95ee-2d2fd9cbe79f | -17.5956 | -46.6648 | 2025-09-26 01:20:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 66.2 |
| fa860d11-0f2f-3453-b974-9d9ded130080 | -5.4562 | -43.0788 | 2025-09-26 01:20:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 40477d80-26d9-39f6-b772-80be5914aee8 | -15.0579 | -42.3424 | 2025-09-26 01:20:00 | GOES-19 | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 59.2 |
| 530a64d5-bd9e-3317-82a6-ca4e8f13aa8e | -3.45 | -44.1238 | 2025-09-26 01:20:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 23.3 |
| ab273326-f9ae-3b42-a8ef-26055b502aed | -16.8538 | -50.5026 | 2025-09-26 01:20:00 | GOES-19 | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 8fc0b254-42e6-354e-a47d-4bc7ddbe9ebf | -12.7377 | -43.4614 | 2025-09-26 01:20:00 | GOES-19 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 29d15f0b-928b-3574-9040-62bdf57b8fbb | -5.4565 | -43.0554 | 2025-09-26 01:20:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 109.1 |
| 61289271-4ad1-3a49-a97e-7c4211cfef9b | -5.475 | -43.0774 | 2025-09-26 01:20:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 63.4 |
| 93af4165-5cc1-33f6-bf7a-54025946f58a | -5.6361 | -43.9258 | 2025-09-26 01:30:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 159.3 |
| a6f9aab5-641b-325c-927b-f6094c4bd126 | -5.7392 | -44.9718 | 2025-09-26 01:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 282.8 |
| fcefd414-fc23-3bfb-9626-d94add69e87a | -17.6155 | -46.6607 | 2025-09-26 01:30:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 35c80759-afe3-3599-b6d0-c281454df350 | -5.739 | -44.9945 | 2025-09-26 01:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 73.6 |
| e9efa800-be26-3f24-af8d-26d59ea16bfd | -5.6359 | -43.9489 | 2025-09-26 01:30:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 52.1 |
| 7375a00c-6118-39dc-ba88-abde8dfdbaaa | -5.7579 | -44.9704 | 2025-09-26 01:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 101.4 |
| b8bca4e0-28c7-3b9e-a129-b03fbfea87bf | -13.8539 | -45.614 | 2025-09-26 01:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 55d5b024-25b1-3e1a-b3ae-d675959c6adf | -17.595 | -46.6882 | 2025-09-26 01:30:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 84.1 |
| ed4dedbb-c5fa-3ae9-9c4e-ad09fae736b3 | -5.7394 | -44.949 | 2025-09-26 01:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 125.0 |
| 0269fd41-dbe1-3c1d-8650-fae98ae5edd4 | -5.6174 | -43.9272 | 2025-09-26 01:30:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 42.3 |
| 21094098-1a4c-3d0d-b221-75c8a0f8f518 | -11.2408 | -45.5563 | 2025-09-26 01:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 48.3 |
| 39392bc9-3126-3767-b6fc-d1a808771666 | -5.4752 | -43.054 | 2025-09-26 01:30:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 27.1 |
| 40baa3f8-aaa0-396c-8f3e-388a12a4917c | -17.5956 | -46.6648 | 2025-09-26 01:30:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 146.9 |
| e9e8b943-6551-3020-b26d-4c299ea366b0 | -11.2412 | -45.5334 | 2025-09-26 01:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 52.3 |
| bcf71359-a7ac-3a90-b77a-84a0e8546753 | -5.4565 | -43.0554 | 2025-09-26 01:30:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 26.3 |
| 1886b4d0-e98c-3c27-9487-980d3178ad17 | -9.6922 | -48.9438 | 2025-09-26 01:30:00 | GOES-19 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 9b5b62ad-5322-3b9c-a928-21129c5e122e | -12.7377 | -43.4614 | 2025-09-26 01:30:00 | GOES-19 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 62a123b7-2f5a-3f77-8458-a5082a625287 | -5.6548 | -43.9244 | 2025-09-26 01:30:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 56.9 |
| 1a241f24-7d22-3689-b236-9572687709c7 | -16.8538 | -50.5026 | 2025-09-26 01:30:00 | GOES-19 | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 74.8 |
| e3d3ac36-6916-39dc-b0b8-599602796dd6 | -15.0585 | -42.3178 | 2025-09-26 01:40:00 | GOES-19 | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 66.2 |
| 480469ad-6ce0-30fe-aec0-64eb690ea7ce | -11.2416 | -45.5105 | 2025-09-26 01:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 42.5 |
| 6d40c75c-e242-3de5-be2b-e312b0562e00 | -15.9966 | -59.4851 | 2025-09-26 01:40:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 7b081b83-3ee9-3be0-8803-dce85efebbee | -5.6174 | -43.9272 | 2025-09-26 01:40:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 77.5 |
| e3a6eb94-56c1-3afe-bd61-af868bddbb5a | -11.2412 | -45.5334 | 2025-09-26 01:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 3927740c-de0d-33c9-8a33-69c53496ad90 | -11.222 | -45.536 | 2025-09-26 01:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 47.1 |
| a1ac770d-c715-3ebf-9166-80f87a1e4689 | -15.0579 | -42.3424 | 2025-09-26 01:40:00 | GOES-19 | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 64.9 |
| b47c8b2b-87b9-3b48-a25c-73c62f8ea576 | -16.8538 | -50.5026 | 2025-09-26 01:40:00 | GOES-19 | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 71.5 |
| c65f9dcd-0a48-3f3c-bda4-208e224acdfb | -11.2603 | -45.5308 | 2025-09-26 01:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 56.4 |
| a5c00fa2-6f22-372e-8b38-9bb53a45013f | -11.2408 | -45.5563 | 2025-09-26 01:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 68.6 |
| 730970c2-e301-335e-b293-db562401bc66 | -11.2217 | -45.559 | 2025-09-26 01:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 58.9 |
| 28e19210-4b4a-3c19-b248-311772dcf653 | -5.6361 | -43.9258 | 2025-09-26 01:40:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 217.2 |
| 4d3b50a9-ecbd-331c-82ba-10c2e760e560 | -5.6359 | -43.9489 | 2025-09-26 01:40:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 61.1 |
| b5af3b5c-68a0-3ade-ade6-5dca8a15bc34 | -5.6548 | -43.9244 | 2025-09-26 01:40:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 5d590a3e-b020-3eef-8f61-72fac62e1310 | -11.2599 | -45.5537 | 2025-09-26 01:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 124.6 |
| 14ef227a-edc0-365a-840e-0b55020fdd57 | -11.2408 | -45.5563 | 2025-09-26 01:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 175.3 |
| 4549b0a7-e9d2-3aaf-9155-4f317e07355c | -16.8538 | -50.5026 | 2025-09-26 01:50:00 | GOES-19 | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 74.5 |
| d4fe35a3-f310-3405-b281-2e5c608663f7 | -5.6174 | -43.9272 | 2025-09-26 01:50:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 63.4 |
| d8c7cb13-aa6b-35d8-9e52-2937a7a0bc8c | -13.5084 | -42.7003 | 2025-09-26 01:50:00 | GOES-19 | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 83.8 |
| c4e62c17-34d3-3f4a-bc14-986c1ccf5483 | -11.222 | -45.536 | 2025-09-26 01:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 6e6d62a0-9d94-39a0-a3fb-d1548e8af436 | -5.4752 | -43.054 | 2025-09-26 01:50:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 77.0 |
| ae21c2c4-0b0a-3874-ba28-f8ced8853a46 | -11.2412 | -45.5334 | 2025-09-26 01:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 185.4 |
| a51ce30c-6381-3b2b-be28-9681a2aa0b9a | -11.2603 | -45.5308 | 2025-09-26 01:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 146.8 |
| 95488087-2f72-3d7d-a767-439499346588 | -5.4565 | -43.0554 | 2025-09-26 01:50:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 6983a4ab-1874-32a9-ab2b-cb4a869f0701 | -5.475 | -43.0774 | 2025-09-26 01:50:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 61.0 |
| 77692d1d-f730-3aca-86d4-8d75de042600 | -5.6359 | -43.9489 | 2025-09-26 01:50:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 9f7414da-554d-3487-98b2-c748e7be3e42 | -11.2217 | -45.559 | 2025-09-26 01:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 641c9813-7373-33b2-9823-e9fd00df1d3e | -5.6361 | -43.9258 | 2025-09-26 01:50:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 179.0 |
| c08ed28b-9c6d-30dd-8ebf-c61d0a0600ec | -5.4562 | -43.0788 | 2025-09-26 01:50:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 65.4 |
| b5b9406a-0cfb-3147-bdf9-3957b450c832 | -13.2859 | -46.9846 | 2025-09-26 02:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 105.9 |
| c9480bec-fef6-3b02-84b5-11935c96c526 | -5.6174 | -43.9272 | 2025-09-26 02:00:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 61.4 |
| 51fe4f98-ae32-3029-bde8-cbefcc146deb | -13.267 | -46.9649 | 2025-09-26 02:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 111.1 |
| 6c88a923-b3a0-39c2-924e-d7ff3955e6c3 | -13.2863 | -46.962 | 2025-09-26 02:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 185.4 |
| fa4b6f9f-7683-314a-b94b-ba2d2a21529e | -5.4752 | -43.054 | 2025-09-26 02:00:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 59.8 |
| 7136025e-0fd1-3474-8e80-b91ffe5b39a1 | -15.9966 | -59.4851 | 2025-09-26 02:00:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 85.2 |
| 203f639b-a6f9-3296-a07c-93d0896aebf5 | -5.475 | -43.0774 | 2025-09-26 02:00:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 41.1 |
| 6c4e4ee7-903c-3e7b-a06c-41d3bcd009ee | -5.4565 | -43.0554 | 2025-09-26 02:00:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 49.1 |
| 8ec36150-1313-384e-9e6d-a05ec1a8ec4f | -5.6361 | -43.9258 | 2025-09-26 02:00:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 169.3 |
| fa159e57-7e59-3f2e-9f44-731464fd6a9e | -13.2863 | -46.962 | 2025-09-26 02:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 104.0 |
| 367adba2-6a45-3c5e-9300-feabe972f8ec | -5.6361 | -43.9258 | 2025-09-26 02:10:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 141.2 |
| 95ac2ae7-d12e-314d-a61f-31a208e3bddd | -5.6359 | -43.9489 | 2025-09-26 02:10:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 55.2 |
| 2c933a72-7e01-30e1-94c9-9b38ab79569b | -13.2859 | -46.9846 | 2025-09-26 02:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 54.6 |
| 663aa5d0-90da-308c-bd34-fbe7f4006cd8 | -13.267 | -46.9649 | 2025-09-26 02:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 90.9 |
| e01dcd71-2b83-39d9-b437-c20147667d10 | -13.2666 | -46.9876 | 2025-09-26 02:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 74.0 |


[Clique aqui para ver as próximas entradas](README4.md)
