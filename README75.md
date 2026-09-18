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

## Dados Diários - Página 75

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5587c0c3-4241-3571-b410-f4a3341be9f5 | -4.77283 | -55.70723 | 2026-09-18 05:16:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 8c471bb5-19d3-3730-9f6f-df2b6230b8c9 | -2.89744 | -54.17393 | 2026-09-18 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 747f3521-b59e-3d93-bdcf-c166ae061ddb | -6.67096 | -50.90829 | 2026-09-18 05:16:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9f0d7528-0d97-3988-ab67-6876b22d8275 | -3.88453 | -58.94257 | 2026-09-18 05:16:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e1327486-270f-317e-a414-c4a91b6f3e7e | -3.27084 | -54.2641 | 2026-09-18 05:16:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| edea71a6-dac3-35ef-ad00-558b133acdd2 | -3.23368 | -54.31825 | 2026-09-18 05:16:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d8fbff76-c7f6-30ee-b0d8-d6377c5ffe8d | -7.05888 | -47.47646 | 2026-09-18 05:16:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| bdc5a36f-4542-3aef-8eac-abe172be758d | -2.81297 | -50.47974 | 2026-09-18 05:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 09897879-b792-30ce-bddb-218790f974c2 | -3.36067 | -50.45937 | 2026-09-18 05:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 51efadb1-ab56-31a4-8fdf-3f24bd32bc90 | -6.3729 | -58.28997 | 2026-09-18 05:16:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8fc80e12-a110-3a17-9f21-c0c6927df23a | -4.49065 | -55.49333 | 2026-09-18 05:16:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 922387e6-4232-342d-a252-a662881513dd | -2.82444 | -49.24207 | 2026-09-18 05:16:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 38f97a5e-0cfe-3220-b0c7-79ad1a4f2060 | -2.56129 | -54.74669 | 2026-09-18 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 936d7e6d-7856-3b8e-9a1f-4243495a288b | -3.70286 | -60.62955 | 2026-09-18 05:16:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1943e228-c71c-3d60-8739-1813181a171f | -2.10321 | -52.03657 | 2026-09-18 05:16:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0859523d-daa0-31a2-ae47-56c818f6e799 | -4.88575 | -56.0677 | 2026-09-18 05:16:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8f6bbfdd-34b9-365d-851f-60c9c7021476 | -4.80589 | -56.0806 | 2026-09-18 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6a6514c3-95a0-340d-900b-69a8ad8dd7f3 | -4.43756 | -55.52222 | 2026-09-18 05:16:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9260890c-be98-3288-a16f-811c0a26ff88 | -2.82238 | -50.47691 | 2026-09-18 05:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 21.7 |
| b05e9f5f-6b1a-3477-a4c7-ecc167033a86 | -4.8863 | -56.06416 | 2026-09-18 05:16:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ba4309c1-632f-3ca3-8237-c7a49b79685d | -6.1004 | -57.63112 | 2026-09-18 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 691a314d-26aa-3646-8a90-0ced88b907ee | -0.77936 | -47.55711 | 2026-09-18 05:16:00 | NOAA-20 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 102d883c-86c6-3736-934f-fe90a91eccd3 | -4.01494 | -49.95493 | 2026-09-18 05:16:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 373e4a8d-274e-382d-865a-a14a75d55e28 | -3.36511 | -50.46001 | 2026-09-18 05:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 08a9e7d7-69ad-3b78-93a6-1d3b6dd746c3 | -2.06452 | -59.66244 | 2026-09-18 05:16:00 | NOAA-20 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d3e5daf6-265f-367e-8201-9a978b5a3aca | -3.44227 | -58.19643 | 2026-09-18 05:16:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4405e648-6b4f-358f-97e8-f3b0c102c8d7 | -7.05775 | -46.22741 | 2026-09-18 05:16:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 64f25ba6-d033-38fe-944b-84c1a669e6c5 | -3.6725 | -58.66878 | 2026-09-18 05:16:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c254ca78-9ce7-37ad-8b73-0277b38940da | -4.27781 | -55.55374 | 2026-09-18 05:16:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 34411bb4-b288-30b7-b6f6-77d0e870dadf | -5.33395 | -45.14506 | 2026-09-18 05:16:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 46454d4f-8dca-399b-a4b4-08c77c4af97a | -3.57663 | -43.4656 | 2026-09-18 05:16:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4b663bf9-63c8-36aa-ae7f-184abcabef84 | -4.51211 | -54.96969 | 2026-09-18 05:16:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f0aa141f-f4f4-3956-ae76-4694052d5cd3 | -3.13453 | -59.02656 | 2026-09-18 05:16:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4f9ca768-34b5-3aaf-9252-c764ae77a0d1 | -3.47261 | -54.69473 | 2026-09-18 05:16:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 00823776-871e-315e-a31e-a6afc969b7bd | -5.85982 | -52.06851 | 2026-09-18 05:16:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 93766286-e213-3781-8c3c-2d9c4e4cc7f1 | -1.03648 | -53.74137 | 2026-09-18 05:16:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e062e9ad-25ef-352d-8a60-902f4a2221e6 | -4.53806 | -54.93892 | 2026-09-18 05:16:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a1687e1f-910e-3b06-91d3-45714c5105e6 | -2.29915 | -48.5792 | 2026-09-18 05:16:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2dbf6339-bbd0-3c49-999d-f563e0c0e249 | -4.56413 | -54.90774 | 2026-09-18 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7954b99a-24c7-3871-960c-6996273604b3 | -3.44889 | -58.42527 | 2026-09-18 05:16:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3ed15def-6b28-3984-ac2c-9c749c2ebea0 | -2.82175 | -50.48111 | 2026-09-18 05:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 21.7 |
| 3cdedd3c-9abe-3842-8b08-e7f3cbd3439b | -3.36715 | -50.44693 | 2026-09-18 05:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 2bba7cae-be34-33ae-98ba-7251c1eda4f9 | -4.88685 | -56.06062 | 2026-09-18 05:16:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fefdea72-f5e9-38c3-aaf7-3d2f8e0e2761 | -3.3408 | -59.81045 | 2026-09-18 05:16:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 566ceb83-4a54-36c2-9c69-612ebb14b4c0 | -3.33222 | -54.17144 | 2026-09-18 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d9e18306-bfd3-33fd-8a20-f7df44726ba8 | -3.33269 | -57.85749 | 2026-09-18 05:16:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a3fef8c5-1e64-3b60-a690-f9673375e629 | -1.14943 | -54.16759 | 2026-09-18 05:16:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5aef2fa0-776d-3b4a-aa88-3af5e9383681 | -3.80449 | -58.89602 | 2026-09-18 05:16:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2309d2fa-18fe-3801-a4f0-e3b5b94ae30f | -4.4797 | -54.98083 | 2026-09-18 05:16:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 81a4ae97-7385-31bc-8cbc-c3046e1bd735 | -2.82215 | -50.47852 | 2026-09-18 05:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 5c4ee517-7dc3-32c7-81c8-135ee6653b7b | -8.5545 | -44.90155 | 2026-09-18 05:16:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dcb10eab-cb9b-39cf-9e9d-9345a93ebcb7 | -4.42968 | -55.52829 | 2026-09-18 05:16:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 93e91284-29e0-366b-8187-bc7b1db59dd5 | -3.46914 | -54.69423 | 2026-09-18 05:16:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 65b7451e-045b-3d32-822d-423d33a21fe6 | -3.37532 | -50.44684 | 2026-09-18 05:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e4a082bd-bcb0-3bdd-b9c1-004f7a383922 | -3.81192 | -58.89341 | 2026-09-18 05:16:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f50ee323-a5b3-3b3d-a7b0-49817803593e | -3.69544 | -60.62833 | 2026-09-18 05:16:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f38dab25-be43-324d-b4a0-b9279a1be8ed | -2.90092 | -54.17756 | 2026-09-18 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d6257210-8ba4-3203-8859-1f94593f0fa8 | -3.44842 | -58.20106 | 2026-09-18 05:16:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b8f3b6a3-5f64-34cb-9125-5364d1b44410 | -3.73771 | -53.42543 | 2026-09-18 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 928c811e-34d2-37f0-9879-cae836edefd2 | -4.71563 | -55.75329 | 2026-09-18 05:16:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e6b1c1d4-7fcb-3618-b11b-dc20c2e1eb70 | -2.10013 | -52.0563 | 2026-09-18 05:16:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 29ed0f30-b6ee-32e0-912b-d7c6f2a423a1 | -4.51786 | -56.0797 | 2026-09-18 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e969e9da-781d-34a3-a335-beae6e8e85e5 | -7.00273 | -43.86927 | 2026-09-18 05:16:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 44c931ae-dda3-3995-8916-f64bef98f44e | -2.84467 | -57.63678 | 2026-09-18 05:16:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 79a0d6e3-7b50-3021-b806-001b290c8831 | -4.48952 | -55.50061 | 2026-09-18 05:16:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| da820f76-0b3c-3a69-9b7e-14706bbff106 | -4.48374 | -54.9776 | 2026-09-18 05:16:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 816e7daf-9e0d-3822-8e1e-24448142ab0d | -3.45009 | -58.21228 | 2026-09-18 05:16:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 265bb4c4-1fb2-3cd8-8dea-3da77fe4c3bf | -1.25 | -54.2179 | 2026-09-18 05:16:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5de0c2ed-0f8a-398f-b1a7-b979863a8745 | -4.77565 | -55.7113 | 2026-09-18 05:16:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 62ee448e-b728-313f-88d8-da67ebf2291e | -3.48582 | -54.72385 | 2026-09-18 05:16:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9f536efb-4aa9-3b42-9fb8-4bceb4cb007a | -7.80145 | -44.90243 | 2026-09-18 05:16:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e85ff891-0fb1-3f75-aaf6-43e59c2d8ede | -4.88465 | -56.07479 | 2026-09-18 05:16:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 235267aa-45a2-38d7-ad80-800c8977b4df | -2.2927 | -47.88302 | 2026-09-18 05:16:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5cfb94a8-5025-3cd4-a58a-85206b4c04d0 | -7.80446 | -44.82795 | 2026-09-18 05:16:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2fc837e2-4890-34b1-b6d2-e0455609507e | -2.81924 | -50.4678 | 2026-09-18 05:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 27.3 |
| 09946a9e-401b-370f-b11b-62d84ca9fe0a | -0.7454 | -47.53572 | 2026-09-18 05:16:00 | NOAA-20 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 616515e5-42e4-395c-9958-f78d457efef1 | -4.54268 | -54.9319 | 2026-09-18 05:16:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2256a18b-288e-36bd-9e7e-3d8d403d73e0 | -1.22576 | -54.12479 | 2026-09-18 05:16:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 17de63ce-16d0-335d-b6e8-10b9cffb3d8c | -2.83127 | -48.65067 | 2026-09-18 05:16:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 15828482-d40d-329a-a2ca-30891cc6fd3d | -2.89207 | -54.18513 | 2026-09-18 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bd074452-865e-31c4-bfea-f07a0d242658 | -3.37597 | -50.44246 | 2026-09-18 05:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f1d3fb9c-02da-3610-be28-a36c4a510b62 | -6.50058 | -58.38234 | 2026-09-18 05:16:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 35e4c3d1-1d3e-343c-b9eb-cb9d4af840dd | -5.86247 | -52.05053 | 2026-09-18 05:16:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e4ac57e5-2059-386c-af14-6b6c8261ea68 | -6.5236 | -49.88589 | 2026-09-18 05:16:00 | NOAA-20 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 8c29c477-80bb-327b-b836-a3f4f7b49bd1 | -3.37022 | -50.45634 | 2026-09-18 05:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 83c03149-8593-34df-89a4-294f06204d90 | -3.44337 | -58.21121 | 2026-09-18 05:16:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bc53890a-a60a-329d-b648-3b25ac594b73 | -3.36709 | -50.44107 | 2026-09-18 05:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| bc0e8321-f0d7-309e-b7d7-2bf1b542c298 | -5.75175 | -45.09643 | 2026-09-18 05:16:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| df69dd81-9dd2-3ee9-8853-d306a4a189b8 | -3.72947 | -60.59637 | 2026-09-18 05:16:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1a1e48da-4298-344d-82cd-c439c3598eda | -4.5091 | -54.97372 | 2026-09-18 05:16:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2cec6364-966e-3adc-98e6-e572841e6dd0 | -3.47319 | -54.69092 | 2026-09-18 05:16:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0cd73f51-2734-31eb-995d-26618e2cda81 | -6.14513 | -57.69134 | 2026-09-18 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| da6c4fa0-0ac0-3499-95d5-c25e98f9328d | -3.96252 | -56.13332 | 2026-09-18 05:16:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d0f16de4-4dcf-36e7-9882-649bb9435d45 | -3.26414 | -54.30707 | 2026-09-18 05:16:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| bb0dfa04-fb04-3229-9af6-f8664409362d | -3.74519 | -51.12675 | 2026-09-18 05:16:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5a392387-7098-3c59-86f3-e4887d91f1b5 | -3.70693 | -54.18163 | 2026-09-18 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b426cd4c-83f5-3a17-881c-0cebf11e981f | -4.36107 | -47.78469 | 2026-09-18 05:16:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 520a3a08-e275-3db3-8d0b-e6461295feee | -3.91861 | -55.74399 | 2026-09-18 05:16:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 78817b80-18df-372d-9aa3-0c66049b37bb | -3.3607 | -50.45365 | 2026-09-18 05:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 36f4e01f-82cd-306d-abac-0f0544e1e467 | -7.81011 | -45.11671 | 2026-09-18 05:16:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |


[Clique aqui para ver as próximas entradas](README76.md)
