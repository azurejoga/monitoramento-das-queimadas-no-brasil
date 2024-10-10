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

## Dados Diários - Página 90

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 48cd9990-f8ec-32db-a0b7-45a3b35d6397 | -3.33879 | -50.12754 | 2024-10-10 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0043161e-a121-37e5-8184-8145095951b1 | -3.33825 | -50.13098 | 2024-10-10 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 161bb76d-b8a6-3a32-82a0-e5fad9f5457f | -3.33603 | -50.12359 | 2024-10-10 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dbb616b9-9fe5-3a34-babe-6a50bff1af37 | -3.33549 | -50.12703 | 2024-10-10 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1d4ee7c5-b5da-3c36-a754-8ecd665b3cf5 | -3.33273 | -50.12308 | 2024-10-10 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b859ab08-f9e8-3264-a23f-c1ae635838cc | -3.31672 | -50.46193 | 2024-10-10 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f3e2c8d4-9135-30fe-b16a-eff07e56a4ec | -3.31618 | -50.46536 | 2024-10-10 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 70394db3-f621-398b-a240-e0e601e4b38c | -3.29437 | -50.17342 | 2024-10-10 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d4b620ea-4252-3dad-a813-34a19c76d042 | -3.29383 | -50.17686 | 2024-10-10 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f96e5170-8a61-3a76-8021-5e5b1cd14028 | -3.27147 | -50.16624 | 2024-10-10 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 103a9d06-d080-345c-9cad-662bb0f865aa | -3.26816 | -50.16573 | 2024-10-10 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 01246ca3-42da-3c73-99f2-4f3b8f976984 | -3.17102 | -50.24562 | 2024-10-10 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 57876fab-094c-37ef-b31b-220af580a99c | -3.1519 | -50.25629 | 2024-10-10 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8cb7570a-efba-3896-9934-62d12b8863d2 | -3.12216 | -50.42406 | 2024-10-10 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 06821b28-6e2d-3f90-a888-84c9a6c42976 | -3.10773 | -50.38663 | 2024-10-10 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7df72618-7946-335b-8f76-6d18821974ca | -3.10443 | -50.38612 | 2024-10-10 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1419596a-24a0-3a57-adaa-fc74cba540b7 | -3.10389 | -50.38955 | 2024-10-10 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a814c862-7f76-3b46-837e-8b26b21aebb6 | -3.09591 | -50.48335 | 2024-10-10 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 062c15e5-32fd-3bf7-909c-34bd1ca7908d | -3.09585 | -50.46221 | 2024-10-10 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 15922246-61c5-3540-a552-12f733715a6e | -3.09531 | -50.46565 | 2024-10-10 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ef020fca-556e-3f4d-a155-fd1e4661216f | -3.09261 | -50.48284 | 2024-10-10 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 317b730f-80ec-3fd5-a08d-32b5ac5f8267 | -3.9533 | -49.91307 | 2024-10-10 04:42:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4fe7cdbc-f135-39f6-8c86-223ae243acb0 | -3.95276 | -49.91653 | 2024-10-10 04:42:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 250edd36-7ed0-303f-9790-445ac22c96ae | -3.94572 | -49.96144 | 2024-10-10 04:42:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cbe502ad-22a3-3884-a7ba-9291df46aaea | -3.9438 | -49.27898 | 2024-10-10 04:42:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6f191873-a839-3a59-8d5a-d9d70ba2a9b7 | -3.93105 | -49.68612 | 2024-10-10 04:42:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 39589c4c-a0da-33ba-9080-721fac1f8af0 | -3.92658 | -49.67111 | 2024-10-10 04:42:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| be7949f6-ef8d-32d7-ab35-3abbd0c07a1b | -3.92109 | -49.68459 | 2024-10-10 04:42:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 07bcd87a-f82e-3f8d-976f-485edc1aec40 | -3.92054 | -49.68808 | 2024-10-10 04:42:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 103ed23a-0f38-30bb-b117-454c6c4d1321 | -3.92039 | -49.9716 | 2024-10-10 04:42:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 07ca32dd-29de-35ed-888f-29195a190cad | -3.88683 | -49.99114 | 2024-10-10 04:42:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b9017eef-f681-353f-b495-ed0f78457ba5 | -3.88405 | -49.98722 | 2024-10-10 04:42:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8c90bc23-7747-3e49-bed7-6cdf92f51ab8 | -3.88352 | -49.99063 | 2024-10-10 04:42:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 82c34686-fa6e-31b2-98a2-28e4f3ef5865 | -3.87544 | -49.89038 | 2024-10-10 04:42:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0a7f00f1-cdd7-3c14-8fc2-9abb659b1aa8 | -3.71439 | -50.15798 | 2024-10-10 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 646ebd10-0842-3df1-8fe6-af8253188e43 | -3.70508 | -50.17416 | 2024-10-10 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c2eef1d4-47cd-3ebd-a0a2-012d659b1089 | -3.70454 | -50.1776 | 2024-10-10 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 01ebae24-a818-3921-b406-f2b882172e67 | -3.704 | -50.18104 | 2024-10-10 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 288d8813-1bc5-3d40-9a83-c532cf27d059 | -3.70177 | -50.17365 | 2024-10-10 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3f24cb95-d469-3649-b413-f1988832bd50 | -3.70123 | -50.17709 | 2024-10-10 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7cfd258f-cb41-34d8-a434-0b6b586573ee | -3.70069 | -50.18053 | 2024-10-10 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a4fabb93-f6c2-3679-b72f-4ebf6b3b8619 | -3.69908 | -49.84496 | 2024-10-10 04:42:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0b62ebc2-96b8-3895-8083-c6114ebace84 | -3.69516 | -50.17262 | 2024-10-10 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2ee6a00d-d3bc-36bb-ae33-7a9922fe2ab5 | -3.69186 | -50.1721 | 2024-10-10 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 993cbb36-cd5d-3ed2-bef0-bff9452fb0de | -3.6903 | -50.20358 | 2024-10-10 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3bb19b2e-a175-3ecc-b484-f8c997602edb | -3.6895 | -50.12241 | 2024-10-10 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| be83f069-c728-33c5-86fd-aa7f40ff1ff5 | -3.68896 | -50.12585 | 2024-10-10 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 7743ac60-1caa-31f4-8db1-8224d53286c8 | -3.6862 | -50.12189 | 2024-10-10 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f240df8f-116c-368d-98b4-4e26374b4d26 | -3.68566 | -50.12534 | 2024-10-10 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2201df0f-4f04-3db6-901d-c413dc2de597 | -3.68289 | -50.12138 | 2024-10-10 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 311986ef-e88b-38b8-a9e0-9a0b5ef12877 | -3.68235 | -50.12482 | 2024-10-10 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5b5b0863-018b-3e83-8d5b-696303082586 | -3.67959 | -50.12087 | 2024-10-10 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b034b575-06c2-33f5-bb2d-53861b4bdd03 | -3.64872 | -49.9503 | 2024-10-10 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aadd0fd3-be91-3d06-8cd8-fbd189dcd298 | -3.57918 | -50.39398 | 2024-10-10 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8bbc4642-1865-3aba-bbbc-b4f65148dc06 | -3.55832 | -50.37273 | 2024-10-10 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 96136cb2-ec3f-3a61-bfbb-b0f5c8296bf0 | -4.17818 | -50.40681 | 2024-10-10 04:42:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e43f7ae0-ded0-398f-942c-a4a2b0c6b2d5 | -3.59065 | -50.55771 | 2024-10-10 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 44caf317-7a1d-3195-9a00-cf5e0187fcf4 | -3.56703 | -50.5787 | 2024-10-10 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3214a331-0ff1-3228-9676-468124f81fee | 0.45248 | -50.21141 | 2024-10-10 04:42:00 | NOAA-20 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| baa9c7c1-da39-300d-988d-791869d10fa6 | 0.4497 | -50.21539 | 2024-10-10 04:42:00 | NOAA-20 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ab0f7ee8-5aa0-3fe8-8377-f136f5a733f4 | 0.44916 | -50.21193 | 2024-10-10 04:42:00 | NOAA-20 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 12c032a7-0cc0-30ac-a512-936c902e0f36 | -0.42786 | -50.68373 | 2024-10-10 04:42:00 | NOAA-20 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 626c9844-a57f-374b-9fed-aa2f34a398ce | -1.85241 | -51.19355 | 2024-10-10 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1d877a88-969e-3fac-9e2b-ec55cdd3fcfc | -2.22135 | -50.6217 | 2024-10-10 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fbcc1d7d-e4b7-33a4-a03c-e72d5277291a | -2.2208 | -50.62516 | 2024-10-10 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6c7bfc04-2f0b-31fd-bc18-ffdb22f8d791 | -2.12652 | -50.70617 | 2024-10-10 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 44cde419-eb02-3e49-90ec-66643c945246 | -2.12321 | -50.70566 | 2024-10-10 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| be273d8e-8d15-3234-8131-d5b267560cee | -2.10258 | -51.24719 | 2024-10-10 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e3435739-0b39-3619-ac32-4304ce81d8fd | -1.22353 | -50.52913 | 2024-10-10 04:42:00 | NOAA-20 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| afaf5ece-6b96-3e49-ad32-7ae0b505cd2b | -1.10183 | -50.52464 | 2024-10-10 04:42:00 | NOAA-20 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 11a6b755-0e9a-374f-94f4-fa6f211a9411 | -3.61528 | -51.43605 | 2024-10-10 04:42:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d622f466-c857-36ba-8a8c-3cde0c861d0f | -3.58133 | -51.43433 | 2024-10-10 04:42:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e1947955-03e8-38ac-9e1d-8ef5ffa9ed79 | -3.54384 | -50.79026 | 2024-10-10 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 15cb0f15-8e99-36f8-887c-d682db9e2d2c | -3.5433 | -50.7937 | 2024-10-10 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7433ff27-9f1c-3351-b165-40767cc432fd | -3.54066 | -50.85342 | 2024-10-10 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e1efbc6b-413b-32a4-becb-80872e70b7a9 | -3.54053 | -50.78973 | 2024-10-10 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 194161f7-2b36-39e8-9be5-0fc26e6617b8 | -3.53999 | -50.79318 | 2024-10-10 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 739123b0-63d5-3680-af32-d1869ab57f39 | -3.49733 | -50.80382 | 2024-10-10 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 5d4cda49-a3ea-3ea3-962e-3860f85c10ba | -3.49678 | -50.80727 | 2024-10-10 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 19fa03d7-5d54-37d5-b4eb-1cd7cbe98846 | -3.49402 | -50.8033 | 2024-10-10 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 313871ff-6db5-3653-8add-3412c2f49c54 | -3.44186 | -50.66103 | 2024-10-10 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d9adc59e-592d-3779-b025-766b485b79d3 | -3.07135 | -51.11415 | 2024-10-10 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e0da60ff-6589-3ca5-a22d-578819e39d3d | -3.05145 | -51.34813 | 2024-10-10 04:42:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 500e7378-0e15-3945-b83c-9314b6e994f2 | -3.04972 | -51.10003 | 2024-10-10 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8d110a11-0d98-3542-9023-e638db6d8bd7 | -3.0492 | -51.1464 | 2024-10-10 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f1c6b670-ad11-3436-be6d-79dd4c367862 | -3.04811 | -51.34761 | 2024-10-10 04:42:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 468474b1-4c2f-3254-9f42-acaa3bee322e | -3.03586 | -51.10143 | 2024-10-10 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bc471f73-2575-3250-a955-114879b626d3 | -3.03531 | -51.10493 | 2024-10-10 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f5aa2b59-1335-309c-9e73-cb67e5139282 | -3.03475 | -51.10843 | 2024-10-10 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6914627f-e1ec-3d32-830b-8991457bce74 | -3.03254 | -51.10091 | 2024-10-10 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 033f3b85-011d-3f03-8b47-4e6b99148612 | -3.03198 | -51.10442 | 2024-10-10 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| db15201e-5e3b-3c38-8f45-5087687f021d | -3.02954 | -51.10013 | 2024-10-10 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d91672fb-888f-36a7-9ec0-4f0479c29e5c | -3.02899 | -51.10364 | 2024-10-10 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6e820d92-b90f-3b54-97f1-2f4a13f84249 | -3.00625 | -51.43867 | 2024-10-10 04:42:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5791a507-9362-3414-a30d-61b106441feb | -2.97236 | -51.03047 | 2024-10-10 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a4937688-b6f3-3a22-9168-e67530c61221 | -2.96967 | -51.11221 | 2024-10-10 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 43ff975b-6a07-3691-bdeb-1bc400bce64d | -2.96634 | -51.1117 | 2024-10-10 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3f384815-a6d6-391f-bea6-da2051982ce9 | -2.92521 | -51.45849 | 2024-10-10 04:42:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 11bf43da-7c59-3687-862c-e8cdc87a6b4c | -2.92186 | -51.45796 | 2024-10-10 04:42:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 27b50852-89de-3d89-be6f-b817dd9c66cd | -2.90901 | -51.45232 | 2024-10-10 04:42:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README91.md)
