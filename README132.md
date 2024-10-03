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

## Dados Diários - Página 132

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8513def3-33f9-3d52-9c82-5d57c68003d7 | -12.52963 | -53.25432 | 2024-10-03 04:51:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d2693a75-7c56-330c-9252-88402930023c | -12.52953 | -53.10796 | 2024-10-03 04:51:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a864c1a7-0fbc-3541-9ad9-b4d750b160d4 | -12.51381 | -53.46693 | 2024-10-03 04:51:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f3fe8ec8-f5b4-30aa-9331-3e58edca529d | -12.51048 | -53.46639 | 2024-10-03 04:51:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3fb93704-74e8-3787-ba5b-d233ec89b313 | -12.50714 | -53.46586 | 2024-10-03 04:51:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b46ebc3d-4653-3b91-97d7-88628882809e | -12.50675 | -53.18865 | 2024-10-03 04:51:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6a0cad27-d118-3d3e-bc43-a89d518ed440 | -12.50057 | -53.14002 | 2024-10-03 04:51:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| fffcb87b-3a05-3972-816b-8c7a0612d19b | -12.49832 | -53.52262 | 2024-10-03 04:51:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 186485c0-4cea-3106-975c-63071eef9c9f | -12.49778 | -53.1359 | 2024-10-03 04:51:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| bbfdeedd-e4bb-3a70-aa3e-1c4246c830b0 | -12.49723 | -53.13948 | 2024-10-03 04:51:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 3f69aac0-1b27-3cb0-86a7-4c8249fb8154 | -12.49667 | -53.14307 | 2024-10-03 04:51:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0af69537-7ff6-3753-af07-790f8cd7189f | -12.49554 | -53.51854 | 2024-10-03 04:51:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b4ee064f-1862-38cf-92a3-5064898a3a86 | -12.49499 | -53.52209 | 2024-10-03 04:51:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f321da3b-a3f4-383b-a248-88307631ab86 | -12.49444 | -53.52563 | 2024-10-03 04:51:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 80d09555-bd6e-35dc-a60d-55fd85be5243 | -12.49388 | -53.13895 | 2024-10-03 04:51:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 321bc1ec-8ce5-361b-990c-c3cd4caa3a95 | -12.49001 | -53.53218 | 2024-10-03 04:51:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| edc85b6b-096c-3e2b-bc9e-0a6f7f4662d8 | -12.48945 | -53.53572 | 2024-10-03 04:51:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 951e40e2-da2d-31f6-addc-51278c320dd3 | -12.48835 | -53.17472 | 2024-10-03 04:51:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c202f849-39aa-362c-88a6-9b48d5343bb0 | -12.48666 | -53.16347 | 2024-10-03 04:51:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 978e6c38-9126-3ceb-8d2b-dae454294d10 | -12.48611 | -53.16704 | 2024-10-03 04:51:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 87a103e4-c594-3822-a3bb-2b8b6e261528 | -12.48556 | -53.17062 | 2024-10-03 04:51:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 748bd15d-225b-301a-a31d-d507a6a07370 | -12.46857 | -53.45618 | 2024-10-03 04:51:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 828737da-2602-34ea-b36d-411268e872bf | -12.46524 | -53.45564 | 2024-10-03 04:51:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 58aa5480-cc46-3d49-ba13-2a465f9005ce | -12.45803 | -53.45811 | 2024-10-03 04:51:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0276e949-6813-32c4-a7a7-6ee6718a43b3 | -12.45469 | -53.45757 | 2024-10-03 04:51:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5b0f7f6f-cd76-313c-b350-6afa349b004b | -12.45414 | -53.46112 | 2024-10-03 04:51:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e57c3322-09fe-3ae4-afe6-1ade3226b05c | -12.45136 | -53.45703 | 2024-10-03 04:51:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a9646ade-bb7f-30d8-a6c0-0c5ea0fb136a | -6.87429 | -59.04023 | 2024-10-03 04:51:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3b609957-ad87-38a7-b519-1dc61b3af824 | -6.87355 | -59.04461 | 2024-10-03 04:51:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ee3d7694-990b-3e9f-8aeb-5d41613969ad | -6.87281 | -59.04897 | 2024-10-03 04:51:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6e7852ae-99a9-35cb-a2b4-30a17a33a992 | -6.87207 | -59.05333 | 2024-10-03 04:51:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6f8c90ad-c277-3208-86d1-eb21b4f12423 | -6.87136 | -59.03068 | 2024-10-03 04:51:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3e503625-9bd2-3b14-bcc5-739ce94a75a8 | -6.87061 | -59.03509 | 2024-10-03 04:51:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b769a032-2dec-3b6f-886e-8aad52cc2087 | -9.19441 | -58.19986 | 2024-10-03 04:51:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bd9b3ca5-df64-3cca-b307-932af4af523c | -9.19277 | -58.18502 | 2024-10-03 04:51:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8299e988-a911-3897-aa33-bcd3d8cde489 | -9.19217 | -58.18854 | 2024-10-03 04:51:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 96cefa2d-0150-3079-845d-e2727ff879c5 | -9.19157 | -58.19209 | 2024-10-03 04:51:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1c32b224-90cd-309b-b4c1-b303683e6365 | -9.19037 | -58.19917 | 2024-10-03 04:51:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c7fd2bc8-e46c-3cde-9f69-98ce8d94e151 | -9.18874 | -58.18435 | 2024-10-03 04:51:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 489394a6-5dd4-3426-9042-a7729269d1b7 | -9.18814 | -58.18787 | 2024-10-03 04:51:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9cae49a0-c39a-3743-b82f-f4b2e37e6b14 | -9.16911 | -59.37846 | 2024-10-03 04:51:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e34519b4-5252-339e-89db-a4057bd6648c | -9.16837 | -59.38266 | 2024-10-03 04:51:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d2bfcde0-4a8e-35ee-bfb9-59db302de06a | -9.16693 | -59.36524 | 2024-10-03 04:51:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cb38ab91-9601-3ff1-93bd-50beef3de540 | -9.16621 | -59.36936 | 2024-10-03 04:51:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a99ae4f0-30d4-3167-8ecd-20e08ae48e15 | -9.16548 | -59.37352 | 2024-10-03 04:51:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3a58a54a-f03e-3fbd-a2a1-8ac6cd0301a3 | -9.16475 | -59.3777 | 2024-10-03 04:51:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8f667ad8-622e-38b4-8f90-d5691441f642 | -9.16401 | -59.38189 | 2024-10-03 04:51:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f498abac-3da3-36e3-ab20-5b3c5e9aa9c8 | -9.16112 | -59.37278 | 2024-10-03 04:51:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3317185d-494a-325f-b842-f533f22c4374 | -9.16039 | -59.37694 | 2024-10-03 04:51:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1b95934e-374e-3c3f-904e-3ab53de80b4e | -9.02426 | -58.89352 | 2024-10-03 04:51:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8ded2bac-1006-3933-a7cc-14cf5cb40cfa | -9.02357 | -58.89749 | 2024-10-03 04:51:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9b093094-aac4-3f55-a84b-207671fb5d31 | -9.0124 | -58.91151 | 2024-10-03 04:51:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b0343359-abe8-32af-9bd6-b45b65c482bb | -9.01169 | -58.91558 | 2024-10-03 04:51:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7f68bbea-6191-3328-9247-059d04954f7e | -9.00813 | -58.91093 | 2024-10-03 04:51:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e02cbab7-7a33-38d9-b7d8-83c5d67f52c8 | -9.00743 | -58.91494 | 2024-10-03 04:51:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bec4ef72-91ac-354e-abf1-9805dd8a7043 | -9.74022 | -59.12803 | 2024-10-03 04:51:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1b8b4a1f-925b-3314-a38a-7adc816949cc | -9.54349 | -59.42399 | 2024-10-03 04:51:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9e833fa8-8425-3fd1-bc5f-60396524d84b | -9.51639 | -58.97715 | 2024-10-03 04:51:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6fcd33d0-aa18-38e2-9c34-94a854d63069 | -9.46861 | -58.97684 | 2024-10-03 04:51:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 52aacfe3-c7a8-3223-979e-36470e8b09c4 | -9.46508 | -58.97212 | 2024-10-03 04:51:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2499912f-d33e-3a48-b104-2b07ff400522 | -9.46439 | -58.97609 | 2024-10-03 04:51:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 5e7b136c-1423-3958-958c-bb7edbb52903 | -10.72503 | -58.51971 | 2024-10-03 04:51:00 | NPP-375D | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 560e9e45-a5eb-3872-9e9d-d6335385e98c | -10.7204 | -58.52254 | 2024-10-03 04:51:00 | NPP-375D | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c7f06bf0-594d-39a6-9b7a-e2791432e1b2 | -10.71978 | -58.52608 | 2024-10-03 04:51:00 | NPP-375D | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 38ca28b3-e03e-3247-af6f-3fe2816b9c95 | -10.71577 | -58.52538 | 2024-10-03 04:51:00 | NPP-375D | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b38b8873-2285-310f-a529-4d4ed2816648 | -10.71112 | -58.52823 | 2024-10-03 04:51:00 | NPP-375D | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7d254558-c9f9-3441-a959-8fc7e856594d | -10.7034 | -58.54871 | 2024-10-03 04:51:00 | NPP-375D | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 68017b22-5a93-3c44-90b1-457a952b6ff9 | -10.70278 | -58.55225 | 2024-10-03 04:51:00 | NPP-375D | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| def3d8d9-7f36-3fe3-86e4-47c4d094148e | -10.70215 | -58.55581 | 2024-10-03 04:51:00 | NPP-375D | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b441891d-e63c-3d42-9382-5b8e80f1722b | -10.70153 | -58.5594 | 2024-10-03 04:51:00 | NPP-375D | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 61a94b66-aab7-3173-aef8-15a1c2cd5fa8 | -10.7009 | -58.56298 | 2024-10-03 04:51:00 | NPP-375D | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4a152c39-120d-39be-9592-cfc66f75e9ff | -10.70027 | -58.56656 | 2024-10-03 04:51:00 | NPP-375D | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4dc9da6e-6812-3d93-bc6f-a34816f238f0 | -10.69965 | -58.57013 | 2024-10-03 04:51:00 | NPP-375D | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9c541c91-8362-3e60-b023-479385977fd6 | -10.69877 | -58.55147 | 2024-10-03 04:51:00 | NPP-375D | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 99bbd7e3-c2d2-3801-ac8a-d0dffc6f17af | -10.69814 | -58.55502 | 2024-10-03 04:51:00 | NPP-375D | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f1070b5e-36b8-313e-8a75-c9483bf55b56 | -10.69659 | -58.54023 | 2024-10-03 04:51:00 | NPP-375D | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e099d1b1-99ae-30de-bd39-69672f7812a7 | -10.69598 | -58.54368 | 2024-10-03 04:51:00 | NPP-375D | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b085eceb-1661-3cf2-9e4a-2ac9f1ad5991 | -10.69257 | -58.53952 | 2024-10-03 04:51:00 | NPP-375D | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2599b62f-7274-30d7-8686-eb1c1797cd23 | -12.32034 | -59.22831 | 2024-10-03 04:51:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 73ab96a9-6b66-3ff6-9f56-cf3f45498798 | -12.3072 | -59.18375 | 2024-10-03 04:51:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 525a9f7e-27fe-32b4-ae66-82d5b0ecbe05 | -12.30655 | -59.18739 | 2024-10-03 04:51:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 50d33454-3505-3d90-9153-5e96353ed291 | -12.30311 | -59.18304 | 2024-10-03 04:51:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9ee02986-6c02-389c-9e48-193abc4ff40d | -12.29967 | -59.17872 | 2024-10-03 04:51:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 066d3482-4f7c-315d-bd28-a647c59ea2eb | -12.29902 | -59.18235 | 2024-10-03 04:51:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b690764a-10c9-35f8-acd7-0fa34d08291c | -11.72474 | -59.13667 | 2024-10-03 04:51:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1c4f0d7f-deb0-3166-8fba-c76e86d05d3c | -10.95128 | -58.96381 | 2024-10-03 04:51:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 44cb18dd-984d-3a50-953f-816340def906 | -12.95007 | -60.10144 | 2024-10-03 04:51:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6321fc0e-751a-3b44-b46d-d7cf46f28c39 | -13.77104 | -60.06828 | 2024-10-03 04:51:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8e28026e-425c-383a-bb1d-15bb8a004722 | -7.46237 | -60.4075 | 2024-10-03 04:51:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5d9a88b8-c9dd-30b5-a65e-c1692fb990e8 | -7.20095 | -59.7935 | 2024-10-03 04:51:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 13e75a3b-3a11-388f-9db8-7cfb6d35b9cb | -7.19632 | -59.79271 | 2024-10-03 04:51:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 4ab8c8af-2726-3430-ba99-7eea91195852 | -7.0182 | -59.38123 | 2024-10-03 04:51:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0ec67555-2249-3c86-847d-5840795a1280 | -7.01744 | -59.3857 | 2024-10-03 04:51:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 74272cb3-a8c8-3108-ba97-862a72a7d1f5 | -6.71476 | -59.12695 | 2024-10-03 04:51:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7c7f91ea-5ddc-3984-b027-a0ea975efc79 | -6.714 | -59.13137 | 2024-10-03 04:51:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3880b32b-322f-393e-bb68-1eb290e629aa | -6.70955 | -59.13052 | 2024-10-03 04:51:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0b0c1efc-0219-39bf-846a-14612a74d936 | -6.70879 | -59.13496 | 2024-10-03 04:51:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| dcb84ab3-944e-3226-bf49-d07d90aa06b5 | -6.6489 | -60.04615 | 2024-10-03 04:51:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 16ea4ce9-4f94-32cc-bd92-edea6e5de2a0 | -6.64801 | -60.05124 | 2024-10-03 04:51:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 615a1809-e561-3c3b-ba5b-9f1b7e48f459 | -9.9315 | -59.93139 | 2024-10-03 04:51:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |


[Clique aqui para ver as próximas entradas](README133.md)
