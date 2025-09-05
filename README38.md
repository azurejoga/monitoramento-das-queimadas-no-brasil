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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 201c4824-d6a4-35f6-9308-0db3f27c51fa | -21.36937 | -46.95254 | 2025-09-05 04:38:00 | NPP-375D | ARCEBURGO | MINAS GERAIS | Brasil | 3104106 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d47ccccb-01a3-3d46-beaf-d14b6ecc662e | -15.14451 | -52.37654 | 2025-09-05 04:38:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| da89eb82-2dcb-36be-a369-6188f0dfb35d | -15.19872 | -52.3769 | 2025-09-05 04:38:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9aea5238-4e87-363f-b3a5-0b248f23b2b8 | -15.04396 | -50.04615 | 2025-09-05 04:38:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| df1ad590-aeaa-3c8f-80f2-0d2b39274323 | -15.31892 | -52.73303 | 2025-09-05 04:38:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| aa995e80-44f5-39b7-a410-7a024ed0e531 | -17.96836 | -46.90375 | 2025-09-05 04:38:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e47473dc-c198-37d3-96eb-34d17949bff9 | -20.45956 | -54.51644 | 2025-09-05 04:38:00 | NPP-375D | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c0baf9db-9f82-3122-86c8-36844448a191 | -16.55625 | -55.12378 | 2025-09-05 04:38:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 6cb0468d-d1b6-3981-a152-feba46424785 | -13.2738 | -51.85665 | 2025-09-05 04:38:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9762e3a8-555e-3b62-b3bc-5a18217b14ef | -14.99936 | -50.09018 | 2025-09-05 04:38:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| acffa7c1-ec5a-3cd2-b421-a73709aa56fb | -21.02414 | -47.67582 | 2025-09-05 04:38:00 | NPP-375D | BRODOWSKI | SÃO PAULO | Brasil | 3507803 | 35 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 41cef09f-62fa-3652-a1ce-fd641a887bf0 | -14.48456 | -53.04432 | 2025-09-05 04:38:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ea93786f-de63-3e0d-a429-ef05464fb4a8 | -15.7544 | -53.67059 | 2025-09-05 04:38:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c81fba10-3e94-3297-abb8-39e09597c2d9 | -15.61519 | -52.90438 | 2025-09-05 04:38:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 8e3ec771-b7f1-32e5-b143-fc1cb0cfd857 | -12.96515 | -54.79861 | 2025-09-05 04:38:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 17.8 |
| ec73f7b9-8f81-3c4e-8b66-24416e4edcad | -16.91045 | -45.74793 | 2025-09-05 04:38:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cc6f1a3d-f722-32e1-bab6-017ea442b98a | -21.02047 | -47.67521 | 2025-09-05 04:38:00 | NPP-375D | BRODOWSKI | SÃO PAULO | Brasil | 3507803 | 35 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 6f5d1b03-00fd-387f-ac04-ca97fcde5987 | -12.35123 | -63.65032 | 2025-09-05 04:38:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 50381188-8302-37b8-bf5e-109e8e8590b7 | -18.56258 | -44.03662 | 2025-09-05 04:38:00 | NPP-375D | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d6f4b6bb-d427-3f66-bf6d-d6026e0f32a3 | -16.63514 | -49.51559 | 2025-09-05 04:38:00 | NPP-375D | TRINDADE | GOIÁS | Brasil | 5221403 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ad700e06-eb5a-32a4-9879-532b54963b8e | -15.7563 | -53.63831 | 2025-09-05 04:38:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e0bbd07c-5025-38c3-9cb2-35f08cf85015 | -14.55731 | -48.08226 | 2025-09-05 04:38:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e89c588b-fdd0-3dd7-afae-ca7c04e967e1 | -12.97476 | -54.79268 | 2025-09-05 04:38:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| be11bb29-5426-3756-8019-be846c62b442 | -15.31251 | -52.72755 | 2025-09-05 04:38:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2ba6267b-aaf7-3c6b-b085-4abbd8b7a6de | -20.5196 | -46.46193 | 2025-09-05 04:38:00 | NPP-375D | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9eb32ebc-7142-36d5-b392-d5f9ed2fa9b5 | -16.32256 | -52.94695 | 2025-09-05 04:38:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 084b234a-4fad-3547-aaed-ab5031557557 | -15.62163 | -52.90982 | 2025-09-05 04:38:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b8f04310-d072-3fde-b5bb-c8d490092c1c | -15.85097 | -52.29954 | 2025-09-05 04:38:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 16c50d53-5a3d-34ae-966a-d3f40734c312 | -14.98167 | -50.07243 | 2025-09-05 04:38:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 76c53ac8-a344-33b8-a809-d16219d9220a | -12.97201 | -54.80788 | 2025-09-05 04:38:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a8822da7-dc58-39b1-9960-03d3d1e49f6b | -12.63358 | -56.98837 | 2025-09-05 04:38:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e99ed95b-ea83-352f-a47e-10fecdd54972 | -15.14577 | -52.32647 | 2025-09-05 04:38:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 18ce826e-1b89-3471-b288-fad949c66075 | -16.56019 | -55.12478 | 2025-09-05 04:38:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| a4fe8906-0903-3cae-bbea-f63c04d86dcd | -14.55329 | -48.03967 | 2025-09-05 04:38:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 06c965d0-f6a9-34de-91bc-11c2a3e3cb03 | -16.55528 | -55.12899 | 2025-09-05 04:38:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| c6c712fa-2329-3c59-a5f8-3178d24b5444 | -14.33898 | -48.64759 | 2025-09-05 04:38:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7f190039-8352-3747-a1e3-a2892b22b3ff | -16.9646 | -49.30346 | 2025-09-05 04:38:00 | NPP-375D | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ade0b987-3184-3928-91dd-9c5bee5d9bed | -12.99409 | -54.82775 | 2025-09-05 04:38:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 526e72d9-e0eb-3f3c-adb9-694ce69cd8a3 | -17.66715 | -52.28816 | 2025-09-05 04:38:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f3ad8712-78e0-307b-a505-67090cac6d03 | -12.98995 | -54.82699 | 2025-09-05 04:38:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 64187dd6-7024-3d9b-b240-044adae1e009 | -20.242 | -51.30458 | 2025-09-05 04:38:00 | NPP-375D | APARECIDA DO TABOADO | MATO GROSSO DO SUL | Brasil | 5001003 | 50 | 33 | nan | nan | nan | Mata Atlântica | 8.7 |
| 5d73355e-f876-31d6-b545-95777b250ffb | -15.74294 | -53.61967 | 2025-09-05 04:38:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b9eb0995-ad57-3e08-85fb-bd7a924a9f3e | -14.03684 | -49.69238 | 2025-09-05 04:38:00 | NPP-375D | MARA ROSA | GOIÁS | Brasil | 5212808 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a02e26ab-cd12-36c2-be5c-ae4a2f06a880 | -18.46634 | -53.03406 | 2025-09-05 04:38:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 32489420-53b7-3613-b500-e855bbe6d8d9 | -17.48442 | -43.3383 | 2025-09-05 04:38:00 | NPP-375D | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b38e188a-61fe-3af7-8f3b-e433d17dd53c | -21.2827 | -43.88342 | 2025-09-05 04:38:00 | NPP-375D | BARBACENA | MINAS GERAIS | Brasil | 3105608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 2126423b-08fb-37df-aa86-37f84b9e9cac | -12.99478 | -54.82391 | 2025-09-05 04:38:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| b5861004-7b28-3896-976b-4787a54c2f86 | -17.62137 | -43.76846 | 2025-09-05 04:38:00 | NPP-375D | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 92cd3d63-127a-3f9d-a4cb-329188b2909b | -17.53296 | -46.61313 | 2025-09-05 04:38:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a88afa64-e516-34e8-981e-13ab267d74a5 | -15.06042 | -50.0631 | 2025-09-05 04:38:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 17b62117-e72e-3d6e-b0c4-e30b93a87632 | -15.57256 | -50.33301 | 2025-09-05 04:38:00 | NPP-375D | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6893a129-e027-3f21-b0f7-8903ea34b85f | -12.97891 | -54.81702 | 2025-09-05 04:38:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 35af805e-d897-305a-bf6e-28f377791682 | -14.56748 | -48.08414 | 2025-09-05 04:38:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9f352c54-5fb5-3211-94c6-b0d7e0b52ce1 | -14.28947 | -45.21476 | 2025-09-05 04:38:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 04d636fe-f1a4-38b1-a6aa-d444275b11ad | -15.54945 | -48.41231 | 2025-09-05 04:38:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e91613df-685d-38da-b5e3-bb78700f3e16 | -15.18802 | -51.17022 | 2025-09-05 04:38:00 | NPP-375D | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b1ec27e2-5a5a-33ff-9683-a3aa43aaf6aa | -15.19805 | -52.38091 | 2025-09-05 04:38:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 8c6cee39-60d9-3063-9b18-7543264841a0 | -13.77551 | -52.70941 | 2025-09-05 04:38:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0bcdac0d-6aea-38d2-970c-36eb879819a0 | -15.84679 | -52.30316 | 2025-09-05 04:38:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c395d868-fb1c-3e54-84ad-15ba6ac9adde | -15.76079 | -53.63456 | 2025-09-05 04:38:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dc563c42-0d81-379a-9737-489f7f57553b | -12.63778 | -56.98658 | 2025-09-05 04:38:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fb91662d-b064-3ce3-a750-4f5df1747cc3 | -12.98578 | -54.80257 | 2025-09-05 04:38:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f906312d-7d34-31e0-9366-63057f006c1a | -13.77477 | -52.71367 | 2025-09-05 04:38:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9b7c0849-221f-3f26-85d0-03427723681e | -15.05709 | -50.06254 | 2025-09-05 04:38:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c3d79388-ea2e-3c43-a8ca-7ff3c2d4ebfa | -15.756 | -53.66159 | 2025-09-05 04:38:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 86af6f7e-6739-3cbf-91c5-d7e386628f44 | -15.7507 | -53.66988 | 2025-09-05 04:38:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f0a9f103-463e-391c-85d4-e3e534d8a691 | -14.04074 | -49.68937 | 2025-09-05 04:38:00 | NPP-375D | MARA ROSA | GOIÁS | Brasil | 5212808 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 36a9772c-21eb-34ab-8532-3ac26acb2cf8 | -14.99385 | -50.08188 | 2025-09-05 04:38:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8e97b343-5398-342d-8626-8ed09d71005f | -15.36274 | -46.4065 | 2025-09-05 04:38:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| df77a0ba-a349-3a53-a095-e4a3c31c45a3 | -13.33813 | -54.39104 | 2025-09-05 04:38:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 73adaf2d-704a-399f-aab0-c19fa76e13b4 | -13.27811 | -51.78814 | 2025-09-05 04:38:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bdc5a648-b8e7-3392-95a7-c353bf85e249 | -17.58265 | -52.55799 | 2025-09-05 04:38:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 56bb0308-67d9-32b9-b502-68f0cf6a59f5 | -15.21368 | -52.37432 | 2025-09-05 04:38:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cf420153-b09c-3d26-befb-0ec385e39557 | -15.16646 | -52.39668 | 2025-09-05 04:38:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 428dc1f3-691e-3b6f-b0ed-0cf76026fea2 | -21.49137 | -46.19443 | 2025-09-05 04:38:00 | NPP-375D | DIVISA NOVA | MINAS GERAIS | Brasil | 3122405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 029aae0a-42a4-3ab1-a279-e5f1183ba467 | -15.13529 | -52.34557 | 2025-09-05 04:38:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6445ab20-dc02-3882-999b-babe5603b79e | -12.972 | -54.78433 | 2025-09-05 04:38:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| df3bb71e-3c55-3a01-8a53-366e56b0a43d | -15.5782 | -50.31915 | 2025-09-05 04:38:00 | NPP-375D | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6bf60afb-c7f2-333e-a882-83910258a240 | -16.3069 | -52.95265 | 2025-09-05 04:38:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 43a5e1cb-a889-3970-af80-75e5aff88fbd | -17.85978 | -40.13169 | 2025-09-05 04:38:00 | NPP-375D | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 89336ad4-468b-3fb8-bc19-ba77d9c1ef9a | -19.68315 | -54.80989 | 2025-09-05 04:38:00 | NPP-375D | CORGUINHO | MATO GROSSO DO SUL | Brasil | 5003108 | 50 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 189daa9f-b5ac-3abd-9f46-d0f7450f70a9 | -14.29456 | -53.08542 | 2025-09-05 04:38:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 79272e67-1912-3f28-a44a-ebde0ec6b4d7 | -15.73842 | -53.62374 | 2025-09-05 04:38:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3b32af4e-74f2-3680-96df-5694976523ef | -16.90268 | -45.74686 | 2025-09-05 04:38:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f7dc5f94-be0c-36fa-94e0-33d83738c760 | -14.98386 | -50.08018 | 2025-09-05 04:38:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fad1e78e-2241-3a69-b296-eb5ed8b97a9c | -15.07763 | -50.06231 | 2025-09-05 04:38:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 120bab50-3149-3775-8dd2-caae56f84011 | -18.46286 | -53.03337 | 2025-09-05 04:38:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d5fc4854-985b-364b-87d9-4cb4b1d2a33f | -12.64315 | -56.99039 | 2025-09-05 04:38:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5a22e8f0-3009-392a-bf65-0c54a572eaf5 | -15.20586 | -52.35666 | 2025-09-05 04:38:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fbc38506-9cc7-36ed-94f7-f45c2b8b56fa | -15.19521 | -52.3763 | 2025-09-05 04:38:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b019b21e-5a41-3059-a478-5fe9466676c5 | -17.62079 | -46.70351 | 2025-09-05 04:38:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 78496a1b-fa7f-3485-9a27-a72839f53a0e | -14.58613 | -48.03012 | 2025-09-05 04:38:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 75f2034e-c554-3bbd-ba1e-9684199882cb | -17.86016 | -40.12791 | 2025-09-05 04:38:00 | NPP-375D | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 0d8d878a-c741-3bee-be09-faaf9b98d286 | -15.63237 | -52.89003 | 2025-09-05 04:38:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f088f308-4f27-31f1-aed7-16b8834c7cdf | -14.54219 | -53.05936 | 2025-09-05 04:38:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a654b98c-3c0f-38db-af84-166979c00f7e | -15.05136 | -50.09842 | 2025-09-05 04:38:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 827f1968-8757-3de7-a810-a68f88461d82 | -15.15161 | -52.37736 | 2025-09-05 04:38:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6473b835-cb83-3fc4-9943-121d79c33de9 | -18.73175 | -46.88452 | 2025-09-05 04:38:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9dc25ac4-088f-3302-8eeb-551c412c15b3 | -15.7528 | -53.67963 | 2025-09-05 04:38:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6d9e7be6-d014-30e1-8f20-4347749f2032 | -16.49483 | -43.73246 | 2025-09-05 04:38:00 | NPP-375D | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README39.md)
