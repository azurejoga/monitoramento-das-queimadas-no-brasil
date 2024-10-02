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

## Dados Diários - Página 154

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b493ecb4-eb95-31cc-88b6-91af73a243c0 | -14.84573 | -58.61308 | 2024-10-02 05:12:00 | NPP-375D | RESERVA DO CABAÇAL | MATO GROSSO | Brasil | 5107156 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 964533ef-fdc4-36f8-b0b1-3d252a2894ed | -14.84517 | -58.61668 | 2024-10-02 05:12:00 | NPP-375D | RESERVA DO CABAÇAL | MATO GROSSO | Brasil | 5107156 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7c5b72fd-acd0-3807-9887-c8ccd8a7e3c1 | -14.84461 | -58.62028 | 2024-10-02 05:12:00 | NPP-375D | RESERVA DO CABAÇAL | MATO GROSSO | Brasil | 5107156 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 49714006-15ef-3f40-8d4f-02dd2809f6de | -14.8346 | -58.61866 | 2024-10-02 05:12:00 | NPP-375D | RESERVA DO CABAÇAL | MATO GROSSO | Brasil | 5107156 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4a2efdc6-638e-37a7-acf6-6b691494ac78 | -14.83405 | -58.62226 | 2024-10-02 05:12:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5888e59b-4e2e-3afe-bd9e-a94673a7b19e | -14.83182 | -58.61452 | 2024-10-02 05:12:00 | NPP-375D | RESERVA DO CABAÇAL | MATO GROSSO | Brasil | 5107156 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f4e1dd8e-d11a-34c5-9d1d-f2e44ea7d861 | -14.83126 | -58.61812 | 2024-10-02 05:12:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1076bb0d-7b05-31b2-9648-8b13ccfd4da0 | -14.8296 | -58.62891 | 2024-10-02 05:12:00 | NPP-375D | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cd6df718-87d5-3595-b816-8c270742e6e9 | -14.82903 | -58.61037 | 2024-10-02 05:12:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 987d08d7-7c7a-3578-941b-aa8c0c9d62d5 | -14.82848 | -58.61397 | 2024-10-02 05:12:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5a0ec227-0f6d-3118-aa5b-2ce2d3e8b820 | -14.82737 | -58.62117 | 2024-10-02 05:12:00 | NPP-375D | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3642f198-081c-35b4-8db4-04d562d2100f | -14.82626 | -58.62836 | 2024-10-02 05:12:00 | NPP-375D | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f876b6d4-0add-3472-b0d1-c632c3e3a161 | -14.82569 | -58.60983 | 2024-10-02 05:12:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e0f5b06e-38d9-3c1f-b4f8-ffcd2b162b73 | -14.82514 | -58.61343 | 2024-10-02 05:12:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 07aedf51-631e-3c55-88d3-fabc0c46ecd1 | -14.93962 | -59.1865 | 2024-10-02 05:12:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1dea1e91-2069-3a4a-a972-a56488e12d06 | -14.93629 | -59.18596 | 2024-10-02 05:12:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| db34ed87-66b4-3f48-9fd2-5cb6a637a682 | -14.89843 | -58.03404 | 2024-10-02 05:12:00 | NPP-375D | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ac45e4c6-d2ee-3370-a63b-99eba9fa8627 | -14.89562 | -58.02979 | 2024-10-02 05:12:00 | NPP-375D | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8dcff65a-2d3a-341a-b984-b6c952c49419 | -16.60957 | -58.22447 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| ac978afc-8912-397b-bcaa-32a080faee2a | -16.60673 | -58.22017 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 37.0 |
| 624306e6-cf3c-3fee-bc29-290eb48ed9bb | -16.60617 | -58.22393 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 37.0 |
| 55191e27-bb9b-3be4-821d-55129e473cf2 | -16.60561 | -58.22768 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 33.8 |
| 9687296d-f2b8-3882-80ac-2e338598f75a | -16.6039 | -58.21585 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| c335f7f5-c809-3039-877a-a0e866d83402 | -16.60334 | -58.21962 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 37.0 |
| 9ce6f470-0a82-3ff5-8067-2a2cab3626b0 | -16.60272 | -58.21949 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 122.1 |
| 92d324a8-8214-3db5-99ad-a1a6aec2c305 | -16.60222 | -58.22712 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 33.8 |
| d36401a6-e962-37a0-b9c5-ad844d2cf073 | -16.60167 | -58.23087 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 33.8 |
| b6152d67-f8e2-34bb-9eff-b0a2bbf8e4eb | -16.60158 | -58.22699 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 223.1 |
| 15b5d960-9ec6-3735-9d34-d63e5107008f | -16.60111 | -58.23462 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 7c54e7a9-f0b7-3467-a7af-eba94e358238 | -16.60101 | -58.23074 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 223.1 |
| e7cb8a20-12be-3634-b4d4-b6f19d69c683 | -16.59876 | -58.2227 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 122.1 |
| 89ccf0d3-b209-379e-b48b-3f54a8dc1b08 | -16.59651 | -58.21464 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 6fc63df4-13db-37db-b5ba-861957a467e6 | -16.59649 | -58.23766 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 6141f25d-a613-3994-a550-2bce1523368f | -16.59537 | -58.22215 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 42.4 |
| e84681ee-0168-31ec-8ce3-890a4dc408cb | -16.5948 | -58.22589 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 74.7 |
| 7936837f-0483-3d59-8e3c-c1df83d04b2d | -16.5931 | -58.23712 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 55.9 |
| 4bdaaa27-3c53-39b3-9d93-eacdd6307b96 | -16.59255 | -58.21785 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 42.4 |
| c02e0e76-48e4-3c2b-846e-971a75138764 | -16.59254 | -58.24084 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| a749c796-14fc-39ae-8489-e7effbb317e3 | -16.59141 | -58.22534 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 74.7 |
| fb5caa93-e912-3f42-87a9-92808cc9addc | -16.59084 | -58.22908 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 74.7 |
| e94be2c2-0b80-3035-b630-ac2dcaea4c22 | -16.58802 | -58.22479 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 18.1 |
| cdbd4258-02ce-3155-af2c-49d315d10e19 | -16.58689 | -58.23227 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 21.4 |
| e85c60d2-c8fd-325f-b5be-3857fd15bc22 | -16.58632 | -58.236 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 21.4 |
| 0cab200d-7904-30c5-811b-9a3e28fcc374 | -16.5852 | -58.22049 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.6 |
| cff3c56e-d18c-3e54-b3e3-b9f15f713a42 | -16.58181 | -58.24292 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.7 |
| 05880695-660e-30d9-bd19-d6cbc812c74c | -16.58125 | -58.22366 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 9954d6d9-b589-3bae-bcf9-8bda8c0d726d | -16.58068 | -58.22741 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| e9e8da2e-37b0-3358-aaaa-1c8b1441e276 | -16.57955 | -58.23489 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| a9300e1d-af28-3ba8-9e20-193fbee65fd6 | -16.57899 | -58.23863 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 8996a1b5-32e1-3b33-8c6b-6c42c5b61841 | -16.57729 | -58.22685 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 5c9a9476-c88d-3b43-8422-2812a5ac27ad | -16.57673 | -58.23059 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| c02b9691-7e1f-3a12-8470-f806c657766b | -16.57616 | -58.23434 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 66647edd-17e0-3f7a-bf9d-ab9279f129ea | -16.57503 | -58.24182 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 40ff7107-126e-3f51-870b-6042ded226f2 | -16.57334 | -58.23004 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 33dbf005-892f-3d98-b0e2-d6a751325a84 | -16.57221 | -58.23753 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 47abff04-2535-3695-b37b-0904169a5451 | -16.57164 | -58.24127 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| aaf0fb1f-78e2-32f2-875d-919b6b8264ce | -16.56939 | -58.23324 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| b08600b7-821f-3d51-b921-d43c0d0cc8ed | -16.56882 | -58.23698 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 0c3c73f1-b185-3a5b-b3be-a3fd24086883 | -16.56826 | -58.24072 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 5b18722a-c805-3b5d-a1dc-1351ded76b11 | -16.57785 | -58.24611 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 3d9a81f8-4008-3ed7-85f7-5a3b431d5497 | -16.57447 | -58.24556 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 4a6e7cfb-ba2d-34a5-b50c-384415a31638 | -16.5739 | -58.2493 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 9a2906bd-81fc-389b-b7c4-aece6000c632 | -16.57108 | -58.24501 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 93b7a894-7a10-3a61-8ef1-55f6b8158abe | -16.56769 | -58.24446 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 5b472d49-9742-3c20-b722-7fb3690648e6 | -16.56713 | -58.2482 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 0860920f-ca2a-3f42-864c-def86f31f68d | -16.55979 | -58.25084 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| bc805922-6882-3c85-90db-bd4529b3b2f4 | -16.1915 | -58.42892 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 4e05dbe2-d1a2-3b59-a203-688976d1827e | -16.19094 | -58.43262 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| eca8d90a-d0db-3930-a927-e83340113d87 | -16.18925 | -58.42102 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| a77b8e0b-4dcc-3ca0-baf5-2e33d84a1f4e | -16.18814 | -58.42838 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 84ba4391-94fa-325a-954d-9134520e7906 | -16.18757 | -58.43207 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| b2866fea-b09d-3300-a154-dc0eec5eb66b | -16.18477 | -58.42783 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 1cf84fce-149d-3d57-a652-072d0b6ae91e | -16.60729 | -58.21641 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 99da3473-a10b-3014-8f66-4dcf81e54460 | -16.60505 | -58.23143 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 33.8 |
| ab54c013-6b0a-31c4-81c3-fb6bffa4570b | -16.60329 | -58.21573 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 12.7 |
| fe0a33db-fae1-34b7-92a1-86d3fc4fbadc | -16.60044 | -58.23447 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 23676e98-d91f-360f-8c5c-81c7d6460b4c | -16.5999 | -58.21518 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 12.7 |
| e4d9b83f-fe4c-3d1e-b980-00a0068d1465 | -16.59933 | -58.21894 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 122.1 |
| 448d2292-4904-3f99-aa81-ae9d438da4f0 | -16.59762 | -58.23018 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 223.1 |
| d7048b4a-ae3b-3359-849e-c231d38fbe22 | -16.59705 | -58.23392 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 7222fbb9-d909-35ed-883c-243d52d9d7d8 | -16.59594 | -58.2184 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 42.4 |
| acc343cd-a44a-3084-80e5-b9eecf4f6509 | -16.59423 | -58.22964 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 74.7 |
| fe6e010d-d332-3fd6-ae30-3ab1bd56ec07 | -16.59367 | -58.23337 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 55.9 |
| 993a1cb3-c15c-38ed-963b-bfa6fbc90f43 | -16.59312 | -58.21408 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| ec7430c8-c4da-3f84-9388-601965bd8fb5 | -16.59198 | -58.22159 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 42.4 |
| 75bb3478-9594-36e0-aac4-de5f912fe20a | -16.59028 | -58.23282 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 55.9 |
| 0ae1f84c-6761-3a0e-9beb-ee9c39c8346b | -16.58971 | -58.23655 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 55.9 |
| 44408f46-444e-3cc2-a91c-cad6b831ec9e | -16.58916 | -58.2173 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.6 |
| cf5b41a4-c168-3fb8-a2a6-63c280d8b707 | -16.58915 | -58.24028 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 9b91836a-8c3e-3567-8fc5-3c9d344cd2ff | -16.58859 | -58.22104 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.6 |
| 04202973-68b2-3203-a5c4-457795c25593 | -16.58746 | -58.22853 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 18.1 |
| 244041d2-9036-3649-b7bf-0799290bff2f | -16.58576 | -58.23973 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.7 |
| ebc78f06-a44d-3427-83e4-f889faf4a958 | -16.5852 | -58.24347 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.7 |
| cfb52b09-a482-3c4f-9653-aeabb7c61f2d | -16.58463 | -58.22423 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 18.1 |
| 442e6d3c-bd79-3fd2-9c1b-b6499a9e5fb3 | -16.58407 | -58.22797 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 18.1 |
| 3ccbf1bc-a80c-32a9-9056-df41a5c4e6dd | -16.5835 | -58.23171 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 21.4 |
| 6e6d696e-836c-3c64-812e-4adabb09d2de | -16.58294 | -58.23544 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 21.4 |
| f48bbf1b-d2df-3d88-892e-c239831c34ba | -16.58237 | -58.23918 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.7 |
| 6e85f487-4a76-30d6-8f5a-ab8a9a3e04d2 | -16.58011 | -58.23115 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 91502e88-aff9-38cf-87ff-f2c565355f2d | -16.57842 | -58.24237 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |


[Clique aqui para ver as próximas entradas](README155.md)
