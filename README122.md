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
| 52c79256-0ccc-34e5-a5c8-0991aff72eeb | -5.01293 | -45.82455 | 2024-10-09 04:38:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1999aa6a-8316-35fc-bc4d-0c63d70c4457 | -5.00931 | -45.82394 | 2024-10-09 04:38:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2400db55-9d97-3d53-97fe-14daf3190cc7 | -5.00614 | -49.59249 | 2024-10-09 04:38:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2278e99d-37b8-3d3f-b477-30c0583e24f6 | -4.96666 | -45.61613 | 2024-10-09 04:38:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b34cfff0-7594-3ec6-b77d-cc771c209f01 | -4.96646 | -45.61425 | 2024-10-09 04:38:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e6ab6e74-f275-3f62-ac90-b9a2f2d7c8ac | -4.95916 | -45.5187 | 2024-10-09 04:38:00 | NPP-375D | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 69c1da30-fb45-3cc5-ae9d-902a0cd8b4da | -4.95548 | -45.51811 | 2024-10-09 04:38:00 | NPP-375D | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| b3afb755-1b90-3db8-a034-bbd51845c53b | -4.95425 | -49.64505 | 2024-10-09 04:38:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a34b3289-fd7d-3150-a393-71891ac8284f | -4.94991 | -49.75907 | 2024-10-09 04:38:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 496e998d-b9a7-30ea-80f0-f0dd381e7008 | -4.94936 | -49.76257 | 2024-10-09 04:38:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4414e3d4-f0d3-3cd6-aacb-733a1d82dba2 | -4.94657 | -49.75854 | 2024-10-09 04:38:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e6af94b9-361e-33ba-9c82-26117b2680d1 | -4.94602 | -49.76204 | 2024-10-09 04:38:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 97f52d9e-c2c3-3537-9aae-a348ac9fb6a7 | -4.94547 | -49.76554 | 2024-10-09 04:38:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| de684c7c-8fe5-3010-bb08-c76348fc56ac | -4.94323 | -49.75803 | 2024-10-09 04:38:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 36ec85ee-5424-39b8-9e0b-affa028f5e1c | -4.94268 | -49.76152 | 2024-10-09 04:38:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dd21c5e9-17e2-3d04-b80e-a2badaf2afc8 | -4.92824 | -45.67111 | 2024-10-09 04:38:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e71ee576-ad70-32a0-b332-a06e09ecfaae | -4.92789 | -44.01537 | 2024-10-09 04:38:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 26c6cf10-c838-3b6d-b25e-ed05f384a144 | -4.92758 | -45.67536 | 2024-10-09 04:38:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b11ce91c-defd-31df-b0ee-adf597682f46 | -4.92737 | -44.01881 | 2024-10-09 04:38:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2a5648f2-212a-3772-8b94-ed99e8d3dab5 | -4.92335 | -44.01818 | 2024-10-09 04:38:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 906c447a-8843-32d0-8324-510877971dfe | -4.92016 | -50.56568 | 2024-10-09 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0fa9f095-9df1-3f60-905c-4d68974088ed | -4.91959 | -50.56932 | 2024-10-09 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dddedd41-40bc-3b30-bc80-af076dc352e1 | -4.90593 | -49.86369 | 2024-10-09 04:38:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b8518da8-5324-3fe4-914e-a7baca0865ea | -4.90537 | -49.86721 | 2024-10-09 04:38:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3783c4ec-26b2-3f2c-a69f-a256ea96fbb6 | -4.90536 | -49.93219 | 2024-10-09 04:38:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dfa50888-4401-33ab-8037-0210fc7a4618 | -4.9048 | -49.93573 | 2024-10-09 04:38:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7071e67c-d2fc-3587-8cf1-c5ba62e7d5de | -4.90281 | -45.10927 | 2024-10-09 04:38:00 | NPP-375D | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8528eb4f-9550-3a2a-9dcb-6a94f6f6c968 | -4.90201 | -49.93166 | 2024-10-09 04:38:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c33541e3-c762-33d6-8d1c-b46ee73e218f | -4.90145 | -49.93519 | 2024-10-09 04:38:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6e917bc6-6fc2-356e-ab12-d29685295ef5 | -4.89454 | -48.56324 | 2024-10-09 04:38:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1327a0c5-505f-342d-886f-81e0a5f916f0 | -4.894 | -48.56671 | 2024-10-09 04:38:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4d6d3618-5305-3a9c-8927-61ff327f2ea4 | -4.8523 | -45.41486 | 2024-10-09 04:38:00 | NPP-375D | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 82e6c114-b04b-33ec-9811-bf3e34beb4e8 | -4.83528 | -48.94049 | 2024-10-09 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d122d61c-001b-30f4-9e0f-7bf5d435e4d6 | -4.82499 | -48.09867 | 2024-10-09 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2dc9d5d3-4896-39fa-b4b8-22e0d9e3126e | -4.8194 | -49.23583 | 2024-10-09 04:38:00 | NPP-375D | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 57caf8c9-201c-3f9c-83be-b7bd62e8457c | -4.81812 | -44.35379 | 2024-10-09 04:38:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5cadb035-d4a5-382e-a834-68f084d445d9 | -4.80667 | -49.93839 | 2024-10-09 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| baa39fb0-a1c0-3c90-bfd1-193f59530a93 | -4.80599 | -45.34517 | 2024-10-09 04:38:00 | NPP-375D | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ca46d3ef-2cf5-3b4c-a5a5-388b32537c88 | -4.80331 | -49.93786 | 2024-10-09 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e414a959-0d2d-348d-84e7-1162b2ffecd2 | -4.78129 | -48.89974 | 2024-10-09 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8675b39a-7046-3bb8-9255-bdd1dc2aa4de | -4.78074 | -48.9032 | 2024-10-09 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d3700df9-f080-319b-b3f3-64e7c097a288 | -4.77905 | -48.8923 | 2024-10-09 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 453a3d27-f9db-3d3d-93eb-f9774e2c8f71 | -4.77851 | -48.89576 | 2024-10-09 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cd768478-6135-3570-8f79-d505380a1c9a | -4.77797 | -48.89922 | 2024-10-09 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c50ad8c2-63f4-337b-bcfd-f65b74124e31 | -4.77742 | -48.90268 | 2024-10-09 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4486261c-f334-3f2d-a4f3-048f54854ed8 | -4.77573 | -48.89178 | 2024-10-09 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 55e7f051-0b84-32c4-8d1c-8ec1d1cabac5 | -4.77241 | -48.89127 | 2024-10-09 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 485ad24a-c33b-3a5f-96d6-55ecac1bafa1 | -4.75875 | -45.759 | 2024-10-09 04:38:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5c630c09-a25f-308a-8447-5ab4f1ebd5bc | -4.75079 | -48.87726 | 2024-10-09 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a9816ef8-6f8d-3fe8-835d-f648290c93d5 | -4.74801 | -48.87328 | 2024-10-09 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9548d342-9fe1-311a-9a13-3bcf8606afef | -4.74363 | -44.10749 | 2024-10-09 04:38:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cfc3510c-2e9f-36cb-bc27-1219b2913e5d | -4.73963 | -44.10688 | 2024-10-09 04:38:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0bb46043-8e1c-3544-b6b1-ce88353aafc3 | -4.73831 | -45.67123 | 2024-10-09 04:38:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d6292090-1acb-366c-9fa7-681c133cce3f | -4.73646 | -46.66026 | 2024-10-09 04:38:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c8273799-1c62-3562-b6d7-5d83d299005c | -4.73587 | -46.6641 | 2024-10-09 04:38:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d5e6e399-ed33-31a6-ab87-a8ecfd4a8ac2 | -4.73466 | -45.67072 | 2024-10-09 04:38:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9c156b48-d9bf-3d57-aefe-29425d002c9f | -4.73416 | -46.65199 | 2024-10-09 04:38:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f6b29f6c-a103-3434-a432-a615600dd48d | -4.734 | -45.67499 | 2024-10-09 04:38:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1c31991a-7e0d-351b-855e-b728dcd907e4 | -4.73357 | -46.65585 | 2024-10-09 04:38:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f5ad3dcd-f6b4-3a52-9e32-e3e83333f84b | -4.73298 | -46.65972 | 2024-10-09 04:38:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9f2ece29-e0a1-39a3-87b4-3e14f6481df2 | -4.73098 | -49.13284 | 2024-10-09 04:38:00 | NPP-375D | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 06f9c700-bd3b-3ea8-88af-6f07447567d3 | -4.72765 | -49.13232 | 2024-10-09 04:38:00 | NPP-375D | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2f1f9a82-1265-3c11-be2a-e65845e72aa5 | -4.72712 | -50.87537 | 2024-10-09 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c1d8ae87-2b12-37f9-ac0c-b32641e3f1c0 | -4.72428 | -50.87111 | 2024-10-09 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 17d1e977-19f3-33d7-b749-4e53bfe5b5a7 | -4.72368 | -50.87484 | 2024-10-09 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 19e787e3-6b65-3955-96ff-0f840a465ef6 | -4.72308 | -50.87857 | 2024-10-09 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f19b4f63-5cc8-31bd-866c-a4514e335a80 | -4.71964 | -50.87803 | 2024-10-09 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b0af9ea1-8ff3-3666-acd5-40d6d7caf731 | -4.71233 | -55.76712 | 2024-10-09 04:38:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b90ee273-2482-31cd-8217-c381508fd39c | -4.70943 | -45.64082 | 2024-10-09 04:38:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d5517310-f8b4-3f66-bef0-f8294337c090 | -4.70578 | -45.64031 | 2024-10-09 04:38:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4365e588-4cab-38ec-83c5-8e54e4469aac | -4.6986 | -50.40085 | 2024-10-09 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f82377d4-57f8-3b8d-b233-f313c9e00c01 | -4.68866 | -45.87218 | 2024-10-09 04:38:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c29c8deb-f1b8-32af-851b-1740d48abe2e | -4.68802 | -45.87632 | 2024-10-09 04:38:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6da8af45-163b-3f96-aa89-7b4b8372fa8f | -4.68541 | -45.82137 | 2024-10-09 04:38:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 538ebb7b-13ce-3bcc-a132-3fdb55da2c4b | -4.68506 | -45.87159 | 2024-10-09 04:38:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 6e42268f-f21e-31eb-bfa6-7c21356b2821 | -4.68442 | -45.87574 | 2024-10-09 04:38:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 443b37fc-7051-3dca-a77e-5bb33d8769c4 | -4.68243 | -45.8167 | 2024-10-09 04:38:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 57acc7cd-0015-3a71-adcd-0da6f0827420 | -4.6818 | -45.82077 | 2024-10-09 04:38:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1118a2e9-5132-3623-a532-6ee4a7e97d9a | -4.68147 | -45.87094 | 2024-10-09 04:38:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 87a34b36-211c-31fc-8c1b-c5082e1d8f11 | -4.67788 | -45.87033 | 2024-10-09 04:38:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2970b2cd-dcf9-3e02-80d4-c3ad39bf96dc | -4.64703 | -44.37208 | 2024-10-09 04:38:00 | NPP-375D | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8c6eaf24-f1ca-36f7-8a50-da829ad758c3 | -4.6431 | -44.37149 | 2024-10-09 04:38:00 | NPP-375D | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 31.0 |
| 93bd84b3-60ab-3080-9b3b-6d786c1b84c9 | -4.64237 | -44.3764 | 2024-10-09 04:38:00 | NPP-375D | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 2b6d4abd-8ad5-3405-88d6-588ce8f5ec0d | -4.62721 | -50.97943 | 2024-10-09 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7f119f45-5e3c-3143-bfb9-062b2757dc2e | -4.62661 | -50.98317 | 2024-10-09 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 49cda804-5d4b-366b-8ceb-cd6f52299e3d | -4.62096 | -45.61193 | 2024-10-09 04:38:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5e0d784f-0cf4-32ae-b1fb-33afd3642b5b | -4.60509 | -56.15033 | 2024-10-09 04:38:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cdbe732d-b472-341f-9641-be7dd0e3697b | -4.60424 | -56.15535 | 2024-10-09 04:38:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 69a05753-0bde-35e4-921d-faef3fb4c004 | -4.52753 | -46.6133 | 2024-10-09 04:38:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3a94274c-8de5-3da5-bf6b-6636a79e2d57 | -4.52522 | -46.60511 | 2024-10-09 04:38:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6ff37248-9731-3ac2-98ed-f278bdf47b82 | -4.52076 | -49.07185 | 2024-10-09 04:38:00 | NPP-375D | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e7a1dfc3-aaa9-372b-9238-acd18e7d6416 | -4.51034 | -46.21 | 2024-10-09 04:38:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 033b4961-e71f-30a7-9da1-7268bfad171b | -4.50005 | -50.87504 | 2024-10-09 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 83c54ddb-bfe4-3eee-9fdd-09a1bc6faf55 | -4.49022 | -48.11915 | 2024-10-09 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 25.1 |
| f0a39377-3c52-3ebd-96eb-90afc40a82cc | -4.47312 | -47.73415 | 2024-10-09 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2b3834ea-3b2d-3275-be9d-edae74b3526f | -4.47257 | -47.73767 | 2024-10-09 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8e736aa8-d72e-31fb-ae65-10c7a433d970 | -4.46946 | -49.54018 | 2024-10-09 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 269d70d7-d5d7-3e68-9d3a-801be6d37526 | -4.46689 | -45.90835 | 2024-10-09 04:38:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ce95b5e4-025d-397a-8d1b-aea7090b467d | -4.46394 | -45.90368 | 2024-10-09 04:38:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2fae73ed-7c76-37a4-9da8-fabd07cf189d | -4.46189 | -47.96008 | 2024-10-09 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README123.md)
