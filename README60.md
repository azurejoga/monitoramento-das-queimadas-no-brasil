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

## Dados Diários - Página 60

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dc647e06-f349-30fb-b297-e9fb62b0c00f | -11.35713 | -54.05265 | 2026-09-29 05:12:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ab9d7d6a-5622-3e29-bff7-1eede6beaa9b | -12.27647 | -50.26873 | 2026-09-29 05:12:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 07b0fb00-20b8-3ba9-94e2-66a303a3e358 | -11.30172 | -58.34182 | 2026-09-29 05:12:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 330ef47a-cef0-3c7d-8de7-e176e3ddc8c4 | -14.5096 | -48.30515 | 2026-09-29 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 87e57929-0e7b-37fd-8049-f96b2a9b4c20 | -11.41486 | -43.45119 | 2026-09-29 05:12:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6fd83e80-f451-3d16-994f-e35a9355b370 | -12.39373 | -50.22449 | 2026-09-29 05:12:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 9a21fcda-d161-3424-bc80-3199ff315f2b | -12.1645 | -50.81918 | 2026-09-29 05:12:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0d5b397c-10ac-3926-8c82-571aa91b619b | -10.26604 | -44.63314 | 2026-09-29 05:12:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 660d544d-2ce9-3070-92d2-fb8c9dbaf269 | -11.95641 | -50.93053 | 2026-09-29 05:12:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a0a4d048-b5b4-32c0-acb2-d443f3fbe281 | -11.18726 | -45.14703 | 2026-09-29 05:12:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5db2dee7-6552-3b79-90b8-1cd02d966d34 | -13.43253 | -48.6211 | 2026-09-29 05:12:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f95b0ba5-df0e-3306-a09c-3a40e8c1eb60 | -11.35476 | -54.04384 | 2026-09-29 05:12:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 056e3571-f063-3647-a709-ff343ba048c3 | -11.17098 | -44.79176 | 2026-09-29 05:12:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 13.9 |
| d3e58745-a81f-3652-bc33-aa0d84768763 | -14.51002 | -48.30164 | 2026-09-29 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0dfb4cf8-e859-3269-a389-fc65a0d34beb | -11.19122 | -45.13259 | 2026-09-29 05:12:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 10419e7b-d76d-3811-bb2f-57447ead2e65 | -11.29896 | -58.33765 | 2026-09-29 05:12:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a699ae33-cba4-3240-934c-030ab206a2c9 | -11.39097 | -47.4553 | 2026-09-29 05:12:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fca6dfcd-51dd-3d17-8dfd-a703dd4f096c | -11.34374 | -54.11846 | 2026-09-29 05:12:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 03e5b651-ca67-3c2d-bf26-4a8298d8cf29 | -11.42346 | -43.43808 | 2026-09-29 05:12:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| be778628-ba91-3564-8f36-fa1f3938f554 | -11.39588 | -45.41124 | 2026-09-29 05:12:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8730c06e-af59-3f37-a5de-3335bd11c51d | -11.96138 | -50.92686 | 2026-09-29 05:12:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d98ecca0-e972-3e62-ac6a-a70479b3d90b | -11.42423 | -43.43119 | 2026-09-29 05:12:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| b20848a4-4deb-3410-ac6b-a52e71069e3b | -11.41258 | -43.43015 | 2026-09-29 05:12:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3241bd08-d608-333d-95aa-2643b9eb5fa3 | -9.08734 | -49.8817 | 2026-09-29 05:12:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5fe10b32-9e08-3319-884d-72fd67967bf8 | -14.21283 | -48.50756 | 2026-09-29 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1b5d7ac4-aa21-339a-bf0c-480ddd551a8b | -13.11063 | -47.40763 | 2026-09-29 05:12:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 362d3c49-f1f2-33a3-a15f-2fd3304a0d06 | -14.09147 | -46.31232 | 2026-09-29 05:12:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1a6bc5b0-39ab-3048-a905-04f1a986d10e | -7.49714 | -55.02613 | 2026-09-29 05:12:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3f18f37f-268b-3d04-82a8-d27d28556eb6 | -9.96395 | -59.25692 | 2026-09-29 05:12:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fe01a58f-aa9d-3546-a5bf-4b89436b0511 | -7.51391 | -55.02873 | 2026-09-29 05:12:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 709cef59-74cd-3904-ab55-5c33f51c5bad | -7.55804 | -55.03207 | 2026-09-29 05:12:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 307ce203-8f9c-3907-9d88-42212b580fbd | -13.14277 | -48.54623 | 2026-09-29 05:12:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d5e81bcc-457d-3ae4-8c97-5bd25fe2af80 | -7.5033 | -55.03075 | 2026-09-29 05:12:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0c87de39-b7d7-3748-a52c-306437e08d57 | -9.69155 | -58.11492 | 2026-09-29 05:12:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c5d92912-c188-334c-a972-93ed39cca6c3 | -13.53376 | -49.18036 | 2026-09-29 05:12:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 352d336a-ffe6-3aef-9057-2e8c1edd641c | -11.39684 | -43.44258 | 2026-09-29 05:12:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cfb4e751-6532-3e2f-ab1e-cdf20ebd5af9 | -12.05416 | -50.216 | 2026-09-29 05:12:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c57ecb55-e254-3854-a436-4074186c0f2c | -13.1724 | -48.56493 | 2026-09-29 05:12:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 47a45659-5031-3fc1-8ce5-8a05a74aa0ea | -9.077 | -49.87788 | 2026-09-29 05:12:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c9fc515f-241c-3e77-a450-cd0d5d0d90c0 | -12.06327 | -46.5018 | 2026-09-29 05:12:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f6f0b330-99a3-3cdc-8997-ba150ad7bb10 | -11.40471 | -43.43635 | 2026-09-29 05:12:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 95c65eea-a6ce-31d0-bf4c-50aa50ffac09 | -11.43603 | -43.45349 | 2026-09-29 05:12:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 26340560-fc49-3d8e-bc52-4c8971706518 | -12.02008 | -50.92447 | 2026-09-29 05:12:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| ccd69f62-2a5d-3534-8168-4cdea440548d | -11.18363 | -45.14259 | 2026-09-29 05:12:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 40b516a8-898b-3ef8-bad9-94773cf81de5 | -13.17203 | -48.56793 | 2026-09-29 05:12:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1b8d00d9-2b5a-3130-a34a-e4efb7d043dc | -11.40151 | -43.44279 | 2026-09-29 05:12:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 67b879be-342e-3f00-ad1d-8edb90242b78 | -11.18789 | -45.14181 | 2026-09-29 05:12:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| efaf1a85-09d4-3542-bab2-c1e74ecb5388 | -12.04141 | -50.93184 | 2026-09-29 05:12:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| dc3e86d4-5677-3756-b632-8ad05d6f210d | -13.16478 | -48.54023 | 2026-09-29 05:12:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 67a2a02f-583d-37c2-8cb4-63523b907029 | -11.34793 | -54.1149 | 2026-09-29 05:12:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 68615d0e-e3e5-3e5e-a929-7e266155834f | -12.94031 | -46.66479 | 2026-09-29 05:12:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 52ef419d-b7c5-3776-b960-5f0458c11d4e | -10.93057 | -47.59489 | 2026-09-29 05:12:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1fe1ad89-61c4-3f8f-995a-308ed4dd48c2 | -14.2132 | -48.50443 | 2026-09-29 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 08f04418-6f73-3d26-8b1c-60b9e105f9db | -12.24569 | -50.43086 | 2026-09-29 05:12:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bf5a6ed5-379e-31c7-b79a-88c73d818fe9 | -12.60826 | -60.90173 | 2026-09-29 05:12:00 | NOAA-20 | CHUPINGUAIA | RONDÔNIA | Brasil | 1100924 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cfd468a0-b298-3d63-a3f7-ffc3073a83de | -11.93571 | -50.91889 | 2026-09-29 05:12:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7806021a-eb90-3b8d-81bd-774c68b5184b | -9.13783 | -49.9811 | 2026-09-29 05:12:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 177c07cd-0208-3b70-9f5e-bd65ba67a65f | -9.78142 | -48.2243 | 2026-09-29 05:12:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4b580f97-e880-3062-90a1-6d13bc872158 | -11.37989 | -54.04765 | 2026-09-29 05:12:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c01ceea6-0ba9-39fe-b045-0235272eee2d | -12.74424 | -47.27762 | 2026-09-29 05:12:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 5dfba546-544d-3276-abbd-689c47fa12de | -12.73901 | -47.27314 | 2026-09-29 05:12:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| b61f7b7e-3876-3af3-93d9-7bad02051e4e | -11.35178 | -54.03912 | 2026-09-29 05:12:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b278411b-91ea-3dcf-8c10-b92a024bf81b | -11.08149 | -47.50813 | 2026-09-29 05:12:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a2a438e3-25b1-3688-88dd-316133fe310e | -9.82541 | -48.20655 | 2026-09-29 05:12:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 42d18f48-3962-3001-a382-cda6738f20a7 | -9.95628 | -50.15288 | 2026-09-29 05:12:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c0674b52-6be5-3de6-bf38-879d9a7a1289 | -13.43778 | -48.62165 | 2026-09-29 05:12:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 60d6e700-7fc2-3d74-ae58-36f91ac66f82 | -10.27186 | -44.63936 | 2026-09-29 05:12:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 186ff3a3-f403-39a6-865e-1dd5f4576181 | -12.93974 | -46.66947 | 2026-09-29 05:12:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0166b18a-e206-34a9-bf69-c512e2d296f8 | -13.45794 | -48.5864 | 2026-09-29 05:12:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c46bb0bb-0eea-3eee-ab5a-3f8489d927ce | -11.95582 | -50.93483 | 2026-09-29 05:12:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 321d13b0-97ca-36ef-a6d3-91406d9999ae | -12.0642 | -50.21539 | 2026-09-29 05:12:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ab8cfef0-4d17-3620-9744-5d5115cc0a5b | -10.4287 | -53.83986 | 2026-09-29 05:12:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c3a2907a-a6f6-347d-9da8-41c23873804f | -11.17679 | -44.79834 | 2026-09-29 05:12:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 4b627779-af37-3165-8adb-50900728024c | -10.25952 | -44.63256 | 2026-09-29 05:12:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| e15823b7-7482-31c9-bb49-cf7599bcc699 | -12.79602 | -54.01538 | 2026-09-29 05:12:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| be9e2064-6f09-3e03-8585-871314d7d789 | -12.00957 | -50.93615 | 2026-09-29 05:12:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| faa6df72-d99f-3c20-89a7-574d90e82962 | -12.73949 | -47.26899 | 2026-09-29 05:12:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 79ec7581-49f9-340a-a910-c2f6129bf8dd | -9.76979 | -54.28425 | 2026-09-29 05:12:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0eafe754-ea63-35d5-8ca3-1d6bd4c7ead2 | -11.43132 | -43.45312 | 2026-09-29 05:12:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1f0407a8-6635-3221-bfd3-5a9f3168cb20 | -11.00857 | -54.1391 | 2026-09-29 05:12:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f7e7bf4b-6b29-38f6-8180-c6c3a0f3b3e8 | -10.38084 | -61.25326 | 2026-09-29 05:12:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b6c87e68-1a87-3cf3-b42d-92392e4607be | -12.009 | -50.94044 | 2026-09-29 05:12:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 4cb19edf-68aa-32a4-a76f-07657eb7eda5 | -14.11934 | -46.2855 | 2026-09-29 05:12:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5286f4ba-cb6e-3b28-b367-1ba5d131e6f6 | -7.51615 | -55.0364 | 2026-09-29 05:12:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f006da54-1120-3ec2-b2f7-71dc9e862ac5 | -12.7231 | -46.99637 | 2026-09-29 05:12:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 20.1 |
| c2c8b589-a0f4-3115-98b1-e849c1301621 | -11.39128 | -54.04514 | 2026-09-29 05:12:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c788f4d4-6875-3c24-a970-92ef0a00ce13 | -11.12843 | -48.33838 | 2026-09-29 05:12:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7096a800-46bb-3160-935b-25d31abcbaa0 | -12.93386 | -46.66849 | 2026-09-29 05:12:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 14189267-b274-3dc5-9291-553b04e5c7bb | -11.41177 | -43.43708 | 2026-09-29 05:12:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d9812807-3377-3601-b541-401b793b0a72 | -12.00527 | -51.0009 | 2026-09-29 05:12:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 5492c510-fa78-3126-bde1-5c30c7dcacb9 | -11.99966 | -50.94351 | 2026-09-29 05:12:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| efed9373-2a68-3e57-bc76-57d3140d8cd2 | -9.16574 | -61.40707 | 2026-09-29 05:12:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 13.6 |
| f4a6f182-4ded-3cc3-976b-0426cce505c1 | -11.34697 | -54.04685 | 2026-09-29 05:12:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3156b7e8-6a0e-32ca-beed-93846a4b7ef6 | -10.39621 | -61.25602 | 2026-09-29 05:12:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 1d9ce462-fc93-3b23-b760-4300f14a648a | -11.55107 | -54.49731 | 2026-09-29 05:12:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 940d1fea-02e8-3060-b198-14e81c90195e | -9.54403 | -56.16048 | 2026-09-29 05:12:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f56387bb-0ca1-394a-9dd6-3736dcb83c94 | -11.43448 | -43.46731 | 2026-09-29 05:12:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 4dfc5e80-a52b-3b17-a973-c5b341997cb1 | -12.04082 | -50.93614 | 2026-09-29 05:12:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8ff7fc27-893b-3c61-bb8b-75f5cf59eca3 | -12.79109 | -54.02354 | 2026-09-29 05:12:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 421a530d-2cf4-3db9-9377-1ee290441168 | -12.03964 | -50.94474 | 2026-09-29 05:12:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README61.md)
