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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 91935363-5734-3749-81e0-1cdfc0499bfa | 3.20966 | -60.51796 | 2025-03-03 05:59:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7d47ea10-96e0-3f4d-b0eb-7fd3b0c85891 | 1.88693 | -60.86183 | 2025-03-03 05:59:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3498cbce-7a51-3e95-997a-08008db9f03e | 1.90567 | -60.45717 | 2025-03-03 05:59:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 244433db-3ee3-3f3a-817c-af6d91911858 | 3.70515 | -60.7584 | 2025-03-03 05:59:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 06602a40-ba36-3667-81bd-b11b7cb7aac9 | 2.76079 | -61.42344 | 2025-03-03 05:59:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6f143271-2d6f-3954-9a6a-4ac9c8c04d38 | 2.01814 | -61.43424 | 2025-03-03 05:59:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 7.6 |
| e7d12176-e3d6-3dd4-8ef4-ca93b32e3891 | 1.93863 | -60.40135 | 2025-03-03 05:59:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 8bb90b94-d5c4-303e-a44e-307f97d2de88 | 4.23299 | -59.84636 | 2025-03-03 05:59:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 60f39355-1142-334b-b6c1-5443d3eba94c | 1.93682 | -60.39027 | 2025-03-03 05:59:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 4.9 |
| e21a660b-4cad-35a4-be4d-9f2834830328 | 1.89135 | -60.39841 | 2025-03-03 05:59:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5a41c66e-aba9-33b3-af5f-73d2da7f6bf2 | 4.35089 | -60.34105 | 2025-03-03 05:59:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d620d987-05a5-3b19-a738-e67d9683ecf4 | 2.19493 | -61.33996 | 2025-03-03 05:59:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 46e0c124-f5a5-36d6-8f2e-017f3b4df54c | 3.52751 | -60.51962 | 2025-03-03 05:59:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 474af893-9574-3f0f-a834-d3f58e6bc5df | 2.11093 | -61.8131 | 2025-03-03 05:59:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cf9fc5b6-0058-354f-ab75-7fd309c1c3ce | 4.3499 | -60.34287 | 2025-03-03 05:59:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 69c064ae-ac7e-3e72-8974-7265e457548d | 2.00433 | -60.56055 | 2025-03-03 05:59:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 015ac91e-1229-34e7-b17f-c07be6dfedeb | 4.6485 | -60.84945 | 2025-03-03 05:59:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| db6f682a-347f-3218-be84-975ab8cd0159 | 3.2095 | -60.51552 | 2025-03-03 05:59:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 034e2108-9713-317c-ba11-d6fe8b97a9a3 | 3.21032 | -60.52062 | 2025-03-03 05:59:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d21a98e6-53d6-39c5-907e-e8ac8d87eff7 | 1.93775 | -60.39595 | 2025-03-03 05:59:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 4.9 |
| d14dae22-ae28-3a12-bec1-f469c0cae6db | 3.49794 | -60.13335 | 2025-03-03 05:59:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1a3bc51f-8072-3965-8a4a-72739bd91c8a | 3.20577 | -60.52382 | 2025-03-03 05:59:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8d00ebd4-85c2-3260-ad4f-cb5fbc2f1e7c | 0.91458 | -59.34752 | 2025-03-03 06:01:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ad04e09c-9c3a-3bcc-bb5b-41c331df1d0d | 0.9576 | -60.53156 | 2025-03-03 06:01:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a49a5cc7-83eb-3e7b-9d9d-0438aaa6c956 | 0.96253 | -60.53078 | 2025-03-03 06:01:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b9b31980-d49e-336d-9511-a6cc4af12380 | 0.81743 | -59.26948 | 2025-03-03 06:01:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0574368d-4d1e-3bfe-9b8a-6847070ab273 | 0.02737 | -60.668 | 2025-03-03 06:01:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d7b388e4-03e0-3438-84d3-ffede94e9aad | 0.02152 | -60.66319 | 2025-03-03 06:01:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 233a55ef-b6ec-3d09-8396-c76bed999f78 | 0.96116 | -60.53212 | 2025-03-03 06:01:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| caaaa9ae-0ee6-3cbe-8bc3-560561d2a60c | 0.96031 | -60.5266 | 2025-03-03 06:01:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c73346e3-e70e-3977-8e12-11f6a5ed31df | 0.82282 | -59.26861 | 2025-03-03 06:01:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2cc1e7bd-8e16-3b44-ba06-b93aceb23427 | 0.96746 | -60.52994 | 2025-03-03 06:01:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 56bc4f7e-e8e1-3f27-bdad-d7b5cf850e10 | 0.82336 | -59.27198 | 2025-03-03 06:01:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dd7d698e-a8c6-330a-b2c0-8f776b0f1a64 | 0.99779 | -59.43359 | 2025-03-03 06:01:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 68650b85-7b8e-3621-ac27-b6b1629c4529 | 0.65753 | -60.57818 | 2025-03-03 06:01:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6ae9f417-1f09-3678-aec4-28b0461f99c8 | 0.91512 | -59.35088 | 2025-03-03 06:01:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8d3861ed-f969-3bbc-aa55-6e47c927cf82 | 2.11179 | -61.81353 | 2025-03-03 06:22:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7e44e4f1-9b8d-35c1-ba34-2b3064f4c0ce | 1.89047 | -60.85785 | 2025-03-03 06:22:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b6a2c2e5-1dd6-33db-ac8c-b7b87af618e3 | 3.70746 | -60.76532 | 2025-03-03 06:22:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8095db82-9bfa-32d1-927b-308a33653bcf | 2.11278 | -61.81949 | 2025-03-03 06:22:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 210d203f-ae66-31e3-bcf0-e65ff4588e44 | 2.10953 | -61.81746 | 2025-03-03 06:22:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2681a13b-e86a-31bd-ad0f-b9d27abe06c2 | 2.11622 | -61.81648 | 2025-03-03 06:22:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ad91ce9a-c6bb-31cc-9fcf-739c45dcb5e1 | 3.70631 | -60.75878 | 2025-03-03 06:22:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ad3c1ae7-5194-3816-a308-b90d49c53a3c | 2.01293 | -61.43003 | 2025-03-03 06:22:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 579018be-4152-3665-8cc0-66a38e575786 | 2.01869 | -61.42255 | 2025-03-03 06:22:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 57984828-44f5-397b-b622-4d7603ef16b4 | 1.8886 | -60.8653 | 2025-03-03 06:22:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 29cecf9d-75e3-3c02-b3c1-226d5c511932 | 2.11727 | -61.82257 | 2025-03-03 06:22:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 533cf684-366d-37df-baf7-83bdc20c7540 | 2.01977 | -61.42899 | 2025-03-03 06:22:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7c3ad583-2f1f-3b89-95c7-28f879d1a32f | 2.11378 | -61.82552 | 2025-03-03 06:22:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a2cf5c1e-04cc-3881-92c1-24de21c0caaa | 1.89158 | -60.86465 | 2025-03-03 06:22:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8792b5f1-dc05-3c4c-a864-202c50c11c5a | 3.21293 | -60.52132 | 2025-03-03 06:22:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7a9fbae4-f080-362e-9b11-ab7b8d2f4bd4 | 2.02097 | -61.4361 | 2025-03-03 06:22:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9e511029-a6e0-35b5-b26f-713208dd3b3b | 2.11055 | -61.82335 | 2025-03-03 06:22:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 146efc07-5115-30dd-924f-e42ef1b7e50b | 3.20588 | -60.52261 | 2025-03-03 06:22:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e6373466-36bd-3efa-90e6-18a048afacb3 | 2.0112 | -61.42098 | 2025-03-03 06:58:00 | AQUA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 23d77d9b-4e73-3542-a752-86e4d2a09d49 | 3.6941 | -60.7543 | 2025-03-03 13:00:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 76.8 |
| 84e18b73-68ff-3e51-861c-231e046b3b8d | 3.2013 | -60.5168 | 2025-03-03 13:10:00 | GOES-16 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 69.6 |
| c89008e6-5acd-378c-a97a-22dbec7394df | 3.6941 | -60.7543 | 2025-03-03 13:10:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 10020d94-24dd-3cb8-8273-70e3f0d368ab | 3.6941 | -60.7543 | 2025-03-03 13:20:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 69.5 |
| c5e57334-9d8c-3bae-b7e1-489ef9aeda6f | 3.6941 | -60.7543 | 2025-03-03 13:30:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 8b6067bb-1392-3112-b2ac-3f47bb199b85 | 3.6941 | -60.7543 | 2025-03-03 13:40:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 72.1 |
| a47482f9-133e-3a54-979b-e885bbcd3015 | 3.6941 | -60.7543 | 2025-03-03 13:50:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 4c30fac4-a6d6-35ca-b957-1dfebe8a1e0a | 3.7124 | -60.7729 | 2025-03-03 13:50:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 2748e530-82bb-363c-aa1a-aa92b4ea48fe | 3.6941 | -60.7543 | 2025-03-03 14:00:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 2655786c-271e-3169-8b47-8a9482d28292 | 2.3988 | -59.9969 | 2025-03-03 14:10:00 | GOES-16 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 7858fc4b-f876-3589-80b4-d999ea287535 | 3.6941 | -60.7543 | 2025-03-03 14:10:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 6d291c68-83fa-3ef2-8756-752545f0a26e | 3.7124 | -60.754 | 2025-03-03 14:20:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 0570946c-ac9d-361e-a935-5a48a72de5cb | 3.6936 | -60.9628 | 2025-03-03 14:20:00 | GOES-16 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 77.6 |
| 25c161d3-052e-3da3-9327-4e5642197155 | 3.6941 | -60.7543 | 2025-03-03 14:20:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 76.6 |
| 00dafbd5-9110-352a-a0de-bc469511a76c | 3.7124 | -60.7729 | 2025-03-03 14:20:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 68.6 |
| e3cf3e69-3e7f-315d-ad77-7f57a4172d7a | 3.7876 | -60.0488 | 2025-03-03 14:30:00 | GOES-16 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 9aaeb63d-99b3-340a-8c36-88005cd50fd4 | 3.6936 | -60.9628 | 2025-03-03 14:30:00 | GOES-16 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 70.9 |


