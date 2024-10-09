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

## Dados Diários - Página 163

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a534614d-e0aa-34ba-9317-6cf24cdc1790 | -3.8476 | -49.45427 | 2024-10-09 05:01:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2957531f-6f45-322a-b320-c3b67b4afe79 | -3.84701 | -49.45816 | 2024-10-09 05:01:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7c96a681-8b98-3b0f-a5e0-bcd90cedd9cc | -3.84338 | -49.45364 | 2024-10-09 05:01:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1d6a6399-b2e8-32ef-9eef-456f15b1f1d6 | -3.8428 | -49.45752 | 2024-10-09 05:01:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6625b9ca-190d-393d-a5ee-1b280279476a | -3.80806 | -49.48806 | 2024-10-09 05:01:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d063b996-3d0a-3b0d-81da-fcf574ad71da | -3.70518 | -50.1748 | 2024-10-09 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| bb3f5734-53cd-3fd1-bdd6-8d2bd31295bf | -3.70466 | -50.17827 | 2024-10-09 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e999859a-f552-30d0-b325-cafc309d82b9 | -3.70117 | -50.17419 | 2024-10-09 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1dc01a7c-1dbe-38cf-8509-78dd94143e43 | -3.70065 | -50.17765 | 2024-10-09 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4bf7a598-8585-39d7-ab0b-a442822d6c25 | -3.69314 | -50.17302 | 2024-10-09 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 850eb9b6-46c9-3b5c-8b8f-b650b37dd97b | -3.69262 | -50.17646 | 2024-10-09 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 02a5e28b-6c1e-389d-9273-7bcd2ddd6d9b | -3.69239 | -50.12296 | 2024-10-09 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 292c2858-64b4-3ab8-b602-f5db24bd53ba | -3.69186 | -50.12649 | 2024-10-09 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5968c024-90df-36b9-878f-edc76ab005d6 | -3.68836 | -50.12236 | 2024-10-09 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 24102319-6aa2-34d9-8980-85084708176e | -3.68784 | -50.12586 | 2024-10-09 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 77aff3fe-a2b8-3607-a716-ac8ad55fa43a | -3.59108 | -50.5579 | 2024-10-09 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7183a29d-74c9-3360-87f5-a51f98a7767a | -3.57937 | -50.3982 | 2024-10-09 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 748c8851-1456-385d-a42f-a81374922e01 | -5.06257 | -50.66332 | 2024-10-09 05:01:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e1598066-76e3-39a0-a16e-7e2253e4f14a | -5.01909 | -50.87269 | 2024-10-09 05:01:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8ab47952-6d19-32a0-a2ff-1a3a96280f32 | -6.48797 | -49.91318 | 2024-10-09 05:01:00 | NOAA-20 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0fd7cf4b-e544-3b7c-adcd-17c71401da6c | -6.48739 | -49.91709 | 2024-10-09 05:01:00 | NOAA-20 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2e62f11a-59ea-31c2-bb21-34930509547a | -6.48371 | -49.91258 | 2024-10-09 05:01:00 | NOAA-20 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3ac59476-47c2-3835-8a71-be487c8e71fc | -6.43525 | -50.12533 | 2024-10-09 05:01:00 | NOAA-20 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1250fd8e-9089-3f6e-bc89-7234631a0e7e | -6.31623 | -49.99554 | 2024-10-09 05:01:00 | NOAA-20 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| dcf28148-c11a-3696-a436-7643115f7089 | -6.31572 | -49.99904 | 2024-10-09 05:01:00 | NOAA-20 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d779926c-e350-3a5c-a0e1-d6fce29c1ad1 | -6.17715 | -50.89707 | 2024-10-09 05:01:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a7d44594-e981-306e-a546-bbfc8fb15717 | -6.12512 | -51.13993 | 2024-10-09 05:01:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 10769447-aaa5-3bc7-bca4-d86d6b88b439 | -6.12218 | -51.13673 | 2024-10-09 05:01:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| bac40d5b-f44d-3538-a2f0-385d27c39ced | -6.12127 | -51.13905 | 2024-10-09 05:01:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e9baea45-8a5b-3b5a-b018-b4bee2cdd8df | -5.9936 | -51.05679 | 2024-10-09 05:01:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4de3c7fd-6060-39bb-943c-3ee942711c00 | -5.853 | -49.94194 | 2024-10-09 05:01:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fb0b0bbe-1c73-32c7-8d29-f244b3a6c492 | -5.84773 | -49.83265 | 2024-10-09 05:01:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 9a856541-ad22-32eb-a7d2-095cd955c505 | -5.77952 | -50.20634 | 2024-10-09 05:01:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 95881950-58f2-3736-a81b-1a0828b6e60f | -5.72355 | -50.05673 | 2024-10-09 05:01:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cabe2072-ddfb-36a2-bae9-fc848ded971d | -5.71653 | -49.98956 | 2024-10-09 05:01:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 222288b7-767d-3260-b691-92b3a74404a3 | -5.70378 | -49.96009 | 2024-10-09 05:01:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 22be89a8-9ff8-31ee-a257-5a072ea4c8e2 | -5.64074 | -50.12898 | 2024-10-09 05:01:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 138d48a1-9cdf-3fde-9baa-73addf063526 | -5.52171 | -49.98981 | 2024-10-09 05:01:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3a44c5fe-aae0-3add-adca-952a582af724 | -5.44659 | -49.56641 | 2024-10-09 05:01:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 91ac8009-a136-363b-9440-82386b597b70 | -5.44599 | -49.57042 | 2024-10-09 05:01:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 9048f46d-9c91-39ef-9476-64148a023129 | -5.44289 | -49.56177 | 2024-10-09 05:01:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 28273fa3-5b9d-337f-8698-4f3455116910 | -5.4423 | -49.56578 | 2024-10-09 05:01:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 2fe66fab-26fd-3118-8e3c-01cb521873bc | -5.4417 | -49.56979 | 2024-10-09 05:01:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| ffac5b46-e90b-3e45-9e3c-78a9947221f0 | -5.26601 | -50.88322 | 2024-10-09 05:01:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c82f85ab-247c-3c87-9744-1ed1410856aa | -6.90873 | -51.26118 | 2024-10-09 05:01:00 | NOAA-20 | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cfceb088-5971-3f78-a480-0e3c640be2ba | -6.84111 | -51.06895 | 2024-10-09 05:01:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c3346a95-ce18-3dd2-badc-8fe87800db9c | -8.81897 | -50.53735 | 2024-10-09 05:01:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| db1fd1ea-a66b-3ed4-b7d8-938244d064ac | -8.5649 | -50.53197 | 2024-10-09 05:01:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4a3adb49-2b58-3b0b-b4bc-2dfc9efc1a87 | -8.56069 | -50.53136 | 2024-10-09 05:01:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ede19651-6fee-314f-8a9a-68c929b62ba0 | -8.55705 | -50.52681 | 2024-10-09 05:01:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6d9f900e-ae2d-3537-9850-e54fd4372d68 | -2.14958 | -50.88921 | 2024-10-09 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b52c7f8f-6b60-3ac6-bba8-bb1141e66641 | -2.14679 | -50.88661 | 2024-10-09 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 724df958-340a-374d-8022-52b18345b7eb | -2.14611 | -50.89115 | 2024-10-09 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fd28eab0-0b6e-390e-a9d4-3544dc89e84d | -2.14582 | -50.88863 | 2024-10-09 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2f44589a-98e7-3de4-975d-d5e00f315b99 | -2.14304 | -50.88603 | 2024-10-09 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 86f96989-028d-3376-8cd2-5f6f622012a1 | -2.14207 | -50.88805 | 2024-10-09 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 42819daa-c5d1-3409-89c8-147ebd9a2965 | -2.13976 | -50.70506 | 2024-10-09 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 573092ca-dc7b-3ae9-a437-1d66c0d12ad0 | -2.13596 | -50.70447 | 2024-10-09 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f4d11ebd-ad5e-38f6-b8b6-14d07771956c | -2.12386 | -50.70734 | 2024-10-09 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ec787b11-792a-3ad6-a3e7-cdef21946801 | -1.95969 | -50.84336 | 2024-10-09 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b9fc5037-4db5-3578-af68-9ab9fece9604 | -1.959 | -50.84791 | 2024-10-09 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5846e265-148b-395d-ac81-6b5bd28c4a08 | -1.79088 | -51.06584 | 2024-10-09 05:01:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a2538c53-d3a7-3ede-98c5-1a318c117534 | -1.78823 | -51.06692 | 2024-10-09 05:01:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0c82bb79-8ccc-39de-bbd3-0ceac1718a63 | -1.55317 | -51.22815 | 2024-10-09 05:01:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 43525a21-f16a-3085-8b9c-675fd3d27afb | -1.55296 | -51.22935 | 2024-10-09 05:01:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 93695789-d861-3107-bfdf-e5d5a7604a15 | -1.26814 | -51.60966 | 2024-10-09 05:01:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8c5d987d-2897-32a5-a1f8-686d0a02f020 | -1.2675 | -51.61372 | 2024-10-09 05:01:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2ddbffe8-cd7d-3333-b837-8782c6cb13b9 | -3.63079 | -51.17962 | 2024-10-09 05:01:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 56709c21-34a0-33e4-b298-29b401f2b0ab | -3.59799 | -51.3729 | 2024-10-09 05:01:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2eb6f91f-bdaa-342b-8b37-8686a9e1041c | -3.59732 | -51.37735 | 2024-10-09 05:01:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c96a81da-fa92-36b2-b8bc-8c7edd4a5dbb | -3.59605 | -51.3746 | 2024-10-09 05:01:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dbd3bf70-fd24-3e67-9e97-7db01a4c85e2 | -3.55119 | -51.29455 | 2024-10-09 05:01:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9ab65118-bbc0-3077-89ff-36d1c8d94698 | -3.48526 | -50.80993 | 2024-10-09 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 2052f9cc-4269-3c02-b6ef-02098680500b | -3.48142 | -50.80933 | 2024-10-09 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 27831a72-4c95-368d-9afd-e4268fb5cebd | -3.4359 | -51.53544 | 2024-10-09 05:01:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 96f8dde7-38de-38a6-9d61-c4847e8d71b5 | -3.25915 | -51.58949 | 2024-10-09 05:01:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d8ec8712-ffcc-37d0-b4f1-a1b40a41c763 | -3.22846 | -50.85143 | 2024-10-09 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 40207ae8-22a9-31b5-84df-75dcab7cafef | -3.22066 | -50.92657 | 2024-10-09 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 26d8c45c-4ad5-3fb9-8873-6546d7f8515d | -3.22033 | -50.92413 | 2024-10-09 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 00c6a9ff-5364-359e-8207-4572b2525785 | -3.21758 | -50.92135 | 2024-10-09 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e4b2cc29-c4cb-3766-ad2f-06ae0775504f | -3.21378 | -50.92077 | 2024-10-09 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 14b8f5b4-52ea-3d93-b7e4-80b220b662cb | -3.20997 | -50.9202 | 2024-10-09 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f2762cd0-c7e2-3f2e-95b8-9e4a30f015f2 | -3.20689 | -50.915 | 2024-10-09 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fdfae17c-dd45-397b-8eef-2665ffb7ae40 | -3.20617 | -50.91965 | 2024-10-09 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| edafcba4-beb1-3cff-a0b8-337d0a49bdf6 | -3.20308 | -50.91445 | 2024-10-09 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fa05b061-4754-355a-b949-07b8bd52f9a0 | -3.20236 | -50.91908 | 2024-10-09 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9aadb6a5-9ccd-3f6b-8f69-d2feb71e7765 | -3.14735 | -51.20018 | 2024-10-09 05:01:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5464f4f2-d8d7-306b-8a8a-4472dc94ed42 | -3.1436 | -51.19968 | 2024-10-09 05:01:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e5a4dbee-36bd-39c5-9982-fdb12e5d3329 | -3.13797 | -51.28558 | 2024-10-09 05:01:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 631720ec-7deb-3725-a075-459c0e6e3339 | -3.051 | -51.14607 | 2024-10-09 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 63e31cd4-3dcd-3856-97d4-26038e6eafb9 | -3.05049 | -51.09969 | 2024-10-09 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3d891f0b-cd71-3e51-b76a-dd3405e09b7f | -3.04974 | -51.35007 | 2024-10-09 05:01:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 303f1e24-3eb5-3ed8-b30d-4bba4c16b99e | -3.04867 | -51.3484 | 2024-10-09 05:01:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d2ef005a-bc01-3d96-b7f7-d7723a04718b | -3.04726 | -51.1455 | 2024-10-09 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 295eccd8-e0f3-313e-8712-8232c57aa9fc | -3.04673 | -51.09916 | 2024-10-09 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 125ed75a-0576-344b-8714-9bdb6781ad0a | -3.04657 | -51.14998 | 2024-10-09 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c0627957-fdae-3bf6-a19d-dfc016de9737 | -3.03342 | -51.11082 | 2024-10-09 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ce200eeb-7356-39b0-a94a-66a5770a3287 | -3.03035 | -51.10575 | 2024-10-09 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7bd49bb2-f87e-39d2-8093-536f511ae200 | -2.97225 | -51.02972 | 2024-10-09 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 92057339-83d9-3efb-a2c9-e2a13e2b9b3c | -2.96848 | -51.02914 | 2024-10-09 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |


[Clique aqui para ver as próximas entradas](README164.md)
