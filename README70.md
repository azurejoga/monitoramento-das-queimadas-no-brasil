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

## Dados Diários - Página 70

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 37791053-6fc8-3719-9add-61e806591ee5 | -11.64601 | -45.32816 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| caaf1f74-a851-3736-9a9c-de9c22d16b17 | -14.71773 | -45.15163 | 2025-10-01 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| abc3571a-7498-310f-93be-c4dfa954cca8 | -15.17391 | -46.41994 | 2025-10-01 04:21:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c525cd17-902c-3e3f-b7c5-d7e523eeda72 | -12.39809 | -44.76627 | 2025-10-01 04:21:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c97d2b89-c5a9-3982-bd35-29c56d7c3452 | -11.74129 | -46.86638 | 2025-10-01 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d4f5faa3-c8ec-3baf-8cdf-40b384999971 | -12.78804 | -46.85718 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 45c78c7e-ed9f-3f0e-ba41-b780bf093a62 | -12.76183 | -48.24923 | 2025-10-01 04:21:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7c3c0981-00b4-3d8c-92ee-63be1f10e767 | -9.4276 | -54.5675 | 2025-10-01 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d6b87290-e962-3c29-88ce-2a85e99c4eb7 | -12.15433 | -47.77046 | 2025-10-01 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 14fc380a-f8e0-32a3-a9ad-d1e4271985e9 | -14.9003 | -47.2088 | 2025-10-01 04:21:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 86df4380-9387-3ad0-b764-e347474419ca | -14.14711 | -49.19805 | 2025-10-01 04:21:00 | NOAA-21 | NOVA IGUAÇU DE GOIÁS | GOIÁS | Brasil | 5214879 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e9a62b34-30df-3870-8c9f-5104bf4eddba | -14.4951 | -48.4462 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| b32f1f05-341d-35e1-ad1a-6bc2946780b1 | -12.96251 | -47.17099 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| af51dd59-f6a6-3497-94b6-833446a16e19 | -14.68396 | -48.23602 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f9208020-e8c8-3d9a-b36a-c3d7cdb0d687 | -13.23411 | -47.32597 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 275f066e-489c-3965-94b3-b9130c049c9c | -14.96604 | -46.88095 | 2025-10-01 04:21:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f1f5b211-5bcc-3aae-a1e2-48c463b2cf30 | -13.77201 | -51.22713 | 2025-10-01 04:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7a8f7998-e8f0-3b50-8424-c28d7cc17eaa | -14.5177 | -48.37282 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 65bad0d8-7f61-3f8c-8a10-899209ba1eb1 | -11.82919 | -44.97597 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bc91073e-206d-3249-979e-66722420ef14 | -12.83821 | -47.033 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9fc6c69b-ad88-32e3-b284-9f24f88fd384 | -13.77756 | -47.96892 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 12.2 |
| eb88bdd8-0b0b-320b-8ea7-1b1318a15464 | -11.74461 | -46.86696 | 2025-10-01 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a84244ae-928a-3755-8828-0721ce58d4b9 | -13.1765 | -47.38672 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bba20dac-161c-3d41-814d-9a71fb87e501 | -14.49944 | -48.41999 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1ff6958f-6dcb-398e-ad1b-a59df9e6a15c | -10.65766 | -48.52573 | 2025-10-01 04:21:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ea88d3f6-6812-301c-bb7f-76389270542f | -14.78632 | -45.80054 | 2025-10-01 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 22d9eacb-f5a1-358e-874c-de27d54e5f9c | -15.35615 | -47.0803 | 2025-10-01 04:21:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 93903280-9cf8-38b8-9feb-91565c346651 | -10.94544 | -44.32956 | 2025-10-01 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e056d54d-ed8f-32d2-a6c3-066d3ac96ff4 | -16.40486 | -47.05531 | 2025-10-01 04:21:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5d76b0eb-ed7a-3892-b56d-628404622dbd | -9.64882 | -48.23297 | 2025-10-01 04:21:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f84f3b24-207c-3708-a0df-b169fece7064 | -14.44902 | -46.35609 | 2025-10-01 04:21:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7bac543f-bc61-3e87-9131-25593f8a4505 | -13.31383 | -47.21051 | 2025-10-01 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 14b0aaa2-77b6-3436-8919-b2865800466a | -11.44337 | -43.505 | 2025-10-01 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 04be1a16-3bfb-352e-94fc-92133b76c3d6 | -13.31268 | -47.21765 | 2025-10-01 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 05f0f6fc-6967-339e-b3a2-11193bfc3d7f | -13.82846 | -47.46175 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b9c4ba7f-c8c3-30ce-acd9-dfd2c3cf5585 | -12.44529 | -50.18229 | 2025-10-01 04:21:00 | NOAA-21 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 017ef519-9b87-373e-9a8e-44898af61a47 | -11.75673 | -46.87637 | 2025-10-01 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| dcc15cdd-9446-3cb3-9b29-00eb37f0b1af | -12.7718 | -46.87258 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bc22b011-8cc4-3808-b6e1-0b7c36e00eee | -11.65317 | -45.32569 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1bce7bf2-50cc-3be6-a414-b971fa6bab67 | -13.06043 | -47.06995 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b4a39e94-a30f-339c-9a52-d2807dbf0b09 | -15.53403 | -45.22768 | 2025-10-01 04:21:00 | NOAA-21 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 8.3 |
| e10cf2a7-405c-3755-992e-a4ff8e4ca558 | -13.77319 | -47.95325 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 4cc8946c-0178-337b-aafb-abe8b3996453 | -10.90596 | -46.53295 | 2025-10-01 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 9f2b7e32-3896-3116-8051-024db79edc4a | -13.66697 | -48.065 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8f470a3a-7ca1-3a66-84c2-3eb4e95d345f | -14.71217 | -48.12656 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 83492e35-d282-3d68-9f83-40d3ccff2f5f | -13.77857 | -47.98405 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5f80ca84-ead6-35b4-b07c-bcaee09d93ab | -14.68865 | -48.12261 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1b72aafc-a70d-35fa-89b2-f67c19cf9b39 | -12.83224 | -47.00637 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 651e3f8a-4674-39b1-b679-38256913fdc7 | -11.46119 | -45.09275 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 9458d632-9755-3ec4-ab38-7c881fde0254 | -15.52718 | -47.86711 | 2025-10-01 04:21:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 80f69191-00fb-362d-9462-745e8a4d6058 | -11.08389 | -47.82427 | 2025-10-01 04:21:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c41a0e64-0ad1-3b29-bb83-73e98084ebe4 | -14.69536 | -48.12376 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8c3daaf6-214e-321f-ac7e-f8fb6e15243c | -15.26567 | -47.88262 | 2025-10-01 04:21:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8720c31f-aacc-3868-87bc-cfba05e7d175 | -12.42165 | -44.09459 | 2025-10-01 04:21:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 50c1aea1-3dc9-3124-8a90-cddef96bdbac | -14.67987 | -46.968 | 2025-10-01 04:21:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 77514d4a-4d94-3f67-98b3-3df7b1f93d76 | -11.46174 | -45.0892 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 560dde91-871b-3583-b30b-6e22e02b147e | -10.54772 | -43.6413 | 2025-10-01 04:21:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b64e4c2c-63e9-3e8b-b0e6-79c945454366 | -10.92084 | -46.54625 | 2025-10-01 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3ad148de-dacd-34fe-b177-d7dbc9070acc | -12.40249 | -51.07461 | 2025-10-01 04:21:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0d333e7c-66ba-3224-a85d-d0ec58002dc4 | -15.3389 | -46.27521 | 2025-10-01 04:21:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8df64e93-dc11-3ff8-8678-a2cf6482ac4f | -14.50314 | -48.43983 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 813329b4-49aa-337f-b635-ec1cbe63d93b | -16.61373 | -49.20168 | 2025-10-01 04:21:00 | NOAA-21 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9771ff39-a38f-3a3c-af62-a77cd073d6f0 | -11.64655 | -45.32463 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f37ad5cd-08b9-3fe6-9aa8-4dbf3879df6b | -10.91399 | -44.30979 | 2025-10-01 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6ddb8bc5-18cb-377e-b266-55294a0e9562 | -12.95921 | -46.42213 | 2025-10-01 04:21:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8ab7752f-6f2b-3410-8dce-78007e1b16b1 | -14.36745 | -47.13451 | 2025-10-01 04:21:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 15f66bed-02dc-302d-93e4-997b1d928246 | -11.83198 | -44.98005 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3cbd761b-0e90-3ae3-9d14-f62b9e658ae5 | -16.25406 | -50.93388 | 2025-10-01 04:21:00 | NOAA-21 | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 9a600346-eb4f-307a-9f6d-cd06255a07ca | -16.29215 | -48.97872 | 2025-10-01 04:21:00 | NOAA-21 | ANÁPOLIS | GOIÁS | Brasil | 5201108 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c8999013-ed6e-3272-96fe-3bd65be9132c | -13.29928 | -47.23747 | 2025-10-01 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 27436761-2ac0-3658-9c2f-438a9e2a7387 | -14.72077 | -48.15864 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ce632d1b-3be1-3f91-b9f6-fcc9e4923935 | -15.17581 | -49.09 | 2025-10-01 04:21:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bdfd16f3-92f1-383b-96b9-8c93b3c525f8 | -14.60198 | -48.21879 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f673201b-362a-30ff-8fb3-83fbf1081b5d | -14.60621 | -48.19275 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| caf1d5c9-f100-3582-88d8-de85b8c95993 | -15.10516 | -44.94763 | 2025-10-01 04:21:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c0a9aef3-5d16-3ff2-a539-bd5d50216c76 | -10.61949 | -49.12673 | 2025-10-01 04:21:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 20a92abd-02e8-318c-bdee-ac55560f8646 | -14.68465 | -48.12592 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 8fcbadc7-d344-3adc-bf2d-043db567d003 | -14.90143 | -51.67014 | 2025-10-01 04:21:00 | NOAA-21 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 996ef71d-fcf0-378a-a9a3-3338f1700b89 | -14.72594 | -48.14805 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 022636b7-3828-3b16-9511-78a289d36223 | -12.00811 | -46.60148 | 2025-10-01 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ed7d1e53-197f-3a90-bf4a-80ac380a7a69 | -11.4711 | -45.07248 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2ac3542e-0d00-37e2-9474-9ed10e65a053 | -12.78412 | -46.88183 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 85a05ae6-7e8a-306d-b3af-8777307875e3 | -12.18495 | -40.41138 | 2025-10-01 04:21:00 | NOAA-21 | RUY BARBOSA | BAHIA | Brasil | 2927200 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 8dc9a5cf-f0ef-3eec-8636-c6000fe42e6d | -16.02461 | -50.90101 | 2025-10-01 04:21:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| c155025e-8336-3774-9a9b-892166015cb7 | -10.03666 | -52.10263 | 2025-10-01 04:21:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 087febbf-684a-3aab-8726-c160f860ecc4 | -11.81593 | -44.99583 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| b6bd9006-7674-3dc0-9880-ea4bf50cb66a | -12.22717 | -43.75256 | 2025-10-01 04:21:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6e3b7a72-96ec-38ab-b0f5-f77e70d67641 | -12.87479 | -44.60322 | 2025-10-01 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 39ba452c-9893-300a-a5c5-cf1a5f62cae6 | -16.25694 | -50.9392 | 2025-10-01 04:21:00 | NOAA-21 | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 36.2 |
| 5b1e9255-5ac8-3466-aa78-09d4fc78009f | -15.16001 | -49.0995 | 2025-10-01 04:21:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 9.8 |
| a1302f25-308c-3adf-8222-95c0c6c5090e | -14.90841 | -51.67689 | 2025-10-01 04:21:00 | NOAA-21 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 6eb61d9d-74da-3eec-b823-1485be1d13bb | -10.90534 | -46.5582 | 2025-10-01 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 6c26e417-7bf6-3f01-a448-d7c669032382 | -11.45491 | -45.02275 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 75c13635-ee60-36aa-a529-d88dec0de90a | -16.21077 | -48.27311 | 2025-10-01 04:21:00 | NOAA-21 | SANTO ANTÔNIO DO DESCOBERTO | GOIÁS | Brasil | 5219753 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b752c29c-6985-3113-8ad8-4c3f20dbf097 | -15.93357 | -48.13503 | 2025-10-01 04:21:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cce33d54-44af-3f6f-8e50-ebd5d842f37a | -10.47751 | -55.62393 | 2025-10-01 04:21:00 | NOAA-21 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1a856bca-1033-3aed-80a2-4b0ed4f8c3d0 | -11.46783 | -45.09377 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| f331cacb-5a93-3ac3-8b5e-384e5b9a3844 | -15.39897 | -44.97638 | 2025-10-01 04:21:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bdb0fd15-ad62-368a-9e6d-9abb1e3e52c0 | -14.35425 | -45.91445 | 2025-10-01 04:21:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e8be3b0e-29dd-3d1b-add8-8f0534263292 | -11.45919 | -44.97237 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |


[Clique aqui para ver as próximas entradas](README71.md)
