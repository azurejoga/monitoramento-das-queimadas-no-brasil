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

## Dados Diários - Página 91

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 27c2a4ff-c469-3a5d-849d-5601065407bb | -10.43471 | -50.80315 | 2024-10-02 04:46:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1aa50d7b-b423-3cc5-b99a-41ffcd654229 | -10.43416 | -50.80673 | 2024-10-02 04:46:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ef6870cd-42dd-352a-a36f-8c2d3f3da756 | -10.85998 | -51.89793 | 2024-10-02 04:46:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9e76277a-79f9-3a4b-8a46-d4cc884e825d | -4.09377 | -51.12449 | 2024-10-02 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c1370711-2371-3015-90ac-626d844a6003 | -4.09431 | -51.12102 | 2024-10-02 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c9158830-3b53-3684-9ab1-7763593ddcc4 | -6.384 | -52.70752 | 2024-10-02 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1c2d3768-255d-3d6e-babe-bbed10bcf47c | -6.38278 | -52.707 | 2024-10-02 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7f4b49a6-d218-35b0-918f-07ed25189c0b | -6.56737 | -52.65435 | 2024-10-02 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a419939b-08ad-3f2b-a436-2a22f055873b | -9.06932 | -53.26885 | 2024-10-02 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0238792f-c7dd-34d8-8277-08dabb2aec60 | -9.0683 | -53.25366 | 2024-10-02 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 23b91507-7204-3009-9f68-53e7e9b84691 | -9.06771 | -53.25731 | 2024-10-02 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 54b37c92-ff76-3af2-925c-48be05727564 | -9.06492 | -53.2531 | 2024-10-02 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f54ee44f-2dbf-30d8-92e1-b16ff95c3b45 | -9.06433 | -53.25676 | 2024-10-02 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ab5a6604-4bbc-3208-95a9-91d81e2e7ab1 | -9.06374 | -53.2604 | 2024-10-02 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ca3e552c-de58-36dc-b4bb-f4a2a40f00a9 | -10.90849 | -52.4146 | 2024-10-02 04:46:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b6ffc5e9-376c-39ef-9e17-97ea2ed20ffc | -10.90574 | -52.41056 | 2024-10-02 04:46:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 0028f8c5-8ab5-3d08-83fa-ee1bc2466bfe | -10.90519 | -52.41406 | 2024-10-02 04:46:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 74eae49c-2ac5-3b89-b46f-b8fbd18944ae | -10.90463 | -52.41756 | 2024-10-02 04:46:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 290ecdfa-7652-3579-bf88-5388d840a2c8 | -10.90408 | -52.42105 | 2024-10-02 04:46:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1f35f93d-5e96-3291-89af-7c4734fe94ea | -10.90244 | -52.41003 | 2024-10-02 04:46:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7d05b748-8be4-39e8-9528-2c730cd6ca29 | -10.90188 | -52.41353 | 2024-10-02 04:46:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 76864d26-a5fa-3ac6-a7bf-95f242372cb3 | -10.90077 | -52.42052 | 2024-10-02 04:46:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9063689c-0529-33f5-b7b9-2bf0e9e67976 | -10.90022 | -52.42402 | 2024-10-02 04:46:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bb784bab-503b-3a65-9175-d45e6601e6df | -10.89913 | -52.4095 | 2024-10-02 04:46:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0f3fdfed-24ab-3911-b671-edb3092ee5d9 | -10.89858 | -52.413 | 2024-10-02 04:46:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a03cbd60-ec75-37eb-b6cf-2912d7839495 | -10.89691 | -52.4235 | 2024-10-02 04:46:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 04195686-7cf7-3dc7-8069-3d9bf5973c7f | -10.89486 | -52.41223 | 2024-10-02 04:46:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 183313c2-e570-39c3-8635-4c0e4cdf55bd | -10.89321 | -52.42272 | 2024-10-02 04:46:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| af1fca65-6df3-3f82-a812-a691861675c3 | -10.88935 | -52.42569 | 2024-10-02 04:46:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ed273dca-56db-315d-a251-0d7fd38351b5 | -10.88605 | -52.42516 | 2024-10-02 04:46:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 759889ce-b014-398a-bd05-46bdf5118623 | -10.8833 | -52.42112 | 2024-10-02 04:46:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 297e41bd-9679-35d3-a536-fa346856de38 | -10.88274 | -52.42463 | 2024-10-02 04:46:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0ab4eb2d-0cf5-3a2a-9b92-f9ef8160f6a2 | -10.87999 | -52.42059 | 2024-10-02 04:46:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b63a43c7-9bb5-3b8e-918f-0a672feb722b | -10.86556 | -52.55478 | 2024-10-02 04:46:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e6ed0ac7-4919-3ecd-9b54-d0d075846830 | -10.86225 | -52.55424 | 2024-10-02 04:46:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f8627a1c-b85c-38ea-b192-0ab58ed80cea | -10.44585 | -52.94609 | 2024-10-02 04:46:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 04523661-9ad5-39aa-a571-eccb1620a659 | -10.44528 | -52.94965 | 2024-10-02 04:46:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 967bdd9f-2e73-3210-ad28-cafb08d62f41 | -10.44365 | -52.93843 | 2024-10-02 04:46:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a866fed9-f7d4-3ee8-9c2a-4469e5d4d815 | -10.44308 | -52.94199 | 2024-10-02 04:46:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9618cebf-c9ae-349d-9272-ee3020300f93 | -10.43756 | -52.93381 | 2024-10-02 04:46:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4bfaaf6a-e380-3c6e-91c2-359968aa401f | -10.39484 | -52.92323 | 2024-10-02 04:46:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 96d900f8-3e9b-36ae-ace8-841cb01bc506 | -10.39151 | -52.9227 | 2024-10-02 04:46:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2d3a4091-aefb-3a3c-b091-c93406511221 | -10.39094 | -52.92624 | 2024-10-02 04:46:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5de4d337-b379-3d94-a08c-da76c8a546bc | -10.38704 | -52.92926 | 2024-10-02 04:46:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 51abe700-353f-3750-b448-a665e897076d | -10.22974 | -52.72158 | 2024-10-02 04:46:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d39d8d1c-b616-3237-a1fe-2a0228d2ef47 | -10.22918 | -52.72511 | 2024-10-02 04:46:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7ea3722e-e134-351b-99fd-fec695d32249 | -10.22204 | -52.70586 | 2024-10-02 04:46:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| be1de955-2245-3a04-8236-babd232a5e5f | -10.46714 | -53.32095 | 2024-10-02 04:46:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c6189c0c-72a0-31a6-b0ee-577d4b0cb247 | -10.04593 | -53.48753 | 2024-10-02 04:46:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0b99016d-6077-3f85-a5a8-eb9c4f68d160 | -10.03274 | -53.44029 | 2024-10-02 04:46:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e44c5533-ab3b-306e-83c9-0b325bd17ca6 | -9.83862 | -52.07554 | 2024-10-02 04:46:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1916c6f0-ae95-37db-9897-69683642d091 | -9.83807 | -52.07902 | 2024-10-02 04:46:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 693179dc-81ec-3829-81fb-b7a632d8aaba | -9.83641 | -52.06806 | 2024-10-02 04:46:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 08a4e59b-141f-3436-9c85-2b0c05027457 | -9.83586 | -52.07153 | 2024-10-02 04:46:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 13cebd29-122f-3d32-8fe9-7c04dd2c83e5 | -9.83311 | -52.06753 | 2024-10-02 04:46:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 941c7dd9-ab73-3956-a7ca-2fa7106c7924 | -9.75999 | -53.16836 | 2024-10-02 04:46:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 020c5c1a-f97a-36ec-b69a-f9043a2ecb44 | -9.75941 | -53.17196 | 2024-10-02 04:46:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 02b37caf-9b06-3228-b9b1-94d5c1ec2390 | -9.67853 | -53.1694 | 2024-10-02 04:46:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 31d799ce-b9f5-3f1f-b163-1ed69e4d6667 | -9.62989 | -53.40811 | 2024-10-02 04:46:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7836fe94-0a22-3fc9-bb34-59a1c9018fab | -9.6293 | -53.41177 | 2024-10-02 04:46:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 67cab92e-37e2-31ba-9117-466c689f3ad0 | -9.62592 | -53.41122 | 2024-10-02 04:46:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f52c393c-9c1f-3901-b117-d75c2d1d852c | -9.61796 | -53.41749 | 2024-10-02 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a9e2d775-4bfa-3816-8632-ceb047f43dbb | -9.61659 | -53.21134 | 2024-10-02 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 44281880-7da4-3667-af3a-ed5aa124e26f | -9.60046 | -53.26835 | 2024-10-02 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 91b98cc2-3841-3d1b-aedf-77b3de7c6a15 | -9.5971 | -53.26778 | 2024-10-02 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| de461f1b-93fc-38e7-b43d-9a0b3514e04b | -9.3945 | -53.19437 | 2024-10-02 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cdac0afe-2b8c-3656-bc9a-b3ba95d80234 | -11.08902 | -52.51912 | 2024-10-02 04:46:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f0aceae3-3ff6-3d51-8c2b-92ba9966ea98 | -11.08572 | -52.51858 | 2024-10-02 04:46:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e65bd025-1367-3f27-b882-de1f94a86662 | -11.08241 | -52.51804 | 2024-10-02 04:46:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3e2ca3b4-0696-3c5d-97df-d67e0ba4af59 | -11.08186 | -52.52155 | 2024-10-02 04:46:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 6211a9e5-361c-364e-ab50-8c2fc1a2d237 | -11.07911 | -52.5175 | 2024-10-02 04:46:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a01db012-65a1-3bc1-a8ff-3bf44e6d2104 | -11.07855 | -52.52101 | 2024-10-02 04:46:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 5b7bbe19-0a12-3dd2-89b7-d220d6416c54 | -11.078 | -52.52451 | 2024-10-02 04:46:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 0c9906b0-f460-3f5b-bd7f-7870c0a6cc7a | -11.07525 | -52.52047 | 2024-10-02 04:46:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 2868216e-4f56-3778-9ddf-8ca77c148043 | -11.07469 | -52.52398 | 2024-10-02 04:46:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 1a41d933-9873-379b-a254-511b51a3ffc8 | -11.07194 | -52.51993 | 2024-10-02 04:46:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 93e51ac0-74fc-33e3-8d76-0865b511c766 | -11.07139 | -52.52344 | 2024-10-02 04:46:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 9a508fae-0e64-3b50-b9be-b561625956c8 | -11.06864 | -52.5194 | 2024-10-02 04:46:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 6ec7a034-7a21-33a7-8ebb-94d392e8b553 | -11.06533 | -52.51886 | 2024-10-02 04:46:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 342ad9dc-77c0-3de2-b67d-553d56245524 | -11.06203 | -52.51834 | 2024-10-02 04:46:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2a71fe76-507e-3f27-8955-061248bc163f | -11.05819 | -52.49974 | 2024-10-02 04:46:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4808d70b-0548-36a5-9e46-9f6603e38e11 | -11.05489 | -52.49921 | 2024-10-02 04:46:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2b0b59b5-3723-34bb-94b8-16fe380147bf | -11.05158 | -52.49867 | 2024-10-02 04:46:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c1189749-af2a-345a-a976-ceafb2de9279 | -11.05103 | -52.50218 | 2024-10-02 04:46:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a743d84a-35ab-3ddb-a3a7-fb3b6de27a99 | -11.04828 | -52.49814 | 2024-10-02 04:46:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b14832e4-297f-3bce-9d43-084fc56426a4 | -11.04772 | -52.50164 | 2024-10-02 04:46:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4c07621f-e098-3a1a-98c6-7a40f1623852 | -11.04553 | -52.4941 | 2024-10-02 04:46:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| eec806c1-8bf1-3bba-a563-dd4826d18729 | -11.04497 | -52.4976 | 2024-10-02 04:46:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f9cc0366-955c-3f8e-b68d-9d4a4e4e6fbc | -11.04278 | -52.49007 | 2024-10-02 04:46:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0469e727-37c2-3ae6-997e-4c09e19c7b67 | -11.04222 | -52.49358 | 2024-10-02 04:46:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2bfaa539-99c5-3018-ba83-c896bcfd2f00 | -11.04169 | -52.47552 | 2024-10-02 04:46:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 60e7e496-538f-3618-a051-564058734e38 | -11.03894 | -52.47149 | 2024-10-02 04:46:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 36a93aa5-a342-30e7-97b7-357ad96d287c | -11.03564 | -52.47095 | 2024-10-02 04:46:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6d3ba96e-55de-3f05-9f4c-6a15b5b804eb | -6.58096 | -52.92288 | 2024-10-02 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2be13b1a-9189-3e63-938a-4f001c1ac71a | -6.58036 | -52.92657 | 2024-10-02 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ad562b08-0251-33d6-89ee-e55d6af3e2f8 | -6.57756 | -52.92234 | 2024-10-02 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5801699f-8507-3229-a2ad-2fde8e484853 | -6.57696 | -52.92602 | 2024-10-02 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7d2ded56-f7da-3c4a-a513-20943973a0c9 | -6.57355 | -52.92547 | 2024-10-02 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6940eae0-87ba-31e3-9e8a-dd744fb76159 | -6.23731 | -53.33173 | 2024-10-02 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3fad4039-9bfc-3f02-bcb9-a7629e453932 | -6.23668 | -53.33559 | 2024-10-02 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README92.md)
