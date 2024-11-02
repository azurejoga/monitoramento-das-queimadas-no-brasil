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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4c625052-2d72-3c79-9e94-17d49732a4f2 | -5.06783 | -44.23187 | 2024-11-02 04:12:00 | NOAA-20 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3e37e304-a391-349b-8043-4e0eea1a7448 | -5.06297 | -44.17609 | 2024-11-02 04:12:00 | NOAA-20 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5349c9e7-0677-3536-8606-4928c9443958 | -6.12929 | -43.97158 | 2024-11-02 04:12:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 609c25e2-7c20-309b-9641-3841456533c5 | -6.12873 | -43.97509 | 2024-11-02 04:12:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7714fea0-426d-3c61-afe1-3b171fa09ec6 | -6.12485 | -43.97807 | 2024-11-02 04:12:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 934190b6-f7df-354f-ba01-e81af99745a9 | -6.12152 | -43.97755 | 2024-11-02 04:12:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| bc4e85e9-b4a4-3b2e-a751-504f0b0afeb6 | -6.1193 | -43.97002 | 2024-11-02 04:12:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7b7fc600-3f0b-322e-969e-210a0b360b1f | -6.1182 | -43.95548 | 2024-11-02 04:12:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e13a3aac-bd65-30ec-8c2e-a659ffd5f508 | -6.11765 | -43.95898 | 2024-11-02 04:12:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8f8b5a92-17ae-39f3-8cf2-0686b49aa367 | -6.11321 | -43.96544 | 2024-11-02 04:12:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 641d9331-49f0-39ab-badc-2a64fc19e66a | -5.62932 | -43.80252 | 2024-11-02 04:12:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 720aa601-14d0-3e98-bd34-176771ee6bb1 | -5.6271 | -43.79501 | 2024-11-02 04:12:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5f8b3b2e-6980-3a45-b2f2-b97c665fc981 | -6.12263 | -43.97054 | 2024-11-02 04:12:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 91e681ab-3b0c-3627-b5e4-7c7e67ba37db | -6.12208 | -43.97404 | 2024-11-02 04:12:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 20f1abec-83f5-3705-be8e-20dd3505cdee | -6.11488 | -43.95494 | 2024-11-02 04:12:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4611bdc1-e764-32f7-919e-30a865aafbc4 | -6.10711 | -43.96087 | 2024-11-02 04:12:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 00a696ff-2f80-32bb-8655-0bc0e9644b53 | -5.72377 | -43.5282 | 2024-11-02 04:12:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1e812d5c-5c32-3f60-b913-1c5b765c05a8 | -5.71669 | -43.78741 | 2024-11-02 04:12:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 418044c6-f6f8-30ac-9b3a-152c6f1fe40c | -5.7028 | -43.53202 | 2024-11-02 04:12:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 939b17b1-d3fb-39cb-a8fd-e5cb6ddf74e3 | -6.05109 | -44.20498 | 2024-11-02 04:12:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d884405c-92ee-312f-be65-db1b2857a3ef | -5.83322 | -44.01795 | 2024-11-02 04:12:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d08aa317-50fc-3636-bd3a-2687e9f68a60 | -5.82932 | -44.02095 | 2024-11-02 04:12:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a06b2278-d1ba-3db6-ab3f-ba95f695df22 | -5.76319 | -44.6004 | 2024-11-02 04:12:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c4d18299-edb1-3a5f-b0c9-af93041d5394 | -5.42233 | -44.62533 | 2024-11-02 04:12:00 | NOAA-20 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 038edbdf-6521-3605-a23f-5124fda46b44 | -5.33953 | -44.19428 | 2024-11-02 04:12:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6501dcf7-a658-3deb-8dea-855280505403 | -5.32785 | -44.84136 | 2024-11-02 04:12:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| eb21fe52-73fa-3da7-a460-0d0c93932948 | -5.28434 | -44.78493 | 2024-11-02 04:12:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9f9fc65e-b875-38e0-adc7-7cad2d81b7a9 | -5.28093 | -44.78438 | 2024-11-02 04:12:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 99be6fab-2f3f-3b2d-8733-a9d5ba7c4625 | -5.27798 | -44.75735 | 2024-11-02 04:12:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7e27c5be-6897-317c-894b-ce6280a52ae9 | -5.20577 | -44.309 | 2024-11-02 04:12:00 | NOAA-20 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fa82dc9b-8cbe-383e-83a3-19525ea5a900 | -5.2024 | -44.30846 | 2024-11-02 04:12:00 | NOAA-20 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 312814e7-1992-3861-836d-b18240be22c2 | -7.89649 | -43.92724 | 2024-11-02 04:12:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1f171318-8740-37df-972e-c62182a8f6bb | -6.93874 | -44.28777 | 2024-11-02 04:12:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cf07f6bc-8ba8-3b8d-97db-64bc72354186 | -6.9354 | -44.28723 | 2024-11-02 04:12:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ad3dff0c-a5d5-359e-80f5-305e3c7b2624 | -7.89594 | -43.93071 | 2024-11-02 04:12:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6085db83-c895-3a35-838c-0b8975f99fad | -7.78879 | -45.24331 | 2024-11-02 04:12:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 55b600f6-c77b-39bb-b3d3-ea3ef35e3be4 | -6.96967 | -45.18989 | 2024-11-02 04:12:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d5bd2369-428c-365e-84f1-e6c48350e3df | -6.96907 | -45.19358 | 2024-11-02 04:12:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ca3bdf51-47fb-33f6-aad7-fce91a00bf0c | -6.96566 | -45.193 | 2024-11-02 04:12:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 654b831f-a331-3212-b4c8-181915f09b9a | -6.96446 | -45.2004 | 2024-11-02 04:12:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d371aa62-f799-30db-bafa-3e28516deda8 | -6.93817 | -44.29131 | 2024-11-02 04:12:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 36e1879f-e0d5-3f61-9506-42c2eeab7e68 | -6.93484 | -44.29077 | 2024-11-02 04:12:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d2aff014-ff7f-3f9f-a30a-0b896fd80c35 | -3.67368 | -44.80949 | 2024-11-02 04:12:00 | NOAA-20 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5901dd89-832d-3368-9e39-75be29c1340f | -3.59793 | -44.91611 | 2024-11-02 04:12:00 | NOAA-20 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c9e97108-17f4-3743-a5b7-8a8b0aaecef9 | -3.37513 | -45.70532 | 2024-11-02 04:12:00 | NOAA-20 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 60411905-2d52-33f7-b983-b331a8bd7d89 | -3.40641 | -44.98547 | 2024-11-02 04:12:00 | NOAA-20 | CAJARI | MARANHÃO | Brasil | 2102507 | 21 | 33 | nan | nan | nan | Amazônia | 17.4 |
| f3186f7d-e974-3643-ad62-bd60e18a0984 | -3.40578 | -44.98937 | 2024-11-02 04:12:00 | NOAA-20 | CAJARI | MARANHÃO | Brasil | 2102507 | 21 | 33 | nan | nan | nan | Amazônia | 17.4 |
| c3828470-20f8-3c1a-bf78-baf514d55c13 | -3.40291 | -44.98492 | 2024-11-02 04:12:00 | NOAA-20 | CAJARI | MARANHÃO | Brasil | 2102507 | 21 | 33 | nan | nan | nan | Amazônia | 17.4 |
| 77757cb7-f802-388d-aceb-86d956d90f63 | -3.37579 | -45.70112 | 2024-11-02 04:12:00 | NOAA-20 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6b10aded-e09a-3122-8da8-7fe1dd272130 | -3.37217 | -45.70053 | 2024-11-02 04:12:00 | NOAA-20 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d56b4e10-940c-3b83-a2aa-245327bbd1dd | -3.32363 | -45.41433 | 2024-11-02 04:12:00 | NOAA-20 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f27f29fd-17bd-3de0-a0ed-da6b2297c6d9 | -3.23601 | -45.59459 | 2024-11-02 04:12:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e0020ad8-f1e3-3f3e-88aa-968d9fd67e46 | -3.23307 | -45.58986 | 2024-11-02 04:12:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| a3d0720c-9a6c-3eb7-bc76-676a728f668d | -3.2324 | -45.59402 | 2024-11-02 04:12:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bfd40a86-987d-36b9-83ee-abedf5d6de5e | -3.22946 | -45.58929 | 2024-11-02 04:12:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| e3e56754-77fa-3a1e-bc1f-17c812dfba34 | -3.21909 | -45.2952 | 2024-11-02 04:12:00 | NOAA-20 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 9a6ce3df-9116-3305-8649-21306bc7e390 | -3.21554 | -45.29462 | 2024-11-02 04:12:00 | NOAA-20 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 4b06db77-d12a-30c1-91e7-ea47210df454 | -3.2149 | -45.29865 | 2024-11-02 04:12:00 | NOAA-20 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 10bceae5-99ea-309f-81ee-40d21234b788 | -3.21198 | -45.29406 | 2024-11-02 04:12:00 | NOAA-20 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5cd1c78f-934c-3ee6-b167-029007ed8371 | -3.21134 | -45.29808 | 2024-11-02 04:12:00 | NOAA-20 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 8.7 |
| bb88a94d-699a-3068-88f3-74125c3b115a | -4.01725 | -45.67223 | 2024-11-02 04:12:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 65e97bd8-a322-38ab-a3c2-7778d1c26eb1 | -3.71721 | -46.00264 | 2024-11-02 04:12:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 88a7452b-7d99-3bd3-9918-9028b32e3bd7 | -3.71355 | -46.00203 | 2024-11-02 04:12:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3331bd38-5ac8-3748-87e8-bad6c45d7cb8 | -3.63991 | -45.94858 | 2024-11-02 04:12:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 514a56eb-7c34-38ec-8ff2-f4461257d30e | -5.04172 | -44.8767 | 2024-11-02 04:12:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6c9eea5b-4f27-3fa7-9881-0860a48732a0 | -5.02116 | -45.53268 | 2024-11-02 04:12:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dc59352b-aef7-3819-ba34-83622fb258d6 | -5.02053 | -45.53661 | 2024-11-02 04:12:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b3c8021f-3e50-3e72-a75a-ef0175a7787f | -5.02011 | -45.16032 | 2024-11-02 04:12:00 | NOAA-20 | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 38b5fb85-61f1-3764-9cef-74871d30e82e | -5.01664 | -45.15976 | 2024-11-02 04:12:00 | NOAA-20 | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b87b9078-c4b3-3f7b-b141-ba38b66eb3c6 | -4.96256 | -45.87573 | 2024-11-02 04:12:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 3656490b-be51-3f31-b163-bbd347c812ed | -4.95898 | -45.8751 | 2024-11-02 04:12:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| be0009f0-91b6-35c0-9960-af40eafa5467 | -4.95658 | -45.55117 | 2024-11-02 04:12:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| eeffdb5b-6000-39d0-a6b7-56f6a66a0539 | -4.95306 | -45.55054 | 2024-11-02 04:12:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0be91641-cb78-3057-8343-25f0947411e4 | -4.92214 | -45.02753 | 2024-11-02 04:12:00 | NOAA-20 | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5d39d739-d26c-39a0-9264-21f6b508c3cf | -4.91929 | -45.91536 | 2024-11-02 04:12:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6435f787-9e41-375c-ae8d-e8dc844418c5 | -4.89555 | -45.70663 | 2024-11-02 04:12:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 833d4e1b-63a6-3b3e-8b4d-95021adc697f | -4.89491 | -45.71064 | 2024-11-02 04:12:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e5faf512-e92d-32b0-9683-a61282827e6b | -4.8938 | -45.95832 | 2024-11-02 04:12:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e942b321-a5d1-34dc-b82b-a28b2a085480 | -4.89313 | -45.96246 | 2024-11-02 04:12:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5f8c5b92-04a9-3d99-b2ab-f6a57f3a6fed | -4.892 | -45.70599 | 2024-11-02 04:12:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 886e7783-b5e6-3078-9799-6423ec642a54 | -4.88399 | -45.90543 | 2024-11-02 04:12:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 93da91ff-d0d9-3f75-a4f5-ee8dafce22f5 | -4.88218 | -45.90612 | 2024-11-02 04:12:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.3 |
| d75d1488-2605-3c9a-b6a5-b5c7c71b8b34 | -4.86737 | -45.76834 | 2024-11-02 04:12:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 41347f77-e0b8-3880-a048-5602b986ef69 | -4.86116 | -45.78419 | 2024-11-02 04:12:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 86451f13-b5ea-3c7e-8d8b-5dc1b570349c | -4.85758 | -45.78361 | 2024-11-02 04:12:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e0980f27-cca4-31b0-97ad-4dbf8e466c0a | -4.854 | -45.78305 | 2024-11-02 04:12:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 39ff95f2-0487-331a-afa2-9747136e509c | -4.85335 | -45.78711 | 2024-11-02 04:12:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1bf189db-49a8-360b-a73a-04b59503683a | -4.81721 | -44.78851 | 2024-11-02 04:12:00 | NOAA-20 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c483b26d-0310-38a1-af31-75251993832d | -4.81332 | -45.63289 | 2024-11-02 04:12:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 30f324e3-a623-33ff-9843-89d999f32f38 | -4.81318 | -44.79175 | 2024-11-02 04:12:00 | NOAA-20 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a6c904ab-f163-3194-9cc6-24308ba9800a | -4.81258 | -44.79548 | 2024-11-02 04:12:00 | NOAA-20 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4a62c526-0eee-3246-944a-edc36facba90 | -4.80751 | -45.77549 | 2024-11-02 04:12:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 24351fce-a382-39b8-a5e6-20a652892a31 | -4.7961 | -45.77794 | 2024-11-02 04:12:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0faed81d-ee56-3f7f-96f6-2fba8a2fc454 | -4.79437 | -45.77546 | 2024-11-02 04:12:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 81708828-bef3-30aa-b2f5-4cd90bce48be | -4.79318 | -45.7733 | 2024-11-02 04:12:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 82259ae8-7e5a-34b5-8524-b4acd96f3cda | -4.79251 | -45.77739 | 2024-11-02 04:12:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0d564918-637e-3485-8eb6-0ce8089e08ff | -4.79137 | -46.03323 | 2024-11-02 04:12:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 52738ca8-deaf-3310-8755-2753372d5ce2 | -4.75535 | -45.78984 | 2024-11-02 04:12:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 74b1103b-0896-39b6-bf89-eefc604e0e4a | -4.75417 | -45.66056 | 2024-11-02 04:12:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 5.8 |
| fd27eaeb-a4f1-34d3-9437-e2cafb695da2 | -4.7409 | -46.15922 | 2024-11-02 04:12:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README39.md)
