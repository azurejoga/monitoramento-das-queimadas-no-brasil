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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5c727f5c-ea05-3f44-963d-195de4e1e873 | -2.17427 | -45.48866 | 2024-10-29 04:38:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8d4f8c0b-36fb-3955-8866-0961dde1646b | -4.27569 | -46.10303 | 2024-10-29 04:38:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 96e1b35f-8d88-3af3-94a3-569173841ea2 | -3.93015 | -45.24405 | 2024-10-29 04:38:00 | NOAA-21 | SATUBINHA | MARANHÃO | Brasil | 2111722 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a751e376-e1a8-3b3a-b361-99a698c1647e | -3.92757 | -45.24137 | 2024-10-29 04:38:00 | NOAA-21 | SATUBINHA | MARANHÃO | Brasil | 2111722 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 5b8f6476-d85c-3ca8-a2fc-2a5c937707e9 | -3.92646 | -45.24349 | 2024-10-29 04:38:00 | NOAA-21 | SATUBINHA | MARANHÃO | Brasil | 2111722 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1d3c0048-7ccd-3fca-9e50-2022b1c5b061 | -3.78865 | -45.51386 | 2024-10-29 04:38:00 | NOAA-21 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1d536d3a-3fa5-3934-8f2f-06af1a3bdf03 | -4.46782 | -45.96217 | 2024-10-29 04:38:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| c1d3a442-734a-3593-ace5-d3d947f900fb | -4.46426 | -45.96156 | 2024-10-29 04:38:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 7027f962-17c8-3327-807d-9f230550ed51 | -4.46364 | -45.96555 | 2024-10-29 04:38:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| d84dcc12-6276-3a4b-8974-1c13842d573e | -4.46007 | -45.96499 | 2024-10-29 04:38:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| db30d4b0-484b-397e-b2d7-2371125e44bf | -4.47854 | -45.9329 | 2024-10-29 04:38:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 95117a90-bb9d-33a0-a4fd-3aab0873a2af | -4.47586 | -45.934 | 2024-10-29 04:38:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5e1d5f57-458e-3155-a60c-4b0d4da253b2 | -4.47435 | -45.93647 | 2024-10-29 04:38:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 30bbd633-fadc-3360-a8fe-716260213e24 | -2.08336 | -46.51202 | 2024-10-29 04:38:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9bace65c-6cfa-376c-a177-4c2909f485ca | -2.08052 | -46.50783 | 2024-10-29 04:38:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c4834a51-74dc-3eab-9a35-ba6f5783d57e | -2.07995 | -46.51149 | 2024-10-29 04:38:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a7dedb89-fae8-3b7d-979a-05a88b16bb20 | -2.07937 | -46.51517 | 2024-10-29 04:38:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1b790d94-c77a-3d7f-b7dd-5b841ca6bf70 | -2.07769 | -46.50363 | 2024-10-29 04:38:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 04da3cb7-3c23-3bc3-a359-1b0d7b5e2808 | -2.07711 | -46.5073 | 2024-10-29 04:38:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eee9f7e1-e450-3f0a-87f7-02fe0c7437ea | -2.07654 | -46.51097 | 2024-10-29 04:38:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 60b42a6a-65b6-3d96-ab4a-2afb6b1a9b8d | -2.07255 | -46.51413 | 2024-10-29 04:38:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 46060a97-052c-3a06-af48-ad216724f0f7 | -2.06229 | -46.53511 | 2024-10-29 04:38:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 22e4b9ac-ecdc-33d5-ab94-d410949e86ee | -2.05662 | -46.5267 | 2024-10-29 04:38:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 59a7503a-0093-386e-b128-2397c25b1796 | -2.05604 | -46.53036 | 2024-10-29 04:38:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 28a3f3e3-c351-3270-9415-0b3f770e17ef | -2.00395 | -46.41327 | 2024-10-29 04:38:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5529111d-a6d8-33c5-841e-666b8ab2327d | -2.05945 | -46.5309 | 2024-10-29 04:38:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5f1e8639-6248-398f-8582-47c5b3153c19 | -2.04602 | -46.89357 | 2024-10-29 04:38:00 | NOAA-21 | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c7548c65-587d-39a1-8f30-451cf98a71a5 | -2.04547 | -46.89716 | 2024-10-29 04:38:00 | NOAA-21 | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6b44f341-40d5-3d5a-a0ac-59e3b18b7d1e | -2.04374 | -46.89661 | 2024-10-29 04:38:00 | NOAA-21 | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 478a0374-b6b2-320e-b07f-d74b296ffc18 | -2.04037 | -46.89608 | 2024-10-29 04:38:00 | NOAA-21 | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 31b74e00-0e09-3206-8f5b-31cecaaab730 | -2.03814 | -46.86633 | 2024-10-29 04:38:00 | NOAA-21 | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d5b92214-ce57-3191-ba7d-f90ceaedf258 | -2.02858 | -46.88325 | 2024-10-29 04:38:00 | NOAA-21 | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f4c887a6-3506-34ed-a765-e7ede2f21b2c | -1.98481 | -46.94252 | 2024-10-29 04:38:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| edbc3790-67c8-3cf0-862b-b59963ccc148 | -1.98421 | -46.88004 | 2024-10-29 04:38:00 | NOAA-21 | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4be80021-c591-38c2-9065-8c82decf91da | -1.91495 | -46.60285 | 2024-10-29 04:38:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0056b5ef-4415-3e42-a341-1b14e4f04bff | -1.91156 | -46.60232 | 2024-10-29 04:38:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 810304db-2400-3e23-b6f9-bb956e2fbc4a | -1.45432 | -46.87594 | 2024-10-29 04:38:00 | NOAA-21 | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3338cef5-9c88-3940-a2bb-b12887a3dee6 | -1.16463 | -46.5296 | 2024-10-29 04:38:00 | NOAA-21 | AUGUSTO CORRÊA | PARÁ | Brasil | 1500909 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 59ebddab-be26-36d9-bf9e-7b78127e0b27 | -1.11086 | -46.83021 | 2024-10-29 04:38:00 | NOAA-21 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 5ba8aafc-f454-3e4d-a5a0-e769eac1f2ab | -1.11031 | -46.83376 | 2024-10-29 04:38:00 | NOAA-21 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f88335ac-12df-3566-8094-7a9573e022f7 | -2.11188 | -46.3301 | 2024-10-29 04:38:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1463c455-0057-3a22-9571-19d0a79f6425 | -3.31162 | -47.19733 | 2024-10-29 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 24105c9f-35e5-3dca-a7b4-f5833f195791 | -3.30825 | -47.19681 | 2024-10-29 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 510251db-be5a-32d4-96af-534847fe15b9 | -3.30204 | -47.02613 | 2024-10-29 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f92726a6-45c0-3ef2-a5ec-072886c026a6 | -3.29865 | -47.02561 | 2024-10-29 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 858118d5-c22c-31c1-9ac4-e86e4b1ac0dd | -3.25334 | -46.86928 | 2024-10-29 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 22.0 |
| cbb3e647-5703-38e1-b1be-554e566a129a | -3.25277 | -46.87296 | 2024-10-29 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 22.0 |
| 0cf5b3a3-79d7-32a0-ae60-93ce5a1f4bd6 | -3.25221 | -46.87663 | 2024-10-29 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| c6bff617-1ca0-3251-b932-6931255f13f1 | -3.2505 | -46.86508 | 2024-10-29 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 88bfd626-a0c8-3f36-8d1b-ec8e17659f3c | -3.24994 | -46.86875 | 2024-10-29 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 37.3 |
| 047a2752-7d54-33ab-97b2-176390e61081 | -3.24937 | -46.87243 | 2024-10-29 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 37.3 |
| c005d535-92cf-3081-9ff2-31e9c35edc20 | -3.24881 | -46.8761 | 2024-10-29 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2b701d09-88c8-3135-854b-77332915435d | -3.24653 | -46.86823 | 2024-10-29 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 37.3 |
| c9d6ea14-1c8e-347f-9d94-996e4580d4e1 | -3.24597 | -46.8719 | 2024-10-29 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 37.3 |
| 8155cde7-59f7-3e7b-ba27-35d1b11031e5 | -3.20192 | -46.18028 | 2024-10-29 04:38:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ee21e0f1-9ab4-333f-8508-8131c3f91124 | -3.19903 | -46.17586 | 2024-10-29 04:38:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 36c8d077-6064-3c47-ad8e-ea709cbca20f | -3.19663 | -46.19132 | 2024-10-29 04:38:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a4990e59-f9af-3262-946c-311573f76066 | -3.17024 | -46.61098 | 2024-10-29 04:38:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b64f4551-6df8-30e8-a885-9e13d1322168 | -3.16965 | -46.6147 | 2024-10-29 04:38:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 23ede081-3c4c-3f7d-902b-0a95536e01e4 | -3.16739 | -46.60672 | 2024-10-29 04:38:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 687e260a-bb06-3f91-9dce-3b814a894a9a | -3.16681 | -46.61045 | 2024-10-29 04:38:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 54e736bb-96db-32f2-9626-6c0f3f9fe8fb | -3.158 | -46.48631 | 2024-10-29 04:38:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 92fb195c-73d0-3db2-b897-e7f781b897c2 | -2.4477 | -46.89935 | 2024-10-29 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2efc9d90-8783-37bd-80ac-653c595e59d1 | -2.44094 | -46.89832 | 2024-10-29 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4f272756-cfd5-3f33-8d86-9422a7ba3773 | -2.42399 | -46.7171 | 2024-10-29 04:38:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c1360bb9-eec1-3b87-9904-b369a6b08a13 | -2.42116 | -46.71292 | 2024-10-29 04:38:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c1dd6a48-ccbc-39c8-a509-3eb3ac47e221 | -2.4206 | -46.71658 | 2024-10-29 04:38:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 1debc119-a8ca-34fe-a0ea-df4ba06d739e | -2.42003 | -46.72023 | 2024-10-29 04:38:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 03f9da95-9f4f-3679-aef1-54158fc0ed5f | -2.41947 | -46.72388 | 2024-10-29 04:38:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| eedd900e-fdcf-3fac-aa4c-6bbb74fa0048 | -2.41776 | -46.71241 | 2024-10-29 04:38:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 855a72aa-cd48-32bb-b8db-4354d23959d9 | -2.4172 | -46.71606 | 2024-10-29 04:38:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3bd8bf6b-e735-349b-9e5f-cfd221b70a6c | -2.41663 | -46.71971 | 2024-10-29 04:38:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0963ffbc-7aa7-34a6-86a2-88c35de2b608 | -2.41605 | -46.70092 | 2024-10-29 04:38:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b3941218-7aa4-3f9f-a2f9-004ead00f5e8 | -2.41549 | -46.70457 | 2024-10-29 04:38:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1f71d30a-54e2-375f-9516-0c4e3723729b | -2.41493 | -46.70823 | 2024-10-29 04:38:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 81e7f08d-3de2-35b9-bf8f-e2c21035fc5b | -2.41436 | -46.71189 | 2024-10-29 04:38:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 327fa272-bfba-3465-a1bc-d9ddbe876223 | -2.41267 | -46.72285 | 2024-10-29 04:38:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| edde1e6e-9223-3211-8a10-8a5064fddd43 | -2.41265 | -46.70039 | 2024-10-29 04:38:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9b8c0344-7f2e-36d4-a5dc-d0a7bf15a164 | -2.41209 | -46.70405 | 2024-10-29 04:38:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a11cfd06-53bc-3964-8cec-f51927b7975f | -2.41153 | -46.70771 | 2024-10-29 04:38:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3ba2a75e-29d8-3843-add9-de6d12a80e79 | -2.41096 | -46.71136 | 2024-10-29 04:38:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 50b01dc5-79fc-3d42-aa41-7d1984118408 | -2.40925 | -46.69987 | 2024-10-29 04:38:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 265d875b-8c05-3ed5-bf31-22954df50f45 | -2.40871 | -46.72598 | 2024-10-29 04:38:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fa21a8d4-04c8-3736-824c-115fc7301a85 | -2.40585 | -46.69935 | 2024-10-29 04:38:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eabfc013-cc06-3b96-a698-9394cd6fffa1 | -2.40532 | -46.72546 | 2024-10-29 04:38:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d897be61-5ad0-373b-91a8-c40e6e95851a | -2.40419 | -46.73277 | 2024-10-29 04:38:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0d35ee32-9ef4-3905-b13c-5088d72c497a | -2.40363 | -46.73641 | 2024-10-29 04:38:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3487da12-f2a8-37de-b905-3ca3be23d2b6 | -2.40246 | -46.69883 | 2024-10-29 04:38:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fd7285d9-c2ad-367f-8242-0c0d8a5a9574 | -2.40192 | -46.72495 | 2024-10-29 04:38:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eead2197-60fb-32a5-9878-530f541ee4f9 | -2.40136 | -46.7286 | 2024-10-29 04:38:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 32cea694-f4bc-3edf-aa98-97d78adbf2be | -2.4008 | -46.73225 | 2024-10-29 04:38:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 27af7e37-cbdf-300c-b75b-63995610a779 | -2.40023 | -46.73589 | 2024-10-29 04:38:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9422a345-c546-3874-ad54-595efaba7d17 | -2.3974 | -46.73172 | 2024-10-29 04:38:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 51169afc-b73f-361c-942d-708ddaa83f68 | -2.3962 | -46.73212 | 2024-10-29 04:38:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1318586f-c198-3677-b3d8-33b766de2207 | -2.39055 | -46.72379 | 2024-10-29 04:38:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 22dd9c93-9205-37e2-bc86-eca8ef4dbe76 | -2.38998 | -46.72744 | 2024-10-29 04:38:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 624e52b5-7784-3bc8-b03e-c20b6480f2d1 | -2.38658 | -46.72692 | 2024-10-29 04:38:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| efb50f6f-6280-353f-a5a1-fabeea67d3da | -2.37437 | -46.55971 | 2024-10-29 04:38:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 36cce104-4b22-3841-bc7b-0e3371922342 | -2.3368 | -46.64436 | 2024-10-29 04:38:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c92c1440-fe22-324d-bbe1-7f486dbb1f2f | -2.33624 | -46.64802 | 2024-10-29 04:38:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |


[Clique aqui para ver as próximas entradas](README36.md)
