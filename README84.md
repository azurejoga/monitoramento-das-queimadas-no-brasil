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

## Dados Diários - Página 84

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 114f405f-dca1-36a8-ae95-2524a9b63f34 | -1.00008 | -51.72876 | 2024-11-29 05:20:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ab1fce79-6e7f-38d0-91cd-81d80fb91a91 | -1.58814 | -52.27699 | 2024-11-29 05:20:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 972af491-40b9-3e9a-87ae-daaa3ac38691 | -1.91455 | -50.5589 | 2024-11-29 05:20:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 609611ac-8529-322b-aadb-29ed803637ec | 1.22045 | -55.94193 | 2024-11-29 05:20:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1fe67fca-bbaf-3d83-a18b-fa18a042b7ae | -1.54141 | -52.665 | 2024-11-29 05:20:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0aa645ee-fae9-37a1-b9c6-abdcf6ee7880 | 2.24774 | -55.91656 | 2024-11-29 05:20:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fbf9577c-ad49-3e77-b376-da6c1455d4f8 | 1.29894 | -60.41903 | 2024-11-29 05:20:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b104054e-e4c6-3c52-9dea-edfbd9c349df | -1.04732 | -51.74144 | 2024-11-29 05:20:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 5.3 |
| ce35e842-1ef6-3cf6-a9f3-55aee2889550 | -1.09333 | -53.37479 | 2024-11-29 05:20:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3a165432-551e-340b-8383-0518cd81a192 | -1.1674 | -53.66933 | 2024-11-29 05:20:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9b615658-2adf-35ff-a963-94d2e9450200 | -1.40328 | -53.40128 | 2024-11-29 05:20:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a20dd271-6f12-3777-b197-d0df02e9f1bf | -1.65642 | -52.49984 | 2024-11-29 05:20:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e8b5008b-51cc-31ed-8daa-ea47afa7bcef | -1.33853 | -51.93902 | 2024-11-29 05:20:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 99b3acd0-c948-3c11-a7ee-0f65d5f503c0 | 1.22918 | -55.93718 | 2024-11-29 05:20:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6fbb7f86-8bd9-3363-b179-3303ee9c17d5 | -1.21527 | -53.55447 | 2024-11-29 05:20:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 27e50129-aaaa-36b4-a76f-e879ba830040 | -1.20447 | -53.68184 | 2024-11-29 05:20:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f2eeb044-9a45-39af-9a93-7b7c07e56775 | -1.06546 | -53.21283 | 2024-11-29 05:20:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a455ecac-dd4f-3fd6-a916-bf495b060065 | -1.31305 | -52.86394 | 2024-11-29 05:20:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 72395f61-2ea4-3c9d-98fb-6591b6970bab | -1.20083 | -53.87213 | 2024-11-29 05:20:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 45077271-b6c5-3964-97f7-b7fa9bd13c61 | -1.08161 | -53.64111 | 2024-11-29 05:20:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 815a2c49-f94e-384c-adfe-b9ae4029647a | -1.38338 | -53.63963 | 2024-11-29 05:20:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d3bfb595-6190-3c15-8c35-1e84f6576e5d | -1.355 | -52.9355 | 2024-11-29 05:20:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c547fbc1-6705-3213-a74a-93204c8bb05c | -1.14268 | -48.33469 | 2024-11-29 05:20:00 | NPP-375D | BELÉM | PARÁ | Brasil | 1501402 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| abc198e7-4d6b-37ed-a083-7be889404e57 | 0.97943 | -50.26381 | 2024-11-29 05:20:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d7ba00dd-8b18-3f99-aeba-b0d4963ff715 | -1.17039 | -53.6777 | 2024-11-29 05:20:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| efb50aed-2837-3dad-bd34-41087fc8b98f | -1.15971 | -53.58069 | 2024-11-29 05:20:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 4ad35235-3f58-3af2-90cc-635758ea7911 | -1.19002 | -51.76067 | 2024-11-29 05:20:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ba107bbc-1717-3f8e-b1c0-1a101b2e5897 | -2.3386 | -46.87881 | 2024-11-29 05:20:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 72a3ddf0-0fc9-36b6-8854-da9e7ce5ed2c | -1.09074 | -53.39119 | 2024-11-29 05:20:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 12095502-55c2-3137-9ab7-98158cbb90a0 | -1.34548 | -51.98815 | 2024-11-29 05:20:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 259d8a90-b22d-32fa-94eb-ca20d8259809 | -1.51159 | -52.55677 | 2024-11-29 05:20:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8974c70f-9071-3924-a9d2-d13ea81682a2 | -1.14329 | -48.34107 | 2024-11-29 05:20:00 | NPP-375D | BELÉM | PARÁ | Brasil | 1501402 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dc10d167-7191-3257-8b19-42a64310c39f | -2.34044 | -46.86695 | 2024-11-29 05:20:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e744ff56-894b-364d-afd3-0421bad01eb2 | -1.4966 | -52.43953 | 2024-11-29 05:20:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7ec482dd-6290-3c32-8992-0d78ab86b94b | -1.59129 | -52.28741 | 2024-11-29 05:20:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 51ebe7ce-70a6-34fe-bf05-343e242e8a69 | -1.61151 | -52.29732 | 2024-11-29 05:20:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 21ac0df3-fb47-3bde-9e91-bc57ab617abe | -1.36359 | -51.96498 | 2024-11-29 05:20:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b7399d6d-08be-3d7b-8413-ce999907d685 | -1.25574 | -51.59243 | 2024-11-29 05:20:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a0dce6e1-8c89-3d32-826a-9a6338928a16 | -1.08902 | -53.3742 | 2024-11-29 05:20:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 669b5ba1-ad79-3a3d-8775-33a7e30bdee1 | -1.62776 | -52.3788 | 2024-11-29 05:20:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 30abe06b-6d08-3359-bd39-e79b92db91f7 | -1.09269 | -53.37881 | 2024-11-29 05:20:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2dc2dc95-680f-3102-85be-544900fc48dd | -1.07851 | -53.38514 | 2024-11-29 05:20:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 805b9258-2b65-3ccc-8dcf-e68823bb1619 | -1.32042 | -51.74094 | 2024-11-29 05:20:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fdf75f72-39f5-3db4-9fc2-0c66bd4d1ed1 | -1.53233 | -52.66358 | 2024-11-29 05:20:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 587aee72-47d4-37fc-b405-c2a20e4033b0 | 4.39833 | -60.74151 | 2024-11-29 05:20:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 259147a2-9d95-3bca-b0dd-88af64d0a8fe | 0.93996 | -50.73944 | 2024-11-29 05:20:00 | NPP-375D | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 0687f7c6-8ca3-32bd-a941-dfbecfcbdce9 | -1.3226 | -54.63404 | 2024-11-29 05:20:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 18cd97ba-0e7d-355f-8325-251bf855b9e2 | -2.3328 | -46.8718 | 2024-11-29 05:20:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| b896080a-13ab-3d7e-9238-5645c16ec5b2 | -0.05277 | -50.8249 | 2024-11-29 05:20:00 | NPP-375D | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bb3bb798-c02a-3c29-975d-8caeab829931 | 0.94417 | -50.73524 | 2024-11-29 05:20:00 | NPP-375D | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8c944a70-dcde-321a-ad57-c500f0f88952 | 1.28068 | -55.91685 | 2024-11-29 05:20:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f1a28e4e-5896-3b3d-91a8-f3be6a16d983 | 1.45732 | -55.89574 | 2024-11-29 05:20:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a7e2da21-a9ed-38c0-9253-037dceb72470 | -1.59824 | -52.29029 | 2024-11-29 05:20:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 846619e3-11b5-38da-960e-4d83f6bf3dc6 | -1.19483 | -51.76143 | 2024-11-29 05:20:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8685558b-d2d5-3e3a-8915-69cf08daa916 | -1.15306 | -53.62315 | 2024-11-29 05:20:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5a31caf0-7eb4-3ffc-92b0-ed55ba8a73b9 | -1.37917 | -53.63882 | 2024-11-29 05:20:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 32d0e396-15b0-3547-970b-84d00ee05bab | -1.36952 | -53.61732 | 2024-11-29 05:20:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 173d5e33-bb0e-3a40-93c0-f3b805fd6e5e | -1.59672 | -52.28328 | 2024-11-29 05:20:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| fc3d0708-6a17-386c-8a98-dcdfe10e4856 | -0.94703 | -51.65643 | 2024-11-29 05:20:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7274b822-b7b2-351a-9f9e-e4766f2dd4a3 | 1.2058 | -55.96478 | 2024-11-29 05:20:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 355327a5-82af-387b-b506-3c12e0df4bc7 | -1.33536 | -51.92819 | 2024-11-29 05:20:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9255c093-3702-32f8-a499-58bab276f3fa | -1.09396 | -53.37077 | 2024-11-29 05:20:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| afd2043e-f848-330b-9342-d6102b6f51d1 | -1.2147 | -53.5582 | 2024-11-29 05:20:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| d0002f95-cc49-3580-8a2a-54313202b81d | -1.50861 | -52.63655 | 2024-11-29 05:20:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6cec844e-8271-396f-83e6-96f986cda2b3 | 0.98373 | -50.12719 | 2024-11-29 05:20:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 12.3 |
| a5dbd1cd-f31c-3499-888e-68c5f29dc4ef | -1.12176 | -53.7407 | 2024-11-29 05:20:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 23909231-e39d-3c0e-ae93-d784a78dfc3f | -1.56031 | -52.01888 | 2024-11-29 05:20:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0811d2e6-2d0c-33bd-8587-0ee875279112 | 0.03345 | -51.11204 | 2024-11-29 05:20:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b1992d54-a500-377a-81b2-28f6110e0fdc | -1.3188 | -51.75142 | 2024-11-29 05:20:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9b52337f-bc1d-3d1c-93da-51ac83cd1441 | 0.94089 | -50.7451 | 2024-11-29 05:20:00 | NPP-375D | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 98561095-8b36-381b-9b85-77070656b59e | -1.23886 | -51.79478 | 2024-11-29 05:20:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3923021a-c509-3f87-ae59-d5d74d30ccb7 | -0.78734 | -52.40718 | 2024-11-29 05:20:00 | NPP-375D | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c692b56d-f2b8-3e47-a489-4d128b2b416a | -2.33469 | -46.87173 | 2024-11-29 05:20:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 6dd900c9-3e06-3ff1-8397-7cf4bc410b56 | 0.33766 | -49.71578 | 2024-11-29 05:20:00 | NPP-375D | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 3a93b8cc-7297-3646-9a0f-474dc1174ead | -1.30193 | -51.73261 | 2024-11-29 05:20:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 97484eda-2767-3f89-befb-d2f3d106c4cf | 0.98508 | -50.26604 | 2024-11-29 05:20:00 | NPP-375D | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 48459483-34f8-3033-b674-5fba21640752 | -1.55471 | -52.27681 | 2024-11-29 05:20:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e66207aa-20bd-3761-bbaf-8c7af02698aa | -1.51087 | -52.56145 | 2024-11-29 05:20:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 601a8618-01bc-39b2-b1fb-02b5b578e89b | -1.31159 | -51.73412 | 2024-11-29 05:20:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 10478570-683f-3486-b2f8-cba8b08830a9 | -0.95377 | -51.65644 | 2024-11-29 05:20:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 96d5ab73-e8f1-3803-8edd-2197d75c64df | 0.94095 | -50.74738 | 2024-11-29 05:20:00 | NPP-375D | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 5.6 |
| b071a52e-c6cb-34c3-90a6-7065544b7d9f | -1.09997 | -53.3884 | 2024-11-29 05:20:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1da7ed45-7612-30c2-825f-44c06be2d470 | 1.22401 | -55.94137 | 2024-11-29 05:20:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b7830f18-0b02-371a-bbcf-bbc1aed7429c | -1.10432 | -54.14699 | 2024-11-29 05:20:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 60aafa2f-e628-3379-92fc-eff7c86d7219 | -1.16058 | -53.68516 | 2024-11-29 05:20:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cc5c42c9-0370-3bdc-8747-f2907284d471 | 1.28449 | -55.94092 | 2024-11-29 05:20:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b58e0d9e-7c1d-36db-9fb4-8125e1e0c4c2 | 1.67869 | -50.66021 | 2024-11-29 05:20:00 | NPP-375D | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b9889de8-df6f-314a-8cfb-29b172404d05 | -1.59987 | -52.29369 | 2024-11-29 05:20:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 7ec0ef47-3cd2-3769-99c4-4fc34993d12d | -1.5889 | -52.27213 | 2024-11-29 05:20:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 44663e25-5c83-3e31-955c-9923dbd54f99 | -1.80719 | -48.77392 | 2024-11-29 05:20:00 | NPP-375D | ABAETETUBA | PARÁ | Brasil | 1500107 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a319991a-7873-364b-9fb2-1fde4444770c | -1.53394 | -51.61845 | 2024-11-29 05:20:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| c32d37bb-80bb-3919-98fa-cb796081c64b | -0.91537 | -52.7001 | 2024-11-29 05:20:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f7926baf-4cc4-3668-91db-bf322bb2baaf | -1.43204 | -53.79872 | 2024-11-29 05:20:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3cc21bf6-53fe-3a39-a3d3-b4ac6a221bc5 | -1.58738 | -52.28185 | 2024-11-29 05:20:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| fd29347a-17e1-3747-aca3-837dc04681d3 | -1.08646 | -53.3905 | 2024-11-29 05:20:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| ded73e3b-0d46-38cf-8809-cda2070d5305 | -1.15916 | -53.58426 | 2024-11-29 05:20:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 76ad7e16-53ab-345e-8c05-5ae347e98c84 | -1.10395 | -54.14647 | 2024-11-29 05:20:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| be39919a-2b9f-372a-aad0-9782ce410273 | -1.10597 | -53.40601 | 2024-11-29 05:20:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 73511d53-c2c3-3be0-955e-b1ad896f2361 | -1.04246 | -51.73674 | 2024-11-29 05:20:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 93acfb3f-3876-3fa0-aca2-83ea35f86b0b | -1.62385 | -52.37329 | 2024-11-29 05:20:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README85.md)
