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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 13f96de6-7b5b-392f-bfa0-13d01fb02dee | -6.35166 | -57.86363 | 2026-09-06 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2395f150-33bb-3798-9a4e-c5a484ebd1aa | -3.77961 | -59.71581 | 2026-09-06 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 39af72ca-c9df-3342-aa1f-7ec7f9e55edf | -5.33496 | -56.03451 | 2026-09-06 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9dcd0682-2520-3f47-8e09-1e9d020867ab | -4.24296 | -62.23487 | 2026-09-06 05:23:00 | NPP-375D | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 40df12bf-e847-3d1c-9a9d-9db7f7658026 | -6.09194 | -55.59468 | 2026-09-06 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 61478a76-1ce0-3b36-bb27-08ec7395c3f4 | -3.81588 | -55.88565 | 2026-09-06 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6c795b8f-0de4-32a5-adb4-2eaf65877146 | -3.89762 | -57.16454 | 2026-09-06 05:23:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b5fce217-3219-3559-82c4-f9cb13947e4f | -3.17738 | -61.13726 | 2026-09-06 05:23:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0f294d64-cf42-36bf-b965-08b89e0302a5 | -4.47053 | -55.0937 | 2026-09-06 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 7d063a0d-18be-3ffe-9b49-c361d1c97bc4 | -4.88135 | -55.88058 | 2026-09-06 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e6c29695-b05d-3b8d-bef3-d4c1fcc0b6d7 | -5.84849 | -52.04914 | 2026-09-06 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f7a35e01-ddcf-3e33-9499-dd750c8ed2d9 | -3.75186 | -55.9656 | 2026-09-06 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 42a2ffcd-700d-396d-bc61-f8263864e090 | -2.85993 | -50.46993 | 2026-09-06 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 02b0cad3-e336-3861-93d4-6249008a6a63 | -3.81142 | -55.89216 | 2026-09-06 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 10c43222-582a-3c66-b8f5-4c278d554a4f | -4.28989 | -59.9622 | 2026-09-06 05:23:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| eb03ebeb-00e4-3159-90ae-ac90d5bbe784 | -3.24367 | -47.24766 | 2026-09-06 05:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 326a567c-6e4e-3383-9fba-139f23b4b199 | -3.27248 | -57.88156 | 2026-09-06 05:23:00 | NPP-375D | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 35cc7611-18f7-3ecb-a022-4b20af81ab20 | -3.81477 | -55.89268 | 2026-09-06 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2ef0a7a3-a615-3143-926b-e9cc855d93bb | -4.6686 | -55.63556 | 2026-09-06 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| cbdbe00c-dcd4-32c7-9709-bae3e13971aa | -3.21514 | -53.1687 | 2026-09-06 05:23:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 29c4930f-695d-3706-9642-3628b7dba078 | -7.95428 | -54.88597 | 2026-09-06 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b213c8c7-ee58-3afa-b8e1-79ecdcde4d9f | -6.00293 | -57.7794 | 2026-09-06 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9905ffe3-7d54-3d80-8150-462029d2b0d3 | -2.73547 | -60.06903 | 2026-09-06 05:23:00 | NPP-375D | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 632eaa76-f19a-383e-8771-aca97425cf23 | -4.67648 | -55.62947 | 2026-09-06 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6baa2786-a5a8-390c-8d3c-da802efc8d55 | -5.35901 | -56.04523 | 2026-09-06 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 218624a6-48b4-3fcf-a9da-2fb593890029 | -5.25592 | -59.98051 | 2026-09-06 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0d91fe54-7429-397f-b646-9f0667004b03 | -10.75143 | -60.71798 | 2026-09-06 05:23:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0b506748-b905-346d-8303-e58cfbe496ad | -6.64137 | -59.44191 | 2026-09-06 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8dc12739-044b-30ee-9098-7566d3fdd08e | -5.13475 | -56.27148 | 2026-09-06 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 1a68a155-50cb-327d-b8e1-18770126170c | -13.35182 | -61.13557 | 2026-09-06 05:23:00 | NPP-375D | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0578028e-9d06-3c4c-9368-48836b0c15d6 | -5.14701 | -55.95105 | 2026-09-06 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 49094f51-9dbb-3c1e-ae3e-2ec1fa068945 | -2.58866 | -49.48921 | 2026-09-06 05:23:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9101396e-6556-3a4f-b2c9-6c48102dbc47 | -5.32879 | -56.0299 | 2026-09-06 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1a9ea2f6-a82a-38b2-bdcf-1a660abdbca1 | -5.35224 | -56.02232 | 2026-09-06 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 214bf718-c8df-3801-ac44-1d64f9eb9891 | -5.92744 | -47.8919 | 2026-09-06 05:23:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5c6a4402-ccf2-3891-b04e-2e79b6a14a2b | -5.35113 | -56.02943 | 2026-09-06 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bfc76392-a977-365f-aef4-69b6d0201a38 | -5.36685 | -56.03917 | 2026-09-06 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| c136670f-3c39-3a78-bc06-7ebe6598a5f8 | -2.92053 | -60.99656 | 2026-09-06 05:23:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a86c2f96-6e02-383d-9658-ca836d3dbc5f | -5.64777 | -60.23584 | 2026-09-06 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ba026f16-0c2f-366f-b2da-0219a159aad4 | -5.99905 | -57.78235 | 2026-09-06 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b5cdcb88-f2b9-37ba-bd01-e5b6c4f42230 | -3.20205 | -58.71242 | 2026-09-06 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2b27b433-b4e0-3ea6-9342-29b2dd56ee89 | -13.8093 | -51.645 | 2026-09-06 05:23:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7e6a3757-10d3-3785-8ca5-37c63c178cdd | -4.36744 | -47.7755 | 2026-09-06 05:23:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 19.7 |
| 952923b2-ccf1-3cfb-b85b-75897f5b2edc | -5.84679 | -52.04594 | 2026-09-06 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1cae0169-e27b-3308-aa04-2c8f8a36bd91 | -5.14309 | -55.95408 | 2026-09-06 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c19ab8ac-8786-32b9-88c4-560eb3481a3d | -7.10373 | -56.51216 | 2026-09-06 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 842ec600-36db-3967-9b03-8667a193086d | -5.13875 | -60.36215 | 2026-09-06 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| edb584ae-89e2-3c7f-8092-db3b1bd4f39c | -3.78718 | -58.85342 | 2026-09-06 05:23:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| cbc02b90-45e1-3cc7-b281-44fbf0cdbc32 | -6.58825 | -58.60065 | 2026-09-06 05:23:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a99670ca-f91a-3319-931f-b3834f8de42e | -10.74313 | -60.76849 | 2026-09-06 05:23:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9e61adcf-6840-332b-bd28-6a3be5c4a29a | -3.90418 | -55.88155 | 2026-09-06 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c09a8f99-dc28-3861-86aa-fcbb767cef59 | -6.26057 | -51.84723 | 2026-09-06 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 861b5a23-8e06-30af-9972-a0248b522b91 | -4.21954 | -59.55725 | 2026-09-06 05:23:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9dda7d5f-4c2a-3fc7-8fae-9eb421048198 | -4.47455 | -55.09051 | 2026-09-06 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c57d3ea3-8eec-3bdc-8eb6-62595f9da8c9 | -5.28192 | -60.12472 | 2026-09-06 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a69d9e75-450d-34c8-8a0d-37369d2a75de | -4.47798 | -55.09104 | 2026-09-06 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6c731383-1332-3748-b5a6-5a276916b2ee | -10.75839 | -60.71917 | 2026-09-06 05:23:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 15c5eda4-6726-3cf5-8606-c1c761c717a6 | -5.36574 | -56.04628 | 2026-09-06 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e93471f1-fb3e-3d2e-8c60-093240db60cb | -13.82088 | -51.66832 | 2026-09-06 05:23:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 820e819c-bb0c-3a97-a92f-a05d86672053 | -5.14927 | -55.9587 | 2026-09-06 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8b3fe821-f83a-39aa-a15f-3378cf6574a7 | -7.03524 | -55.49852 | 2026-09-06 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a4f79bc4-d390-3b45-817a-8045de0d25ab | -6.09058 | -57.69333 | 2026-09-06 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ad3802ab-cf47-32f0-8353-616c5745c375 | -5.35616 | -56.01927 | 2026-09-06 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 94da8bb4-cc9e-3b64-a327-fd837a1b9802 | -1.4895 | -54.8275 | 2026-09-06 05:23:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e083b0de-9d35-38e4-8259-e55502f5ac48 | -5.16681 | -56.04501 | 2026-09-06 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ef981639-8f16-36bb-80ee-93070832910b | -3.15553 | -50.82836 | 2026-09-06 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 469ccf28-1f37-3ba2-84ab-e4f9c3270497 | -5.34887 | -56.0218 | 2026-09-06 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8484187b-4179-34a7-b9cc-230a75ff98bc | -3.80918 | -55.88461 | 2026-09-06 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c8508067-a86a-363f-a34f-7b30dc384380 | -3.03932 | -59.36055 | 2026-09-06 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cb55376f-eb37-3410-bb89-44a9e8e3834f | -4.66521 | -55.63507 | 2026-09-06 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e657199c-2dc4-3103-be5c-d221419aab49 | -5.35339 | -56.03707 | 2026-09-06 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 85b9dd63-f6bd-306d-8049-161dc8504732 | -2.86431 | -50.47057 | 2026-09-06 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 409bd213-6355-37e5-bcee-04e7e12e6898 | -5.1342 | -56.275 | 2026-09-06 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 9715733c-8391-34cd-8121-25729027bc66 | -10.74859 | -60.71352 | 2026-09-06 05:23:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6453e3da-468b-3f72-b8f7-c655cca6dd99 | -5.35842 | -56.02692 | 2026-09-06 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c86932a0-b41d-3723-a399-8fa33492a04e | -6.88071 | -55.61382 | 2026-09-06 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3a5445b2-cba9-34a1-8413-c5eba1429836 | -10.74447 | -60.71681 | 2026-09-06 05:23:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 28335447-38c1-315f-808a-1424b116a64d | -10.75555 | -60.71471 | 2026-09-06 05:23:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| fcf8d64a-0b68-3a2f-a3ce-11eee608db5e | -6.95887 | -59.73951 | 2026-09-06 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2faa9712-9fa8-3d80-867f-4dda05f33539 | -6.06619 | -57.80349 | 2026-09-06 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f7a460a1-d894-3d45-830a-54f018a45a8e | -3.79633 | -55.879 | 2026-09-06 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ab13a35e-8ca2-3a50-8e57-a750b75071a2 | -5.34943 | -56.01823 | 2026-09-06 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 616c132e-bb35-3f38-9f87-14e5d49f0ea6 | -7.24571 | -59.52589 | 2026-09-06 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| eaca148c-cac1-33d6-a895-f31691e3724f | -3.78136 | -59.71473 | 2026-09-06 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e793f21d-d961-3af2-95a3-2b76e96c6075 | -6.09536 | -55.59521 | 2026-09-06 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8d0af533-ba84-3937-8cc7-c22bc03b3383 | -6.02118 | -57.68615 | 2026-09-06 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c08a2b3b-1159-32c6-8c91-de8f024aeaba | -5.92149 | -47.8945 | 2026-09-06 05:23:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6789ff5f-ecdc-317d-ba4d-1161ceac6986 | -1.39327 | -55.17446 | 2026-09-06 05:23:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 077f9cf2-c603-3305-9682-09e7241f6c94 | -3.859 | -51.03828 | 2026-09-06 05:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 831e1478-291c-34e2-af1e-47063f6b7b73 | -3.10898 | -60.65347 | 2026-09-06 05:23:00 | NPP-375D | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 49294fd9-0be8-306e-a705-2887ac6788e6 | -6.89563 | -62.95793 | 2026-09-06 05:23:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 41395343-dc4d-3757-8cb5-29e1acf56a06 | -6.12716 | -57.74189 | 2026-09-06 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e184b32e-6fc6-3d48-90c1-45dd1fd06279 | -3.15614 | -50.82435 | 2026-09-06 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 76245ef6-b136-3b55-ae37-ca2c17b4f2dd | -3.56293 | -56.3106 | 2026-09-06 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 1080a5ef-c37c-3013-ad8d-489db390e900 | -10.75491 | -60.71857 | 2026-09-06 05:23:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e1bb64dd-b22e-3021-86b3-6add46aedae5 | -6.87097 | -55.60848 | 2026-09-06 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| b70b94b1-e94f-3213-9e49-523905b990c3 | -6.15307 | -57.78941 | 2026-09-06 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 34e0fe5a-ee6c-3dc2-bbe8-2a9f038a46cb | -6.95257 | -59.73454 | 2026-09-06 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 46d30006-9763-33ae-a948-0d0bf7b88258 | -5.14143 | -55.96477 | 2026-09-06 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 38b57adc-26e3-3bd3-af50-805e9590043f | -5.14424 | -55.96885 | 2026-09-06 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |


[Clique aqui para ver as próximas entradas](README24.md)
