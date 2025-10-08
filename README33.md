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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 79e8bbea-e0a8-312a-bf95-544e0cc6b762 | -6.4259 | -47.24182 | 2025-10-08 04:17:00 | NPP-375D | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d15ac6a0-c55b-3d1b-a214-38d138e9ee75 | -12.01374 | -45.1945 | 2025-10-08 04:17:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 39485600-669a-38dc-957f-537fa796ec0e | -11.18248 | -54.89859 | 2025-10-08 04:17:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 965b56f0-5abe-39f6-ade2-b5e0e4884292 | -11.17337 | -54.88313 | 2025-10-08 04:17:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 09279406-ad89-3048-8fcd-7170b105386b | -11.34254 | -44.88045 | 2025-10-08 04:17:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 22898e1d-f308-3f02-8a33-559e061cde19 | -11.67321 | -50.96906 | 2025-10-08 04:17:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5e4634d2-d063-3a0c-88d4-0bd7f62f4cc8 | -7.70193 | -42.38891 | 2025-10-08 04:17:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c06b9a12-9c4a-3ed0-9d3e-2c1e61cf8fe7 | -13.33735 | -47.56053 | 2025-10-08 04:17:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 0c5c9ba1-1e16-3f61-80d8-8df537dd2889 | -7.67532 | -42.58085 | 2025-10-08 04:17:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| e3e6f5d4-4a9d-3832-9fad-4b659d548c37 | -11.11214 | -54.03775 | 2025-10-08 04:17:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b4f31005-8a47-3120-822e-31e85d83d0b4 | -7.43755 | -43.14302 | 2025-10-08 04:17:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 0a1ceea0-e4ac-3720-ae36-6fc9aea43ad9 | -11.17996 | -54.8802 | 2025-10-08 04:17:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3a138e76-672b-3a3e-8bc7-2aa7f1a391d9 | -11.72646 | -50.94086 | 2025-10-08 04:17:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| db0560ed-7a0e-308b-aa30-830fb8950137 | -12.91606 | -46.83899 | 2025-10-08 04:17:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b036afe2-a242-3c83-9601-6417e8fed4fe | -12.63598 | -50.56024 | 2025-10-08 04:17:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3357f8c8-f13c-331c-829c-00ca26b38703 | -5.2494 | -43.15989 | 2025-10-08 04:17:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 484f9a14-afb8-3799-a37d-49be99c6797e | -4.8717 | -46.82825 | 2025-10-08 04:17:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bb2094e3-752e-3973-8635-0e474a3dd1a3 | -11.18411 | -54.89004 | 2025-10-08 04:17:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| cbf50350-9dad-3b0b-953b-3ee697d73520 | -11.8581 | -44.9212 | 2025-10-08 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8adb7822-fc3e-33ab-8337-e7a5c7766dad | -11.9055 | -46.20581 | 2025-10-08 04:17:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 476c8d40-b397-3a16-bd78-dda419d13006 | -7.63643 | -43.05975 | 2025-10-08 04:17:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| d0c7c7ab-55e3-3a0c-a4ba-9d637e029214 | -11.75883 | -45.13464 | 2025-10-08 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d55b4b39-280d-3b9d-a789-6d62857c3a59 | -11.18157 | -54.89606 | 2025-10-08 04:17:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 07729d80-6234-3568-a43c-96fdce23af64 | -11.1642 | -54.86211 | 2025-10-08 04:17:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3a23c87b-16ef-323d-9058-979ba8a543c5 | -7.45027 | -43.12719 | 2025-10-08 04:17:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| f1fe8d06-8d0b-383d-9772-cfbed063a5fd | -10.99619 | -51.25404 | 2025-10-08 04:17:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e162f4d2-9a9e-37ad-8fc1-38c6420d6e76 | -5.84553 | -44.30605 | 2025-10-08 04:17:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e61e8588-e366-37ce-8049-51f3c5db8faf | -11.18242 | -54.89178 | 2025-10-08 04:17:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 96630ad8-2d11-3c78-98b9-6e6153a5b8b8 | -13.05879 | -47.94771 | 2025-10-08 04:17:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 96f58383-4080-360c-9ef9-20b3685b77e1 | -5.1332 | -44.95977 | 2025-10-08 04:17:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 17b7e828-c227-305a-9a0e-0da94cb905ad | -5.76018 | -45.75264 | 2025-10-08 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a7d90946-184f-3e8d-b06d-dac0f29836b4 | -5.88997 | -49.37274 | 2025-10-08 04:17:00 | NPP-375D | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a2f526b5-d9ac-3995-8adc-2caa59eb8194 | -5.71311 | -45.68328 | 2025-10-08 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 64b6fcdd-a270-35a4-bf87-f9a2da8e24c2 | -13.08419 | -47.93013 | 2025-10-08 04:17:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f047bf9f-5149-311a-9938-5d36bf10e726 | -11.17421 | -54.91022 | 2025-10-08 04:17:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b6006684-9d6e-32dc-9537-e82aa0062633 | -11.33186 | -56.20618 | 2025-10-08 04:17:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2456c9a2-da00-3c43-b8c4-a9d43330a5eb | -5.8675 | -44.29856 | 2025-10-08 04:17:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 329b75f6-e8e8-32f8-904d-6f8da76ffcc9 | -11.44496 | -50.20498 | 2025-10-08 04:17:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| adc1c465-edbd-3bf8-9af0-05290d8398d3 | -11.11342 | -54.03748 | 2025-10-08 04:17:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a24d3366-09df-38bb-b11e-5055475a6eb6 | -13.2824 | -48.03971 | 2025-10-08 04:17:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2b8aa4ff-1a4a-351a-bf85-b364ef91a468 | -9.04314 | -50.62475 | 2025-10-08 04:17:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bcda5eb3-ed2d-37c2-9495-3167f88282ca | -11.85199 | -44.91656 | 2025-10-08 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| df4d3a59-e8c2-322b-ad8a-cf0ed3346d36 | -5.71247 | -45.68723 | 2025-10-08 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 18f17adf-4de9-3d52-b37c-f6e52352a0c6 | -13.06637 | -47.8373 | 2025-10-08 04:17:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ffbba71d-59e8-39ac-9205-0eb8952a76dc | -11.11826 | -54.04208 | 2025-10-08 04:17:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e111d081-2e49-352b-9497-444b073049f2 | -4.49579 | -42.85999 | 2025-10-08 04:17:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 12.9 |
| a9c8fbc0-ebaf-317b-8714-423ff8d19360 | -11.77219 | -45.13687 | 2025-10-08 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0a273adc-4a58-3bd9-9b6e-a5e095d089de | -11.43999 | -45.07458 | 2025-10-08 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 33fc3fd5-3a2d-309d-abc9-4ccd55960b0d | -7.78893 | -42.62408 | 2025-10-08 04:17:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 5c7c0361-2b49-3572-8389-014286eeddb1 | -5.02255 | -43.6566 | 2025-10-08 04:17:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6c10817c-06ba-39d0-a3f3-0830c97b2287 | -12.14162 | -39.68124 | 2025-10-08 04:17:00 | NPP-375D | IPIRÁ | BAHIA | Brasil | 2914000 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| a5ff3fc8-eab5-3a06-9ed3-7862dbe3444b | -4.82055 | -46.00525 | 2025-10-08 04:17:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 78c49153-7f14-345f-9fee-671ba02d5e9d | -7.79501 | -42.60696 | 2025-10-08 04:17:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| d1963bc3-a31a-302a-a39c-f6ceb8ef2ff3 | -12.94186 | -46.85553 | 2025-10-08 04:17:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 608b66c3-eaf7-308a-966a-9b2c1ffd0abd | -7.62257 | -43.06115 | 2025-10-08 04:17:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 9f0927d2-b34c-398a-82ec-7f2463579684 | -5.39115 | -40.98244 | 2025-10-08 04:17:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| dad1f47b-4fed-3f96-9542-93f52d542e12 | -9.77515 | -48.29324 | 2025-10-08 04:17:00 | NPP-375D | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 9d560f57-5116-39a7-af9c-8a4194399e8a | -6.32291 | -41.61132 | 2025-10-08 04:17:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| fc422ac3-d0ee-34b7-8573-ede29d51f217 | -12.24921 | -47.87076 | 2025-10-08 04:17:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 5efe995b-c216-36bf-8858-d3124cd204c0 | -5.02797 | -43.65753 | 2025-10-08 04:17:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8dbbe3f2-3eb2-30f8-aa7a-732765e1af90 | -5.1447 | -44.96447 | 2025-10-08 04:17:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 66be301b-83aa-3813-80a9-9f82fabec5c5 | -13.03333 | -47.92164 | 2025-10-08 04:17:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1aa5447e-318f-3ecd-9fbf-f339f2e3c69c | -11.87241 | -45.74854 | 2025-10-08 04:17:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4ac4678a-35b7-3b1c-970f-5bae63e429cc | -11.18492 | -54.88578 | 2025-10-08 04:17:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| ffdd4e2a-d5c6-348c-b0c9-70e964cda9ee | -7.69074 | -42.39443 | 2025-10-08 04:17:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| cfe2547f-c2b4-3ad6-a0b4-02a32e70e2ea | -13.23368 | -47.79464 | 2025-10-08 04:17:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2d22ed96-9d75-3908-89a4-3cb4207f4807 | -12.71769 | -44.37855 | 2025-10-08 04:17:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b6ffec2c-1567-3583-acd9-aa1d10f05d93 | -11.4209 | -56.29567 | 2025-10-08 04:17:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 81cb8a3e-b17b-30b6-8683-57c94293465c | -7.24689 | -44.15023 | 2025-10-08 04:17:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ea0a574c-6790-3a07-8523-06e215ebf80b | -6.30227 | -45.13735 | 2025-10-08 04:17:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 02d8edbd-5e10-3e6a-bd18-1afc76efd860 | -7.62923 | -43.0622 | 2025-10-08 04:17:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 688b21ff-d63a-32c8-bf24-a861da629bab | -5.73649 | -43.61118 | 2025-10-08 04:17:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e5c8e67a-b990-3d6b-8b98-67255256007a | -13.00192 | -46.78246 | 2025-10-08 04:17:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 743f79b8-d2b3-3463-ba3c-48da14d58bf3 | -12.3956 | -51.13421 | 2025-10-08 04:17:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 78563f69-72ff-3759-b5f0-4006c5443a22 | -13.07079 | -48.00978 | 2025-10-08 04:17:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 98dbd3d6-0c3e-30c8-9675-7dd3868ae6aa | -10.34496 | -50.25596 | 2025-10-08 04:17:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 60886e64-bbcb-3cb0-86e3-ebc5216c21e6 | -6.66894 | -41.38217 | 2025-10-08 04:17:00 | NPP-375D | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 3e4d275e-a18e-34f3-a40d-ac2f7ee926c4 | -2.52224 | -44.12265 | 2025-10-08 04:17:00 | NPP-375D | PAÇO DO LUMIAR | MARANHÃO | Brasil | 2107506 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 3d570ea4-2b82-3d46-915b-f8f9a3ecdd27 | -13.01966 | -47.91425 | 2025-10-08 04:17:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f1eeb714-d1fa-3eaa-8180-358dac410afa | -12.91195 | -46.84225 | 2025-10-08 04:17:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d1d8af10-5b48-3766-9cca-b1e4663d75f7 | -8.15143 | -38.62946 | 2025-10-08 04:17:00 | NPP-375D | MIRANDIBA | PERNAMBUCO | Brasil | 2609303 | 26 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 5f9b99de-aca8-3a33-bc31-880d7641bf78 | -10.68427 | -40.4946 | 2025-10-08 04:17:00 | NPP-375D | ANTÔNIO GONÇALVES | BAHIA | Brasil | 2901809 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 65484a35-989f-3488-9179-c30d0007ba36 | -12.39196 | -51.1289 | 2025-10-08 04:17:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fbc57873-ddef-3b3f-a016-fc54e5c0ac7d | -12.32415 | -50.27767 | 2025-10-08 04:17:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3cf2a2e3-15c7-365d-b9ec-b08125a4ed45 | -5.1899 | -45.95881 | 2025-10-08 04:17:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9110ee60-ad6e-3f74-bca6-c44a1d7b7732 | -4.49587 | -46.3673 | 2025-10-08 04:17:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 8a211a12-729a-397b-bf14-d1883b4056fd | -12.13834 | -45.59436 | 2025-10-08 04:17:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 95033f97-d8d5-38ea-a0c4-6a00d0d89474 | -10.90853 | -47.13977 | 2025-10-08 04:17:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cfc74019-d2df-32fc-b9be-043dac8ec5f2 | -7.73865 | -42.7565 | 2025-10-08 04:17:00 | NPP-375D | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| e5871455-8cd8-3671-a836-6936bf576038 | -12.36577 | -46.49227 | 2025-10-08 04:17:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f3b8e2db-9d3e-3915-8667-0deebb00e84a | -3.90088 | -44.90966 | 2025-10-08 04:17:00 | NPP-375D | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| f083f115-c4f2-3e41-a3a5-8f41c56fbe4f | -4.84937 | -45.759 | 2025-10-08 04:17:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9e8ecb31-75c1-32aa-9c68-5ed6bd245336 | -11.71676 | -50.94361 | 2025-10-08 04:17:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7aa825fd-2e12-3b6d-9612-96981ce2e2d7 | -7.01005 | -42.86846 | 2025-10-08 04:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.1 |
| 178d0555-a451-36f2-a3fa-27995494b695 | -11.71993 | -50.97644 | 2025-10-08 04:17:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4beea685-a904-3456-b1bc-5a8963e146d4 | -11.71268 | -46.36101 | 2025-10-08 04:17:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9c07622e-58f5-31b2-bb93-5de6b99839d7 | -5.7326 | -43.61413 | 2025-10-08 04:17:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1c580b32-4e4c-341f-87a5-3079e57384a0 | -3.14635 | -50.30385 | 2025-10-08 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| e4e12a57-d747-3cc6-8645-89e17ca0fa50 | -3.09957 | -47.01215 | 2025-10-08 04:17:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9170f57f-d9c9-36ef-ac81-06b9995954de | -5.80558 | -44.89807 | 2025-10-08 04:17:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README34.md)
