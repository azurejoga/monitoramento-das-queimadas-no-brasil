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

## Dados Diários - Página 64

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| df885a97-161f-3b27-b7e9-e446f392b5d6 | -2.22677 | -48.38369 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cb5238ad-eab1-3df1-950d-e929c16744bc | -2.56537 | -46.53307 | 2024-11-10 04:36:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 669672ad-e950-3895-a8d7-cc0e095e8a72 | -2.62559 | -46.14053 | 2024-11-10 04:36:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4249d71d-066d-39c5-b702-5d6015a94f09 | -2.3356 | -48.48888 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ba44355a-c773-3afc-af89-5f0de31deb66 | -2.44014 | -45.98739 | 2024-11-10 04:36:00 | NPP-375D | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8350ac69-27d2-3386-a7cc-00a4a503b904 | -2.17823 | -48.4114 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f6b4bb8a-d90e-3726-b4e5-3bda300fab8f | -2.19637 | -48.38248 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 204a333b-4039-3915-8863-ade18bc27de5 | -1.21463 | -54.20488 | 2024-11-10 04:36:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| de363cde-4ef0-38e2-a8f7-75ba078ffc0a | -2.22183 | -46.43608 | 2024-11-10 04:36:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6c1a0716-9f76-364f-b862-af18358f9e45 | -2.37322 | -48.56929 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7c860b9f-0d46-3961-8a04-71086ebe7691 | -2.54645 | -47.32286 | 2024-11-10 04:36:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7b104c6f-a5d5-32dc-85a7-e41032ef02f1 | -1.50832 | -52.16979 | 2024-11-10 04:36:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 81fdb1b2-4d43-389a-9b71-35703138fc69 | -0.63997 | -52.3686 | 2024-11-10 04:36:00 | NPP-375D | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1409c1f7-1062-353e-9b88-2df8b8b5591d | -2.6279 | -46.14875 | 2024-11-10 04:36:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 55a4532b-7479-39fd-8c1f-e49c6f2e52ab | -1.22505 | -54.02741 | 2024-11-10 04:36:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5dbff453-48bf-3ad8-906f-18a1d61864bc | -1.68289 | -50.41268 | 2024-11-10 04:36:00 | NPP-375D | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| daa3f56a-116a-33b0-8c32-90e313c53f85 | -2.00264 | -50.06975 | 2024-11-10 04:36:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 93a8ec7b-f895-3bc5-a1d5-07a0173fb89a | -2.54425 | -46.312 | 2024-11-10 04:36:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1d6a0fb7-4681-3390-b982-43bb9efa85a5 | -1.39665 | -52.07011 | 2024-11-10 04:36:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b85c77bf-a529-3bac-9274-d492097e0788 | -1.45796 | -52.56054 | 2024-11-10 04:36:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 42693323-5a32-3fba-9ef4-b7fe6abdcefc | -1.99247 | -51.39747 | 2024-11-10 04:36:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 486001fd-a6cf-337d-a4b1-255b3c83afcd | -2.30637 | -48.3291 | 2024-11-10 04:36:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5c0c4ada-f564-3e2f-b05f-5c6b13ed9c8e | -2.337 | -48.58792 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5399f46d-e1e4-38a9-9d48-ea203edec359 | -0.33367 | -51.73875 | 2024-11-10 04:36:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d83769e2-4146-3fdb-9f7c-ffdb199f63e6 | -0.90533 | -49.51916 | 2024-11-10 04:36:00 | NPP-375D | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7958ee58-4919-3aed-8e8f-848e27d1886a | -2.62555 | -46.16413 | 2024-11-10 04:36:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cf93ff6b-6c06-38e0-8ea1-679509c543ef | -1.64617 | -52.05433 | 2024-11-10 04:36:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 91326cb0-e739-3b60-8722-73cb7a481e20 | -2.37105 | -48.58308 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bd4de220-a495-3085-a06c-f47e2c5bcde6 | -2.5402 | -46.31523 | 2024-11-10 04:36:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 50879fed-a61c-3e57-b3e1-e9beabeee02d | -1.61211 | -52.39249 | 2024-11-10 04:36:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2a23f303-4d4d-36c7-b28a-0a159067cf8d | -2.42599 | -48.47164 | 2024-11-10 04:36:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 41969ba4-0f83-3e44-8ea1-e8b568c8d82c | -2.56908 | -47.34112 | 2024-11-10 04:36:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 78542193-3455-31c2-8ddf-b82d7f36d168 | -1.16962 | -52.0894 | 2024-11-10 04:36:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 86b7f266-a8b1-30e2-8138-0d607e936949 | -1.58466 | -48.03296 | 2024-11-10 04:36:00 | NPP-375D | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c3aaf276-862c-3c0e-a2d9-9a909f15a8fc | -1.63604 | -48.20319 | 2024-11-10 04:36:00 | NPP-375D | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fbad163d-8957-3fff-9355-c053c5f60f53 | -0.14927 | -51.56401 | 2024-11-10 04:36:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c65ab753-76e7-3f0e-978e-34d5174422e8 | -2.29435 | -48.55658 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 839cbf01-0371-3c30-9805-81f7817bf331 | -2.24058 | -48.38231 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1ca66d7c-838c-322a-a7bb-319e4090d866 | -1.22752 | -51.96853 | 2024-11-10 04:36:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9793031e-0076-35fe-9385-338c4c1d3dc4 | -2.20132 | -48.37267 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 7e392f93-0e9a-301f-881d-7cba2e51e82a | -2.51991 | -46.37754 | 2024-11-10 04:36:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c4a73bcd-99a5-3563-9ae3-793717faa4e1 | -2.67769 | -46.7767 | 2024-11-10 04:36:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d56c9f4d-94cb-38ed-b952-763eab3c9ba2 | -2.35577 | -46.6718 | 2024-11-10 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6f037960-42e6-3de0-8f21-fade34a5f59c | -2.17797 | -48.32669 | 2024-11-10 04:36:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a7c26100-aa33-34f7-9532-f1d746b05684 | -2.24002 | -48.70706 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 66e10833-b04b-3bc1-8084-d8b47c69b87a | -2.20343 | -47.73628 | 2024-11-10 04:36:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 64d3f5dc-f5cb-3758-b88a-69ae454d9c3a | -2.06211 | -50.72769 | 2024-11-10 04:36:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 53ede75f-d532-3986-83b8-ef78b1f436c3 | -1.62355 | -50.53951 | 2024-11-10 04:36:00 | NPP-375D | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fb8c6660-20be-3b70-8d87-d31c0bec4109 | -2.32816 | -48.9195 | 2024-11-10 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7b57c106-40a5-374c-8fa9-c8ad55c70259 | -1.78077 | -46.14854 | 2024-11-10 04:36:00 | NPP-375D | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5efab2cd-056d-3279-a4e6-74e9d65c23f6 | -2.57188 | -47.34518 | 2024-11-10 04:36:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1ad786c1-421d-3fb9-85b2-ab88ed43f8bd | -2.63963 | -46.797 | 2024-11-10 04:36:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a684d9c2-79c2-3823-a639-ae0979d02b25 | -1.51356 | -52.16126 | 2024-11-10 04:36:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 27a355cd-0ff9-38d3-9dcf-d115c5e322be | -1.34216 | -51.4088 | 2024-11-10 04:36:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 09a37937-7bfc-3156-b04f-68f2291df04e | -0.04331 | -50.77127 | 2024-11-10 04:36:00 | NPP-375D | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 62c7ec9e-01e4-3c74-b7db-f56ef790a552 | -2.40561 | -48.49316 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bea85c44-92e2-3f81-88da-28aa63a8d29f | -1.31318 | -52.18502 | 2024-11-10 04:36:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e0d814ec-c04d-3a84-8f64-9c150166179b | -2.10888 | -48.29491 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 65e2a7f5-7b43-348e-9096-0217faccf735 | 2.60564 | -50.86328 | 2024-11-10 04:36:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6eee767c-933d-3b06-8839-275e58a8b799 | -0.46178 | -52.0276 | 2024-11-10 04:36:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cc67a9f5-fc97-336b-b5ff-e17c9a0f4bb8 | -2.6828 | -46.7887 | 2024-11-10 04:36:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fae15f6f-5d7a-352e-8410-4314f0e38762 | -1.77893 | -52.35714 | 2024-11-10 04:36:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| df1cc4b4-97c6-385d-ba3c-841aed374c2d | -1.64691 | -50.43802 | 2024-11-10 04:36:00 | NPP-375D | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 253f073f-5879-321b-a536-d2fad8ec1116 | -1.95443 | -48.86789 | 2024-11-10 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5ce579e4-5fb4-3c1f-9f07-2df7e549bd71 | -1.20043 | -53.6917 | 2024-11-10 04:36:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9d727ef6-5c6e-377a-9737-786983618a2a | -2.20512 | -47.74721 | 2024-11-10 04:36:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aad4c7ba-04ed-3c25-9765-f1a2aef8fc0d | -1.50919 | -52.18869 | 2024-11-10 04:36:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f0dc0a4b-afca-3c76-815e-240c8a3276b3 | -1.12063 | -53.60165 | 2024-11-10 04:36:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 003d11fd-ea79-36fe-84dc-df68fc9ebdc3 | -1.14681 | -53.78581 | 2024-11-10 04:36:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| bd6e8eb2-3c7a-3e54-81ba-a7b73c6a914a | -2.39549 | -46.77515 | 2024-11-10 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8ce8f8b0-02ec-38b1-8088-ae5ca5543e67 | -2.05705 | -48.51614 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| eb8db96a-a64f-37a5-b9f3-aace5a8ebf6a | 0.28626 | -51.26001 | 2024-11-10 04:36:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 34ced459-80be-35a2-b63f-6d70a71283c4 | -2.29647 | -46.71545 | 2024-11-10 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0d9e398b-9ca7-393b-9b1b-dc372cad8640 | -2.03503 | -50.08575 | 2024-11-10 04:36:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c0938617-2b57-3fda-b0cd-a4a6780ce095 | -2.37278 | -46.8089 | 2024-11-10 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0cbc12d9-6abd-3513-b00b-21dd88b49b56 | -2.69018 | -46.80855 | 2024-11-10 04:36:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4c38c89c-1678-33b1-bf92-562eea3dd778 | -1.38824 | -51.56612 | 2024-11-10 04:36:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7f84abe5-ef43-30f3-ab83-1eb45e8cac97 | -2.68902 | -46.81592 | 2024-11-10 04:36:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6c74f162-f34d-359e-83d3-c66f398ec22b | -2.11606 | -48.29249 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 269f5c96-d841-3764-9162-128d823ffa73 | -2.37168 | -46.72672 | 2024-11-10 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1c9269e4-b538-388b-a23d-c67cca0fdc84 | -2.1274 | -48.56592 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| da518254-4362-35c4-ba60-82d708252d9e | -1.15884 | -54.0834 | 2024-11-10 04:36:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7e20ddc2-ff88-3e73-a86d-56bf10cfcf6e | -1.51734 | -52.16186 | 2024-11-10 04:36:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d1879279-ddbf-3bcd-98d9-cbc4d3f2d830 | -1.58071 | -50.44329 | 2024-11-10 04:36:00 | NPP-375D | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 55df68d5-0f87-3694-93ee-924b06c194da | -1.64992 | -52.05494 | 2024-11-10 04:36:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 85ec01c4-bd0d-3ce6-8920-13bcaf5d7ed9 | -2.07709 | -46.33032 | 2024-11-10 04:36:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ac12f1c2-b2a2-3aa9-88bf-0135c3ef656b | -2.09758 | -48.90083 | 2024-11-10 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a5351e55-ee38-393f-955f-7864f2cdc48b | -2.29157 | -48.55262 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4a9abfeb-a537-3c0e-a360-5ce65502c73c | -1.39385 | -54.99452 | 2024-11-10 04:36:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2a8a9a24-a0bd-3826-8e7c-1fb614bc87a9 | -2.1114 | -46.40435 | 2024-11-10 04:36:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d247a4f8-f34d-3814-9d6d-add5ede8c6d3 | -1.32666 | -54.59957 | 2024-11-10 04:36:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 478e1405-595e-37ea-af4f-d64a7a73b604 | -1.67452 | -52.11886 | 2024-11-10 04:36:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4499c83c-24e7-3e4e-bdd8-329cb65919cc | -2.36825 | -46.79333 | 2024-11-10 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fb005c0c-e9d5-3be4-b73f-91383ac45f99 | -2.52695 | -46.30928 | 2024-11-10 04:36:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 060e1c91-8b4c-33b5-b253-237511a1a3a7 | -2.14054 | -46.68746 | 2024-11-10 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dfe0a58b-384c-38f1-8d70-9bb91e01e2fe | -1.59053 | -52.18496 | 2024-11-10 04:36:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a495893a-fbc8-3976-8578-67ee2d6f0aa0 | -2.10844 | -50.5705 | 2024-11-10 04:36:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 825a5247-1eb2-30eb-bed0-5b93151925a6 | -2.31673 | -46.54182 | 2024-11-10 04:36:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4bf565d0-82c0-3771-a709-74a3621d3cee | -1.64344 | -50.43748 | 2024-11-10 04:36:00 | NPP-375D | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5360ef81-a211-31a5-b419-4a81703c6150 | -2.15929 | -46.67912 | 2024-11-10 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README65.md)
