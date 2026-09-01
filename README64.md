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

## Dados Diários - Página 64

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7b44e7bb-9ad6-3a93-99cc-36c304b89eb3 | -4.14976 | -60.6963 | 2026-09-01 05:16:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4fc702a6-e322-3b70-999c-9f89ca0879b1 | -6.18299 | -57.72916 | 2026-09-01 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 8de4d707-5800-388e-8b32-3448d96fe980 | -6.15897 | -57.79031 | 2026-09-01 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f7ebb4d4-6b4c-3ff1-86a7-1b8cbb1259ab | -7.04053 | -59.22397 | 2026-09-01 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 31cf3b16-f741-3743-8867-e4ee3c7ba428 | -6.61769 | -47.63567 | 2026-09-01 05:16:00 | NPP-375D | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 17d6922c-cffd-3ec7-9dbf-e6bfba297e14 | -4.20992 | -48.60416 | 2026-09-01 05:16:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 703b0bd7-26ee-3bf7-ae92-cc6f90c485cb | -3.11013 | -58.12254 | 2026-09-01 05:16:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e261cd60-99f0-3141-a8ad-42e9049ed84d | -2.67061 | -59.37187 | 2026-09-01 05:16:00 | NPP-375D | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 10407bf8-980a-3db5-a474-b247ffea1b8f | -5.94895 | -57.68419 | 2026-09-01 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 48c1c0a7-959b-36b1-aba8-3a745d05e2f0 | -9.98187 | -53.93378 | 2026-09-01 05:16:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7f90b7b3-3704-3e14-8ab0-d65e5e0d058d | -6.25283 | -55.43113 | 2026-09-01 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6d12198c-d25c-37ab-b837-e8ca663d1cf7 | -6.86958 | -59.03615 | 2026-09-01 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d2eb07b4-88ea-396e-95de-c5c75e7b5068 | -8.50437 | -55.30537 | 2026-09-01 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aad5eb79-5ebd-328f-8e71-e9e3dbb90e37 | -10.87026 | -45.36185 | 2026-09-01 05:16:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 97e859fd-f821-3051-96e7-1304e6757afd | -5.49183 | -57.14195 | 2026-09-01 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c4b2d1ab-190a-3711-8598-44fd0a284a6c | -7.19144 | -60.6855 | 2026-09-01 05:16:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 32e11f91-e44a-33f9-a435-9b1b27a2a219 | -6.52089 | -55.22669 | 2026-09-01 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 92427239-184c-3903-b1cf-39aa7fb2d2ec | -7.5662 | -61.37318 | 2026-09-01 05:16:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b90b130e-4d39-3afe-83bf-6693d6bb087f | -8.93126 | -62.36808 | 2026-09-01 05:16:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 22f6cc75-7a4f-3602-9cb5-c48ce135ed4f | -6.81245 | -59.09067 | 2026-09-01 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 147f792d-fb8c-34e2-a202-387fc0e6a43e | -10.97235 | -48.41092 | 2026-09-01 05:16:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a71de48d-10a9-3100-951c-85e6d55817e9 | -7.52616 | -55.3339 | 2026-09-01 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1330de4b-1b54-30af-8dae-72ee0ed6b287 | -7.35659 | -60.58775 | 2026-09-01 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 14.7 |
| f25add54-dfde-3c60-ac61-8a51c6dd39fa | -7.91305 | -61.33558 | 2026-09-01 05:16:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| ab44e1aa-b7c6-327f-8676-ec314c942825 | -4.15203 | -60.7081 | 2026-09-01 05:16:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7fbffc99-578e-3752-a895-27945c24cfc1 | -9.4759 | -57.02034 | 2026-09-01 05:16:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 974254b8-f0c8-31e7-b550-05f99cfe6002 | -4.29777 | -49.10009 | 2026-09-01 05:16:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ba53ecdf-ba22-35d7-9abe-79cea2d496b9 | -6.62359 | -53.17822 | 2026-09-01 05:16:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9695d812-aaf2-3c4f-ba6d-308898cb6ec9 | -8.58716 | -54.77112 | 2026-09-01 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1fa3cde1-4875-3029-bc2c-8947d6fdba3d | -9.47478 | -57.02738 | 2026-09-01 05:16:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e757b863-b9f6-3a99-bdb1-933b9c7a5397 | -6.0194 | -57.68048 | 2026-09-01 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 15d691f5-2f34-3ea1-bcd0-aa7ad0ec70e5 | -10.86401 | -45.3612 | 2026-09-01 05:16:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8006c0c1-d583-308b-bc2f-36c87d0ee96c | -6.25781 | -55.42122 | 2026-09-01 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c72659dc-6367-3da2-9bdd-b8df2311ea00 | -7.92848 | -44.23084 | 2026-09-01 05:16:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6f23e3be-db41-3b29-b0b5-882d36b0cc10 | -4.22367 | -59.86843 | 2026-09-01 05:16:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 366bf67e-199f-3b89-acfe-fff50ab5b94a | -9.21142 | -60.88091 | 2026-09-01 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9b5d05bc-3f97-3356-9e90-62d90ddfb235 | -7.62372 | -55.29117 | 2026-09-01 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c90cdd5d-02be-3bba-9d19-c9710020e3bb | -5.24694 | -55.90365 | 2026-09-01 05:16:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3c5c3ea1-4914-3e31-b2a2-805949cd05d4 | -5.24417 | -55.89966 | 2026-09-01 05:16:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a51662d2-0a6a-3cfd-9a4e-15d894349e3d | -6.69588 | -55.41164 | 2026-09-01 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d138f15c-6e93-39d0-80fb-35fba5de1090 | -4.34559 | -55.44175 | 2026-09-01 05:16:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f3f39035-9581-3ff4-90ea-63ca6ec871c8 | -8.50107 | -55.34864 | 2026-09-01 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ab6a6d78-e28c-3edc-807f-46fcc96c59c3 | -6.7938 | -55.66645 | 2026-09-01 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b00d51a0-83ba-3bf5-ace7-924bc1ea59e8 | -5.2425 | -55.88874 | 2026-09-01 05:16:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3a072b0c-1f5b-372b-b34f-e6ef7d01eb81 | -5.86095 | -57.56028 | 2026-09-01 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f97067d1-be07-3eaa-bfef-3cbebb9619cc | -9.48749 | -57.02631 | 2026-09-01 05:16:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0336aa2d-8d73-389c-b2cc-2aef4a5d5507 | -9.2046 | -59.55526 | 2026-09-01 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c9bf0a9c-aea2-37f3-823a-7e2654573b3f | -6.265 | -55.4188 | 2026-09-01 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ab2ed103-1a1f-3ec8-bd7b-8cbdc8283bec | -9.97831 | -53.93324 | 2026-09-01 05:16:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3ec6990d-d623-3c41-a7a6-0b1ef2d613b0 | -6.80099 | -55.66403 | 2026-09-01 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 178afb18-c98d-3989-9774-50641d1c21c8 | -7.53573 | -61.37909 | 2026-09-01 05:16:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 82643d43-b961-3964-bba9-3303d2c2c657 | -8.61724 | -54.68915 | 2026-09-01 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3169642f-9029-30d1-be70-d9ecf2dc3db5 | -9.22166 | -59.41011 | 2026-09-01 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 02ac2a52-c2c5-3d4b-8733-ea4707cab84a | -10.58821 | -50.37907 | 2026-09-01 05:16:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 25f82928-a555-3be6-8049-b4cba7b10c0f | -6.60209 | -58.59501 | 2026-09-01 05:16:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b8722525-5491-376f-b91b-049a74621cf2 | -7.48284 | -61.39249 | 2026-09-01 05:16:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1d284d9d-c509-3404-a89f-2e525c95a76e | -6.95018 | -55.641 | 2026-09-01 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 712c22d9-afca-38a9-9c0a-606e3deeac00 | -8.22027 | -54.93487 | 2026-09-01 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 14641a5a-7204-3409-8ba0-c9041578d3c5 | -7.35216 | -55.1946 | 2026-09-01 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ae86df2b-0bdf-3d0b-9e87-e8ee656c5f6f | -6.42665 | -53.56264 | 2026-09-01 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6aa93cbf-feec-3e9d-85d9-5bca8b8b34aa | -6.18523 | -57.73713 | 2026-09-01 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 77c318bb-b549-3d46-a9e4-6d57d3fe15f4 | -7.18112 | -55.48423 | 2026-09-01 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7e40f72d-0248-3b78-bffe-349643a203a3 | -5.87473 | -57.78035 | 2026-09-01 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5b1c467e-b073-310c-9696-ac7d7a32c189 | -6.78496 | -55.67929 | 2026-09-01 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 73c5e916-c692-3be0-a478-bb1084f5ba7f | -8.6269 | -54.69444 | 2026-09-01 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c2eca784-227a-374f-884e-0fd7d8e62b85 | -5.49125 | -57.14557 | 2026-09-01 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 14074eea-1f26-3963-a2fe-3981505872f8 | -10.32489 | -49.11083 | 2026-09-01 05:16:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 224c1e36-577b-3a6e-b442-71c37a5c9799 | -7.03759 | -59.21912 | 2026-09-01 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1cd71fc7-f610-33e5-bd59-ab24a6c1e696 | -6.38409 | -55.21929 | 2026-09-01 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2a17f727-9b05-381e-9cf7-d1bb7f59ad89 | -8.94407 | -62.37032 | 2026-09-01 05:16:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7d26180d-03fa-3a1e-a73b-5cb98d0260ae | -8.13081 | -54.96884 | 2026-09-01 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 3e5646ef-8f5f-31ce-8881-6533d0bbf08e | -4.96648 | -55.83812 | 2026-09-01 05:16:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0b09d622-71db-36f4-818d-3fe468f5e786 | -3.78807 | -52.40763 | 2026-09-01 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 431b8044-b953-34e4-b230-cc6dad18cd5b | -7.03104 | -55.64297 | 2026-09-01 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e46b9158-a033-3f12-b8e4-925bfc001dd5 | -5.89689 | -52.25522 | 2026-09-01 05:16:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0120f738-91da-347d-90fe-7fffdf74aebb | -6.95241 | -55.64848 | 2026-09-01 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 4949dd05-e459-31bc-83bc-0f3aad2f7cf3 | -11.48423 | -45.08152 | 2026-09-01 05:16:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 241579e7-6fc1-32bc-ac37-30841bd07704 | -4.9676 | -55.8525 | 2026-09-01 05:16:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 8109d56a-cbf5-319b-a94f-0cf764b1336b | -6.05692 | -57.64467 | 2026-09-01 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 585c61f6-4b65-3af6-8409-0deaedfd7d13 | -9.40501 | -51.68034 | 2026-09-01 05:16:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1c8623d9-527e-3280-9a6e-01bc2c5e9da5 | -6.95128 | -55.63404 | 2026-09-01 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| eefbf452-02c2-3811-88a9-ac9d4cf9ab0a | -6.12294 | -57.6934 | 2026-09-01 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f45f2c38-bfeb-36e7-901b-fc610fdda4bd | -6.20357 | -42.51733 | 2026-09-01 05:16:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| cf433b14-4397-361d-b2da-38c0f8281006 | -7.68728 | -55.34457 | 2026-09-01 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6239f9bf-f065-329e-b4bc-0c5e794e73c5 | -6.95296 | -55.645 | 2026-09-01 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fadc7c6c-6f59-3698-b189-fd3f30ca1f8b | -10.58376 | -50.37844 | 2026-09-01 05:16:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e138b267-e486-34af-882d-31140b741eea | -7.272 | -46.80828 | 2026-09-01 05:16:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 645145cd-9e9e-3feb-a8d0-84e31c033f6d | -6.94299 | -55.64343 | 2026-09-01 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4d10d3b4-ee59-3cd4-8c07-082700f3ae83 | -6.74315 | -55.45092 | 2026-09-01 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a63f47c1-bc0a-34e3-9fc0-0304a6e99770 | -6.81883 | -59.44058 | 2026-09-01 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5eda325b-bc8e-39c6-80de-8ca94a63fbca | -6.15735 | -57.77854 | 2026-09-01 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f7806a8d-fb29-3656-aae7-bcb7b502cb04 | -6.21049 | -42.5188 | 2026-09-01 05:16:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| f728a941-a401-33ca-aac0-2bb273ab2004 | -4.15844 | -60.72061 | 2026-09-01 05:16:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8b6f4133-e325-3d7e-9a43-119048db2f51 | -4.96318 | -55.85889 | 2026-09-01 05:16:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| dbab8885-bdef-3862-89b9-054d093f98b8 | -8.62283 | -54.85528 | 2026-09-01 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cdab4864-b861-3aa4-8e74-fe9eb985d321 | -8.79062 | -62.49296 | 2026-09-01 05:16:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d6d5ffb8-d8b7-337f-a3b9-e46a5d9d101c | -9.9629 | -53.93918 | 2026-09-01 05:16:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4c4b1239-d68d-3b3b-ba7a-da810458c51a | -4.76999 | -41.7976 | 2026-09-01 05:16:00 | NPP-375D | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 220a3b38-fcb8-35c2-879e-abfa91b7c89d | -8.79132 | -62.48885 | 2026-09-01 05:16:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 48cfb263-6da3-3485-9f3c-8a5434b944b2 | -7.30443 | -60.56372 | 2026-09-01 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |


[Clique aqui para ver as próximas entradas](README65.md)
