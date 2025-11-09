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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6e729bfa-7a0d-3f43-9244-e01c6c1bab33 | -2.61238 | -49.22821 | 2025-11-09 05:29:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e9ec3be8-6164-3d90-aa5a-eb0a7df99c62 | -4.40081 | -49.65684 | 2025-11-09 05:29:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 8fd6f3cb-fdcd-3929-9df9-45d44c78199c | -3.94959 | -49.02873 | 2025-11-09 05:29:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| da47da28-2a68-327a-b21e-acf2076f24e0 | -3.61651 | -49.27753 | 2025-11-09 05:29:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 90f0b916-c67e-3dbb-81a4-9180ae77484d | -3.1027 | -50.2003 | 2025-11-09 05:29:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 027a49b6-26a9-33c9-9ffa-65a196d8028e | -3.84179 | -50.74685 | 2025-11-09 05:29:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d520b1c7-cc33-3b1d-8d54-a96c1ba8b40f | -3.32384 | -53.36337 | 2025-11-09 05:29:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8321003c-3867-37dd-84aa-1f309cf393eb | -3.84362 | -50.74421 | 2025-11-09 05:29:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bac4f4c2-c2a2-307b-a387-94e0c73febf6 | -2.48169 | -54.19613 | 2025-11-09 05:29:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 60a7fefc-1a75-3d35-bb6c-12a5b8fcab08 | -3.31477 | -50.12471 | 2025-11-09 05:29:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c029ca7b-5052-34fc-9a03-350461be8154 | -3.09306 | -49.26604 | 2025-11-09 05:29:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3bed2b8a-ace5-3c5a-9e8d-29510b1483c8 | -2.94145 | -49.35634 | 2025-11-09 05:29:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| a01f86a0-83c1-3469-a6f5-4286ad605f25 | -3.14978 | -50.6083 | 2025-11-09 05:29:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 391665f6-98b0-3f4c-86b0-3dc29f092831 | -3.07667 | -49.3806 | 2025-11-09 05:29:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8e41b42c-500a-3ecb-9311-2860ae293ebc | -3.34585 | -50.20934 | 2025-11-09 05:29:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3ea51b70-302e-30a3-8023-b4c9be75e8f4 | -6.05147 | -58.05631 | 2025-11-09 05:29:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ddae7a3f-f054-370e-b6d6-f2a3bf071e2b | -3.08536 | -52.91955 | 2025-11-09 05:29:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 31ba25bc-cc45-38ce-b747-d9ceac3eae15 | -3.0614 | -50.21593 | 2025-11-09 05:29:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| e230c323-0f50-308e-bccb-60f412f2695a | -2.92386 | -52.51338 | 2025-11-09 05:29:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3deb006c-b063-3b15-8846-92dc10b8ae81 | -6.04615 | -57.9632 | 2025-11-09 05:29:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| db706998-0433-352a-94c7-24038d51a7f3 | -4.58989 | -49.38756 | 2025-11-09 05:29:00 | NOAA-21 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 81d5ee23-41c6-3753-82c3-915cda9c79b7 | -3.33186 | -49.12797 | 2025-11-09 05:29:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5d25b672-5cb3-35bb-9805-e55020c9474d | -3.56675 | -51.12434 | 2025-11-09 05:29:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d5844c1a-6bca-372a-a73b-ca0cfa10b841 | -3.32417 | -49.13284 | 2025-11-09 05:29:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3e19ab1b-6056-3aab-a70a-491abf3cb6dd | -3.80196 | -48.90285 | 2025-11-09 05:29:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7589d783-8857-344e-9ede-c5993debc1c0 | -4.28339 | -60.01851 | 2025-11-09 05:29:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dc3bddb4-4231-342c-9f56-6a25782f30ea | -3.14351 | -50.27226 | 2025-11-09 05:29:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 59001308-843e-3561-a848-b0abffeeb82b | -2.48624 | -54.19698 | 2025-11-09 05:29:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 742e1f40-25cd-3835-9f02-c4c1b50acdfc | -1.72426 | -54.68014 | 2025-11-09 05:29:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8d0b17c7-25f1-3685-8ddf-ba9bae16d95f | -3.3333 | -53.25172 | 2025-11-09 05:29:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9a9f52b9-f311-31e8-b463-8fdeb097523b | -3.14086 | -50.27554 | 2025-11-09 05:29:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| b16f7005-3fcf-36d8-bd7e-7036c7139ff1 | -5.18652 | -56.1097 | 2025-11-09 05:29:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f0bbb4e5-9e02-3eaf-b35f-8eb1aaf71308 | -10.08171 | -66.9268 | 2025-11-09 05:29:00 | NOAA-21 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0f1ebf70-2ecb-32ed-ab45-498a5900eabf | -3.65679 | -50.27214 | 2025-11-09 05:29:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 0d788701-0173-3a61-8ff5-79de99a1fdd5 | -1.65834 | -53.71467 | 2025-11-09 05:29:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 07fb6b65-ebe8-3463-817b-d0f9db7faded | -3.97873 | -51.03471 | 2025-11-09 05:29:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 88d23eb9-5298-349f-90cf-09e12f25b727 | -4.39445 | -49.65586 | 2025-11-09 05:29:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 61667368-058e-35f0-956d-38e439129334 | -1.70306 | -54.67273 | 2025-11-09 05:29:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 906ebae6-1fb9-389a-9e20-83f2c6a49da5 | -2.91869 | -52.51254 | 2025-11-09 05:29:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 72dc857d-97b4-3845-bdc6-0ca61d50a78f | -3.32458 | -49.13269 | 2025-11-09 05:29:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5759a557-e135-3b77-abe5-1ab6cb58d5bd | -3.09694 | -50.32347 | 2025-11-09 05:29:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 058faf22-c6f1-32db-8ea9-56e0812104f4 | -6.88819 | -49.25037 | 2025-11-09 05:29:00 | NOAA-21 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 16bdedcb-5d12-374c-b104-f1244542bbce | -3.14917 | -50.61248 | 2025-11-09 05:29:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3479ad7e-33a1-30b7-a361-84e2f0dc99bc | -4.52267 | -48.83581 | 2025-11-09 05:29:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 53d64079-8389-3da9-b62a-81c4a375dc30 | -3.50199 | -50.04504 | 2025-11-09 05:29:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2e17da60-2f67-300d-b166-c71bc676f94e | -3.80114 | -48.90863 | 2025-11-09 05:29:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0ba77fbb-7077-3061-8ec5-a010f216ec36 | -4.29327 | -50.65848 | 2025-11-09 05:29:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| f44d27eb-ea32-38ba-b377-976f2410fc74 | -3.33414 | -53.24615 | 2025-11-09 05:29:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 97693918-a3e0-3b98-bc43-34cc9d7315f9 | -12.09787 | -63.88691 | 2025-11-09 05:29:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aec6155e-93da-3f03-8ae1-c88bd7a9b05d | -3.41045 | -50.45399 | 2025-11-09 05:29:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 55250552-1faa-3d00-b9bd-379ed3a7aad4 | -3.40779 | -50.26174 | 2025-11-09 05:29:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| af8ec410-b522-3d8b-9749-2c62053ab9fd | -3.31854 | -50.31112 | 2025-11-09 05:29:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d5223acb-e4c6-3216-8e5c-874edc8bc46a | -2.26096 | -47.87272 | 2025-11-09 05:29:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 87a97ef0-fc66-33f2-98c3-7bf4d31aa96a | -1.2434 | -54.14755 | 2025-11-09 05:29:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8d6b8c94-613a-395d-b804-a2fe00ffa012 | -3.34651 | -50.20484 | 2025-11-09 05:29:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 87a376db-dfab-3000-8fa5-9024a0da3d5b | -3.79596 | -48.91106 | 2025-11-09 05:29:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 92d50951-bea5-3b89-8261-66779fcc79fb | -3.95159 | -49.02368 | 2025-11-09 05:29:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2c4a9b6a-6ed4-3c05-8ead-045b5443d202 | -2.61315 | -49.22302 | 2025-11-09 05:29:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 3725e0a4-8433-3b32-8985-d5951fc2c2d1 | -3.06329 | -50.21688 | 2025-11-09 05:29:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 316b04df-a4fa-3f63-a460-eaddd2b9baf3 | -2.94965 | -53.28529 | 2025-11-09 05:29:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a36c34ee-c349-336e-880e-ae2b9365c992 | -8.74092 | -67.22252 | 2025-11-09 05:29:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| edffac38-990d-303b-bf5a-b35440b70193 | -3.05592 | -59.17902 | 2025-11-09 05:29:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 42fbf263-4544-3c8a-b6b4-a6a92f079553 | -3.76217 | -60.30541 | 2025-11-09 05:29:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9185a129-018c-34c1-8ce5-9b6d6b367ee7 | -5.09428 | -56.15783 | 2025-11-09 05:29:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a04f1812-c528-384d-afca-d1b464b728e2 | -4.33146 | -49.76194 | 2025-11-09 05:29:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 9393dee5-7960-361b-a6a8-c88cfa855e83 | -4.4001 | -49.66203 | 2025-11-09 05:29:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| ab9d6eed-4831-316d-b352-a5d43e94766f | -3.6514 | -50.26667 | 2025-11-09 05:29:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5a04b28e-d698-37a5-9e19-ade8671cc29a | -3.26963 | -50.04377 | 2025-11-09 05:29:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 743891a5-2c94-3224-9140-7027b6e251cc | -3.60628 | -55.44784 | 2025-11-09 05:29:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 00b11117-a1fb-3561-97ad-af94974d7e5b | -2.98766 | -52.82365 | 2025-11-09 05:29:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 75a41ac9-e3ef-3aae-8c34-3c8b428b971c | -2.94581 | -49.35243 | 2025-11-09 05:29:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 430107fe-2e4b-31ec-b693-a5ae4164461a | -2.98647 | -52.82353 | 2025-11-09 05:29:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 42d87379-abed-3003-8ba0-57334f30ffc0 | -3.99229 | -50.43502 | 2025-11-09 05:29:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d9410f99-7256-36aa-a5fd-504bf48354d7 | -6.647 | -63.1707 | 2025-11-09 05:29:00 | NOAA-21 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 80e06f39-a9d9-34ec-83de-04d74117dcea | -4.27969 | -49.90269 | 2025-11-09 05:29:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d0179263-8f78-3f8d-ac22-c6db642769e2 | -2.92209 | -52.51221 | 2025-11-09 05:29:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c9f1a867-05b4-3003-b380-77abddd619a7 | -3.14755 | -50.27191 | 2025-11-09 05:29:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7de02415-52e9-39fc-bcef-a0fede6dc2a3 | -3.40386 | -50.45728 | 2025-11-09 05:29:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 70626f78-e4f4-3127-b0e4-288d22526fb7 | -3.53577 | -50.85348 | 2025-11-09 05:29:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 641b5c2c-1267-3bf5-ac5d-58671cc71747 | -3.56096 | -51.12392 | 2025-11-09 05:29:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4d6e8654-18c9-36d9-a530-4c724272fe46 | -4.27537 | -49.90419 | 2025-11-09 05:29:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 69ee630f-f6e5-3978-bc25-f7382d30ff79 | -3.50133 | -50.0497 | 2025-11-09 05:29:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b278764a-45c4-38f0-8b5c-997e364b6619 | -1.65443 | -53.70911 | 2025-11-09 05:29:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0f149d0e-b0dc-335c-8e0a-96097b8fa3a6 | -2.26699 | -56.12107 | 2025-11-09 05:29:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3e4701ca-1b61-3cf8-ab91-4e71de438a17 | -3.43781 | -52.63772 | 2025-11-09 05:29:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4854eafa-84e2-39b6-b57c-604f8ef99925 | -3.14287 | -50.27678 | 2025-11-09 05:29:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 9a46113f-674c-343b-b6de-187c3ab7142a | -3.15039 | -50.60411 | 2025-11-09 05:29:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e34c4d39-2e01-305a-bb10-2f0a503f89d3 | -2.44703 | -55.41167 | 2025-11-09 05:29:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2f10f386-5d3a-39e0-9b04-ceebf0634462 | -2.26003 | -47.87908 | 2025-11-09 05:29:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 04465815-3061-31a5-9479-8f7a6eeb4c8c | -2.60525 | -49.23238 | 2025-11-09 05:29:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 1a48bbed-2381-3cb1-a545-89be23f5caab | -10.94773 | -59.09737 | 2025-11-09 05:29:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5d1d841d-ede0-3c4e-9f85-affb3a45803f | -3.75618 | -52.0997 | 2025-11-09 05:29:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ad451879-d464-3a90-86f5-d0ba6254903f | -6.63179 | -56.28748 | 2025-11-09 05:29:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e6c37139-82b2-35d9-927a-f92f6590b4c9 | -3.14486 | -50.2899 | 2025-11-09 05:29:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a7f556a9-85d7-3820-b297-beefffdbab90 | -3.87459 | -52.13772 | 2025-11-09 05:29:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d328e68c-dd4f-3288-a1bf-94b9dc46a3fc | -3.32462 | -53.35794 | 2025-11-09 05:29:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bb336434-6736-31ba-b20e-35bb1627d4ca | -4.25418 | -48.63588 | 2025-11-09 05:29:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 9e2b6a05-4ab7-33cb-9052-4d82ad6922a6 | -3.09095 | -50.32257 | 2025-11-09 05:29:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| a54ec5a0-02fe-3598-88e2-a3ea64e9be61 | -6.80545 | -59.42345 | 2025-11-09 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a92fbb65-7a59-34e9-8e8f-e55a06f2e9c7 | -4.28605 | -50.66654 | 2025-11-09 05:29:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |


[Clique aqui para ver as próximas entradas](README35.md)
