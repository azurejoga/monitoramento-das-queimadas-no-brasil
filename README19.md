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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 09de931e-7342-3d55-a519-d63d661e2a17 | -12.7959 | -54.0121 | 2024-09-28 01:07:53 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 50293ced-71a4-33ca-a7f1-833d144c0745 | -12.7975 | -54.019501 | 2024-09-28 01:07:53 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 42339ca0-99f7-3e83-b9e3-f605c267117b | -13.4827 | -57.244099 | 2024-09-28 01:07:53 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 83969443-6877-39b1-8f7d-a2dfa8bb8b98 | -13.4849 | -57.254902 | 2024-09-28 01:07:53 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e4816eac-f270-35b2-b58b-fe8dc7deef1f | -13.4871 | -57.265701 | 2024-09-28 01:07:53 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 22d3b8d9-9cc4-3c01-b9df-85d82055b420 | -12.5955 | -53.1534 | 2024-09-28 01:07:53 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d781a507-ac1d-30b1-9e02-d4c7070682e3 | -12.5971 | -53.1605 | 2024-09-28 01:07:53 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3d59584f-dfd8-36bb-a3f3-6a56965db17e | -12.7828 | -53.999401 | 2024-09-28 01:07:53 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d10f058e-ed4a-38a6-b3cd-8952e7e24589 | -12.7844 | -54.006802 | 2024-09-28 01:07:53 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6a4fac33-8837-3e3a-90f2-427817827194 | -12.7861 | -54.014301 | 2024-09-28 01:07:53 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e74d80a0-2dad-32fa-8f2f-0033fd2724f5 | -12.7877 | -54.021702 | 2024-09-28 01:07:53 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4ef65543-9813-3e61-85a0-41f904dc581e | -12.5842 | -53.148499 | 2024-09-28 01:07:53 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0876c6aa-825f-3aa0-a5c6-3bb64804e555 | -12.5857 | -53.155602 | 2024-09-28 01:07:53 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e83a38d9-3d6b-36b2-8e15-2237a91bcc86 | -12.7746 | -54.008999 | 2024-09-28 01:07:53 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e0f5e91c-1420-34de-baa2-451acea3b847 | -12.7763 | -54.016499 | 2024-09-28 01:07:53 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a843dd78-cc02-3930-916a-ec627f5ccf8a | -12.7779 | -54.023899 | 2024-09-28 01:07:53 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 06526711-c8d5-3a16-8ac2-4ddd3242bc2d | -12.7795 | -54.0313 | 2024-09-28 01:07:53 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e4ab838d-302a-3998-850b-e8455cdd8622 | -12.5759 | -53.157799 | 2024-09-28 01:07:53 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| eba749ea-36f2-3344-9ffd-d2bb3784ad4f | -12.7648 | -54.0112 | 2024-09-28 01:07:53 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6bc3467c-c07f-30f4-858e-572d80ac1c0e | -12.7665 | -54.0187 | 2024-09-28 01:07:53 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f78220bc-a1c9-3ad3-9c24-138787412e13 | -12.7681 | -54.0261 | 2024-09-28 01:07:53 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 11231369-05c4-30a5-a99e-8c5fa407afb7 | -12.7697 | -54.033501 | 2024-09-28 01:07:53 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a996f262-2ae6-3fc4-83c8-b6b37637fb18 | -12.7583 | -54.028301 | 2024-09-28 01:07:53 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 16eae7ae-e6a2-3f26-9e1f-d1728d2d8e3f | -12.5337 | -53.152599 | 2024-09-28 01:07:54 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5d92faaa-fcae-30a3-98e8-c1be57ebed23 | -12.5255 | -53.1619 | 2024-09-28 01:07:54 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 90b75415-4112-3618-acc5-efda79a9dc13 | -12.527 | -53.168999 | 2024-09-28 01:07:54 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0cfeb9d0-17c2-3884-8b6a-64231441fd50 | -12.5172 | -53.1712 | 2024-09-28 01:07:54 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0c5a1a96-e05a-39fc-bdd8-15ae90a5e121 | -12.6946 | -54.065899 | 2024-09-28 01:07:54 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d5d2f1fe-80d0-38f1-bb0e-45e0f3539cec | -12.6962 | -54.073299 | 2024-09-28 01:07:54 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 899741c0-92f2-3cc7-b69e-824192e9d6e1 | -12.6979 | -54.080799 | 2024-09-28 01:07:54 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ab8e9d0f-59ac-3787-b121-563652910ec9 | -10.8876 | -46.417599 | 2024-09-28 01:07:55 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5eeb137a-511c-398d-8648-a1379ab53c17 | -10.6673 | -45.868401 | 2024-09-28 01:07:56 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3771f84e-0a66-3905-8e9b-c1e8258b98a0 | -10.6707 | -45.882198 | 2024-09-28 01:07:56 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b86b0372-d4b1-3fa3-911f-e7a635eab12f | -10.6506 | -45.843102 | 2024-09-28 01:07:56 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2d4a269c-1538-3aea-94fe-bb96ce18d32a | -10.6541 | -45.856998 | 2024-09-28 01:07:56 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 02601bd7-a2f1-3757-a303-bc30c8bde593 | -10.6714 | -45.925999 | 2024-09-28 01:07:56 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2e5be89b-fac6-3c8d-8260-dfc934ea0a2b | -10.6749 | -45.939701 | 2024-09-28 01:07:56 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| edad6354-1625-37b2-8420-7257a3670166 | -10.6783 | -45.9534 | 2024-09-28 01:07:56 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b6ac7d26-0b13-3dd0-a484-5cf4d17e26dc | -10.6617 | -45.928501 | 2024-09-28 01:07:56 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c9da8c67-4bcd-3e15-9c1d-d14933a374b2 | -10.6652 | -45.9422 | 2024-09-28 01:07:56 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6c55fefc-051d-3939-86d1-e038221aa4e8 | -10.6686 | -45.955898 | 2024-09-28 01:07:56 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1ec5e14d-a21a-3057-b135-85dc7167e41a | -10.6721 | -45.969601 | 2024-09-28 01:07:56 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 898b1b94-40ed-3059-a043-148fd01501de | -10.6555 | -45.944698 | 2024-09-28 01:07:56 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| faf5aaf5-9cee-383f-b2b5-10aa556afa03 | -10.6589 | -45.958401 | 2024-09-28 01:07:56 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| bb268003-6539-3ce0-b170-a6dd00bec4b2 | -10.6624 | -45.972 | 2024-09-28 01:07:56 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f93de0ac-9681-3098-b124-1ce6e038324f | -11.7063 | -50.043201 | 2024-09-28 01:07:56 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b0740110-e41a-3e6b-b601-dee7a9f7fdde | -11.6947 | -50.0378 | 2024-09-28 01:07:56 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9ab9fb23-7dd4-3510-bddb-fa8298fe3dd6 | -11.6965 | -50.045601 | 2024-09-28 01:07:56 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 953faa08-c1ae-358a-95cc-b20547a75db4 | -10.6372 | -46.036301 | 2024-09-28 01:07:57 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7f438d0f-6d1d-3122-9154-a6d4e6620a40 | -10.6406 | -46.049801 | 2024-09-28 01:07:57 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a25e4c2f-3e2f-3b12-8c6f-f7fb3841b6f6 | -10.6308 | -46.052299 | 2024-09-28 01:07:57 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| fde3b65a-cce6-3bc4-a6a2-77cd1da2eb90 | -10.6342 | -46.065701 | 2024-09-28 01:07:57 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3be71ed8-7ffe-36d2-8930-7e412b46cd0b | -10.6211 | -46.054798 | 2024-09-28 01:07:57 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| da9c03f6-8e46-340e-acda-2309185b01f8 | -10.6245 | -46.068199 | 2024-09-28 01:07:57 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b5fc1abc-9bbb-3ba8-a0b5-c0c1fac3aa5c | -10.6279 | -46.081699 | 2024-09-28 01:07:57 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 114fc507-3576-36bb-93c1-93a4c9594007 | -12.6934 | -54.6717 | 2024-09-28 01:07:57 | METOP-C | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 51d32d97-827a-323f-bcae-a6c002fc5286 | -12.6951 | -54.679501 | 2024-09-28 01:07:57 | METOP-C | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 72e264e2-9e8a-326b-906d-61e9fb565f85 | -12.6968 | -54.687302 | 2024-09-28 01:07:57 | METOP-C | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a6c002fe-4643-3e45-9c59-0c07ff428f8c | -12.6985 | -54.695099 | 2024-09-28 01:07:57 | METOP-C | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2c9215bd-5dab-36b7-a72f-fab25ebb7086 | -12.7002 | -54.7029 | 2024-09-28 01:07:57 | METOP-C | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9b4862f2-e292-3691-8b8b-748424df516f | -12.7019 | -54.710701 | 2024-09-28 01:07:57 | METOP-C | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2631736b-d518-3a7a-a216-3b38a802f407 | -12.7036 | -54.718601 | 2024-09-28 01:07:57 | METOP-C | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0d332313-50a8-3575-accb-a4da3045fcba | -12.6819 | -54.6661 | 2024-09-28 01:07:57 | METOP-C | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 212f4b88-43b1-304f-8c4e-fc73d3f35c92 | -12.6836 | -54.673801 | 2024-09-28 01:07:57 | METOP-C | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c528a68b-689e-32f5-895f-816049e80936 | -12.6853 | -54.681599 | 2024-09-28 01:07:57 | METOP-C | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4d370f84-f6c2-30cf-90c2-c4f84cdff37f | -12.687 | -54.6894 | 2024-09-28 01:07:57 | METOP-C | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 56508ec1-ef97-33ab-ab1c-a6f7c18696fc | -12.6887 | -54.697201 | 2024-09-28 01:07:57 | METOP-C | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 06b9af23-37f5-3d73-95e9-53f7a213fd09 | -12.6904 | -54.705002 | 2024-09-28 01:07:57 | METOP-C | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d1bc03df-3494-3dc8-93a4-e8396bb9ab54 | -12.6921 | -54.712799 | 2024-09-28 01:07:57 | METOP-C | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e09f6392-5e36-30ed-8bda-5b5c9f583b34 | -12.6938 | -54.720699 | 2024-09-28 01:07:57 | METOP-C | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9f12d98b-5657-3040-9da0-200916f7fafb | -12.6954 | -54.7285 | 2024-09-28 01:07:57 | METOP-C | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7743486a-5a41-3d9c-a891-c7c1c9e4629f | -12.6687 | -54.652699 | 2024-09-28 01:07:57 | METOP-C | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b4050988-eb0a-3e4e-b868-b9edb99a5e2e | -12.6704 | -54.6605 | 2024-09-28 01:07:57 | METOP-C | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cabce6a1-94db-3cf0-bd45-78da2d6b7e5f | -12.6738 | -54.675999 | 2024-09-28 01:07:57 | METOP-C | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8560c0df-3654-363d-b862-6b72c923ac7d | -12.6755 | -54.6838 | 2024-09-28 01:07:57 | METOP-C | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 74e5b004-2357-32de-a605-337f4e4d83e1 | -12.6772 | -54.691601 | 2024-09-28 01:07:57 | METOP-C | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d47dcd0c-bc47-3757-8658-9d555e32bf02 | -12.6789 | -54.699402 | 2024-09-28 01:07:57 | METOP-C | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 43859d42-939e-37a6-b347-3237013f0527 | -12.6806 | -54.707199 | 2024-09-28 01:07:57 | METOP-C | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b4853977-e2de-3eb6-8528-69bf0accdb77 | -12.6823 | -54.715 | 2024-09-28 01:07:57 | METOP-C | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 46795cdc-398e-380e-b3c8-6a98745c379d | -12.684 | -54.7229 | 2024-09-28 01:07:57 | METOP-C | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8726880f-e040-39da-980e-866de4a178f3 | -12.6856 | -54.730701 | 2024-09-28 01:07:57 | METOP-C | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c84d859b-3c1b-39d6-8af1-5e971372ccea | -12.6589 | -54.6548 | 2024-09-28 01:07:57 | METOP-C | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 698de68e-58a5-3367-8eba-85f3bb02df0c | -12.6606 | -54.662601 | 2024-09-28 01:07:57 | METOP-C | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 84b075fd-d08c-3734-a0b9-e954cd4213fb | -12.6657 | -54.685902 | 2024-09-28 01:07:57 | METOP-C | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8307bd8d-342c-3fc4-8f12-81da41c555d0 | -12.6674 | -54.693699 | 2024-09-28 01:07:57 | METOP-C | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8810bd6e-f9ea-36d1-8f33-5c39e566f0ba | -12.6691 | -54.7015 | 2024-09-28 01:07:57 | METOP-C | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| de7e9753-60d6-333e-a143-f573a1c9109e | -12.6708 | -54.709301 | 2024-09-28 01:07:57 | METOP-C | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9e6ec667-397d-3b10-8eaa-35ec2e7fd572 | -12.6725 | -54.717098 | 2024-09-28 01:07:57 | METOP-C | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8c87e8c6-af0d-317d-a652-e5ed43583124 | -12.6742 | -54.724998 | 2024-09-28 01:07:57 | METOP-C | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2fc0cca3-37ac-3d86-bb30-9b209ef40d83 | -12.6525 | -54.6726 | 2024-09-28 01:07:57 | METOP-C | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fd5fd36c-3e64-3fdc-8cf5-75e4aad1b7ba | -12.6542 | -54.680302 | 2024-09-28 01:07:57 | METOP-C | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ebfb5389-d7d0-3a3e-a242-f64617aa951b | -12.6559 | -54.688099 | 2024-09-28 01:07:57 | METOP-C | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d1f381d3-98eb-3ab3-865c-d14e717849ae | -12.6576 | -54.6959 | 2024-09-28 01:07:57 | METOP-C | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 21b2245b-9d64-3293-a3c1-3338f8d08fc8 | -12.6593 | -54.703701 | 2024-09-28 01:07:57 | METOP-C | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d4961b23-3f1f-31e2-ac4b-73b7dd9ac9da | -10.6114 | -46.057201 | 2024-09-28 01:07:58 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| fe91ecd4-e8eb-350b-8341-88d290567d38 | -10.6148 | -46.070702 | 2024-09-28 01:07:58 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 453c0b70-1dc2-32fc-bdf9-853c661892a7 | -10.6182 | -46.084099 | 2024-09-28 01:07:58 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4c6997a2-5c1e-36a5-a1d2-a999687be0df | -10.5818 | -46.021599 | 2024-09-28 01:07:58 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 78920d1e-129b-3690-a816-c9668ed18b18 | -10.5852 | -46.035099 | 2024-09-28 01:07:58 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d6102996-dba1-368b-a2f8-7536fe2f5f99 | -10.5886 | -46.048698 | 2024-09-28 01:07:58 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README20.md)
