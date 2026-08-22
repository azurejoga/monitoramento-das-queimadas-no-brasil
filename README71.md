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

## Dados Diários - Página 71

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 99b3aa3f-02ee-32d0-9e12-21b0e65303a7 | -10.77255 | -51.0048 | 2026-08-22 05:25:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ab84f7a1-8ac9-3986-9f5e-936c5b5578a9 | -8.38702 | -62.68602 | 2026-08-22 05:25:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 28.2 |
| a07e86d7-839d-37d4-851e-dd9acdc8ff93 | -9.22085 | -60.7769 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e133cf0a-2394-3d4e-ac74-ab6e46b33cda | -8.40497 | -62.68898 | 2026-08-22 05:25:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7c0475d8-c8c0-3f60-8415-b2757d302fb7 | -9.43267 | -51.61655 | 2026-08-22 05:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 338116f2-16e4-3ab2-aea5-323e560f566a | -9.42451 | -51.64012 | 2026-08-22 05:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| e0647b90-a1b4-3cc4-9d52-9912a5126337 | -8.89794 | -60.54317 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 19.2 |
| a80059a7-9233-379b-9637-775a97db2f69 | -9.10911 | -60.92281 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ea067b7d-5db9-3772-99a7-eac3a21a7e06 | -9.41519 | -60.56195 | 2026-08-22 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a1ac6d25-b895-332e-a7b2-dca105a916ad | -9.18277 | -59.45786 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 8441a690-fb08-3448-8ede-f57c79627b94 | -15.20274 | -52.77458 | 2026-08-22 05:25:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 46abd479-ed34-3e7e-ac30-e23c2c5d439c | -10.75668 | -50.26096 | 2026-08-22 05:25:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c85becae-c3b3-3a87-be92-5f716ed377c5 | -9.43691 | -51.62314 | 2026-08-22 05:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 75137191-708d-3671-b717-20a8c14d629b | -8.69322 | -62.87492 | 2026-08-22 05:25:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 66eb3716-901f-39be-b86b-008483faab49 | -11.59513 | -46.58779 | 2026-08-22 05:25:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 893db3b4-c178-3bb6-b0aa-946871457baa | -9.04766 | -60.43723 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4b8d0b48-bd40-33ae-8f98-416d38c01918 | -9.17891 | -59.46081 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 0d1e66b8-d3a2-3ad3-8b35-44386bfc8402 | -9.05486 | -60.4348 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5e3e988a-c5d6-32bf-b0d4-c445cdbbb875 | -9.46419 | -60.55215 | 2026-08-22 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b9df4b60-1099-33c6-ac3c-29833a15fb50 | -9.17062 | -59.44876 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0f2ce6a0-de82-3e74-bf4a-e8e39c1afaf4 | -9.4113 | -60.56493 | 2026-08-22 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fcfd2313-62af-3da5-b2bf-3c5437a7316d | -9.41488 | -60.43579 | 2026-08-22 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 619d4c5a-7b52-316d-b323-3173bd4d7f96 | -9.52357 | -60.50052 | 2026-08-22 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9f8436db-eaef-301f-aa30-b8b6618e490b | -7.87014 | -63.76703 | 2026-08-22 05:25:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4bca42c4-132f-3742-99c4-a375f685c219 | -15.67971 | -53.78115 | 2026-08-22 05:25:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| baf02629-3c1d-3187-83e6-9bc4db5e4811 | -9.36026 | -61.02648 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4c66cdcf-3289-3bd4-8e1b-6ab9070e5e23 | -10.94767 | -51.42035 | 2026-08-22 05:25:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 835f0512-828b-3fc1-a960-1b5940029ba3 | -9.169 | -59.48067 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f2de0701-3ca9-3629-b281-cda817989e4c | -9.10634 | -60.91869 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 2ebe3599-6c9c-3552-b480-4693058fab5a | -9.19435 | -59.44897 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d9acd75a-1ed6-3952-bdfd-5a7a5266ebd1 | -8.39488 | -62.68306 | 2026-08-22 05:25:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| da5c399a-9176-3970-8ab7-d7ee8e13060f | -9.40552 | -60.40909 | 2026-08-22 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d8bdc034-2289-3e94-9eb8-9ad576aa425b | -9.21886 | -59.76706 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 825f5a85-47a1-38fb-bfe0-dfc080263306 | -10.68398 | -50.30455 | 2026-08-22 05:25:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| bf15bd3f-fc60-3b4e-a693-f2107d0f6991 | -8.8985 | -60.53964 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 19.2 |
| e1e7cc50-35e3-351d-bd90-ecd8d3a6f907 | -9.53816 | -63.56439 | 2026-08-22 05:25:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 604bb1b9-2f32-3ca6-a591-4888f83dd863 | -9.11669 | -61.59245 | 2026-08-22 05:25:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 77c43a4e-bea1-317c-bdb4-a353c7340a70 | -8.89128 | -60.54208 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 21.4 |
| 77e4721a-c9d1-3d86-abe1-3b36bc53d928 | -9.40936 | -60.4277 | 2026-08-22 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bfa2f900-2b76-350b-b6b9-2b97e5e4b379 | -8.95553 | -60.58868 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d57bc82d-7878-3c11-abc0-3dfbb8700d57 | -10.27613 | -50.37729 | 2026-08-22 05:25:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c34fbf0d-2163-3cac-a4bf-7c3c0055a519 | -9.19049 | -59.45193 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 134f6c02-32fe-3c4a-b992-36087c48e5c7 | -10.79577 | -50.98141 | 2026-08-22 05:25:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| caed9eff-76ce-3597-ae42-4991af394e5a | -11.10483 | -49.89414 | 2026-08-22 05:25:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e4bf5fc9-807f-3329-8395-0827da782c74 | -16.03513 | -52.17217 | 2026-08-22 05:25:00 | NOAA-20 | ARAGARÇAS | GOIÁS | Brasil | 5201702 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5037c79d-e2d2-33e6-a223-02ae3e9b318f | -9.19372 | -60.28837 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 48b29cb1-c8e2-31d9-9857-1d8a2234ad96 | -16.50471 | -55.18563 | 2026-08-22 05:25:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 73ee98bd-d7c7-31e2-b762-12a7679ff7ae | -9.10299 | -60.91814 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b1f98cca-b5be-3610-9ac5-9d4839619f7e | -9.38916 | -60.5541 | 2026-08-22 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6d2820e5-6e4d-3009-8c23-f9dd25ad5f82 | -9.04597 | -60.44773 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f470da2f-5458-3445-8f48-a5831ea42ce9 | -9.43232 | -51.61761 | 2026-08-22 05:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fd0e057e-fdfa-34be-8279-7d19c947ea29 | -9.12752 | -61.59042 | 2026-08-22 05:25:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 90731d98-ee74-3e81-bea7-877892a1bd69 | -9.11829 | -61.60418 | 2026-08-22 05:25:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7bb628b8-b507-3860-a83d-27b01198dc6c | -9.43373 | -51.60848 | 2026-08-22 05:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3983d5ad-c902-3bd8-a563-fb1e3ff2f7d4 | -14.50192 | -59.8265 | 2026-08-22 05:25:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2655d8f9-c195-387c-94b5-ed960ae5863d | -8.89608 | -60.59713 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c4c80a2b-1175-3be5-b780-2c33d4600f3c | -9.41436 | -60.41772 | 2026-08-22 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0aaa9e5b-2ddf-3c22-8488-915417f523c9 | -10.03781 | -59.46183 | 2026-08-22 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f8e07f66-60b9-32d6-8dae-54da8aa311cd | -10.30156 | -48.22898 | 2026-08-22 05:25:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 167e2c50-a115-37ab-b909-284bbc96810b | -10.79647 | -50.98751 | 2026-08-22 05:25:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 96599d0a-186b-3c4b-8bfd-13d7b2870551 | -11.63149 | -46.52012 | 2026-08-22 05:25:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2d8a5dd8-b1c9-3dcc-b912-753ff75cc4cd | -7.39481 | -64.63091 | 2026-08-22 05:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e949c5a2-1613-32d0-a9a3-30e098f8ced4 | -9.19103 | -59.44844 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 911d1934-d9aa-31a5-925e-145fae5e08e9 | -9.24368 | -59.80315 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3841245d-0f4e-3509-a941-e4fdb8ccad77 | -11.13536 | -49.04419 | 2026-08-22 05:25:00 | NOAA-20 | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b1485671-b85f-35db-ab9f-718b82a4a384 | -9.40164 | -60.41206 | 2026-08-22 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4e243a86-6638-34db-a688-a4fa1ad7c61c | -10.30265 | -48.22035 | 2026-08-22 05:25:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 24839a53-ce10-355e-84d9-9114b2392283 | -9.40384 | -60.41961 | 2026-08-22 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 29971bf5-c5ac-3ce9-8664-6dacdf44f7f8 | -8.40138 | -62.68839 | 2026-08-22 05:25:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7259966b-77ca-3816-85d8-4a53441b1864 | -9.21141 | -60.77171 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| df42fa2e-cc20-30ad-acb2-b19475e9f709 | -9.87702 | -60.79652 | 2026-08-22 05:25:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 123c819b-764e-3524-aa4c-fcf3de8a4c31 | -9.52689 | -60.50106 | 2026-08-22 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1daea79e-12b8-36f7-b710-d3a7576aa58d | -9.40608 | -60.40558 | 2026-08-22 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 38649f2d-f46e-3d44-bb9c-73e64ed972b4 | -11.59588 | -46.58112 | 2026-08-22 05:25:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b912b8ab-06c3-3ecf-b762-f014dd4872bc | -10.9043 | -50.23729 | 2026-08-22 05:25:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 078cd230-5fc2-3f25-b725-bc25cb8dae99 | -15.2024 | -52.77742 | 2026-08-22 05:25:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0218aed3-0aac-3d73-b6d5-4f6ae6cedaaa | -8.95384 | -60.59928 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 263d0cd2-f5f7-304d-a1d0-56af3a25fc81 | -9.40185 | -60.58145 | 2026-08-22 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d01bff8c-14c2-3b99-8383-079c392eb539 | -8.68961 | -62.8743 | 2026-08-22 05:25:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2e4bb7b5-a45c-3539-b981-279b1cc6868c | -9.40716 | -60.42014 | 2026-08-22 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6bacaba9-bd1e-3205-8286-63248a1fc1ef | -10.27062 | -50.37656 | 2026-08-22 05:25:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c57794b6-0aaf-33d7-aaa6-b18260c21dc7 | -9.16566 | -59.45869 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 84a4d0fa-a3c7-3df7-abe9-d0292f106613 | -9.17781 | -59.46778 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7ccb450b-cbb7-312f-86ad-6489cca78a71 | -7.67511 | -61.11466 | 2026-08-22 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bacfc641-5ec1-36a0-92e4-473e01907cd2 | -9.3886 | -60.55762 | 2026-08-22 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a258fc01-ade1-3a7d-be21-308d395db81a | -7.75022 | -61.08531 | 2026-08-22 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 05fc4293-974c-306a-aa79-0cb1640362c9 | -9.21 | -59.77993 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bdab03cf-6104-3e84-82a6-36bc801657a2 | -7.87413 | -63.74318 | 2026-08-22 05:25:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0f188320-ac6e-34c1-8ff1-1b84f1502ceb | -15.2453 | -52.84316 | 2026-08-22 05:25:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 06263456-5716-34dd-9957-48c9d9c9dc45 | -10.045 | -59.45937 | 2026-08-22 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a6e3ad86-4763-3d48-99d3-0cb7547de96d | -10.89314 | -50.28196 | 2026-08-22 05:25:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0cfe96f7-5ba6-39f5-b5bd-812b1a7614ae | -9.1787 | -57.00287 | 2026-08-22 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b93057fc-ab3f-3e23-8018-0be040ff5470 | -9.43728 | -51.61864 | 2026-08-22 05:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5c17bb39-c588-32f5-9772-34e427648405 | -8.67574 | -54.76081 | 2026-08-22 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b985bc79-c2a0-3657-8058-e652fb8eed37 | -9.41271 | -60.40666 | 2026-08-22 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e5704dac-a520-34f1-be8d-13c9ca14cc3d | -9.4394 | -51.60413 | 2026-08-22 05:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c92e4383-6a04-3003-9ae2-cf2f21201577 | -9.39394 | -55.98334 | 2026-08-22 05:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4c896087-ca34-3924-8640-44572dc7f66d | -9.03933 | -60.44667 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3ef73ed7-ce3b-32d1-94e1-3ce03f607cfe | -9.17779 | -59.44633 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.1 |
| bcb099b7-13c3-37eb-9140-8ab53ebcc2ac | -10.89985 | -50.24047 | 2026-08-22 05:25:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README72.md)
