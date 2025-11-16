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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0173e9d8-e60d-3c9a-b288-c39613bca91a | -4.65593 | -46.74241 | 2025-11-16 04:06:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 07f8ca51-e449-3df8-875d-d2735e4ea95b | -3.34299 | -40.20973 | 2025-11-16 04:06:00 | NOAA-20 | SANTANA DO ACARAÚ | CEARÁ | Brasil | 2312007 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 77efb9a9-0e23-3233-bf4e-58ea89831462 | -4.20786 | -48.56675 | 2025-11-16 04:06:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9db81698-4a06-341c-a4ea-32fd251432b7 | -4.69716 | -46.31836 | 2025-11-16 04:06:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 60f9d8c2-5e0b-3a4c-a0a3-73a82e37fc06 | -2.78434 | -43.34924 | 2025-11-16 04:06:00 | NOAA-20 | PRIMEIRA CRUZ | MARANHÃO | Brasil | 2109403 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bf433d84-c02b-361e-a7aa-9240774fe0c7 | -2.46967 | -48.86605 | 2025-11-16 04:06:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7a9b1fca-2383-3776-bb86-9bceb553876b | -3.58954 | -41.6612 | 2025-11-16 04:06:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 5ac04882-92c2-3bdb-a647-eff4b87737c1 | -5.06983 | -44.34174 | 2025-11-16 04:06:00 | NOAA-20 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9a4cda9f-83d2-33fc-af38-da00be6c1312 | -5.71645 | -41.40706 | 2025-11-16 04:06:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 4acfdafd-370a-36d8-8837-a56b689712e7 | -3.72044 | -49.53865 | 2025-11-16 04:06:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c9b61f15-1ae7-3bca-a313-463a60584c24 | -3.08192 | -52.92896 | 2025-11-16 04:06:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 53fbf483-827e-37ec-8293-193fd7ddbf5b | -3.58623 | -41.66091 | 2025-11-16 04:06:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| f789c955-6684-37b2-88c1-63f6c36c8b0a | -4.43423 | -43.41071 | 2025-11-16 04:06:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 2fc3c434-224e-3a1c-b68c-aecc7b62ba43 | -3.33951 | -45.61323 | 2025-11-16 04:06:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 985ef35d-0410-34c7-b8c5-a7f7f8fc1578 | -2.80097 | -52.97153 | 2025-11-16 04:06:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7a896aa1-79ab-3d91-87b6-669914cc1b1a | -3.45646 | -46.12524 | 2025-11-16 04:06:00 | NOAA-20 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 81bf45db-5d70-312e-b535-5c1207746f30 | -5.47681 | -42.6821 | 2025-11-16 04:06:00 | NOAA-20 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| cf2525d8-5caa-300b-983f-bbf4906eb8e1 | -4.07111 | -46.34472 | 2025-11-16 04:06:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9f37ca03-89e9-32d2-a629-d6562dd4ad27 | -4.00246 | -44.26855 | 2025-11-16 04:06:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ad9e02ec-160b-3a57-a95c-76577b27b83b | -4.59077 | -45.92443 | 2025-11-16 04:06:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9867da1c-a6ca-396c-8995-0bf201c74c7d | -3.92746 | -47.05218 | 2025-11-16 04:06:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| baf447d2-8cba-3325-b571-417f59715f9e | -3.86637 | -40.64207 | 2025-11-16 04:06:00 | NOAA-20 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| bfe14162-accc-313d-aac7-6259e8e36947 | -4.6423 | -45.65869 | 2025-11-16 04:06:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 001cfa9a-da56-361a-93ee-cce07c77edc1 | -4.01366 | -40.1582 | 2025-11-16 04:06:00 | NOAA-20 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 0b5d9bcf-89af-34c8-af30-e916163c5fa8 | -3.30698 | -42.65365 | 2025-11-16 04:06:00 | NOAA-20 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 66f76d39-f704-3970-a1a4-5f098b582412 | -5.33195 | -43.04482 | 2025-11-16 04:06:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8562101e-79f7-37ad-bdd4-82de80020e5b | -2.93305 | -49.35452 | 2025-11-16 04:06:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 45d2389a-9956-3a9e-ad5d-512677628592 | -4.81492 | -41.60649 | 2025-11-16 04:06:00 | NOAA-20 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| dde1728d-5447-3eec-ad49-ac2763f0d845 | -3.33836 | -45.54535 | 2025-11-16 04:06:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ee61a66b-994f-3bc9-be04-5ed131295bb7 | -4.44849 | -46.41335 | 2025-11-16 04:06:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b079acc5-0121-3115-a442-d9d1ff142ca4 | -4.67874 | -46.73429 | 2025-11-16 04:06:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6203387d-34ad-3811-b62e-df553606af5d | -4.39489 | -49.66971 | 2025-11-16 04:06:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c50cf774-38ea-3035-950c-077d78240f61 | -5.32855 | -43.04426 | 2025-11-16 04:06:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 80664e87-622b-38f1-9e15-b3532d3e56fe | -2.51935 | -47.81844 | 2025-11-16 04:06:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 19.7 |
| 55fe13b4-716c-3799-a1f6-83ebc9d11b73 | -5.05745 | -42.67112 | 2025-11-16 04:06:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3c397b8c-8ea7-307f-ac5e-7e84d34a504b | -2.78509 | -45.21335 | 2025-11-16 04:06:00 | NOAA-20 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6dd04296-6066-3748-8abd-1a1fcfb9c9f2 | -4.42977 | -43.39431 | 2025-11-16 04:06:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0c5f9a3e-e42c-3b2c-9601-99c8bf192939 | -3.33825 | -46.28931 | 2025-11-16 04:06:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 753f45b5-294c-3aed-bb84-f3d90344a691 | -4.41973 | -43.41235 | 2025-11-16 04:06:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fe830d37-15d8-3887-91f0-9e4c9f2e8ebb | -3.78529 | -47.47243 | 2025-11-16 04:06:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0f47c2b7-2c00-3442-befb-b4498bfa1680 | -5.52027 | -40.99092 | 2025-11-16 04:06:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 617cda34-969d-3f67-b671-79f437dc160f | -4.81295 | -45.50726 | 2025-11-16 04:06:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a375d452-7dc4-3370-8f58-ee1825bc126b | -3.02123 | -51.63249 | 2025-11-16 04:06:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 489bf8cd-be98-3ce9-8cc9-e0542e62c891 | -3.99884 | -44.26795 | 2025-11-16 04:06:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f48d20f2-6f9f-36ef-9885-e32d6e475d60 | -3.72366 | -45.99577 | 2025-11-16 04:06:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 43a26683-322d-3138-b8ae-049df59d4d3b | -3.84965 | -40.76986 | 2025-11-16 04:06:00 | NOAA-20 | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 20804f30-e693-371a-a429-8217a657339f | -4.24925 | -50.05355 | 2025-11-16 04:06:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e5f1f0ff-97d3-3760-9b04-baaccee99948 | -4.57279 | -45.81203 | 2025-11-16 04:06:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5ff8776a-f457-3abd-b03a-eb39e93f9ede | -2.90886 | -49.79523 | 2025-11-16 04:06:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8fc09d30-e7c5-3d88-8009-7544cf0b7b10 | -3.83757 | -40.78205 | 2025-11-16 04:06:00 | NOAA-20 | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 40fd6a69-7836-3720-9f7e-597e0bdd3310 | -4.93782 | -44.53237 | 2025-11-16 04:06:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4806548f-4374-3bff-af06-1b04ef9e5112 | -3.07638 | -52.92252 | 2025-11-16 04:06:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bbef9e86-c2c3-3b68-a053-d8f8de439f8a | -2.524 | -47.81923 | 2025-11-16 04:06:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 31.0 |
| e0cbab33-9c1b-325c-b7e2-026d9b97dd04 | -4.41403 | -43.40356 | 2025-11-16 04:06:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 475943ce-2d6f-337b-99bc-f1436b5cee67 | -3.33868 | -45.61832 | 2025-11-16 04:06:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 61bb7184-afe5-3a2f-8aca-7d1799585703 | -5.3859 | -41.15306 | 2025-11-16 04:06:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| ccfef008-9eeb-3a22-9c75-af2c558e38d2 | -5.71754 | -41.40017 | 2025-11-16 04:06:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 1819b979-b447-379e-a1e5-37a298eb5bf4 | -2.68754 | -49.07353 | 2025-11-16 04:06:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| bde9c055-1d75-388a-84cd-0cc48823e67c | -4.24395 | -50.05273 | 2025-11-16 04:06:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2acc9bb4-e76a-3028-83e4-0b2c46a15dee | -4.81547 | -41.60304 | 2025-11-16 04:06:00 | NOAA-20 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 6ba549c4-a457-3b3b-953a-02c1d5ed389c | -3.57616 | -50.42285 | 2025-11-16 04:06:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 30ae4f90-6e2f-3b11-91be-4cff4992dd34 | -4.60944 | -43.30546 | 2025-11-16 04:06:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 78212b2a-540c-3a49-9a4b-4c67aacb97a7 | -3.82299 | -46.02685 | 2025-11-16 04:06:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b9f58a9a-3085-3fd5-ac77-3acb922a0049 | -4.22641 | -44.64332 | 2025-11-16 04:06:00 | NOAA-20 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2481cc48-88ae-3df7-acef-c1b2c594557f | -3.57806 | -44.0899 | 2025-11-16 04:06:00 | NOAA-20 | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d12bede3-e84b-3451-bd52-1ce4341d6252 | -2.75246 | -49.53265 | 2025-11-16 04:06:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ef741926-ca9f-36bf-b615-2017f5f2688b | -2.25206 | -46.06777 | 2025-11-16 04:06:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 00d0f682-b51d-3f67-8c59-24263d3556d9 | -3.42176 | -42.59272 | 2025-11-16 04:06:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dd6bd469-11cc-3852-af58-5dfd8a23f74d | -4.18713 | -51.02563 | 2025-11-16 04:06:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2ef3f6ce-001f-3395-813a-705453d291fa | -3.30148 | -45.797 | 2025-11-16 04:06:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3e9dbea9-32ff-387f-9e36-ce34d5585b7c | -2.73166 | -49.56321 | 2025-11-16 04:06:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 01a5c147-7832-35b6-81ee-102161ce89ad | -4.81374 | -45.50255 | 2025-11-16 04:06:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8d348a8b-9104-3584-87ac-1e43e4a86d80 | -4.88992 | -45.02402 | 2025-11-16 04:06:00 | NOAA-20 | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 82247f06-6c70-3b85-acde-d0287b1f6b20 | -2.68705 | -49.07649 | 2025-11-16 04:06:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0488a91b-7382-3cb9-a22f-b504dc4ec67b | -2.80221 | -52.96571 | 2025-11-16 04:06:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f9a92d9f-570b-3d40-a9ce-923362e04d75 | -4.04715 | -40.87528 | 2025-11-16 04:06:00 | NOAA-20 | SÃO BENEDITO | CEARÁ | Brasil | 2312304 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 3e397313-612c-3250-b69d-7ee0cf76f1bc | -4.41911 | -43.41616 | 2025-11-16 04:06:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 851f3579-d597-3f37-a18d-7f9ad2203168 | -5.53217 | -41.77745 | 2025-11-16 04:06:00 | NOAA-20 | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 3a487b4f-a5bc-3e32-8c82-ce76fdc9d120 | -3.94664 | -47.20512 | 2025-11-16 04:06:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0d71eb5f-f9e5-33a3-957f-46b223162866 | -4.64265 | -47.94932 | 2025-11-16 04:06:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8adbd7fb-5a1f-37d5-a4ab-cda9361a4922 | -4.07523 | -46.34531 | 2025-11-16 04:06:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d01ba263-55e5-3861-8978-d8603dc668b6 | -4.40585 | -43.41008 | 2025-11-16 04:06:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1d516d06-1026-32d7-9969-135167c7bc86 | -4.31657 | -46.54505 | 2025-11-16 04:06:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a104269e-53d2-34ef-bde1-b2232e8183c2 | -5.72139 | -41.39725 | 2025-11-16 04:06:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 1470734a-65a5-3627-9021-a24a61e7fa34 | -2.52016 | -47.81354 | 2025-11-16 04:06:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 16.7 |
| de5a9066-03c9-3858-8914-c88fdd457dea | -4.54295 | -43.21365 | 2025-11-16 04:06:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 71c955d5-6c1c-350a-b05c-c7ff16d619c6 | -4.28089 | -46.43913 | 2025-11-16 04:06:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4c6d0e8f-5d39-3856-9c56-f3615bf92919 | -4.39791 | -45.82639 | 2025-11-16 04:06:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 92dc7412-5a1c-3686-85d8-39e410bb3355 | -4.05557 | -50.73477 | 2025-11-16 04:06:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| df37357b-8940-3610-bd27-c7d4ef236daa | -4.42444 | -43.40525 | 2025-11-16 04:06:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 22.1 |
| a386bd0c-d691-35dc-bf38-fb41c7b9d5db | -4.4232 | -43.41289 | 2025-11-16 04:06:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 083057a7-7eac-350c-9205-c097d304d88e | -2.75326 | -49.53083 | 2025-11-16 04:06:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dd313120-c98e-3afa-a2c0-da4b56a610a9 | -4.41341 | -43.40739 | 2025-11-16 04:06:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 73601b3e-10bc-3795-86e6-864cc7e1f220 | -5.53855 | -42.69536 | 2025-11-16 04:06:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c8d5bf64-7118-3067-a4da-44993aa963c7 | -3.45706 | -46.12161 | 2025-11-16 04:06:00 | NOAA-20 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 37dfedf9-ad4d-309e-ac8d-51d4a28b6e9c | -3.89113 | -47.18451 | 2025-11-16 04:06:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5f8ca7f5-8a2f-3b5b-ba15-6c87ace0b176 | -4.43076 | -43.41015 | 2025-11-16 04:06:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 125354a8-a904-378c-bf7b-2d16e2ed59e4 | -4.74105 | -46.38136 | 2025-11-16 04:06:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| ffd3a5cf-1af9-3f45-8432-280f2c3b7efe | -3.85019 | -40.76643 | 2025-11-16 04:06:00 | NOAA-20 | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 90963724-4557-3ac5-beb5-d3c936c7d0a8 | -4.14464 | -46.35254 | 2025-11-16 04:06:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README31.md)
