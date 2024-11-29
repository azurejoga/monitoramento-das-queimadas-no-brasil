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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 29b557d8-1143-3524-be8a-569b5e4a9bce | -3.5949 | -50.3594 | 2024-11-29 00:52:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 1f8865cb-6bd4-32ee-86a3-5a40998d8b1e | -3.61635 | -49.84846 | 2024-11-29 00:52:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| ac48eb2b-92dd-390a-8d6b-96d1c3e85139 | -3.46958 | -50.53536 | 2024-11-29 00:52:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 29.6 |
| b1179b51-debe-378f-9d3d-02540fca4f1b | -2.64754 | -47.12448 | 2024-11-29 00:52:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| d761b3c2-6b25-37e5-955f-6005adddadbf | -2.86008 | -45.53976 | 2024-11-29 00:52:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 270.4 |
| bc1adb6c-8100-33b6-8258-255bd33fc775 | -3.37437 | -50.83182 | 2024-11-29 00:52:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 4bbf8d84-ac17-367c-bad6-9a6793f583b4 | -4.93383 | -44.52434 | 2024-11-29 00:52:00 | TERRA_M-M | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 5ba627c5-5ef6-383a-b08e-b8a00b6e8e35 | -1.60373 | -52.29936 | 2024-11-29 00:52:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 45d4b0b6-e77b-3518-b61a-5a4b7eacb924 | -3.44765 | -45.86381 | 2024-11-29 00:52:00 | TERRA_M-M | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 12.1 |
| e7013104-8aee-3460-890a-f5e6225dd215 | -3.94129 | -46.69236 | 2024-11-29 00:52:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 11.3 |
| dabb7826-bba0-36c5-ba77-e39e1018f20d | -2.77775 | -48.58194 | 2024-11-29 00:52:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| b61c7671-0768-3169-adc1-5ed6812f98b8 | -3.35984 | -50.40435 | 2024-11-29 00:52:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 08f4ed9c-41c9-3880-b11e-679bade5a369 | -2.58159 | -49.22382 | 2024-11-29 00:52:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| cc0d9911-5166-3e0c-ae4e-7b7a667c371c | -1.62401 | -52.37108 | 2024-11-29 00:52:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 16.9 |
| bc477537-482c-34a9-b6f0-af2741ba99ec | -2.78564 | -48.10696 | 2024-11-29 00:52:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 53f6509a-d537-32c5-9010-117700ffde43 | -2.71974 | -48.63194 | 2024-11-29 00:52:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 95b27e2d-efba-3db1-a6be-b054cff2a59a | -2.66759 | -48.78951 | 2024-11-29 00:52:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 3caa0828-26da-3682-a63c-bfb6ff2e67ff | -2.98564 | -53.27248 | 2024-11-29 00:52:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 52.7 |
| aee00413-f875-3727-9e54-3a0a4d51e499 | -3.96267 | -48.82923 | 2024-11-29 00:52:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| e54b15d0-68bd-3430-bbfa-80035144f562 | -0.02905 | -50.73917 | 2024-11-29 00:52:00 | TERRA_M-M | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| f26e9bcc-d58e-3213-9fef-1d86ebfa061d | -2.68535 | -46.26837 | 2024-11-29 00:52:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 2527f2b5-4c1b-356f-9454-654bf7963647 | 0.04002 | -51.11102 | 2024-11-29 00:52:00 | TERRA_M-M | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 52.9 |
| a455ed79-048b-3dab-a8de-f18e030cd772 | -3.0265 | -54.01518 | 2024-11-29 00:52:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 17.7 |
| 5f9921c1-93a2-392d-95c6-52dce8b8f646 | -3.32854 | -50.22484 | 2024-11-29 00:52:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 2971e84b-72b9-3090-b688-8efcabc40ad4 | -4.10335 | -53.9795 | 2024-11-29 00:52:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| f29664c7-2bcf-33fd-901f-9a773af8c7a2 | -5.43221 | -48.13773 | 2024-11-29 00:52:00 | TERRA_M-M | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 46a8707f-2ea6-34c1-8d26-d0af63a821c1 | -3.8016 | -44.04288 | 2024-11-29 00:52:00 | TERRA_M-M | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 062ce9dd-b122-3998-bc5b-ce85ea32b742 | -1.72154 | -52.49015 | 2024-11-29 00:52:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 23.5 |
| 8de39e5d-1cf2-336c-8aa1-43db5b160c8f | -2.96812 | -53.72435 | 2024-11-29 00:52:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| c9e9cf2f-ade4-34f9-86cb-e5956e6658c7 | -3.04508 | -48.51668 | 2024-11-29 00:52:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| ff943ef6-bbd6-3093-a6f7-7237c05f4804 | -3.05756 | -51.06053 | 2024-11-29 00:52:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 9e63ad35-1a93-3888-94d5-c344359063cb | -2.87244 | -45.54318 | 2024-11-29 00:52:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 41.2 |
| 24c07b8c-8b97-3c27-a05c-87cfd824c212 | -1.44077 | -55.16038 | 2024-11-29 00:52:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 73f42fc4-0fa0-361c-93ab-fc9c0bc60147 | 0.94781 | -50.73222 | 2024-11-29 00:52:00 | TERRA_M-M | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 7ebdc3d3-38b5-36ad-864f-15b32a394682 | -3.53396 | -45.09564 | 2024-11-29 00:52:00 | TERRA_M-M | CAJARI | MARANHÃO | Brasil | 2102507 | 21 | 33 | nan | nan | nan | Amazônia | 7.0 |
| ddc2eec1-4bb2-37c5-ba2a-085cb7961dec | -4.14421 | -44.28026 | 2024-11-29 00:52:00 | TERRA_M-M | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| e7a5532a-5228-398e-bcd9-7c318078fb39 | -1.34764 | -51.99247 | 2024-11-29 00:52:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 2cfe91fd-4f25-3d31-833e-9aa4646bbe92 | -1.98913 | -50.86583 | 2024-11-29 00:52:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 6f733eb1-0953-31ff-9602-7df112c31724 | -4.76191 | -46.37764 | 2024-11-29 00:52:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 1f89ea05-9a7b-3aef-93db-383843e42a6b | -3.81763 | -46.60063 | 2024-11-29 00:52:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 21.8 |
| 31df1521-8540-3e0b-a6d3-fa4916a2b731 | -4.19046 | -50.67492 | 2024-11-29 00:52:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 87edfca0-7562-3df5-9efb-0fd013cbb16d | -3.33238 | -46.69045 | 2024-11-29 00:52:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 20.8 |
| 0e5e6c6d-3f50-3bf4-98ce-0ba2c84c7479 | -3.6163 | -50.19015 | 2024-11-29 00:52:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 22.7 |
| 68733c9f-fc89-391c-9521-8a8dac41665d | -1.00276 | -51.71704 | 2024-11-29 00:52:00 | TERRA_M-M | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 508d9669-a280-375c-9cb6-81d8456b403c | -3.26359 | -49.89319 | 2024-11-29 00:52:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 59.1 |
| b9152e0d-1ace-3285-a57e-f80882a3bdd8 | -3.46822 | -50.52527 | 2024-11-29 00:52:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 2c4dbc0f-981d-313a-956e-e9e596d07f2c | -3.28217 | -50.62104 | 2024-11-29 00:52:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| b48919d4-4250-31eb-9d2e-3ef8c3f4bed6 | -1.22963 | -51.808 | 2024-11-29 00:52:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 13dff4a4-f602-31af-8f7b-363d73cf5283 | -3.81627 | -46.59098 | 2024-11-29 00:52:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 9ae78a93-187c-36cd-9e8a-b0f5416ace26 | -2.80897 | -46.83094 | 2024-11-29 00:52:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f9d55f5c-9c24-3d77-b297-6cd1d5310d0e | -3.71042 | -47.14999 | 2024-11-29 00:52:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 8fafb7bc-73c2-3633-910f-c4c1df0204c5 | -3.83473 | -46.53349 | 2024-11-29 00:52:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| c2cd9f54-8dbe-3f64-a0d6-21593488f645 | -2.73 | -48.90062 | 2024-11-29 00:52:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 81788dcd-a53f-3e07-94fe-61978ff39b5b | -3.24663 | -46.15489 | 2024-11-29 00:52:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 94aca368-117a-35f4-997e-76bc34f30c49 | -3.95155 | -52.20481 | 2024-11-29 00:52:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 78f117cc-0399-3d80-b7ed-4a2c69806751 | -2.60523 | -46.55848 | 2024-11-29 00:52:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 4d4a151a-9aa4-38e6-b683-ae7bdaec49e9 | -2.02835 | -48.55682 | 2024-11-29 00:52:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| dfea85da-fe9f-353b-918a-bc9c87b5201c | -1.97736 | -49.51615 | 2024-11-29 00:52:00 | TERRA_M-M | LIMOEIRO DO AJURU | PARÁ | Brasil | 1504000 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| f70d954b-fce7-3a39-9c9d-0e5610babbfc | -4.4596 | -44.06479 | 2024-11-29 00:52:00 | TERRA_M-M | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 5b686114-9806-3fba-8fd7-8b6159feba6b | -3.11314 | -54.47791 | 2024-11-29 00:52:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 02d21a6d-3bf8-312e-8acd-26ca36473276 | -2.66636 | -48.78068 | 2024-11-29 00:52:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 1f261a06-c497-3e17-80c9-556d8133e222 | -2.60074 | -53.98326 | 2024-11-29 00:52:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| b80242f6-3518-378f-820f-d1fe9b5b76dc | -3.02173 | -54.02225 | 2024-11-29 00:52:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 19.8 |
| f0a9cdef-9d1d-3346-acbf-cb9b1366b12c | -2.44904 | -48.60778 | 2024-11-29 00:52:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| fc995fc2-de5d-3e1d-af6c-61c6309506b5 | -3.20411 | -46.56876 | 2024-11-29 00:52:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 45f95813-4fde-30f6-af99-156f986ed21a | -1.5949 | -52.2939 | 2024-11-29 00:52:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 32.3 |
| 718e0d52-7fc3-3f92-a503-3bad00042587 | -5.03898 | -43.62135 | 2024-11-29 00:52:00 | TERRA_M-M | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 140.2 |
| 6820fa57-9b4e-37e2-87c2-daadcaa03039 | -4.88059 | -44.64649 | 2024-11-29 00:52:00 | TERRA_M-M | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 35459388-2836-3535-b2bf-6ea4020e4d8a | 0.98655 | -50.12474 | 2024-11-29 00:52:00 | TERRA_M-M | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 14.6 |
| bf2ad9db-2437-3ae1-b403-dd23c5f02280 | -2.80648 | -53.04963 | 2024-11-29 00:52:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 38f8e3c8-a0ba-392c-9818-89ae50d92e6d | -3.10313 | -53.8112 | 2024-11-29 00:52:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 44.4 |
| 3f01b6fe-f29c-32c1-9b47-d6190f3a5c05 | -3.06104 | -51.30153 | 2024-11-29 00:52:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 863b3e41-7672-3c69-a3ae-374a086371d7 | -2.98699 | -45.41911 | 2024-11-29 00:52:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 12.8 |
| a6c2652c-08b8-38ab-9da4-a10d86a613a6 | -3.93326 | -46.51327 | 2024-11-29 00:52:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 2f1cb6a8-5554-3f17-8f70-479884617d40 | -3.33507 | -46.70946 | 2024-11-29 00:52:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 5af1bd31-0b18-37e3-88bb-ce04be8f8bb2 | -3.10734 | -50.36721 | 2024-11-29 00:52:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| ffd396bc-de33-34b5-9ac5-a0a8f2bda2b3 | -1.09731 | -53.38618 | 2024-11-29 00:52:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 21.3 |
| d5eb9382-5477-3dbf-a68e-cdbe0afcbdf6 | -3.94261 | -46.70181 | 2024-11-29 00:52:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 8.4 |
| d26414a9-b070-3d79-970c-e1a06e88df08 | -4.07085 | -47.02741 | 2024-11-29 00:52:00 | TERRA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 9b5cb191-8e86-3303-9256-ed130dbc16d7 | -2.86982 | -46.87432 | 2024-11-29 00:52:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 1c67749e-7af9-3f33-9d8b-b8d57c54f7ef | -2.72877 | -48.89176 | 2024-11-29 00:52:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| c9371efa-e534-3a8e-894c-4c11333371a7 | -0.96444 | -51.65592 | 2024-11-29 00:52:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| c9fa43a4-7da0-3cc8-9e15-e1f695c32a29 | -4.40514 | -50.82647 | 2024-11-29 00:52:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 08ab4d27-c1ef-362f-81ff-8dc5e97a6c20 | -1.18396 | -51.76915 | 2024-11-29 00:52:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| def95b77-3a0c-302c-a1f8-1e32f2a424d6 | -4.51141 | -48.06197 | 2024-11-29 00:52:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 19.0 |
| 5227f116-334a-318c-81a0-9df8129b796f | -3.41416 | -50.24665 | 2024-11-29 00:52:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| ab579680-36f9-363a-b71b-30953ea35164 | -1.08558 | -53.39387 | 2024-11-29 00:52:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 32.3 |
| b2ae90b6-fc70-3699-9110-6749710b74a2 | -4.26307 | -47.60392 | 2024-11-29 00:52:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 4529d6d8-66c6-3922-9603-8ea857adea8f | -2.84562 | -46.8257 | 2024-11-29 00:52:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 38.3 |
| 2b952a8c-0b5a-30da-ad81-f9ed41c81092 | -1.32804 | -51.92545 | 2024-11-29 00:52:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 3e08e681-c03e-3e14-89e0-117cf13c6594 | -4.38504 | -49.75414 | 2024-11-29 00:52:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| fa8e53df-f618-38b2-80d6-6fe28f9a0393 | -2.82995 | -46.84726 | 2024-11-29 00:52:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| bd101b31-8fdc-3cea-998a-dcf279380dc2 | -1.15831 | -53.58295 | 2024-11-29 00:52:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 690ec308-3d13-302b-b4f7-1ed11e27dd62 | -3.4641 | -43.53745 | 2024-11-29 00:52:00 | TERRA_M-M | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| c33f5a7f-e03d-3a83-9202-f4d15735b4fc | 0.98567 | -50.2626 | 2024-11-29 00:52:00 | TERRA_M-M | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 2ddd23c9-cf05-3913-8835-c391aac30eba | -2.674 | -46.15012 | 2024-11-29 00:52:00 | TERRA_M-M | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 11.6 |
| d435e9d7-ac4d-3e29-a857-4855aef9b213 | -1.09668 | -53.39239 | 2024-11-29 00:52:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 32.6 |
| acd17c1b-3ad3-3cec-888b-6d54c987a482 | -2.34556 | -46.15888 | 2024-11-29 00:52:00 | TERRA_M-M | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 7.5 |
| cbc07f9b-8084-3a36-ae01-2c0a4a291bae | -2.67083 | -49.86976 | 2024-11-29 00:52:00 | TERRA_M-M | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 8c0601ce-ccd3-35c0-8a10-5ddf47874a91 | -2.87086 | -45.53222 | 2024-11-29 00:52:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 21.8 |


[Clique aqui para ver as próximas entradas](README5.md)
