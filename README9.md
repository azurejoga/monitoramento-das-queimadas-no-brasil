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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 35f6f7d6-7818-3d4a-b2d8-30a5bfe6f43e | -7.13866 | -47.28162 | 2025-06-16 04:53:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fb86c6ea-146b-345c-a07c-d23ad9cde9d5 | -7.64298 | -48.31137 | 2025-06-16 04:53:00 | NPP-375D | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 7b463824-7f76-3ebf-92a0-be34e9577cbd | -7.9311 | -47.80806 | 2025-06-16 04:53:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d16bfe90-ac50-3db5-bc7b-4177b68a93ec | -14.82917 | -48.4482 | 2025-06-16 04:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f4afba5a-1959-32a5-838a-710313401975 | -13.91735 | -54.62753 | 2025-06-16 04:55:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a7c448e4-dd05-37f3-84ee-47d774608f65 | -15.05672 | -49.47162 | 2025-06-16 04:55:00 | NPP-375D | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 251dd668-2bba-3181-a82e-55258316e62f | -13.92011 | -54.63164 | 2025-06-16 04:55:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 442edac6-ebfc-39b2-b19e-7e89ecadd9d8 | -16.29044 | -52.93856 | 2025-06-16 04:55:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c956db54-53eb-3841-927d-0208ddce1cc9 | -16.28758 | -52.9341 | 2025-06-16 04:55:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9abaf193-12a1-369c-a5ff-7cbd472174aa | -12.48682 | -58.47067 | 2025-06-16 04:55:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c794c1fc-6706-3596-ae12-a7fd241ed2be | -13.48698 | -47.86767 | 2025-06-16 04:55:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1a3f86b1-2054-3615-8309-41ce63f726c1 | -13.91346 | -54.63054 | 2025-06-16 04:55:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 00cbc26e-b543-3742-88cc-29463cf18ee3 | -13.92068 | -54.62807 | 2025-06-16 04:55:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2465e913-bc32-3397-a3b8-6ec11d49e457 | -15.40419 | -47.84626 | 2025-06-16 04:55:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| eb2ea332-830e-3dc3-abec-38b546c43a06 | -13.91678 | -54.63108 | 2025-06-16 04:55:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 53ee4f69-09fb-314e-98bb-98ce4bb3cf4d | -13.91459 | -54.62342 | 2025-06-16 04:55:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9531159d-1870-3ac4-a7ae-ee1a4358ec6a | -16.29388 | -52.93914 | 2025-06-16 04:55:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1bc1ebfb-8ebd-3e28-adc4-be36f77d851d | -16.29447 | -52.93522 | 2025-06-16 04:55:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d441f118-2719-37c1-aa7e-66d893392994 | -12.02424 | -57.09042 | 2025-06-16 04:55:00 | NPP-375D | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1cf0dc4e-35e2-384d-b95c-5edef1fc5f31 | -16.43752 | -54.84346 | 2025-06-16 04:55:00 | NPP-375D | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7e285235-eeda-392f-a013-bd67002a22ed | -13.91515 | -54.61986 | 2025-06-16 04:55:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fe318950-b2d3-3cab-83e0-0633203be099 | -14.65274 | -48.05347 | 2025-06-16 04:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| beb3ba7b-8a53-3787-9f6d-6045130260a0 | -12.02352 | -57.09467 | 2025-06-16 04:55:00 | NPP-375D | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a2fee282-5483-36a9-a287-a6535f7c0d11 | -14.74268 | -48.29293 | 2025-06-16 04:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 52d2b850-e7f6-353d-a491-99cf8551c8c9 | -15.05215 | -49.47474 | 2025-06-16 04:55:00 | NPP-375D | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4e9ae612-44d6-3c74-8550-2bba0a584a17 | -14.83303 | -48.45236 | 2025-06-16 04:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fede3e41-508b-3a88-a08b-27ba7486c51b | -15.05265 | -49.47107 | 2025-06-16 04:55:00 | NPP-375D | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0f96ca7f-91b3-3f4d-b135-3fb8a4b76e7c | -15.05622 | -49.47529 | 2025-06-16 04:55:00 | NPP-375D | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d0d05186-6bde-35c8-9610-8fe5ed4a3440 | -14.82436 | -48.41734 | 2025-06-16 04:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e50d471e-c9d5-389e-9317-f8d11017bb7d | -16.29103 | -52.93466 | 2025-06-16 04:55:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d80636ce-5ad4-3802-9ffb-37a8ce638979 | -19.0021 | -57.62459 | 2025-06-16 04:55:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.4 |
| a1dd52f8-791f-3311-8eed-325be29e04c9 | -14.02626 | -55.12926 | 2025-06-16 04:55:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 17a4ce0f-958e-33cc-9a92-f5473ccd7d26 | -11.98455 | -57.19273 | 2025-06-16 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 61ad93e8-94d1-38a1-89c8-9cece5b81ca8 | -14.68726 | -54.35561 | 2025-06-16 04:55:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9ff39b56-cdee-3848-8b5f-ddf62f348d64 | -12.49026 | -58.46938 | 2025-06-16 04:55:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6b6c94c2-626c-3f3d-a11c-dbd5a58f32c5 | -14.83745 | -48.4523 | 2025-06-16 04:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4614a3c9-82b2-343c-a871-ab35647aa848 | -12.52444 | -57.22732 | 2025-06-16 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f9a873bb-f0ca-3cee-8720-fce14a715aaa | -13.91183 | -54.6193 | 2025-06-16 04:55:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6fe72c4d-e277-3d93-bc98-1ed281d5b0bd | -12.02785 | -57.09103 | 2025-06-16 04:55:00 | NPP-375D | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c1b654b7-9ad8-39f9-b70e-a8e1a0f4a331 | -14.03018 | -55.12624 | 2025-06-16 04:55:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 426f99fa-0dc8-3a60-9cd4-d78db5f1bc89 | -14.82382 | -48.4215 | 2025-06-16 04:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| aeb988a4-2ae3-3170-b77f-12deb1206f61 | -13.74378 | -53.92797 | 2025-06-16 04:55:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| aa356bb0-0947-3c2e-9a4d-4125b2526e95 | -12.49155 | -58.46647 | 2025-06-16 04:55:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0a7d9964-a082-3046-973d-ea83d291e7f7 | -14.03468 | -55.11963 | 2025-06-16 04:55:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 00d4552b-20ea-3f66-9868-c90d4fb0154a | -15.07697 | -48.9446 | 2025-06-16 04:55:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f4c07fd5-6fb5-355f-b256-1d6247f08dca | -14.02684 | -55.12568 | 2025-06-16 04:55:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3bb6e7d5-d32a-3e6d-859d-6d07d98c26ae | -14.65226 | -48.05723 | 2025-06-16 04:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4409b4b2-17da-3c2b-9099-cd3b15692655 | -12.48639 | -58.46872 | 2025-06-16 04:55:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| be831b1d-4b95-32a0-a7f3-88ba18f54345 | -14.03076 | -55.12265 | 2025-06-16 04:55:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 84d6a067-03e8-3b2f-a675-0f27c3bccefa | -13.91792 | -54.62397 | 2025-06-16 04:55:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| aa0ceb13-4f81-3c8c-ba3e-df9aef340b7b | -12.52515 | -57.2231 | 2025-06-16 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e5d5ed30-2791-3a27-a3b6-92ef35b55d97 | -15.4036 | -47.85099 | 2025-06-16 04:55:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d4026b88-be9d-3ce4-8ded-14a462320021 | -14.03134 | -55.11907 | 2025-06-16 04:55:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 344de9df-4adc-35b9-ae3e-9492dca28523 | -14.83692 | -48.45634 | 2025-06-16 04:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f6cd16d3-de25-396a-a7ca-8b45936da189 | -13.29077 | -57.07384 | 2025-06-16 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 48824e6f-ef2e-3935-80f0-8a396833e0eb | -14.82861 | -48.45247 | 2025-06-16 04:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6f277b0b-c87a-34b9-b2c6-96451cf17dbd | -15.40761 | -47.89305 | 2025-06-16 04:55:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dcfcb879-aec2-3c73-901e-63cebf9988e5 | -13.91402 | -54.62698 | 2025-06-16 04:55:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6acc669f-dac1-3472-be0a-8e9023c1306a | -11.98382 | -57.19702 | 2025-06-16 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| efe53644-4e4d-3eb6-afec-1b1dbf2a0087 | -14.73833 | -48.29216 | 2025-06-16 04:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 44bf7566-efc0-35d2-9000-493d027ce4fc | -15.40307 | -47.89255 | 2025-06-16 04:55:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dfb26cf2-3a95-3acb-8569-36aaf21c977d | -13.9107 | -54.62642 | 2025-06-16 04:55:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| abeb12d6-fb8b-3fc6-aca0-c0734ab5fba0 | -20.47677 | -53.67496 | 2025-06-16 04:57:00 | NPP-375D | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| de6a920e-cf2a-3087-b854-c3a5c6f115ed | -22.53961 | -48.81341 | 2025-06-16 04:57:00 | NPP-375D | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d18aede2-c0a4-3f3b-a01a-a8d8db330a7e | -9.49954 | -57.13989 | 2025-06-16 05:16:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0e992a03-6707-3a56-b748-11602024f6af | -12.72784 | -46.27727 | 2025-06-16 05:16:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 6aac3227-29ac-3477-b083-6f556485717e | -11.88139 | -54.68225 | 2025-06-16 05:16:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9befe818-c672-39a3-a5ea-ae5cd13bf14e | -11.00884 | -55.07685 | 2025-06-16 05:16:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b8899e95-5c0f-3c90-826e-55a91aa4f93b | -12.71781 | -46.28053 | 2025-06-16 05:16:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4dc88a63-5c1a-3ec5-8f58-7c4ffbba1e86 | -12.22585 | -54.29894 | 2025-06-16 05:16:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 76ea343b-faa5-3dbc-96cb-6c709c13a61e | -10.99989 | -55.05399 | 2025-06-16 05:16:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 1adba0ef-4b80-3894-b4a4-b446d05c4a7a | -12.05264 | -48.07594 | 2025-06-16 05:16:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 15828fb1-002d-32d3-b62d-74400cb0fb20 | -10.78319 | -55.45255 | 2025-06-16 05:16:00 | NOAA-20 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 742665d7-e009-3425-ad24-df80ed29a010 | -12.52494 | -57.22279 | 2025-06-16 05:16:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b71a4728-f335-3274-83bb-da6e793248a6 | -7.64627 | -48.31252 | 2025-06-16 05:16:00 | NOAA-20 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 96dd67f8-25f2-30ec-a62e-5264a8fe1d41 | -12.09125 | -49.48991 | 2025-06-16 05:16:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 51d6836c-a922-3cee-b445-3a582372a378 | -7.92879 | -47.80915 | 2025-06-16 05:16:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7a6e0d52-c572-380c-a51d-d3a3adc2a5b3 | -11.13881 | -53.93901 | 2025-06-16 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 8033c378-0ee7-380c-bf8f-fff0da8aeda7 | -11.00786 | -55.05522 | 2025-06-16 05:16:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 20bbe1cf-78bf-3260-8408-829979b6bb55 | -8.7422 | -47.17219 | 2025-06-16 05:16:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 96a60886-42b3-32b0-9e10-e03f7e280736 | -9.45909 | -57.84595 | 2025-06-16 05:16:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b9a8498d-9f36-3ba3-a872-9588e2053f68 | -10.84984 | -53.78729 | 2025-06-16 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dc74162b-31ea-332b-bab0-5e783e53403f | -10.85041 | -53.78317 | 2025-06-16 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 30fc668d-e593-3883-b208-9bd6f5e50772 | -8.74827 | -47.17496 | 2025-06-16 05:16:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0d1cb228-0f7c-3de1-b3ea-2631227ae1a4 | -11.01035 | -55.06636 | 2025-06-16 05:16:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 5b7326c9-8275-3a90-9896-d79f07b44c63 | -10.5687 | -52.01584 | 2025-06-16 05:16:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 93c904c1-8c3b-34b4-b8aa-2230fc56858d | -12.05767 | -48.0765 | 2025-06-16 05:16:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8257ea94-8625-35ab-8876-99a0a9ede2fd | -12.08536 | -49.48919 | 2025-06-16 05:16:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9177651e-444f-3d59-8d51-5f51e351be2d | -11.00535 | -55.07279 | 2025-06-16 05:16:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9a4bd5a8-2276-33c2-b358-c8706c4140ee | -8.74233 | -47.16928 | 2025-06-16 05:16:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c26a3ab1-5393-3922-b1a8-295a8b209a65 | -10.09177 | -52.73645 | 2025-06-16 05:16:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| ba8eac3a-dd49-3083-a424-f598a19cc390 | -11.13733 | -53.91777 | 2025-06-16 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4b5cbfb7-2b19-3bd4-bd54-1634b02ec8b8 | -10.09638 | -52.73706 | 2025-06-16 05:16:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 0bd3ad7d-0777-32ea-a074-c5f80f35d134 | -8.74172 | -47.1743 | 2025-06-16 05:16:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2f36330e-540a-35c4-b64c-bf36fba89bf0 | -12.17435 | -54.23884 | 2025-06-16 05:16:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5223b3a3-f69a-3225-9939-7075a357497e | -10.09113 | -52.74119 | 2025-06-16 05:16:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 11.1 |
| cfe4b556-2ad6-3a5d-9304-dc0deb153a52 | -11.14368 | -53.93554 | 2025-06-16 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 19ced27f-607f-34c6-8f95-4c55121040fd | -12.02514 | -57.09027 | 2025-06-16 05:16:00 | NOAA-20 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 09aeece7-2f71-3310-bf0d-fbd84d5dde14 | -11.00636 | -55.06578 | 2025-06-16 05:16:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| f7bd28e2-1bc8-3507-9982-e278aa29de21 | -10.85213 | -53.77074 | 2025-06-16 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README10.md)
