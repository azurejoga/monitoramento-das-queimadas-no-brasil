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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 910b17f2-1b4c-3d26-af75-68a327e3234e | -5.57105 | -44.88107 | 2024-10-19 04:49:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 5e3bb454-c3dd-3b79-8b00-69bd96150868 | -5.57032 | -44.88613 | 2024-10-19 04:49:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 7518e35e-0cf0-3d87-a1ff-cd3a25527eae | -5.56484 | -44.89037 | 2024-10-19 04:49:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 25812ed7-d755-31ff-a809-39b68ff6c779 | -5.11494 | -44.733 | 2024-10-19 04:49:00 | NPP-375D | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 28417031-a263-3a53-9012-310c9b1c00b3 | -5.11119 | -44.73128 | 2024-10-19 04:49:00 | NPP-375D | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fc49c00f-8fcc-3ae4-aedd-9b711ba3509e | -5.11016 | -44.73227 | 2024-10-19 04:49:00 | NPP-375D | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 06d5dcc3-6a1e-3068-adaa-52ff657f7cbd | -5.5696 | -44.89115 | 2024-10-19 04:49:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| e0d6b8c8-8786-3d8f-ae73-9a3021878fa2 | -5.56411 | -44.89543 | 2024-10-19 04:49:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 4117b277-b54a-3397-a847-abc422fce206 | -5.1104 | -44.73658 | 2024-10-19 04:49:00 | NPP-375D | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 074f41b3-0137-392b-9bff-28a6a057a429 | -2.52546 | -44.91161 | 2024-10-19 04:49:00 | NPP-375D | PERI MIRIM | MARANHÃO | Brasil | 2108405 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ef887a03-c0cc-387e-9dc5-ca09f21e888c | -2.52489 | -44.91404 | 2024-10-19 04:49:00 | NPP-375D | PERI MIRIM | MARANHÃO | Brasil | 2108405 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2e23628c-e85e-36f3-b7f9-f01d4361ca7c | -3.55679 | -45.35395 | 2024-10-19 04:49:00 | NPP-375D | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c56d875c-8cc2-35f9-870d-894f6852a199 | -5.12112 | -45.15763 | 2024-10-19 04:49:00 | NPP-375D | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 216d9be6-17d5-31e6-980d-fd47fe4ca894 | -4.92156 | -45.72266 | 2024-10-19 04:49:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5d4e73b5-9d67-3a8f-bf7c-de28118316ee | -4.7518 | -45.81537 | 2024-10-19 04:49:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8e867ffe-1fff-3176-ab85-f287836d54dd | -4.75118 | -45.81943 | 2024-10-19 04:49:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 18d103cb-2c97-3909-b691-f9f78e7cef31 | -4.71475 | -46.032 | 2024-10-19 04:49:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 7.6 |
| d6a6f0c2-1298-3561-b12f-8902514a8887 | -4.71413 | -46.03625 | 2024-10-19 04:49:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 70d849af-33a7-3423-8363-7c311d42dfcf | -4.71403 | -46.03363 | 2024-10-19 04:49:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| fb3e778d-a121-3b9a-a7be-ee255f9427d1 | -4.71194 | -45.84037 | 2024-10-19 04:49:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 23.9 |
| 45ab17ea-c21c-3675-a006-10fb1cc8640c | -4.71064 | -45.84899 | 2024-10-19 04:49:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 91139465-c8f3-36ff-ba8a-8f4dd9f32f27 | -4.71001 | -45.85322 | 2024-10-19 04:49:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 8.7 |
| b0c55c67-c6b0-384d-9682-a4c579534fe8 | -4.70818 | -45.83537 | 2024-10-19 04:49:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 9a8e7e43-5546-3983-8183-fdc703ed1f93 | -4.70562 | -45.85246 | 2024-10-19 04:49:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 7f7bf795-902a-3604-b96f-bb69b021d9d6 | -4.70315 | -45.83889 | 2024-10-19 04:49:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 7b9a2efa-a5f7-3555-b24d-9c4c309bfd97 | -4.70187 | -45.84743 | 2024-10-19 04:49:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 33.2 |
| a7c2e491-63a9-38ef-bcf2-df6ce2c227a8 | -4.70124 | -45.85168 | 2024-10-19 04:49:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 33.2 |
| db52a913-7dbc-3650-8178-2d861b59fffe | -4.69875 | -45.83819 | 2024-10-19 04:49:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 869f01bb-6442-3198-a57c-ed145c3a1c49 | -4.69812 | -45.84241 | 2024-10-19 04:49:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 67d4522a-ade4-3a9d-8a32-7c84eb1f22a3 | -4.69749 | -45.84663 | 2024-10-19 04:49:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 33.2 |
| 08879422-60a8-3de2-94b1-4e3ad260f506 | -4.69371 | -45.84176 | 2024-10-19 04:49:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ddd9b797-9cec-354e-9b4f-080ae9a7f25d | -4.67478 | -45.69376 | 2024-10-19 04:49:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 22f5e193-0d5f-3333-bb53-2432c316ddde | -4.52403 | -46.07878 | 2024-10-19 04:49:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 453ed67a-1a5b-3aa4-93e0-4e1e3aa5ba60 | -4.46589 | -45.89791 | 2024-10-19 04:49:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b7dbf145-823a-3d12-8be5-294d55f941fc | -5.12184 | -45.15274 | 2024-10-19 04:49:00 | NPP-375D | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6f427fc8-fecc-33d5-b772-e1c11863ee7a | -4.92663 | -45.71916 | 2024-10-19 04:49:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8a8f9748-2403-35e7-9727-19725b205b3e | -4.926 | -45.72343 | 2024-10-19 04:49:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 045933e0-5a9b-3b24-ba0e-e0a668a21ca8 | -4.75086 | -45.8133 | 2024-10-19 04:49:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c1b4c329-99d9-382b-831d-e488c418c340 | -6.62923 | -47.35243 | 2024-10-19 04:49:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 81872539-91e3-3e78-8e73-5ec7dd18c3e9 | -4.75028 | -45.81736 | 2024-10-19 04:49:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e7458017-8004-33fb-94bd-ad915f5ffed1 | -4.71837 | -46.03436 | 2024-10-19 04:49:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 39d1122d-6e43-3de1-aeb7-b295a9faff73 | -4.71128 | -45.84472 | 2024-10-19 04:49:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 23.9 |
| d8459799-ccab-3b56-981b-10f744637468 | -4.70754 | -45.83961 | 2024-10-19 04:49:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 23.9 |
| 822dd4c6-6ee4-301e-85d9-3e7f03d49093 | -4.7069 | -45.84394 | 2024-10-19 04:49:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 23.9 |
| c4d89c9a-bdf0-3c57-9fec-2804af158d65 | -4.70626 | -45.84821 | 2024-10-19 04:49:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 0575050b-19ec-3504-8699-073057d38807 | -4.70377 | -45.83471 | 2024-10-19 04:49:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 5db706e1-1b41-3368-b7f3-7efe4e0c8daa | -4.51968 | -46.07828 | 2024-10-19 04:49:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8cc896e3-b4d2-3ed1-8ca8-a020f47886a8 | -4.46651 | -45.8937 | 2024-10-19 04:49:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7434cda9-7957-3462-ad08-7752bf26c574 | -4.27584 | -45.8502 | 2024-10-19 04:49:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cc867fb1-8bc3-3c4f-b4ad-4eac5ebfb259 | -3.77026 | -45.81792 | 2024-10-19 04:49:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6ddbc789-1bde-3add-8d25-9c547ac0d7bf | -3.76966 | -45.82204 | 2024-10-19 04:49:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d1443986-a687-332c-9b27-6d6d8d172401 | -3.70324 | -45.90218 | 2024-10-19 04:49:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 65c11149-022f-3a01-b81f-32d121414e43 | -4.27146 | -45.84962 | 2024-10-19 04:49:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 76efc414-dd87-3845-968f-16955be33b96 | -3.76901 | -45.81942 | 2024-10-19 04:49:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 68347273-ad7b-30e8-81e1-fe7b17e2da03 | -5.5065 | -45.48819 | 2024-10-19 04:49:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 337ec00c-917d-3f13-ae32-1533d6b90519 | -5.43833 | -46.35178 | 2024-10-19 04:49:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 26b5de59-b713-39fb-8e87-bbbc064d8681 | -5.32024 | -45.16507 | 2024-10-19 04:49:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 708ccd52-24fb-3de0-8f2f-ac48fbae77ba | -5.13845 | -46.10204 | 2024-10-19 04:49:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2f8ef741-c9b1-35fe-bf26-5edc5073c6d4 | -5.09421 | -45.94693 | 2024-10-19 04:49:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b4844603-3c82-382d-b807-80e2f71d9360 | -5.07965 | -45.76706 | 2024-10-19 04:49:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 88e3bb41-3a13-3a3e-befb-b05029e35f79 | -5.07636 | -45.76885 | 2024-10-19 04:49:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8eb021d9-91a0-3f71-9446-368fa8165061 | -5.68446 | -46.43908 | 2024-10-19 04:49:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ca6d032f-be4f-3dd9-952b-360c5d6ac97b | -5.31556 | -45.16452 | 2024-10-19 04:49:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 00551166-1145-33b4-ac5d-375c2a1de464 | -5.09863 | -45.94743 | 2024-10-19 04:49:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 00b8e7ec-4753-39be-ad3f-a52af13de283 | -5.08083 | -45.76941 | 2024-10-19 04:49:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d492f3c9-baa8-3fa6-bcbb-65f80f9970bf | -5.07902 | -45.77145 | 2024-10-19 04:49:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 91b9f93f-a724-3b1d-ae9c-808d183493e8 | -2.0491 | -46.89113 | 2024-10-19 04:49:00 | NPP-375D | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f072cbd7-484c-39f5-8e5f-b1bdb1121cb7 | -1.66877 | -47.15705 | 2024-10-19 04:49:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9cae010a-cec9-3c5b-a94b-4f018d2df8b4 | -1.4253 | -45.90612 | 2024-10-19 04:49:00 | NPP-375D | LUÍS DOMINGUES | MARANHÃO | Brasil | 2106201 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7dec3a74-e062-35d9-86d6-8d5a6f48d8e0 | -1.38069 | -46.69793 | 2024-10-19 04:49:00 | NPP-375D | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8aa2bfdc-fecb-3504-92f7-516a602a8d97 | -1.37854 | -46.70007 | 2024-10-19 04:49:00 | NPP-375D | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0b7f156b-9495-37b1-8512-a189802bcffa | -2.57339 | -47.06855 | 2024-10-19 04:49:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d4b55784-d484-3a5d-9515-d5cede8fa93e | -2.57263 | -47.07349 | 2024-10-19 04:49:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 92cd7ce8-bd70-3bbd-8e3e-5ee4b31aa0d7 | -2.56946 | -47.06795 | 2024-10-19 04:49:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 1e730429-8620-3ae8-9fca-5537c82ec56a | -2.5687 | -47.07291 | 2024-10-19 04:49:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 3d62ad4c-b091-36fc-b1dc-f1fe909f6756 | -2.56553 | -47.06733 | 2024-10-19 04:49:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| e78248e3-ca03-3b71-8077-149b596300df | -2.56476 | -47.07232 | 2024-10-19 04:49:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| ffa744cd-f514-3965-97c2-64409bb15ccf | -2.53744 | -47.22398 | 2024-10-19 04:49:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| efd522d3-e1e7-3364-9eec-9d355700ecad | -2.53355 | -47.2234 | 2024-10-19 04:49:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e7871dc8-0ff4-395d-be88-35b7b9c6d1b0 | -2.5328 | -47.22827 | 2024-10-19 04:49:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c24fa1e8-b467-3137-9218-02dc9e87f208 | -2.4039 | -46.71558 | 2024-10-19 04:49:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 63e51911-965e-3715-b6c8-52ba938b5047 | -2.40337 | -46.71904 | 2024-10-19 04:49:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b52f45ac-7327-3aef-8609-40b470b99c9e | -2.39936 | -46.71844 | 2024-10-19 04:49:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8d32c833-0c70-3f46-b375-bd6f2d5c3c5b | -2.36767 | -46.9772 | 2024-10-19 04:49:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 55163e33-d9a9-3b0b-821b-6ea61c368525 | -2.18279 | -46.90852 | 2024-10-19 04:49:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b40e1cd2-1f4c-337e-95d9-9060170b385c | -2.14706 | -47.0606 | 2024-10-19 04:49:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7199c4b8-d1fe-39ac-8cfb-ac861929ab7c | -4.64973 | -46.85368 | 2024-10-19 04:49:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f627d939-3303-3dc9-92c2-d189031b0c1f | -4.64918 | -46.8573 | 2024-10-19 04:49:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| feca6b6d-4d67-37c7-a9e7-a6a441e99bc0 | -4.95279 | -47.40463 | 2024-10-19 04:49:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b8da496f-1918-3802-9f44-63996488ccde | -3.91397 | -46.45141 | 2024-10-19 04:49:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 34de65ec-fd02-3efd-80b6-70864f7f4a8f | -3.89424 | -46.44041 | 2024-10-19 04:49:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a0154592-5b70-394f-8cc8-b72c9395e8a1 | -3.84759 | -46.11153 | 2024-10-19 04:49:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e75e9f7d-0fb7-38ff-abd3-f5c638be7263 | -3.84512 | -46.11165 | 2024-10-19 04:49:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 125a607d-ac21-38ba-9d31-750c5af1931f | -4.27344 | -46.28952 | 2024-10-19 04:49:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e3308e16-a828-3155-aa35-c34eaffbb543 | -5.49712 | -46.77285 | 2024-10-19 04:49:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3c68259d-cbcc-3768-8597-e962562b2995 | -5.49294 | -46.77221 | 2024-10-19 04:49:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ea6bd280-ed88-3e56-9073-4f6ddc888991 | -5.35694 | -47.7499 | 2024-10-19 04:49:00 | NPP-375D | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 67a0d3f3-08bb-3b4d-9fe4-5cb97f01c9e9 | -2.62348 | -49.06739 | 2024-10-19 04:49:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b09dc24a-09c9-3eba-b188-1f8ade0fde03 | -5.24276 | -46.77301 | 2024-10-19 04:49:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c94c67c7-a19a-3711-aa7b-f47952fa4312 | -5.21619 | -47.1912 | 2024-10-19 04:49:00 | NPP-375D | SÃO FRANCISCO DO BREJÃO | MARANHÃO | Brasil | 2110856 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README27.md)
