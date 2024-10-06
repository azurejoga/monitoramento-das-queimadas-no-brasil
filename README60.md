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
| 1f341db5-8577-308f-bca3-5e834dc4de17 | -20.68285 | -47.5316 | 2024-10-06 03:57:00 | NPP-375D | RESTINGA | SÃO PAULO | Brasil | 3542701 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5d665054-430d-3fc8-afcc-ec6d7b380420 | -20.51659 | -47.4906 | 2024-10-06 03:57:00 | NPP-375D | FRANCA | SÃO PAULO | Brasil | 3516200 | 35 | 33 | nan | nan | nan | Cerrado | 32.4 |
| 353d68a4-a931-35ed-8eef-9bc20f172f67 | -20.51581 | -47.49463 | 2024-10-06 03:57:00 | NPP-375D | FRANCA | SÃO PAULO | Brasil | 3516200 | 35 | 33 | nan | nan | nan | Cerrado | 32.4 |
| b1297229-87ce-3754-94aa-03c496bd4b05 | -20.51243 | -47.48965 | 2024-10-06 03:57:00 | NPP-375D | FRANCA | SÃO PAULO | Brasil | 3516200 | 35 | 33 | nan | nan | nan | Cerrado | 22.6 |
| fbc3a081-e4ef-3311-ab1c-6d08430d7e76 | -19.96388 | -46.82541 | 2024-10-06 03:57:00 | NPP-375D | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 65a55203-675e-346b-842d-53f3f2c6d3ce | -19.96323 | -46.82895 | 2024-10-06 03:57:00 | NPP-375D | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0e5d769d-413c-303a-9477-0978b7b32c83 | -19.96303 | -46.82426 | 2024-10-06 03:57:00 | NPP-375D | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1dfd4d50-beba-3aa7-a62b-edc21c1a3e2e | -19.96236 | -46.82779 | 2024-10-06 03:57:00 | NPP-375D | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f89d617f-c320-315e-bd10-6ac7d1453d13 | -19.95826 | -46.8272 | 2024-10-06 03:57:00 | NPP-375D | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e7719999-d6b6-3d60-8979-4845a53f3afc | -21.8516 | -48.44759 | 2024-10-06 03:57:00 | NPP-375D | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 04172bd3-ebce-3ae1-a3d6-2f68f857d333 | -21.8507 | -48.4521 | 2024-10-06 03:57:00 | NPP-375D | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1bdd6237-2516-3216-9370-876a6d94bb11 | -21.85027 | -48.36427 | 2024-10-06 03:57:00 | NPP-375D | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 98d19774-998f-32ad-abd1-6b14892b2237 | -21.84603 | -48.36299 | 2024-10-06 03:57:00 | NPP-375D | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7812afc4-f6dd-3b7a-867a-1f13eff6eb3a | -21.84583 | -48.3598 | 2024-10-06 03:57:00 | NPP-375D | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4f39e87b-8429-3f67-90eb-bc2892a3fdd8 | -21.59021 | -47.94656 | 2024-10-06 03:57:00 | NPP-375D | GUATAPARÁ | SÃO PAULO | Brasil | 3518859 | 35 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4349e81c-43c3-3d1e-9dab-bd202961dd55 | -21.58979 | -47.94501 | 2024-10-06 03:57:00 | NPP-375D | GUATAPARÁ | SÃO PAULO | Brasil | 3518859 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4a3c8b73-88ca-3a0f-bfad-8f06a4218701 | -21.58896 | -47.94917 | 2024-10-06 03:57:00 | NPP-375D | GUATAPARÁ | SÃO PAULO | Brasil | 3518859 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 21943ebb-21c7-3ceb-8dd4-c31192201ac8 | -21.58601 | -47.9456 | 2024-10-06 03:57:00 | NPP-375D | GUATAPARÁ | SÃO PAULO | Brasil | 3518859 | 35 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 88732555-4a68-30f7-a234-e94fa7f493db | -21.49511 | -47.30147 | 2024-10-06 03:57:00 | NPP-375D | SANTA ROSA DE VITERBO | SÃO PAULO | Brasil | 3547601 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2afe4b4f-fa94-3b5f-ae05-77725bb4fd7a | -21.31635 | -47.606 | 2024-10-06 03:57:00 | NPP-375D | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a68ed902-32b7-3c61-8587-3d7bd5d9416a | -21.31551 | -47.61041 | 2024-10-06 03:57:00 | NPP-375D | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 20cf68b4-9d05-3d1f-9156-d177c5ce9124 | -21.31227 | -47.60474 | 2024-10-06 03:57:00 | NPP-375D | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 60c6cbb4-b001-3f8f-bf1b-a49de4f9dff3 | -21.31142 | -47.60921 | 2024-10-06 03:57:00 | NPP-375D | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 943794d5-3f5a-3b77-be93-7711d9f74104 | -22.83111 | -47.49146 | 2024-10-06 03:57:00 | NPP-375D | SANTA BÁRBARA D'OESTE | SÃO PAULO | Brasil | 3545803 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 18527a81-4a0a-3898-af8b-9317536cf57c | -22.83039 | -47.49526 | 2024-10-06 03:57:00 | NPP-375D | SANTA BÁRBARA D'OESTE | SÃO PAULO | Brasil | 3545803 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| d396b27a-4ad6-36e9-bd1a-0a5e25a6d030 | -22.82855 | -47.48302 | 2024-10-06 03:57:00 | NPP-375D | SANTA BÁRBARA D'OESTE | SÃO PAULO | Brasil | 3545803 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 70695ffb-0ff1-3576-9f3f-23761c7d0b36 | -22.82783 | -47.48679 | 2024-10-06 03:57:00 | NPP-375D | SANTA BÁRBARA D'OESTE | SÃO PAULO | Brasil | 3545803 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 4d4d3f4c-b0f7-3bfe-aaf4-3fa8153e46d6 | -22.8271 | -47.49059 | 2024-10-06 03:57:00 | NPP-375D | SANTA BÁRBARA D'OESTE | SÃO PAULO | Brasil | 3545803 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 263732b3-edaa-3d48-a958-71c9e9cb06b5 | -22.82637 | -47.49442 | 2024-10-06 03:57:00 | NPP-375D | SANTA BÁRBARA D'OESTE | SÃO PAULO | Brasil | 3545803 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 515d3f6d-b6a6-36f7-ac18-74c7b693bf6e | -22.82308 | -47.48975 | 2024-10-06 03:57:00 | NPP-375D | SANTA BÁRBARA D'OESTE | SÃO PAULO | Brasil | 3545803 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| bcf922c1-92ea-370d-9416-39f60d40046e | -18.07802 | -47.97684 | 2024-10-06 03:57:00 | NPP-375D | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ca9392b1-21fd-37fc-a1eb-873831a31276 | -17.61656 | -48.77808 | 2024-10-06 03:57:00 | NPP-375D | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 71e29070-d93f-3f85-8806-ac79875a09d9 | -17.61494 | -48.77879 | 2024-10-06 03:57:00 | NPP-375D | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d50591b6-2587-3dbf-a26f-38d0817527e8 | -19.13996 | -48.29033 | 2024-10-06 03:57:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 31213110-95b0-3f85-907c-8cb7c948323f | -19.12598 | -48.29445 | 2024-10-06 03:57:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0b328b9f-f7a9-3844-95fc-222abcae3cfa | -19.08747 | -48.19944 | 2024-10-06 03:57:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 957550f0-97f9-3770-b52a-0a045a650575 | -20.78922 | -48.59602 | 2024-10-06 03:57:00 | NPP-375D | COLINA | SÃO PAULO | Brasil | 3512001 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4cabc989-d36a-33ad-84ab-ca1d0965f25e | -20.78568 | -48.59043 | 2024-10-06 03:57:00 | NPP-375D | COLINA | SÃO PAULO | Brasil | 3512001 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3c403ead-4702-3161-99a3-6f945a9ac868 | -20.78477 | -48.59508 | 2024-10-06 03:57:00 | NPP-375D | COLINA | SÃO PAULO | Brasil | 3512001 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2f0c35cb-0b29-3b40-b38b-35df107a192f | -20.58914 | -49.37825 | 2024-10-06 03:57:00 | NPP-375D | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 40.4 |
| a4736ae3-4da9-3d79-b7b9-28af909b245a | -20.58804 | -49.38359 | 2024-10-06 03:57:00 | NPP-375D | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 40.4 |
| a768e237-7aa6-3d9a-b3bb-b4062062768a | -20.58556 | -49.37176 | 2024-10-06 03:57:00 | NPP-375D | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 9.5 |
| cf9a2bca-c576-39ce-8904-5346a972ce31 | -20.58446 | -49.37714 | 2024-10-06 03:57:00 | NPP-375D | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 40.4 |
| 2bc66f01-cb02-3bc2-8390-771f9d86f348 | -20.58337 | -49.38244 | 2024-10-06 03:57:00 | NPP-375D | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 40.4 |
| 8b7bc506-6155-39e9-9beb-d26b45501ae9 | -20.58229 | -49.38768 | 2024-10-06 03:57:00 | NPP-375D | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 7596c938-ebe1-3e57-bbef-c588bcfe34d2 | -20.5812 | -49.393 | 2024-10-06 03:57:00 | NPP-375D | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 63.6 |
| d78f68b5-f650-3de0-9a43-dd40cec157b9 | -20.58011 | -49.3983 | 2024-10-06 03:57:00 | NPP-375D | IPIGUÁ | SÃO PAULO | Brasil | 3521150 | 35 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a44b1040-c19b-3b10-9836-7e75a627ab4e | -20.57977 | -49.37603 | 2024-10-06 03:57:00 | NPP-375D | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 9.7 |
| b25e7099-6723-333b-a7f2-863dd3808b19 | -20.57869 | -49.38129 | 2024-10-06 03:57:00 | NPP-375D | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 4091dad8-afad-33c4-b1d1-e796e458a34c | -20.57763 | -49.38649 | 2024-10-06 03:57:00 | NPP-375D | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 147.1 |
| 77efc4a4-3070-3867-9952-1dfad919d863 | -20.57652 | -49.39184 | 2024-10-06 03:57:00 | NPP-375D | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 147.1 |
| b84f6a3e-e391-37bb-9479-ba60d09f6f1d | -20.57542 | -49.39722 | 2024-10-06 03:57:00 | NPP-375D | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 230.1 |
| df3db981-0231-3611-9f99-8654f74d133c | -20.57511 | -49.37486 | 2024-10-06 03:57:00 | NPP-375D | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 97d5960e-559c-3aa1-ac4c-a6a48aace994 | -20.57433 | -49.40251 | 2024-10-06 03:57:00 | NPP-375D | IPIGUÁ | SÃO PAULO | Brasil | 3521150 | 35 | 33 | nan | nan | nan | Cerrado | 230.1 |
| 8e947b91-3a21-3921-a2a2-883238c52ff9 | -20.57403 | -49.3801 | 2024-10-06 03:57:00 | NPP-375D | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 59f375c3-d294-3050-9d67-3e99bded13e3 | -20.57324 | -49.40782 | 2024-10-06 03:57:00 | NPP-375D | IPIGUÁ | SÃO PAULO | Brasil | 3521150 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 293ac619-b8b2-3db8-9bd0-8da270f65040 | -20.57295 | -49.38533 | 2024-10-06 03:57:00 | NPP-375D | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 147.1 |
| 5a19091c-773a-3171-a188-e6c81c5d17ff | -20.57074 | -49.39609 | 2024-10-06 03:57:00 | NPP-375D | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 230.1 |
| c4c4feb2-0d5f-38a0-9ee2-b6e587e9fff3 | -20.56964 | -49.40142 | 2024-10-06 03:57:00 | NPP-375D | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 230.1 |
| 4951d399-f178-33ba-8b81-c7d06001941f | -20.56936 | -49.37892 | 2024-10-06 03:57:00 | NPP-375D | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 942be3e5-82c9-35f3-833d-fcecdd4c0425 | -20.56854 | -49.40673 | 2024-10-06 03:57:00 | NPP-375D | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a286a47a-e4d7-3b90-9271-99feae6023c4 | -20.56745 | -49.41206 | 2024-10-06 03:57:00 | NPP-375D | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 04655345-03d2-392b-91c9-671e7436bf0e | -20.56716 | -49.38957 | 2024-10-06 03:57:00 | NPP-375D | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 122.6 |
| b23a9ef5-4cc2-322f-8382-ff2063d81bce | -20.56606 | -49.3949 | 2024-10-06 03:57:00 | NPP-375D | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 142.8 |
| 0452c762-0215-303d-90be-93cc57dd96a5 | -20.56497 | -49.4002 | 2024-10-06 03:57:00 | NPP-375D | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 142.8 |
| a080347f-5169-3e99-93d1-598ac882f674 | -20.56387 | -49.40553 | 2024-10-06 03:57:00 | NPP-375D | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 48ff048a-6092-3cde-85e4-54ad63d25ae7 | -20.56357 | -49.38317 | 2024-10-06 03:57:00 | NPP-375D | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 122.6 |
| 74283688-4494-3214-9076-1749f4617db9 | -20.56247 | -49.38851 | 2024-10-06 03:57:00 | NPP-375D | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 122.6 |
| c3f34dfd-d25c-3b5e-a696-bf38d509d986 | -20.56139 | -49.39373 | 2024-10-06 03:57:00 | NPP-375D | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 142.8 |
| d752c37c-4b55-39fc-8bb5-5e66dfb7ffb0 | -20.5603 | -49.399 | 2024-10-06 03:57:00 | NPP-375D | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 142.8 |
| ab0d850c-c169-3451-b89e-bd7ad2e86a11 | -20.55889 | -49.38202 | 2024-10-06 03:57:00 | NPP-375D | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5e0dddf2-6bce-39b6-896b-84234169e460 | -20.55779 | -49.38732 | 2024-10-06 03:57:00 | NPP-375D | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ef8dca11-529a-3225-b495-374603a9ad74 | -20.55672 | -49.39254 | 2024-10-06 03:57:00 | NPP-375D | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1238c433-a2f4-3dab-ad34-b403af77b6bc | -21.59277 | -48.60715 | 2024-10-06 03:57:00 | NPP-375D | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b01f10fb-2aad-345b-825b-0ff434356388 | -21.59187 | -48.6116 | 2024-10-06 03:57:00 | NPP-375D | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 766fac75-5795-3cd8-ae0d-226d772ebf2b | -21.29637 | -48.80463 | 2024-10-06 03:57:00 | NPP-375D | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| fc43177e-0c7e-3f92-85fc-8a6a6044ec5b | -21.29544 | -48.80934 | 2024-10-06 03:57:00 | NPP-375D | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| c18e9f8d-c779-36ae-9b58-0c642cecd535 | -21.16396 | -48.87523 | 2024-10-06 03:57:00 | NPP-375D | PINDORAMA | SÃO PAULO | Brasil | 3538105 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 46b9eb22-f80f-3b79-a272-05ef15fcfc31 | -21.16299 | -48.8801 | 2024-10-06 03:57:00 | NPP-375D | PINDORAMA | SÃO PAULO | Brasil | 3538105 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| b75ecea0-801c-310b-892c-e9e41e44314b | -21.15949 | -48.8741 | 2024-10-06 03:57:00 | NPP-375D | PINDORAMA | SÃO PAULO | Brasil | 3538105 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 9c0ea47b-2648-30c8-9564-951a82bf29a1 | -21.15852 | -48.87894 | 2024-10-06 03:57:00 | NPP-375D | PINDORAMA | SÃO PAULO | Brasil | 3538105 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 6f45f03d-167a-3160-87a8-74ef092764dd | -23.72445 | -50.05622 | 2024-10-06 03:57:00 | NPP-375D | JABOTI | PARANÁ | Brasil | 4111704 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 2740c3e8-6c4a-3e33-a168-7a0f661a9093 | -17.30702 | -49.3233 | 2024-10-06 03:57:00 | NPP-375D | CROMÍNIA | GOIÁS | Brasil | 5206503 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 34a47bf6-fb74-3a74-9a51-88507f73e2f0 | -21.52689 | -50.90197 | 2024-10-06 03:57:00 | NPP-375D | SALMOURÃO | SÃO PAULO | Brasil | 3545100 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| fcc060c9-4348-3a73-a348-2420f5542233 | -21.52622 | -50.90506 | 2024-10-06 03:57:00 | NPP-375D | SALMOURÃO | SÃO PAULO | Brasil | 3545100 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 377e30a2-44c1-393c-9b68-c00abda249e3 | -21.52489 | -50.90149 | 2024-10-06 03:57:00 | NPP-375D | SALMOURÃO | SÃO PAULO | Brasil | 3545100 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| f62c840e-547d-3bb2-ae8f-3cb7409633cd | -21.52424 | -50.9046 | 2024-10-06 03:57:00 | NPP-375D | SALMOURÃO | SÃO PAULO | Brasil | 3545100 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 80f3cf0b-0665-3d64-869a-8109f44ef21f | -21.52359 | -50.9077 | 2024-10-06 03:57:00 | NPP-375D | SALMOURÃO | SÃO PAULO | Brasil | 3545100 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 2244c800-5508-3037-9b8f-3f9d77510010 | -21.51851 | -50.90656 | 2024-10-06 03:57:00 | NPP-375D | LUCÉLIA | SÃO PAULO | Brasil | 3527405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| e8ec33ff-78b1-3828-856d-68fb6e665646 | -21.51784 | -50.9097 | 2024-10-06 03:57:00 | NPP-375D | LUCÉLIA | SÃO PAULO | Brasil | 3527405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| f8130ac5-963f-3703-a227-9437af53441e | -21.51342 | -50.90546 | 2024-10-06 03:57:00 | NPP-375D | LUCÉLIA | SÃO PAULO | Brasil | 3527405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 2505b389-032c-33c6-ae45-1ea3c6238ea3 | -21.51275 | -50.90862 | 2024-10-06 03:57:00 | NPP-375D | LUCÉLIA | SÃO PAULO | Brasil | 3527405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| f18769f0-0a02-3d76-b851-51b7c40e9711 | -21.51208 | -50.91175 | 2024-10-06 03:57:00 | NPP-375D | LUCÉLIA | SÃO PAULO | Brasil | 3527405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| 98936a78-dc49-30f3-9382-42f287f35116 | -21.51142 | -50.9149 | 2024-10-06 03:57:00 | NPP-375D | LUCÉLIA | SÃO PAULO | Brasil | 3527405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| 0e7cc8c9-e932-3f80-848f-a7a60d324782 | -21.51075 | -50.91805 | 2024-10-06 03:57:00 | NPP-375D | LUCÉLIA | SÃO PAULO | Brasil | 3527405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| 4836e9a2-8e9e-3401-a0fb-964a23f3c88c | -21.50767 | -50.90748 | 2024-10-06 03:57:00 | NPP-375D | LUCÉLIA | SÃO PAULO | Brasil | 3527405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 9689ef03-3e8d-3688-bcd9-e3676c524d6b | -21.50634 | -50.91374 | 2024-10-06 03:57:00 | NPP-375D | LUCÉLIA | SÃO PAULO | Brasil | 3527405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 00166971-4370-3836-a788-400807d34212 | -21.50567 | -50.9169 | 2024-10-06 03:57:00 | NPP-375D | LUCÉLIA | SÃO PAULO | Brasil | 3527405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 9e2e1e89-27f6-3bfc-9bf8-fb5f8275eb33 | -22.60859 | -53.04622 | 2024-10-06 03:57:00 | NPP-375D | ROSANA | SÃO PAULO | Brasil | 3544251 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| cc9845f8-f078-3099-b653-90f2b4271e44 | -22.60394 | -53.04056 | 2024-10-06 03:57:00 | NPP-375D | ROSANA | SÃO PAULO | Brasil | 3544251 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |


[Clique aqui para ver as próximas entradas](README61.md)
