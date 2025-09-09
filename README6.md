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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6d1e4aa2-8078-3e3b-8dbf-0219cf430d68 | -12.9482 | -54.7519 | 2025-09-09 02:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 3faa5e15-be90-3749-8160-e87225a95ded | -18.8174 | -49.6816 | 2025-09-09 02:00:00 | GOES-19 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 169.7 |
| 4d567c13-7eef-32fb-b65b-d3a2b9be1be9 | -5.5892 | -45.0278 | 2025-09-09 02:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 0e5e631b-cac8-3b8e-ad4d-4ee943d7a673 | -18.8375 | -49.6777 | 2025-09-09 02:00:00 | GOES-19 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 269.2 |
| fbdc1f4c-e2d7-38a6-a0fa-0903f9f69e8c | -5.589 | -45.0505 | 2025-09-09 02:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 80.4 |
| c29c117f-ac99-3ba4-829a-28ce938d6cbe | -21.6329 | -47.0218 | 2025-09-09 02:00:00 | GOES-19 | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Cerrado | 55.9 |
| 5d7de1b5-2ce6-3c5e-bcdf-d59f22dca807 | -12.1988 | -53.9024 | 2025-09-09 02:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 9142a0a6-5f58-33fb-9055-c359854ca355 | -10.011 | -64.9339 | 2025-09-09 02:00:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 100.0 |
| 4a9c72c0-6aae-3da3-9f50-4e4cabef267d | -10.0111 | -64.9151 | 2025-09-09 02:00:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 158.7 |
| b9a85ce0-f105-37ac-938a-6bd65b65fb43 | -18.4808 | -49.5447 | 2025-09-09 02:00:00 | GOES-19 | CACHOEIRA DOURADA | GOIÁS | Brasil | 5204250 | 52 | 33 | nan | nan | nan | Cerrado | 101.6 |
| 55b19932-7d77-3bbb-9cd6-e6a534b1afdb | -18.8375 | -49.6777 | 2025-09-09 02:10:00 | GOES-19 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 199.5 |
| 460dfe2e-a75d-3eb4-b8cf-35fecf6744a4 | -18.8174 | -49.6816 | 2025-09-09 02:10:00 | GOES-19 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 136.1 |
| 879c16ee-6c0c-3d1a-adfe-30946a764356 | -12.9482 | -54.7519 | 2025-09-09 02:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 52.3 |
| a57e754a-1132-3c08-9a33-545248d06d70 | -14.3231 | -47.3171 | 2025-09-09 02:10:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 66.5 |
| 27792972-6e22-3abf-a764-cc237cecda2a | -14.3425 | -47.3139 | 2025-09-09 02:10:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 77.4 |
| be03dcb0-d5da-3c86-a39c-c6ddeb0058eb | -5.5705 | -45.0291 | 2025-09-09 02:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 70.8 |
| aca35d68-b043-3819-9d3a-0a9c0972acb0 | -10.0111 | -64.9151 | 2025-09-09 02:10:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 180.7 |
| 8b651e26-9c3b-3a6d-9677-16381ce0f864 | -5.5703 | -45.0518 | 2025-09-09 02:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 101.6 |
| 9124c9b9-248e-36ba-b578-d0d49911bbd0 | -12.1988 | -53.9024 | 2025-09-09 02:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 84.5 |
| 94b5eaa4-b0ac-3764-82fd-94fae08267a3 | -14.362 | -47.3107 | 2025-09-09 02:10:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 68.7 |
| cbbf19cd-0107-3bd4-b20f-764876e8db77 | -12.1991 | -53.8817 | 2025-09-09 02:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 1103ed30-7c83-3923-ac48-6262007fc73e | -5.589 | -45.0505 | 2025-09-09 02:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 75.8 |
| ad9a40da-3af4-3d7d-b9dd-b082ae12f0f3 | -11.4277 | -43.6017 | 2025-09-09 02:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 65.5 |
| b550689c-c3d4-3ecb-b239-14932c6cb283 | -10.011 | -64.9339 | 2025-09-09 02:10:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 103.7 |
| 600189c6-f343-3316-9e9c-25ef929136a0 | -12.1991 | -53.8817 | 2025-09-09 02:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 79.2 |
| 7ec14f17-5000-3e79-b1dc-cbf19a6b987c | -12.1988 | -53.9024 | 2025-09-09 02:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 88.1 |
| 9edaebcb-3bf6-3485-b089-c49a8dfd5ecb | -18.8174 | -49.6816 | 2025-09-09 02:20:00 | GOES-19 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 178.1 |
| 48cf6eaa-c6a8-3719-a471-515a6014f34c | -18.8168 | -49.7042 | 2025-09-09 02:20:00 | GOES-19 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 82.2 |
| b7bf1a32-d011-33f4-a6cb-42e86204fafe | -18.838 | -49.6551 | 2025-09-09 02:20:00 | GOES-19 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 83.6 |
| fd9e7aab-92ab-395e-a7f9-48f54ad0089f | -14.362 | -47.3107 | 2025-09-09 02:20:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 62.8 |
| 334fb387-d63d-3afa-8bd8-2b9548639347 | -18.8369 | -49.7003 | 2025-09-09 02:20:00 | GOES-19 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 141.3 |
| 799d41bd-a3bc-3c46-ad9d-cbaf32ff2df9 | -11.4277 | -43.6017 | 2025-09-09 02:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 70.0 |
| e1a7f997-4ca4-3776-873e-cf088f8cf92e | -5.5703 | -45.0518 | 2025-09-09 02:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 89.8 |
| e7b63237-62a5-316d-8ab2-3dde21865c64 | -5.589 | -45.0505 | 2025-09-09 02:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 90.9 |
| eb5b0102-0789-3e70-af9e-2b2a3e4cc322 | -10.0111 | -64.9151 | 2025-09-09 02:20:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 161.6 |
| ba65c5eb-34ab-3c9b-8f8a-9126fe18a68f | -10.011 | -64.9339 | 2025-09-09 02:20:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 95.3 |
| 0dbcb185-49ee-3f9a-ab4c-3700a5cc0e59 | -18.8375 | -49.6777 | 2025-09-09 02:20:00 | GOES-19 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 323.3 |
| 8fef9533-2908-3767-adfd-31c240ee5fa0 | -17.2757 | -46.7538 | 2025-09-09 02:20:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 45407d49-9984-3147-8a83-a93aed94c208 | -11.3014 | -46.5018 | 2025-09-09 02:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 48.2 |
| b085781d-e8c2-38ab-b0cc-2375814793cb | -5.5703 | -45.0518 | 2025-09-09 02:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 84dd920d-a546-336c-9d79-d7eed2b4f248 | -17.2757 | -46.7538 | 2025-09-09 02:30:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 770b8056-72c2-3d55-abfd-f5bb66a9d22d | -18.8168 | -49.7042 | 2025-09-09 02:30:00 | GOES-19 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 64aa2129-d81d-322b-bc5c-449f43d0c1d9 | -12.1988 | -53.9024 | 2025-09-09 02:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 86.6 |
| 5e8659ed-2d61-343b-b0b6-cc9b5c898ad3 | -5.589 | -45.0505 | 2025-09-09 02:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 61.9 |
| 6aa6f771-9236-34aa-b891-b6b756765d2d | -10.0111 | -64.9151 | 2025-09-09 02:30:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 166.2 |
| aa0109db-cb4b-33d1-aff1-a80f15dad5cd | -11.3014 | -46.5018 | 2025-09-09 02:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 54.8 |
| ea5a8a78-2810-39b9-aaff-8856669a2324 | -18.8369 | -49.7003 | 2025-09-09 02:30:00 | GOES-19 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 126.7 |
| 86e17827-5c6a-37d4-9662-8a893cef7f15 | -12.9482 | -54.7519 | 2025-09-09 02:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 50.3 |
| f7d7c4bc-e1d3-3662-a134-deaa9d67901c | -5.5705 | -45.0291 | 2025-09-09 02:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 57.5 |
| ac422000-cad7-3f6b-81ed-e32f33ed2c6e | -10.011 | -64.9339 | 2025-09-09 02:30:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 95.1 |
| c416916c-ea48-3a37-9340-ff6e4750c398 | -18.8174 | -49.6816 | 2025-09-09 02:30:00 | GOES-19 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 161.0 |
| 80ead0b5-fcc9-3864-a202-8bb29e457425 | -18.8375 | -49.6777 | 2025-09-09 02:30:00 | GOES-19 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 232.0 |
| fb7edf7d-9e14-3ddd-9e04-65e0bcb3be7d | -12.1991 | -53.8817 | 2025-09-09 02:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 81063fc2-4477-3b88-850b-4e273b07d304 | -5.5703 | -45.0518 | 2025-09-09 02:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 88.2 |
| 10d38698-b4d1-37b6-bce6-22366eb7e9d7 | -18.8369 | -49.7003 | 2025-09-09 02:40:00 | GOES-19 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 140.3 |
| 2bdbfbb3-b077-3ee8-8561-c4f18773603e | -11.9361 | -50.9765 | 2025-09-09 02:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 61.0 |
| 98747f4a-50da-3355-a487-49d014b1ab1b | -10.011 | -64.9339 | 2025-09-09 02:40:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 76.0 |
| 8ff81947-48e8-3757-bac3-4246fcc7c846 | -11.4277 | -43.6017 | 2025-09-09 02:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 68.2 |
| d638fa12-77ec-3a9d-adfd-6a77d32362a1 | -12.1991 | -53.8817 | 2025-09-09 02:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 81.5 |
| e241c645-905c-37cb-9544-d7a5e873d723 | -5.589 | -45.0505 | 2025-09-09 02:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 64.1 |
| 65322f50-ffcf-39b8-bc65-3dfc27d2c6d7 | -12.1988 | -53.9024 | 2025-09-09 02:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 98.6 |
| 2b0fef16-5b09-3cf6-ac78-0fdd520f1d37 | -10.0111 | -64.9151 | 2025-09-09 02:40:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 145.3 |
| 5ebb7bfb-4d5f-32a7-9ae0-ad808a96933c | -18.8375 | -49.6777 | 2025-09-09 02:40:00 | GOES-19 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 216.3 |
| 7afd1234-f1b3-3034-9ae9-55be8a2318f6 | -17.6847 | -52.2615 | 2025-09-09 02:40:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 64.1 |
| 1d043c24-1def-3365-b359-82343fca743d | -18.8174 | -49.6816 | 2025-09-09 02:40:00 | GOES-19 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 131.3 |
| 2ce29ed3-61aa-32b7-89dd-1977fdc5c126 | -11.9551 | -50.9743 | 2025-09-09 02:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 54.4 |
| 216eccb1-407e-3b53-a095-b1017623e5cc | -17.2757 | -46.7538 | 2025-09-09 02:40:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 62.1 |
| 761cede2-577b-3aca-a040-cd7b0a4ef7cc | -17.2757 | -46.7538 | 2025-09-09 02:50:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 88.9 |
| 03d5b9b2-1175-3a3a-8c7d-390e90823389 | -5.589 | -45.0505 | 2025-09-09 02:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 66.1 |
| ee4bca00-ab43-3ec1-bbf9-d01ad3e5788b | -18.8375 | -49.6777 | 2025-09-09 02:50:00 | GOES-19 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 143.2 |
| 93d59980-05b3-3d0b-bbf1-a2c5b9a1a95f | -10.011 | -64.9339 | 2025-09-09 02:50:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 83.9 |
| 5f198eb7-39f0-39ab-a25b-70c21ad004af | -11.3014 | -46.5018 | 2025-09-09 02:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 53.1 |
| 0c8d4594-bf68-3146-8054-f41eb4c27e5f | -18.8369 | -49.7003 | 2025-09-09 02:50:00 | GOES-19 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 95.0 |
| 30b722c2-3ebf-3c9b-9d95-3a970e7166d1 | -12.1991 | -53.8817 | 2025-09-09 02:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 83.3 |
| 463faea8-869f-3fc2-99e1-bf154a23c5d8 | -15.5264 | -48.3985 | 2025-09-09 02:50:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 50.5 |
| 9ebf61ec-519a-3be4-86a1-dbe9d6aba836 | -5.5703 | -45.0518 | 2025-09-09 02:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 79.9 |
| d60c66ee-d059-3228-b53d-80d348f4a1ef | -12.1988 | -53.9024 | 2025-09-09 02:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 90.8 |
| d24260d5-e896-3d04-940c-6bbef2119691 | -17.6847 | -52.2615 | 2025-09-09 02:50:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 6502f9e0-064d-391e-a259-9ea8a2314f4a | -18.8174 | -49.6816 | 2025-09-09 02:50:00 | GOES-19 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 80.2 |
| ae7a7e45-c66e-355a-8c9a-c6f802cd0c70 | -11.9551 | -50.9743 | 2025-09-09 02:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 60.2 |
| 03720278-d556-3355-aa9a-9a2f07f4d4d4 | -10.0111 | -64.9151 | 2025-09-09 02:50:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 132.1 |
| 5a25fc70-8a7e-3f0d-adff-b8838b29cb62 | -11.9361 | -50.9765 | 2025-09-09 02:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 50.6 |
| 19887951-4302-3ea0-a2fc-5ee4c3b6faba | -18.74035 | -40.092 | 2025-09-09 02:56:00 | NOAA-21 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| b167c7fe-d13b-380a-b1ea-8c7416ab6c05 | -10.962 | -45.113 | 2025-09-09 03:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 358.7 |
| 642d1f79-7a71-3842-be39-15372523d28e | -10.0111 | -64.9151 | 2025-09-09 03:00:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 120.8 |
| 6ce3c86a-1b32-3fbc-af8d-acdcdfca724a | -11.9551 | -50.9743 | 2025-09-09 03:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 77aa8995-20cb-3532-9bbc-2b327ccae5b9 | -10.011 | -64.9339 | 2025-09-09 03:00:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 57.6 |
| d4ad7606-ef00-3976-893f-42164a9c0504 | -18.8168 | -49.7042 | 2025-09-09 03:00:00 | GOES-19 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 14cbd3e8-1857-3418-b26c-1d651f4a1228 | -12.5295 | -45.2524 | 2025-09-09 03:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 57.7 |
| cf37af94-1bdd-3b13-b0fc-d2560698ae10 | -10.9811 | -45.1104 | 2025-09-09 03:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 710.2 |
| 273db3d4-ca18-3c89-bbcb-a6a00d6a1c0b | -9.9925 | -64.9158 | 2025-09-09 03:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 46.3 |
| 70dbc91b-8b99-3c3a-ac4d-69c18e8982e9 | -11.9735 | -51.0148 | 2025-09-09 03:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 55.5 |
| b9a12eaa-72e7-38ff-be57-d79a4717b609 | -10.9616 | -45.1361 | 2025-09-09 03:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 47.6 |
| b0a8502d-d4a5-30bc-b275-c0a10c6fb858 | -18.8369 | -49.7003 | 2025-09-09 03:00:00 | GOES-19 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 82.2 |
| 9662c19e-d1fd-3fb8-9d9c-6fd0cb0af814 | -12.1991 | -53.8817 | 2025-09-09 03:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 67cc3cce-b4a1-3c44-92b9-8e1d1aa036ef | -11.3014 | -46.5018 | 2025-09-09 03:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 59.5 |
| 5d818d27-6246-312b-8572-a67e3f0f40a1 | -18.8375 | -49.6777 | 2025-09-09 03:00:00 | GOES-19 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 168.3 |
| a6c651ee-cfe8-359c-8d90-4f2c49421f68 | -10.9624 | -45.09 | 2025-09-09 03:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 235.2 |
| ec43be48-e3f4-3f75-aee4-b57e0f8fd3de | -17.2757 | -46.7538 | 2025-09-09 03:00:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 6f751be2-9efc-317a-b617-70177b0a5ad1 | -12.1988 | -53.9024 | 2025-09-09 03:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 84.2 |


[Clique aqui para ver as próximas entradas](README7.md)
