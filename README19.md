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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 198790d6-eb11-349f-a7ec-e909881d819d | -8.6569 | -49.70835 | 2026-07-02 04:38:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 78285304-f253-3f2c-a0f4-8f5bfd604638 | -12.91823 | -49.47742 | 2026-07-02 04:38:00 | NOAA-20 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5a9d6871-f070-3bc8-a69f-eea9b48430af | -12.91879 | -49.4739 | 2026-07-02 04:38:00 | NOAA-20 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4cf336fb-688b-3845-adcb-94e577895f38 | -13.73846 | -47.88729 | 2026-07-02 04:38:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b3896249-818a-33c9-9221-329ab9780e0f | -11.0427 | -56.9291 | 2026-07-02 04:38:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 6013c10d-9cce-3da1-bb03-e35b7226961b | -6.90351 | -48.04527 | 2026-07-02 04:38:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 212df2a7-5563-3f77-94df-4d616639cf93 | -12.86489 | -44.33835 | 2026-07-02 04:38:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 56.0 |
| 6f143119-bf47-3596-bb7a-f1c72699aef5 | -8.36253 | -45.66193 | 2026-07-02 04:38:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b95f1374-7f92-3a8f-8949-a39960497d5f | -10.37546 | -46.70428 | 2026-07-02 04:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 138.4 |
| ac494e3a-225e-37bd-bbca-19c2956573fb | -12.86791 | -44.34611 | 2026-07-02 04:38:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 41.0 |
| 30f03853-e604-3a49-9513-af9d02575adb | -7.10004 | -46.50953 | 2026-07-02 04:38:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 791c6655-e264-3dd5-a8e3-e8f84daeba7d | -10.37087 | -46.71143 | 2026-07-02 04:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 18.9 |
| ea35190e-44ce-36c3-9ef9-4b3781953dec | -10.94915 | -43.05416 | 2026-07-02 04:38:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 32.3 |
| 0a59b8b8-37e4-3592-8089-71b6df8ec68b | -9.15588 | -47.23885 | 2026-07-02 04:38:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e5dbe3a7-83d8-32ce-a67c-5902e3c1566c | -8.35748 | -46.8055 | 2026-07-02 04:38:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cf57e86f-ca35-34a3-a607-146c358a5c81 | -10.12108 | -52.09557 | 2026-07-02 04:38:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7f871e2c-9809-3546-aa2a-ce6b7b458f05 | -12.74161 | -44.47637 | 2026-07-02 04:38:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4528ffd7-d0a2-38da-bfd6-08320b40d5fc | -10.94173 | -43.04486 | 2026-07-02 04:38:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 1bc77a99-efc5-3256-8d12-f89ae295be1a | -12.76059 | -44.50124 | 2026-07-02 04:38:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 34.9 |
| be1275f7-bce2-3295-97b9-51b8ab3d05bc | -10.84699 | -45.05919 | 2026-07-02 04:38:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0092494c-4189-3a3b-a1f3-ac92d23a4268 | -10.12832 | -52.0968 | 2026-07-02 04:38:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 7a617a94-1e48-3d32-9e48-3fd2a45679cd | -8.31867 | -45.37433 | 2026-07-02 04:38:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 11e12ec9-a015-30dc-ba16-ff26905e9666 | -9.18319 | -58.05064 | 2026-07-02 04:38:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a37d933b-5dfd-3c51-9fce-39467d4c1c8f | -11.41535 | -56.06487 | 2026-07-02 04:38:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 4b095239-07c3-3627-a614-142b7436ab71 | -10.37718 | -46.69278 | 2026-07-02 04:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 5cac07aa-08a8-35f7-9813-98dc52b3c646 | -12.84576 | -44.35759 | 2026-07-02 04:38:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5e6231be-1429-3f64-a123-040b3cfc5835 | -11.00302 | -47.18432 | 2026-07-02 04:38:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 5017fed0-9ab4-312b-bdb1-245b29cf400f | -12.78593 | -44.49421 | 2026-07-02 04:38:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 508c40d8-e00e-3355-aac9-b652a08e9351 | -9.1598 | -47.23578 | 2026-07-02 04:38:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 99a887b5-6769-3bbf-9f26-a2fa7d09d3e7 | -12.86236 | -44.35632 | 2026-07-02 04:38:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 39.5 |
| 8704eaf6-ec37-381b-8a5b-9ddeced08aa3 | -12.51076 | -48.28491 | 2026-07-02 04:38:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 3f7b9d3e-8aef-371f-95f8-1319a48f8bf6 | -10.37803 | -46.6698 | 2026-07-02 04:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c6b0b2b4-ea9c-367e-b81e-633ec3f18ef4 | -8.17942 | -47.12152 | 2026-07-02 04:38:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4e485bd0-93a5-3f60-b5ab-33b7ca075599 | -12.85934 | -44.34859 | 2026-07-02 04:38:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 28.6 |
| 23ad9f66-9835-3e05-9478-267b1eb1706d | -10.02564 | -46.661 | 2026-07-02 04:38:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 664542fd-7cb9-3446-85f9-a30dd7a7904c | -11.42923 | -56.07032 | 2026-07-02 04:38:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 631c558d-bfe9-3b39-b729-7b49eee0797b | -13.73791 | -47.89091 | 2026-07-02 04:38:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d7044f1e-866b-3fb3-84bc-5a0da5a2b6a6 | -7.6616 | -46.89092 | 2026-07-02 04:38:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 77e8d9d2-2916-33f1-82be-75f94b99506b | -8.7159 | -48.33852 | 2026-07-02 04:38:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 06b45914-a7f3-3d6d-9f7e-7921559fd601 | -12.83822 | -44.35285 | 2026-07-02 04:38:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0c346017-5f55-363c-af3d-143ea680ff16 | -12.86438 | -44.34196 | 2026-07-02 04:38:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 56.0 |
| ec820930-fe9a-38b7-bd6a-4abf24f1784e | -12.74896 | -44.48188 | 2026-07-02 04:38:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 86.3 |
| 6a235014-3642-3773-939a-49fff972f21d | -12.76016 | -44.48885 | 2026-07-02 04:38:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 95.0 |
| 926c3fbb-45c5-3e2e-b413-06a63467b092 | -11.42444 | -56.0665 | 2026-07-02 04:38:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| b3036778-835f-344f-bbe2-a0cc8bdf6310 | -11.40274 | -49.00713 | 2026-07-02 04:38:00 | NOAA-20 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9acf9ef2-ee98-3488-935a-1e4c5a12b5b3 | -9.74743 | -49.0324 | 2026-07-02 04:38:00 | NOAA-20 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 48c3c480-ab4a-3574-9111-12443c516918 | -10.37333 | -46.70037 | 2026-07-02 04:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 3d4bc4cc-b7b2-3f01-8688-e14122e40a82 | -12.87092 | -44.35387 | 2026-07-02 04:38:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 57.6 |
| 08166573-7ec1-33e9-97fe-0cbc981f4344 | -12.51934 | -48.29005 | 2026-07-02 04:38:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ecc22eec-28da-361f-b498-551a8a7ac794 | -10.36812 | -46.71133 | 2026-07-02 04:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 8bc7fb3f-d641-373b-887e-30c2eb40ffdd | -10.81575 | -58.0206 | 2026-07-02 04:38:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6bdab99e-c9b5-3e0c-9d5b-b1eb73955e8a | -8.49238 | -46.90449 | 2026-07-02 04:38:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 538a7f97-fb09-39f3-a98a-784a621b65e2 | -12.50575 | -48.27303 | 2026-07-02 04:38:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fc49ba44-61f0-3934-8dab-cc5766022b1f | -8.71314 | -48.33452 | 2026-07-02 04:38:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 83331923-4093-3a95-bb72-52b60277c0ed | -12.84676 | -44.35045 | 2026-07-02 04:38:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 11.6 |
| e5a1f582-ae7d-3b94-9469-f3502a3afeb3 | -12.7657 | -44.52325 | 2026-07-02 04:38:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 994b8bd6-6edb-32fb-99df-09b725ab09fb | -9.26026 | -57.85991 | 2026-07-02 04:38:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 25fbf1cb-cd68-391b-9197-abbec4947141 | -12.85985 | -44.34501 | 2026-07-02 04:38:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 28.6 |
| 9e8cf0a2-5fa1-3392-922e-f7f309b287a1 | -8.7192 | -48.33905 | 2026-07-02 04:38:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| dc4735fd-904a-3ee6-8300-56d470cbbf0f | -10.02448 | -46.66858 | 2026-07-02 04:38:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| ca6b2ec0-4505-3342-a876-bbb7ac9e75df | -8.71535 | -48.342 | 2026-07-02 04:38:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 3daf1269-1750-380f-9c95-7dee01dac38f | -11.80263 | -57.00495 | 2026-07-02 04:38:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 128ecf83-987e-3b7b-84a7-1a97f6a48efb | -9.20771 | -45.32331 | 2026-07-02 04:38:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 01917db5-99cf-3b7e-99db-4646729ad3ee | -10.66326 | -54.52055 | 2026-07-02 04:38:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 41bf4770-8780-3dfb-ac09-492355783d9f | -9.4631 | -49.02554 | 2026-07-02 04:38:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c3734f60-35fb-3d9e-94d4-45181e9e950c | -12.51187 | -48.27772 | 2026-07-02 04:38:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8b3947d5-d95f-376d-a491-605636b3b523 | -12.86842 | -44.34249 | 2026-07-02 04:38:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 6b233d4d-b5c1-3b7e-8628-98a458afdf2d | -8.06744 | -46.70941 | 2026-07-02 04:38:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 90d71e83-38e3-3f9e-8447-8b284a4bca9f | -11.49028 | -47.38746 | 2026-07-02 04:38:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b74df1aa-0474-37d5-a89e-d3c546c9bcda | -12.87194 | -44.34666 | 2026-07-02 04:38:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 41.0 |
| 9ff229d5-1b32-3a9a-8aab-8af2fbcde8a1 | -10.78634 | -53.54216 | 2026-07-02 04:38:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 59306dc7-a41b-34ca-a962-330a070b49f0 | -10.80314 | -48.56559 | 2026-07-02 04:38:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7b6c24fc-2bd0-3c10-93e3-8baad2aedd2d | -11.4199 | -56.06566 | 2026-07-02 04:38:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| fa64cc0c-f124-39de-b612-705bf9ddf494 | -8.87511 | -50.18221 | 2026-07-02 04:38:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6c0d55e8-418d-329a-834f-c24d348e30a9 | -10.37392 | -46.69654 | 2026-07-02 04:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 19.0 |
| c19d741e-df63-3cb8-8463-a5268e2bbf52 | -13.72489 | -47.88495 | 2026-07-02 04:38:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e53b2e0b-89c5-309a-b5c7-a545e8044910 | -12.76856 | -44.50238 | 2026-07-02 04:38:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 17528d7a-084f-3ee6-923b-c6cdfb17899a | -11.30006 | -46.46161 | 2026-07-02 04:38:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1e3968d5-6508-3e40-bc38-bde403fe3454 | -11.41905 | -56.07042 | 2026-07-02 04:38:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ac19ddd3-e698-3217-93d1-974dc423b9d4 | -12.45362 | -46.91425 | 2026-07-02 04:38:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 15b093b0-0211-3d56-a9af-c449a0d419f0 | -10.78148 | -53.54396 | 2026-07-02 04:38:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7a9b2fd0-e174-33f3-a9c5-50aac6716c38 | -8.65297 | -49.71139 | 2026-07-02 04:38:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8e2839b0-47da-3bfc-a29d-9a36495a3008 | -8.87391 | -50.18953 | 2026-07-02 04:38:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c1a82912-c247-3fb8-82be-0c83e54ff354 | -9.20834 | -45.31903 | 2026-07-02 04:38:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fa52c7dd-9666-3026-b36d-269a84a5bcf0 | -10.66957 | -54.53333 | 2026-07-02 04:38:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 62d97f1d-ccc1-32b7-b1a5-56856c6a9cdf | -12.85079 | -44.35102 | 2026-07-02 04:38:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 6b18a23b-8c3e-3642-9095-539bf343ad17 | -12.85531 | -44.34803 | 2026-07-02 04:38:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 80ec74c7-f250-3b87-a729-e39679d1e8c5 | -10.37451 | -46.6927 | 2026-07-02 04:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 6c017ea7-6b15-33de-8af2-630ba58ed10c | -11.42016 | -56.06861 | 2026-07-02 04:38:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 2159fad9-5ff2-3440-8908-fd6e81e450d2 | -11.4165 | -56.06307 | 2026-07-02 04:38:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 11.8 |
| c9427de4-d49d-3e8e-8d02-57da1adddb32 | -9.15644 | -47.23525 | 2026-07-02 04:38:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 83768af9-0ada-357b-a823-8d1e1bb2c265 | -12.86286 | -44.35275 | 2026-07-02 04:38:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 39.5 |
| 35a9b8ba-adcf-305a-935c-d908267af84a | -7.09722 | -46.50536 | 2026-07-02 04:38:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b294887c-fdf6-3098-b509-ae6d4ffa387a | -12.23174 | -47.48415 | 2026-07-02 04:38:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bfe61b03-48ba-3ebe-98bb-a56baa6a9f2e | -12.62318 | -44.65914 | 2026-07-02 04:38:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 658a712f-a51d-331c-9f69-4f35864dee82 | -12.5141 | -48.28545 | 2026-07-02 04:38:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 7023e24d-6a5f-3bd2-ad34-9fe687f671db | -12.76896 | -44.52903 | 2026-07-02 04:38:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 69d28e52-533a-39fe-90e1-222e0be19e8a | -9.75643 | -47.87651 | 2026-07-02 04:38:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2b600be8-9122-3364-9fa2-de7a5cd43bf4 | -11.91118 | -43.38902 | 2026-07-02 04:38:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1979822f-a57a-3ab9-8390-d61006593c3e | -11.35293 | -55.42746 | 2026-07-02 04:38:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README20.md)
