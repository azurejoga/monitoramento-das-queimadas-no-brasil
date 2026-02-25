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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 77245fa7-685b-3aef-a95e-b4e6b6946772 | 2.72258 | -60.23786 | 2026-02-25 05:54:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6cfb44f6-1d62-332c-8296-21c0ba094a7b | 1.49986 | -59.93434 | 2026-02-25 05:54:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 13.5 |
| c49043b6-d55b-3656-bf90-7fe56ce88874 | 1.48223 | -59.91286 | 2026-02-25 05:54:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 32e63708-2dec-3406-87ab-5c02dc74cf14 | 1.50749 | -59.92352 | 2026-02-25 05:54:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 33e97a43-3f6d-37cf-9d8d-c71c4692fcfd | 1.51658 | -59.95052 | 2026-02-25 05:54:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ae36e6cd-d9c4-33c7-a44d-51206c938dda | 1.49302 | -59.95058 | 2026-02-25 05:54:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 30.4 |
| a2666622-46ea-395e-bcec-4d048f092f71 | 3.45201 | -59.90095 | 2026-02-25 05:54:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 42c25512-45e0-353a-a54d-334b9a0857b9 | 1.63495 | -60.28408 | 2026-02-25 05:54:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f562bc1e-fdc3-3417-8302-68fc79df30be | 1.48302 | -59.91765 | 2026-02-25 05:54:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1e03e00d-affa-3b6f-a965-a0b39bbdf3fc | 1.49158 | -59.94136 | 2026-02-25 05:54:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 26.0 |
| f385b987-9871-30be-b42f-0b189986eb88 | 3.44535 | -59.88844 | 2026-02-25 05:54:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c8e0a4b7-0d3d-3078-ae32-85a6072ebf84 | 2.87579 | -60.26384 | 2026-02-25 05:54:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8273e6d6-1669-3dd6-84c9-f1e36b4f19c8 | 1.49223 | -59.94498 | 2026-02-25 05:54:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 38.3 |
| af28c9e9-d831-3575-a931-86f5dbd504a4 | 1.48389 | -59.95211 | 2026-02-25 05:54:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 239e2f90-70d8-385c-8b4b-83b9c66f97fa | 2.23777 | -60.70152 | 2026-02-25 05:54:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 954b7e87-2277-3ee3-8399-c84947f4357d | 1.50518 | -59.93815 | 2026-02-25 05:54:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 0dcbcc94-7047-32a7-839e-643fc25f3c5c | 1.49218 | -59.91615 | 2026-02-25 05:54:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2ecf7ce0-2d73-3267-a1b5-8012a75f9efa | 1.49148 | -59.94045 | 2026-02-25 05:54:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 48.5 |
| b4245f03-8920-3240-9773-579fda887131 | 1.48765 | -59.9457 | 2026-02-25 05:54:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 8ee28bf8-e701-30a9-ab43-01f1d3cfd1ff | 1.49067 | -59.90698 | 2026-02-25 05:54:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0488dddf-bc88-38ec-bdc8-9fd2356d3f26 | 1.94061 | -60.36488 | 2026-02-25 05:54:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 93498e74-873f-3690-aa6a-5d7d28a42246 | 1.51506 | -59.94119 | 2026-02-25 05:54:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 0e09590e-8519-30b5-b64b-36c1770826e8 | 1.51582 | -59.94587 | 2026-02-25 05:54:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 71ae80d5-28e8-323e-96fa-b2b36b3bc580 | 1.36548 | -60.29507 | 2026-02-25 05:54:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 4864b7c5-0125-3eb0-88b6-51937e31d696 | 1.48146 | -59.90818 | 2026-02-25 05:54:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cbac17b6-957a-34c2-ab7f-8fefeebbe2b3 | 1.93842 | -60.86167 | 2026-02-25 05:54:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 645f5a11-821d-33e2-aa14-5fbb0d9a07af | 1.51963 | -59.94041 | 2026-02-25 05:54:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ebffbb58-0044-38fb-84cd-4324ca0b85d4 | 1.48682 | -59.91214 | 2026-02-25 05:54:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 08a2280e-ea5a-3d4b-b6c2-3683cb13c7e3 | 1.48643 | -59.90849 | 2026-02-25 05:54:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 58fcb048-3036-3bf8-b3ef-a753b0d514b8 | 1.50745 | -59.95202 | 2026-02-25 05:54:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 8cd68fbe-1eae-3f30-b53c-d211ca396e07 | 1.4968 | -59.94424 | 2026-02-25 05:54:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 38.3 |
| 46946698-1439-38ca-ba59-aa7b4fe90e92 | 1.48331 | -59.91857 | 2026-02-25 05:54:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8319dacd-6b30-3ca6-a4b7-5bdbb5cbdac7 | 2.23713 | -60.69753 | 2026-02-25 05:54:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4b76fb77-bd98-3c3a-ae8a-21d7493ef201 | 1.94013 | -60.84494 | 2026-02-25 05:54:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 203266bc-c35d-32c5-bb79-27ac8bf3586c | 1.48463 | -59.95682 | 2026-02-25 05:54:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 11.0 |
| afb08ae8-5d78-3ce5-b3e6-df51bbdb6c5b | 2.71559 | -60.24881 | 2026-02-25 05:54:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4d71b9b4-3dd9-3449-b978-af59c6c38a8a | 1.93551 | -60.36131 | 2026-02-25 05:54:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f1e6960b-8d47-302e-b48e-8ec8ae1687f4 | 2.23285 | -60.69822 | 2026-02-25 05:54:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f47160b2-77ad-39c0-802d-cba7174bea47 | 1.35474 | -60.05567 | 2026-02-25 05:54:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 75d63ca2-819b-360f-ad06-84ddb6e120b1 | 2.72294 | -60.23887 | 2026-02-25 05:54:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3e39f3ee-7cf3-3f8c-a598-b06b756add63 | 1.47933 | -59.95289 | 2026-02-25 05:54:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 9e97e08b-83fe-342d-bf90-f573bdc24bbb | 1.48863 | -59.92253 | 2026-02-25 05:54:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d226e085-16fd-3aec-a291-42e1844b2095 | 1.49832 | -59.92491 | 2026-02-25 05:54:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9f6a3a4b-7336-3ccb-a2ad-5fbc19cf7add | 1.94502 | -60.36417 | 2026-02-25 05:54:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| db21413e-3439-3bb2-aa08-7fa306f9f06c | 1.48608 | -59.90764 | 2026-02-25 05:54:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e10e020d-35fc-3b30-9478-816dffa2cfaf | 1.50291 | -59.92425 | 2026-02-25 05:54:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c547496d-7603-3499-9b1f-4302b0f42162 | 3.13709 | -59.98769 | 2026-02-25 05:54:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b56572d3-0a26-3f31-aed6-dbf2750df233 | 2.2292 | -60.70295 | 2026-02-25 05:54:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ce2cf0ec-caef-3e6e-ad5a-2033ccecf964 | 1.50597 | -59.91426 | 2026-02-25 05:54:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 544fac17-5c53-3289-98c3-93388042bdd0 | 1.49013 | -59.93209 | 2026-02-25 05:54:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 57deffce-df17-3c46-a57f-369723d14eec | 1.49756 | -59.94886 | 2026-02-25 05:54:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 38.3 |
| 9d0691ba-ede9-3273-9eca-556f0076512e | 1.49299 | -59.94962 | 2026-02-25 05:54:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 38.3 |
| 267abb4e-0806-351f-8292-e1b3740fa4e4 | 3.45054 | -59.89214 | 2026-02-25 05:54:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 51565dc0-2332-3004-8391-e161569a0099 | 1.94806 | -60.35492 | 2026-02-25 05:54:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d62ef50f-1f3f-3b53-b4a6-79befa865956 | 1.48788 | -59.91777 | 2026-02-25 05:54:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5c79229e-a04d-3755-a0f6-3ea15eb4ce85 | 1.49911 | -59.92972 | 2026-02-25 05:54:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 836e7bd8-8f3a-3b9c-8d32-e0322972cf3f | 1.48381 | -59.92242 | 2026-02-25 05:54:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7fb98ba6-d5e3-3560-b9f6-44e027118cb3 | 1.49753 | -59.92011 | 2026-02-25 05:54:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 434995ca-7467-3cea-a87d-ca0415837682 | 1.49605 | -59.93968 | 2026-02-25 05:54:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 48.5 |
| b2264369-c69f-3ee3-bbbe-ed85c410017c | 3.49918 | -60.29037 | 2026-02-25 05:54:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 04fcf611-f8ee-3763-8769-3041f4c59ff4 | 1.93109 | -60.36199 | 2026-02-25 05:54:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e3289687-c107-389d-8010-f06034bc94f3 | 3.44904 | -59.91046 | 2026-02-25 05:54:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 4.2 |
| e409bef3-1a41-3de9-beec-a325b1abd7a7 | 1.49229 | -59.94592 | 2026-02-25 05:54:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 26.0 |
| eb7ed7a2-71c7-3eb9-960d-9835ef92a181 | 1.50212 | -59.94811 | 2026-02-25 05:54:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 470aac57-534a-36f7-b770-dbaaea732837 | 1.88161 | -60.91553 | 2026-02-25 05:54:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 31c3fffb-427a-3b6f-8e5f-08f835396ee5 | 1.50212 | -59.91947 | 2026-02-25 05:54:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 59b5b074-f1b7-348c-882b-a22362e237c8 | 1.51812 | -59.93118 | 2026-02-25 05:54:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9d6d3d7b-68fc-3e63-b194-503a5ceb475f | 1.88096 | -60.91158 | 2026-02-25 05:54:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 17ca240a-e9cb-3624-b83a-2384f81d02e6 | 3.05249 | -60.88772 | 2026-02-25 05:54:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ccec5a49-8b04-32b4-953b-6c8d7ff89965 | 2.71201 | -60.22747 | 2026-02-25 05:54:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ab4caf5c-0fd8-330d-8df4-9c65d92e3cd0 | 3.49417 | -60.28696 | 2026-02-25 05:54:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8381a4b5-3b3f-3e26-8647-5177cd33b247 | 1.94364 | -60.35562 | 2026-02-25 05:54:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 932c1a0f-96ca-38c9-88c6-1ba40b51e0b8 | 1.94141 | -60.85298 | 2026-02-25 05:54:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a12b06f1-9e37-37d9-a7c9-d049631e1115 | 1.93778 | -60.85765 | 2026-02-25 05:54:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c3d8323e-2423-3f69-9895-7761da553225 | 3.45127 | -59.89654 | 2026-02-25 05:54:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0bd63ba5-677c-36f0-af9d-17ed4d25a6e0 | 1.50672 | -59.91885 | 2026-02-25 05:54:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a2101501-7fc7-3174-aaf0-a93cc45d8de3 | 1.93714 | -60.85363 | 2026-02-25 05:54:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aecb4654-138b-35f5-b95a-98c0fe50425d | 1.4876 | -59.91687 | 2026-02-25 05:54:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c59957f8-66ac-3d21-aef7-d2f04a06c223 | 1.50061 | -59.93892 | 2026-02-25 05:54:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 8c2a49be-5795-38c8-bd4a-c455ec311d0c | 3.63013 | -60.65933 | 2026-02-25 05:54:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 964b202b-4e43-3b37-b05c-1bb2c58af158 | 1.49295 | -59.92085 | 2026-02-25 05:54:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 79de5137-7e1d-3e61-bb7e-34d287f9d9ee | 1.5037 | -59.92908 | 2026-02-25 05:54:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 8ebb1d68-745b-30b2-ba95-e60ccb04af8b | 1.48938 | -59.92734 | 2026-02-25 05:54:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c43f9782-b32b-3d61-a4ac-9be8ec126106 | 1.3662 | -60.29951 | 2026-02-25 05:54:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 6.3 |
| ddd6d0d5-e5f9-30c9-8552-a345917c9dea | 1.48995 | -59.93116 | 2026-02-25 05:54:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 8405ab1d-05cc-3e4b-a6d4-5a249db47306 | 1.48714 | -59.91303 | 2026-02-25 05:54:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a630296d-efa4-3c6d-bbc7-b60c3a508fbf | 1.5143 | -59.93655 | 2026-02-25 05:54:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 59e86206-3a2e-3c3e-aa97-ade1ad2c3885 | 3.4483 | -59.90607 | 2026-02-25 05:54:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 8d473e5c-0b9f-3c5b-9702-09fd6ce2bbbb | 1.48256 | -59.91377 | 2026-02-25 05:54:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bff6de64-ddb6-35b0-bfe7-14aa13a32616 | 1.31175 | -60.40556 | 2026-02-25 05:54:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 533c72cf-6b06-336b-8ce2-8cca51ae099c | 1.50825 | -59.92822 | 2026-02-25 05:54:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 59092529-e90c-388a-ba2a-b17fb81e7c54 | 1.36907 | -60.31726 | 2026-02-25 05:54:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 23ac244b-e915-3439-8e0d-9c2393b96f5d | 3.62949 | -60.65544 | 2026-02-25 05:54:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 87f5b088-3d3b-3afc-8634-6cf41f1a465a | 1.48842 | -59.95035 | 2026-02-25 05:54:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 10.5 |
| a2066c0a-a48a-3f46-ae86-0a76cf3830a0 | 1.49142 | -59.91152 | 2026-02-25 05:54:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0d05274b-24a7-3706-ad87-3e92f888d22c | 1.48838 | -59.9216 | 2026-02-25 05:54:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 397be80f-47d2-3088-9d83-0c6a606e87bb | 1.88521 | -60.91086 | 2026-02-25 05:54:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 57054893-9737-352d-a19b-2954cd98d354 | 1.4846 | -59.9272 | 2026-02-25 05:54:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 58b3aa8b-35b1-31ac-a7bb-091c480c9bec | 2.23348 | -60.70223 | 2026-02-25 05:54:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 59c3ef91-f4ca-3a63-bad3-7770711bfa04 | 1.9365 | -60.84963 | 2026-02-25 05:54:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README9.md)
