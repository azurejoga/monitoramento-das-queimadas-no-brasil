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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 54ae9f84-0646-3ca6-8c40-b143cc1f2836 | -11.30087 | -54.72079 | 2026-06-23 05:27:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9a8ac7fb-5548-3cc3-8b4c-7eb705a2fdb5 | -12.65373 | -47.6851 | 2026-06-23 05:27:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c3234c9a-cdd6-30a0-9aec-84a80351d7e5 | -10.56992 | -57.32145 | 2026-06-23 05:27:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4fbb25da-d284-3864-99d4-1afb400f1463 | -10.23478 | -54.26618 | 2026-06-23 05:27:00 | NPP-375D | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 4141abe2-cb6f-327d-91d8-04e5d16aa21c | -12.50692 | -48.27531 | 2026-06-23 05:27:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b4e2fd2a-35a8-3174-9c9f-14e51c41b815 | -10.94096 | -56.8485 | 2026-06-23 05:27:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c06de18d-173e-3d88-9fe7-7fa76f84287f | -10.5601 | -46.22709 | 2026-06-23 05:27:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 99f5bc66-d725-3087-a9a8-abfe61a6faa5 | -13.51577 | -52.16908 | 2026-06-23 05:27:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6860657b-1406-3a57-9d13-c5bc374edc29 | -12.54854 | -57.18966 | 2026-06-23 05:27:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7a0028d2-1c1c-33bc-8fbc-1bc26db5c431 | -10.76863 | -54.10958 | 2026-06-23 05:27:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 34d56453-8d5d-3db0-8f1e-6ba2658e9f89 | -10.5673 | -46.22779 | 2026-06-23 05:27:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e4e50134-2fbd-3797-a3a5-95330f054ae0 | -11.87425 | -57.84053 | 2026-06-23 05:27:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3d79082c-906b-3bf7-ad10-9092fd0d61df | -10.57408 | -57.31793 | 2026-06-23 05:27:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 985f03a7-4d00-3fbb-84b6-6ae2106ac455 | -10.88402 | -49.54497 | 2026-06-23 05:27:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2e22992b-c3ae-32dc-9e48-43ac4c8edcd5 | -8.86053 | -46.94764 | 2026-06-23 05:27:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| e069e018-45a1-3055-a645-735db543543f | -11.0558 | -49.575 | 2026-06-23 05:27:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a8af32c5-1afe-3db4-b6a9-01954b1b61db | -9.44718 | -50.84399 | 2026-06-23 05:27:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b2be561c-7f7f-3078-831e-88005ce76740 | -12.03774 | -47.80708 | 2026-06-23 05:27:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e4dbe0ab-7250-31f6-876a-808c61092025 | -11.27754 | -55.78794 | 2026-06-23 05:27:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 642dcb27-671b-3c24-a961-025321102815 | -10.93665 | -56.85227 | 2026-06-23 05:27:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e383f0a5-581c-32d6-b7a3-eca5ba5e57f1 | -9.44762 | -50.84063 | 2026-06-23 05:27:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 70f4e13a-4738-386b-a971-351d3e7d0cfd | -6.93557 | -51.94363 | 2026-06-23 05:27:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 48f38dba-989b-39c0-a94d-2ea06d893e7e | -9.12605 | -50.93793 | 2026-06-23 05:27:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 952edae5-d44b-3e3c-9a84-dccdc2a0a9e1 | -12.28803 | -57.57469 | 2026-06-23 05:27:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f2d00429-615a-3c05-a990-7dc81788d2ec | -11.30871 | -54.72588 | 2026-06-23 05:27:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1cb35a1a-e711-33e3-aee7-b94d8d251883 | -11.87543 | -57.83252 | 2026-06-23 05:27:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2f4ffec3-f2cb-3ebd-9b3b-be112827dbd3 | -9.45951 | -49.83512 | 2026-06-23 05:27:00 | NPP-375D | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 72899f9c-ef65-330c-bdb3-d4812c51117c | -10.90657 | -54.13995 | 2026-06-23 05:27:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1bff1713-425f-3436-9b63-0792151f4fc1 | -12.65442 | -47.67904 | 2026-06-23 05:27:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7c25c02c-f8d6-3742-9d16-fe8dc8f04ae6 | -11.28072 | -55.79355 | 2026-06-23 05:27:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9a17836d-60eb-3094-b4ac-84f3c4e54f19 | -12.28864 | -57.57053 | 2026-06-23 05:27:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4d7d2647-aebc-38f7-b640-3b4328551ce3 | -9.21513 | -47.93219 | 2026-06-23 05:27:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8aa03cc6-d043-3c57-b995-f2161ae90a2f | -8.87462 | -46.94486 | 2026-06-23 05:27:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9436b57e-2ba1-3218-ba8c-ed6cee8967e6 | -9.36944 | -50.53775 | 2026-06-23 05:27:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 85bb1b9e-e593-379e-9255-5ee3a6e3a740 | -12.54424 | -57.19347 | 2026-06-23 05:27:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0767df7f-fcaa-3004-a281-5679aebce094 | -11.05086 | -52.46978 | 2026-06-23 05:27:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 12371a70-7766-32a0-96f6-2d7e2301a3bc | -11.30924 | -54.72204 | 2026-06-23 05:27:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6cc2e962-adb2-365f-9edf-b0e749a96bc5 | -11.87251 | -57.82922 | 2026-06-23 05:27:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2245680c-2d3d-354f-ac01-f351a713ca12 | -11.46954 | -46.6884 | 2026-06-23 05:27:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| a923bdff-7407-3a58-8206-5e5e93fe1bc2 | -11.86837 | -57.8327 | 2026-06-23 05:27:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6c11ed46-33ae-3e30-b522-6895da5f010b | -10.77728 | -54.11088 | 2026-06-23 05:27:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 78056e33-5b15-39b7-b104-38f74e3e817e | -12.6837 | -54.57999 | 2026-06-23 05:27:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6a954336-768d-373d-92f6-4c7f0b593f43 | -12.50043 | -48.27436 | 2026-06-23 05:27:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e8946d41-40d4-310c-8850-23b7b368f590 | -8.8612 | -46.94238 | 2026-06-23 05:27:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c8e6885d-69a7-3273-a206-0964beb2463d | -10.27608 | -60.54528 | 2026-06-23 05:27:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a5d4ba03-8c6c-3c39-bdff-ac7f52e97ae7 | -9.36899 | -50.54122 | 2026-06-23 05:27:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 144c37f5-cc06-3600-aacf-a5d93fb16bd3 | -10.12101 | -52.20163 | 2026-06-23 05:27:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3bb18e62-1bf0-3c45-aced-150646b351ec | -10.8835 | -49.5492 | 2026-06-23 05:27:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7abdacde-a1a1-3bc6-800a-b9721c416918 | -12.50065 | -48.26977 | 2026-06-23 05:27:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 58a7c17a-45d7-3e46-b4a8-467498d2c2c3 | -11.87604 | -57.82977 | 2026-06-23 05:27:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c15e996d-a8b9-3904-9d58-588bfc3c5cd3 | -10.56648 | -46.23492 | 2026-06-23 05:27:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d9ae039a-0155-341b-ac71-3e2ea2f75f81 | -11.05571 | -52.47053 | 2026-06-23 05:27:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 56dc6382-0c03-357b-b1b9-4876c09726d5 | -11.79959 | -47.34291 | 2026-06-23 05:27:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ab7e6a8a-1d21-3ec9-a5d1-d261050a15a9 | -12.43029 | -58.4034 | 2026-06-23 05:27:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9419bc41-0370-3d63-8970-6f06ba760f13 | -11.80641 | -47.34381 | 2026-06-23 05:27:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4fef72c1-26f9-35ab-89bb-ab7e26a1f7d5 | -9.36805 | -50.54003 | 2026-06-23 05:27:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 19709ae9-e740-3798-a662-379e351362b3 | -10.97054 | -48.15549 | 2026-06-23 05:27:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 638eb82f-e318-3af1-ac91-8b54d3889e64 | -12.46717 | -55.12818 | 2026-06-23 05:27:00 | NPP-375D | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e386b347-7022-336a-a0ff-f5ed81055a85 | -11.47725 | -46.68357 | 2026-06-23 05:27:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 09964802-6b27-3b96-ae8a-543423882de6 | -14.03066 | -54.47588 | 2026-06-23 05:27:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 32c26a93-e0f1-33d9-9d19-3754f4c3ee33 | -12.91549 | -49.47788 | 2026-06-23 05:27:00 | NPP-375D | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9fbb7ef4-6a16-3acb-bb3d-3887014c3dff | -9.38181 | -58.20525 | 2026-06-23 05:27:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 293655f6-3a36-3713-ae63-2a264985a967 | -11.0467 | -52.46368 | 2026-06-23 05:27:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| eb113188-c0e2-3e9e-ba17-d185cf63331e | -12.29162 | -57.57522 | 2026-06-23 05:27:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e1bed2de-2b22-3229-9ab3-e95eff22eaf8 | -11.54391 | -52.78238 | 2026-06-23 05:27:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c138df9a-ae21-3f7f-a416-333e9c2da37b | -9.3784 | -58.20472 | 2026-06-23 05:27:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 692177d0-7e63-369f-9fee-9de3c1bb3e97 | -13.50116 | -56.57058 | 2026-06-23 05:27:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ec10a710-dfb5-38ec-a45f-f4ab87b27ab9 | -11.57907 | -47.44196 | 2026-06-23 05:27:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c362c5d1-d410-330a-8ddd-9d8f374a5eb9 | -12.29039 | -57.58351 | 2026-06-23 05:27:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 53cffe2b-ce17-3009-a056-3ca1767f1702 | -12.28741 | -57.57884 | 2026-06-23 05:27:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6dc97515-35a2-3f52-bdf1-afab40059074 | -10.27275 | -60.54473 | 2026-06-23 05:27:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e57347c4-a170-3d07-ad3a-011bab2d3442 | -11.8104 | -52.52632 | 2026-06-23 05:27:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 9929f35f-155f-332e-8541-e94fe35a55b2 | -12.03115 | -47.80563 | 2026-06-23 05:27:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| fa4c621f-2081-318b-b589-96cc7bdfb231 | -11.30505 | -54.72143 | 2026-06-23 05:27:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b9c0fa44-9fb3-38cc-a40b-12eb1cb90238 | -10.40259 | -49.44891 | 2026-06-23 05:27:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c812ff12-ee56-3d16-9b2b-51cbb32c26a3 | -12.56225 | -57.76077 | 2026-06-23 05:27:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6d379ddc-1270-3508-8e79-4b4da6465524 | -12.91496 | -49.48251 | 2026-06-23 05:27:00 | NPP-375D | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 570b9985-5589-3e88-b258-b777438657c1 | -12.50004 | -48.27531 | 2026-06-23 05:27:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5f99a51c-2172-3a88-b3e2-b44281dd5ea9 | -12.29223 | -57.57106 | 2026-06-23 05:27:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d4399544-76c0-3aa9-9ddf-d63b9d3a8b4d | -9.46001 | -49.83121 | 2026-06-23 05:27:00 | NPP-375D | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 88d35f3a-d3d0-3484-a4b9-d3843bf2c01a | -10.27552 | -60.5488 | 2026-06-23 05:27:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 33f1e81c-418d-3bf0-bbc6-5e03d1d60799 | -9.38238 | -58.20156 | 2026-06-23 05:27:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8665bafe-906e-314a-954f-f77a894c56e3 | -12.432 | -58.41551 | 2026-06-23 05:27:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 886e0a6e-2a34-38a8-b610-51be45db4aaf | -12.43087 | -58.39955 | 2026-06-23 05:27:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9ce4157c-d404-3542-af9d-367006168b4b | -11.87129 | -57.83725 | 2026-06-23 05:27:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 69b6ea6f-5c54-3cfd-b3dc-3866e4b5417d | -10.90716 | -54.13585 | 2026-06-23 05:27:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0b30bef0-9737-3850-8dd9-2e206e71b53d | -11.57227 | -47.44138 | 2026-06-23 05:27:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 82bc6435-99ce-37ad-a5b4-10d2e35c9d59 | -17.67992 | -47.24179 | 2026-06-23 05:29:00 | NPP-375D | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 67eb165a-9a1e-30eb-9d42-019f2f8c52c6 | -17.68778 | -47.23616 | 2026-06-23 05:29:00 | NPP-375D | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3752d923-ff69-3269-a568-7d14a89cfceb | -16.00757 | -57.82304 | 2026-06-23 05:29:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 2008166c-3bac-33d9-a642-3d24677741ad | -12.8548 | -44.3625 | 2026-06-23 05:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 138.0 |
| 89f15720-de8a-35fe-ab11-ff1394ccdff6 | -12.8552 | -44.3389 | 2026-06-23 05:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 62.6 |
| cddeb97b-52ee-345c-8dca-3a98b707cd59 | -12.8741 | -44.3593 | 2026-06-23 05:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 79.2 |
| 5ca3e50e-12a0-310a-8f44-43ed86727a4f | -12.8746 | -44.3357 | 2026-06-23 05:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 43.4 |
| 7859de85-c2ed-3f3d-bfc1-533e91ab0821 | -12.8741 | -44.3593 | 2026-06-23 05:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 67.8 |
| e8a67289-e2a3-3cdd-93d3-fd50443ad905 | -12.8552 | -44.3389 | 2026-06-23 05:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 0c9e09a1-68fd-370f-b876-bb9a1e8fdaa8 | -12.8548 | -44.3625 | 2026-06-23 05:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 110.7 |
| e3c1cf16-a329-3363-b98c-0903e39138d8 | -12.86467 | -44.35484 | 2026-06-23 05:44:00 | AQUA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 100.6 |
| 5c4d1646-db8d-3c89-860a-7bbd25b48295 | -12.84943 | -44.35176 | 2026-06-23 05:44:00 | AQUA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 187.4 |
| c9f5c898-8f7c-39fc-8c93-c26dacc2d80f | 2.58672 | -60.69595 | 2026-06-23 05:44:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README17.md)
