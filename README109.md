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

## Dados Diários - Página 109

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f84c13ff-a156-3b31-be7c-c564f150a90d | -9.82327 | -51.92357 | 2024-10-04 04:32:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| b7bd440c-f09d-3547-aa88-37b772a7bc29 | -9.82034 | -51.91859 | 2024-10-04 04:32:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f5d2781b-188e-374e-ae4c-cc5e5df60285 | -9.81962 | -51.9229 | 2024-10-04 04:32:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 05e76188-b85d-30bd-98dd-0b2b4be779aa | -9.81596 | -51.92227 | 2024-10-04 04:32:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6bc78cbd-a186-31ed-bf0f-0ae41d328bfb | -9.81123 | -51.81734 | 2024-10-04 04:32:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ba24d861-7716-31b3-9bd6-2ed098cd6edc | -9.80899 | -51.80818 | 2024-10-04 04:32:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c54539c4-08c8-3639-a39d-0d1469096949 | -9.80858 | -51.81084 | 2024-10-04 04:32:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7c2f008f-5fa2-3e86-9d80-c46cf164e4b5 | -9.8083 | -51.81241 | 2024-10-04 04:32:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b90ee1ef-e453-3c9f-8cd5-5226ebf19656 | -9.80786 | -51.81509 | 2024-10-04 04:32:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d6074ca9-c8de-3451-89e1-edee1c9f0820 | -9.80759 | -51.81668 | 2024-10-04 04:32:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1dcd3b52-6ccf-39a2-9544-1241fb8a2e46 | -9.80713 | -51.81936 | 2024-10-04 04:32:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2d2898e4-0066-3149-8419-1610e9e72b89 | -9.77831 | -51.9262 | 2024-10-04 04:32:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f88db3db-71b2-37b0-8769-e7861cc2a9c9 | -9.77678 | -51.91266 | 2024-10-04 04:32:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1fe05bc0-e40c-37f4-8c93-591abf2cd5a6 | -9.77535 | -51.92128 | 2024-10-04 04:32:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c8e2ae49-fd5b-3977-93f4-92d071a37096 | -9.77463 | -51.92563 | 2024-10-04 04:32:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3efa98de-ebd7-333c-bc1e-dd35186ec198 | -9.77321 | -51.93425 | 2024-10-04 04:32:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ec093500-14a3-3777-812b-ec2b44f09fb6 | -9.77313 | -51.91199 | 2024-10-04 04:32:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2a2bf36b-d29a-3503-ad20-5585a1125963 | -9.77249 | -51.93859 | 2024-10-04 04:32:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ec15eccb-9ed8-357f-bb87-680e6210ce76 | -9.77168 | -51.92076 | 2024-10-04 04:32:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| af096666-5780-3eac-a25f-517f1547284a | -9.77096 | -51.92509 | 2024-10-04 04:32:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 89e94b02-e9bb-35d5-8744-fe03aac13de0 | -9.76947 | -51.91137 | 2024-10-04 04:32:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2c633009-c797-3c58-b809-240bced67930 | -9.76883 | -51.93793 | 2024-10-04 04:32:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d6215ac0-bd29-3141-8430-b013b47bae83 | -9.76518 | -51.93725 | 2024-10-04 04:32:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0ffa6321-c8de-3def-9567-b5ee30f3aff0 | -9.76507 | -51.91522 | 2024-10-04 04:32:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1087064c-fd70-3dfd-988e-bc2572b0d7fe | -9.76221 | -51.93248 | 2024-10-04 04:32:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fe08879d-851a-347b-a7f4-3b87ec7a0f41 | -9.76152 | -51.93662 | 2024-10-04 04:32:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ffc7b6b4-e43f-31aa-aabc-327ef2d76e65 | -9.7614 | -51.91465 | 2024-10-04 04:32:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7e0925c6-b38b-3df8-8966-58e5d5c6921b | -9.68357 | -51.37704 | 2024-10-04 04:32:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a70b6809-f487-3c8e-b1f3-4d6b9823637f | -9.68288 | -51.38113 | 2024-10-04 04:32:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fb9a5c2e-2162-34f2-ab00-e8eb35772cd0 | -9.68124 | -51.34723 | 2024-10-04 04:32:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0a35c491-8899-31fe-a9da-5e729d4319ba | -9.67768 | -51.3466 | 2024-10-04 04:32:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 58cbd5bb-78ef-3da4-bba5-7ca231158ae6 | -9.60646 | -51.4531 | 2024-10-04 04:32:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c37f432c-82ef-3191-95fd-e79f5abd5021 | -9.60288 | -51.45244 | 2024-10-04 04:32:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 190ce5fd-d429-36b3-a30a-e4cdf3b2066b | -9.59722 | -51.4644 | 2024-10-04 04:32:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 7a6d1c62-26db-39dc-a5c3-1e669020f8cd | -9.59363 | -51.46381 | 2024-10-04 04:32:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| a3184d9e-604a-3f69-995c-12f5d9d70386 | -10.47427 | -50.83215 | 2024-10-04 04:32:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ffb48a36-50e7-30d9-861d-0ca25c4d2e6f | -10.46164 | -50.73596 | 2024-10-04 04:32:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 779f94ec-819d-385e-a9a0-e00c635584b6 | -10.45882 | -50.73158 | 2024-10-04 04:32:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| da287e9d-d00f-31ba-a9de-7cf1babf012f | -10.4582 | -50.73536 | 2024-10-04 04:32:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c9d6e5f6-63f5-3b2f-a29e-8a740f4fd3df | -10.45757 | -50.73914 | 2024-10-04 04:32:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0773e30c-3483-3835-9446-56751d261c4a | -10.45695 | -50.74294 | 2024-10-04 04:32:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5d9fab99-b535-315d-92bd-93d1ebaf3eb9 | -10.45537 | -50.73099 | 2024-10-04 04:32:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 36e82e97-c4a9-3009-8e72-36910218fab9 | -10.45475 | -50.73476 | 2024-10-04 04:32:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c5a104d6-217e-3b4c-b1f4-70f621708134 | -10.45413 | -50.73854 | 2024-10-04 04:32:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e843b9ce-c542-310e-8dd4-22c70af427b1 | -10.45192 | -50.73042 | 2024-10-04 04:32:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 10adfee9-a406-3408-8e16-7786dd061762 | -10.4513 | -50.7342 | 2024-10-04 04:32:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f67952ae-90cf-381b-a606-d6dc752725c1 | -10.45067 | -50.73798 | 2024-10-04 04:32:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ca756d9e-c73c-3953-a9d7-c23859a40bd1 | -10.45005 | -50.74179 | 2024-10-04 04:32:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 061fd5c2-190c-3a5e-8e8f-aa4512e76d00 | -10.44847 | -50.72987 | 2024-10-04 04:32:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 654fca1f-e1b5-3bc0-bba3-d0379f1d31ae | -10.44784 | -50.73365 | 2024-10-04 04:32:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| db6e3a42-54bf-30f5-989b-4c763b9968f3 | -10.44722 | -50.73745 | 2024-10-04 04:32:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8e7f46aa-6871-39c8-8a6b-a3e55be6a325 | -10.44659 | -50.74124 | 2024-10-04 04:32:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 910271ac-2563-3be3-bb5a-31959c810798 | -10.44596 | -50.74504 | 2024-10-04 04:32:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f80005f9-8a01-39d3-888f-fc7e80ad4469 | -10.44534 | -50.74883 | 2024-10-04 04:32:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8cdd96b0-7bc5-33f3-883d-367f9344243b | -10.44532 | -50.79198 | 2024-10-04 04:32:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3ae63f36-1f61-343d-832c-29ed66d6498d | -10.44502 | -50.77226 | 2024-10-04 04:32:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a34a9918-8f1e-365c-9dbf-98324dbb0216 | -10.44501 | -50.72931 | 2024-10-04 04:32:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b5b2e22d-5c9f-3c3a-9834-498ceb4343bf | -10.44472 | -50.75262 | 2024-10-04 04:32:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2b7e3161-6ac8-363e-aefd-add70f28dcdc | -10.44439 | -50.77609 | 2024-10-04 04:32:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ddfce86b-253d-398e-ae53-2d508739de3f | -10.44439 | -50.7331 | 2024-10-04 04:32:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8bc8d936-c8cc-34f0-adaa-67c185ad1754 | -10.44409 | -50.75642 | 2024-10-04 04:32:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bb2520cc-320c-3092-b229-f4065d3b561b | -10.44376 | -50.77993 | 2024-10-04 04:32:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 04e15043-5e49-3205-9f34-ed63bb74bcba | -10.44376 | -50.73689 | 2024-10-04 04:32:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| cc057fc6-a494-3c66-839f-8a14a9bd6cdb | -10.44346 | -50.76023 | 2024-10-04 04:32:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a1bed7ab-41cb-3837-8bb8-117a68516d73 | -10.44314 | -50.74068 | 2024-10-04 04:32:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 44cfd25b-2d69-36f5-8245-5b27ead0ea1c | -10.44283 | -50.76405 | 2024-10-04 04:32:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3bb07b5b-466d-35a5-ad49-dbf62c8e2c77 | -10.44251 | -50.74447 | 2024-10-04 04:32:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5dfaca75-0d6e-3d8e-9aa9-19630069341d | -10.4425 | -50.78759 | 2024-10-04 04:32:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 84ec1418-8d83-35bb-8dca-b04ec4f0b746 | -10.4422 | -50.76787 | 2024-10-04 04:32:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8b7d0f52-2ff2-348f-a246-de92e34f8cfa | -10.44189 | -50.74827 | 2024-10-04 04:32:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 12360da6-e0aa-3dad-9cbc-5c08e5a1fd57 | -10.44157 | -50.7717 | 2024-10-04 04:32:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b992af5e-644e-3d52-8e57-ee44185b34ac | -10.44094 | -50.77553 | 2024-10-04 04:32:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7fb2e02c-3f53-394b-a993-02f9a21ad231 | -10.44094 | -50.73254 | 2024-10-04 04:32:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 8e0778e9-2b55-3c57-acc4-6c591ea1bf28 | -10.44031 | -50.73633 | 2024-10-04 04:32:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 3e1f6787-0899-34f6-9e01-3eddd06f9e38 | -10.44029 | -50.8225 | 2024-10-04 04:32:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f49f2571-41e1-384b-b5be-3f0219edb61a | -10.43968 | -50.74012 | 2024-10-04 04:32:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 331355b5-9bc6-3a6a-b873-691be726e8ae | -10.43841 | -50.79084 | 2024-10-04 04:32:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 33ec8dd9-b08c-3532-984f-74b1fbd93fcd | -10.43495 | -50.79026 | 2024-10-04 04:32:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a951f7c4-cec9-309e-bac5-73e0405fe78d | -10.434 | -50.81753 | 2024-10-04 04:32:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e6d903de-fbd9-3425-84c2-6593b15946b9 | -10.4315 | -50.78968 | 2024-10-04 04:32:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2a088ffe-a76a-3a88-9e21-2d4745f81359 | -10.43117 | -50.81313 | 2024-10-04 04:32:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 126cdea0-19c5-31d2-b216-b29c1af80094 | -10.43087 | -50.79348 | 2024-10-04 04:32:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 424fb4e7-b5bb-3b6d-9c6c-2b5fe02fc0eb | -10.43024 | -50.79726 | 2024-10-04 04:32:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 23453a78-3e9f-3b46-be3a-24fca48fb75d | -10.42962 | -50.80101 | 2024-10-04 04:32:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| cd4a0d47-1920-3ca9-badb-c1f5e52b64c7 | -10.42836 | -50.80867 | 2024-10-04 04:32:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 15cf58e8-cf82-33d5-bb37-9f32cabd1451 | -10.42771 | -50.81255 | 2024-10-04 04:32:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 92b5115f-6393-32fb-a799-1f663803f7ed | -10.42741 | -50.7929 | 2024-10-04 04:32:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f48b3aee-e837-3cee-9d0f-e66498ae8d7a | -10.42708 | -50.81638 | 2024-10-04 04:32:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d0ee008a-b680-3bc6-af3f-4f91a627e49b | -10.42678 | -50.79668 | 2024-10-04 04:32:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2b8304a6-157c-3bbf-97fd-ce9aaea98057 | -10.42616 | -50.80044 | 2024-10-04 04:32:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 06c183b1-5489-38e7-80db-4fae126edc65 | -10.42554 | -50.8042 | 2024-10-04 04:32:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ce812a9a-8722-3084-84e4-876b4cc5024e | -10.4249 | -50.80809 | 2024-10-04 04:32:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2d4336fd-8efe-32a3-885b-f5e6fc542e3d | -10.42425 | -50.81197 | 2024-10-04 04:32:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bb137734-c029-3872-b0fa-0da62b1fda7b | -10.4227 | -50.79988 | 2024-10-04 04:32:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| efc06da8-22f0-3839-bbf0-2c74f1722612 | -10.42208 | -50.80365 | 2024-10-04 04:32:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 21c8d695-84ba-3a00-84b5-4404e9cd4e4e | -10.42144 | -50.80751 | 2024-10-04 04:32:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 2c9eaa9d-2f31-32e4-9a98-03579b1a5b96 | -10.42079 | -50.8114 | 2024-10-04 04:32:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| dd9b3391-5b47-3b5c-90a9-dfb799c49398 | -10.63783 | -51.11231 | 2024-10-04 04:32:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c20bbce5-fe5b-3325-9d2b-5bd5f463f796 | -10.63718 | -51.11621 | 2024-10-04 04:32:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| abdc859f-a29d-3a24-a8ac-70515deff2fb | -10.57593 | -51.09071 | 2024-10-04 04:32:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README110.md)
