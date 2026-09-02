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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 385328f6-2461-397e-9fc6-3ff9644a51c7 | -4.36514 | -47.7765 | 2026-09-02 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 1ea91037-f035-3e40-88dc-bb0bce407bca | -5.76093 | -53.40114 | 2026-09-02 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 899c0fb5-3ddb-3d77-94c1-ad15ee3b663a | -6.20164 | -53.48587 | 2026-09-02 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7cc0480f-d7af-3d77-a0cc-2cc7783d0775 | -5.59487 | -42.3152 | 2026-09-02 04:19:00 | NOAA-21 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 4280dcc8-e0aa-3750-82af-5ae7542c1bdb | -3.37527 | -52.79301 | 2026-09-02 04:19:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 732c97b7-ada8-3b78-979b-fc03ec731783 | -5.83356 | -44.46915 | 2026-09-02 04:19:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e93eb8fb-2fed-3a93-b249-8ca280c0ea56 | -6.0903 | -53.8092 | 2026-09-02 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 45f4bc97-7314-39dd-911e-07fc4152f7b0 | -6.67988 | -43.41053 | 2026-09-02 04:19:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 1004e5d0-d9ac-3ec7-86fa-2996934df134 | -7.07438 | -44.36219 | 2026-09-02 04:19:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a2801e0f-26c8-3ca0-9b57-148235484577 | -6.436 | -53.56392 | 2026-09-02 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 73036f19-a497-3877-87b6-b7aed18f2bec | -7.64145 | -46.70842 | 2026-09-02 04:19:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 26c66c40-2280-3276-999a-d84c7f2206ed | -3.44533 | -47.27236 | 2026-09-02 04:19:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 04bf0e1c-97de-3663-bbd3-767501102524 | -6.04797 | -53.83841 | 2026-09-02 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fce7b8bf-ec08-3cb8-afd2-51e64355db19 | -6.94844 | -45.19391 | 2026-09-02 04:19:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c193cd05-8547-33d4-b236-a57b34bf7170 | -5.97692 | -53.58945 | 2026-09-02 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d6c3b56d-cd77-3b91-9ce3-6e36ec38183c | -5.98265 | -53.58727 | 2026-09-02 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0880bf47-c7a9-3a6a-ade8-60264b304ef1 | -6.98478 | -35.13297 | 2026-09-02 04:19:00 | NOAA-21 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| e06866c3-ba16-381d-b5ea-5381c371ed60 | -6.15005 | -55.68031 | 2026-09-02 04:19:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 05d2e760-a3d1-3ae7-9ebb-2ad7d534b922 | -1.96395 | -48.38001 | 2026-09-02 04:19:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 40461b77-9325-349b-9519-92e23e385f62 | -6.67886 | -43.43994 | 2026-09-02 04:19:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 10dbb152-5a14-32fa-8011-4bde8bde1703 | -6.83645 | -41.68563 | 2026-09-02 04:19:00 | NOAA-21 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 7.8 |
| b3ed5e3f-d11b-3825-b8b5-7aca3618f377 | -5.97829 | -53.58562 | 2026-09-02 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 46071d1a-0394-3798-83df-0de031ac68c9 | -6.05224 | -53.83995 | 2026-09-02 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 48fe000e-b71d-3a97-90c0-7f6964630c3f | -6.43075 | -46.27047 | 2026-09-02 04:19:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 4e60ce77-53e6-3219-b4cf-e31e21cdad60 | -4.97228 | -55.84646 | 2026-09-02 04:19:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 118bbe4d-42c4-3cfa-9a35-c49b68142175 | -4.27032 | -55.15866 | 2026-09-02 04:19:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 02e4be4f-5068-32a1-ac36-af55c420bd6c | -7.6606 | -45.87812 | 2026-09-02 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| a0d64ec9-f991-34d7-a431-134936910424 | -4.09623 | -50.42629 | 2026-09-02 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e83f2bc9-fced-3128-b27e-35c088a3ae03 | -4.49887 | -45.91172 | 2026-09-02 04:19:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 16.6 |
| a2dd4b41-970b-3f6b-bb67-146052718a39 | -6.61864 | -47.63871 | 2026-09-02 04:19:00 | NOAA-21 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9ab524c0-1359-30b1-a8a1-ce04504813ec | -6.77112 | -41.17162 | 2026-09-02 04:19:00 | NOAA-21 | SANTO ANTÔNIO DE LISBOA | PIAUÍ | Brasil | 2209401 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 8f819001-e3cd-3ac5-b86f-7f0704f72793 | -2.31002 | -48.63316 | 2026-09-02 04:19:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| c63a355c-e5a2-3ec6-b024-163edd0f6a5c | -4.3761 | -47.77821 | 2026-09-02 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 29afff9e-d537-3104-9d8f-4d7c7ed645e5 | -5.97419 | -53.57849 | 2026-09-02 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9ccfa087-aab5-30c2-bc4e-20b8ea4ec7c5 | -6.58368 | -44.78578 | 2026-09-02 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 77e9019e-32dd-364c-8e60-7be1983e20c9 | -5.97333 | -53.57902 | 2026-09-02 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1a3ec823-01f5-3a72-97ca-c638c1a4301a | -6.43142 | -53.55975 | 2026-09-02 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 89707eb3-7d35-3081-b09a-b6094c6ea898 | -6.36062 | -51.75177 | 2026-09-02 04:19:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e1ad6084-44c5-3e72-aebc-4be8d663077a | -6.07132 | -53.66883 | 2026-09-02 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| efb5c241-ce0d-3a35-b3dd-193af2962f30 | -4.97063 | -55.8558 | 2026-09-02 04:19:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| c3efb032-22f8-3cec-9953-a1fa6aeb4870 | -4.18269 | -49.4049 | 2026-09-02 04:19:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aec3c167-8c35-3b26-ab7e-11ddcd32e583 | -4.81385 | -42.67829 | 2026-09-02 04:19:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 90edad20-43f0-322e-a010-6aa0c00f755c | -6.25993 | -55.4255 | 2026-09-02 04:19:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 0b51b01c-59a7-325b-973a-74b8c80ec73e | -6.25184 | -55.43713 | 2026-09-02 04:19:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fbb3b8e9-3d1b-3a21-ae12-8fa123b1a3ab | -3.34179 | -42.80264 | 2026-09-02 04:19:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 31031e1c-7d17-3f9e-baf2-45fc6b075894 | -6.68043 | -43.4069 | 2026-09-02 04:19:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0f2579ff-2d2f-32b0-a760-f233be1c9759 | -6.85952 | -41.65496 | 2026-09-02 04:19:00 | NOAA-21 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b475b494-e4d7-3285-b12a-1dd340a122ef | -6.32145 | -54.75115 | 2026-09-02 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b2324020-d917-3fea-a662-91e0d9e3acb7 | -5.51825 | -39.86427 | 2026-09-02 04:19:00 | NOAA-21 | PEDRA BRANCA | CEARÁ | Brasil | 2310506 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 48ecdbeb-bc41-30fd-8327-f2cb0c95eef6 | -6.29752 | -47.47071 | 2026-09-02 04:19:00 | NOAA-21 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cb07498e-f730-3b03-80eb-2ed98da49dc7 | -5.25089 | -55.91394 | 2026-09-02 04:19:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| af675148-422c-3dfe-bf45-4204b6ceade6 | -6.14497 | -55.67431 | 2026-09-02 04:19:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b2a17ed7-cae4-3547-8869-d9d75e6a290a | -4.27109 | -55.15417 | 2026-09-02 04:19:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 0e099c08-69f3-33e7-80bf-0edd1e402e87 | -3.84819 | -52.03953 | 2026-09-02 04:19:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| afb7a0c5-63f0-3b27-9f06-0a84aba03b18 | -5.02659 | -43.60058 | 2026-09-02 04:19:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cb635d73-cb3d-35f9-adbf-563c169a980e | -6.43658 | -53.56063 | 2026-09-02 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4bdc41eb-430e-30d6-9969-2756957d8426 | -5.85698 | -57.5561 | 2026-09-02 04:19:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| af5e7be2-3292-3244-8b83-603ed543b5fb | -6.04583 | -53.84532 | 2026-09-02 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 22009ea1-4b3c-3602-bc65-151211af3011 | -7.13743 | -45.80875 | 2026-09-02 04:19:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8b7f4186-79d5-35db-89be-3911b5f90dd5 | -5.63583 | -43.55362 | 2026-09-02 04:19:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1bb457b1-ecd5-3195-86b2-85261bba3abb | -7.15627 | -46.84571 | 2026-09-02 04:19:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d6af626b-f05f-3447-861b-bd434a2b5d60 | -6.6765 | -43.41001 | 2026-09-02 04:19:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 16.7 |
| ce6d9513-151a-3f02-b849-8ba1b0ed3b41 | -6.19587 | -55.28035 | 2026-09-02 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 055fbd50-046a-3a7e-a423-6a40a6bf5cd4 | -5.25476 | -55.89095 | 2026-09-02 04:19:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 20740a19-8611-3917-a20c-26496d812838 | -3.52395 | -50.53058 | 2026-09-02 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bc70afb8-2bcd-3d31-82af-42c69317ce84 | -4.36742 | -47.78557 | 2026-09-02 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3f82ede6-8a2e-3b92-954d-b379c2e34f69 | -6.85589 | -41.65442 | 2026-09-02 04:19:00 | NOAA-21 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 70be71e1-7660-3eea-89ea-1d15aa0cf07e | -1.39696 | -48.15355 | 2026-09-02 04:19:00 | NOAA-21 | SANTA IZABEL DO PARÁ | PARÁ | Brasil | 1506500 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 68e7247f-e211-3e6e-b56e-0af67f0d3659 | -6.11334 | -53.45216 | 2026-09-02 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4633de98-1a2b-39dd-9055-3699cbdbf127 | -5.97172 | -53.58851 | 2026-09-02 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 3b2658aa-c7a1-3f18-a50f-307d28e9d069 | -5.62251 | -42.9349 | 2026-09-02 04:19:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 12c2cf9c-102d-31d9-b5d7-42fbf1f103b4 | -6.57376 | -44.78424 | 2026-09-02 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cd032d10-b6b0-3e8f-b3f2-7b7e23b0674e | -4.52054 | -48.75134 | 2026-09-02 04:19:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 71c043bb-05c8-3083-8bcd-7e2c693643f2 | -4.37541 | -47.78248 | 2026-09-02 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fefff17a-bbc2-30eb-94fc-dd5fe6749a57 | -6.07709 | -53.66653 | 2026-09-02 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| de6e7426-7124-3e1d-a128-dbc8f44b2bbd | -6.14768 | -55.67765 | 2026-09-02 04:19:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 742c6b53-cad9-3604-ab64-3257381bdc0b | -6.20043 | -55.42613 | 2026-09-02 04:19:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 730849be-3b6e-3a41-9d4e-bb7b3e67abfd | -6.15082 | -55.67591 | 2026-09-02 04:19:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| af542465-4d30-30c0-865a-e8c9c3078f26 | -3.85105 | -44.05632 | 2026-09-02 04:19:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ba7b2928-00da-3c83-abdf-6808c2cb2040 | -4.16437 | -47.83556 | 2026-09-02 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| a8561fde-8b37-3862-88af-6838b94d7fa4 | -7.13966 | -45.81627 | 2026-09-02 04:19:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e96e2b58-3ce1-35cd-ac8b-5507efda052b | -4.95925 | -55.84873 | 2026-09-02 04:19:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 16a6f487-c998-3b6c-a4bb-6d6621474445 | -6.43025 | -53.56636 | 2026-09-02 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 95f28cc9-7303-31d8-b91e-7173b2f94c27 | -4.35813 | -55.02631 | 2026-09-02 04:19:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4302c604-6a05-303e-b66a-c18fc3d5d58e | -3.46189 | -39.58137 | 2026-09-02 04:19:00 | NOAA-21 | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 4800956a-b875-3f3b-b7cb-995a0cb5b256 | -3.37477 | -52.796 | 2026-09-02 04:19:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 4d681be4-14e8-3f7e-bf37-e6e1fc2a2dd8 | -4.99451 | -37.1002 | 2026-09-02 04:19:00 | NOAA-21 | AREIA BRANCA | RIO GRANDE DO NORTE | Brasil | 2401107 | 24 | 33 | nan | nan | nan | Caatinga | 3.3 |
| a8d9da62-088e-3c19-a44a-61f374ecb559 | -3.06006 | -48.74657 | 2026-09-02 04:19:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 97091f93-1250-33c6-9920-fff781614a69 | -6.09089 | -53.80582 | 2026-09-02 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| debf0768-f170-35a9-a06e-da7df2e08cf3 | -6.43083 | -53.56306 | 2026-09-02 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 334a9214-e88c-3e27-acba-ca16f53ef4ac | -5.97307 | -53.58477 | 2026-09-02 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2d86a103-1e87-3872-a3cc-21fd93669adb | -5.97226 | -53.58532 | 2026-09-02 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| b75faacc-9583-3795-831d-ee49f421bf0e | -6.43541 | -53.56723 | 2026-09-02 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c9be74b1-a99c-32db-8ad3-07c8abbbdb50 | -6.81223 | -43.52635 | 2026-09-02 04:19:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5206aae1-93c4-3bee-9c90-9beb8f1ff90d | -4.97146 | -55.85112 | 2026-09-02 04:19:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 94946d58-7c6a-3e5b-acf9-d2ffd9d069b1 | -7.65063 | -45.87654 | 2026-09-02 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| a7a6dbf9-f974-3abb-8799-2c62822e8687 | -5.97771 | -53.58887 | 2026-09-02 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9c5481db-5ac2-3283-a429-003cf56a4c62 | -4.36879 | -47.77708 | 2026-09-02 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 9a846129-7dc9-3bd5-a24b-40df2d43f021 | -5.25554 | -55.8864 | 2026-09-02 04:19:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 22bd7225-f127-3c6f-81b5-bfffda63c712 | -5.73206 | -43.27748 | 2026-09-02 04:19:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README20.md)
