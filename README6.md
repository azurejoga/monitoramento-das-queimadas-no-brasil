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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 136e8e97-c589-3077-99e0-bd6874718252 | 1.88291 | -60.35534 | 2025-03-03 05:33:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| cf25e4f4-29ff-3f04-8360-0ec747b76e56 | 3.7019 | -60.75603 | 2025-03-03 05:33:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 154b88b6-2cbc-3b4c-a963-582f7fe844b0 | 4.35151 | -60.34096 | 2025-03-03 05:33:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| db63d361-28c0-3f33-aefc-71c3e365f8a0 | 3.20863 | -60.51921 | 2025-03-03 05:33:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ee4980a8-724f-3a62-87cf-f6ce197847c0 | 2.22145 | -61.34215 | 2025-03-03 05:33:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dac294d1-480b-32a0-b17b-ff450ba2b168 | 1.94154 | -60.38683 | 2025-03-03 05:33:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e4a7cb21-4eb8-3718-ad72-523cff548183 | 2.00593 | -60.55538 | 2025-03-03 05:33:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 187062ed-ceb7-3da2-a2d1-5c009cab3cb5 | 1.93989 | -60.39816 | 2025-03-03 05:33:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 80b076e5-64cc-3e1e-8534-2e0df5cd21db | 2.88599 | -60.13784 | 2025-03-03 05:33:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dbc8f426-076b-3a09-8f38-c4d8e79047fe | 3.22369 | -60.46293 | 2025-03-03 05:33:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e86c86f8-4597-38d4-be9f-466324b21b80 | 0.95801 | -60.53072 | 2025-03-03 05:33:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ba08409d-10cd-31f2-a364-bfd1a96f6983 | 2.11198 | -61.81897 | 2025-03-03 05:33:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7ed46406-c7aa-3423-808f-fe627b395d41 | 1.89357 | -60.40136 | 2025-03-03 05:33:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bed84222-11f9-3ff6-a0cb-1886acd1b1d9 | 2.02453 | -61.43254 | 2025-03-03 05:33:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 174486e7-a2b6-3e8e-ad37-12ec7e333c72 | 2.19 | -61.85931 | 2025-03-03 05:33:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7bbfd5d1-e704-3d8e-aa72-bdfa55f00b29 | 1.57757 | -60.19537 | 2025-03-03 05:33:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9e48e59e-73f0-3701-a2e5-b2d67effe57e | 1.90142 | -60.38546 | 2025-03-03 05:33:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e80a4326-9b75-364b-98dc-a7f454525f2b | 1.31134 | -60.07063 | 2025-03-03 05:33:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 08905835-ff9a-372f-a6c5-c9400f001d70 | 2.00314 | -60.55944 | 2025-03-03 05:33:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9d5f2d97-e62c-35b3-b3f8-6133b215c8a1 | 1.8869 | -60.85881 | 2025-03-03 05:33:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f41ae379-e828-3b1b-8871-6ca01c6e37f9 | 2.76166 | -61.42221 | 2025-03-03 05:33:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f39f9637-6f08-3e2d-9528-bfd326adcd8f | 2.0108 | -61.43113 | 2025-03-03 05:33:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 7.0 |
| d1cee4fe-98c1-3483-9cc8-b688329cc1bf | 1.02382 | -59.52983 | 2025-03-03 05:33:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 44c9334d-0efe-3328-a2b9-ec4b8ce90d03 | 1.93875 | -60.39095 | 2025-03-03 05:33:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 03504710-65ad-3167-9ea3-3736cda88202 | 1.93652 | -60.39861 | 2025-03-03 05:33:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 24dfe534-5898-34f2-8718-76dd711c47ff | 3.20808 | -60.5157 | 2025-03-03 05:33:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 774f8012-8adb-3af4-849c-19954ebe0d41 | 1.30736 | -60.06746 | 2025-03-03 05:33:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e7918bfc-7ef7-3d53-b677-4f3b26049362 | 1.07096 | -59.5468 | 2025-03-03 05:33:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 497386a1-310e-3681-8e08-f7f76bde6dfd | 2.19451 | -61.3428 | 2025-03-03 05:33:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 3f96ecd7-f2aa-37c3-80b7-b05751da53f7 | 2.10922 | -61.8229 | 2025-03-03 05:33:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ee7907bd-6c03-3919-8ec5-389ab6eefe0d | 1.07009 | -59.58648 | 2025-03-03 05:33:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e9b7c2ab-af3c-3602-8b90-75c3490501a6 | 1.79512 | -60.26953 | 2025-03-03 05:33:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 84ffe5d5-9bf2-3413-81d7-a9054e72fbb9 | 3.50263 | -60.13663 | 2025-03-03 05:33:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3939fe25-2dee-38e8-bd31-9fdd0aab6e3e | 1.18683 | -60.32564 | 2025-03-03 05:33:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8fc12ae6-7c14-3bd4-a321-23a61cdba38c | 4.33081 | -61.12253 | 2025-03-03 05:33:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b99233a9-1b96-38c2-9df3-d56d8231c5b3 | 2.01794 | -61.43356 | 2025-03-03 05:33:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 6e42b3cc-665b-38c4-b81e-0bf996167576 | 3.49928 | -60.13716 | 2025-03-03 05:33:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e4321ce5-64d3-31b1-8716-1113d5b3aef0 | 1.89077 | -60.86179 | 2025-03-03 05:33:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8df67528-8421-3cae-a58e-0546b1ccfbe5 | 1.84831 | -60.74271 | 2025-03-03 05:33:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fd08b6d9-f315-38cc-b92e-cab2ee21f401 | 1.31077 | -60.06694 | 2025-03-03 05:33:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0125664a-4ef3-334d-ae0e-578695d2df04 | 2.0141 | -61.43062 | 2025-03-03 05:33:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 7.0 |
| d62efee6-5000-3645-ba3f-9867e733683e | 2.00258 | -60.5559 | 2025-03-03 05:33:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bf392ecc-bd63-340d-be22-4f54161e87d9 | 1.8441 | -60.30612 | 2025-03-03 05:33:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4dc12dc4-687e-3139-9a05-287c48956089 | 3.68926 | -60.74027 | 2025-03-03 05:33:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f1b0bd1a-103a-3ea3-9717-ddd386faae3a | 0.89022 | -60.25141 | 2025-03-03 05:33:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1d0ccb93-9c52-3522-a293-5e54ae973ca9 | 1.58154 | -60.19847 | 2025-03-03 05:33:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c63216ba-de0a-3479-a9b2-57f5de1b7e3a | 2.3361 | -60.51136 | 2025-03-03 05:33:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 85e818fd-c304-3ec2-904d-3964c41771f1 | 1.93318 | -60.54477 | 2025-03-03 05:33:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 46448ebf-10bc-3789-ad45-6fbcb0b02a90 | 3.21812 | -60.47099 | 2025-03-03 05:33:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8ac9ac47-ece7-39fa-8099-a6be22dc2138 | 0.99786 | -59.47808 | 2025-03-03 05:33:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f2160fb4-0d44-375f-bc4e-9c44cd9042f4 | 3.70244 | -60.7595 | 2025-03-03 05:33:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0f600bb9-1d02-30c2-af1f-bfb57d602935 | 4.23678 | -59.84698 | 2025-03-03 05:33:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 404d83ac-28e9-3795-aa71-d64ff148abe6 | 0.02933 | -60.66979 | 2025-03-03 05:33:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f0541e4a-86cf-35c6-9d11-4ff9be7cfc49 | 0.9642 | -60.52608 | 2025-03-03 05:33:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 400f8a98-0333-362f-8440-75feaefd5726 | 2.18947 | -61.85589 | 2025-03-03 05:33:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8ba17870-82d5-3298-897f-705128b97387 | 1.89023 | -60.85829 | 2025-03-03 05:33:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5c759692-f460-3138-b985-56593c7c355b | 0.82045 | -59.26963 | 2025-03-03 05:33:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e0f9249c-1a8d-3747-afa2-ef32c67d6a41 | 1.92586 | -60.60759 | 2025-03-03 05:33:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 76bb2e0b-6be5-36b0-9cc5-56e613549e48 | 1.10882 | -59.35258 | 2025-03-03 05:33:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6b862f0a-072d-3aa4-a32d-5d7f2e9d0216 | 0.75501 | -60.23866 | 2025-03-03 05:33:00 | NOAA-21 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 80696e03-3f60-3262-810c-2c2ce2751432 | 1.79568 | -60.27314 | 2025-03-03 05:33:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b8998801-f5b5-3605-92e3-722f42ef5e0c | 2.00649 | -60.55892 | 2025-03-03 05:33:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 91f21b9f-3298-3f45-9f9a-14dd98b4f18d | 0.99818 | -59.43394 | 2025-03-03 05:33:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 89be3b7c-7ff8-327f-b717-f3f6e1936949 | 1.5855 | -60.20157 | 2025-03-03 05:33:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f837ccf0-4624-3eaa-864e-750f557b3577 | 0.77256 | -60.54877 | 2025-03-03 05:33:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9399ad2f-f395-347d-a5ee-db372e96401b | 1.19879 | -60.06875 | 2025-03-03 05:33:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6d7878da-42cd-3293-ac41-58d333b5e3df | 0.9715 | -60.52862 | 2025-03-03 05:33:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a3c546ef-9b46-3372-a40c-472c51225f8d | -21.23154 | -56.06119 | 2025-03-03 05:40:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c0a8064c-f637-3ca9-9754-d94df1d73427 | -21.23113 | -56.06563 | 2025-03-03 05:40:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 740f5875-24c0-308d-bf9a-8b940a0c1575 | -21.23036 | -56.06191 | 2025-03-03 05:40:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ea5c4888-14e4-3f7c-b154-22716845e0a5 | 2.11162 | -61.81743 | 2025-03-03 05:59:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 49e719a8-b11a-3c9a-8ab9-06e02202818d | 1.8936 | -60.40269 | 2025-03-03 05:59:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8e7c4594-9713-3e7f-b41d-b5e6618ef138 | 1.89269 | -60.39721 | 2025-03-03 05:59:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 59ddded8-d2a4-3e26-bdd3-8d2d10bac3e9 | 1.88611 | -60.85679 | 2025-03-03 05:59:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d21dbcdd-0d95-3c78-8eb2-a6421f502e06 | 1.94282 | -60.39626 | 2025-03-03 05:59:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 4.9 |
| ab3db513-14c6-3fba-a9d3-33ebeccf9f44 | 2.10787 | -61.82243 | 2025-03-03 05:59:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 130d44e8-dd42-35a6-8b3b-90fd0e5e6164 | 1.90259 | -60.45669 | 2025-03-03 05:59:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b65ff869-9acf-3186-84a5-a4528587d51f | 1.93223 | -60.54512 | 2025-03-03 05:59:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0f2a604b-3933-31ed-ad82-465b1cad2703 | 3.52824 | -60.51764 | 2025-03-03 05:59:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c6692704-c686-3a93-82dc-74f759bf05ab | 1.76665 | -60.22685 | 2025-03-03 05:59:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 47da22d5-8c94-3119-9fcc-56a1ccc1aedd | 2.10651 | -61.81385 | 2025-03-03 05:59:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c289bfcc-a91c-3db6-ad8e-d7ca886a607b | 3.5037 | -60.13792 | 2025-03-03 05:59:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| efae8a32-c7d6-3a34-bcdf-e1a0a9bf907b | 2.45403 | -61.32129 | 2025-03-03 05:59:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e5b8cf52-3c2d-3c4d-b8fa-ae18268eac73 | 2.19568 | -61.34456 | 2025-03-03 05:59:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aa50440f-39d9-30f0-bf1b-28bf8e7a76f5 | 1.94179 | -60.38989 | 2025-03-03 05:59:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 2e417e58-d4b8-3dc2-a843-930cb1f820f3 | 2.00347 | -60.55521 | 2025-03-03 05:59:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0c48e407-ab0e-333a-9f9e-da90cdb62bad | 2.10209 | -61.81459 | 2025-03-03 05:59:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e8be7e85-7bbf-3b29-a15b-454c526a4107 | 2.337 | -60.5107 | 2025-03-03 05:59:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9d9a026f-f1ba-324c-8e90-fd4255b93be8 | 1.90746 | -60.45588 | 2025-03-03 05:59:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c4f6dd50-6e35-363b-a0e0-2c89e679da0e | 3.20556 | -60.52144 | 2025-03-03 05:59:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e8f8a999-6967-3b11-80b1-2ee7f91cb0c7 | 2.01281 | -61.43012 | 2025-03-03 05:59:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 246ba28e-7afa-3980-8871-d282b998cb03 | 2.113 | -61.82615 | 2025-03-03 05:59:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b3934751-6d8e-3643-8609-f358b47fcb5b | 1.90068 | -60.38471 | 2025-03-03 05:59:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e9b39489-1af3-3f0f-bfe7-d27ff38e4e6a | 2.38368 | -60.58334 | 2025-03-03 05:59:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1c76a9b6-a331-36da-8dae-f18aa0a7e442 | 1.76576 | -60.22124 | 2025-03-03 05:59:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bd24c3c9-bc00-3803-a0be-67d7489523c8 | 3.70596 | -60.76323 | 2025-03-03 05:59:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 634874b7-3369-3010-b602-d006771d4ae5 | 2.10719 | -61.81811 | 2025-03-03 05:59:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c105f008-92d2-36c9-a52a-66345260fe0e | 2.01661 | -61.42472 | 2025-03-03 05:59:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 8077554e-61cf-3632-8329-f187b23b9219 | 2.339 | -60.5116 | 2025-03-03 05:59:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1b8f9d1f-05a6-3a90-ae15-f2991c536eeb | 2.11231 | -61.82178 | 2025-03-03 05:59:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |


[Clique aqui para ver as próximas entradas](README7.md)
