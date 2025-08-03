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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a32dd6d1-e8ad-380e-8f24-fa17623260c4 | -12.64342 | -44.5098 | 2025-08-03 04:27:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5d25a600-cc9f-343d-94d5-29217a52dfe8 | -12.03294 | -44.02038 | 2025-08-03 04:27:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 7f0ffe3f-f576-3299-b2f2-7209e1b9cc88 | -12.66889 | -44.51363 | 2025-08-03 04:27:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0695797f-5b5d-3125-8fd3-219cfd12da0e | -12.62523 | -44.50703 | 2025-08-03 04:27:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c668f43e-31c2-3c26-b778-beada06c71e0 | -11.93527 | -46.71362 | 2025-08-03 04:27:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a5502140-4998-38cf-aa6c-e7a3a0de8e4a | -13.07805 | -47.39127 | 2025-08-03 04:27:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5f74802a-8b2a-30bf-b2ab-8afade839137 | -12.68041 | -48.0898 | 2025-08-03 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2ea45c18-b649-3305-a6c4-7fe1e59ab3db | -8.93894 | -46.74871 | 2025-08-03 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 3f6316cb-670a-3113-8e7d-942637a4f1d1 | -11.20901 | -51.5324 | 2025-08-03 04:27:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 26bec7e7-1f7f-3154-8a3c-3a55b9a20546 | -15.65677 | -43.58273 | 2025-08-03 04:27:00 | NOAA-21 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a8be3895-00e8-3b0a-a9ff-cc7ad2b3feb6 | -6.83162 | -59.26421 | 2025-08-03 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7d2ff9da-33b2-3dbc-87a5-f0db05feb960 | -7.78292 | -45.20742 | 2025-08-03 04:27:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 3a0cbe3c-6cbe-3f16-8382-7fabd6081897 | -11.95304 | -44.93887 | 2025-08-03 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 03ad97ba-06e4-3118-b460-181e8a77bc96 | -13.23328 | -47.24409 | 2025-08-03 04:27:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| de35c2c7-1328-314f-a237-eff7e60bba7f | -12.66347 | -44.4996 | 2025-08-03 04:27:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| ec5698df-1222-3da7-b2b3-8f0ea7bfc9e2 | -14.16422 | -45.44175 | 2025-08-03 04:27:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4985ca4f-ad40-300c-b000-06e95057c480 | -11.76971 | -44.9798 | 2025-08-03 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 487750ad-698d-3d41-87d9-3fc3297103a7 | -10.47757 | -46.95409 | 2025-08-03 04:27:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a82e4af2-c760-3c05-a318-424c3389179b | -12.6782 | -48.08224 | 2025-08-03 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cb35c62b-11af-3c88-9d50-59de580b4de8 | -12.66099 | -44.51685 | 2025-08-03 04:27:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5d07ec60-05d6-3d5a-a964-2498e1b4be1e | -12.46115 | -47.0267 | 2025-08-03 04:27:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3fc601a2-945b-3897-92fa-55963f5edbc3 | -12.64219 | -44.51839 | 2025-08-03 04:27:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4f0d2ef9-20a9-38ba-bb97-cc13b8da4e1c | -12.70167 | -45.0361 | 2025-08-03 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7e6c6abf-36ae-3b82-91a0-a9787aff0459 | -11.74619 | -54.72543 | 2025-08-03 04:27:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 88b68c39-e2e9-3fc5-8a2b-4f8c98178575 | -12.50285 | -49.01337 | 2025-08-03 04:27:00 | NOAA-21 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 842c9ded-2e5a-3add-8d3e-d372544bb3fc | -10.25696 | -50.24542 | 2025-08-03 04:27:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 19f2c20b-8104-33b6-8fe0-21b02e039bfb | -14.17304 | -45.45563 | 2025-08-03 04:27:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5e17f2d5-1d0a-32a4-afa0-fd17e784f7e9 | -7.97181 | -45.09795 | 2025-08-03 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e44352c0-3b84-36ab-8f3d-81d561ffc080 | -12.43402 | -44.86506 | 2025-08-03 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 18ecfaf8-aca4-3319-9ae5-5aa2d18715e9 | -12.64403 | -44.5055 | 2025-08-03 04:27:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 19a35fca-b4e3-3048-85b2-2292a7d8b6d9 | -8.9417 | -46.75271 | 2025-08-03 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 17cf3184-d5b3-33d7-aa7c-224909657fab | -13.07152 | -47.43354 | 2025-08-03 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 77d368a4-b1de-3570-874b-85332004de04 | -13.07043 | -47.44062 | 2025-08-03 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1bbe28df-d462-3ff9-8121-45c83cc7f6fb | -11.77627 | -44.98759 | 2025-08-03 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ad87246f-5dc6-3789-86f4-2b758219770d | -10.78646 | -48.80878 | 2025-08-03 04:27:00 | NOAA-21 | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 47331d74-042a-35fe-9837-03f1c1aefb27 | -12.66037 | -44.52115 | 2025-08-03 04:27:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3d31b5dc-2394-3b42-a93c-9de5263bae01 | -12.63856 | -44.51784 | 2025-08-03 04:27:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e9283ba0-7b3e-3d3c-bd0c-6b5670aa7071 | -7.95831 | -45.11837 | 2025-08-03 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1405a99d-2e98-3dda-8d06-9851453089df | -11.77275 | -44.98706 | 2025-08-03 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e7a0a7d1-65bf-32fd-b383-46380eb86c06 | -12.62281 | -44.49787 | 2025-08-03 04:27:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dc26f97b-0561-3e64-95f5-1ee3467e0da2 | -10.3444 | -44.90771 | 2025-08-03 04:27:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6f9a0318-c066-3cda-99f4-da3f517a235c | -11.9501 | -44.93428 | 2025-08-03 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a450e068-26a4-36db-a85a-381e0416ab21 | -12.66897 | -44.4872 | 2025-08-03 04:27:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 4845cc5d-b833-3036-bf48-60639b5cbd5a | -7.88432 | -45.52486 | 2025-08-03 04:27:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d30a617a-721c-364b-abb0-fe2ecc096654 | -12.62645 | -44.49842 | 2025-08-03 04:27:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c5a4e026-d29e-3d5a-85a7-552d96d27af0 | -11.77263 | -44.98435 | 2025-08-03 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a3665878-d43e-33f4-be9e-5f1039529cc3 | -7.87986 | -45.53148 | 2025-08-03 04:27:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1011bfd0-b413-3360-ba6a-52aeeaacd898 | -6.81615 | -59.27367 | 2025-08-03 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 5baaa2d9-6769-3b6f-92a6-946782dc483d | -14.1707 | -45.44692 | 2025-08-03 04:27:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7a41fcbc-ba07-3e38-8e83-88ee4baa5f58 | -10.48038 | -46.97964 | 2025-08-03 04:27:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 94442bce-a1d5-312b-b248-b81268730db5 | -13.06489 | -47.43247 | 2025-08-03 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4db8e6a3-76f6-38c9-8e1d-7acbc0bdb061 | -12.62948 | -44.50329 | 2025-08-03 04:27:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| b0de1940-1bc7-3d5f-bffe-d2acf911521a | -14.16541 | -45.43356 | 2025-08-03 04:27:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d4226cdd-050b-3c15-b6b3-1f6018865914 | -12.67066 | -44.5271 | 2025-08-03 04:27:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 85f95272-72ea-3945-8159-d2d627a16889 | -13.68016 | -41.36895 | 2025-08-03 04:27:00 | NOAA-21 | ITUAÇU | BAHIA | Brasil | 2917201 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 16c57396-a891-3c9b-ac14-c8288f780520 | -11.93797 | -46.67373 | 2025-08-03 04:27:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 686a5278-f5bc-3402-9e4e-08fd5d6fd720 | -12.49918 | -47.17845 | 2025-08-03 04:27:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c444ec18-3c77-3873-8024-b5c36a8b4275 | -12.67261 | -44.48774 | 2025-08-03 04:27:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 9d2e32b0-7780-341d-8a26-59419e8cd43a | -11.9507 | -44.93019 | 2025-08-03 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9ecd394b-1d18-3d42-a22a-c95b49a896a0 | -12.49085 | -47.16621 | 2025-08-03 04:27:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 99bc072f-a1ee-360d-ba71-8c4a059c65d8 | -11.21277 | -51.53304 | 2025-08-03 04:27:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 176d125d-e11b-30d6-b56a-e3362ec4fc34 | -13.70018 | -41.37376 | 2025-08-03 04:27:00 | NOAA-21 | ITUAÇU | BAHIA | Brasil | 2917201 | 29 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 2a36fdd2-190b-3c53-86b8-f50ec3ef9e3d | -11.81568 | -44.86454 | 2025-08-03 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 73ee4c19-5859-3817-bbfa-4f55a023079d | -9.39233 | -45.50411 | 2025-08-03 04:27:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 85ceb1ec-82c3-34c9-93b5-65dcee26723a | -12.64465 | -44.50119 | 2025-08-03 04:27:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4f9cd5e3-2aef-33f5-9ec2-7afeb78e03c8 | -8.43193 | -47.46603 | 2025-08-03 04:27:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 87180d5b-a5ad-33df-8797-272f54ac39a2 | -12.6568 | -44.49419 | 2025-08-03 04:27:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 020f3d7b-8a4c-3114-ac3f-b8a6e7feb3ff | -12.63553 | -44.513 | 2025-08-03 04:27:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b9b01406-c6e3-38bb-8b99-fcb2474ab5d6 | -10.47816 | -46.97212 | 2025-08-03 04:27:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0fcbba96-4d8c-37c7-b076-19efe8bc8672 | -8.28032 | -47.32759 | 2025-08-03 04:27:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4080a32d-99e2-3674-ba99-467f67b83230 | -9.35292 | -50.73726 | 2025-08-03 04:27:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1f24474f-cec0-3ee6-9c2f-35919457073c | -12.93579 | -43.19015 | 2025-08-03 04:27:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 24d7ebbe-315a-3a9a-a920-be09eb541867 | -7.96565 | -45.11576 | 2025-08-03 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c3daf0f4-7953-3677-bcab-7d7a36d06988 | -12.65557 | -44.50283 | 2025-08-03 04:27:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| be554d39-af44-3e45-8a70-9d1d6a4f1f28 | -12.65254 | -44.49797 | 2025-08-03 04:27:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 49c5f4a9-0e30-3e33-8fb9-daab0fff1ec3 | -7.9673 | -45.10477 | 2025-08-03 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 86eca47c-9943-3aac-925f-495a55482267 | -12.62342 | -44.49356 | 2025-08-03 04:27:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6a0476a8-5bea-31ea-942f-d23608fd81cd | -12.41063 | -47.06984 | 2025-08-03 04:27:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 59632ca7-c2e9-3bca-9c5d-36a573b3835d | -8.94555 | -46.74975 | 2025-08-03 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| faeaffba-fb23-3695-88c1-335060c9957b | -11.76678 | -44.97525 | 2025-08-03 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 95902c6b-7e2e-3252-ab20-03d9d80d8728 | -11.94482 | -44.9703 | 2025-08-03 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6d7d5d41-ad15-3f6c-a514-e0e4a95a297e | -10.78983 | -48.80933 | 2025-08-03 04:27:00 | NOAA-21 | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5dbec661-2f3a-31d1-8315-c20c966a91a3 | -11.77556 | -44.98888 | 2025-08-03 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4bb1976a-365f-3b8a-8691-4d596f595ef9 | -12.42887 | -47.03993 | 2025-08-03 04:27:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 18ab1f39-2583-3bf3-9857-ad3f33074fda | -12.79495 | -45.44188 | 2025-08-03 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| aa6c47b2-340e-3e6f-b797-b290622465ca | -12.61917 | -44.49732 | 2025-08-03 04:27:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0046195b-39c6-3bc5-a865-441eca9d6435 | -13.66041 | -47.31686 | 2025-08-03 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3a30266d-ff23-315d-821c-7514046ef84a | -13.6729 | -44.22651 | 2025-08-03 04:27:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 91928e48-62fa-3a3f-86dc-5f9ef516deb5 | -12.65495 | -44.50715 | 2025-08-03 04:27:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8b7104bd-7224-3201-890b-13146b10bbde | -6.65144 | -59.10689 | 2025-08-03 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 23.6 |
| 0eb3847f-8825-36f3-89a7-30efba7f7d69 | -12.4914 | -47.16265 | 2025-08-03 04:27:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d088b2df-d54e-3f50-b363-ffb4ce9659be | -11.93369 | -44.92273 | 2025-08-03 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9700fdcf-de79-3122-a979-8ea3ae711ed9 | -7.96841 | -45.09741 | 2025-08-03 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b0277d49-9824-310f-a49c-d4fa25880df5 | -8.93563 | -46.74818 | 2025-08-03 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 33538b76-8888-3437-b52a-602274d87ad4 | -8.94279 | -46.74575 | 2025-08-03 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f041f41e-cf71-3721-a4a1-17aeda0af13c | -13.06988 | -47.44417 | 2025-08-03 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2ff8d4ef-8061-366b-b5df-e9839bc1fe92 | -12.61783 | -44.66309 | 2025-08-03 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2beb9cf3-64df-3893-833f-40d9368f1d5c | -8.40486 | -47.4868 | 2025-08-03 04:27:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7a64dcc9-0ce3-3967-ac00-9d7934e28a0c | -13.67093 | -47.31491 | 2025-08-03 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 32c1da9e-37da-3f23-b004-6201e6ad1c7c | -11.93888 | -44.96159 | 2025-08-03 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README17.md)
