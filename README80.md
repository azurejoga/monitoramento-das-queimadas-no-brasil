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

## Dados Diários - Página 80

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3ed1cdd9-1cef-39b7-92d5-4f9bcc3db663 | -2.23205 | -53.65226 | 2024-10-13 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bd1111f6-92a0-3bae-9a3f-401af8e76e54 | -2.22094 | -53.67939 | 2024-10-13 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dcde347d-1d2d-3b3d-bcda-a34c439549dc | -1.88697 | -54.42838 | 2024-10-13 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e0078821-4e2d-3fad-908a-69353343469d | -1.88643 | -54.43183 | 2024-10-13 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e660d4fe-76ae-35ba-a6e5-a254a1f4b4a4 | -1.88257 | -54.43476 | 2024-10-13 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 62c24a58-2c22-37ce-94bd-be9ef400b13a | -1.88202 | -54.43821 | 2024-10-13 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5ae6d37d-69b0-307d-a587-00a012f240ec | -1.73189 | -54.01488 | 2024-10-13 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d7ef3318-4858-393d-aa0a-96a1662a885d | -1.73135 | -54.01836 | 2024-10-13 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8b59612c-6d68-3111-ae5b-e52dc8e6db22 | -1.73017 | -54.17781 | 2024-10-13 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1bfb31ef-90b1-3364-a68e-f4297179ed20 | -1.72963 | -54.18126 | 2024-10-13 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0a0bc95d-1615-34d4-8821-47828ea53f46 | -1.72856 | -54.01437 | 2024-10-13 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3cf89b97-c7e2-3f18-8879-c676e5f5bfdb | -1.72685 | -54.17729 | 2024-10-13 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4ec89a88-7878-3057-9266-6749162d0352 | -1.72631 | -54.18075 | 2024-10-13 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 108c59ad-20e7-3e4e-a61c-cb43f03eeb9f | -1.69535 | -54.85067 | 2024-10-13 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 65e13f9d-6822-368d-af1a-20736e3a5f60 | -1.62973 | -54.77316 | 2024-10-13 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8edce56f-3e0c-3aad-abd7-114f4a6f7077 | -1.4795 | -54.48158 | 2024-10-13 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 504c8849-8ad3-35d0-88d2-220866b46b70 | -1.47618 | -54.48107 | 2024-10-13 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1203a9c1-a769-3b04-87be-e906acc61030 | -1.59906 | -53.34835 | 2024-10-13 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5a68eb96-1b62-3ba6-b1e4-200bd54dbe24 | -1.59569 | -53.34783 | 2024-10-13 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 32506b3a-d954-300e-90da-50141cd10186 | -1.59233 | -53.34731 | 2024-10-13 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3985d1f8-e7ce-3863-aae9-9d154e4e9b1d | -1.22736 | -53.37509 | 2024-10-13 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e5d8ac44-0396-3fc1-a05f-fb94f4db1bb1 | -1.19774 | -53.38858 | 2024-10-13 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 33c9b85c-7f7c-3a91-908a-f8f639d805f1 | -1.19493 | -53.38454 | 2024-10-13 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 37a8d473-3cf3-3288-9727-1b027a534ef1 | -1.19438 | -53.38806 | 2024-10-13 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 24ec849a-226b-3bcd-9f76-0a8a1c9dd10e | -1.16423 | -53.40504 | 2024-10-13 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bc5bf56d-8663-3c3b-92ee-8f13f57ac50b | -1.26616 | -54.67738 | 2024-10-13 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 85481ee0-0aa2-34ee-92bb-b797a5a4b717 | -1.26508 | -54.68427 | 2024-10-13 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a917cb69-0ba9-3a23-b00b-253bf2fef3c4 | -1.2623 | -54.68031 | 2024-10-13 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 442cbfc3-4acc-3c82-bdce-e667e01d816f | -1.26176 | -54.68376 | 2024-10-13 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| aa48e703-77a7-3b8f-8ae4-f47ff030f026 | -1.23301 | -54.11497 | 2024-10-13 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0c97ddb9-f136-329a-b0cb-08e42151a79a | -1.23247 | -54.11842 | 2024-10-13 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8f1983eb-4a45-3877-8a29-68d58504bdf6 | -1.20155 | -54.52628 | 2024-10-13 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fef6c633-f723-3ba3-b5ff-b28c47a3700a | -1.1691 | -54.19687 | 2024-10-13 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ac9e1d5d-1087-35cc-87f7-7c68a73836ad | -1.16578 | -54.19635 | 2024-10-13 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bb26092b-0021-3cdb-816a-05037b6e1b72 | -1.14666 | -54.10149 | 2024-10-13 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4410b8c1-322c-3799-8b46-bb223e10511a | -1.14612 | -54.10495 | 2024-10-13 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 82ee071c-cc80-3d68-9f55-f70c6dbb5276 | -1.14425 | -54.09756 | 2024-10-13 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 086e6fea-c417-3619-bc2a-e0d75239796e | -1.14371 | -54.10102 | 2024-10-13 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fe643ac4-167d-34e8-959e-e5038b07e845 | -1.14093 | -54.09705 | 2024-10-13 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 35f55575-f9b8-3628-ab3d-445b6e71dc84 | -1.12511 | -54.17587 | 2024-10-13 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 96b65089-87f3-3449-81ad-0911851a7f4d | -1.12179 | -54.17536 | 2024-10-13 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 32fe647b-758e-34db-8261-3258e576a99c | -1.09522 | -54.17124 | 2024-10-13 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a70d0d7b-186b-3b2a-855f-3c63993f5005 | -1.0919 | -54.17073 | 2024-10-13 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f1fc6a1b-5663-3514-ab31-a5419074a334 | -1.02565 | -53.73129 | 2024-10-13 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 524f2224-4fc6-3b51-88ff-304d194d86ac | -1.02286 | -53.72731 | 2024-10-13 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 96cc5998-3027-3989-bd39-5fc6f9d3c49b | -1.02232 | -53.7308 | 2024-10-13 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d1a544bf-9497-37d4-a5ea-10522bf9357e | -1.01898 | -53.7303 | 2024-10-13 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d42e06b9-1171-363d-b98d-d6558fe4e2b5 | -3.29965 | -53.85619 | 2024-10-13 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| b3861d3d-209d-3d3f-84e8-89cf25acb540 | -3.29684 | -53.85213 | 2024-10-13 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 80dd77c6-2623-3668-910f-c71580a6aed9 | -3.29629 | -53.85567 | 2024-10-13 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 881deb4e-722f-3d7d-b25e-2b49aae22462 | -3.29459 | -53.84454 | 2024-10-13 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ea4029df-ad54-32cd-9533-6bccac54f50a | -3.29404 | -53.84808 | 2024-10-13 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cd190e00-9c61-31ff-b2d7-d49ee5853b23 | -3.29349 | -53.85161 | 2024-10-13 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b971d448-3dae-36c4-9f90-7c6d65264ce6 | -3.12209 | -53.73857 | 2024-10-13 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5a774851-0259-348b-af2f-8f834f2c3683 | -3.11872 | -53.73805 | 2024-10-13 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fe29b0b6-6607-3ba4-bbb0-8dd3c81b57eb | -3.06865 | -53.88222 | 2024-10-13 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8517444a-7ec4-312d-9aa8-033bf2d8bc4a | -3.0681 | -53.88577 | 2024-10-13 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a866f477-0471-3e81-930b-526b54ec5844 | -3.06475 | -53.88524 | 2024-10-13 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b4fda956-9433-3a3a-8425-1372eff3e0d1 | -3.00663 | -54.03804 | 2024-10-13 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 535f6f22-d97a-3f02-aeb2-1d0bf45228be | -3.00411 | -53.91156 | 2024-10-13 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c3699360-33a5-3119-8b11-5453a97ed175 | -3.00076 | -53.91104 | 2024-10-13 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 57747b61-f38a-3dff-a2ee-ec2b41316ba5 | -3.0002 | -53.91455 | 2024-10-13 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 75dedb10-29af-3958-8347-9aec89c4566a | -2.99965 | -53.91806 | 2024-10-13 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 44a4eb67-5579-34a7-8e88-5b004cf7f25f | -2.99741 | -53.91052 | 2024-10-13 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 20488ae1-7441-376f-8020-76cf3e9a5a66 | -2.99685 | -53.91403 | 2024-10-13 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 587f8473-329a-3e05-988d-7eb3c93a28ba | -2.9963 | -53.91754 | 2024-10-13 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ba9afbd7-f40e-3561-8219-4db3142af332 | -2.93295 | -54.21198 | 2024-10-13 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 66db9a3a-ee12-313f-8478-0a45388def17 | -2.93016 | -54.20798 | 2024-10-13 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8af2d17c-33f9-31fc-bde3-9f68123c8175 | -2.8216 | -54.0126 | 2024-10-13 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 787b1cc7-dce4-3d3a-8b3f-c25ab151e62e | -2.79044 | -54.01493 | 2024-10-13 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 077aa278-0b9b-3f2e-b142-d7964dbd1dda | -2.78765 | -54.01091 | 2024-10-13 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3d42803e-fbcc-3ff8-bd4d-09f93e072a86 | -2.57603 | -54.26342 | 2024-10-13 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4162bd3b-6110-3ebb-9e52-53ba200aabd2 | -2.53563 | -54.28197 | 2024-10-13 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 09fc850f-7454-3fbc-826d-19ca10ef1620 | -2.47806 | -54.77872 | 2024-10-13 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 68c13a79-aaec-3ffb-aa96-7e249c716e18 | -2.18935 | -54.48645 | 2024-10-13 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a7d671b5-d6a4-3dce-a4a9-f32952034d34 | -2.1888 | -54.4899 | 2024-10-13 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4a5abb1f-c391-31e0-ad66-f871c4d23e24 | -2.18548 | -54.48938 | 2024-10-13 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f8383820-1d96-3156-80a9-1c45824bc66f | -2.12543 | -54.63549 | 2024-10-13 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 22a10350-ce13-3915-9f9c-32c37f596dfd | -1.23845 | -55.90294 | 2024-10-13 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 73c22362-5009-3f9e-be4e-f04becef7a36 | -1.71774 | -55.14105 | 2024-10-13 05:01:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0cdfe344-adee-3f0f-84b4-c7c0364f68ef | -1.71719 | -55.14452 | 2024-10-13 05:01:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 25c536bc-762c-371f-bc5b-70c9d60e1c60 | -1.67957 | -55.18842 | 2024-10-13 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a8fd7f8c-8f65-32d5-a677-1707494954f3 | -1.67624 | -55.1879 | 2024-10-13 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| eaec708e-d043-3650-a0db-8dbf343da698 | -1.67058 | -55.13725 | 2024-10-13 05:01:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2e161d92-73d7-3680-819f-9d2d2ef00217 | -1.66671 | -55.1402 | 2024-10-13 05:01:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b74f4612-0693-334c-9670-4d46e5f9366a | -1.65439 | -55.0886 | 2024-10-13 05:01:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3c95ef9f-62ae-38a9-a2bf-a7f044795169 | -1.65406 | -55.19867 | 2024-10-13 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 90d2ccf6-edc4-33b6-9668-1af321b46902 | -1.65385 | -55.09206 | 2024-10-13 05:01:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ea19afb2-14c0-3fce-a8ce-a48c4d767266 | -1.65351 | -55.20214 | 2024-10-13 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1ee5266d-ea68-3fbd-9e19-3a05d7ce2bc7 | -1.65052 | -55.09155 | 2024-10-13 05:01:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0c1ebd37-c222-3de0-9c55-108c44bc40cb | -1.65018 | -55.20163 | 2024-10-13 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5c2486ec-0dc7-3ec4-8819-1ae7a3318e2c | -1.63898 | -55.14299 | 2024-10-13 05:01:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ff27103e-5839-3fc7-be9f-36e25676d5c7 | -1.63564 | -55.14248 | 2024-10-13 05:01:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ddfa980d-50be-3ba7-a810-fa65b073722e | -1.63016 | -55.17716 | 2024-10-13 05:01:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b7413b5f-938f-3e92-acd0-8877e3195d55 | -1.9507 | -56.45914 | 2024-10-13 05:01:00 | NPP-375D | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 01b0d47c-c7f8-30f8-919b-fb0716220d63 | -1.94785 | -56.45491 | 2024-10-13 05:01:00 | NPP-375D | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| e377e10d-7d97-33ac-b063-31fde678beb7 | -1.94727 | -56.4586 | 2024-10-13 05:01:00 | NPP-375D | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 750877c3-2fbf-3cfa-9cb5-79f5a3f97474 | -1.94443 | -56.45438 | 2024-10-13 05:01:00 | NPP-375D | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 51de10c0-3cdd-3234-9fe2-0fe83c1918c0 | -1.56415 | -55.89808 | 2024-10-13 05:01:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4366b7e9-a0e4-3652-8b29-f95df064df04 | -1.56359 | -55.90165 | 2024-10-13 05:01:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README81.md)
