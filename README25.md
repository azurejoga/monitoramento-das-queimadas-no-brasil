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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 010dcfae-5ac0-35c9-829a-c5f6fde6546d | -6.1072 | -59.92397 | 2025-08-13 05:06:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e39ca025-a0d4-3dfc-ab1b-5cfc70a1906c | -7.46572 | -59.8867 | 2025-08-13 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| bfec15c5-4483-331c-a89d-9342a46149b3 | -5.89238 | -57.7482 | 2025-08-13 05:06:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2d74f8a2-b332-3a88-9417-c98d76d7ad83 | -7.26316 | -60.62965 | 2025-08-13 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| aa4a8435-38ac-3b0e-995a-543ec690804d | -4.9589 | -47.60093 | 2025-08-13 05:06:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 0a08a938-492a-3191-991c-94a733f65752 | -6.21199 | -55.66793 | 2025-08-13 05:06:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c956869a-668d-3ccd-b909-b25e9ec307aa | -7.18313 | -56.6945 | 2025-08-13 05:06:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 39b7c47d-7c2c-37a7-b10d-6587e4784f97 | -7.14195 | -56.42126 | 2025-08-13 05:06:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eb904e66-d4bb-38c7-8a1c-1f771f1679f7 | -7.26222 | -57.64071 | 2025-08-13 05:06:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e307aee1-e14c-374c-8bf9-6f3d3dde4ffd | -6.89956 | -59.14495 | 2025-08-13 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.5 |
| 95f829d1-ecc8-30ca-8e7f-85ec624d886a | -6.88057 | -59.14614 | 2025-08-13 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 28.7 |
| 50f8ee1c-ffad-3ed4-aa6e-5cde1269987c | -7.45928 | -57.6532 | 2025-08-13 05:06:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 46995e0d-c215-3036-b900-8b0347198392 | -6.09091 | -59.92635 | 2025-08-13 05:06:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cfaa7a5b-1d03-38bd-bfc5-b5830bcac820 | -8.12291 | -55.5638 | 2025-08-13 05:06:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7ad8f755-bd73-3b87-baf1-6e5fe59f3c84 | -8.56348 | -54.71166 | 2025-08-13 05:06:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 17ee42df-4a9e-3ff1-8ff5-72434af421db | -7.0955 | -60.02665 | 2025-08-13 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 365e0f82-51cf-3e8f-8608-1c5a245bf267 | -6.88197 | -59.13762 | 2025-08-13 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 19.7 |
| 33838e9f-8d36-372d-87a0-9adf3d870a48 | -7.09933 | -60.02729 | 2025-08-13 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9e8c31cf-56e1-3b0b-bd6b-87c322b7555b | -6.09626 | -59.94207 | 2025-08-13 05:06:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 8c37a029-0ecc-325b-bcf3-d55ef0741c1d | -6.89435 | -59.13087 | 2025-08-13 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 0c23abec-971a-32fc-b138-481b8d54763c | -7.27109 | -60.63108 | 2025-08-13 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9b88ef57-b615-3af2-9c48-7d222b64c67e | -6.90462 | -59.13701 | 2025-08-13 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 17.3 |
| 18e0ee92-43b6-3432-b174-598985eebd5f | -7.09627 | -60.02192 | 2025-08-13 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| b0b7663e-08dd-301a-a086-15205007dfe7 | -7.28848 | -57.6483 | 2025-08-13 05:06:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8f71e53d-e596-3e6a-bd1b-6f8da33144be | -10.34169 | -50.81538 | 2025-08-13 05:06:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b9766a5a-de54-346f-82d3-d48710f50a56 | -8.56684 | -54.68984 | 2025-08-13 05:06:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fe5a03fe-8999-339e-8013-7c723db21089 | -8.57419 | -54.7096 | 2025-08-13 05:06:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e012f3dd-649a-30f7-8cd0-9d95ed1083d3 | -6.61228 | -43.89286 | 2025-08-13 05:06:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 30aea6e1-5f8b-3b8e-aee0-09801ed8cdac | -6.88127 | -59.14188 | 2025-08-13 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 19.7 |
| a5ae113b-964c-3aff-863e-ec3c56c57364 | -7.43881 | -57.64978 | 2025-08-13 05:06:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d116225d-c5be-3e32-91cd-00e5b5950c24 | -7.26227 | -60.63491 | 2025-08-13 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 82ae6dda-a9c0-320f-b8f1-b1e1b96a7d44 | -8.57307 | -54.71688 | 2025-08-13 05:06:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5db49f71-d794-31b6-8ab7-865ae2ae2ed7 | -8.56686 | -54.71219 | 2025-08-13 05:06:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7982f81c-5391-3be5-bba0-a6fd54dc35bf | -9.01413 | -59.54274 | 2025-08-13 05:06:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 74fcf537-7e6e-377c-b503-991f4ff482bc | -10.35437 | -50.81731 | 2025-08-13 05:06:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f759479d-e615-32fe-94cf-4a9540a49c46 | -6.09011 | -59.93119 | 2025-08-13 05:06:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3bd79eec-a8fd-3ee6-8081-5a96048a959b | -7.09472 | -60.03137 | 2025-08-13 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 725e33a9-80e4-3827-8ffb-816e9efbe8f6 | -6.09238 | -59.94148 | 2025-08-13 05:06:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 20bf4735-4e04-3e6e-8140-169f522c0c52 | -10.34592 | -50.81601 | 2025-08-13 05:06:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1b4bfd7a-fab1-338b-9e53-90af27689fa7 | -6.10333 | -59.92336 | 2025-08-13 05:06:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 03284c2a-bd14-31e4-ba4c-e497b4790747 | -7.13191 | -60.124 | 2025-08-13 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 61d2db8f-1f22-3b76-8959-365cc7815af4 | -8.56404 | -54.70803 | 2025-08-13 05:06:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3ceb4a50-7221-3819-ae25-ac95885ab065 | -6.96731 | -59.27807 | 2025-08-13 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a7a931ce-8754-3c52-a13b-78d6802d51a9 | -6.07692 | -59.93876 | 2025-08-13 05:06:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e5e3185b-01b7-35e7-8a02-40cacc037865 | -5.44392 | -45.10614 | 2025-08-13 05:06:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 89f195a6-c44f-3b83-820d-73d0e19a2873 | -6.871 | -59.13574 | 2025-08-13 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| c6ecadfe-164f-3cbb-a59d-d30dd9b70b69 | -8.57702 | -54.71376 | 2025-08-13 05:06:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 73a01809-fa76-3b51-8c32-c6a8f2525bd9 | -6.87621 | -59.14979 | 2025-08-13 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| da465b1c-90a0-3f1b-b2ed-afbce1e73bfa | -7.81848 | -61.33252 | 2025-08-13 05:06:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0db6f320-7969-33a9-a23f-c194e14d2006 | -6.86818 | -59.15287 | 2025-08-13 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 44dc9a35-dd05-39a1-8c55-0ba198d9b5df | -10.34535 | -50.81997 | 2025-08-13 05:06:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ddbf14f7-538b-360a-b6f1-7ae3cde6cfc4 | -10.3448 | -50.82391 | 2025-08-13 05:06:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fb895aa0-2d74-347f-b8d3-d0033c600f3f | -6.90672 | -59.1241 | 2025-08-13 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| aef3d2b4-027b-3976-9354-5b157021c757 | -7.07671 | -59.20137 | 2025-08-13 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ff74ab39-f1bd-35d5-89cc-5698a99e1b31 | -8.57024 | -54.71273 | 2025-08-13 05:06:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1c8b243c-4c41-39f7-b868-56f84f78d9cb | -7.31815 | -60.61797 | 2025-08-13 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 42ef94eb-75a9-3185-9c19-8f0be5be73e2 | -6.90392 | -59.14129 | 2025-08-13 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 29.7 |
| a63b4b7d-3264-38ee-89e4-5205387c0f47 | -7.14427 | -60.12118 | 2025-08-13 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| f14c11b3-eb2b-35e4-9290-d632f8892850 | -7.45635 | -60.6244 | 2025-08-13 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f9759c8a-28a6-3629-9e40-314d228a23aa | -7.45855 | -60.63536 | 2025-08-13 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 04317333-eb90-308f-b1c3-8447278364a5 | -7.45709 | -59.89286 | 2025-08-13 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1fa62cac-c92c-364a-8895-5da650723bd0 | -6.09945 | -59.92277 | 2025-08-13 05:06:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b831dacf-6fa0-3b37-bcd9-ad8b5017478e | -7.14812 | -60.12186 | 2025-08-13 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| d56a09c9-cad4-3596-9adf-b5242ea7cead | -10.35015 | -50.81667 | 2025-08-13 05:06:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 72ae5b9b-a5ff-3b32-80a2-830c8d06c9e0 | -7.06868 | -59.20441 | 2025-08-13 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2557ebd8-7e7f-397b-a125-d5cedb2ad084 | -7.24171 | -59.99838 | 2025-08-13 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| cf24b9c7-71bf-3d0b-adbc-9b925ab3aaeb | -6.97396 | -59.28362 | 2025-08-13 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d0d821d3-9c4f-32b9-82d3-6505cb25c7e4 | -6.90096 | -59.13641 | 2025-08-13 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 92c09b43-2490-3924-9306-9bd9f86a3665 | -8.10796 | -55.57219 | 2025-08-13 05:06:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d0c44179-9da0-3ebb-98f3-a975e19c2970 | -6.95272 | -56.39482 | 2025-08-13 05:06:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3b70ce83-a2c9-3194-b052-918852b00f15 | -6.90897 | -59.13331 | 2025-08-13 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 17.3 |
| 2dbfc8d4-917e-3324-8dde-3c0e70eb88e8 | -7.13577 | -60.12463 | 2025-08-13 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2cb2fcb9-8160-3f06-992a-16166f6759ec | -7.45767 | -60.64054 | 2025-08-13 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| edf61f05-cfd5-32ff-8d35-e5af3d9d3e08 | -6.8703 | -59.14001 | 2025-08-13 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| a08278c5-8296-393c-9f66-5e5c1d6cf5ee | -6.86735 | -59.13512 | 2025-08-13 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 13d2bfa7-8b66-33c2-8eb6-f8ba6ae6333d | -7.61957 | -56.71692 | 2025-08-13 05:06:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ea52e86e-e861-3089-a94e-88a62cb7db1f | -6.69514 | -59.14022 | 2025-08-13 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 85440bd4-644e-3e50-8d89-92441c82dcc7 | -8.11904 | -55.56678 | 2025-08-13 05:06:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7358c9a2-2a42-324d-b6db-823d61252529 | -6.09865 | -59.92762 | 2025-08-13 05:06:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 02856ab8-de11-311f-b3bb-e13917f8ea13 | -6.87987 | -59.15041 | 2025-08-13 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 28.7 |
| 0182b458-47b4-365a-80f5-76d3ed5eb7fc | -6.88353 | -59.15102 | 2025-08-13 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 28.7 |
| a0fc58b0-a5db-36ed-9a65-d26b99ff441d | -6.87691 | -59.14552 | 2025-08-13 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| a2fb108c-8782-3d87-834a-9cfb28aba737 | -7.14268 | -60.1307 | 2025-08-13 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 107c4dc5-1d77-3483-99ee-28d2de3bd111 | -6.28086 | -53.63355 | 2025-08-13 05:06:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 281a843b-fc91-33db-be35-412b98f2f629 | -7.28968 | -57.6409 | 2025-08-13 05:06:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0a3e1e83-70d4-302d-ab0c-7dee702cb40f | -6.55136 | -56.19501 | 2025-08-13 05:06:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| d0dae95b-051c-30ca-a817-72c0e6b6bc8f | -6.28027 | -53.63733 | 2025-08-13 05:06:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 97461388-3e8a-36f8-a575-152b2ec00885 | -3.21802 | -60.59971 | 2025-08-13 05:06:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 66425baa-2a41-3986-84e7-bc78cac2ee6e | -8.10851 | -55.56869 | 2025-08-13 05:06:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7bbce762-5c07-3388-9a69-bfa16ece6993 | -7.71441 | -55.21224 | 2025-08-13 05:06:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a2f3899f-de3c-3475-8c24-07e766f8d85b | -6.87831 | -59.137 | 2025-08-13 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 7f803ec5-4859-3b1c-a596-f5e227997857 | -7.06431 | -59.20809 | 2025-08-13 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 83f8241a-48f9-3241-b2b8-82ff6a61329a | -6.87551 | -59.15408 | 2025-08-13 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 31.7 |
| e2c4cdd6-1284-3395-b331-d2a30769d0f3 | -8.57137 | -54.70544 | 2025-08-13 05:06:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a3c7c600-024e-3f97-862f-ef3d18d5b912 | -6.87466 | -59.13637 | 2025-08-13 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 292e2dad-6ea0-3a1f-954a-6e0b812582c5 | -9.84162 | -47.81657 | 2025-08-13 05:06:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b65fe388-b60d-33a4-8fd7-b6819180064a | -7.45814 | -59.88553 | 2025-08-13 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7f051cec-52c1-3d99-829d-cb3fcc0aeef5 | -7.12805 | -60.12338 | 2025-08-13 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e2c4d070-c88b-3706-8ef8-cdcde0ef1d5a | -6.41826 | -53.37805 | 2025-08-13 05:06:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e2c5b791-e08c-3040-914d-b01938071c8b | -6.09786 | -59.93244 | 2025-08-13 05:06:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |


[Clique aqui para ver as próximas entradas](README26.md)
