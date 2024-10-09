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

## Dados Diários - Página 209

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 99d7f239-1b67-391a-a3aa-02a4c128580f | -10.29932 | -68.68868 | 2024-10-09 05:55:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 246ed4d5-23b4-3aa5-930f-511efd10686d | -10.29834 | -68.73886 | 2024-10-09 05:55:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a9779cbd-370c-3ef1-b76b-1063e3d654d5 | -10.29546 | -68.69167 | 2024-10-09 05:55:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0b719311-a82d-37ae-99f9-8bea308ead34 | -10.24896 | -68.28617 | 2024-10-09 05:55:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b564e383-b5b8-36ef-b844-ce88456e5016 | -10.24787 | -68.29329 | 2024-10-09 05:55:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a7f57e5a-9b31-39d9-838b-d4879f2cb324 | -10.24732 | -68.29685 | 2024-10-09 05:55:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 96e1c360-603c-3c73-a624-86c66d461fbb | -10.24562 | -68.28564 | 2024-10-09 05:55:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cc925394-2e8a-3b1c-952f-9fe63dde342a | -10.24508 | -68.28921 | 2024-10-09 05:55:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5216dd65-e2ac-330e-a39e-4cd011f9aa25 | -10.24453 | -68.29276 | 2024-10-09 05:55:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 65e26bd1-def4-3082-b8ac-6d8615928365 | -10.2412 | -68.29224 | 2024-10-09 05:55:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cec7b7a5-edff-3842-98c6-d33de2a6c6cc | -10.22393 | -68.66967 | 2024-10-09 05:55:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| aa81b4be-67dc-35d7-b630-78b7a6f0f6e0 | -10.19403 | -68.29167 | 2024-10-09 05:55:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d0e2eaf1-fbfc-3f34-b6a4-ee172607ccc9 | -10.19015 | -68.29471 | 2024-10-09 05:55:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6124c31d-526f-3be4-a1c9-68be19e0bb0f | -10.16921 | -68.36414 | 2024-10-09 05:55:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 6b38d94a-63d6-32f9-8c97-e20caba496f4 | -10.14378 | -68.39646 | 2024-10-09 05:55:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 994958b2-1436-3ff7-ae8c-d2cd1fa00368 | -10.14324 | -68.4 | 2024-10-09 05:55:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 989f0c91-f4ae-36a8-b78b-9ff1b3488f32 | -10.14046 | -68.39594 | 2024-10-09 05:55:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b3de7be8-0c64-30ca-bbd7-cda21157ae34 | -10.13991 | -68.39948 | 2024-10-09 05:55:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ee91a590-356a-3da0-90ba-45a87ae5f433 | -10.13713 | -68.39541 | 2024-10-09 05:55:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 160aef63-f39f-3296-a71d-742e687e780c | -10.13441 | -68.4131 | 2024-10-09 05:55:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d7eadbbb-acc6-3df1-a381-1d8af04c0836 | -10.13108 | -68.41259 | 2024-10-09 05:55:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 93ffc5a6-cdae-3170-8f3a-8e72fb2a3e79 | -10.10719 | -68.3907 | 2024-10-09 05:55:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 055648b4-caed-3a2f-8fa7-93503e42f3c4 | -10.10664 | -68.39425 | 2024-10-09 05:55:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4efcc538-a45c-3aa3-9661-53450603dc3c | -10.10556 | -68.40134 | 2024-10-09 05:55:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f70e7cf2-8d93-30f3-bd07-c8245ca04bdd | -10.10502 | -68.40488 | 2024-10-09 05:55:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2d9b9171-d280-347d-b331-1557e1c2e2cd | -10.10332 | -68.39373 | 2024-10-09 05:55:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 72ae5bb7-c6a4-3019-97e1-32293f6e7d4a | -10.10223 | -68.40082 | 2024-10-09 05:55:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6dca4a4e-9d5b-3321-8e7e-29dadedb7a7d | -10.08326 | -68.52443 | 2024-10-09 05:55:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f38f098c-e752-319b-936b-8291e785309b | -10.08194 | -68.46673 | 2024-10-09 05:55:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2876a68b-085e-3805-871b-86b5a51c9207 | -10.08139 | -68.47026 | 2024-10-09 05:55:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3554b5e4-0896-3f6f-b8e3-2ab354e7c87f | -10.07862 | -68.46621 | 2024-10-09 05:55:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b0f71be9-0847-3131-906e-a22a04a1c5e3 | -10.07807 | -68.46973 | 2024-10-09 05:55:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f3d76481-fed3-3ea9-8498-d354d35b3a48 | -10.07584 | -68.46215 | 2024-10-09 05:55:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 262decd8-4013-3fd6-ab3f-973eb3c09294 | -10.0753 | -68.46568 | 2024-10-09 05:55:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 92a25e5d-016d-38de-b297-4481fb69d6e2 | -10.06213 | -68.5286 | 2024-10-09 05:55:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 45588c23-12ca-3a45-a67b-44dd5c315b25 | -10.06159 | -68.53213 | 2024-10-09 05:55:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7f53b509-43e1-3aa3-9ff0-0f5c2695e4d4 | -10.05827 | -68.5316 | 2024-10-09 05:55:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| bc4517bf-87cd-3c8d-9e02-fc1db67b330b | -10.03544 | -68.45941 | 2024-10-09 05:55:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 512d71e9-e0c6-35d1-a6bb-4ba29e57e3d0 | -10.03211 | -68.45888 | 2024-10-09 05:55:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2bd89747-b0f4-3643-b8e9-4d295121489e | -10.0296 | -68.56311 | 2024-10-09 05:55:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ca482ac1-065d-39f6-a30f-5ba051f53ec4 | -10.01436 | -68.44162 | 2024-10-09 05:55:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6a3e9710-9d22-3849-8a84-da6fa8c83244 | -10.01382 | -68.44514 | 2024-10-09 05:55:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e42a1a3c-15d4-3490-9d7c-f37e3ff83a7c | -10.01049 | -68.44462 | 2024-10-09 05:55:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 325af707-b63d-3c76-b7c9-3628cf55346e | -10.00646 | -68.84305 | 2024-10-09 05:55:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| adf53ee7-7bb3-3319-8482-8d036c7168fb | -10.70835 | -69.07671 | 2024-10-09 05:55:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 982875c0-52b7-363a-b6a3-e33c11a10258 | -10.67498 | -68.85259 | 2024-10-09 05:55:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b552dd07-519a-3b99-bef4-1645314d0e0d | -10.66987 | -69.10641 | 2024-10-09 05:55:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c7474b6b-1789-3d65-ab9d-ccee4cd6e585 | -10.66711 | -69.10239 | 2024-10-09 05:55:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 13b127ee-20f2-3ce6-82b4-b34d23146e32 | -10.55754 | -69.1065 | 2024-10-09 05:55:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7abc9476-ec12-3108-9426-3a55ad6fcc03 | -10.50025 | -68.77467 | 2024-10-09 05:55:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3cad912b-6b80-3e12-9cdc-6e7cd4cf9cd5 | -10.43147 | -69.0436 | 2024-10-09 05:55:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 23e2154d-43a6-3098-98b8-fcc82298b664 | -10.39595 | -68.65704 | 2024-10-09 05:55:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9c607755-ac07-3c44-bf4d-1661923ae799 | -10.82636 | -68.3577 | 2024-10-09 05:55:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 20c0e560-9d14-36f8-938f-1e4d3f37f7ad | -10.82581 | -68.3613 | 2024-10-09 05:55:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fa6b477e-d5ba-330d-b2d2-3522e1e5bb22 | -9.62 | -67.48548 | 2024-10-09 05:55:00 | NOAA-21 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d8069436-fdd7-399f-bb1d-666b63afcd42 | -9.61944 | -67.48916 | 2024-10-09 05:55:00 | NOAA-21 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2b1ef3f8-bf88-3b78-86dd-a962ede2ecc5 | -9.61605 | -67.48862 | 2024-10-09 05:55:00 | NOAA-21 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4ad6982c-5404-38f6-8231-f55cee169722 | -10.93364 | -68.41158 | 2024-10-09 05:55:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6a98489b-2596-364b-b295-64477c317537 | -10.91416 | -68.40485 | 2024-10-09 05:55:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ec5311fd-f135-3343-87f8-f10197f97b0f | -10.9036 | -68.40688 | 2024-10-09 05:55:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b9f0bf60-5b53-3442-8b40-e61112987254 | -10.90081 | -68.40277 | 2024-10-09 05:55:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6f6d6b03-7c6a-393e-8f80-56c2100f6303 | -10.90026 | -68.40636 | 2024-10-09 05:55:00 | NOAA-21 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8704fa54-c1b8-3fa3-a674-b4db626344d9 | -10.88521 | -68.21278 | 2024-10-09 05:55:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| abcfec2b-5d9e-33c0-86d4-e5b6555e8817 | -10.883 | -68.21207 | 2024-10-09 05:55:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1897c463-13e7-35ef-9762-df00be5e2b16 | -10.88244 | -68.21569 | 2024-10-09 05:55:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 55813d75-e6db-3cfb-9735-e7ede6b198d5 | -10.87965 | -68.21154 | 2024-10-09 05:55:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e2184d6f-dc59-3cd2-804a-ef9f0af1a322 | -10.87909 | -68.21516 | 2024-10-09 05:55:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 09ad7539-a0a3-315a-b858-4505961b79ef | -10.9175 | -68.40539 | 2024-10-09 05:55:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 226af948-13e7-370a-9f51-1d790a7236d8 | -10.91361 | -68.40844 | 2024-10-09 05:55:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| db08089e-c50a-3819-bce4-0c1530c9450e | -10.91028 | -68.40792 | 2024-10-09 05:55:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fafac586-db49-3c63-94c0-5cd25108b7df | -10.90749 | -68.40381 | 2024-10-09 05:55:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 14c9f412-1c96-33a6-8807-d0e26c65814c | -10.9047 | -68.39971 | 2024-10-09 05:55:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2f2552ce-83c8-3a27-b567-51da386ddd33 | -10.90415 | -68.40329 | 2024-10-09 05:55:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 398d49f2-090c-3dd3-8a93-3490c921db2f | -10.89692 | -68.40585 | 2024-10-09 05:55:00 | NOAA-21 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1a7e775d-e5fd-3553-afdb-05f1f941e5fe | -10.88879 | -69.12029 | 2024-10-09 05:55:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 86f4fee7-3db4-379a-94e0-8a079d4ede06 | -10.87688 | -68.22957 | 2024-10-09 05:55:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| db52df50-7dec-38b5-afef-1a7538dc549a | -1.19729 | -54.22224 | 2024-10-09 05:55:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 37a70d4a-e5b1-3f0e-b105-999ca77ac34c | -1.13603 | -54.10831 | 2024-10-09 05:55:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 39a415be-3b96-3d06-99b8-347be9cc73d4 | -1.12002 | -53.61525 | 2024-10-09 05:55:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e9d14a8a-ea98-35fc-98a2-4e48c10cc563 | -1.11874 | -53.62363 | 2024-10-09 05:55:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 02aea54a-5176-3a95-8d30-b98792c7e3e7 | -1.11268 | -53.61592 | 2024-10-09 05:55:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 16.2 |
| ec1978fc-8b2c-3fa0-a42f-3ab0c7b20c47 | -1.11151 | -53.62358 | 2024-10-09 05:55:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 16.2 |
| a93c43b7-77e5-3f5d-a4c9-149ac74fa547 | -1.10888 | -53.61054 | 2024-10-09 05:55:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 2bb8f2a4-35ae-3f70-94e2-dc5690cfa226 | -1.10773 | -53.61778 | 2024-10-09 05:55:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 0e961530-fcce-3ffe-a31a-53b2638c00c1 | -1.02553 | -53.72742 | 2024-10-09 05:55:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 63df18c2-5ebd-3182-a9ea-e74bca16510c | -8.48732 | -55.16184 | 2024-10-09 05:55:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 80c518a1-49b0-320c-b88f-1cedc8ea494b | -8.48641 | -55.16906 | 2024-10-09 05:55:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 95a78dc8-0f29-3b70-892b-b20880dd00e0 | -8.30162 | -55.11245 | 2024-10-09 05:55:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 6117302a-f462-3702-82bb-356633ce7a2d | -10.63547 | -55.893 | 2024-10-09 05:55:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 2c872c2b-33ba-3167-bc69-8866787ffbcd | -10.63471 | -55.89963 | 2024-10-09 05:55:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| d5a1d2b3-8aef-3d20-b7c9-f644dff356ee | -10.63395 | -55.90629 | 2024-10-09 05:55:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| f5b7665b-cb7a-349f-a889-74b228aee990 | -10.62921 | -55.88572 | 2024-10-09 05:55:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 47a1b52d-fb35-3be1-b357-2658c3888008 | -10.62849 | -55.89206 | 2024-10-09 05:55:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| e1ecc1f8-90f1-3d2a-a7d5-2a0aaf670e76 | -10.62776 | -55.89845 | 2024-10-09 05:55:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| e2bdab7b-adf7-301c-bf5d-63422cc76a26 | -10.627 | -55.90516 | 2024-10-09 05:55:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| aa7231c5-40a6-3833-a4de-11870ae7f8df | -10.62622 | -55.91206 | 2024-10-09 05:55:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 58232df5-6782-3922-a9d3-c9568bf689c9 | -10.62543 | -55.91894 | 2024-10-09 05:55:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 10.2 |
| a4ac4c8c-5336-35fe-a284-4b2dc17708b1 | -10.62467 | -55.92569 | 2024-10-09 05:55:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 10.6 |
| c8d14585-3924-3c4e-9dca-57e329c14010 | -10.61848 | -55.91787 | 2024-10-09 05:55:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 6478caa2-6efb-36c6-a594-295963c747f9 | -10.6177 | -55.92474 | 2024-10-09 05:55:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 16.8 |


[Clique aqui para ver as próximas entradas](README210.md)
