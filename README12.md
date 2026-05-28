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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a1b8aa91-6a18-3450-9292-7cf80259d3b2 | -11.99361 | -47.15644 | 2026-05-28 05:14:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1ddb131a-4034-3656-bf83-d260638a7a0b | -10.77922 | -46.90551 | 2026-05-28 05:14:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| caeaf3fe-7b5a-3abd-8967-c20acc634396 | -11.47113 | -52.91857 | 2026-05-28 05:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 45d139e0-5eb2-3f04-97b8-67c79d76084b | -10.63276 | -46.90303 | 2026-05-28 05:14:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b4674602-9354-38cb-988b-20dd631d31e3 | -5.10069 | -46.94694 | 2026-05-28 05:14:00 | NPP-375D | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bd2896de-efce-3df4-a2e6-7f3b14b7181e | -10.91315 | -54.12352 | 2026-05-28 05:14:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7e9bcedd-762f-344e-8582-568c9c394261 | -5.80799 | -45.12553 | 2026-05-28 05:14:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6397cbd6-8187-3fd0-9957-e2205ae31efe | -11.58735 | -47.45128 | 2026-05-28 05:14:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 7bd67b80-05ed-34da-90cd-5523d6fece4a | -6.53304 | -55.0636 | 2026-05-28 05:14:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1ff0db48-b1cb-3e46-b2bd-d61675f92f6e | -10.04997 | -51.68398 | 2026-05-28 05:14:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fd9cec9c-ebf5-39f0-b794-adae8a1958cb | -9.34073 | -45.47213 | 2026-05-28 05:14:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 18300181-d263-3346-a0ee-984fdd00a1de | -9.05414 | -46.30259 | 2026-05-28 05:14:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d7f0b83e-7c44-34dd-898c-f2fafc1951ff | -9.39263 | -48.44112 | 2026-05-28 05:14:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 9895a27a-661d-35d5-a150-611a82880851 | -12.68586 | -44.78882 | 2026-05-28 05:14:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e3d399ad-fb7f-3df7-9c53-52e62e575743 | -8.68419 | -48.30254 | 2026-05-28 05:14:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c7ae2e0a-049b-34a3-ba43-95bbe2019fd7 | -9.39766 | -48.44188 | 2026-05-28 05:14:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3560abda-68ae-30fa-abef-2a7f3222f532 | -11.29913 | -54.03207 | 2026-05-28 05:14:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5a4e164f-87f1-35fb-b169-f17f3b4ecf5c | -11.58782 | -47.44756 | 2026-05-28 05:14:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 36d9065b-d107-3ced-ba29-6c99b15ca529 | -10.77828 | -46.91308 | 2026-05-28 05:14:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9c08ddbe-a8d4-3f64-a4c8-6e6725b83127 | -9.35334 | -45.46537 | 2026-05-28 05:14:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c5ac3919-e6ff-33e1-abe2-5321e3c7a8c3 | -6.52969 | -55.06308 | 2026-05-28 05:14:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 09aba063-e676-38cd-b69a-a15605364d66 | -11.59291 | -47.45195 | 2026-05-28 05:14:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 81d9b1bc-b0e4-35b9-90a6-50700ffed37c | -9.361 | -45.4601 | 2026-05-28 05:14:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6eb23569-00a4-3c82-bdfe-9dc53122e4de | -5.7913 | -45.14122 | 2026-05-28 05:14:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b9caa0b0-f17a-3b18-8538-434750c76c12 | -12.69314 | -44.78382 | 2026-05-28 05:14:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a9c97e3f-f1bb-3908-b7ac-c5f15b5e263d | -11.27427 | -53.96973 | 2026-05-28 05:14:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9b60826b-74c6-3cd3-a015-972269990042 | -11.99552 | -47.15892 | 2026-05-28 05:14:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1012152e-c781-326d-b550-93c31baefd0c | -11.59384 | -47.4445 | 2026-05-28 05:14:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a943d2d5-9366-35f8-8c9c-e4bd353dddb2 | -10.4819 | -48.90735 | 2026-05-28 05:14:00 | NPP-375D | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| eee318bf-b667-32d4-a183-8a339ffd0f8f | -7.00045 | -42.88245 | 2026-05-28 05:14:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 299d0cce-da27-386c-826e-9c76ec9be8bb | -5.79847 | -45.13363 | 2026-05-28 05:14:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4e73a2dd-2e42-3072-897f-c32ee33654db | -6.99347 | -42.8817 | 2026-05-28 05:14:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 8a76717c-0108-376f-9281-f9d6f5d73ffb | -10.05456 | -51.68093 | 2026-05-28 05:14:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3e7696e8-9791-34e8-bd3c-b9c54612b4d5 | -12.68917 | -44.78285 | 2026-05-28 05:14:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| acdfc340-0811-35b8-9002-0e36532f4796 | -10.90956 | -54.12297 | 2026-05-28 05:14:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3642c855-dc39-37bd-85d4-86fe74a498ab | -5.80566 | -45.12595 | 2026-05-28 05:14:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f2e33c49-dad5-3db4-b09d-9c351d09f1e1 | -10.13843 | -52.40149 | 2026-05-28 05:14:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3335cb90-2975-3c52-955b-31185235e428 | -10.47795 | -48.90743 | 2026-05-28 05:14:00 | NPP-375D | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 38f3b0df-ad9c-3967-a07d-e3a05bc52cc2 | -7.00132 | -42.87589 | 2026-05-28 05:14:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 3a35c686-a930-3f5f-9d43-3c5577922fd1 | -11.9706 | -47.38295 | 2026-05-28 05:14:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 14b8fb31-5035-3f96-ac80-e3e636df96fb | -11.97108 | -47.37921 | 2026-05-28 05:14:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| de376707-9c48-3003-906c-a0788f4a3ace | -10.63936 | -46.89624 | 2026-05-28 05:14:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2af2f54c-2654-3182-aeee-7eeea487a877 | -10.65685 | -49.72824 | 2026-05-28 05:14:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b8830353-53da-34d1-b824-3342071ec7da | -9.74025 | -49.21244 | 2026-05-28 05:14:00 | NPP-375D | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 42bbb476-4b8c-393d-b77d-eda4cbbed408 | -10.4829 | -48.90817 | 2026-05-28 05:14:00 | NPP-375D | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| ce8f9285-aaca-3cdc-b289-11ab0ca0e6c9 | -15.82574 | -58.61752 | 2026-05-28 05:16:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Pantanal | 0.5 |
| 3f867991-620a-3f0a-8b69-48f6a53403d2 | -13.2077 | -54.50154 | 2026-05-28 05:16:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a37b08a4-c25a-3d86-b977-8b5d549f6b69 | -12.90473 | -51.87543 | 2026-05-28 05:16:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4665ee9c-0f77-3442-a8ab-bd80a1504e6e | -11.72015 | -56.84486 | 2026-05-28 05:16:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| df9e7e75-92bd-37a1-9682-dffaa5f9ca13 | -13.21977 | -54.49473 | 2026-05-28 05:16:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5446d2f1-b2c6-352a-bfd9-acef018fa446 | -11.73126 | -56.8394 | 2026-05-28 05:16:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7a8927e5-9205-3243-b313-aa5b11a881cc | -17.95615 | -54.46143 | 2026-05-28 05:16:00 | NPP-375D | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b486e8d8-e3d3-3933-9469-8c302d9a82fa | -11.73181 | -56.83586 | 2026-05-28 05:16:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f4e6a8b4-0669-3f30-bafb-9fd7d3d40198 | -16.21677 | -59.66918 | 2026-05-28 05:16:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e05c74fa-b127-3edb-829a-63d1fe56e1d1 | -13.19926 | -54.50887 | 2026-05-28 05:16:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2b954221-8387-3414-9e7e-186cafde5dc5 | -13.22213 | -54.50372 | 2026-05-28 05:16:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fde1f7a7-93a2-342d-ac59-25bb62bdf4d9 | -11.72404 | -56.84185 | 2026-05-28 05:16:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8b66022d-b451-347b-a32a-cfd135609afe | -11.63559 | -56.86698 | 2026-05-28 05:16:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d489c6fd-be63-3312-b14f-0ec6e2574f72 | -13.95357 | -53.86507 | 2026-05-28 05:16:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 57806821-a5f5-373e-9144-6665ce65eeae | -13.21667 | -54.51579 | 2026-05-28 05:16:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| da735111-e798-33b7-9a0e-8938c97589ef | -13.22276 | -54.4995 | 2026-05-28 05:16:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a693ffbf-0648-31be-ad60-d30561d578d8 | -11.79007 | -57.0084 | 2026-05-28 05:16:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6930c863-109d-3735-9aef-99ac68d3f1e9 | -11.63281 | -56.86291 | 2026-05-28 05:16:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| c73c97fc-619a-3534-ae57-e467c8e6186a | -15.42022 | -56.31124 | 2026-05-28 05:16:00 | NPP-375D | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8ce6b41d-6374-30f9-ba45-6a87bcd5a0fc | -16.2661 | -60.00706 | 2026-05-28 05:16:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 37095a2e-3aae-36dc-a3be-3bae881e0e43 | -13.20709 | -54.50578 | 2026-05-28 05:16:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4b75bf8a-9fca-35ca-ad2b-abeb6d5ec750 | -11.93286 | -57.04196 | 2026-05-28 05:16:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 844c2fb3-777a-351f-95b2-b1900c569e58 | -13.20348 | -54.50522 | 2026-05-28 05:16:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a0012758-47ae-32b8-a9c6-a304d3469523 | -17.93686 | -51.33329 | 2026-05-28 05:16:00 | NPP-375D | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cf3177fe-310d-35f0-a164-6261341b01d5 | -13.20225 | -54.51363 | 2026-05-28 05:16:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6f589012-5666-3776-92d5-c8d8d5c33086 | -13.21852 | -54.50319 | 2026-05-28 05:16:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e8e963f2-8001-3436-b0c4-37b9de72b9eb | -13.20524 | -54.51838 | 2026-05-28 05:16:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a466b5a1-4a4c-31b4-a4cd-7c8cd8f3feab | -13.21915 | -54.49896 | 2026-05-28 05:16:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 14a9c734-ea04-32f4-9cf1-7a16f3bf565e | -13.18419 | -52.70457 | 2026-05-28 05:16:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7c2dd33d-ce7d-3f34-842b-df6a57d8078b | -11.63615 | -56.86345 | 2026-05-28 05:16:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d6050f16-f178-384e-ade0-bff1c6413ec1 | -13.22575 | -54.50425 | 2026-05-28 05:16:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a2423cae-7570-3064-a0d3-9e636ce3240d | -13.2209 | -54.51213 | 2026-05-28 05:16:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 593bc1f0-882e-3b88-8e53-75c64038cd17 | -17.95233 | -54.46082 | 2026-05-28 05:16:00 | NPP-375D | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ecb8c460-8ca6-33b3-8595-0eca39d75e30 | -11.7207 | -56.84132 | 2026-05-28 05:16:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 68bcca8e-f729-33ea-902b-478391e958d9 | -12.725 | -54.19294 | 2026-05-28 05:16:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| db18dfd6-7249-3388-97a0-c73566d204bc | -13.2041 | -54.501 | 2026-05-28 05:16:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b987210f-b662-3f93-bd60-6667d8e6b463 | -11.63948 | -56.86399 | 2026-05-28 05:16:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b0e19a22-f4f6-39f1-8e0c-dc17e5d90901 | -13.2143 | -54.50686 | 2026-05-28 05:16:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a2126185-9ebc-318e-ab8c-b9325755184c | -16.16278 | -58.4739 | 2026-05-28 05:16:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| e5e65f80-b300-30d2-bf1b-3a931e5e4e82 | -11.8024 | -57.3541 | 2026-05-28 05:16:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ce2d9048-5289-347d-8bef-e39392917c63 | -11.79907 | -57.35356 | 2026-05-28 05:16:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b2eda259-1ce0-33e4-adb8-852a9d8731bc | -16.26889 | -60.01147 | 2026-05-28 05:16:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a8dcc382-32b8-3d3c-a4ef-0e12cc4a523e | -13.19987 | -54.50467 | 2026-05-28 05:16:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6347dbe5-088f-3048-8ac1-5f114bab9636 | -12.54882 | -54.58346 | 2026-05-28 05:16:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f7c9b954-b9b9-30be-95a6-cff0918d4ced | -15.42365 | -56.31179 | 2026-05-28 05:16:00 | NPP-375D | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a8eac020-cb36-37aa-8662-8356d002684e | -16.22077 | -59.66604 | 2026-05-28 05:16:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bd3495c5-35c4-3eb7-a2e8-71ad65afe7cd | -13.22637 | -54.50003 | 2026-05-28 05:16:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0cea9a00-ff43-38cd-937d-251fabe853e0 | -11.79774 | -57.0166 | 2026-05-28 05:16:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 54f811d1-66b6-3cc0-b968-4ca94ada28ce | -16.218 | -59.66171 | 2026-05-28 05:16:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6a36219d-9054-391a-a77c-5cbfe3748925 | -13.20647 | -54.50998 | 2026-05-28 05:16:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 71e2bbe3-3f46-32eb-b4c7-8835e6eeb08d | -13.21791 | -54.5074 | 2026-05-28 05:16:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9ee27f82-4b19-3426-889c-6f448e756f84 | -11.6367 | -56.85991 | 2026-05-28 05:16:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4d7dd78c-3bbb-3109-aa42-148aea34c09b | -13.19864 | -54.51307 | 2026-05-28 05:16:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| daa79b94-d328-3632-8550-fcbd3011c80c | -13.21606 | -54.51997 | 2026-05-28 05:16:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 34578904-a508-3355-9e51-c99d280de25f | -16.15888 | -58.47688 | 2026-05-28 05:16:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |


[Clique aqui para ver as próximas entradas](README13.md)
