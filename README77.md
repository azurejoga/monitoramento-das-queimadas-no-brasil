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

## Dados Diários - Página 77

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2ed89000-108e-3146-b376-0a3ff3b437bd | -3.81926 | -52.40114 | 2026-09-23 05:01:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 543a12bc-432e-3e01-b4c6-19158835c3f0 | 1.4363 | -50.82975 | 2026-09-23 05:01:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6f0e8e47-a2f9-39ba-8d4c-c81912290f03 | -1.32372 | -54.66374 | 2026-09-23 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b925418b-b656-30c6-b08d-ba0059b7157d | 0.60203 | -50.79492 | 2026-09-23 05:01:00 | NPP-375D | ITAUBAL | AMAPÁ | Brasil | 1600253 | 16 | 33 | nan | nan | nan | Amazônia | 0.2 |
| ac519581-6d06-3173-942e-ee5c6cd43414 | -2.97681 | -54.15306 | 2026-09-23 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 876945e8-0523-3a87-99ef-da5cc438adcd | -2.9477 | -54.08217 | 2026-09-23 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 47cf5a61-1044-3615-9323-5b0d926eb211 | -1.59324 | -54.41861 | 2026-09-23 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1854f0fc-a80f-303a-9661-ea85eb4bca6f | -3.36177 | -50.76785 | 2026-09-23 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0714e006-bf82-3528-82d0-c31c8155dc3f | -3.38396 | -50.4082 | 2026-09-23 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2712d57e-d0c7-3971-818f-8a5eb71a78f0 | -2.45387 | -49.21491 | 2026-09-23 05:01:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3a1e47dd-7a92-3de8-8e68-2be7aafddfd6 | -3.39214 | -50.82294 | 2026-09-23 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8845aba3-e2a1-31f9-ba06-9aca08fa5442 | -11.66677 | -43.47961 | 2026-09-23 05:04:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 804ec847-0f30-3e7d-808f-4d35c28a138d | -5.02951 | -49.68248 | 2026-09-23 05:04:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 30fea746-0125-343d-a231-4eb484a86dbc | -7.42377 | -49.86253 | 2026-09-23 05:04:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a1abbd65-8924-393a-8e98-84113526c700 | -6.30652 | -56.04276 | 2026-09-23 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d7fcd558-6380-38f5-a21c-000ef44013d7 | -6.61789 | -59.90914 | 2026-09-23 05:04:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a5b9843b-1078-390f-8bf9-f2fa8570efd7 | -8.08386 | -44.34267 | 2026-09-23 05:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7b8abd41-e002-3ccb-b300-67cf6e5ce620 | -3.78128 | -60.75661 | 2026-09-23 05:04:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a7a7b60b-0617-3b8e-8253-71f1605bdc05 | -3.58266 | -59.06653 | 2026-09-23 05:04:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 311fe64c-9e1e-3b8b-b49c-1c0f97b12cad | -5.81561 | -57.73642 | 2026-09-23 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f16f4084-1ce9-353b-8e55-82245211bdb1 | -6.25784 | -55.43529 | 2026-09-23 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 729d77f2-0e3b-3218-8b47-b90147cb4452 | -8.48269 | -44.75308 | 2026-09-23 05:04:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3c21f3d2-b961-38f6-aa08-b50884beb376 | -7.45149 | -61.379 | 2026-09-23 05:04:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 4c906526-0945-3b38-87a6-afc2ed686a4c | -4.83656 | -55.76675 | 2026-09-23 05:04:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f33a66e5-b8a8-3adc-9751-f4526218bccb | -7.55584 | -55.01843 | 2026-09-23 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e76ecdbf-64d4-311e-b0c6-e0e400cfad26 | -6.10635 | -44.14841 | 2026-09-23 05:04:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1fa609b9-eb0d-3577-a38f-cfa23bc11563 | -6.81465 | -59.43684 | 2026-09-23 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2d360427-39f1-3151-beb9-b2e788cd686c | -6.3442 | -43.36667 | 2026-09-23 05:04:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fde65003-edbc-305e-83db-9b12cb24e94a | -5.60857 | -45.94633 | 2026-09-23 05:04:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e0ec0f33-3cf0-30a0-bbd0-fb01a3aedc65 | -7.59015 | -57.66451 | 2026-09-23 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7e1c2977-7aa5-394b-aae9-5769968bc15f | -10.4567 | -46.27777 | 2026-09-23 05:04:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b61d1db8-a16d-3e92-9bd6-cbed92a46594 | -6.12812 | -57.75533 | 2026-09-23 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 02630f66-1a19-3a29-93f4-ca201ffc06f2 | -6.61869 | -43.72556 | 2026-09-23 05:04:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e20f20e7-d50c-37a2-93b1-4b072215b89b | -6.12753 | -57.7589 | 2026-09-23 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c912e815-62dd-3f92-8e67-a7ef61af4a32 | -11.66727 | -43.47556 | 2026-09-23 05:04:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a9ad9fef-b17d-3041-abb2-21a3b6a317c2 | -7.414 | -44.72807 | 2026-09-23 05:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 318786c3-d0cf-362a-9cc5-43f5fc24157f | -8.10594 | -44.42336 | 2026-09-23 05:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c761e2d7-02b3-33db-9741-030330806802 | -5.87832 | -52.06591 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a862feef-c34c-36e2-81ec-91e72c138350 | -11.64993 | -50.978 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 16950c49-a4c4-3aec-b7b6-56349ac271f3 | -10.27095 | -49.97788 | 2026-09-23 05:04:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c2ce73df-757e-30a5-9067-965e7b5696fa | -6.84751 | -45.55181 | 2026-09-23 05:04:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 3eb9cae2-4d89-31c3-bdce-46a671c9b4e6 | -6.84201 | -55.30451 | 2026-09-23 05:04:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d06aff4b-39aa-36bf-9987-2524fd2c4969 | -6.13764 | -43.84847 | 2026-09-23 05:04:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 43b2a35f-e802-3424-b014-5bb41d6b7ac8 | -11.29901 | -51.34824 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1978dffe-b813-364d-b841-73524a34447f | -6.6281 | -59.98825 | 2026-09-23 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9172bfe9-cb80-3450-a7f1-35e4bf25beb4 | -3.83855 | -55.86459 | 2026-09-23 05:04:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 9da7fe26-73df-3b57-a44e-ee7551110727 | -9.16355 | -61.36596 | 2026-09-23 05:04:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3f8e56f2-329a-32da-bea1-13304be4061a | -6.67457 | -50.94199 | 2026-09-23 05:04:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5c9b7f86-9a0b-3df6-94d9-b891a63a5c7b | -8.31707 | -54.88913 | 2026-09-23 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 037a1ce0-2d60-3056-bc49-1d463c996fb2 | -3.78701 | -60.75438 | 2026-09-23 05:04:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d4940d1a-2566-3a92-bbb2-0739627f73ec | -6.62686 | -59.93494 | 2026-09-23 05:04:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 34f63235-cd7a-3a4f-abf7-53d99493e4c0 | -6.16332 | -57.71214 | 2026-09-23 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cdf028ca-5731-3f25-ba92-340a54109fcd | -6.62771 | -59.92994 | 2026-09-23 05:04:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 09648f45-6820-31c9-9d63-8d8d8160bae2 | -11.13018 | -51.0567 | 2026-09-23 05:04:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1377776e-66f3-34a0-a887-2fde03bbcaed | -7.12826 | -43.07829 | 2026-09-23 05:04:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 7d31432c-48bd-36f0-b342-02b094ac60b6 | -6.77582 | -59.63382 | 2026-09-23 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 05ca9a87-a123-307d-a86e-2896554da756 | -7.39814 | -55.21443 | 2026-09-23 05:04:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2f38ce46-a104-3d66-8c41-914efba7502f | -3.7527 | -58.8645 | 2026-09-23 05:04:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f7d456dc-69a3-3b24-98aa-5e4af4e9e483 | -7.09631 | -52.75061 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 722178f4-3060-3342-88fa-43719bda2db4 | -11.35527 | -43.3795 | 2026-09-23 05:04:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9a47ba22-d295-3f14-91c1-e1695c54322a | -6.68026 | -55.0778 | 2026-09-23 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9a40dd2c-38af-3569-a1c6-deb3451f3234 | -8.91646 | -50.89426 | 2026-09-23 05:04:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d09daeac-151a-3b4b-835a-7c9a0ce1efb8 | -6.73336 | -55.30796 | 2026-09-23 05:04:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 25205d03-ecf5-303e-8a88-c8e7be17d73c | -9.24183 | -57.16188 | 2026-09-23 05:04:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2de97014-fc43-3346-8b8a-10bee6bb34ef | -6.13533 | -45.01595 | 2026-09-23 05:04:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1a2f83b6-f7f0-31c0-b351-17fcdbd7849f | -6.3075 | -56.04469 | 2026-09-23 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 96336e38-6469-343c-b894-1e1df65b8752 | -5.61573 | -45.24529 | 2026-09-23 05:04:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 1b2fc2e1-2f03-3f5f-ac11-e5ef71cb5960 | -10.70923 | -48.7212 | 2026-09-23 05:04:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 03529b5d-3976-354d-bb17-fd14cb769d37 | -8.08989 | -44.34687 | 2026-09-23 05:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 97eff691-9be7-32c2-9399-63f645653427 | -6.89919 | -43.63314 | 2026-09-23 05:04:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7b88c4fd-2a7c-3d41-acab-933f36605563 | -11.6535 | -50.97855 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0ffe55d4-9430-3609-bf0d-64becd3dabd2 | -6.61746 | -59.93328 | 2026-09-23 05:04:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 26.6 |
| 90272408-cd74-364b-bb13-ebc0d96659cd | -3.65062 | -57.08028 | 2026-09-23 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 803fcaa3-49cf-353a-90a0-a78be8d46121 | -3.16009 | -58.12316 | 2026-09-23 05:04:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 8ca2cb16-d281-3021-b8b8-8651dbe55220 | -6.01405 | -52.74877 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| efb0f4c8-9b9a-32a0-8e96-0a4ae0715f22 | -6.48197 | -53.57289 | 2026-09-23 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 943460b6-048f-3ffe-9fca-120194ca08e4 | -5.87512 | -52.12953 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cf2be9e3-5784-37fe-bb05-f3dd4777770f | -12.03124 | -47.81237 | 2026-09-23 05:04:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ff48d0f4-4917-3ba6-8e8c-916622bcb4a6 | -9.87059 | -48.393 | 2026-09-23 05:04:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 79989af1-0593-3daf-8a4e-fb382bc975e7 | -10.26725 | -49.97732 | 2026-09-23 05:04:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 739f1c6f-eb78-3693-a6a8-91f981f1c85a | -5.89004 | -52.0998 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 591e77e5-ab24-38a5-a1b6-081fd770b707 | -6.63628 | -59.93652 | 2026-09-23 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 16.9 |
| d647d77b-f03c-377f-83f9-ded236415432 | -8.51063 | -63.36283 | 2026-09-23 05:04:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3867f3ca-81e9-3a15-8f7a-1d8dd7099796 | -6.4669 | -53.55962 | 2026-09-23 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7fa38005-99ac-3752-848d-9a08437713a0 | -9.92457 | -48.48001 | 2026-09-23 05:04:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fe2a566a-b2e2-3ead-b831-87badbb04a07 | -7.41662 | -49.86113 | 2026-09-23 05:04:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ac20a2fe-d7ba-3bbb-95e9-1e2ec51d32b8 | -6.32839 | -43.93243 | 2026-09-23 05:04:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 79caa90f-ee56-3063-9df6-11b37c583752 | -10.90884 | -53.94062 | 2026-09-23 05:04:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 0a23c780-1cb9-3ca5-b0b8-42dd403e05c9 | -6.71271 | -59.45456 | 2026-09-23 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d520d858-892c-30dc-b988-9f0bd07eedb6 | -4.42258 | -55.47742 | 2026-09-23 05:04:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| de961ac0-2d5a-36f9-b16f-cf2de08a02e3 | -11.43249 | -47.3869 | 2026-09-23 05:04:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| c23f0ec3-5da7-31c3-83a3-104423edc5df | -5.59718 | -60.20686 | 2026-09-23 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 974790dd-81c8-3027-b84c-92d14508ba64 | -9.91395 | -45.0976 | 2026-09-23 05:04:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 81a4e45a-4ea4-3416-a3a4-1af4ca3f7f27 | -8.25469 | -54.77591 | 2026-09-23 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 92096b8d-5b41-3b09-aa32-dccefa1cfbe7 | -6.4607 | -59.99152 | 2026-09-23 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8ad5bf38-e2f6-35b0-aaa6-2422697232d4 | -9.05127 | -65.42691 | 2026-09-23 05:04:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8d7b9c17-f981-3639-a004-b1f3ccd8f9e8 | -9.0415 | -65.40828 | 2026-09-23 05:04:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 052574a1-e922-30d3-8d98-b5cdab61f978 | -6.18322 | -52.79395 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b038fdaa-e430-34f0-9362-529db2cbb19c | -6.6774 | -55.07328 | 2026-09-23 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 085f8a36-e31d-3d18-9c28-62880d0bf559 | -8.08512 | -44.34306 | 2026-09-23 05:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README78.md)
