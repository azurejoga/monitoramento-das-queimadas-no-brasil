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

## Dados Diários - Página 122

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9ae25579-68d5-311c-b560-58446c0be0da | -18.8534 | -54.48383 | 2024-10-02 04:51:00 | NOAA-21 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6529f90a-0a3e-329a-b23c-4bd9a055e4f5 | -18.85281 | -54.48749 | 2024-10-02 04:51:00 | NOAA-21 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 61beaf0a-96bc-318d-a082-497524ddbb9c | -20.77406 | -54.84105 | 2024-10-02 04:51:00 | NOAA-21 | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9090975f-44ba-3bb3-b93f-6d000180476c | -20.77076 | -54.84043 | 2024-10-02 04:51:00 | NOAA-21 | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 567a1d47-3406-31fb-a952-fb328ccf650a | -20.76768 | -54.81712 | 2024-10-02 04:51:00 | NOAA-21 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cce3ac98-da71-33ba-a3a1-a82669645619 | -20.76379 | -54.82021 | 2024-10-02 04:51:00 | NOAA-21 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f7157624-1a91-357b-b50c-b864d8810fd2 | -19.99663 | -55.47383 | 2024-10-02 04:51:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3eef322c-adee-3988-9ae5-15e6ce1c1126 | -19.99602 | -55.47754 | 2024-10-02 04:51:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 55f7fa30-75f3-375e-b45a-3fc3cf09878b | -19.99451 | -55.46578 | 2024-10-02 04:51:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 171a45ed-a7a5-371e-8fc3-7d9ab3324232 | -19.98854 | -55.46836 | 2024-10-02 04:51:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d66aee2c-7754-35a4-9be7-915a86296127 | -19.98731 | -55.47586 | 2024-10-02 04:51:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9bd0597c-4886-383e-9238-ec1bd627b4eb | -19.98458 | -55.4715 | 2024-10-02 04:51:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 142d9fb6-e341-3b3d-9ae9-7421ff659454 | -19.98397 | -55.47524 | 2024-10-02 04:51:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 0594ba92-b0b9-3647-aa18-f53e9c593d8d | -19.98336 | -55.47897 | 2024-10-02 04:51:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 35e3f0cb-0778-35bd-aa00-2716a9b08a23 | -19.98062 | -55.47462 | 2024-10-02 04:51:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 795c40f1-695c-3024-a166-1be4d8fbfb1b | -19.98001 | -55.47834 | 2024-10-02 04:51:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 5.3 |
| b8411aa7-3879-39dd-9920-558d8bc82927 | -19.97666 | -55.47775 | 2024-10-02 04:51:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f7545d37-3f7b-3cd6-867e-aad1882ff929 | -19.97606 | -55.48147 | 2024-10-02 04:51:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c4393241-31dd-3fc5-be88-04fa7ff73135 | -19.96935 | -55.48032 | 2024-10-02 04:51:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 22145840-a6b4-3e70-8bea-252a9a3da0e9 | -19.96874 | -55.48404 | 2024-10-02 04:51:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 03c722cb-b2be-399c-9d97-2af33e9eb844 | -19.96538 | -55.48348 | 2024-10-02 04:51:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6dc8a85d-40f7-37d1-b549-fdea67d23623 | -19.96477 | -55.48724 | 2024-10-02 04:51:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 438c78c0-66a1-38ea-8b4c-4c76a7475528 | -19.96414 | -55.49108 | 2024-10-02 04:51:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0d97c7e1-edd2-30ef-9e30-6bd37933569f | -19.96351 | -55.49492 | 2024-10-02 04:51:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2dace116-11b9-3367-bdc9-e25ab05187ae | -19.74962 | -54.5202 | 2024-10-02 04:51:00 | NOAA-21 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 84c6c5db-a16a-3614-82fd-b84a92d34600 | -22.16742 | -56.03751 | 2024-10-02 04:51:00 | NOAA-21 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 74290d30-3028-381f-897a-9404ab91697b | -21.89249 | -56.10919 | 2024-10-02 04:51:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 16ff9d3b-8f35-36c3-b3d4-47b001aef8d0 | -21.88913 | -56.10855 | 2024-10-02 04:51:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0e300878-f2ca-3d90-b9e5-df8f54aecd13 | -21.359 | -55.69003 | 2024-10-02 04:51:00 | NOAA-21 | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 24.6 |
| a84a8678-cada-3fea-b6b3-fbf9aa223af9 | -21.35628 | -55.68562 | 2024-10-02 04:51:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 24.6 |
| 6be1b38e-a6b7-39c6-bd35-b0f41713c50b | -21.35567 | -55.68939 | 2024-10-02 04:51:00 | NOAA-21 | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 24.6 |
| 6bf0e44f-376d-3918-951d-128bb56fe1b3 | -21.35505 | -55.69318 | 2024-10-02 04:51:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 29.9 |
| be04eb13-bef8-3df0-8e09-5caab97af49f | -21.35295 | -55.68499 | 2024-10-02 04:51:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 32.9 |
| f830f47e-d12f-3232-8200-ca8c0591d277 | -21.35233 | -55.68875 | 2024-10-02 04:51:00 | NOAA-21 | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 32.9 |
| 9b230135-b771-32e2-8f68-3436dd061206 | -21.35171 | -55.69254 | 2024-10-02 04:51:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 0160f25e-101d-3a85-bb38-2e6d775b428e | -21.349 | -55.68811 | 2024-10-02 04:51:00 | NOAA-21 | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 32.9 |
| 242a66f7-48e9-3f57-ac45-2d2af3e6a6ca | -21.34838 | -55.69189 | 2024-10-02 04:51:00 | NOAA-21 | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 19.2 |
| c66ff269-426b-36ef-bded-5ed529d298ae | -21.34714 | -55.69948 | 2024-10-02 04:51:00 | NOAA-21 | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7a64f110-3202-3ecb-a7e8-015297224d41 | -21.34504 | -55.69127 | 2024-10-02 04:51:00 | NOAA-21 | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f86080ab-c610-308f-aca7-52fec9bbccfe | -21.34442 | -55.69506 | 2024-10-02 04:51:00 | NOAA-21 | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f315ac68-f5a2-3c59-b983-9ad3513baa26 | -21.3438 | -55.69886 | 2024-10-02 04:51:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9473123c-917f-3302-b97a-79f4e745ff62 | -17.22451 | -56.18211 | 2024-10-02 04:51:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| f22faa69-536e-36f5-93fc-5aefbeb85e1a | -17.22446 | -56.16114 | 2024-10-02 04:51:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 84cfab12-0b71-354e-a1d2-65c107dca43d | -17.16575 | -56.20915 | 2024-10-02 04:51:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| a1add414-2310-3734-aaa5-f96d144fc596 | -17.16295 | -56.20443 | 2024-10-02 04:51:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 0826cdf7-7a49-36c6-92c7-c6b9fd63c4bb | -17.16225 | -56.2085 | 2024-10-02 04:51:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 460d1f64-e813-3386-8e56-0d403424e8d6 | -17.15946 | -56.1618 | 2024-10-02 04:51:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.2 |
| be408169-41fb-361a-8d94-dacf03d4ada5 | -17.15945 | -56.20378 | 2024-10-02 04:51:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 9e90b46d-9a58-350e-b62d-785d01687ae0 | -17.15945 | -56.18278 | 2024-10-02 04:51:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 7ec77bdb-8927-3472-94ac-cdb0467fc6f6 | -17.15876 | -56.16586 | 2024-10-02 04:51:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.6 |
| a7a479af-cc2f-37dd-aaf9-bfa536696570 | -17.15874 | -56.20786 | 2024-10-02 04:51:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 3ac20f89-d56d-3dfa-816d-8db203607111 | -17.15806 | -56.16993 | 2024-10-02 04:51:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.6 |
| 0712b249-6ad0-3108-a7d6-36bba77695f7 | -17.15806 | -56.14898 | 2024-10-02 04:51:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| ac937e15-77fb-38ab-99d0-f2ec91865ad9 | -17.15736 | -56.17399 | 2024-10-02 04:51:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| 612361c1-0db9-3eee-95d7-4af438564b3c | -17.15666 | -56.17806 | 2024-10-02 04:51:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| 8f9734b7-bde7-37c0-b2d5-98046a74f33f | -17.15596 | -56.16116 | 2024-10-02 04:51:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.2 |
| ae6c0a05-e513-3c5f-a202-00cf8e33f452 | -17.15595 | -56.18213 | 2024-10-02 04:51:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 307755bd-61e1-3ed7-b0cf-6429f61e26aa | -17.15594 | -56.20314 | 2024-10-02 04:51:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| df8f8e70-4d5c-3074-b5ac-e56839bf2e41 | -17.15526 | -56.16522 | 2024-10-02 04:51:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.6 |
| bc4f7298-adcd-33ba-9f57-59904b6b40e2 | -17.15525 | -56.18621 | 2024-10-02 04:51:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| c442e659-7afd-3ecd-b81b-838bda3efff7 | -17.15524 | -56.20723 | 2024-10-02 04:51:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 729eab41-35cf-383a-ad76-10ba8d09e8d7 | -17.15456 | -56.16928 | 2024-10-02 04:51:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.6 |
| c9f99cc4-e35c-32c8-8bc4-02b1b1242b00 | -17.15386 | -56.17335 | 2024-10-02 04:51:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| 460cde70-d918-373a-8633-428f580d643e | -17.15316 | -56.17742 | 2024-10-02 04:51:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| 358d9d3a-0f3f-33de-9048-ab6920357b57 | -17.15246 | -56.18149 | 2024-10-02 04:51:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 09f105e9-7472-386e-a3c1-3723f45cbe56 | -17.15244 | -56.2025 | 2024-10-02 04:51:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| ba799472-ae89-3984-9f8b-0f5cc3b7692d | -17.15175 | -56.18556 | 2024-10-02 04:51:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 11b646b7-41e5-3d88-9b6f-5ba60c801697 | -17.15174 | -56.20658 | 2024-10-02 04:51:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| c263f6ca-c32f-3bec-9c77-fe6687f10ce1 | -17.15106 | -56.16865 | 2024-10-02 04:51:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 1509f3ce-f99f-3b17-ae6f-af2836b825b8 | -17.15036 | -56.17272 | 2024-10-02 04:51:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.9 |
| 071c8e08-0aa1-3b2c-8e51-d41bffad1b1b | -17.14966 | -56.17679 | 2024-10-02 04:51:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.9 |
| b39913ac-666a-3ea4-a418-c39c0cab6df8 | -17.14939 | -56.17292 | 2024-10-02 04:51:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 7.1 |
| 60ac9361-297e-36d0-bb11-5204a854f8e7 | -17.14895 | -56.18085 | 2024-10-02 04:51:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| f8d51330-bacd-38b2-980e-b7dbd651a9ee | -17.14894 | -56.20187 | 2024-10-02 04:51:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 349a9754-f0a0-3735-aa77-f32e3ba05fa1 | -17.14823 | -56.20595 | 2024-10-02 04:51:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| ba2a1212-ef89-32cf-bc04-22e466fd5e90 | -17.14034 | -56.18384 | 2024-10-02 04:51:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 6c083b7b-3b7e-3e78-87c9-fcdc9d70d729 | -17.13966 | -56.18791 | 2024-10-02 04:51:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| a112754a-5467-3308-afdf-8deefda645d2 | -17.13615 | -56.18727 | 2024-10-02 04:51:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| e22d0f99-2a93-3ac0-bc0d-42da22f32156 | -17.13547 | -56.19135 | 2024-10-02 04:51:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| dbb7acef-b2fd-3e0e-9514-397ab624281e | -17.13478 | -56.19543 | 2024-10-02 04:51:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 45ffba1c-63f3-3cf4-99ec-c52f53e304ed | -17.13334 | -56.18256 | 2024-10-02 04:51:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 7c756c7b-622b-35d1-919f-ef721e4cb105 | -17.13265 | -56.18662 | 2024-10-02 04:51:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 193c066c-2510-3796-9c4b-fefcaf4b58f0 | -17.11736 | -56.23438 | 2024-10-02 04:51:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| ebd5e765-923b-32f6-aced-5749aec932b0 | -17.11666 | -56.23848 | 2024-10-02 04:51:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 2005c289-f3c2-3c3d-a86a-80a538c146aa | -17.11597 | -56.24258 | 2024-10-02 04:51:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 2680d5f7-e65a-3a19-9584-49ff3ecee416 | -17.11454 | -56.22964 | 2024-10-02 04:51:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 81fca586-f86d-3007-b3c7-91e771dfeaa1 | -17.22382 | -56.18618 | 2024-10-02 04:51:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| fe7d1987-f472-3217-9d69-afe0fa7ced10 | -17.22377 | -56.1652 | 2024-10-02 04:51:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| a43b99d4-b273-39d9-993c-54e009e27da4 | -17.22313 | -56.19025 | 2024-10-02 04:51:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 6c6b3e93-a3d0-34c4-a533-6bee05f83ade | -17.22239 | -56.17333 | 2024-10-02 04:51:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| f9269237-ef47-3726-8891-f9520b3014eb | -17.21963 | -56.18961 | 2024-10-02 04:51:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 553d1632-5d0d-3d7d-8078-8b0259e6fd43 | -17.2182 | -56.17676 | 2024-10-02 04:51:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 168bcd46-1324-3ef8-96ba-92948ffc2492 | -17.21259 | -56.16735 | 2024-10-02 04:51:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 7e8e0e40-674f-3c22-8c6b-ccb23b6883f9 | -17.21117 | -56.15453 | 2024-10-02 04:51:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 9ea858ba-1870-318b-aedc-f05fc6f987a2 | -17.21056 | -56.20053 | 2024-10-02 04:51:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| b16b51a2-3d3e-3dd3-a244-84751b4d209e | -17.21048 | -56.15859 | 2024-10-02 04:51:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.8 |
| fb18f294-f354-31b7-a21f-aaa02348b9e9 | -17.21043 | -56.13768 | 2024-10-02 04:51:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 91a4e6d1-e411-34c3-9314-f68b5bd9d1e6 | -17.20979 | -56.16265 | 2024-10-02 04:51:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 0cf2b2ae-df3c-309c-84e9-7b11e33c9657 | -17.20845 | -56.19175 | 2024-10-02 04:51:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 6511f81d-9a70-3898-bdd5-37312f4f846c | -17.20775 | -56.19582 | 2024-10-02 04:51:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |


[Clique aqui para ver as próximas entradas](README123.md)
