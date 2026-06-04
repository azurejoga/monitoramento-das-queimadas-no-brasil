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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fd59e14d-3ca5-3b96-af08-d6c263f9bc9a | -14.791 | -50.626999 | 2026-06-04 00:28:00 | METOP-B | MOZARLÂNDIA | GOIÁS | Brasil | 5214002 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| dd1ed2ec-1f17-3e8b-b2e1-feac8b598995 | -10.5719 | -57.3097 | 2026-06-04 00:28:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f7a91fcf-76d7-3538-bdd6-0a915239829b | -12.4494 | -58.450901 | 2026-06-04 00:28:00 | METOP-B | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 883c2bb3-e95d-3400-942a-089dbb26ab14 | -12.5533 | -48.343601 | 2026-06-04 00:28:00 | METOP-B | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a54eb9fa-9b6a-34ee-8c00-12619411d62a | -14.1419 | -58.945599 | 2026-06-04 00:28:00 | METOP-B | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a6016032-fd55-3477-a4cf-7c7189a45512 | -16.182199 | -58.4366 | 2026-06-04 00:28:00 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b89400fa-fdbf-39ff-800c-c3e441c21fee | -12.2164 | -57.256699 | 2026-06-04 00:28:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5d6e3cf0-fe23-3064-a04e-03352a348e2b | -11.6249 | -55.174301 | 2026-06-04 00:28:00 | METOP-B | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bc217ea8-8fdf-316b-a997-749c690eac27 | -14.0942 | -59.3801 | 2026-06-04 00:28:00 | METOP-B | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 04d87c2e-1e04-3d3a-b86f-ff2a1a6c61b3 | -11.5434 | -52.780102 | 2026-06-04 00:28:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9d12a77d-465b-3a73-95df-6b3f0501e59f | -10.5502 | -46.604301 | 2026-06-04 00:28:00 | METOP-B | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 33d708de-6d63-306a-8e48-c14d0f007bda | -16.1849 | -58.450699 | 2026-06-04 00:28:00 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 01d504b8-7e0e-3e7c-bda4-3103f4363220 | -9.5256 | -47.740601 | 2026-06-04 00:28:00 | METOP-B | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 317816fa-0b0c-35c0-8ee4-c8cc9641d603 | -23.0968 | -49.8708 | 2026-06-04 00:28:00 | METOP-B | JACAREZINHO | PARANÁ | Brasil | 4111803 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| faca4e47-67fb-3b2b-b990-74a14e009160 | -18.465799 | -54.692101 | 2026-06-04 00:28:00 | METOP-B | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| ba030081-82ae-3d41-9d47-2a8a80a9e964 | -17.4622 | -55.187 | 2026-06-04 00:28:00 | METOP-B | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 2c11af4e-8bd1-35bc-900c-27bdc4420329 | -12.2206 | -57.277302 | 2026-06-04 00:28:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b15a33f5-d55b-3a87-859c-82ede606f4ab | -14.4414 | -48.8932 | 2026-06-04 00:28:00 | METOP-B | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| a68e3272-0812-3a71-89b9-8af72da5a36a | -12.736 | -54.182701 | 2026-06-04 00:28:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a19c6561-20b2-3ec1-9bd2-c4db572f8a80 | -12.2185 | -57.266998 | 2026-06-04 00:28:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 24be5085-eb27-3d76-8d7e-a01a3181f4bd | -11.8822 | -57.8153 | 2026-06-04 00:28:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 119604d7-c2ed-3e79-b1ad-393eeb199d80 | -12.2241 | -57.244301 | 2026-06-04 00:28:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 089dacac-2503-3a26-8789-73b3a4bc5f57 | -14.7708 | -52.663601 | 2026-06-04 00:28:00 | METOP-B | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 537ba605-f1a2-30c4-99fa-fa55fb349238 | -12.236 | -57.252602 | 2026-06-04 00:28:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6a513769-cdaf-35ee-8ac7-a951eba6e1df | -16.129 | -58.476398 | 2026-06-04 00:28:00 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 6d3d9c1b-5105-31a3-8bf1-3357149ab398 | -14.0635 | -53.383701 | 2026-06-04 00:28:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| cc72d5dd-c9ba-3bc6-b1a0-33d5abc6b8e3 | -10.3825 | -49.428299 | 2026-06-04 00:28:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a6864a3f-1141-31e4-9711-906d389930dc | -11.8919 | -57.813202 | 2026-06-04 00:28:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3cf92f8a-a5c6-3595-9115-fb87f657e4fc | -12.4714 | -58.459202 | 2026-06-04 00:28:00 | METOP-B | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6673d4c4-dd61-3519-b6fb-68514abd1e38 | -14.4433 | -48.901501 | 2026-06-04 00:28:00 | METOP-B | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 1bf99724-6523-36eb-8dbd-1defb37c261e | -12.312 | -47.898399 | 2026-06-04 00:28:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 42bd7188-ed87-3b7e-a565-ab1835f5eeac | -12.437 | -58.3894 | 2026-06-04 00:28:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9a48137c-874a-3ba4-ad7b-db55e4822caa | -12.4592 | -58.448898 | 2026-06-04 00:28:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 65c529ce-2af7-34e0-ad17-a4133954d203 | -16.194599 | -58.448799 | 2026-06-04 00:28:00 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d1635f1b-140f-3e24-969d-97abfd64ad98 | -12.2108 | -57.279301 | 2026-06-04 00:28:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b27a4443-217e-3fb6-b85f-3832d410c412 | -14.0884 | -59.349998 | 2026-06-04 00:28:00 | METOP-B | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9ff95ebc-8d24-3a8e-b669-7bb997d0f4aa | -11.545 | -52.786999 | 2026-06-04 00:28:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8a25826b-8a59-36e1-88a6-495ea64694f5 | -14.0847 | -53.386501 | 2026-06-04 00:28:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9aff8f8e-d239-346c-a985-8f091c0ef760 | -12.3097 | -47.8885 | 2026-06-04 00:28:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 45e40844-2a26-3190-bc96-c2a26f729729 | -11.5419 | -52.773102 | 2026-06-04 00:28:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 26e4d496-1d08-39ed-a60e-1df8c4fae932 | -10.6376 | -49.722801 | 2026-06-04 00:28:00 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 118ac228-7fc2-331b-ac77-1549dd3fa480 | -13.5116 | -54.303699 | 2026-06-04 00:28:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cbf01ba5-cc70-3ef7-bae0-d68f85f3f43c | -14.167 | -58.9701 | 2026-06-04 00:28:00 | METOP-B | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5a5692fc-59c4-328d-a11c-242f1a03694c | -19.736601 | -53.540001 | 2026-06-04 00:28:00 | METOP-B | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 061d3473-1df5-3151-b9ba-d006ec822e8f | -11.5532 | -52.777802 | 2026-06-04 00:28:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d48d5823-d7ee-315a-9357-d1e8573c5973 | -11.1644 | -49.239899 | 2026-06-04 00:28:00 | METOP-B | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 910b2046-9229-39dc-a53b-8ee9c470ed91 | -17.4603 | -55.1777 | 2026-06-04 00:28:00 | METOP-B | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c072e929-636a-3b3b-9a64-67ef0da8a96d | -10.3943 | -49.434502 | 2026-06-04 00:28:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 345fcaf5-8d7b-3901-9ee9-a7debb6af47d | -21.502701 | -48.769001 | 2026-06-04 00:28:00 | METOP-B | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| c7a56bc0-5828-349d-9c9a-ab8f66f31eb7 | -12.2143 | -57.246399 | 2026-06-04 00:28:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 380e98dc-ae96-391e-ab5a-441c3aebfef6 | -12.4395 | -58.401699 | 2026-06-04 00:28:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9954b061-d309-3905-9c67-10ffee6eb2db | -21.551201 | -49.8675 | 2026-06-04 00:28:00 | METOP-B | PROMISSÃO | SÃO PAULO | Brasil | 3541604 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1ed917b7-301d-3e41-bdfe-b6a4a9962da1 | -10.3842 | -49.4338 | 2026-06-04 00:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 0f20c1ae-0d82-3498-b1e4-6c6a0d7129a8 | -11.5688 | -52.7848 | 2026-06-04 00:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 81.8 |
| b630fabc-962b-3cb8-a998-9c584a1066db | -12.4464 | -58.4825 | 2026-06-04 00:30:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 45.9 |
| 41940d78-96d2-3d84-9667-c83549e6ca28 | -12.2325 | -57.2872 | 2026-06-04 00:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 247.4 |
| 27e9f962-f7db-3f47-98fc-4b154a26aa61 | -11.5499 | -52.7867 | 2026-06-04 00:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 256.1 |
| 91b59682-de58-3ea2-ba70-b3931f1c838f | -12.2138 | -57.2688 | 2026-06-04 00:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 325.5 |
| f3c473cc-27ed-327d-97eb-8590abae7302 | -14.0919 | -59.3777 | 2026-06-04 00:30:00 | GOES-19 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 40.5 |
| d633f6a2-94a5-39c7-90b1-2c28f70adafa | -12.4656 | -58.4612 | 2026-06-04 00:30:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 9b68ac40-34d6-3bc5-b7a7-24d26e262d0d | -11.5309 | -52.7887 | 2026-06-04 00:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 88.3 |
| 8bc552ab-1c9a-333e-ac29-0da6c0383665 | -12.2327 | -57.2672 | 2026-06-04 00:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 399.1 |
| ca67629d-bea5-3c06-91a8-95287709176f | -12.1946 | -57.2904 | 2026-06-04 00:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 4db7e3cf-d770-3a6e-b63b-82aff43a7e92 | -12.2136 | -57.2888 | 2026-06-04 00:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 293.7 |
| 1c938df0-f15f-3029-8057-6d80755a1430 | -11.5496 | -52.8076 | 2026-06-04 00:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 62.8 |
| f2f4fff3-2fa2-3a98-9f2b-c8440950fc50 | -10.3839 | -49.4554 | 2026-06-04 00:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 85.6 |
| a0b56b24-c677-368b-9d77-1d1fb540dac9 | -12.4654 | -58.481 | 2026-06-04 00:30:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 3abf2eb6-9f88-3ace-9dac-3dfd2aaa89c6 | -12.4656 | -58.4612 | 2026-06-04 00:40:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 75.7 |
| bba3e28b-52f2-3474-9f3c-a5e8b48ae8e5 | -12.4464 | -58.4825 | 2026-06-04 00:40:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 48.2 |
| bd6cf89b-231c-3093-a0ec-a3dc62f6308f | -11.5499 | -52.7867 | 2026-06-04 00:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 200.1 |
| 94b9fa64-1b54-34a8-8a14-82da7225b7a9 | -11.5502 | -52.7659 | 2026-06-04 00:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 241503ef-fad4-3efe-a7ed-91a87010ffef | -10.3842 | -49.4338 | 2026-06-04 00:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 91d45b05-9431-36fb-8f0c-e1f8cc27d3b7 | -14.0919 | -59.3777 | 2026-06-04 00:40:00 | GOES-19 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 38.8 |
| 694249d5-06d6-3c04-973c-f7627ee0e8df | -11.5309 | -52.7887 | 2026-06-04 00:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 93.1 |
| d43a1aae-cdb8-343a-a406-60d7e2bed793 | -10.3839 | -49.4554 | 2026-06-04 00:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 75.7 |
| a19dc3a3-015b-37e2-a323-e0f88dcc2edd | -11.5688 | -52.7848 | 2026-06-04 00:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 934eae12-823f-3e44-a2f6-ca3d0cae1449 | -12.4466 | -58.4627 | 2026-06-04 00:40:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 48.2 |
| 959f3281-8938-351e-9503-8a2f5c8ef1ad | -12.4654 | -58.481 | 2026-06-04 00:40:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 84.8 |
| c93fcd6d-7188-3a22-93b1-5dbd7c0deeae | -3.9867 | -47.9326 | 2026-06-04 00:50:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 61.5 |
| de185af4-e747-35c2-8bea-cc3083e6379e | -14.0919 | -59.3777 | 2026-06-04 00:50:00 | GOES-19 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 39.6 |
| 7d1d1067-09e1-32bd-8218-c9936538679d | -10.3839 | -49.4554 | 2026-06-04 00:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 9a9621fa-d99d-3e9e-a287-55d890c37755 | -10.4029 | -49.4534 | 2026-06-04 00:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 63.4 |
| 4f2baedc-835d-36cc-9f6a-e36d5f4c9ecd | -11.5688 | -52.7848 | 2026-06-04 00:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 4163a143-69df-3891-92dd-16c0d77ddc9d | -11.5496 | -52.8076 | 2026-06-04 00:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 3a9acc43-f302-3a36-bf4e-0a5ca830d887 | -11.5309 | -52.7887 | 2026-06-04 00:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 75.6 |
| 0400c7ab-098e-3f2a-b28f-423bcb602b68 | -11.5499 | -52.7867 | 2026-06-04 00:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 197.6 |
| 23d6b6e4-3e16-3ea0-9716-99acef656c08 | -12.4656 | -58.4612 | 2026-06-04 00:50:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 94.7 |
| c6d10d2b-7f36-3385-9176-96fb324d1631 | -12.4654 | -58.481 | 2026-06-04 00:50:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 86.6 |
| bfe0b2fd-a1a3-3e18-a5a6-cbfade2d5349 | -11.5309 | -52.7887 | 2026-06-04 01:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 2340b2e2-7714-3732-be6e-3b8fc997dc68 | -11.5688 | -52.7848 | 2026-06-04 01:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 35f0903d-804f-3675-9768-fe03efc62525 | -10.4029 | -49.4534 | 2026-06-04 01:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 56.6 |
| a54925c7-03a1-3829-972e-8b9f33b17217 | -12.2327 | -57.2672 | 2026-06-04 01:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 685.0 |
| a0961b7f-4a8d-33ac-abef-369674412f0a | -12.4654 | -58.481 | 2026-06-04 01:00:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 95.9 |
| 4682eab1-f71d-32e2-82d6-e3cfea557d80 | -11.5499 | -52.7867 | 2026-06-04 01:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 197.4 |
| a65f8833-7609-3495-91e3-3c9b9137ce36 | -12.2136 | -57.2888 | 2026-06-04 01:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 584.3 |
| aca03c6f-fce6-3cd0-b73c-be8a5224c0dd | -12.2325 | -57.2872 | 2026-06-04 01:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 342.3 |
| 15b7d4c6-09f5-3b72-9843-42f5fa0ba13b | -10.3839 | -49.4554 | 2026-06-04 01:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 53255fee-bdcd-3670-ad45-c8ed75c0bd01 | -12.233 | -57.2472 | 2026-06-04 01:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 55.5 |
| d3d3a568-e09b-3592-8df7-64a254b6e521 | -12.4656 | -58.4612 | 2026-06-04 01:00:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 9dac3d20-37c6-31df-9720-8395a2112bd4 | -12.2138 | -57.2688 | 2026-06-04 01:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 842.2 |


[Clique aqui para ver as próximas entradas](README3.md)
