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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bbfec463-3b54-3e24-89fb-4e9e9e65a395 | -2.24909 | -51.91847 | 2025-10-20 05:01:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 2b884ec5-fd44-3622-a26f-cf7e8e9a828c | 2.04243 | -55.7189 | 2025-10-20 05:01:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 30c955e4-33e3-3154-b9c5-52ca1f5ec351 | 1.07803 | -51.30395 | 2025-10-20 05:01:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 60424bf2-d951-3f16-bf64-a0440a6f3184 | -2.24971 | -51.91446 | 2025-10-20 05:01:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 0db9ab83-0717-30f9-9c6b-c339a9a1ee04 | -2.81618 | -54.37764 | 2025-10-20 05:01:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 863a3dc0-827b-3c8e-a776-dcf355771c2b | -3.14666 | -49.51966 | 2025-10-20 05:01:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| aacad74a-d3db-325a-8413-099d89de0747 | 1.00386 | -51.13106 | 2025-10-20 05:01:00 | NOAA-21 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4db266be-3302-38b2-a6a9-5aa30e7d065f | -3.01536 | -52.35781 | 2025-10-20 05:01:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 2b4272e0-8635-31af-890f-85543c3c854e | 2.04188 | -55.76043 | 2025-10-20 05:01:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 27328ec4-0f13-37f3-90af-633716002836 | 1.77023 | -55.71143 | 2025-10-20 05:01:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 52ea8bc4-204f-3087-8a0f-a8de957a28d2 | -2.6566 | -49.37489 | 2025-10-20 05:01:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 72602ad5-3fde-3a8a-9390-eed3b2ad0385 | -3.42575 | -49.48249 | 2025-10-20 05:01:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e5b3240b-f2fa-3e83-a60f-ff4e13864a32 | 1.79971 | -55.69226 | 2025-10-20 05:01:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e4ecec1c-41db-37b2-88a4-8ab53f095bed | 1.78047 | -55.70269 | 2025-10-20 05:01:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3ef8f865-23f9-306b-8e67-39b8994cdff2 | 1.43252 | -50.73706 | 2025-10-20 05:01:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 85cce3fa-6b4f-35c4-a359-78cac2a9120b | 1.74617 | -55.91482 | 2025-10-20 05:01:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| e7728dcb-25f9-3d84-a410-e008c60a218e | 1.82008 | -55.66678 | 2025-10-20 05:01:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 4e38cc2e-24ae-3dc2-a01f-47a8f5280bf0 | -2.15592 | -51.95856 | 2025-10-20 05:01:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cf6af16e-8555-3c4b-9f31-857dbd708a4b | -3.43537 | -51.61499 | 2025-10-20 05:01:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 45859405-37d2-3122-8570-cf4e2dde9941 | 1.88768 | -55.78773 | 2025-10-20 05:01:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 89637f35-8fab-3e75-867d-3a87f2c65449 | -2.91189 | -52.71617 | 2025-10-20 05:01:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 47115721-1434-36b8-bba2-233ce91bd9de | 1.76402 | -55.71615 | 2025-10-20 05:01:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| afee9862-5068-3258-82df-8bc9c9f768e9 | -1.44644 | -49.29902 | 2025-10-20 05:01:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| bede18a3-5f98-304a-a83e-2426a5b3372f | 1.84664 | -55.65895 | 2025-10-20 05:01:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e54a72f1-da27-367f-8ca4-abb10644ebf3 | 1.74217 | -55.91162 | 2025-10-20 05:01:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f7a28dc6-88fe-3c07-aa4f-89f90eea822f | -2.86959 | -50.73602 | 2025-10-20 05:01:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dacde065-5a49-3d1f-b5fb-7211bd4abc2e | -2.91474 | -52.72053 | 2025-10-20 05:01:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d616e27c-4368-347f-ace9-4d87439fc4fd | 0.97735 | -51.14769 | 2025-10-20 05:01:00 | NOAA-21 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d4c9debd-f61b-30c2-b04f-50f8df6f4089 | 1.71826 | -55.98379 | 2025-10-20 05:01:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 72e8da4d-db95-3f9b-bcff-ece88f738598 | -2.15553 | -56.65439 | 2025-10-20 05:01:00 | NOAA-21 | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 19dc3dff-444a-3421-a947-c65a969a74ad | -1.09447 | -54.13648 | 2025-10-20 05:01:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 86100f21-d24c-3f8a-8ef7-bd101eea3a64 | 1.70629 | -55.76996 | 2025-10-20 05:01:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7f889a89-f476-3535-81e5-5079f9295d9c | 1.76684 | -55.71196 | 2025-10-20 05:01:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ae906eec-f598-3fe1-87cb-cfadf005c9a7 | 1.75723 | -55.71719 | 2025-10-20 05:01:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2fd15905-0dbd-32ac-973e-b78e7fc8ad5d | -2.87032 | -50.7313 | 2025-10-20 05:01:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eb6a17d8-4433-3505-a22e-9ec2407a0682 | 0.99676 | -51.13221 | 2025-10-20 05:01:00 | NOAA-21 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1c7caf95-690e-3424-85b8-911a45dd7c7f | -2.8794 | -50.72305 | 2025-10-20 05:01:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e62fa40c-cbfb-3635-82f4-64d6bbf2e1a8 | 1.72852 | -55.93657 | 2025-10-20 05:01:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 81bcb4d7-1a15-3e4d-837f-a87d25d1fbed | -2.4386 | -48.62014 | 2025-10-20 05:01:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 063eba42-b4a6-32fa-bfbd-83a175e4293e | 1.79121 | -55.70477 | 2025-10-20 05:01:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d8b986f9-e03f-3968-9682-867660b43279 | 0.87452 | -51.25362 | 2025-10-20 05:01:00 | NOAA-21 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 10.7 |
| d0e50f34-d267-368d-a683-23144f648d83 | -3.32842 | -50.2276 | 2025-10-20 05:01:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3cdf629c-b4f0-3578-ab15-4d7b6610714a | -2.91593 | -52.7129 | 2025-10-20 05:01:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0e5b0234-d854-32c4-831e-6e423079f654 | -3.24168 | -50.02725 | 2025-10-20 05:01:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 68d0591a-8e47-35cd-8ceb-3ebc1d75bfbf | -3.3303 | -50.74247 | 2025-10-20 05:01:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2ca06c00-1a81-33e4-8489-598d77dd1ee7 | 1.84721 | -55.6626 | 2025-10-20 05:01:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6b992f53-31c1-34fa-8b91-98ee3e0ddbc9 | 1.71253 | -55.76526 | 2025-10-20 05:01:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9e6489d0-ded4-3650-a704-e53533d7e72c | -2.86052 | -50.74425 | 2025-10-20 05:01:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bf673852-19a8-30ab-9465-b86203e11b2a | -2.86794 | -50.7213 | 2025-10-20 05:01:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 22828752-10d7-3487-bb6d-56f48c983e26 | 0.9833 | -50.06428 | 2025-10-20 05:01:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7ddd1f43-c2e0-35d0-b651-f2e184b7b225 | -1.6384 | -54.05281 | 2025-10-20 05:01:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1f36a931-9f78-3be2-8287-b7664cef0220 | -3.1451 | -50.24725 | 2025-10-20 05:01:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f36a94a8-4e62-3388-a622-2335a6bde4ff | -2.43924 | -48.61591 | 2025-10-20 05:01:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 43bdbeb2-78d9-3fa3-bcbe-72d3e4a09af3 | -3.14905 | -50.24786 | 2025-10-20 05:01:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7cd82bc6-8290-3326-beb3-5695ef10ce6b | -2.44457 | -49.37154 | 2025-10-20 05:01:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7b0c6631-0758-314a-8814-9c1587031286 | -2.72439 | -54.44104 | 2025-10-20 05:01:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e1a2032f-1d0f-3589-9067-cedd68822176 | -1.41258 | -52.67084 | 2025-10-20 05:01:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a61a1435-5354-311a-ad92-41ae7bfb78a7 | -2.63111 | -49.37482 | 2025-10-20 05:01:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a0f035dd-6c52-3393-8b10-c5d66a9d4bac | -2.30715 | -50.53162 | 2025-10-20 05:01:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4c877a20-d677-328b-9804-b3b25a7d1e94 | 1.7251 | -55.9371 | 2025-10-20 05:01:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a0f0759e-dbff-3c7a-96e1-2dcfe6368554 | -2.50762 | -49.04659 | 2025-10-20 05:01:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 666aabb7-76ca-3743-a736-d09f67076af6 | 1.73649 | -55.92013 | 2025-10-20 05:01:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fcac60d3-8338-38c3-9be3-2483d16dfd71 | 2.03962 | -55.76833 | 2025-10-20 05:01:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4d778815-9a1c-3f8d-9067-5b2d41ffccb0 | 0.96797 | -51.15743 | 2025-10-20 05:01:00 | NOAA-21 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 699947b1-813b-300a-91fd-2a0bf477da5e | -3.25966 | -50.04437 | 2025-10-20 05:01:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1c63146a-fafa-3dda-a14f-56db8f637787 | -2.27038 | -51.92178 | 2025-10-20 05:01:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 97e49465-7010-3173-af14-0d58b1db4e44 | 1.66683 | -55.96904 | 2025-10-20 05:01:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1ebe2b3d-75ba-3253-ac04-592c80fee1fd | -2.87104 | -50.72658 | 2025-10-20 05:01:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e4475199-f4ab-36a6-b110-348bb81b8219 | -3.32893 | -50.22422 | 2025-10-20 05:01:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| fbcc8346-6c9f-3d61-93d6-6f87fe6eb1e5 | 1.70402 | -55.77781 | 2025-10-20 05:01:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8d40e485-66ff-3eac-b518-10269ba36aa6 | 2.0169 | -55.7341 | 2025-10-20 05:01:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c00f4d34-362c-3c70-9c56-822cf45592d7 | 1.71536 | -55.76108 | 2025-10-20 05:01:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d9a4efde-c2d4-36db-a65b-fefb49f834be | -2.25681 | -51.91557 | 2025-10-20 05:01:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 352e450c-2f3f-3a10-b95c-4d83ba81ad23 | -2.91297 | -52.7319 | 2025-10-20 05:01:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cd61df43-b5cb-3730-af89-6881382e124a | 1.77645 | -55.70676 | 2025-10-20 05:01:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 429140c7-fc72-3f5e-9727-f0293c4fa13b | -3.3334 | -50.7478 | 2025-10-20 05:01:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5c3098e4-c951-38c5-bdee-c3548604de90 | -2.25096 | -51.90641 | 2025-10-20 05:01:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| b4b08aec-a2f1-3bc5-b245-c81bc20c47a8 | 2.04131 | -55.75675 | 2025-10-20 05:01:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0bbdfb06-3602-3c52-aa17-70f666d82855 | -1.095 | -54.13305 | 2025-10-20 05:01:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d249a486-2a09-3c43-bfbe-e90f3de4d032 | -3.33289 | -50.22483 | 2025-10-20 05:01:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 833a4297-f258-3caf-b2b1-7a5aaa7abee1 | -2.06067 | -56.83326 | 2025-10-20 05:01:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a1e7d2c8-82cb-3777-ba81-5d78b53efa8d | 1.74558 | -55.91108 | 2025-10-20 05:01:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| e2b0e9f7-4466-3db5-8c58-048fd516436f | 0.91963 | -51.14774 | 2025-10-20 05:01:00 | NOAA-21 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cfac4394-e778-3e35-9e2c-9adf733a3630 | 2.03846 | -55.71576 | 2025-10-20 05:01:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 805db1cb-0a97-3da9-b58b-beabcd7e09b3 | -4.83262 | -42.74741 | 2025-10-20 05:01:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 9a52ff56-aa88-37e0-bdb4-8c5396d548d6 | -2.50339 | -49.04594 | 2025-10-20 05:01:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 57b449d8-68b0-3f45-a5c8-f850995e6630 | 1.78103 | -55.70633 | 2025-10-20 05:01:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9bbdacaa-6055-39c5-9722-6794a6dd6526 | -2.08462 | -56.92492 | 2025-10-20 05:01:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| abdc2ac0-8c36-3cec-8dba-992bec36e49a | -2.15154 | -56.65755 | 2025-10-20 05:01:00 | NOAA-21 | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3efcfa5c-df76-36cb-9706-73449e350d16 | 1.84325 | -55.65947 | 2025-10-20 05:01:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d9ad271f-51f9-3991-b6cc-f09f13eb8b12 | 2.06682 | -55.7189 | 2025-10-20 05:01:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 000d0379-a20a-3355-8043-f3bd94380fce | -3.25914 | -50.04787 | 2025-10-20 05:01:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 537c009b-e21a-36e2-9b21-482ef34735cd | -3.41995 | -49.48291 | 2025-10-20 05:01:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bef692e8-87e4-393b-ab2f-6f0a84e33091 | -2.86506 | -50.74014 | 2025-10-20 05:01:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 50fddf46-9c80-37c8-b5b0-83aa5c2bc324 | -3.14116 | -50.24662 | 2025-10-20 05:01:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 71204817-8656-320e-a35a-eeebfb25af66 | -3.1343 | -53.00198 | 2025-10-20 05:01:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 89016a1d-dbf1-38aa-92c6-17e2c4caefd7 | -1.92456 | -52.13863 | 2025-10-20 05:01:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f21260a7-63bf-374d-82e6-250d0e84404e | -3.32957 | -50.74722 | 2025-10-20 05:01:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fb5c4dbf-61e1-3348-b582-728f5917d67b | -3.33414 | -50.74306 | 2025-10-20 05:01:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 04f3ccb2-a47a-3456-98d3-b5aab6556070 | 1.8116 | -55.67926 | 2025-10-20 05:01:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README16.md)
