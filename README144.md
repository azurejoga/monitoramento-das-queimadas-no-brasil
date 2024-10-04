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

## Dados Diários - Página 144

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7b86e97a-d03d-3e9f-a1f4-17ca13cc39e2 | -3.24671 | -50.36631 | 2024-10-04 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 7a6480eb-3c35-3b04-9c5c-c9023491aa8a | -3.24608 | -50.3704 | 2024-10-04 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| fd2abb03-4287-3a30-819d-c650cdffad27 | -3.24545 | -50.37449 | 2024-10-04 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d854a1bb-b66b-397e-8f07-f7bae0e52c6d | -3.24482 | -50.37859 | 2024-10-04 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 52e079c8-656e-3bc4-81c4-25878070b788 | -3.24375 | -50.36166 | 2024-10-04 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4e10cae8-ba1c-3751-9968-7146ac12fb72 | -3.24312 | -50.36575 | 2024-10-04 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| cdef2962-9784-3990-b3d4-dba02aedab97 | -3.24249 | -50.36985 | 2024-10-04 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 6c6b22de-91d5-3931-9333-0bbae9abcc00 | -3.24186 | -50.37394 | 2024-10-04 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f7f65a5c-f03d-3d33-8aab-3552f8496122 | -3.24123 | -50.37802 | 2024-10-04 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| bf79d7c5-cc9c-3aba-bfc4-1b1b773e1ac7 | -3.23953 | -50.3652 | 2024-10-04 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 49ec45d8-da7a-379d-890d-79c772166d48 | -3.23891 | -50.36929 | 2024-10-04 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| d4681d71-40f5-36e3-bf53-1896259db4d1 | -3.23828 | -50.37338 | 2024-10-04 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| df2f9fc9-2352-31f2-9147-6ec41808c8ae | -3.23532 | -50.36874 | 2024-10-04 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 9f8ebc67-b8d1-32b2-8369-7d3e4d982106 | -3.23469 | -50.37282 | 2024-10-04 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c857228f-2386-3013-a337-b0a2db6c5a68 | -3.20773 | -50.38129 | 2024-10-04 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| db0be13b-8ec3-31ae-9153-bc1068099bfc | -3.12961 | -50.18091 | 2024-10-04 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 533e14ad-c753-3cac-b3c2-b5c92b1bff02 | -3.12662 | -50.17623 | 2024-10-04 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2da5af4c-40d7-30de-ac7b-5408d002d3be | -3.12599 | -50.18039 | 2024-10-04 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| de97e37e-1c80-35fa-b4ff-a6f02c9562e9 | -2.79937 | -50.28619 | 2024-10-04 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 41a4e590-0921-30e5-a9d5-0b498a774daa | -2.79579 | -50.28563 | 2024-10-04 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8b387362-b244-3ba7-b03c-e1c1e4a99103 | -5.06069 | -49.79283 | 2024-10-04 04:55:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5aa6bd18-29e8-3cc7-866d-961773addf3f | -5.06 | -49.79744 | 2024-10-04 04:55:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4924e1dd-2081-3150-bf59-dd6cddf67664 | -5.02179 | -49.76796 | 2024-10-04 04:55:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cfd8ad6c-d4d9-380f-bdc2-36d29d69a28c | -5.02159 | -49.76989 | 2024-10-04 04:55:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 64accc89-3258-3dff-82b3-47c5faf0f858 | -5.02111 | -49.77261 | 2024-10-04 04:55:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| da20044f-aef0-3e15-96a6-3adc43877b6d | -5.0178 | -49.76931 | 2024-10-04 04:55:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6ff583b7-2507-3194-87c2-f658fc3610d2 | -5.01732 | -49.77204 | 2024-10-04 04:55:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| d5e18d63-f352-3cfd-8126-0a6dff2c392a | -5.01709 | -49.77394 | 2024-10-04 04:55:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f4f0d82a-8386-3b58-9438-a3c897e11a29 | -5.01189 | -49.78259 | 2024-10-04 04:55:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b727c360-01fb-32e2-980d-2331a8c9058b | -5.01119 | -49.78713 | 2024-10-04 04:55:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0333e9f8-9fae-38db-88ce-44251e212f84 | -4.65439 | -49.53638 | 2024-10-04 04:55:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cc899691-9aef-3484-9fea-96d019f34332 | -4.45242 | -49.62031 | 2024-10-04 04:55:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| b3582c65-9152-3a0a-9b5d-5be8754da86e | -4.38225 | -50.42688 | 2024-10-04 04:55:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 9cd4a3b5-1bd4-32a8-9aad-e353f80b1756 | -4.3812 | -50.42816 | 2024-10-04 04:55:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 19d12dd5-8de6-3d1e-b9d1-592139627ab8 | -4.37863 | -50.42631 | 2024-10-04 04:55:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2524e7ca-9545-38c9-80ad-d3222219e6e3 | -4.08555 | -50.45893 | 2024-10-04 04:55:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 34a1c40b-3ac3-3187-9c54-2fca8b03b8ca | -4.03943 | -50.38896 | 2024-10-04 04:55:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 184c7a7e-6e50-3751-996e-6eea5df2a9f6 | -4.03495 | -49.5667 | 2024-10-04 04:55:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6f81616d-d71a-3be2-91d5-a8c3c03d6f04 | -3.99184 | -49.6726 | 2024-10-04 04:55:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7833a4ff-a5c9-35ff-9a5d-15ead3156138 | -3.92777 | -49.68377 | 2024-10-04 04:55:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fc747936-002e-308a-bc30-10c221115c86 | -3.92706 | -49.68835 | 2024-10-04 04:55:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ad608554-ad83-3ad2-b357-f2ae7e88e287 | -3.9233 | -49.68784 | 2024-10-04 04:55:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8fa522d1-939c-3777-b164-696374824c60 | -3.92261 | -49.6923 | 2024-10-04 04:55:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 79d28bff-1ffd-34fa-beda-0c8762c8520d | -3.84437 | -49.39585 | 2024-10-04 04:55:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2903d5cb-9dfe-3848-9f65-0232a3b0077d | -3.56859 | -50.57867 | 2024-10-04 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ffc28c8d-dd17-3b94-aac3-4d286d2717fd | -3.56424 | -50.36917 | 2024-10-04 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| dc877d68-dc00-33cd-8744-5aa2283bd96c | -4.66396 | -50.88631 | 2024-10-04 04:55:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9efd00b9-f47d-3b97-bcea-03c6051a8c39 | -4.66102 | -50.88173 | 2024-10-04 04:55:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e477d4fd-0bc2-380a-9dca-8551994bf12d | -4.66041 | -50.88576 | 2024-10-04 04:55:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ad414500-0c1a-3fcd-ac15-91c6ee4ba43e | -5.89914 | -50.25898 | 2024-10-04 04:55:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8dced4a6-8090-3d2f-b08c-389cb21319fa | -5.64495 | -49.71469 | 2024-10-04 04:55:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 66f0b61f-d662-3970-8acc-2dc28bee0f3e | -5.64112 | -49.71412 | 2024-10-04 04:55:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 84411f0b-6a8f-3383-a36b-d82e493acf1f | -5.51427 | -50.04566 | 2024-10-04 04:55:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c0fb037e-2a1f-3857-945f-3f51ad9f7f6a | -5.51389 | -50.04311 | 2024-10-04 04:55:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e4b493fa-0914-345c-8bca-eec987aa2831 | -6.17946 | -50.90198 | 2024-10-04 04:55:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1a9233ad-bd9f-3842-8757-42e018bf2bfe | -5.53809 | -50.93917 | 2024-10-04 04:55:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3169ac44-8049-38cf-b986-cf5e144ed73a | -7.83308 | -50.52118 | 2024-10-04 04:55:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 134c4534-e224-3e5a-9278-2abad24c8931 | -7.83242 | -50.52578 | 2024-10-04 04:55:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 7d010ac2-77f9-3f3a-ae01-2a9ed23fbd39 | -7.83224 | -50.52327 | 2024-10-04 04:55:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| dffa3195-469b-3991-ba76-74c78d0024ea | -7.83175 | -50.53039 | 2024-10-04 04:55:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 0c0d7f04-d5a6-38e3-8110-6cad873d504a | -7.83154 | -50.52787 | 2024-10-04 04:55:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| e65c744f-afd3-365b-b91b-16f36e0d8b3f | -7.83109 | -50.535 | 2024-10-04 04:55:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3f952edd-0096-34cc-bcd3-56b434cb077a | -7.83085 | -50.53248 | 2024-10-04 04:55:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 02a0643e-fb31-3b09-8def-db3602dd2063 | -7.83042 | -50.5396 | 2024-10-04 04:55:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 703aa57c-2db7-30e6-9b5f-893c2a1f690f | -7.83015 | -50.53709 | 2024-10-04 04:55:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| ec534bd5-f446-3869-893d-6f3e1827eeb1 | -7.82932 | -50.52065 | 2024-10-04 04:55:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ff0afa7d-935e-33be-8191-6a06ca79ba79 | -7.82865 | -50.52526 | 2024-10-04 04:55:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| ead572a3-938d-3168-8a30-bd60aeb669c0 | -7.82847 | -50.52275 | 2024-10-04 04:55:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8ebc2bbd-ac77-3da7-a9c5-83dc9b84430f | -7.82798 | -50.52989 | 2024-10-04 04:55:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 967ef4b3-e1d3-3331-a265-48ce192b100b | -7.82732 | -50.5345 | 2024-10-04 04:55:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 577f6237-5e6d-30cb-9dcf-dfd7e864dfa7 | -7.82708 | -50.53198 | 2024-10-04 04:55:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| de77b8ab-1493-3f97-bee5-c696f6d7fa43 | -7.82666 | -50.5391 | 2024-10-04 04:55:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 229f7990-b97e-309a-a1bb-a812ac5e752a | -7.82639 | -50.53657 | 2024-10-04 04:55:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3ee988ef-6855-303b-bf64-43a7288b01e1 | -7.8229 | -50.53857 | 2024-10-04 04:55:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 91b3167f-023d-3b82-bc6d-d3e12c9c76c8 | -7.82193 | -50.54068 | 2024-10-04 04:55:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1fe9d1e8-1f23-35ee-95cf-9d590cb3ae84 | -7.82095 | -50.52168 | 2024-10-04 04:55:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 436c4221-9f5f-3780-8b85-bac8114e6046 | -7.82024 | -50.52635 | 2024-10-04 04:55:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1321a1a5-1832-39a6-8ceb-8b885ea98ed6 | -7.81955 | -50.53098 | 2024-10-04 04:55:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2b2c2966-6901-3a07-bf22-b8dbaaf2ed5e | -7.81886 | -50.53552 | 2024-10-04 04:55:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0c05e3cb-f9c6-3793-b3ca-6b84023ea517 | -7.81817 | -50.54012 | 2024-10-04 04:55:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 06378c96-ab64-38b7-a92d-4a2132785617 | -7.81718 | -50.52117 | 2024-10-04 04:55:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 642035e7-599c-38b6-8ae1-af5b149a082c | -7.81648 | -50.52584 | 2024-10-04 04:55:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 54099ade-ad4d-360c-861a-32c7cdde1ba5 | -7.37736 | -50.8084 | 2024-10-04 04:55:00 | NOAA-20 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 063d9be5-e81e-353f-97b3-fd7f2def9c8a | -7.02751 | -50.72799 | 2024-10-04 04:55:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5b8c1aa9-1c63-3131-83d7-8a52b2b03190 | -9.42871 | -50.68083 | 2024-10-04 04:55:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c0880141-63bf-3563-a3fc-37a80bd345a6 | -9.37216 | -50.74904 | 2024-10-04 04:55:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 70a30881-5bbf-3472-a98c-cc18eeb26a6d | -9.36769 | -50.7532 | 2024-10-04 04:55:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 24536fda-0ea2-36ed-9974-33b3d7608a15 | -9.36457 | -50.74802 | 2024-10-04 04:55:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ab14e240-2910-3d17-9c4b-3afe2a699b21 | -9.33076 | -50.795 | 2024-10-04 04:55:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 8aa4fbd8-cd9b-3c6e-a59d-936a8f68ca33 | -9.33009 | -50.79962 | 2024-10-04 04:55:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| fc421cc1-eeeb-3338-94c4-bc0d7d4087b9 | -9.32943 | -50.80426 | 2024-10-04 04:55:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| fc0874eb-8cf0-3708-9f11-fcda7f316317 | -9.32876 | -50.80889 | 2024-10-04 04:55:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| a909bee6-ad23-3482-96f5-265e13d83d1f | -9.32807 | -51.12782 | 2024-10-04 04:55:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5c941c08-61b1-34de-b6f8-c33cb8103312 | -9.32697 | -50.79451 | 2024-10-04 04:55:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 61f92614-3fa8-3c5e-827e-cf2ed3e5ee0e | -9.3263 | -50.79918 | 2024-10-04 04:55:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 3f52d814-00a6-334b-befe-cd482ad2a070 | -9.32563 | -50.80389 | 2024-10-04 04:55:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| c6dcc2f3-9c9b-3f19-b598-d945c4de3c29 | -9.32503 | -51.1228 | 2024-10-04 04:55:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b65d9b47-b194-3c57-86e2-2a73ad8605e5 | -9.32497 | -50.80846 | 2024-10-04 04:55:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 880b650f-ea55-32a9-b049-21410d9609dc | -9.32432 | -50.81301 | 2024-10-04 04:55:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 30e12547-6359-3ebd-b8a7-733e7deb7c2c | -9.32372 | -51.13166 | 2024-10-04 04:55:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |


[Clique aqui para ver as próximas entradas](README145.md)
