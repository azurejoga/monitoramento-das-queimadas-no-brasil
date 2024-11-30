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

## Dados Diários - Página 108

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 08400f98-456d-3773-be3c-a0a4eda16620 | -2.26477 | -50.35596 | 2024-11-30 05:01:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2266739d-c9b4-3dba-9cc3-ec463805107f | -1.62834 | -52.37616 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3a45c196-f60c-3bc6-bb0f-21fb7b97b734 | -2.1993 | -48.33762 | 2024-11-30 05:01:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1ae20564-ee7b-3323-acd4-68e3b3ab4f72 | -2.47099 | -50.36698 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 503a601f-3ae0-3853-b869-063049c46b0b | -1.13288 | -51.67468 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4a179811-231a-3fc6-90ae-cd965759dd86 | 0.89133 | -51.98453 | 2024-11-30 05:01:00 | NPP-375D | SERRA DO NAVIO | AMAPÁ | Brasil | 1600055 | 16 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 025b5397-df94-3406-bcf0-750d7ac93825 | -2.59856 | -53.98052 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 17b4f371-5bb1-3506-a852-25aca729c8e7 | -1.39812 | -52.05336 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d45480dd-5ec9-38bf-ae59-f7f4a3c80426 | -2.56546 | -53.96126 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 849467ec-2499-3e9e-af13-47da1053c5dd | -1.09859 | -53.38913 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 9acc4916-d91d-31b7-a6bc-7acd336ba208 | -4.17 | -48.62756 | 2024-11-30 05:01:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4a7715ad-f813-3e42-bd42-36d1016dcae6 | -2.95185 | -49.44744 | 2024-11-30 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 77e44af5-7e65-3ded-b8f5-5c2adc170d47 | -1.13265 | -53.70737 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 87e7a80b-0afb-363c-9f8d-7949b21f6a11 | -1.12341 | -53.78802 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a7fa71a9-4cff-3d44-87d7-e2216236fd48 | -3.26755 | -50.56522 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d9597be7-770e-30c1-82e3-c5f20a220d73 | -3.25642 | -51.21328 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 760bf73d-4c3f-3213-9564-daa393bf2299 | -3.8309 | -46.4674 | 2024-11-30 05:01:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| af6e9fbd-a729-3af5-99e8-8bb94b91514e | -1.09241 | -53.36279 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a2fa5e30-65d9-3453-9042-10aa7cccfbc2 | -3.07782 | -53.30206 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 94d9236b-0ed8-3e56-85da-9a57315dc2ce | -0.58123 | -51.69659 | 2024-11-30 05:01:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 19cb41af-036e-326c-b2a2-02ad71d336ad | -2.70151 | -46.12479 | 2024-11-30 05:01:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 081c696d-cfc8-3026-99a2-c4e8f9a18dff | -1.6864 | -46.77897 | 2024-11-30 05:01:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| ad41c6b2-7337-3760-ba18-9fd368f3e327 | -3.05997 | -53.68623 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e2b0f8c8-c656-3ca4-b314-5c3c175c6402 | -1.99354 | -53.29278 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fe6252e7-e6e8-319b-987a-1373e279049f | -2.60203 | -54.24175 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bfd75296-1fe9-309b-a8ac-fd3d9dcef787 | -3.20505 | -50.21429 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 55ca6db3-da99-367d-9b4a-27ee796dad90 | -2.81775 | -54.09371 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7fe51c63-c512-3e02-9e13-ee6c44814fd9 | -1.08993 | -53.64008 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| feecea5c-0d22-30eb-96c7-6b8ddc4ec70a | -3.19046 | -54.32654 | 2024-11-30 05:01:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a855c489-0330-3d81-bda0-5d34652bbed6 | 0.99426 | -50.26606 | 2024-11-30 05:01:00 | NPP-375D | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e4aeb45b-017a-3411-abdb-ff671628f171 | -2.26034 | -50.35786 | 2024-11-30 05:01:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4105d5e5-09ed-34d5-8abc-f9e386fedd77 | -3.15042 | -53.82445 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ce27f1c3-3792-3917-ba7c-b907f2f9e772 | -3.74482 | -54.67947 | 2024-11-30 05:01:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9afa5853-d020-3e0e-b83a-1dcd1c23ca54 | -2.86876 | -53.98683 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 1c57963d-39a7-32dc-b6f4-0422a2a4e874 | -4.05635 | -46.82388 | 2024-11-30 05:01:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| be22a3c2-2a87-3c98-8a65-dc267894b47e | -2.92751 | -49.43189 | 2024-11-30 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c4a97bb3-a30c-3378-a92a-7df46d7ef673 | -2.35077 | -53.92808 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 71518d11-13cf-36b6-adb4-5273bbd00268 | -1.59279 | -52.28445 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 57e6b6a2-180d-31f0-87e7-ba9927134b81 | -3.09141 | -53.32658 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9e6cdc5e-fc94-3f4d-b1a1-61361a0a2819 | -2.06113 | -56.08094 | 2024-11-30 05:01:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| aad341a5-8d0e-3d4a-9e74-25c647a9f5fd | -2.84447 | -54.09785 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 341272c8-a49c-33ad-9ec4-c9c5196ae069 | -3.10774 | -50.35897 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4dab3bbd-e276-396b-ba62-8e8234712b7e | -3.05571 | -54.0442 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 09b99202-6e24-3d1e-adda-bd5c328bde89 | -1.49141 | -54.46174 | 2024-11-30 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5bbb7b9a-c51a-3823-88ee-6993491204fc | -3.09427 | -50.34156 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b1ee5cda-1c78-3b04-91d1-9b99c0e2df80 | -3.41911 | -53.88737 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c66d9836-108f-3a8a-8300-6072ec6196bb | -3.99007 | -48.93921 | 2024-11-30 05:01:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5a88e454-d18c-3692-800c-be3644dd1d1f | -4.10576 | -50.98562 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f9c3c440-0ff0-3abf-9fb9-1a95ac8392cc | -3.53212 | -50.21809 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ffe5a0be-ec85-3069-a0db-bf73346b92f9 | -2.97901 | -53.88848 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b3765da3-77fa-313e-8db2-4765d978608c | -1.09547 | -53.605 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 97c6f7aa-be62-36ee-8b60-355151568bc9 | -1.62394 | -52.4604 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2efc2762-e313-3ed0-b460-efb9ba4d9fa2 | -3.38943 | -54.28584 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3afa32a5-23f8-3e6f-9fe3-dfe0a9de746e | -3.09835 | -53.81597 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 714e9f31-d3bc-3ed7-bd69-288d0ef16b39 | -2.81101 | -54.07118 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 222596ec-ec30-3272-840a-bc7bf7a44c68 | -1.47418 | -55.13012 | 2024-11-30 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 85150033-447b-3ff4-9025-754f0a4840be | -2.7608 | -49.22684 | 2024-11-30 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 464147a6-6b40-395c-8090-503a93daf20d | -2.62995 | -54.06411 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 89fd320a-862d-340d-b588-c49fce751235 | -1.52438 | -52.03172 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 57464e18-7434-33cc-b49d-c27249ff1585 | -3.48969 | -53.81797 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 17b175bc-6124-336b-b994-04b6feb38a35 | -2.84657 | -54.04084 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 59d58377-6db9-3089-abe2-c3bd115ca7ff | -3.26606 | -54.10577 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4b9b6598-0546-385d-b353-bd297a99cb98 | -2.84831 | -54.07338 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bdd3b88c-8117-3249-88c8-5f74ccf6ff26 | -1.6126 | -53.62699 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 175b0b87-6321-3c48-83cb-156bd44964cf | -2.03509 | -53.49639 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4a54b901-604c-3ac5-9a2c-0760bed2f9e6 | -3.18046 | -54.32498 | 2024-11-30 05:01:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e413e88a-aa66-3119-90c3-1b83bc31e8b2 | -3.06061 | -51.05753 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b06ec8f8-2033-33f0-b6bd-f60e69421a65 | -2.88279 | -52.89474 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0040900f-7ff2-3ef6-84ef-b0003c790915 | -1.1613 | -53.56839 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2b8af7c9-38f4-3041-a99e-78f1bb3bf59c | -2.72692 | -54.13697 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e50c8cb3-410b-3b94-aae2-034b1b501b9a | -2.61356 | -51.81418 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 424b34e1-5034-39a0-8da3-a4449a058448 | -3.74427 | -53.39097 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6e02568d-2cfe-3843-8258-1d65a6f77d49 | -2.41259 | -53.85128 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 98570862-0cb9-3698-9623-406ab4b1d6bb | -2.6064 | -53.99608 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 615023e1-f51c-300b-b348-af1f0ad773fa | -1.33028 | -52.18703 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3737f0f7-24a1-3f01-91c4-2d3464b118df | -2.35831 | -55.87597 | 2024-11-30 05:01:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 29e1e94b-e75e-3237-8df9-c543863e9858 | -3.51677 | -54.79593 | 2024-11-30 05:01:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7c629e27-cad0-3fa7-aa08-9b9185096060 | -2.59328 | -54.07985 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e3c52d92-fab4-3497-9798-ca0a183ad39d | -2.60828 | -54.07146 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 45652b44-4ec1-36f0-9ca0-647ac66c9490 | 1.18354 | -55.97071 | 2024-11-30 05:01:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 365119e0-206e-3b59-aeb2-1588e2c40703 | -2.71187 | -46.12313 | 2024-11-30 05:01:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ca772f82-317c-32ed-ae55-038e780e0fdf | -1.19666 | -53.71353 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a103e169-e1ec-304a-8798-d027aae4f08f | -2.82443 | -54.09475 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b0d170e6-0a91-3bb4-86bd-a5719ef06394 | -3.24656 | -53.29404 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 97be7c80-4fb8-3e54-b59c-7647edb55881 | 1.98969 | -60.56454 | 2024-11-30 05:01:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b0a8cd2f-f0c4-3865-9a9e-e853cbe4c5d6 | -1.70042 | -52.64093 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 0577c698-1347-332a-8870-f268e9ef67e1 | -2.89106 | -54.16579 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 40d07731-8a92-355a-83e0-c271db8c155c | -1.07142 | -53.21044 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 495edff1-f36f-3105-9c0d-80028a466bbe | -2.57012 | -54.33628 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 22cbc887-c5e5-39dc-bf2a-4de31ef55b3c | -3.07839 | -53.2984 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d1da0223-b8ad-3202-ad40-95ac0befee55 | -3.70752 | -54.61334 | 2024-11-30 05:01:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8897f5ea-dfaf-3e4f-88ef-de9dc9701e9e | -3.37466 | -50.82495 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ca30d3df-2878-39b4-bd20-20247a44edac | -3.59996 | -49.99091 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ebad4e3d-b5c0-3c28-8147-2889c99b9ff8 | -3.07488 | -50.98936 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0e34810b-79f8-3e0d-819c-5827b3ea7533 | -1.70026 | -52.47218 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d0d6988a-0403-39ef-b98d-279d6e1065ac | -3.05855 | -48.52299 | 2024-11-30 05:01:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9ee4f8ce-ec50-35ff-9da9-d092f86ffdf4 | -2.83395 | -54.12126 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 16cf665d-e747-3099-baed-c28f26de6953 | -3.97667 | -41.52519 | 2024-11-30 05:01:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 60b28c72-5823-3adf-9370-fbd438e2a540 | -1.11991 | -53.72324 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5ca63321-55c4-3f7b-bca1-387b209ab0c8 | -4.06538 | -49.06064 | 2024-11-30 05:01:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README109.md)
