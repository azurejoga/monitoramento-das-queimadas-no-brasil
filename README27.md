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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 527bbd19-c23f-3645-b78a-843cbe36d86a | -12.53552 | -58.36814 | 2024-12-11 05:22:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 3ca4cedb-ad5e-3e59-b613-367b6c8bdcf0 | -12.91595 | -55.0512 | 2024-12-11 05:22:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| eab16b3b-c749-3c4f-9ab3-449c6b6c6954 | -12.91985 | -55.05647 | 2024-12-11 05:22:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 27d34ca9-549e-38b0-8610-f6c5c8a157e7 | -12.57136 | -57.76553 | 2024-12-11 05:22:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 95e116a7-23a2-3636-946c-79dd786a301e | -12.5345 | -57.72669 | 2024-12-11 05:22:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 29187cc6-d827-3f02-8d64-36b42ca8c231 | -10.76958 | -58.84097 | 2024-12-11 05:22:00 | NOAA-20 | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d2ba00e6-d2a5-34f0-9d3e-099159e03368 | -12.56171 | -58.36763 | 2024-12-11 05:22:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e9be6813-fbe0-368f-8b00-82e0f1fba645 | -12.5471 | -58.3655 | 2024-12-11 05:22:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7b091401-018b-3a4c-b08e-c7811d2f073f | -11.36022 | -57.80701 | 2024-12-11 05:22:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5c94520e-1577-3fe0-af08-458a2cc3c55d | -12.71121 | -54.97551 | 2024-12-11 05:22:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 3615d375-deb5-3057-b56b-d3762c697224 | -12.70668 | -54.97487 | 2024-12-11 05:22:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 703b29ae-02db-336f-bd1b-dcf5a58ddb4a | -12.54005 | -57.74184 | 2024-12-11 05:22:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 311e99cc-8a43-3940-abe0-e7d1a3c11ae8 | -9.47929 | -61.86407 | 2024-12-11 05:22:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cfb3ad28-37ea-3d15-92d5-62597bd87008 | -12.24594 | -54.29422 | 2024-12-11 05:22:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 50105fce-fc10-355d-9d2b-66c2e0f2aca5 | -11.10128 | -54.62112 | 2024-12-11 05:22:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a841d622-8bee-31bd-8157-4ca0ac8538bc | -12.54407 | -58.36061 | 2024-12-11 05:22:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 8d7b5ede-7021-342b-9bbb-19bb34f75cc4 | -12.55567 | -58.35787 | 2024-12-11 05:22:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 045c0a22-9ade-3e04-97aa-1c3f6243c5b2 | -14.2865 | -57.46637 | 2024-12-11 05:22:00 | NOAA-20 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f9fbcc47-78e3-3a48-992b-9a0884f68656 | -12.53802 | -58.3508 | 2024-12-11 05:22:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 55e3e5fe-4ecf-3b9e-b5ce-6238502b3e73 | -12.53312 | -58.35892 | 2024-12-11 05:22:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 73711425-c1bd-3f4d-8c77-08171f2119ba | -12.92437 | -55.05706 | 2024-12-11 05:22:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ef50ed2c-556d-3f81-881c-0139ded9bc36 | -11.66145 | -58.27312 | 2024-12-11 05:22:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3d9f75ec-e806-3bc3-a873-cae9ac2e5dd4 | -9.87492 | -65.24538 | 2024-12-11 05:22:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 216d2e0d-175a-357c-af6b-065102be64de | -12.53627 | -57.74132 | 2024-12-11 05:22:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 7c16162f-455a-38c0-9b10-93accdc4a0ef | -11.72262 | -57.43966 | 2024-12-11 05:22:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3aa94807-7593-349f-8704-3ecff39a09f1 | -12.53614 | -58.36382 | 2024-12-11 05:22:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| d0c91609-a3d3-3421-967d-04d7036f5bac | -11.6657 | -58.26939 | 2024-12-11 05:22:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b0d4fa56-700c-3e12-8e02-547468aab39e | -12.55201 | -58.35733 | 2024-12-11 05:22:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 32019626-c675-32fd-98b8-3e47c64c74d9 | -12.92047 | -55.05185 | 2024-12-11 05:22:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| c89c3e8c-4ef1-3115-862c-e47d108671f4 | -12.53865 | -58.34644 | 2024-12-11 05:22:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 5ada11a6-65af-3fe4-9674-b676601a9158 | -12.53009 | -58.35401 | 2024-12-11 05:22:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1c1e43e7-2912-34c9-8ace-b305d9bfa3a0 | -10.69101 | -58.61768 | 2024-12-11 05:22:00 | NOAA-20 | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 69ac210c-7672-3585-9f51-ba1c6cdd6c59 | -12.54899 | -58.35244 | 2024-12-11 05:22:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 8.9 |
| a2d994c0-8364-33fe-ac68-652fafc9430e | -12.55933 | -58.3584 | 2024-12-11 05:22:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| eee51cb7-a6f3-3022-aa24-06e667306e5d | -12.53138 | -57.72144 | 2024-12-11 05:22:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fa0571c1-b962-3728-a921-6d225420b104 | -12.54835 | -58.35681 | 2024-12-11 05:22:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 5c7ab32d-cd14-3140-8bac-f16f12eab483 | -14.28256 | -57.46584 | 2024-12-11 05:22:00 | NOAA-20 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f8509733-791c-3a72-bab2-46b72d9a9790 | -12.55996 | -58.35401 | 2024-12-11 05:22:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 9a4dba8f-83f8-3f7a-bb12-8fc482d764e1 | -11.1124 | -54.64156 | 2024-12-11 05:22:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a3ed2d4f-bcf4-3459-b845-0164a13b8e2a | -12.53374 | -58.35458 | 2024-12-11 05:22:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 9fa80468-5dad-35ea-8ba1-455e8ce254db | -12.53693 | -57.73666 | 2024-12-11 05:22:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 63ebb82b-3f67-384e-95f0-b4d290e22b68 | -12.55631 | -58.35347 | 2024-12-11 05:22:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 267b3eb5-bee8-3706-bd4e-8a4bbc9fa3af | -14.28721 | -57.46119 | 2024-12-11 05:22:00 | NOAA-20 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dc720bf1-6f8a-36c3-8f0b-d397e6e72513 | -9.25902 | -63.26445 | 2024-12-11 05:22:00 | NOAA-20 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1886e3da-9c25-34f8-8aa3-aeb2c7f9f2ae | -12.5399 | -58.33776 | 2024-12-11 05:22:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 02d48545-5fb6-3e01-9556-52c83d85f3b1 | -12.53979 | -58.36438 | 2024-12-11 05:22:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 8ae8a623-951b-31fc-900c-0fe29f13048a | -9.05069 | -62.71468 | 2024-12-11 05:22:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6f38ab68-2c31-333a-ad18-07db52ee427a | -12.53928 | -58.3421 | 2024-12-11 05:22:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 706ce45f-2454-32bc-b840-6ad94b0838b0 | -10.13095 | -64.85299 | 2024-12-11 05:22:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2e9fc8ab-72f1-3262-800b-7e6d3902d20a | -11.36153 | -57.79811 | 2024-12-11 05:22:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c4fed62c-1fa9-3861-90a0-b0392f711ff6 | -12.53739 | -58.35516 | 2024-12-11 05:22:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 9.7 |
| b6a412b3-b526-3b76-9cd9-0afe2fe517d0 | -12.84651 | -59.03283 | 2024-12-11 05:22:00 | NOAA-20 | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bfdd712e-3060-33e3-82e1-fbb3ea98c00f | -12.55392 | -58.34421 | 2024-12-11 05:22:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8ec4d773-fc75-3deb-ba42-171b69402d27 | -12.53917 | -58.36871 | 2024-12-11 05:22:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 738fba5c-c8fe-36f4-ade8-9dc7b07ac54c | -9.37481 | -58.21303 | 2024-12-11 05:22:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8aaa1a5d-9a9b-3c05-a351-0f843099227a | -11.36524 | -57.79862 | 2024-12-11 05:22:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| eff1803f-2dd3-31e7-b1e9-a87c3874948b | -12.55025 | -58.3437 | 2024-12-11 05:22:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f02f9e73-1db1-35db-a7a0-caf25b96a797 | -12.54962 | -58.34807 | 2024-12-11 05:22:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 639ee5b7-4524-3ce3-b323-a85ace1892ac | -12.53761 | -57.73194 | 2024-12-11 05:22:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 072fa6d3-2b39-354d-922e-8d66ac31c1ac | -12.56362 | -58.35453 | 2024-12-11 05:22:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 39893641-280d-324d-9b6e-88b379499bc1 | -12.5599 | -57.71123 | 2024-12-11 05:22:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 54eeb52c-0275-38b3-8957-5debf9fee04b | -12.56312 | -57.76911 | 2024-12-11 05:22:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 9315c99e-d9b3-3ec7-b5c1-0a0e37dffd36 | -12.5447 | -58.35627 | 2024-12-11 05:22:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 7afdec7e-bc74-3552-b40f-1cc9ad14b03b | -15.01978 | -57.62518 | 2024-12-11 05:22:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b0dd34f6-7f16-38fc-9994-7573f4093245 | -9.3235 | -63.42538 | 2024-12-11 05:22:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f1aa8ecb-b4d3-30c0-b9b9-489b9a0bfb2c | -9.71564 | -54.89148 | 2024-12-11 05:22:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c8a23a83-adec-3411-a5f7-60e9a058b736 | -12.53896 | -57.72249 | 2024-12-11 05:22:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f58e02b7-fe96-37a5-bd70-61790106161c | -12.53677 | -58.35949 | 2024-12-11 05:22:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 39569d9b-4072-3da3-80b8-55461d9ee202 | -12.5568 | -57.70592 | 2024-12-11 05:22:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0b241ec5-1e29-35bd-9919-68a0b3e39159 | -12.54167 | -58.35136 | 2024-12-11 05:22:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 0eec9f10-4f30-3c3e-8d05-4f23af340a6d | -12.53829 | -57.72722 | 2024-12-11 05:22:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 078e45b7-bb6c-347e-a63d-c7525b1dd4eb | -12.54344 | -58.36495 | 2024-12-11 05:22:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 5bdf28fe-c1d3-39f1-ad72-819007faaad1 | -9.71505 | -54.89572 | 2024-12-11 05:22:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e9a9405f-bba6-3b3a-9b7a-a51a4fb74ccc | -12.535 | -58.34587 | 2024-12-11 05:22:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 262faa7d-1370-3231-a073-3005b3ace3c3 | -14.28328 | -57.46065 | 2024-12-11 05:22:00 | NOAA-20 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d701e164-49cc-350b-bfd8-3ba92c8f3576 | -12.53249 | -58.36325 | 2024-12-11 05:22:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 0be22840-e01b-38da-9543-3f873892161e | -12.55694 | -58.3491 | 2024-12-11 05:22:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| f5883f0f-bd8c-33d2-bf05-db961d6e2dea | -12.54042 | -58.36005 | 2024-12-11 05:22:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 7.9 |
| c5301f80-c18f-38d0-9acd-7662d7f3df95 | -12.56298 | -58.35892 | 2024-12-11 05:22:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 29e73378-b98b-3cca-a0a0-0995a90d03e1 | -9.72001 | -54.89205 | 2024-12-11 05:22:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1b7cce24-92d1-3d55-b76c-bf731775e297 | -12.81993 | -59.04123 | 2024-12-11 05:22:00 | NOAA-20 | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 18d1cf78-53a5-3334-9caa-aefccd73bad0 | -12.56234 | -58.3633 | 2024-12-11 05:22:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4546383e-7d80-317c-b95f-79ed31118537 | -12.54722 | -58.33883 | 2024-12-11 05:22:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 64ac52d6-4dea-3123-ae19-54be4846226c | -12.56752 | -57.76688 | 2024-12-11 05:22:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| a6e24995-a7b1-375d-97dd-f611a2ad8daa | -12.55075 | -58.36604 | 2024-12-11 05:22:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2c47f496-1c62-3ed0-8db1-19503b1e443b | -12.55743 | -58.37144 | 2024-12-11 05:22:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 87145b3b-2826-3db6-8569-db41077bdf2d | -12.53072 | -58.34965 | 2024-12-11 05:22:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d0444ca2-f1f4-3d25-a4cc-32a5b1155626 | -9.1374 | -62.72087 | 2024-12-11 05:22:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4ba629e0-9edc-39f7-98fb-f3962229da6e | -15.15576 | -56.47705 | 2024-12-11 05:22:00 | NOAA-20 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3e7fbffc-9b64-3eed-a7c7-c35c8df8cd13 | -12.8201 | -59.04218 | 2024-12-11 05:22:00 | NOAA-20 | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 438f8178-ce4d-3213-a253-8049cea033c5 | -11.78076 | -55.13198 | 2024-12-11 05:22:00 | NOAA-20 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a76e9af8-9af3-327c-8055-4264e788a16e | -9.37422 | -58.21706 | 2024-12-11 05:22:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7abc9eb6-e6e9-304b-8647-535bec27e6f8 | -12.53437 | -58.35023 | 2024-12-11 05:22:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 90f29bbf-d316-31b6-844e-781c86b37234 | -11.09676 | -54.62043 | 2024-12-11 05:22:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b9f30ad2-6db2-3f7a-9cde-e3c370ff98e8 | -12.54533 | -58.35191 | 2024-12-11 05:22:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f905c1b6-a6cf-39e5-8d7f-4d4f65129e81 | -15.02118 | -57.61485 | 2024-12-11 05:22:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| dbb80f6a-79cc-372c-bf08-e760f417d237 | -12.54772 | -58.36117 | 2024-12-11 05:22:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 11.3 |
| e29d4179-7c34-3d4c-bd17-5815b9c98e0b | -12.55328 | -58.34858 | 2024-12-11 05:22:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 8.9 |
| f23c37e4-c02c-3983-b99e-54848ce16bd1 | -12.56108 | -58.37198 | 2024-12-11 05:22:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 89506233-0093-3569-b9ac-38df9c6447b6 | -12.566 | -58.36382 | 2024-12-11 05:22:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README28.md)
