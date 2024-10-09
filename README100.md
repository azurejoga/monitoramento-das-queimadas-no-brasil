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

## Dados Diários - Página 100

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c9bcec74-31e5-340a-853d-10ec34ce4071 | -17.12431 | -57.44227 | 2024-10-09 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 12.8 |
| c0845177-a8ae-3971-a260-e8745ba74421 | -17.12323 | -57.44709 | 2024-10-09 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 12.8 |
| 7861202b-0dd2-3212-bf8c-34a2fb4ce2ea | -18.60525 | -57.23899 | 2024-10-09 04:17:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| ff133b93-85f4-31c3-8e6e-67e7b7b5f241 | -17.12215 | -57.45192 | 2024-10-09 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 23.8 |
| be67edbe-d311-3784-bd56-52e8bedf191d | -17.11933 | -57.43608 | 2024-10-09 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.4 |
| afb6f795-81ca-33ff-9744-24dd20ff85ef | -17.11825 | -57.44088 | 2024-10-09 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 14.9 |
| f64fbf6c-0abd-3ee7-8bb2-7217e6d52974 | -17.11718 | -57.44569 | 2024-10-09 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 14.9 |
| 61004a6e-7bfc-3a53-88b2-17a9306bfeff | -17.11609 | -57.45052 | 2024-10-09 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 15.6 |
| 226d6fc0-469c-34ef-b642-787f6bae33a5 | -17.11501 | -57.45535 | 2024-10-09 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 15.6 |
| 2a215aa8-e475-3a55-958d-ce2e96ecfc62 | -18.60418 | -57.23728 | 2024-10-09 04:17:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 45310126-bd8d-3523-8587-9021d915c6b1 | -18.59952 | -57.26551 | 2024-10-09 04:17:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.6 |
| af8e00f5-8a55-3967-8741-24ab4b6407df | -17.15493 | -57.41907 | 2024-10-09 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.1 |
| 10b91086-9b7c-37df-8393-18e24bb8c8e9 | -17.15386 | -57.42387 | 2024-10-09 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.1 |
| 9e895959-8633-35b7-a614-69f972323260 | -17.15457 | -57.44934 | 2024-10-09 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 72.4 |
| 6f2920ea-1317-3e75-9d4c-0aecaef060dc | -17.1528 | -57.42867 | 2024-10-09 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 19.3 |
| 38704def-209c-3924-aeeb-30c7d2fce6b0 | -17.15173 | -57.43348 | 2024-10-09 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 19.3 |
| 00d54b68-afbc-3768-aabf-f59453f6e360 | -17.15066 | -57.4383 | 2024-10-09 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 68.3 |
| c52c5e9c-712e-3bf1-922b-24fee2fbd0d1 | -17.14959 | -57.44312 | 2024-10-09 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 68.3 |
| 38bce9c1-b48b-3eae-92a6-808f4c680113 | -17.14852 | -57.44793 | 2024-10-09 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 72.4 |
| 8ca9c1c2-29ed-3f94-902d-f8ba616e479a | -17.14745 | -57.45276 | 2024-10-09 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 72.4 |
| 63ccb00b-e6e3-33cd-bb01-054ad8c124bb | -17.14569 | -57.43205 | 2024-10-09 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.7 |
| 45d60a61-3e07-32bf-979a-e2b4d27f0eb3 | -17.14462 | -57.43686 | 2024-10-09 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.9 |
| bff9a2bc-6a43-3dc4-9a6b-5135316342ba | -17.14354 | -57.44169 | 2024-10-09 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.9 |
| ee0b5f2c-d194-3093-92ed-db7e0ee12e6a | -17.14247 | -57.44651 | 2024-10-09 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 16.7 |
| 12192aa0-df31-3d86-87a3-f9866d857767 | -17.14139 | -57.45134 | 2024-10-09 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 16.7 |
| 4cbcb017-a692-3556-9292-0de020a9c8cd | -17.14032 | -57.45617 | 2024-10-09 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 17.2 |
| b751ac0b-a63c-3a1a-b910-e30696d4834e | -17.13964 | -57.43065 | 2024-10-09 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.7 |
| 1864dec5-2e85-3ab0-a91d-1eba96be83a4 | -17.13856 | -57.43547 | 2024-10-09 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.9 |
| 090e7835-c8e5-3668-9e43-38d45e877754 | -17.13749 | -57.4403 | 2024-10-09 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.9 |
| 4ae6244e-4dd4-3ac3-9668-63d4561f69ea | -17.13641 | -57.44511 | 2024-10-09 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 16.7 |
| 2d5d6804-bba2-32ac-a38d-b9c7e402d941 | -18.72089 | -57.36817 | 2024-10-09 04:17:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| d3b9b276-946b-300a-a538-dcc481f070ae | -18.67679 | -57.21302 | 2024-10-09 04:17:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| f29538bf-7977-3a38-9b56-5317e00d77ac | -18.67583 | -57.2174 | 2024-10-09 04:17:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 567833dc-ee7d-39a5-9abe-a79a9d29a4f7 | -18.6594 | -57.20884 | 2024-10-09 04:17:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.6 |
| c40be639-dcaa-36de-9e43-486e0eb213a0 | -18.65263 | -57.21184 | 2024-10-09 04:17:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.6 |
| f32859ba-df22-367b-b69c-35fc106dc7b2 | -18.59848 | -57.242 | 2024-10-09 04:17:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.2 |
| 33ccf6a4-097c-37a6-8186-3e6afc9cfa8f | -18.59827 | -57.2637 | 2024-10-09 04:17:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.8 |
| 6d2fca82-1482-34fe-a6c7-ffbd61d63144 | -18.59753 | -57.2464 | 2024-10-09 04:17:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.2 |
| bd68f8f5-5eb3-3b0c-96b0-52a4444fbcd5 | -18.59738 | -57.2403 | 2024-10-09 04:17:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.4 |
| 3907f0f6-af63-3a1a-bb70-3f3e935ccd4b | -18.59728 | -57.26811 | 2024-10-09 04:17:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.5 |
| 638073cc-c6e2-35b8-9f13-4ecbce6dea78 | -18.59657 | -57.25083 | 2024-10-09 04:17:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.8 |
| 421ea89a-c21a-3aa9-983e-edccf8240fa0 | -18.5964 | -57.24467 | 2024-10-09 04:17:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.4 |
| e8a1bad3-9cc9-39b0-bf57-101fc27cd4ec | -18.59561 | -57.25525 | 2024-10-09 04:17:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.8 |
| f7d1b0b4-50fd-3bdf-95e5-7a1237c4bac4 | -18.59465 | -57.25967 | 2024-10-09 04:17:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.6 |
| 4c46d3eb-6de5-32a4-9372-16e34ff8fa56 | -18.59442 | -57.25349 | 2024-10-09 04:17:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 19.0 |
| 6a8180dc-0e84-38e3-9f77-64377ce3b9e7 | -18.59369 | -57.2641 | 2024-10-09 04:17:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.6 |
| 82be6f55-bb24-32dc-ac42-e48e522c4698 | -18.59343 | -57.25791 | 2024-10-09 04:17:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.8 |
| decedbe2-9ece-306f-ab0e-f20143d460e4 | -18.59245 | -57.26232 | 2024-10-09 04:17:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.8 |
| bd470687-6f6a-34d9-9491-11a0659d1f13 | -9.72483 | -57.80145 | 2024-10-09 04:17:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| dcb63f5c-4e0b-3cee-9b4e-c4fb71f61795 | -9.48144 | -57.92996 | 2024-10-09 04:17:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| b08cdc95-237d-3c04-82f2-808f43e93e59 | -10.33403 | -57.50523 | 2024-10-09 04:17:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| bfd6c58f-2a7a-3587-81d1-26ba18a732fa | -10.334 | -57.50444 | 2024-10-09 04:17:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2a7ada99-dc00-38c8-9415-44134b4dfaea | -10.3327 | -57.51094 | 2024-10-09 04:17:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 892f31c5-a1c7-320e-b136-fabd80d002d0 | -10.23162 | -57.82545 | 2024-10-09 04:17:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9ac1beaf-71ba-3b55-85a0-ef144bbe7680 | -10.22811 | -57.81688 | 2024-10-09 04:17:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ab4d9098-01f8-3c18-bdf6-11ede312e013 | -10.22673 | -57.82368 | 2024-10-09 04:17:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 80f21da4-7e06-3e77-930a-374172eeade1 | -10.22608 | -57.81707 | 2024-10-09 04:17:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 3dd08ce6-a198-3bca-9e73-421df1599b46 | -10.22465 | -57.82393 | 2024-10-09 04:17:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| eeb2c4f1-a2c9-3c49-8e1b-79f24ec9f15a | -10.12684 | -56.77268 | 2024-10-09 04:17:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7f14254a-5d38-38a8-b64a-1668b2c4c4dc | -10.12566 | -56.77842 | 2024-10-09 04:17:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ddc871bc-5195-3181-acdf-89cb4b2fe842 | -12.29672 | -57.88424 | 2024-10-09 04:17:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3bf228b7-57dc-3a89-b831-eeb4d6fe25c6 | -12.29206 | -57.87989 | 2024-10-09 04:17:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 92c67220-1299-3cef-b22a-4e6c30484c91 | -12.00283 | -57.82014 | 2024-10-09 04:17:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 00dfb24a-cf6e-3ff0-a74f-a643c40d1372 | -11.9961 | -57.81844 | 2024-10-09 04:17:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 043b5bf4-73aa-3eba-88f7-d895b6405b05 | -11.96306 | -57.59777 | 2024-10-09 04:17:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9dee803a-6e83-3a8c-b558-8ab0a4b15c85 | -11.96178 | -57.60389 | 2024-10-09 04:17:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 68599fe9-af83-39c4-a76a-c6e8ddfdfa52 | -12.29878 | -57.88156 | 2024-10-09 04:17:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5d830e0a-458c-3ff2-bba0-f3eb8100301c | -21.572 | -46.9898 | 2024-10-09 04:17:05 | GOES-16 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 076f8a8b-63bd-314c-b3c1-d953a5545b67 | -21.5727 | -46.9659 | 2024-10-09 04:17:05 | GOES-16 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 87.6 |
| cbeea676-a448-3793-98af-64101e81b847 | -19.26292 | -40.05001 | 2024-10-09 04:19:00 | NOAA-21 | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 9c48aeb5-cab7-3d4a-b740-35ca051e3b2a | -18.03894 | -39.92607 | 2024-10-09 04:19:00 | NOAA-21 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| c3e70bae-ee21-3491-aaef-e16e58367084 | -17.89462 | -41.44139 | 2024-10-09 04:19:00 | NOAA-21 | TEÓFILO OTONI | MINAS GERAIS | Brasil | 3168606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 43c1e416-e69b-33e1-b1d8-dbafe8056464 | -17.89343 | -41.42878 | 2024-10-09 04:19:00 | NOAA-21 | TEÓFILO OTONI | MINAS GERAIS | Brasil | 3168606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| e15732b6-0e5a-3a88-9f05-b6e4b976016f | -17.89275 | -41.42591 | 2024-10-09 04:19:00 | NOAA-21 | TEÓFILO OTONI | MINAS GERAIS | Brasil | 3168606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 0961dce7-2abb-38b7-b374-487da926ace7 | -17.89209 | -41.431 | 2024-10-09 04:19:00 | NOAA-21 | TEÓFILO OTONI | MINAS GERAIS | Brasil | 3168606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 28842e94-e8e2-3b83-8371-10753f244116 | -17.89522 | -41.43686 | 2024-10-09 04:19:00 | NOAA-21 | TEÓFILO OTONI | MINAS GERAIS | Brasil | 3168606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 63d66691-80c2-31bd-8ab7-18f403776a88 | -17.89587 | -41.43184 | 2024-10-09 04:19:00 | NOAA-21 | TEÓFILO OTONI | MINAS GERAIS | Brasil | 3168606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 87bd48c2-790b-35f9-be4f-d2d77afb9b16 | -18.66117 | -41.50864 | 2024-10-09 04:19:00 | NOAA-21 | DIVINO DAS LARANJEIRAS | MINAS GERAIS | Brasil | 3122108 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 257300d8-62dc-3c00-96cf-0f72e1f9eafc | -18.65799 | -41.50299 | 2024-10-09 04:19:00 | NOAA-21 | DIVINO DAS LARANJEIRAS | MINAS GERAIS | Brasil | 3122108 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 2f417f00-235c-3398-8dc2-8672116bd649 | -18.66188 | -41.5032 | 2024-10-09 04:19:00 | NOAA-21 | DIVINO DAS LARANJEIRAS | MINAS GERAIS | Brasil | 3122108 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 609f3975-c2c0-3531-88a6-cf119aa2ec55 | -18.63024 | -41.13121 | 2024-10-09 04:19:00 | NOAA-21 | MANTENA | MINAS GERAIS | Brasil | 3139607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 2c4d6ff4-66de-39e2-a360-e6cdd2137b0c | -18.62632 | -41.13064 | 2024-10-09 04:19:00 | NOAA-21 | MANTENA | MINAS GERAIS | Brasil | 3139607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| c274c9d0-7166-3a15-8d0c-dab17a09a93a | -19.41521 | -41.72926 | 2024-10-09 04:19:00 | NOAA-21 | ALVARENGA | MINAS GERAIS | Brasil | 3102209 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 3211fc69-d28e-3233-b7cb-31d72f627f3d | -17.38027 | -42.63608 | 2024-10-09 04:19:00 | NOAA-21 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9514ad0d-52d0-35b1-8ad9-88b14b8994cd | -17.37435 | -42.62659 | 2024-10-09 04:19:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ce6e7973-1521-3d3b-9810-1683b1d67047 | -17.37079 | -42.62603 | 2024-10-09 04:19:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3ec5782d-7ebe-3553-b857-c8cffbfdaee3 | -17.36899 | -42.63868 | 2024-10-09 04:19:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a6d2cca2-a913-3370-8889-892d09c82f31 | -17.36603 | -42.6339 | 2024-10-09 04:19:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 768c02f1-bae7-36c2-afcc-aaddf070178c | -17.36543 | -42.63811 | 2024-10-09 04:19:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| aec7f5d1-4b14-327e-93bf-5ebebdb8eca4 | -17.36308 | -42.62913 | 2024-10-09 04:19:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 65483632-549d-3422-8e58-fcfaf1b5d783 | -18.06302 | -42.11063 | 2024-10-09 04:19:00 | NOAA-21 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 8fc3a77c-f053-3ad6-a70a-556c4ac49bd7 | -18.02172 | -42.08249 | 2024-10-09 04:19:00 | NOAA-21 | FRANCISCÓPOLIS | MINAS GERAIS | Brasil | 3126752 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| e0384558-24c0-32a4-9f92-e8256eb0973d | -18.01562 | -42.07965 | 2024-10-09 04:19:00 | NOAA-21 | FRANCISCÓPOLIS | MINAS GERAIS | Brasil | 3126752 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 22abd8ee-25a7-39ee-a717-2bc29c7b6bee | -18.01143 | -42.13081 | 2024-10-09 04:19:00 | NOAA-21 | FRANCISCÓPOLIS | MINAS GERAIS | Brasil | 3126752 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 1350462b-63ab-30f2-9199-c93cb972c9e0 | -18.00755 | -42.13721 | 2024-10-09 04:19:00 | NOAA-21 | FRANCISCÓPOLIS | MINAS GERAIS | Brasil | 3126752 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 4f913744-8976-3658-a1ee-d5d017e75ea0 | -18.00345 | -42.13436 | 2024-10-09 04:19:00 | NOAA-21 | FRANCISCÓPOLIS | MINAS GERAIS | Brasil | 3126752 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| b275278c-1911-3381-874b-df2f93b5ac98 | -18.01862 | -42.07758 | 2024-10-09 04:19:00 | NOAA-21 | FRANCISCÓPOLIS | MINAS GERAIS | Brasil | 3126752 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| ca87968c-86b0-382f-8234-ea43ff04243d | -18.00714 | -42.13485 | 2024-10-09 04:19:00 | NOAA-21 | FRANCISCÓPOLIS | MINAS GERAIS | Brasil | 3126752 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| c5ada234-3b61-3c42-842b-798f54aedaaa | -17.67936 | -42.74269 | 2024-10-09 04:19:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 124ba9d3-c5db-3419-8ee0-bc07e829aeea | -18.01186 | -42.13323 | 2024-10-09 04:19:00 | NOAA-21 | FRANCISCÓPOLIS | MINAS GERAIS | Brasil | 3126752 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |


[Clique aqui para ver as próximas entradas](README101.md)
