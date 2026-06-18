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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2a2a09d0-05a0-35ec-b3c9-3ffa274c72d2 | -4.3588 | -47.7636 | 2026-06-18 00:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 7930b911-dc9c-32ec-8165-eda9ce012134 | -9.215 | -47.9461 | 2026-06-18 00:00:00 | GOES-19 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 61.5 |
| f7872d95-60ef-3bba-9e97-6e772ccda6c6 | -12.7741 | -44.5396 | 2026-06-18 00:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 57a74c11-8124-33a2-967e-c815300fad15 | -10.9353 | -56.8522 | 2026-06-18 00:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 41.3 |
| 38abebfa-24df-3a9b-86c3-d77ea5aae545 | -10.8976 | -56.855 | 2026-06-18 00:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 40.0 |
| ed69a330-8122-3764-b4ac-51190b89fcf9 | -9.2152 | -47.9241 | 2026-06-18 00:00:00 | GOES-19 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 96.6 |
| 6b9dd484-9271-345f-b98c-24ae97c477ae | -4.3402 | -47.7645 | 2026-06-18 00:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 3b0a8cdd-f003-3e0d-915e-c83174ef008b | -10.9164 | -56.8536 | 2026-06-18 00:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 86.3 |
| e390c168-e111-3d47-b421-78bc850bbdf0 | -12.8354 | -44.3657 | 2026-06-18 00:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 77.7 |
| adceb3a2-3e7e-3c44-b08a-03ce9becd018 | -13.2069 | -50.3275 | 2026-06-18 00:00:00 | GOES-19 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 59.5 |
| 35004046-fff2-3542-bc9d-659cb0a9d3c5 | -7.7176 | -44.1611 | 2026-06-18 00:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 71.4 |
| e72275ef-efcb-3b1d-9e46-b34ef43c1e52 | -13.2066 | -50.3492 | 2026-06-18 00:00:00 | GOES-19 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 6fce934e-120a-38a0-90f4-5368e044381d | -9.4196 | -40.3447 | 2026-06-18 00:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 78.3 |
| 5f86d6ec-fb97-3ca8-8f1b-87454db5ad4d | -14.091 | -59.4569 | 2026-06-18 00:10:00 | GOES-19 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 47.7 |
| 77cd095e-edc7-3e45-b901-d9b8a4bc2b9e | -9.4387 | -40.3419 | 2026-06-18 00:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 88.6 |
| 3c178c10-ed0b-35ff-90aa-15734fb96f36 | -9.2152 | -47.9241 | 2026-06-18 00:10:00 | GOES-19 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 17b69a55-fb7e-326a-bf88-190c64ea387d | -7.7176 | -44.1611 | 2026-06-18 00:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 86.9 |
| c2706291-beb5-38d9-8a13-7d4a6ee65be5 | -4.3402 | -47.7645 | 2026-06-18 00:10:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 3401c2b7-cb4f-3019-8386-ae49fc4828b8 | -12.8354 | -44.3657 | 2026-06-18 00:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 540e7199-f063-3dc3-b876-cddf373eee4f | -10.8976 | -56.855 | 2026-06-18 00:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 46.7 |
| 6ec32286-2031-3933-ac45-57453025f8a6 | -12.7741 | -44.5396 | 2026-06-18 00:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 62.4 |
| aa4d4373-c6cc-3cde-a795-cde6ad882fe6 | -13.2066 | -50.3492 | 2026-06-18 00:10:00 | GOES-19 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 71.9 |
| cf5846ad-da54-330d-9090-62c40d9f56af | -10.9164 | -56.8536 | 2026-06-18 00:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 95.4 |
| ffefd31b-0274-3428-8889-275a6aebec5a | -4.3588 | -47.7636 | 2026-06-18 00:10:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 78.5 |
| 1b052883-6af0-3288-b2cc-f6147b1a51c6 | -4.3588 | -47.7636 | 2026-06-18 00:20:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 78.7 |
| 3ca49108-3f67-381c-9f76-b40d3667d499 | -4.3402 | -47.7645 | 2026-06-18 00:20:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 5f490990-ee48-3525-9c3d-cf4287b5fb17 | -9.2152 | -47.9241 | 2026-06-18 00:20:00 | GOES-19 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 92233060-89ad-34e3-9d32-17a037593c5e | -12.7741 | -44.5396 | 2026-06-18 00:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 55.8 |
| b288e2e0-4632-33d1-aeb5-2c8669db8371 | -9.4387 | -40.3419 | 2026-06-18 00:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 206.5 |
| c08d63d8-1f71-30fb-a385-a398342f3414 | -10.9162 | -56.8736 | 2026-06-18 00:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 34.6 |
| 09934b88-604a-3a77-b554-e84d0b7ab3e3 | -10.9164 | -56.8536 | 2026-06-18 00:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 91.5 |
| a979e3e8-57b9-333d-b2c0-a406da083d8a | -13.2066 | -50.3492 | 2026-06-18 00:20:00 | GOES-19 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 64.5 |
| a09447a0-85ce-39e8-8104-acb3fa48755f | -9.4196 | -40.3447 | 2026-06-18 00:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 92.6 |
| 598c570d-7c0b-36ad-8cff-9b3b030c289c | -7.7176 | -44.1611 | 2026-06-18 00:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 457e32bf-bbfb-372f-bf75-011a2cec3abf | -9.4391 | -40.3171 | 2026-06-18 00:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 93.2 |
| 68d9b790-a323-3365-bba2-e2da91d9bf31 | -12.8354 | -44.3657 | 2026-06-18 00:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 58.7 |
| 53cf8e70-18c8-36d6-b4c9-41f160b60a2a | -10.9164 | -56.8536 | 2026-06-18 00:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 97.7 |
| a6e66061-ab2f-3451-aa98-5f044a432da6 | -12.8548 | -44.3625 | 2026-06-18 00:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 53.8 |
| b7cf8520-0ad5-3e16-8516-6f644f61b0e6 | -7.7364 | -44.1592 | 2026-06-18 00:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 862d88d0-bde4-35ba-9c95-f50abac39037 | -4.3588 | -47.7636 | 2026-06-18 00:30:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 73.9 |
| ceb875cb-3134-3b01-8684-cb0bd3086ea3 | -7.7176 | -44.1611 | 2026-06-18 00:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 83.5 |
| a90c0625-9692-3191-802a-22101883aa18 | -6.7809 | -45.638 | 2026-06-18 00:30:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 59.9 |
| a5c987a0-5f63-39fe-b980-96c50468fceb | -9.2152 | -47.9241 | 2026-06-18 00:30:00 | GOES-19 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 62361928-7231-3ebd-89e6-91dc8e08590f | -12.8354 | -44.3657 | 2026-06-18 00:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 52.5 |
| 21819b48-4e1c-3daa-8497-183af38ece12 | -9.4387 | -40.3419 | 2026-06-18 00:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 93.1 |
| 0f985eb2-e351-3f76-9d56-e453f48718c6 | -9.4391 | -40.3171 | 2026-06-18 00:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 77.8 |
| 8abb8154-fa5f-398a-a74f-284f5034308f | -12.4685 | -55.112598 | 2026-06-18 00:36:00 | METOP-B | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a60c902f-3f7a-30c5-aedd-d13159cef054 | -4.3585 | -47.748402 | 2026-06-18 00:36:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f88636a9-aa3f-36e4-9796-16adb6cc28bf | -12.825 | -44.3386 | 2026-06-18 00:36:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 941eb8d6-3ad9-3fbf-9aac-a70f09d398e4 | -14.0847 | -59.4524 | 2026-06-18 00:36:00 | METOP-B | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c18eff2a-ee92-3725-92cf-45cf2d976673 | -15.6485 | -58.003899 | 2026-06-18 00:36:00 | METOP-B | MIRASSOL D'OESTE | MATO GROSSO | Brasil | 5105622 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e12e4ef2-094e-3368-83d3-25c85c17570e | -14.0925 | -59.4403 | 2026-06-18 00:36:00 | METOP-B | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ac597fed-16c9-351b-997f-73fd288160b0 | -14.0965 | -59.460201 | 2026-06-18 00:36:00 | METOP-B | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 08290ffc-4030-36da-8ce4-a7eeaafda4c5 | -4.3488 | -47.750702 | 2026-06-18 00:36:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7ff0240c-acd9-34ea-8a01-b9116423f0a6 | -11.3577 | -55.813099 | 2026-06-18 00:36:00 | METOP-B | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ea9b15bc-4e48-3445-9ee1-82614869f6cc | -11.8117 | -52.516102 | 2026-06-18 00:36:00 | METOP-B | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8ac9bb59-2567-3157-ac04-5b8a300f9b7c | -13.1927 | -50.331001 | 2026-06-18 00:36:00 | METOP-B | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 08c39f3f-a41c-3ce7-9b04-0b221f3818d5 | -11.8098 | -52.5079 | 2026-06-18 00:36:00 | METOP-B | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 88f07097-469e-3867-8862-629ebb0b298f | -9.7765 | -48.959999 | 2026-06-18 00:36:00 | METOP-B | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 07574d8f-84af-386f-a072-ea971e07de6a | -13.2024 | -50.328499 | 2026-06-18 00:36:00 | METOP-B | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| d4bf2900-5606-3abf-90f4-790c0d011ef6 | -10.6383 | -51.790901 | 2026-06-18 00:36:00 | METOP-B | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8a3921d1-5cb4-3647-adc0-2a42b5bbdf38 | -7.5972 | -46.462399 | 2026-06-18 00:36:00 | METOP-B | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 94d015ca-151d-3bb5-84f1-860a666acc9e | -12.2034 | -52.777699 | 2026-06-18 00:36:00 | METOP-B | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 730bb14d-042b-34b1-94b1-f14d00c6192c | -10.1552 | -56.6115 | 2026-06-18 00:36:00 | METOP-B | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| da5853dd-e681-331b-8f4b-ad7030c9f525 | -12.2113 | -52.767399 | 2026-06-18 00:36:00 | METOP-B | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6a2a9c22-19a7-3766-b234-e950d9cb8e02 | -6.7821 | -45.630501 | 2026-06-18 00:36:00 | METOP-B | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 45d836de-5da2-3507-b46a-0a69f59ed170 | -13.1952 | -50.341202 | 2026-06-18 00:36:00 | METOP-B | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| c92fbec3-1ae2-36ce-a7a1-568620093699 | -9.2108 | -47.929401 | 2026-06-18 00:36:00 | METOP-B | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b78d67c9-4cbd-3dd3-a452-19e87d4b4de1 | -12.4701 | -55.119598 | 2026-06-18 00:36:00 | METOP-B | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4e6d825e-8b13-302d-83b9-85dd15bebb6c | -7.8413 | -55.395901 | 2026-06-18 00:36:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7855fb38-35d8-35f1-8d5d-a9b2f5cb4208 | -9.2204 | -47.926899 | 2026-06-18 00:36:00 | METOP-B | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 73101dc4-41b2-33e4-833d-10ef3cc3cbbe | -10.9835 | -47.719398 | 2026-06-18 00:36:00 | METOP-B | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1794c924-0732-347f-9731-892612bd353d | -12.8346 | -44.335899 | 2026-06-18 00:36:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e23ea939-c102-3ec9-b66b-e872ee0fb23f | -12.2015 | -52.769798 | 2026-06-18 00:36:00 | METOP-B | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fc5c8967-de34-359c-9c94-79423e7382a3 | -10.1536 | -56.6045 | 2026-06-18 00:36:00 | METOP-B | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 19582994-f958-3913-962b-5d25505c859e | -10.9078 | -46.413601 | 2026-06-18 00:36:00 | METOP-B | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 78b5345d-e7ba-3a41-953f-63b8f43645ba | -13.2049 | -50.338699 | 2026-06-18 00:36:00 | METOP-B | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 3c40d499-3a9a-3429-8d77-ba2e67911b17 | -12.7604 | -44.52 | 2026-06-18 00:36:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 45219a60-04e1-3334-8d10-859bbbb7b164 | -12.77 | -44.5173 | 2026-06-18 00:36:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ddaf831d-9308-306d-b00e-989812c53156 | -12.8415 | -44.3615 | 2026-06-18 00:36:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 94c8dc3c-fe9c-3f50-afb7-57e390de8f81 | -12.2132 | -52.775299 | 2026-06-18 00:36:00 | METOP-B | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e6f402c5-bd53-30c7-aff1-70cae2dbeafb | -9.2066 | -47.912601 | 2026-06-18 00:36:00 | METOP-B | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 658e8b6a-ae64-3b6d-abad-907542de3c2f | -10.8981 | -46.4161 | 2026-06-18 00:36:00 | METOP-B | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| dce5d576-bc03-388d-845a-25ce8bb68eaa | -8.9741 | -47.971699 | 2026-06-18 00:36:00 | METOP-B | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6ed7c50a-3e21-35e1-8380-c4f79f7ab646 | -10.9779 | -47.738201 | 2026-06-18 00:36:00 | METOP-B | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b23c35b6-1502-36d0-bb91-ed1fbefe093c | -10.9876 | -47.735699 | 2026-06-18 00:36:00 | METOP-B | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 698080b8-5d2c-3fb4-b467-be892832d26c | -12.8319 | -44.364201 | 2026-06-18 00:36:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 71e6ea4d-06f4-3ff9-903d-17558249e127 | -14.0945 | -59.450298 | 2026-06-18 00:36:00 | METOP-B | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 26680f2c-8c72-3557-972d-4f52f3e8aa81 | -9.2162 | -47.910099 | 2026-06-18 00:36:00 | METOP-B | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 83c6e361-bcdc-3e09-bd2c-9a0947f874f5 | 2.5893 | -60.687199 | 2026-06-18 00:39:00 | METOP-B | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| f343fbb4-197b-33a0-9b1d-ece16bdb26d9 | 2.591 | -60.679901 | 2026-06-18 00:39:00 | METOP-B | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| cc621fa5-7f80-35b5-a801-31d97a69aa6c | -10.9193 | -56.855301 | 2026-06-18 00:39:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f4fd3faa-5f7b-3d54-abd8-e628c7c53a91 | -10.9161 | -56.841099 | 2026-06-18 00:39:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9b069cf4-2b92-3be5-8950-c330564df66c | -10.9177 | -56.848202 | 2026-06-18 00:39:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 303a3810-406b-3eea-b1d7-73e93b29d25f | -12.8354 | -44.3657 | 2026-06-18 00:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 8b898801-2dcd-327c-8a4e-7f9912ebf64d | -10.9164 | -56.8536 | 2026-06-18 00:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 0e885368-5fb0-337f-b010-eaee83937e3a | -4.3588 | -47.7636 | 2026-06-18 00:40:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 55.5 |
| a44ea1ca-a237-3ece-8241-9674f7eb26b4 | -9.4196 | -40.3447 | 2026-06-18 00:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 105.9 |
| 58f4a349-9892-3311-ac1a-e4c457dc04d1 | -4.3402 | -47.7645 | 2026-06-18 00:40:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 46.6 |
| 310682d4-8451-3fda-af85-6d8c5b25298e | -9.2152 | -47.9241 | 2026-06-18 00:40:00 | GOES-19 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 80.9 |


[Clique aqui para ver as próximas entradas](README2.md)
