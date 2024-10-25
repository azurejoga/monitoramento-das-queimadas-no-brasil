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

## Dados Diários - Página 160

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d883affa-a54c-3a78-8a05-77d6ff3688d3 | -4.11501 | -39.79459 | 2024-10-25 16:52:00 | NOAA-21 | IRAUÇUBA | CEARÁ | Brasil | 2306108 | 23 | 33 | nan | nan | nan | Caatinga | 65.9 |
| 112ce2fe-f551-37da-ae66-4a407f353c4c | -3.90519 | -39.52184 | 2024-10-25 16:52:00 | NOAA-21 | TEJUÇUOCA | CEARÁ | Brasil | 2313351 | 23 | 33 | nan | nan | nan | Caatinga | 64.9 |
| 6cfc73c1-b466-32a2-a158-b812c1c2f8bd | -3.90401 | -39.52323 | 2024-10-25 16:52:00 | NOAA-21 | TEJUÇUOCA | CEARÁ | Brasil | 2313351 | 23 | 33 | nan | nan | nan | Caatinga | 66.2 |
| d47c85f9-27a5-36fa-8ff5-e054624b894a | -3.90317 | -39.51842 | 2024-10-25 16:52:00 | NOAA-21 | TEJUÇUOCA | CEARÁ | Brasil | 2313351 | 23 | 33 | nan | nan | nan | Caatinga | 49.6 |
| 57aa2042-9806-396a-9dae-3f55d61c1b0b | -3.83381 | -39.47865 | 2024-10-25 16:52:00 | NOAA-21 | TEJUÇUOCA | CEARÁ | Brasil | 2313351 | 23 | 33 | nan | nan | nan | Caatinga | 38.9 |
| 42d7ca83-7ea0-3098-81bc-6094c8e71344 | -4.96432 | -40.04419 | 2024-10-25 16:52:00 | NOAA-21 | MONSENHOR TABOSA | CEARÁ | Brasil | 2308609 | 23 | 33 | nan | nan | nan | Caatinga | 9.4 |
| e7969b10-1511-378f-9bff-6bd540736e92 | -4.96271 | -39.97797 | 2024-10-25 16:52:00 | NOAA-21 | MONSENHOR TABOSA | CEARÁ | Brasil | 2308609 | 23 | 33 | nan | nan | nan | Caatinga | 10.2 |
| 4eedd847-0062-31bc-b87d-6c7dc0f51b46 | -4.96234 | -40.04501 | 2024-10-25 16:52:00 | NOAA-21 | MONSENHOR TABOSA | CEARÁ | Brasil | 2308609 | 23 | 33 | nan | nan | nan | Caatinga | 10.7 |
| 447c7149-9664-329b-bcbc-992f9721e14e | -4.87366 | -40.04845 | 2024-10-25 16:52:00 | NOAA-21 | MONSENHOR TABOSA | CEARÁ | Brasil | 2308609 | 23 | 33 | nan | nan | nan | Caatinga | 32.0 |
| 2f3b4882-b13f-3682-968f-3558ffd1c0c6 | -4.86004 | -40.00569 | 2024-10-25 16:52:00 | NOAA-21 | MONSENHOR TABOSA | CEARÁ | Brasil | 2308609 | 23 | 33 | nan | nan | nan | Caatinga | 26.4 |
| d89a566e-cd45-38ef-a208-dc89bc8b108a | -4.85926 | -40.00121 | 2024-10-25 16:52:00 | NOAA-21 | MONSENHOR TABOSA | CEARÁ | Brasil | 2308609 | 23 | 33 | nan | nan | nan | Caatinga | 27.2 |
| cca22451-e419-3237-a827-8946b0dc9e87 | -4.84022 | -39.98191 | 2024-10-25 16:52:00 | NOAA-21 | MONSENHOR TABOSA | CEARÁ | Brasil | 2308609 | 23 | 33 | nan | nan | nan | Caatinga | 10.0 |
| 42997246-5737-3516-90aa-1020ca225b17 | -4.83802 | -39.98497 | 2024-10-25 16:52:00 | NOAA-21 | MONSENHOR TABOSA | CEARÁ | Brasil | 2308609 | 23 | 33 | nan | nan | nan | Caatinga | 15.5 |
| 6bd62ab9-ac12-3ead-975b-b366cf595bf6 | -4.83665 | -40.0687 | 2024-10-25 16:52:00 | NOAA-21 | MONSENHOR TABOSA | CEARÁ | Brasil | 2308609 | 23 | 33 | nan | nan | nan | Caatinga | 23.5 |
| b510aa8d-d86a-3bb5-b21d-d9bb2e56e6c1 | -4.83504 | -40.0714 | 2024-10-25 16:52:00 | NOAA-21 | MONSENHOR TABOSA | CEARÁ | Brasil | 2308609 | 23 | 33 | nan | nan | nan | Caatinga | 15.3 |
| 6b068645-cdf5-3431-a3dd-aed789adc94f | -4.8343 | -40.06723 | 2024-10-25 16:52:00 | NOAA-21 | MONSENHOR TABOSA | CEARÁ | Brasil | 2308609 | 23 | 33 | nan | nan | nan | Caatinga | 15.3 |
| ed29d53c-a646-3048-8b0b-3233caa9df94 | -4.83425 | -39.98284 | 2024-10-25 16:52:00 | NOAA-21 | MONSENHOR TABOSA | CEARÁ | Brasil | 2308609 | 23 | 33 | nan | nan | nan | Caatinga | 10.0 |
| f6e8b357-d6fe-38a1-881e-c48cf5bc7185 | -4.8069 | -40.03744 | 2024-10-25 16:52:00 | NOAA-21 | MONSENHOR TABOSA | CEARÁ | Brasil | 2308609 | 23 | 33 | nan | nan | nan | Caatinga | 45.0 |
| 2bc0dbbe-fe16-3508-928d-d412a4e2ddab | -4.80606 | -39.99699 | 2024-10-25 16:52:00 | NOAA-21 | MONSENHOR TABOSA | CEARÁ | Brasil | 2308609 | 23 | 33 | nan | nan | nan | Caatinga | 9.6 |
| 935277a8-b61f-3f96-abec-8ba1b380f99a | -4.79788 | -39.98506 | 2024-10-25 16:52:00 | NOAA-21 | MONSENHOR TABOSA | CEARÁ | Brasil | 2308609 | 23 | 33 | nan | nan | nan | Caatinga | 18.6 |
| 5c58e658-7924-382a-b7cd-ec1c1e9fa969 | -4.77823 | -40.08313 | 2024-10-25 16:52:00 | NOAA-21 | MONSENHOR TABOSA | CEARÁ | Brasil | 2308609 | 23 | 33 | nan | nan | nan | Caatinga | 23.4 |
| 30cbf244-7cb4-3365-aa9d-aabd3fe1d0fb | -4.77234 | -40.08427 | 2024-10-25 16:52:00 | NOAA-21 | MONSENHOR TABOSA | CEARÁ | Brasil | 2308609 | 23 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 49580018-7227-3a65-ad98-068f16dcfb93 | -4.76402 | -40.03677 | 2024-10-25 16:52:00 | NOAA-21 | MONSENHOR TABOSA | CEARÁ | Brasil | 2308609 | 23 | 33 | nan | nan | nan | Caatinga | 19.7 |
| 8d0b27b3-6905-3448-8141-ef766ae31a71 | -4.76186 | -40.05926 | 2024-10-25 16:52:00 | NOAA-21 | MONSENHOR TABOSA | CEARÁ | Brasil | 2308609 | 23 | 33 | nan | nan | nan | Caatinga | 20.7 |
| f0f6de55-0e05-38be-82de-cab775605325 | -4.75426 | -40.01597 | 2024-10-25 16:52:00 | NOAA-21 | MONSENHOR TABOSA | CEARÁ | Brasil | 2308609 | 23 | 33 | nan | nan | nan | Caatinga | 9.1 |
| 6e77c571-36d8-3ebb-bb4b-2dfc3eb1d0c9 | -4.75276 | -40.00748 | 2024-10-25 16:52:00 | NOAA-21 | MONSENHOR TABOSA | CEARÁ | Brasil | 2308609 | 23 | 33 | nan | nan | nan | Caatinga | 15.8 |
| 8b23fdbc-0dcf-3efa-8dff-9e07f9b3cb1b | -4.75092 | -40.0155 | 2024-10-25 16:52:00 | NOAA-21 | MONSENHOR TABOSA | CEARÁ | Brasil | 2308609 | 23 | 33 | nan | nan | nan | Caatinga | 22.3 |
| efc3ef05-2ab8-3450-befb-501db5c6c060 | -4.74951 | -40.00711 | 2024-10-25 16:52:00 | NOAA-21 | MONSENHOR TABOSA | CEARÁ | Brasil | 2308609 | 23 | 33 | nan | nan | nan | Caatinga | 19.2 |
| d7bd44fa-5fe8-32cb-a6c9-55525bcb591e | -4.74943 | -40.04293 | 2024-10-25 16:52:00 | NOAA-21 | MONSENHOR TABOSA | CEARÁ | Brasil | 2308609 | 23 | 33 | nan | nan | nan | Caatinga | 43.8 |
| ed209156-edcb-3284-9f9b-a97211cd5023 | -4.74834 | -40.01712 | 2024-10-25 16:52:00 | NOAA-21 | MONSENHOR TABOSA | CEARÁ | Brasil | 2308609 | 23 | 33 | nan | nan | nan | Caatinga | 9.0 |
| 20f566c5-b845-3852-9ab9-1431f38b79ce | -4.747 | -40.04428 | 2024-10-25 16:52:00 | NOAA-21 | MONSENHOR TABOSA | CEARÁ | Brasil | 2308609 | 23 | 33 | nan | nan | nan | Caatinga | 36.2 |
| 25e97481-8514-3790-8d38-9face558e99c | -4.74568 | -40.07136 | 2024-10-25 16:52:00 | NOAA-21 | MONSENHOR TABOSA | CEARÁ | Brasil | 2308609 | 23 | 33 | nan | nan | nan | Caatinga | 63.2 |
| e366eeda-73ba-37ed-9087-f8fb2afd7630 | -4.7449 | -40.06693 | 2024-10-25 16:52:00 | NOAA-21 | MONSENHOR TABOSA | CEARÁ | Brasil | 2308609 | 23 | 33 | nan | nan | nan | Caatinga | 33.6 |
| 0a4e49d0-79e0-360d-b88e-63c20d25d84c | -4.74419 | -40.08409 | 2024-10-25 16:52:00 | NOAA-21 | MONSENHOR TABOSA | CEARÁ | Brasil | 2308609 | 23 | 33 | nan | nan | nan | Caatinga | 94.8 |
| 99b62ec6-222c-3b82-a6bc-74fc4b17c334 | -4.74345 | -40.07974 | 2024-10-25 16:52:00 | NOAA-21 | MONSENHOR TABOSA | CEARÁ | Brasil | 2308609 | 23 | 33 | nan | nan | nan | Caatinga | 94.8 |
| b6a7f4e6-58ea-3ac2-881e-72892e203c37 | -4.7427 | -40.07528 | 2024-10-25 16:52:00 | NOAA-21 | MONSENHOR TABOSA | CEARÁ | Brasil | 2308609 | 23 | 33 | nan | nan | nan | Caatinga | 65.3 |
| 659849a0-191b-3d59-a9c1-27b175086806 | -4.74208 | -40.08547 | 2024-10-25 16:52:00 | NOAA-21 | MONSENHOR TABOSA | CEARÁ | Brasil | 2308609 | 23 | 33 | nan | nan | nan | Caatinga | 204.9 |
| 64957f02-fc1b-3405-beda-36aa138d75c0 | -4.74194 | -40.07079 | 2024-10-25 16:52:00 | NOAA-21 | MONSENHOR TABOSA | CEARÁ | Brasil | 2308609 | 23 | 33 | nan | nan | nan | Caatinga | 65.3 |
| 11e95ee3-4797-3210-9121-f00deb81c0de | -4.74119 | -40.06638 | 2024-10-25 16:52:00 | NOAA-21 | MONSENHOR TABOSA | CEARÁ | Brasil | 2308609 | 23 | 33 | nan | nan | nan | Caatinga | 45.0 |
| 80050861-2c51-3abb-9f65-0c6e71581870 | -4.74051 | -40.07662 | 2024-10-25 16:52:00 | NOAA-21 | MONSENHOR TABOSA | CEARÁ | Brasil | 2308609 | 23 | 33 | nan | nan | nan | Caatinga | 63.2 |
| d8cc952a-40cf-343c-b72a-4d0de67c0e11 | -4.73971 | -40.07214 | 2024-10-25 16:52:00 | NOAA-21 | MONSENHOR TABOSA | CEARÁ | Brasil | 2308609 | 23 | 33 | nan | nan | nan | Caatinga | 63.2 |
| 5e241f3a-885b-39bf-a742-c0a8b050b76c | -4.73893 | -40.06772 | 2024-10-25 16:52:00 | NOAA-21 | MONSENHOR TABOSA | CEARÁ | Brasil | 2308609 | 23 | 33 | nan | nan | nan | Caatinga | 33.6 |
| 2b8cb090-4850-3592-a87e-18150f826b4d | -4.73827 | -40.08508 | 2024-10-25 16:52:00 | NOAA-21 | MONSENHOR TABOSA | CEARÁ | Brasil | 2308609 | 23 | 33 | nan | nan | nan | Caatinga | 15.6 |
| 1468234d-0536-30de-bce7-522f0973cf69 | -4.7375 | -40.08057 | 2024-10-25 16:52:00 | NOAA-21 | MONSENHOR TABOSA | CEARÁ | Brasil | 2308609 | 23 | 33 | nan | nan | nan | Caatinga | 15.6 |
| a7f8cf58-eeba-332f-94e4-906eefd73de9 | -4.73674 | -40.07608 | 2024-10-25 16:52:00 | NOAA-21 | MONSENHOR TABOSA | CEARÁ | Brasil | 2308609 | 23 | 33 | nan | nan | nan | Caatinga | 21.2 |
| c4aa489a-ebc9-369e-942e-cc7f99d6945a | -4.73598 | -40.07163 | 2024-10-25 16:52:00 | NOAA-21 | MONSENHOR TABOSA | CEARÁ | Brasil | 2308609 | 23 | 33 | nan | nan | nan | Caatinga | 21.2 |
| f1229ad6-3166-3750-a55f-1db0ddaf0fd6 | -4.71141 | -39.9632 | 2024-10-25 16:52:00 | NOAA-21 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 1c8fd5e6-7ef0-3174-bbd2-1171ad841090 | -4.70914 | -40.05735 | 2024-10-25 16:52:00 | NOAA-21 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 14.0 |
| b4f58613-0cdd-3c93-a243-bafc608135db | -4.70837 | -39.96465 | 2024-10-25 16:52:00 | NOAA-21 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 9.7 |
| e8db6f51-5c66-3c94-8d09-740cd9d7b202 | -4.69681 | -40.0921 | 2024-10-25 16:52:00 | NOAA-21 | CATUNDA | CEARÁ | Brasil | 2303659 | 23 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 8970479f-9298-35ff-bcb8-793353cc0b4d | -5.79767 | -40.10084 | 2024-10-25 16:52:00 | NOAA-21 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 32.3 |
| b05dd33e-fec0-30fa-a4d7-cbfcdd754e69 | -5.65229 | -39.23317 | 2024-10-25 16:52:00 | NOAA-21 | MILHÃ | CEARÁ | Brasil | 2308351 | 23 | 33 | nan | nan | nan | Caatinga | 10.6 |
| a7599b84-ae2a-3a09-bf51-d364e3d4c7ec | -5.65157 | -39.23278 | 2024-10-25 16:52:00 | NOAA-21 | MILHÃ | CEARÁ | Brasil | 2308351 | 23 | 33 | nan | nan | nan | Caatinga | 8.5 |
| 9864f2fc-663c-36ce-b680-88c515a9ea87 | -5.64248 | -39.10427 | 2024-10-25 16:52:00 | NOAA-21 | MILHÃ | CEARÁ | Brasil | 2308351 | 23 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 8546bd53-241b-3a7a-9db9-5127ef465a81 | -5.6409 | -39.10431 | 2024-10-25 16:52:00 | NOAA-21 | MILHÃ | CEARÁ | Brasil | 2308351 | 23 | 33 | nan | nan | nan | Caatinga | 5.1 |
| e7aa2b0f-9634-3dfb-aec6-045b6f5ffc79 | -5.59444 | -39.65865 | 2024-10-25 16:52:00 | NOAA-21 | PEDRA BRANCA | CEARÁ | Brasil | 2310506 | 23 | 33 | nan | nan | nan | Caatinga | 11.1 |
| 3a7f6c48-2b60-3246-8e2b-7ff27e3bcd21 | -5.55417 | -39.67564 | 2024-10-25 16:52:00 | NOAA-21 | PEDRA BRANCA | CEARÁ | Brasil | 2310506 | 23 | 33 | nan | nan | nan | Caatinga | 8.4 |
| e37ee740-8b9d-3497-8c98-4f0587706398 | -5.55342 | -39.67142 | 2024-10-25 16:52:00 | NOAA-21 | PEDRA BRANCA | CEARÁ | Brasil | 2310506 | 23 | 33 | nan | nan | nan | Caatinga | 8.4 |
| f2691b6f-e852-3fc9-83eb-8febcfae5d0f | -5.55181 | -39.67523 | 2024-10-25 16:52:00 | NOAA-21 | PEDRA BRANCA | CEARÁ | Brasil | 2310506 | 23 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 7fbc76fe-ef0c-38b8-aaf8-10837ac47d1a | -5.55108 | -39.67093 | 2024-10-25 16:52:00 | NOAA-21 | PEDRA BRANCA | CEARÁ | Brasil | 2310506 | 23 | 33 | nan | nan | nan | Caatinga | 7.4 |
| cfa05d60-dcad-3d22-96c7-72f6af6aed90 | -5.35237 | -39.6098 | 2024-10-25 16:52:00 | NOAA-21 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 10.1 |
| 6dd2dba7-1e5a-3982-9c1f-49db5520986e | -5.33965 | -39.50226 | 2024-10-25 16:52:00 | NOAA-21 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 9.6 |
| 8a725418-0f96-36b4-8463-5fc617e5f969 | -5.32492 | -39.69987 | 2024-10-25 16:52:00 | NOAA-21 | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 67cc929d-4755-306a-aad7-9db7744e93a5 | -5.32272 | -39.69947 | 2024-10-25 16:52:00 | NOAA-21 | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 19.3 |
| 3ea1340a-4971-3824-a848-1d17220efb2c | -5.31894 | -39.70108 | 2024-10-25 16:52:00 | NOAA-21 | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 0173c69e-3d56-3e8e-944b-b24144d13ecb | -5.2849 | -39.80153 | 2024-10-25 16:52:00 | NOAA-21 | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 56eb90f2-e5f2-32e0-beb7-5275bfc0c246 | -5.28474 | -39.87053 | 2024-10-25 16:52:00 | NOAA-21 | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 46.6 |
| 02ade91a-777c-30c9-a38c-ae55e47babaa | -5.27022 | -39.64709 | 2024-10-25 16:52:00 | NOAA-21 | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 67.5 |
| 279ee4de-7c3d-3253-91cd-080500289176 | -5.26936 | -39.64215 | 2024-10-25 16:52:00 | NOAA-21 | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 67.5 |
| 616ecfd7-0c88-3e72-8250-96aeed59aa22 | -5.26338 | -39.64353 | 2024-10-25 16:52:00 | NOAA-21 | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 67.5 |
| 11f57d98-b582-3ad1-8b4f-0ff8fd5de453 | -5.24479 | -39.67911 | 2024-10-25 16:52:00 | NOAA-21 | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 15.6 |
| b2707695-c6df-34d1-9902-114704c23941 | -5.24394 | -39.67435 | 2024-10-25 16:52:00 | NOAA-21 | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 15.6 |
| 8266592e-a907-39eb-8904-958c92c3f839 | -5.22426 | -39.66848 | 2024-10-25 16:52:00 | NOAA-21 | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 16.3 |
| 8394cec2-69d0-3e8d-be44-70a67f124fae | -5.2236 | -39.96131 | 2024-10-25 16:52:00 | NOAA-21 | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 116.0 |
| 55be364a-6d53-3f49-8ba3-e374225f7002 | -5.2224 | -39.66849 | 2024-10-25 16:52:00 | NOAA-21 | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 14.5 |
| 67a91071-6543-3b1e-a838-ae5a481893ba | -5.21907 | -39.67422 | 2024-10-25 16:52:00 | NOAA-21 | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 16.3 |
| 7ca2a774-c37e-3674-8436-55fabc3cfac7 | -5.21716 | -39.67417 | 2024-10-25 16:52:00 | NOAA-21 | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 11.1 |
| 206e6c34-c038-3748-b73c-3fad9846cd6f | -5.21182 | -39.70309 | 2024-10-25 16:52:00 | NOAA-21 | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 50.1 |
| 1d04888f-f80f-35aa-b6c3-8f7bce52d11d | -5.211 | -39.69854 | 2024-10-25 16:52:00 | NOAA-21 | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 50.1 |
| 903671f5-f1e1-3ce7-9fc5-1abae9a9334a | -5.20972 | -39.70314 | 2024-10-25 16:52:00 | NOAA-21 | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 97.3 |
| 232389c9-faab-3a5e-b15d-78026cf88031 | -5.20894 | -39.69856 | 2024-10-25 16:52:00 | NOAA-21 | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 97.3 |
| 9c6fca85-4e80-3b91-80cd-52ce14e124ef | -5.20579 | -39.70407 | 2024-10-25 16:52:00 | NOAA-21 | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 34.1 |
| dbdad75f-7827-32b1-9de9-84a9e8c4ab67 | -5.20497 | -39.69948 | 2024-10-25 16:52:00 | NOAA-21 | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 34.1 |
| 0f00b2bc-ffa5-36be-aa21-ad7f9c862425 | -5.16229 | -39.7156 | 2024-10-25 16:52:00 | NOAA-21 | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 9.6 |
| 91f65881-d28f-3f80-84b5-715230db0903 | -5.15084 | -39.91362 | 2024-10-25 16:52:00 | NOAA-21 | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 43.0 |
| 24626332-8f66-3dbc-824a-989e20945b9b | -5.15005 | -39.90899 | 2024-10-25 16:52:00 | NOAA-21 | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 43.0 |
| b6900241-144d-3ab6-87e6-eeaa8047834e | -5.14893 | -40.08016 | 2024-10-25 16:52:00 | NOAA-21 | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 35.6 |
| ee2ea1f6-0b33-36c3-ad42-fe64677a4393 | -5.1482 | -40.07588 | 2024-10-25 16:52:00 | NOAA-21 | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 36.2 |
| 5379ad23-63b6-31c2-8cca-9ffc2921fb60 | -5.14698 | -39.90809 | 2024-10-25 16:52:00 | NOAA-21 | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 49.6 |
| 7dcf12a5-5168-3b5b-8b14-c4ea7921f998 | -5.13581 | -39.56465 | 2024-10-25 16:52:00 | NOAA-21 | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 6.4 |
| f0918547-e19a-3497-a2aa-28b78c78894e | -5.13491 | -39.8563 | 2024-10-25 16:52:00 | NOAA-21 | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 100.5 |
| f0ef69dc-9644-3362-a6da-1190003d31a2 | -5.1315 | -39.85571 | 2024-10-25 16:52:00 | NOAA-21 | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 54.8 |
| 9ea63ef1-aa10-3033-9a52-d7cec71f940e | -5.12107 | -39.48074 | 2024-10-25 16:52:00 | NOAA-21 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 07b8a07a-c36a-3636-9744-79cfc63a84d4 | -5.12024 | -39.47601 | 2024-10-25 16:52:00 | NOAA-21 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 293b5d42-8d9f-360b-be8b-f4f93da5519d | -5.10989 | -40.06484 | 2024-10-25 16:52:00 | NOAA-21 | MONSENHOR TABOSA | CEARÁ | Brasil | 2308609 | 23 | 33 | nan | nan | nan | Caatinga | 3.3 |
| cba7437c-65f6-3c25-8c50-323fac1cdd28 | -5.09474 | -39.76611 | 2024-10-25 16:52:00 | NOAA-21 | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 159.9 |
| a059ea44-cbf8-39f9-844c-8b9ae4c43fe4 | -5.09397 | -39.76162 | 2024-10-25 16:52:00 | NOAA-21 | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 159.9 |
| 311cb9d6-5cc0-3b5b-be86-23db9d95a06c | -5.09205 | -39.99767 | 2024-10-25 16:52:00 | NOAA-21 | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 42.4 |
| 36f660d0-a4fb-3fc3-9b4a-2ad9883304fb | -5.09126 | -39.99316 | 2024-10-25 16:52:00 | NOAA-21 | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 42.4 |
| 0ed0c9bc-ab37-3a19-aecd-79e295276599 | -5.08954 | -39.77176 | 2024-10-25 16:52:00 | NOAA-21 | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 110.7 |


[Clique aqui para ver as próximas entradas](README161.md)
