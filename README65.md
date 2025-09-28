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

## Dados Diários - Página 65

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a97542ef-0214-3600-aba2-fede3e4be1b3 | -6.92097 | -39.58609 | 2025-09-28 04:25:00 | NOAA-20 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 2d56f5ff-5850-3d69-be97-1c3ad0e54c05 | -7.16772 | -45.49913 | 2025-09-28 04:25:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0d2045a9-3c07-310b-8c5f-9b40ac708f56 | -6.77939 | -44.08364 | 2025-09-28 04:25:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4e340441-f489-3821-921a-410a364817cc | -9.40827 | -54.69453 | 2025-09-28 04:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2bf606f3-824b-3e19-86bb-1a6f64a998c3 | -11.35548 | -45.00242 | 2025-09-28 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| edf00a45-24ba-31e9-8aa0-fe809becd142 | -12.87528 | -46.79801 | 2025-09-28 04:25:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 085d181b-50ed-3734-903c-ecebe76d2fa0 | -6.3225 | -41.88314 | 2025-09-28 04:25:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| d3e6868d-db2c-3c11-a4b4-8247b0176d7a | -12.86973 | -46.78977 | 2025-09-28 04:25:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 10315937-a15a-31bb-a0e0-83a71695b226 | -7.5054 | -44.30339 | 2025-09-28 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8be52a98-1ca3-3e69-859c-9703f9f7556e | -11.44353 | -44.98383 | 2025-09-28 04:25:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0543d736-d60e-3779-83e5-a2d3654343be | -7.73943 | -47.00454 | 2025-09-28 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| df1c6b12-3426-36ee-941b-3078da458073 | -9.29104 | -45.70973 | 2025-09-28 04:25:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5302f852-5174-3d92-9684-f54162d193cd | -11.94565 | -47.94088 | 2025-09-28 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 22208ed5-55cc-30d2-960e-8d2e433ca13f | -7.04023 | -44.77545 | 2025-09-28 04:25:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 87e084e5-aeb1-33e3-9b11-9f77b07493a6 | -8.82271 | -46.20755 | 2025-09-28 04:25:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 90e43eef-6a8c-3f28-99fb-a48c9ddd26f1 | -7.81277 | -47.01265 | 2025-09-28 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| b7f365be-88d3-324a-9857-1a8757cb05b2 | -10.99676 | -57.06182 | 2025-09-28 04:25:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 77b61d21-01be-318f-90f8-8dc3420c2304 | -12.02068 | -47.91681 | 2025-09-28 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5b392c3a-2948-3b05-8d2a-8dbdc102551f | -12.0068 | -47.93985 | 2025-09-28 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 58b95921-bab8-39af-a048-668bfa016f82 | -7.75822 | -45.74268 | 2025-09-28 04:25:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 791a322c-12df-34d7-9dad-95318bf630b7 | -11.35615 | -45.04585 | 2025-09-28 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6a42cd62-4ed2-341c-8a43-d6958dcd5974 | -11.43703 | -48.68891 | 2025-09-28 04:25:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 27875d27-f659-3b34-875d-23e7e93a61d3 | -7.09413 | -45.12582 | 2025-09-28 04:25:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 472e83a9-ad7c-3b44-bdfb-864407114b31 | -11.99002 | -47.87575 | 2025-09-28 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b5c9a58d-1942-3cbd-a76f-7be1be68d430 | -8.43337 | -46.86965 | 2025-09-28 04:25:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e0811bc9-d339-3fa6-a3af-e585f8e33d7a | -9.09404 | -48.1811 | 2025-09-28 04:25:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f8c93e43-4ecf-3885-9382-3170a8af9403 | -11.42099 | -44.92052 | 2025-09-28 04:25:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d9921afe-ac34-3697-b18b-542ca4972c99 | -11.65209 | -48.26708 | 2025-09-28 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e4c330da-e7d1-34e8-b996-5a463a579f7c | -8.82934 | -46.20859 | 2025-09-28 04:25:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1aa7c438-cf69-3c53-9719-772f6ba0aa84 | -12.78728 | -47.75303 | 2025-09-28 04:25:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 003b5d9b-b01b-3050-8b7c-8520b43a018a | -12.94482 | -45.11649 | 2025-09-28 04:25:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6eb7289e-dcaa-3585-9390-b96925701141 | -12.89277 | -45.17763 | 2025-09-28 04:25:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 14.5 |
| e5b36e02-0204-3f4f-913f-7292d5906f83 | -11.9457 | -47.91916 | 2025-09-28 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f649ddbd-fb66-31bd-98d4-e35d7abb7339 | -11.35612 | -44.9631 | 2025-09-28 04:25:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d5f37647-aeb9-3226-80b9-8f43bdb8e076 | -11.39549 | -46.92905 | 2025-09-28 04:25:00 | NOAA-20 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| e3d44b0c-9d69-32d5-914c-d610539acaf0 | -5.81714 | -44.44466 | 2025-09-28 04:25:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 881d5b7c-e43b-3304-b601-af50ce054361 | -7.8006 | -47.02501 | 2025-09-28 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 4a082542-30aa-3034-a314-c1e344961864 | -9.21661 | -46.76998 | 2025-09-28 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e150304f-3aee-3416-ad53-3260996fb3a3 | -10.90185 | -45.75883 | 2025-09-28 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| bfdc902f-626c-370b-b0a4-94bf0f27f8e6 | -7.18573 | -41.70565 | 2025-09-28 04:25:00 | NOAA-20 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a66dd9f8-2438-3dd5-bf41-1992d3e1dad2 | -6.25067 | -42.46975 | 2025-09-28 04:25:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 25195e22-36d0-39ee-bc75-a367fd6aa972 | -7.80779 | -47.02258 | 2025-09-28 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 52a5ed7b-83a9-3e42-9cde-d330083fcd9a | -11.57999 | -45.49156 | 2025-09-28 04:25:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 09bed71d-4bb6-3c22-847f-97e5f8586f38 | -11.37747 | -44.97382 | 2025-09-28 04:25:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 90617f04-d40c-3fc0-a5bc-02509a4c5581 | -11.98005 | -46.59421 | 2025-09-28 04:25:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9c5b4da5-efab-3c4a-ab16-86a047bbc0de | -6.25501 | -42.46612 | 2025-09-28 04:25:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 372c2deb-2b15-3ab1-a9b0-f488ed8f985f | -10.71628 | -48.00014 | 2025-09-28 04:25:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4e248153-bb29-312c-a24e-b66a048b076f | -11.70832 | -44.46895 | 2025-09-28 04:25:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8ef4977d-8f12-3804-978a-c7cfec4ff307 | -10.13603 | -45.3233 | 2025-09-28 04:25:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4de8b91e-daaf-3be5-8711-71ebff1628fc | -9.50684 | -54.66547 | 2025-09-28 04:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5b1b10d5-b62b-3f47-a4a0-34f9298d75c9 | -11.4481 | -45.00065 | 2025-09-28 04:25:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 46.5 |
| 6485967e-7508-3846-9621-e76c247a2ed7 | -7.87079 | -44.56865 | 2025-09-28 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4e0d2a53-1ba0-3bd9-b9e1-bc2028fe3c19 | -6.15558 | -42.80206 | 2025-09-28 04:25:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| e2c9a6f7-f642-3738-948f-985b6905ef8b | -11.51132 | -46.94763 | 2025-09-28 04:25:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7a7bfbea-3aac-3839-8ecd-8dc156401cf8 | -8.26941 | -45.46371 | 2025-09-28 04:25:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6ff0d6f3-d1ad-32c8-a8ea-3fc48211c72f | -5.91022 | -43.28876 | 2025-09-28 04:25:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 148cf430-e688-3122-92b9-4ce374d169cd | -11.62172 | -52.84786 | 2025-09-28 04:25:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| e29b9c91-161c-3547-a117-1edb94c907bd | -6.4212 | -43.07037 | 2025-09-28 04:25:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| ff6539f9-13d5-359c-bf73-de01f0165fd8 | -10.41194 | -46.13995 | 2025-09-28 04:25:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 64cb652c-0db8-382d-813b-396c3562aa1b | -12.68661 | -46.8782 | 2025-09-28 04:25:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 16f4188b-ff3b-3288-896e-533417c43072 | -8.4807 | -47.80943 | 2025-09-28 04:25:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9e8ca933-f365-38c6-a862-9464f6b0544e | -9.75117 | -47.76752 | 2025-09-28 04:25:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5cfa9b5d-56e1-3df1-aed8-6c0fb56a1c01 | -7.75325 | -47.00317 | 2025-09-28 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7ca9ff47-205a-34bc-a23c-ec28bf90b60f | -11.98612 | -48.00531 | 2025-09-28 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a42468c7-4378-33b8-a57b-39c3b0476fc9 | -5.89837 | -43.29511 | 2025-09-28 04:25:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 06cd9e2d-c36c-3899-8773-b2600b4583ba | -11.98556 | -48.00885 | 2025-09-28 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 12902671-34ec-3501-9ee9-0069b1996d97 | -6.47709 | -44.2503 | 2025-09-28 04:25:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4b200f89-d9c0-3522-ac01-4fc1833d775d | -6.0555 | -44.86411 | 2025-09-28 04:25:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| eaf7a41b-6e1d-35a7-9bf9-8e28ec59e87f | -10.90288 | -44.80935 | 2025-09-28 04:25:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 586fd743-ba7b-38f2-8f9c-2f82d9a54ffd | -6.42417 | -43.07508 | 2025-09-28 04:25:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| c6026242-c147-384e-8ab6-3db80ab442fb | -6.27619 | -44.07965 | 2025-09-28 04:25:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 873a3e1d-ed1f-3768-89e6-12f685a2f704 | -10.91509 | -44.79928 | 2025-09-28 04:25:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6a7b51b0-6a04-36e0-954a-6eac45d9a9a7 | -12.00511 | -47.95043 | 2025-09-28 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7982b470-38e9-305a-a314-f845e5ffb041 | -10.81996 | -45.3814 | 2025-09-28 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| eff6fad7-56d1-35f6-a5e6-2b5557bf6e92 | -7.37702 | -47.03959 | 2025-09-28 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4f42efea-9fcf-3be1-831a-0a6706643c81 | -8.82216 | -46.21105 | 2025-09-28 04:25:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cff20dea-781d-3ba5-a3b0-67fc55b3a2b4 | -6.36197 | -42.64986 | 2025-09-28 04:25:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 8fa89b12-2a1f-3eaa-b1f2-e8938f5151fb | -12.93596 | -45.15181 | 2025-09-28 04:25:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 59c84709-4414-38fc-b37f-aabc86eff395 | -10.41374 | -48.1519 | 2025-09-28 04:25:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c8073470-73eb-3408-af1a-f98123cc05f4 | -11.95717 | -47.97535 | 2025-09-28 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f17879b6-e920-3a63-aa93-006291687916 | -12.00436 | -47.09523 | 2025-09-28 04:25:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| ccd50230-165f-3d33-8651-e9f21a7566f3 | -6.06542 | -44.85847 | 2025-09-28 04:25:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| aea92d46-8b5c-375e-8499-02d45d3e6ab4 | -5.82165 | -44.43791 | 2025-09-28 04:25:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7e0399da-4ed5-3ac9-bd41-0b138a20ac57 | -11.99228 | -46.60346 | 2025-09-28 04:25:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4d7feefb-590f-3a56-97ac-e8ebc56d09f7 | -11.68943 | -44.39859 | 2025-09-28 04:25:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3616ff07-f367-3d3e-a9a9-009a2fa5dff9 | -7.10629 | -44.23657 | 2025-09-28 04:25:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 59a44aa5-c0a9-386c-8e51-caf115db60b4 | -7.87022 | -44.5724 | 2025-09-28 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5fa1dfd4-d04f-3ccb-bd27-3837a00ce478 | -8.49639 | -47.00755 | 2025-09-28 04:25:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 237b44ac-8323-33ca-a322-2eccc5063629 | -9.95972 | -43.59109 | 2025-09-28 04:25:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9337a1d2-63fb-3386-8807-2f5ae5c23a6b | -7.1771 | -41.70953 | 2025-09-28 04:25:00 | NOAA-20 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 164f3293-4839-3db1-a63b-41cc34c610cf | -11.4458 | -44.99234 | 2025-09-28 04:25:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 21.5 |
| 63d4314b-0bd1-3228-8ba8-80b297a9e0e4 | -11.44928 | -44.99282 | 2025-09-28 04:25:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 21.5 |
| 452d8fd7-007f-3352-b54f-a46ede139de0 | -11.58057 | -45.4878 | 2025-09-28 04:25:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 65c11582-2313-3c38-83ae-8697762d51f8 | -11.97467 | -46.58982 | 2025-09-28 04:25:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f853dd91-26ba-3816-bc2b-c552de27bbdd | -12.41412 | -44.10968 | 2025-09-28 04:25:00 | NOAA-20 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 686f6af9-e10d-344c-8d18-cd5b1690fbce | -6.03037 | -43.92276 | 2025-09-28 04:25:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6e2e8320-6c6f-372c-ac9e-a61e6704bd5c | -12.01062 | -47.95858 | 2025-09-28 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e0329f9f-8494-3e4e-93d4-c44b97855f69 | -8.47686 | -47.79054 | 2025-09-28 04:25:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 09f27b5f-61ff-3486-916d-e18e8f993267 | -6.76072 | -44.5949 | 2025-09-28 04:25:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8143e911-859e-3c63-b45e-63c52cf03c0b | -6.04074 | -43.92434 | 2025-09-28 04:25:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README66.md)
