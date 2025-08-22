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

## Dados Diários - Página 49

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b7f9bdf9-3e2d-36b6-8854-11616be0d4f8 | -9.21271 | -59.46682 | 2025-08-22 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 896bb2a4-ad2e-3595-b9d6-9f83d8835fd7 | -13.45699 | -47.05412 | 2025-08-22 05:12:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 695d11d7-071f-3d0d-ab72-6a52d331aef4 | -8.96451 | -61.67366 | 2025-08-22 05:12:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2311352a-f69b-3e29-8104-7d5eb254f85a | -12.99814 | -56.87852 | 2025-08-22 05:12:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0341d4bd-5335-3bb0-ac0d-5f1614048179 | -7.08734 | -63.08453 | 2025-08-22 05:12:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1b053135-2c04-3729-921d-82db04b94a0a | -9.51685 | -60.5431 | 2025-08-22 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 689198d7-e7dd-3086-9680-8b1e79407a22 | -13.39908 | -49.1338 | 2025-08-22 05:12:00 | NOAA-21 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8e272df0-9168-3d54-a8f6-d62126ea8ad9 | -9.51214 | -60.55024 | 2025-08-22 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 77e41a49-7d2a-38a6-9294-57641da22bac | -9.22823 | -59.7669 | 2025-08-22 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 020bea22-207a-37d4-b3b2-433d1cab48bd | -12.98722 | -56.88082 | 2025-08-22 05:12:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 55a0dad0-2a88-3d27-ae2c-aa31aac57f9a | -8.60899 | -62.61487 | 2025-08-22 05:12:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1dc3fb08-1a3a-30d8-9623-e3aba6fd73bf | -9.81858 | -64.27186 | 2025-08-22 05:12:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4447093d-ca25-3979-b38f-287f04b83bfd | -7.29761 | -59.62375 | 2025-08-22 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 01ebcb72-e0ad-33c6-87c3-eef98672b9c6 | -9.58095 | -55.35429 | 2025-08-22 05:12:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cc839a71-1739-3448-b7d6-fa19f72b5415 | -9.18388 | -59.62495 | 2025-08-22 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 45155923-2eb3-3666-9571-aab2759df0a6 | -12.92355 | -46.16478 | 2025-08-22 05:12:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 5c603e23-61e5-3b1e-aad3-ba54bf457659 | -13.35884 | -46.25742 | 2025-08-22 05:12:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 62fa2d9c-6045-32a0-b976-23f2b1f7fbbe | -13.0315 | -45.18002 | 2025-08-22 05:12:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5e171dc3-6b2a-3fe2-92e6-4f68c5257d1f | -9.52822 | -60.56075 | 2025-08-22 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 71fe4d7c-5706-39ae-a25b-d11d9745e1b2 | -12.51805 | -57.65673 | 2025-08-22 05:12:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 5cd937b7-de23-3525-b0cc-692c55288154 | -13.02922 | -45.20115 | 2025-08-22 05:12:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 52f180b9-ee5b-317a-83d9-d34805d058db | -12.42875 | -48.70502 | 2025-08-22 05:12:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 86e4ebdd-aba2-340c-9b7c-2be4669d5530 | -9.20658 | -59.46214 | 2025-08-22 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0ff18bdf-c096-3688-876a-e4c7e0eac718 | -7.30102 | -59.62427 | 2025-08-22 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 03b62262-f403-35f4-940d-38db862fbf1c | -13.65381 | -45.70679 | 2025-08-22 05:12:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b78fcfe4-8c05-35b8-be29-902f35becfca | -9.2253 | -59.77719 | 2025-08-22 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 805c2981-3537-3765-9cf3-1d9391c0d7bf | -13.14489 | -46.89762 | 2025-08-22 05:12:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 02a7dcf3-9af5-3235-a6ed-6478430cfe7a | -8.60732 | -62.62482 | 2025-08-22 05:12:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| aa8e9f68-a2f7-3d0f-b5b6-1f8bdd05949a | -13.38697 | -46.24754 | 2025-08-22 05:12:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b323a213-dc0b-3018-8edd-b967f5997b1d | -6.62698 | -58.54576 | 2025-08-22 05:12:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 99676b66-4f57-3602-bc7c-89c515ba98d4 | -8.51673 | -48.82478 | 2025-08-22 05:12:00 | NOAA-21 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0141ab8d-0ac8-369e-84ae-eabf1c5b4549 | -7.45625 | -59.94379 | 2025-08-22 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1cb33921-4b21-35bd-9b8f-3c459c7c5b6a | -9.20265 | -59.46519 | 2025-08-22 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4e4cea00-f713-32cf-ac0a-279ca5dde29b | -9.19099 | -60.76623 | 2025-08-22 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c090504e-c6c9-3164-b4f4-2326c9dcdd54 | -12.95235 | -46.24744 | 2025-08-22 05:12:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 00e49b6b-d85f-3b82-b3b0-d6a1635cdcbf | -10.72932 | -48.22426 | 2025-08-22 05:12:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 24f6c74e-bb53-36e2-908e-0707a5b334ee | -8.5478 | -66.94657 | 2025-08-22 05:12:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a15060cb-eec2-373e-8d10-e167b40ea1e1 | -8.89156 | -62.4296 | 2025-08-22 05:12:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2c3c0558-d23a-31f3-92c4-7c59a19c6d76 | -12.02711 | -57.09378 | 2025-08-22 05:12:00 | NOAA-21 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a936e344-3f94-3419-a7d1-890d8fb9de73 | -9.64899 | -59.65615 | 2025-08-22 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 432be5cb-3da1-3fe7-a0c8-1c0be660b80b | -8.55106 | -66.95312 | 2025-08-22 05:12:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b65db769-b857-362d-9404-862f703d8aeb | -9.88358 | -60.2942 | 2025-08-22 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 7e3f86ce-699e-38c5-b95a-557ee0f677b1 | -9.1962 | -59.63432 | 2025-08-22 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 03430aad-20de-3403-b59f-76b57466ceb9 | -13.1466 | -46.89358 | 2025-08-22 05:12:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d4e8630e-c733-3014-ab90-c9464a25866c | -13.02364 | -45.18633 | 2025-08-22 05:12:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b82469f2-beb6-31a2-ac10-0116ba0c3f7a | -12.97919 | -56.88749 | 2025-08-22 05:12:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bccd7cbf-89f5-3619-a979-b3b557da4ded | -13.00162 | -45.23697 | 2025-08-22 05:12:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 9ea280a1-1d50-307c-9d8c-1d24530e1d74 | -12.96188 | -46.28397 | 2025-08-22 05:12:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 7d287bf2-7dd6-3a5d-89f9-b4af75e08dfe | -7.04922 | -59.83352 | 2025-08-22 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ac8dbaea-2b93-3d31-a332-ef2550082273 | -9.58512 | -55.35077 | 2025-08-22 05:12:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| baaef850-2939-3f06-8ca8-f32acaf53901 | -9.59528 | -55.35152 | 2025-08-22 05:12:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| b0924986-a6a8-3367-9e0d-044bc6e02954 | -9.21549 | -59.47096 | 2025-08-22 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 397388d0-cf4f-3273-9427-fb5cb590b443 | -10.11419 | -57.75876 | 2025-08-22 05:12:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 14ba3990-66d8-3643-af1d-df6c53bc2b8b | -12.4945 | -53.80379 | 2025-08-22 05:12:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1bfde9f1-2f3a-3430-9697-f053fc84749d | -6.6281 | -58.53872 | 2025-08-22 05:12:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cb1f377a-95c8-30b7-93d0-6f54fc365a07 | -10.96922 | -61.56202 | 2025-08-22 05:12:00 | NOAA-21 | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 944d7117-34f4-31c7-8c13-f4c0d833318e | -10.72827 | -48.23266 | 2025-08-22 05:12:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c1ccb44f-ac0d-3704-a834-5c86809c50d6 | -9.16321 | -59.60307 | 2025-08-22 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c3560164-a15c-3d96-b519-f6d889d27447 | -13.00502 | -45.22647 | 2025-08-22 05:12:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 62233b16-84aa-3bea-bd19-3e5264144bdc | -11.31711 | -55.22731 | 2025-08-22 05:12:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 43652046-118a-386f-b1d2-0031c05c25f0 | -12.99758 | -56.88237 | 2025-08-22 05:12:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6bf97d6d-d701-3573-9dfb-e7365df68caf | -7.5969 | -55.19139 | 2025-08-22 05:12:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4e014e64-1f71-3b4b-9fd8-cd4cee719e66 | -7.56068 | -63.85804 | 2025-08-22 05:12:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8ba751dd-ae42-3b1a-9f4c-21b661f96b85 | -9.95869 | -64.86487 | 2025-08-22 05:12:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8f19513a-3b4a-3a73-96eb-855a561a9ec9 | -9.46645 | -60.37394 | 2025-08-22 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2adb13ff-7812-3aa4-9e74-7a3295f88d48 | -13.16416 | -46.91168 | 2025-08-22 05:12:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c5673ee6-4910-371f-a976-a6827005b8fa | -9.21398 | -59.78286 | 2025-08-22 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 598e40f0-5c8a-3bd8-8c36-853df35bdc42 | -9.23042 | -59.77473 | 2025-08-22 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e2094dc4-706c-3724-8abc-a6e281a699ef | -9.21721 | -59.46019 | 2025-08-22 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3eaf7f33-6460-3532-bb77-7d1937f06c50 | -12.92688 | -46.16914 | 2025-08-22 05:12:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| e3ef0985-5f28-3a3f-9d40-05522d77cd98 | -6.31388 | -59.88684 | 2025-08-22 05:12:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| da9e8501-0347-35a3-b225-b66e0f090ea5 | -9.18492 | -59.63997 | 2025-08-22 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3937130a-f455-3477-8368-75dd6da6aa6c | -13.45987 | -47.04843 | 2025-08-22 05:12:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8fa9e1f2-9de5-336f-85d7-05e0b3d97a1f | -9.20945 | -59.44421 | 2025-08-22 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7b15e832-1e30-392f-afe3-17014232fae7 | -13.02899 | -46.32559 | 2025-08-22 05:12:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 90859720-95c4-3b83-9ad4-76913778e3a7 | -13.03224 | -45.17315 | 2025-08-22 05:12:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 48f15eff-6cae-367f-8366-a598bb88026c | -9.18238 | -59.59128 | 2025-08-22 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 70a1661a-68f2-3190-a594-317f68fb25b7 | -9.21328 | -59.46324 | 2025-08-22 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bddc1707-fbf5-3dba-b90e-465eb6a1494c | -9.58401 | -55.35393 | 2025-08-22 05:12:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 30f47a2f-bb27-3890-b9f6-d20f92ba486e | -13.02439 | -45.17934 | 2025-08-22 05:12:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4abab7b8-dd62-3c3c-a1f3-bef899363917 | -9.17331 | -59.6047 | 2025-08-22 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d496645e-4659-3857-96d3-f08990844986 | -9.20715 | -59.45856 | 2025-08-22 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 49765d13-7673-3591-9478-865dac5e9d84 | -12.9815 | -56.8957 | 2025-08-22 05:12:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4a3bc3af-8b6f-3707-bbd5-840365881ac8 | -12.92814 | -46.1843 | 2025-08-22 05:12:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| dad1fdc4-dbc1-3aad-b697-200f61e1f7d9 | -10.86923 | -50.85265 | 2025-08-22 05:12:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 13.2 |
| d4e66a41-06c2-3dce-bf47-6f8ee1194cb5 | -13.02916 | -45.17669 | 2025-08-22 05:12:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ea377aac-96c4-3071-bdcc-84789198aac5 | -13.64691 | -45.70569 | 2025-08-22 05:12:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6f6c90ce-8b7a-3d5f-9701-ceaaa1a3c57c | -12.50104 | -53.81591 | 2025-08-22 05:12:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c3793862-2d24-3fe4-b24e-f0eb0243e37a | -12.92617 | -46.17589 | 2025-08-22 05:12:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 98865548-f1bd-32b4-abf8-479804957228 | -9.52724 | -60.5448 | 2025-08-22 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 1a06ac2e-78cd-3c25-86da-779a16b5a5d2 | -7.05451 | -59.82272 | 2025-08-22 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c792d8f3-6843-359e-9958-09da3d0739a5 | -10.46346 | -59.1344 | 2025-08-22 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 84623344-503d-32ff-9cf4-ecfdf164cdf9 | -8.60119 | -62.61357 | 2025-08-22 05:12:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ce3398cc-54f5-3145-aa43-a2273173dc9e | -9.31082 | -57.01667 | 2025-08-22 05:12:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| af0a7ea8-c574-33af-aacd-72ac87a39617 | -9.63253 | -48.33317 | 2025-08-22 05:12:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 049ab977-8996-3e78-97c2-7424c57fe8a3 | -12.99469 | -56.87801 | 2025-08-22 05:12:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1ac58900-b967-3187-ad3a-5726f45fd0d5 | -7.77738 | -66.95438 | 2025-08-22 05:12:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 20710f0f-f647-3403-8206-b01d368940b2 | -12.99356 | -56.8857 | 2025-08-22 05:12:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3c295546-e2a3-3a01-94e4-5255a626d204 | -7.55638 | -63.8573 | 2025-08-22 05:12:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d7793230-1b15-3502-a6a3-a9f4193341a5 | -7.55278 | -63.85247 | 2025-08-22 05:12:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README50.md)
