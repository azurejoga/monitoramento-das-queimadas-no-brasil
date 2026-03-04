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
| 31376ffc-a453-3af2-ad19-ce00bf3b1add | 2.66736 | -60.41478 | 2026-03-04 05:22:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 442713d5-0fa1-3411-90f1-516f70cbcd55 | 2.91551 | -60.45219 | 2026-03-04 05:22:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b62cf2e6-d6e9-3275-b236-e9fe41edd6c0 | 1.5092 | -59.92433 | 2026-03-04 05:22:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e3bfbd7b-36a6-3352-82a0-31b558ae1108 | -2.33268 | -60.06696 | 2026-03-04 05:22:00 | NOAA-20 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2b907342-4229-39ab-a1c2-fe58383196ab | 1.48701 | -59.91349 | 2026-03-04 05:22:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7c87613b-d7e1-3719-be4a-932b84cf0b84 | 4.18391 | -60.38136 | 2026-03-04 05:22:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 83ba2f2d-fc53-3ed8-bc55-0b119fbac3f8 | 4.6465 | -60.697 | 2026-03-04 05:22:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a392a891-d86e-364b-9e75-4d34d4d20f51 | 2.95203 | -61.09129 | 2026-03-04 05:22:00 | NOAA-20 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 87ac5d51-2bf9-3edd-b6ab-22747eed0723 | 2.22514 | -60.74578 | 2026-03-04 05:22:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7a25822b-52a9-3ce5-8894-09b8c50ab5be | 1.94549 | -60.81826 | 2026-03-04 05:22:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3577b59c-5a6c-3a59-8603-fb781e728ee8 | 1.49034 | -59.91296 | 2026-03-04 05:22:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 70ba387f-89b6-3871-830b-eb3959564685 | 2.91266 | -60.4338 | 2026-03-04 05:22:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 5c4e3d9a-0524-38ff-81b2-d94ae9b47318 | 1.49977 | -59.90788 | 2026-03-04 05:22:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5b9427c1-de79-3983-a5d6-05e8c6abd59c | 1.5103 | -59.90977 | 2026-03-04 05:22:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 22.7 |
| 8b4472cd-aa50-38a0-8238-a9eab66ccd77 | 4.18352 | -60.40128 | 2026-03-04 05:22:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b2cba997-0e91-396d-858f-fc44f3bf8280 | 2.6548 | -60.10593 | 2026-03-04 05:22:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2ee25b19-670e-3216-8771-bae5aa5d53e6 | 3.03347 | -60.64657 | 2026-03-04 05:22:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2724ffc6-3880-337b-b05a-ede167e27c3a | -0.62684 | -67.15051 | 2026-03-04 05:22:00 | NOAA-20 | SÃO GABRIEL DA CACHOEIRA | AMAZONAS | Brasil | 1303809 | 13 | 33 | nan | nan | nan | Amazônia | 0.2 |
| c234f892-564b-32a6-b94a-c1e057694f48 | 2.58842 | -60.60389 | 2026-03-04 05:22:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5ddcfb60-127d-35e8-aeff-c22d2b9e7172 | 1.50809 | -59.91732 | 2026-03-04 05:22:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 7fef4a9a-fed8-39e8-bb9b-6a39cbcb203b | 2.68226 | -60.41658 | 2026-03-04 05:22:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 97742033-8431-3429-a80d-c9fa0ad72706 | 1.83088 | -60.84708 | 2026-03-04 05:22:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| eea3f656-4b9c-3d52-a3e2-8db95e99e9ef | -0.50664 | -64.60914 | 2026-03-04 05:22:00 | NOAA-20 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 84d88c0f-48e6-3d2b-a74b-5f3431c8228c | 2.91665 | -60.45956 | 2026-03-04 05:22:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f33f993f-3eb0-3775-ac03-a349714de1f6 | 1.96083 | -60.51158 | 2026-03-04 05:22:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0b375d5e-b15e-3789-b6f6-938db36a0795 | -3.04453 | -59.08823 | 2026-03-04 05:22:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2ee98bde-7758-3a5f-bd70-2a39d6c5a11e | 2.91608 | -60.45588 | 2026-03-04 05:22:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 11480047-0f02-3c18-8a40-33cb804098ec | 4.18052 | -60.38217 | 2026-03-04 05:22:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 06ca1a30-364a-3c13-b238-78f0c05cccb7 | 1.497 | -59.91191 | 2026-03-04 05:22:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5437dc57-1c97-34dd-b507-15635e910831 | 1.50032 | -59.91138 | 2026-03-04 05:22:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4b4db5bc-ac15-3748-bf53-0f7630a2a5e9 | 1.51198 | -59.9203 | 2026-03-04 05:22:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6605827b-f274-31cf-bdc9-5b8f8ae96854 | 1.50421 | -59.91435 | 2026-03-04 05:22:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 37039c4d-c9d5-307f-b0af-7de21f13bd22 | 1.61022 | -60.24501 | 2026-03-04 05:22:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a141c1de-242b-3486-ba74-42575c657c06 | 1.01218 | -59.51186 | 2026-03-04 05:25:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9b1178ad-7a63-3b5e-9273-45229bc793da | 0.73466 | -59.90597 | 2026-03-04 05:25:00 | NOAA-20 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 450e456a-e430-3fcc-a83a-2926a4b3973f | 0.0878 | -60.6265 | 2026-03-04 05:25:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 13cfd384-29b8-3465-b752-96b163ca35a0 | -8.84644 | -59.7226 | 2026-03-04 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.2 |
| a260a970-6a75-3474-9b8c-cdd899a663e4 | -6.55029 | -67.79591 | 2026-03-04 05:25:00 | NOAA-20 | ITAMARATI | AMAZONAS | Brasil | 1301951 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c68fd653-a70d-33d3-9a61-ff4f5c0be938 | 0.07479 | -60.54465 | 2026-03-04 05:25:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0f3e8307-84a3-3b06-9610-c57e098c5dfa | 1.02291 | -60.54833 | 2026-03-04 05:25:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8a1eee17-10f7-3962-8eb0-dfcdc3ca6f26 | 1.21474 | -59.97722 | 2026-03-04 05:25:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 551f9d4c-efdc-3050-9f5e-fa6dcccf3c0b | 0.89626 | -60.09203 | 2026-03-04 05:25:00 | NOAA-20 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8dfc5ab1-2d35-38c4-b7a6-98b381c65cfc | 0.05579 | -60.5549 | 2026-03-04 05:25:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 53eae2fc-9018-35e1-881c-638610abc464 | 0.92519 | -60.50819 | 2026-03-04 05:25:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 78717f68-d79b-3902-b245-75b29346bfcb | 0.95841 | -60.22634 | 2026-03-04 05:25:00 | NOAA-20 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c5af9a04-d5d5-3693-8143-a76b024a3e54 | 1.35797 | -60.06697 | 2026-03-04 05:25:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| be6b6034-cb64-359f-aabc-6c615e1d9d80 | 1.10889 | -59.19726 | 2026-03-04 05:25:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2323454a-7010-3179-9454-d2ccd5221f6e | 1.10998 | -59.20411 | 2026-03-04 05:25:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ac17fe6d-3c33-3956-94b3-bbba8fe3d3ae | 1.12681 | -60.51726 | 2026-03-04 05:25:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 127f6f59-f84b-38f2-875b-48ff3e2b8df9 | 1.15048 | -60.84481 | 2026-03-04 05:25:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6954462a-d3ee-3f70-acc0-fc23fb2af3fa | 0.05508 | -60.98997 | 2026-03-04 05:25:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cc43c2d1-7792-357e-9635-252c8364519d | 0.76068 | -59.89865 | 2026-03-04 05:25:00 | NOAA-20 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 033835c0-8849-3247-835e-ea51eb2060b3 | 1.06314 | -59.4897 | 2026-03-04 05:25:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 101ffea1-a8dc-3f03-969f-4828ccb8f81e | 1.06038 | -59.49365 | 2026-03-04 05:25:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 70166263-93fc-3d73-967e-611848edcaec | 0.96399 | -60.23999 | 2026-03-04 05:25:00 | NOAA-20 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0f2271c9-a61d-380a-ac3d-334018c99f18 | 0.05563 | -60.97122 | 2026-03-04 05:25:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 4.7 |
| fb4f4695-a951-3840-8d40-49c3bde4b548 | 0.15176 | -60.49646 | 2026-03-04 05:25:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ceddd2a4-9fea-3d40-93ee-e0bf4e305ada | 1.02234 | -60.54473 | 2026-03-04 05:25:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| aab5833e-d10d-321e-aa38-ee0bdbdc2765 | 0.49101 | -60.51306 | 2026-03-04 05:25:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d0c945b5-71a0-3d83-b35a-de6cae068a25 | 0.05959 | -60.97432 | 2026-03-04 05:25:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d1e39465-a6f6-3d7f-8e73-c6fab15b8163 | 0.03948 | -60.98496 | 2026-03-04 05:25:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 4a019824-a53f-3214-aa8a-2d47b974ed0a | -6.96311 | -52.74693 | 2026-03-04 05:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| e8d1c0ab-cf50-3e82-b95d-273ad3c307a9 | 0.30989 | -60.44691 | 2026-03-04 05:25:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 11cd17e9-c8b3-3505-9534-54fac2e5613c | 1.34745 | -60.02181 | 2026-03-04 05:25:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 0464fd4f-6ae8-3916-9c28-1eb8eacd4a97 | 0.05565 | -60.99365 | 2026-03-04 05:25:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f97034ff-cf87-3a73-ab73-bde8e73cb3fe | 1.07961 | -59.25139 | 2026-03-04 05:25:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 9b9dd3ba-fdfa-349f-8f2a-90acdb10e9b8 | -5.14877 | -60.37432 | 2026-03-04 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1434736f-360e-326a-aa38-10031e91de57 | 0.05393 | -60.98263 | 2026-03-04 05:25:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 5.1 |
| de15ed23-c470-3a5e-9854-8087a924bda0 | 0.04229 | -60.98078 | 2026-03-04 05:25:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 20a1b509-4c7d-31dc-a793-712674ccb9fe | 0.06188 | -60.98891 | 2026-03-04 05:25:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f006ba65-8a9d-3cf1-9baa-89d5a5efe324 | 0.49826 | -60.49368 | 2026-03-04 05:25:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3547bd03-50bf-3236-89be-3dd76bdb8c30 | 0.05247 | -60.97913 | 2026-03-04 05:25:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 48.2 |
| c02a3d87-0fdd-358e-9a77-79a51128d5bb | 0.09116 | -60.62598 | 2026-03-04 05:25:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 779ea3a5-8c06-3561-8ac8-67316609d127 | 0.58171 | -59.84099 | 2026-03-04 05:25:00 | NOAA-20 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 37fe0c94-cb33-32e6-811a-c65d7cc8eb43 | 0.27989 | -60.6185 | 2026-03-04 05:25:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 5e78b93d-d1e7-3618-8055-59fe2b6b3a0f | 0.30933 | -60.44337 | 2026-03-04 05:25:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0f52bd3b-2e4c-31c8-9c7b-9ff807ac9efa | 0.04908 | -60.97969 | 2026-03-04 05:25:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 48.2 |
| b56d1b78-ea5d-3a68-ba99-f03a1821619c | 1.00673 | -59.47746 | 2026-03-04 05:25:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e0ce18cd-40ac-33de-a07c-e4fbf183b98b | 0.93492 | -60.31705 | 2026-03-04 05:25:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3c395df3-3dd9-39b9-95d4-3bebc03e93f7 | 0.16404 | -60.48727 | 2026-03-04 05:25:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ad2feb06-0593-338b-90c0-9ffbc74c8fb9 | 0.05905 | -60.99312 | 2026-03-04 05:25:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6fd806e3-acf5-30a2-bdd0-ab7974fae92b | 0.1703 | -60.59188 | 2026-03-04 05:25:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 96602373-89ac-37f4-9e4f-c65f3b293fb0 | 0.04404 | -60.99173 | 2026-03-04 05:25:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 32.8 |
| c1f228e7-01f7-39f7-b7a7-a3e23dc925ac | 1.11382 | -59.20702 | 2026-03-04 05:25:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2e2eb5ec-15f4-3164-9de6-68504b3cf935 | 0.69526 | -59.61452 | 2026-03-04 05:25:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8dfd582c-1e17-3107-8a9a-91d0042e5bec | 0.30095 | -60.45558 | 2026-03-04 05:25:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8c5161b0-fb53-3a03-913d-46879fac14ab | 0.80056 | -59.87107 | 2026-03-04 05:25:00 | NOAA-20 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 236c1284-a3f2-396b-9c53-b7f1cc8f7c58 | 0.05336 | -60.97897 | 2026-03-04 05:25:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 5.1 |
| bf936b43-4fa5-3e52-9a96-116a79262b71 | 1.00564 | -59.47057 | 2026-03-04 05:25:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0e4149da-f4d3-3156-8265-2200c3546734 | 0.49324 | -60.50539 | 2026-03-04 05:25:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8c1bdd18-597e-32ad-8b46-8b2f015eb00f | 0.49773 | -60.51199 | 2026-03-04 05:25:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b3029185-c6fe-31b3-a99a-c3031475bd6a | 0.94788 | -59.4479 | 2026-03-04 05:25:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1303411a-efdc-3479-ae1e-b47c0928f47c | 0.30765 | -60.45453 | 2026-03-04 05:25:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 715f69f7-6791-3377-85cd-5c84a12a807a | 0.91725 | -60.43624 | 2026-03-04 05:25:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 39138ebe-acc5-37f1-86d1-0aef054d31f3 | 0.04966 | -60.98334 | 2026-03-04 05:25:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 48.2 |
| d59bf7b2-db28-3e89-af71-a412336dd30d | 1.14941 | -60.88266 | 2026-03-04 05:25:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b24aa239-169c-3db1-a191-b566db96f5bc | -9.79466 | -54.20404 | 2026-03-04 05:25:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| aae86bf3-6eb5-3e80-82cf-cdc0b72ac287 | 0.49493 | -60.51608 | 2026-03-04 05:25:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dc5d2a1d-5239-3968-a894-1c8be52181b9 | 1.05927 | -59.25105 | 2026-03-04 05:25:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7280a161-fcb3-3bfe-aac8-ad4ae35f103d | 0.0562 | -60.97483 | 2026-03-04 05:25:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 4.7 |


[Clique aqui para ver as próximas entradas](README9.md)
