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

## Dados Diários - Página 58

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 38276b88-d570-3553-bda2-57793985fd8b | -4.33137 | -48.63362 | 2024-10-25 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 56cf2681-597d-3ff7-91ee-da753aaca006 | -4.33082 | -48.63708 | 2024-10-25 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| de69466c-2158-39bd-bcc3-533ed05aef02 | -4.33028 | -48.64053 | 2024-10-25 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| ae9d694e-0564-3ca7-9bff-b0ad33dd5d28 | -4.32859 | -48.62964 | 2024-10-25 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| b4760a68-480c-3ce4-be84-3edba27010ef | -4.32804 | -48.6331 | 2024-10-25 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 0d00f4eb-04a0-3bcf-9d44-36fcb967ec83 | -4.3275 | -48.63656 | 2024-10-25 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 46c06422-365d-3b33-b414-a40950eb154f | -4.29646 | -48.61755 | 2024-10-25 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 30af6339-fef3-3a43-825d-02c44677d541 | -4.2926 | -48.62049 | 2024-10-25 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 4d1fee02-27ae-36aa-8e0a-090e1e86acb2 | -4.29205 | -48.62395 | 2024-10-25 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 8c60d504-a1cc-31f7-af57-44d91ad0c08a | -4.28866 | -48.60221 | 2024-10-25 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| fe39b86b-3b4d-3337-afe2-e75861734d18 | -4.28541 | -48.62291 | 2024-10-25 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b880681a-3609-38d0-8e95-2f6c1c825c63 | -4.27931 | -48.61842 | 2024-10-25 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 539032e4-5efe-3ecc-a0a2-cac1cc06ec01 | -4.27219 | -48.6421 | 2024-10-25 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 720d491b-24dd-3289-abab-125538712af9 | -4.26874 | -48.5991 | 2024-10-25 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 6fb7e0b2-07df-314e-b307-09ff8c3ab00b | -4.25335 | -48.55089 | 2024-10-25 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 92461d84-09a0-321c-97de-00d6594d81a0 | -4.25003 | -48.55037 | 2024-10-25 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 92e921b1-7ef2-3108-840a-80da17f52acc | -4.24949 | -48.55383 | 2024-10-25 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 02298c9b-8647-3b08-967a-9b10b7629ad2 | -4.24671 | -48.54985 | 2024-10-25 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 2fd79bfe-53c4-3e89-8107-a0cac2f01b49 | -4.24617 | -48.55331 | 2024-10-25 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 703b3ef3-0a2b-3b6f-b876-7fd7a85b9e2e | -4.24562 | -48.55677 | 2024-10-25 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 52463345-8eeb-34ec-b411-8f6b4fea7241 | -4.24393 | -48.54587 | 2024-10-25 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| f901cdc4-ef67-311a-8fac-323dbb584b5e | -4.24339 | -48.54933 | 2024-10-25 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 296e1339-1f56-343c-9014-067dc0a39b93 | -4.24285 | -48.55279 | 2024-10-25 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| c60a03d1-c4e9-3ec0-8081-f3ded1b429e3 | -4.2423 | -48.55625 | 2024-10-25 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 296eb0ae-840e-34a5-b19e-a49bc75c14dd | -4.24176 | -48.5597 | 2024-10-25 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| c8dcb83e-a321-350a-8017-94d96242855b | -4.24007 | -48.54881 | 2024-10-25 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 2cd13b85-d011-3f2d-823c-08d1366bc835 | -4.23952 | -48.55227 | 2024-10-25 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| f5e7a260-753f-3370-b5ce-35ced7863083 | -4.23898 | -48.55573 | 2024-10-25 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| af98ba0a-6031-3c9f-b94f-77c58f7fae3b | -4.23844 | -48.55919 | 2024-10-25 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 1e5ea10d-4af4-3f12-855f-f59ce65224b3 | -4.23566 | -48.55521 | 2024-10-25 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 56414853-0492-3642-8042-5b37eed42e6c | -4.22129 | -48.56005 | 2024-10-25 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4d977af4-3810-3dc6-9221-95d29277217b | -4.22074 | -48.56351 | 2024-10-25 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 78c24169-918a-3fb6-8e01-70863afa34c9 | -4.21796 | -48.55954 | 2024-10-25 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2a7ffbb2-aa96-3b95-abc0-72563295f0b8 | -4.21742 | -48.56299 | 2024-10-25 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 23bd7cda-fa32-319e-b2ae-726600e36b76 | -4.21464 | -48.55902 | 2024-10-25 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b626ff67-4c0b-3e59-ba68-427552921276 | -4.21173 | -48.0384 | 2024-10-25 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 80a04345-958e-3311-8d10-63a7be1a3852 | -4.20505 | -48.03739 | 2024-10-25 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bf3a9a1a-76f9-375b-881b-5d3f9e829a2f | -4.2045 | -48.04088 | 2024-10-25 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fb4bda72-082b-336b-a32a-3f6bf80c506c | -4.20171 | -48.03687 | 2024-10-25 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1c3ec179-20ea-332c-b7a9-e660e3d36907 | -4.20061 | -48.04385 | 2024-10-25 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 68a3a61c-15f6-3853-8385-cdbbbbb94c04 | -4.20007 | -48.04733 | 2024-10-25 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 400c71cc-023a-3edf-b2ae-10a05444e6b9 | -4.19952 | -48.05081 | 2024-10-25 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b958db05-ccf3-36d3-b68f-d9f99536c5ef | -4.19837 | -48.03635 | 2024-10-25 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ba6d439a-c20d-3051-9824-0abb15fa4a19 | -4.19782 | -48.03984 | 2024-10-25 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 60a50ec3-ac43-37f4-aada-eb57b3d9821e | -4.18211 | -48.59286 | 2024-10-25 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d5eca47e-8b10-3576-b927-17fcef3d57fd | -4.17879 | -48.59234 | 2024-10-25 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9925f768-d783-3d07-a14f-b2f3b05fd2e6 | -4.17546 | -48.59182 | 2024-10-25 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 44e57886-37e5-34d3-88b5-268538706067 | -4.35657 | -49.09773 | 2024-10-25 04:38:00 | NPP-375D | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9f7dace0-dfd9-37ad-8d41-dc5c65f67b52 | -5.71884 | -49.27657 | 2024-10-25 04:38:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| de141bff-0620-3ce2-8b6c-cdcf5d3a6b8b | -5.69565 | -49.29422 | 2024-10-25 04:38:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 891ff4ef-2d36-3feb-8acc-b61977bea14c | -5.69233 | -49.29369 | 2024-10-25 04:38:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c0ce1a7a-8d95-333d-8cef-3ea4f751980b | -5.4931 | -49.50752 | 2024-10-25 04:38:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9398539d-8d00-32d5-a7b6-6915c5b99bed | -5.49255 | -49.51099 | 2024-10-25 04:38:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e21638eb-0c5f-3265-86e5-42de70a85622 | -5.39324 | -48.83165 | 2024-10-25 04:38:00 | NPP-375D | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 52efef2f-e6f3-3441-bce5-aa82f6b25996 | -5.38991 | -48.83113 | 2024-10-25 04:38:00 | NPP-375D | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4de538d2-2a0b-37dd-a2b4-bfee0d699020 | -6.41852 | -49.58271 | 2024-10-25 04:38:00 | NPP-375D | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8dcecbb3-52f5-34da-be45-ef42fe48dd01 | -6.41797 | -49.58617 | 2024-10-25 04:38:00 | NPP-375D | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 19632c96-c686-3f6b-992c-cff81fa27a83 | -6.41188 | -49.58165 | 2024-10-25 04:38:00 | NPP-375D | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4a8f3f8d-a65e-334c-a4f2-cc26db0bcbc1 | -6.29699 | -49.30389 | 2024-10-25 04:38:00 | NPP-375D | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| dab91630-3b56-3ec3-b9a3-74d49885f792 | -6.29644 | -49.30735 | 2024-10-25 04:38:00 | NPP-375D | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 83593fff-c6ba-33bd-ab1a-75c2d19db301 | -5.7294 | -49.29597 | 2024-10-25 04:38:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 051ce0fe-eb4f-34d6-ae64-437f3d5046b6 | -6.48973 | -48.76437 | 2024-10-25 04:38:00 | NPP-375D | PIÇARRA | PARÁ | Brasil | 1505635 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ed9558d0-c7fc-3e61-b3c9-b16f79ec3089 | -6.48744 | -48.73538 | 2024-10-25 04:38:00 | NPP-375D | PIÇARRA | PARÁ | Brasil | 1505635 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 83dd6066-c632-3151-8b0a-652158e90363 | -6.48694 | -48.76036 | 2024-10-25 04:38:00 | NPP-375D | PIÇARRA | PARÁ | Brasil | 1505635 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3dd41e14-5868-3f79-8ba4-39321c26bb16 | -6.48689 | -48.73887 | 2024-10-25 04:38:00 | NPP-375D | PIÇARRA | PARÁ | Brasil | 1505635 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 94802ff0-5387-38ef-98a6-2ffba3f42ba1 | -6.48411 | -48.73486 | 2024-10-25 04:38:00 | NPP-375D | PIÇARRA | PARÁ | Brasil | 1505635 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ecc38968-63ca-3db6-ae31-60bde4dba69d | -6.48356 | -48.73835 | 2024-10-25 04:38:00 | NPP-375D | PIÇARRA | PARÁ | Brasil | 1505635 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3cc78d17-b350-383c-8ba5-4365c88bda43 | -5.52632 | -48.10424 | 2024-10-25 04:38:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6bdcaf2d-c6f4-35b0-830c-36d8a37025d0 | -5.3861 | -48.85538 | 2024-10-25 04:38:00 | NPP-375D | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4f407071-eeae-363f-a203-d1262d248069 | -5.38567 | -48.90144 | 2024-10-25 04:38:00 | NPP-375D | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 5d7494f1-0e93-3d68-86db-8958c4727cbd | -5.38512 | -48.90491 | 2024-10-25 04:38:00 | NPP-375D | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 60ca9b4e-40cd-3d7f-97c5-98c544402438 | -5.38235 | -48.90092 | 2024-10-25 04:38:00 | NPP-375D | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 2f48708e-224b-353e-b232-27590f380d84 | -5.3818 | -48.90439 | 2024-10-25 04:38:00 | NPP-375D | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 26eeb866-fc99-3cc4-815e-034e06257a54 | -5.35494 | -48.16857 | 2024-10-25 04:38:00 | NPP-375D | BURITI DO TOCANTINS | TOCANTINS | Brasil | 1703800 | 17 | 33 | nan | nan | nan | Amazônia | 0.4 |
| a7b14df1-0f17-31ce-a2c6-223f99dcbc7d | -5.25028 | -48.4502 | 2024-10-25 04:38:00 | NPP-375D | ESPERANTINA | TOCANTINS | Brasil | 1707405 | 17 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6c3e588a-a1fc-341d-93ff-5704084ed2ad | -5.2237 | -47.95277 | 2024-10-25 04:38:00 | NPP-375D | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fe3d55e7-fe50-376e-8f11-26208d1d5474 | -5.21466 | -48.21895 | 2024-10-25 04:38:00 | NPP-375D | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 81a06ad9-74f5-3e9b-be66-bb5eb08f0cb0 | -5.21132 | -48.21843 | 2024-10-25 04:38:00 | NPP-375D | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 40c19529-27ad-302b-9015-983e59062046 | -5.20852 | -48.21441 | 2024-10-25 04:38:00 | NPP-375D | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c57764e6-3b1b-3f76-a717-87a878245866 | -5.20797 | -48.21791 | 2024-10-25 04:38:00 | NPP-375D | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 8d1a62a3-0443-3649-94cb-bfdc1b98ac77 | -5.20743 | -48.22142 | 2024-10-25 04:38:00 | NPP-375D | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 33ece46e-499d-38d1-bd19-e8bd943a57e1 | -5.20463 | -48.2174 | 2024-10-25 04:38:00 | NPP-375D | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 06287e20-9d81-37ef-b4b3-6d8958c13fd9 | -5.20408 | -48.22091 | 2024-10-25 04:38:00 | NPP-375D | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 18b0a83b-7020-39f8-a664-d65bc3848dc4 | -7.85573 | -48.72108 | 2024-10-25 04:38:00 | NPP-375D | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 55e7bf38-6ef6-31f2-b74e-247ba2792e15 | -7.34152 | -49.13339 | 2024-10-25 04:38:00 | NPP-375D | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1da33110-017b-3891-b89a-524f9e83c9dc | -7.34097 | -49.13688 | 2024-10-25 04:38:00 | NPP-375D | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e0ccbfa3-3157-3f8f-be72-2b85d674cdac | -7.33765 | -49.13635 | 2024-10-25 04:38:00 | NPP-375D | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3ed8f4e6-930e-3d37-b1eb-f3d370c89d71 | -7.3371 | -49.13984 | 2024-10-25 04:38:00 | NPP-375D | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f7eb072b-0618-3cc2-8ef0-95f5e941ea06 | -7.33378 | -49.13931 | 2024-10-25 04:38:00 | NPP-375D | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4900654f-e274-3939-9504-68048db7a675 | -7.1137 | -49.14076 | 2024-10-25 04:38:00 | NPP-375D | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 1.2 |
| da8a9f0e-1760-3266-bba0-f1d51ad423b6 | -7.11321 | -49.16564 | 2024-10-25 04:38:00 | NPP-375D | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bc154220-c09c-3650-94f2-3768ac178b5d | -7.11267 | -49.16912 | 2024-10-25 04:38:00 | NPP-375D | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1da9aa57-f3a0-3ffb-b40f-6607a26a6feb | -7.11037 | -49.14024 | 2024-10-25 04:38:00 | NPP-375D | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 65786c26-1db5-3e73-928b-b212dcb46767 | -7.10934 | -49.16859 | 2024-10-25 04:38:00 | NPP-375D | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f5c40a98-2349-3039-a3b5-f5af18b54a6a | -7.1088 | -49.17207 | 2024-10-25 04:38:00 | NPP-375D | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 24295eac-1e83-3214-bd2a-f9b1bf9768ea | -7.10874 | -49.15068 | 2024-10-25 04:38:00 | NPP-375D | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 90a49444-6550-3ae2-9311-2981397f1a88 | -7.1065 | -49.14319 | 2024-10-25 04:38:00 | NPP-375D | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dbc5c1af-9759-399f-85d3-5fb84a73e23c | -7.10602 | -49.16807 | 2024-10-25 04:38:00 | NPP-375D | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f542e6cf-3329-3162-8395-734b60f4e773 | -7.10596 | -49.14668 | 2024-10-25 04:38:00 | NPP-375D | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ac3f253e-6916-32ea-a4f6-d62bde3ade87 | -7.10547 | -49.17155 | 2024-10-25 04:38:00 | NPP-375D | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README59.md)
