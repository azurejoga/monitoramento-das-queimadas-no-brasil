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

## Dados Diários - Página 132

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ea3edc01-e405-3939-b82d-caa52da1d6fd | -10.85909 | -68.24625 | 2024-10-06 05:36:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4fae86f4-a5cb-329a-a9d0-2e5b61d49179 | -10.75822 | -68.71796 | 2024-10-06 05:36:00 | NPP-375D | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9633a279-e23b-3c5c-82b0-036f196d688d | -10.65798 | -69.13292 | 2024-10-06 05:36:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 91bf3e80-cee1-34f8-a753-152e1fdb82d9 | -10.58097 | -69.06627 | 2024-10-06 05:36:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 012d31fd-1896-304e-99ef-fa1d02329526 | -10.57792 | -69.06059 | 2024-10-06 05:36:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6e2a3ab0-72c9-3510-b129-6946bf8b4d7b | -10.57708 | -69.06554 | 2024-10-06 05:36:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 657c37e4-3b59-3ad4-b11b-b368e337e4a5 | -10.53092 | -67.73796 | 2024-10-06 05:36:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 1fdbcb94-acba-354e-9c62-d5f2cf70de65 | -10.5302 | -67.7422 | 2024-10-06 05:36:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 5.4 |
| cea16f8e-e1b9-30d9-bed5-2c7368d833a6 | -10.50119 | -68.6664 | 2024-10-06 05:36:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b01e687f-316d-30e8-b6ee-db7bda835929 | -10.4589 | -67.88033 | 2024-10-06 05:36:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2ce659f7-a466-3b67-8386-dd7d43a49e66 | -10.45819 | -67.88463 | 2024-10-06 05:36:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| afbf0131-cd9c-3cb2-9e87-d7a04620a210 | -10.38585 | -67.9567 | 2024-10-06 05:36:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 29f987a0-e14f-3bdc-9db0-9938ea9d65ea | -10.38219 | -67.95605 | 2024-10-06 05:36:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 32bf8cbd-6b65-3b08-a939-d7e0bdb89da5 | -10.36417 | -68.17477 | 2024-10-06 05:36:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9cf4c87a-8dbf-392f-ae11-1e895e0de0f1 | -10.28819 | -68.02699 | 2024-10-06 05:36:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6cb4974e-0522-3df6-b6da-e9c14f066b08 | -10.28745 | -68.03136 | 2024-10-06 05:36:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 503e5c08-526a-386a-b8ee-263541cb093b | -10.25009 | -68.20772 | 2024-10-06 05:36:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5ec61262-8cf8-35d3-b785-289774f7b81f | -10.24636 | -68.20708 | 2024-10-06 05:36:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f6e985e6-abee-334f-948b-7fb8d8563164 | -10.10362 | -68.06301 | 2024-10-06 05:36:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0909db12-0932-36ac-8637-1b953fa1af46 | -10.10289 | -68.06744 | 2024-10-06 05:36:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 79f665a2-51e2-333c-9003-38bf38f98188 | -10.10238 | -68.28221 | 2024-10-06 05:36:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 62eb6854-c85e-3e87-8751-918ac2077ce7 | -10.1016 | -68.28676 | 2024-10-06 05:36:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 5.8 |
| dd013afc-5914-3b00-9b0f-c260d894fdc9 | -10.06008 | -68.37144 | 2024-10-06 05:36:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ea59f443-e4f9-354b-99d5-fa6aeb937362 | -10.05956 | -68.37371 | 2024-10-06 05:36:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c954f5f5-4f74-3780-91f8-e2e90842aa31 | -10.05631 | -68.37081 | 2024-10-06 05:36:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 7404dacf-8c78-3bbd-999d-605eac580d55 | -10.05554 | -68.37543 | 2024-10-06 05:36:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e5ce5ca1-d9b0-3007-a8db-52804c3c54c4 | -9.71751 | -67.73428 | 2024-10-06 05:36:00 | NPP-375D | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cfea23e4-bce5-3cc3-9fb5-c90694e52242 | -9.71385 | -67.73366 | 2024-10-06 05:36:00 | NPP-375D | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 6.0 |
| d9d0dfd2-1e24-398b-9749-c423916dd0d8 | -10.954 | -68.34879 | 2024-10-06 05:36:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 99e46644-136e-33a0-a776-5332ed94d59b | -10.9359 | -68.49908 | 2024-10-06 05:36:00 | NPP-375D | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8d91d2cf-9a8d-3df1-ad8f-bff9dfb470eb | -10.92968 | -68.42321 | 2024-10-06 05:36:00 | NPP-375D | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f67ca30b-a0f3-3e54-966f-d2bb78b6fd74 | -10.92858 | -68.4244 | 2024-10-06 05:36:00 | NPP-375D | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4c760f2f-67d7-3f5e-98bc-0e3113ab48d4 | -10.92426 | -68.24398 | 2024-10-06 05:36:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5491f9e4-c5cb-3d6e-b23c-b6690a9f288f | -10.92131 | -68.23888 | 2024-10-06 05:36:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 45874626-7f04-36f1-9198-72180a05c251 | -10.92057 | -68.24332 | 2024-10-06 05:36:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a5beba7d-a2d9-3498-9ff0-057cbe05bd07 | -10.90644 | -68.28198 | 2024-10-06 05:36:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1005ec99-725b-3e63-a22e-9bd7eba3b9fc | -10.88846 | -69.12204 | 2024-10-06 05:36:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4977db83-9fa5-3fa7-9d43-6cf9607695e6 | -10.85999 | -68.64908 | 2024-10-06 05:36:00 | NPP-375D | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7ab551cd-8d29-309e-8922-8e9b0dc48281 | -13.68077 | -51.18537 | 2024-10-06 05:36:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f3bb3c9c-1822-3f6b-a389-098da330f297 | -13.67356 | -51.18456 | 2024-10-06 05:36:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 0e95fdad-af64-328b-b583-6aa5ed09b193 | -13.67282 | -51.19179 | 2024-10-06 05:36:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| af7625d8-3ab9-353d-a667-562c96dc08d6 | -13.66636 | -51.18377 | 2024-10-06 05:36:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 58c1dad5-e5c4-32bd-bace-7786bc0666ad | -13.66562 | -51.19099 | 2024-10-06 05:36:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 5d7f707b-9dc0-3d1e-85ed-52d75bbf87ee | -10.89958 | -52.37762 | 2024-10-06 05:36:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| af59467c-3386-36cc-94af-e545de15fae2 | -10.89892 | -52.38319 | 2024-10-06 05:36:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9b4d16a5-deda-3b3e-98e8-39a510f7b6fc | -11.65185 | -54.53067 | 2024-10-06 05:36:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8d56cc79-a61c-3b4e-9744-00e722e7ae71 | -11.65093 | -54.52816 | 2024-10-06 05:36:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6cca2f16-ef94-34c9-9862-4bf29ffb1fbe | -11.65042 | -54.53223 | 2024-10-06 05:36:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0f03a26a-b232-3780-98de-5f9296ddb9e6 | -11.64658 | -54.52587 | 2024-10-06 05:36:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 07de6639-31e4-399a-a506-7e49e0897e0b | -11.64609 | -54.52999 | 2024-10-06 05:36:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c63f0798-b283-38e6-84e7-f0b16bcd9269 | -11.64569 | -54.52335 | 2024-10-06 05:36:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 288fb1ac-7db5-3e41-807a-cfb9099a1f0a | -11.64517 | -54.52748 | 2024-10-06 05:36:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 380b4b21-93ee-3e6e-96c9-d1261590029d | -11.64467 | -54.53156 | 2024-10-06 05:36:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 579df22a-8401-3dd9-9b47-3a375bb803d9 | -11.38382 | -54.35952 | 2024-10-06 05:36:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 48ceaa05-1e61-316e-b78c-2334b91976b7 | -11.38332 | -54.36367 | 2024-10-06 05:36:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 385e1a0b-19e1-3cea-8e00-f1787163ad2e | -11.10624 | -54.22666 | 2024-10-06 05:36:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4aadb4fe-51ab-3790-aa32-1becf77058db | -11.10575 | -54.23071 | 2024-10-06 05:36:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e6aa8ddc-8c93-3e0a-8c8a-cd1aa291de0e | -11.10525 | -54.23472 | 2024-10-06 05:36:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c649edf8-ec66-3dd5-b267-478fdf9ceb79 | -11.10476 | -54.23875 | 2024-10-06 05:36:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a8877235-17dc-3e5b-8808-7933d0b14f6f | -11.09995 | -54.22979 | 2024-10-06 05:36:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 6eb5dffe-aa3d-384f-b05e-425e5c405eaf | -11.09945 | -54.23384 | 2024-10-06 05:36:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 1dbd9b9d-f50d-3563-803d-3e7f853ccce5 | -11.09896 | -54.23789 | 2024-10-06 05:36:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7af59106-c466-3c55-9ee7-b46c668d2fb7 | -11.09316 | -54.23703 | 2024-10-06 05:36:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6fba69a9-e9d0-3b5f-b53e-cb8e11ee0f32 | -11.08436 | -54.77407 | 2024-10-06 05:36:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| dd16b0b7-4f86-3f09-961a-5b2d509c255b | -11.08339 | -54.78177 | 2024-10-06 05:36:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 75dcf9cf-5e41-397c-841c-18a6a415f35c | -11.0829 | -54.78562 | 2024-10-06 05:36:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0693dd0b-bacb-39d4-af1d-ca9dcdd38af8 | -11.08214 | -54.03183 | 2024-10-06 05:36:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d7263b8e-d47f-3d0e-a30f-13bbec73c4aa | -11.0778 | -54.78089 | 2024-10-06 05:36:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 220162dd-cd3a-3b4e-8058-fa9d5e6e92aa | -11.07765 | -54.03163 | 2024-10-06 05:36:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 7e1bdfd8-f0eb-3333-b0aa-dc4edbab8285 | -11.07624 | -54.0311 | 2024-10-06 05:36:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 92181c63-bb68-3e82-bf42-063682491c13 | -11.07219 | -54.7801 | 2024-10-06 05:36:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1b431dd2-6b4e-3c8f-81e0-6505b5197762 | -10.97512 | -54.00856 | 2024-10-06 05:36:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fd4835a1-d445-359f-ba30-6cbef68b76fe | -10.97459 | -54.01272 | 2024-10-06 05:36:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3bcce8f5-a51f-3df7-b470-6955801ff23d | -10.97408 | -54.01683 | 2024-10-06 05:36:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3d7e0fbc-b6ad-366b-b037-658babdfa8df | -10.97216 | -54.01373 | 2024-10-06 05:36:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| af7b670c-866c-332f-9f80-2360a5263979 | -10.97167 | -54.01784 | 2024-10-06 05:36:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 081ce02f-9d36-3d23-a646-ec96d0a2a61c | -10.97118 | -54.02196 | 2024-10-06 05:36:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a3f9d9e9-f4bf-3af9-be5e-a0e613c3a626 | -10.96714 | -54.02441 | 2024-10-06 05:36:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 79246ce1-50e8-3d43-b0d0-4fb484c9fee0 | -11.56451 | -55.66602 | 2024-10-06 05:36:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8e8ee028-9d41-381d-958b-3ddc3439e0f6 | -11.5641 | -55.66936 | 2024-10-06 05:36:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 72276154-852a-372a-8e10-bd0b3198864f | -11.55918 | -55.66536 | 2024-10-06 05:36:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9d8f0b65-f037-349b-866d-e078f63ca132 | -11.55876 | -55.66875 | 2024-10-06 05:36:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 2c14171b-e56f-3397-a0f9-12b644e7d210 | -11.92117 | -56.93023 | 2024-10-06 05:36:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4d901623-bc6a-37dd-9ff3-f1e9fdca866e | -11.91696 | -56.92401 | 2024-10-06 05:36:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 41343203-161d-345b-b636-ab44e8eb4796 | -11.91625 | -56.92961 | 2024-10-06 05:36:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 85fec400-a664-37af-bbdf-91755812e8a4 | -11.91205 | -56.92333 | 2024-10-06 05:36:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 778b0acd-fec3-3220-8b75-ebe35f7bbd20 | -11.91134 | -56.92896 | 2024-10-06 05:36:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 386d46e1-c424-38fa-b69a-eeb19ebd81c6 | -11.91063 | -56.93455 | 2024-10-06 05:36:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 19c1b56f-a8cc-32f9-9894-607456766fce | -11.90715 | -56.9226 | 2024-10-06 05:36:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7835389c-d2b1-38b7-8e89-50e40baeabbf | -11.90644 | -56.9282 | 2024-10-06 05:36:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4d9f8735-788a-3402-92d5-43727b9cda27 | -11.90573 | -56.93382 | 2024-10-06 05:36:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 44a34760-7b17-3828-b4b9-a95c5f6c8071 | -11.90515 | -56.92733 | 2024-10-06 05:36:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 58690ade-cb0a-32ff-957b-3f65cd9fb97e | -11.9044 | -56.93292 | 2024-10-06 05:36:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d8d18887-b708-3289-9d63-52dce66b6148 | -12.34584 | -57.36671 | 2024-10-06 05:36:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6a30f82b-a9f5-3ca6-8f5b-c4b408793a9f | -9.98549 | -59.44735 | 2024-10-06 05:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 612e099f-e263-30e8-b186-dedfa7338781 | -10.74612 | -59.32623 | 2024-10-06 05:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 658f794f-581f-3f14-b052-dacf69133a63 | -10.21922 | -59.40161 | 2024-10-06 05:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 30865b83-e44c-3e14-b4fc-56bc1a44f94a | -10.21871 | -59.40515 | 2024-10-06 05:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 5a828e53-5e48-387b-bc0f-9eff4f4e8c6f | -10.21466 | -59.40456 | 2024-10-06 05:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 0649fa2c-c84a-3278-9d43-af54c429159a | -11.86148 | -59.04933 | 2024-10-06 05:36:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README133.md)
