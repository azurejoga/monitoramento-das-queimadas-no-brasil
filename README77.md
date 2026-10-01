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

## Dados Diários - Página 77

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ac0cc417-91d3-34bf-9408-eb36c1e23895 | -12.18599 | -47.38917 | 2026-10-01 05:18:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| def6744b-4142-3cf4-b747-711d6a49532b | -6.06822 | -57.60668 | 2026-10-01 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| de0e6248-222a-3528-ab55-de0a38f776bb | -6.33241 | -51.1247 | 2026-10-01 05:18:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a58f62e5-eb78-34d8-a8fa-02d4fa390223 | -10.52768 | -55.01126 | 2026-10-01 05:18:00 | NOAA-21 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b3fcabee-bfd6-3caa-b65a-8dac3541f7c4 | -7.49104 | -55.00079 | 2026-10-01 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| ddad05c4-3e77-3d4e-9996-2bc9e5405bb6 | -10.77669 | -54.75205 | 2026-10-01 05:18:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 64135407-a330-380b-8e73-4c0dda986836 | -8.00081 | -61.36459 | 2026-10-01 05:18:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 12d8bb4f-1b55-386a-bc1d-12f2b2ee019f | -11.4084 | -51.02365 | 2026-10-01 05:18:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 0fd2ca84-4371-3c4c-a920-0ce6dcdd96d0 | -7.55 | -55.02978 | 2026-10-01 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5b7aed16-5322-3560-a34d-2f05390c1207 | -7.55316 | -55.03517 | 2026-10-01 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3c11d218-bbf3-3298-8663-41e0cea65d70 | -12.1792 | -47.38833 | 2026-10-01 05:18:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 11d396ca-4fd8-3ae0-8390-36472f7ab5cd | -10.52966 | -57.78275 | 2026-10-01 05:18:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 46d46241-c7c1-3e30-a624-42699bc2fdf3 | -5.99974 | -53.66492 | 2026-10-01 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 712497db-4184-3db8-bf27-0733409a510e | -6.73447 | -45.53898 | 2026-10-01 05:18:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 73965b75-1f9f-3817-a3d2-e136ee466e5f | -11.32515 | -50.96621 | 2026-10-01 05:18:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 9.3 |
| e24927a7-9724-3500-b777-27d26dac4959 | -10.52501 | -55.01073 | 2026-10-01 05:18:00 | NOAA-21 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d8b4633f-9480-304e-90be-a5217dbc2669 | -11.79557 | -50.5172 | 2026-10-01 05:18:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7ef0bdc3-3dcf-3509-b4d0-2888a8477bf3 | -10.7754 | -54.75459 | 2026-10-01 05:18:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c943e2d8-725d-32ff-8320-42268931fcff | -6.69934 | -55.05185 | 2026-10-01 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 3cd3d441-25b7-302b-b286-da07ed5970f3 | -7.49651 | -55.00492 | 2026-10-01 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 87b78766-604c-3a79-bbd0-34e37b7367dd | -6.64787 | -52.59961 | 2026-10-01 05:18:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 77a48d58-cabd-3c97-bb51-25f65fb015af | -6.65719 | -58.88054 | 2026-10-01 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 03a0cbb9-cab7-316d-8bab-a62f2ee9ffc1 | -8.3049 | -54.71188 | 2026-10-01 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 70563ae9-daa8-3935-a34c-1dff9f8aaea3 | -6.13383 | -53.27316 | 2026-10-01 05:18:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d1cc68e0-0d06-352b-b92b-92adc5ac20dd | -7.73528 | -54.80357 | 2026-10-01 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 65e2fadc-c423-3900-b7ad-12ae7c2fb738 | -6.76241 | -48.67934 | 2026-10-01 05:18:00 | NOAA-21 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a7c72f34-cc1a-30b4-b8fa-5bc911ce1154 | -9.58487 | -54.62458 | 2026-10-01 05:18:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 743f20fe-7fb5-34aa-ad03-88a3e361027e | -8.86226 | -50.52692 | 2026-10-01 05:18:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1c6ba4e8-02de-3531-9450-44dc23e991d2 | -11.34123 | -50.96838 | 2026-10-01 05:18:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 561e54fa-e1d8-3e1c-a908-6e4602a7a3c1 | -5.12274 | -56.00599 | 2026-10-01 05:18:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 682b0665-0d5e-3260-ac8f-52985c480bf1 | -9.8883 | -65.14487 | 2026-10-01 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7cea737f-99b9-3026-99eb-54e777793f0f | -11.83917 | -50.9484 | 2026-10-01 05:18:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0eb3db89-32a1-3b02-aa64-7daf5eeffe77 | -11.26151 | -54.81833 | 2026-10-01 05:18:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8eba78ab-46f9-3da7-af83-070d3032b922 | -8.31387 | -54.76345 | 2026-10-01 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d880a7fc-5245-362e-91c6-73ac49f31c07 | -10.77489 | -54.75838 | 2026-10-01 05:18:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 30591e73-b04f-3330-bb45-dd191fa37c63 | -11.79091 | -50.50895 | 2026-10-01 05:18:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 656ee4e5-7dbc-3c1a-ac28-5ab0b82825cc | -8.19448 | -54.73672 | 2026-10-01 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 92893743-bba2-3ecb-b3fd-2f4384ae8afc | -10.28588 | -53.96769 | 2026-10-01 05:18:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 40caea06-cd9d-3140-bcc4-05456262c1e4 | -7.49407 | -54.99478 | 2026-10-01 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f425973b-1542-3e1b-9236-5cd1143642db | -7.50131 | -55.02558 | 2026-10-01 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| a16e8b17-3fc7-3c46-9885-a1996ca63e35 | -6.74892 | -55.08072 | 2026-10-01 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f545a9c9-a5b4-3f95-8249-223dae0326b8 | -5.11858 | -56.00944 | 2026-10-01 05:18:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 087bf618-8baf-3a4a-8988-c23430dacc00 | -7.60583 | -55.69929 | 2026-10-01 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 710aaaa7-a37b-3765-9929-7e5d51ea55fc | -6.43329 | -55.80724 | 2026-10-01 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 401c2ba2-f6e0-3b49-8448-bf93b86ee602 | -10.24612 | -59.02776 | 2026-10-01 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 83dd6b61-c58b-3413-9435-096967bfa274 | -6.92448 | -59.28329 | 2026-10-01 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 703e15c6-f53b-3c4c-b68f-2d6595386d6d | -12.19335 | -48.4409 | 2026-10-01 05:18:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 4d40ad90-9f5f-3454-8003-ff3b4926982d | -7.71844 | -54.75328 | 2026-10-01 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f0b755a2-f4c8-37af-9591-f00892efdff5 | -11.37623 | -55.12776 | 2026-10-01 05:18:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b3584751-fbc4-3085-a205-90605b09d0ba | -7.85631 | -45.82644 | 2026-10-01 05:18:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f2a8fde5-171e-336a-af55-9013201cd123 | -5.80971 | -57.73979 | 2026-10-01 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eed0f47c-ee8b-30cb-a42e-d218213a6063 | -10.53427 | -57.77559 | 2026-10-01 05:18:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 45c222fb-7df0-352a-a1f7-35877ba9b07e | -5.11798 | -56.01341 | 2026-10-01 05:18:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a55f7938-21df-32c3-93a3-bf98b580d00e | -8.48518 | -54.91173 | 2026-10-01 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a8d5b633-fb46-3471-9ba7-15469eed2a74 | -6.07752 | -53.30503 | 2026-10-01 05:18:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 93ddbb15-81b4-382c-85d1-d5af5f4fd4ae | -6.14391 | -53.05987 | 2026-10-01 05:18:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 533a563f-1042-3a8e-9e6d-fa609cc92c9f | -6.07496 | -57.60769 | 2026-10-01 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 70761646-405b-337b-a982-7898003c295c | -11.79002 | -50.51646 | 2026-10-01 05:18:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 85592466-c869-34c0-acb8-b6a53a801f4d | -5.29949 | -56.00927 | 2026-10-01 05:18:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e2779449-38cf-3eca-a12e-07619e5203a4 | -6.08175 | -53.30568 | 2026-10-01 05:18:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cc1cd096-9f8c-3f8c-b135-cc555b430dc9 | -10.82917 | -57.20314 | 2026-10-01 05:18:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b790f05d-25eb-3b7a-b881-f2dc70d94c9b | -6.6863 | -58.86736 | 2026-10-01 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 707e7954-4e51-3acf-9427-48a2a3fe4d93 | -11.7241 | -50.41232 | 2026-10-01 05:18:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 087667ed-e338-3057-9cd0-18f67bd7e955 | -6.66433 | -58.8781 | 2026-10-01 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 25.4 |
| adcd9644-0a5f-3cad-a758-015129372d1a | -5.27465 | -55.96132 | 2026-10-01 05:18:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9e78f0b1-86dc-3647-88cf-7712b79f9272 | -6.73189 | -45.53556 | 2026-10-01 05:18:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8d47f363-8cfb-32e2-bdbf-aa33982e013e | -6.36883 | -55.13781 | 2026-10-01 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d299a03d-6b7d-3e36-9dce-4dea4d1b620e | -7.32336 | -55.23061 | 2026-10-01 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5fee174b-bd64-3f2b-aa05-be9a6c4fda0f | -10.30185 | -59.4597 | 2026-10-01 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9e5652e4-d090-38dc-8706-bd281b8c7b62 | -7.4956 | -54.99642 | 2026-10-01 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 646e02d4-4f9d-3f8e-84b7-9b40f65a4f82 | -9.34217 | -57.17581 | 2026-10-01 05:18:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 439654f1-703a-3067-a2ab-31e2af8d2552 | -10.84708 | -48.70683 | 2026-10-01 05:18:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d476f599-ceb4-31a2-9092-0dc6f26f9ad1 | -5.12093 | -56.0179 | 2026-10-01 05:18:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3187b03a-b4ef-3d4b-9188-e059294fb29b | -5.12569 | -56.01045 | 2026-10-01 05:18:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 2874806a-c268-3d4b-88f5-56f597a9ba60 | -6.5158 | -55.88347 | 2026-10-01 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7cb7e5a2-9e2c-3369-aacd-48161c7303a0 | -6.08502 | -56.47157 | 2026-10-01 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 049ea596-a204-33e2-a9db-8d81b77b642c | -9.21693 | -50.68699 | 2026-10-01 05:18:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3fddd4b3-9ebb-3990-911a-3c4239c97102 | -11.28021 | -50.97741 | 2026-10-01 05:18:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9155c8f7-61e4-33cc-a77b-2b3c5e9c292a | -8.7984 | -48.00639 | 2026-10-01 05:18:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1e4a5a78-397e-315d-9526-ed32e0607888 | -6.76314 | -48.6802 | 2026-10-01 05:18:00 | NOAA-21 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 057dff77-2398-3c96-82da-17fb5a7114e6 | -9.35039 | -57.16896 | 2026-10-01 05:18:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8202abe3-5ea1-37b9-acef-5b2dd67b2ef0 | -7.49242 | -54.99104 | 2026-10-01 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2373d5c5-f3b5-32f6-b1c9-87e51eb2eeda | -8.84527 | -49.69283 | 2026-10-01 05:18:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| a72498ac-767f-3192-bb75-7e7110cbea7a | -9.58382 | -54.6319 | 2026-10-01 05:18:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2b951c39-8c68-3a11-b5cc-7177622cff5c | -9.06474 | -49.86454 | 2026-10-01 05:18:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cb8a135e-e382-3ee4-bc5e-647cf7f4c626 | -7.56683 | -55.02255 | 2026-10-01 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d5e2a82e-1c2d-38c7-91ab-28f300180c41 | -10.52908 | -57.78659 | 2026-10-01 05:18:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bc7e6063-ef11-3365-bed6-79bc555a4e1e | -8.16019 | -54.805 | 2026-10-01 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| af888d9b-bfe2-3a6f-8437-7bbc9d36989d | -11.28196 | -50.97881 | 2026-10-01 05:18:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 53067c2d-7af0-3e14-b1fb-ef31e5a9e1be | -6.0151 | -49.56071 | 2026-10-01 05:18:00 | NOAA-21 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 41b7ed65-fb7f-3007-9a6d-a516b8b5a6a0 | -9.70403 | -58.12275 | 2026-10-01 05:18:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0ad0927d-9b1c-3154-abdd-92d3cf01a907 | -8.19324 | -54.73772 | 2026-10-01 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 001fc388-42c8-3792-8270-c8c96cbd632e | -10.84074 | -48.70755 | 2026-10-01 05:18:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9b687d39-5726-3099-baf6-538e77e86792 | -6.05786 | -59.92697 | 2026-10-01 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 87baebf1-74f2-3e2a-a769-ad419145dc0a | -6.72686 | -52.95703 | 2026-10-01 05:18:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 56d45573-e881-3b95-b71b-17681672275e | -11.40882 | -51.02024 | 2026-10-01 05:18:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| abdca65c-404d-3b5f-a358-a759dc58707d | -7.59677 | -55.07352 | 2026-10-01 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| cb07da48-c064-3019-8edb-067375212b5e | -11.16754 | -54.11821 | 2026-10-01 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| eba66935-fbaf-3902-848f-37dcc89fac25 | -11.41751 | -50.99375 | 2026-10-01 05:18:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fb46d44a-d4a7-39b7-8f9c-cf9d54329c01 | -7.70006 | -54.79677 | 2026-10-01 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README78.md)
