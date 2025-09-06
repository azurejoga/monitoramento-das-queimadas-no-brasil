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

## Dados Diários - Página 64

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 263921b2-7f66-34f4-b08a-94ad61194405 | -12.962 | -54.77855 | 2025-09-06 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a57544f3-0a11-33eb-8aba-8acf3991dc90 | -11.60634 | -52.15878 | 2025-09-06 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0ce28e2b-a90f-3bea-875c-9f33eab5790a | -10.31435 | -46.41799 | 2025-09-06 04:40:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5ccbc967-5e2e-3857-b7af-c84576687433 | -15.7086 | -53.58668 | 2025-09-06 04:40:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 84225863-1c57-32c1-a902-4fa285cbd108 | -9.60833 | -55.02128 | 2025-09-06 04:40:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f26693d9-08f0-349a-86b2-3ac965176840 | -13.01834 | -54.83799 | 2025-09-06 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d8e1af0d-c9f6-3fa1-9462-ccfc392972a0 | -12.93455 | -48.04649 | 2025-09-06 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 48c13a2f-1a37-312d-bf45-687ee1a07653 | -13.74969 | -46.93134 | 2025-09-06 04:40:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 25e40f78-9ad3-307b-92ab-55fceb0054dc | -16.63778 | -51.86406 | 2025-09-06 04:40:00 | NOAA-20 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5a1ed917-5b6c-3a87-8749-2d403b8507be | -11.09572 | -52.01846 | 2025-09-06 04:40:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ca7b139c-9fc5-3b57-ab99-a40cbe88d437 | -12.99844 | -48.05033 | 2025-09-06 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 15d8a134-a1cf-3d54-82bd-b5e2ae4f996f | -11.06358 | -55.38211 | 2025-09-06 04:40:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| edfb9a98-7331-332b-9916-77c75aaed0f0 | -9.71366 | -49.49115 | 2025-09-06 04:40:00 | NOAA-20 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 3a703076-e428-316d-803f-134f5d0e59e8 | -10.09289 | -48.08502 | 2025-09-06 04:40:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cc054f87-287c-30f5-8ed5-34cd5ca59d3a | -11.60792 | -52.17035 | 2025-09-06 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c7f8d1e0-104a-3d56-a394-d3ad54fd021b | -11.61109 | -52.19353 | 2025-09-06 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bb02a86a-347e-3972-9ea2-383ad730b203 | -9.39721 | -54.74984 | 2025-09-06 04:40:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e8fdea6d-f81f-3767-9a47-3a02261b788c | -11.60493 | -52.18872 | 2025-09-06 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4f14a132-f764-3db5-893a-d5476e46ecef | -11.64769 | -47.15253 | 2025-09-06 04:40:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6c0e60c9-5389-3ba3-a31e-a92fc596c1e3 | -11.60155 | -52.18814 | 2025-09-06 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c1ccacce-d4c5-30c2-a236-d7bcf46390f9 | -12.95093 | -46.56621 | 2025-09-06 04:40:00 | NOAA-20 | NOVO ALEGRE | TOCANTINS | Brasil | 1715150 | 17 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 158ada39-d14f-3d28-9081-2ea599e61ef1 | -12.98798 | -54.81372 | 2025-09-06 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0bab9fc5-9f8f-3331-b934-7cd846be26cf | -12.95227 | -54.79078 | 2025-09-06 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 864400f3-1250-31c7-83a1-d54863c178a9 | -12.9908 | -49.16396 | 2025-09-06 04:40:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d5dc63fc-614f-3786-a2f3-a1eca0bd1b43 | -12.50935 | -53.86305 | 2025-09-06 04:40:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 7c0e43a1-60bb-381e-82f3-0c573b81d34e | -12.48291 | -53.84571 | 2025-09-06 04:40:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b3055e7a-f761-3901-902f-6627e19549f3 | -9.32967 | -55.21012 | 2025-09-06 04:40:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aaab32be-a58e-3eb3-9d9e-1f78ce3c8896 | -14.96094 | -47.59187 | 2025-09-06 04:40:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 39664d6e-77a5-34fe-bb75-352ed1620a01 | -14.57186 | -48.03432 | 2025-09-06 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f4ef8dc7-7a26-389f-ac10-708c359896fe | -16.32656 | -52.95195 | 2025-09-06 04:40:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2adf743d-3699-343b-9b6d-f27ce3c7becd | -15.58873 | -52.91294 | 2025-09-06 04:40:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8a1860b6-bc08-3531-b884-8a909ae53deb | -16.32106 | -52.9435 | 2025-09-06 04:40:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8197555b-8404-386e-966a-65ab0bb44cc4 | -12.95739 | -54.81298 | 2025-09-06 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ecca2d7c-195e-37f2-9a21-3bcdacb67610 | -16.31978 | -52.93994 | 2025-09-06 04:40:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 68578bae-cae5-3e95-8265-b54295a46148 | -9.42833 | -62.37177 | 2025-09-06 04:40:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d866c649-f34f-315f-8045-760735c5f448 | -12.88594 | -56.95229 | 2025-09-06 04:40:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f62ee500-a7df-30c5-8279-35f07aa4a216 | -13.8928 | -47.95452 | 2025-09-06 04:40:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 198fb3d7-6535-3abd-a5f5-c0f52943c3cf | -12.48866 | -53.87661 | 2025-09-06 04:40:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 32eec0b8-f22c-3c5d-97b4-f6fec43240cb | -10.15255 | -46.22929 | 2025-09-06 04:40:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6c28f7e4-61d8-354f-b987-92eec2c1f656 | -13.55589 | -48.1152 | 2025-09-06 04:40:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| be5aa76d-66e3-3c43-9839-54fd92f88e57 | -15.76067 | -53.65508 | 2025-09-06 04:40:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c4a777bc-d348-3ff8-a974-deeb1f5e9fcc | -12.95599 | -54.79145 | 2025-09-06 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2ac231ca-1529-3dc1-bd8d-8ea78b579494 | -15.57558 | -52.88783 | 2025-09-06 04:40:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 12e60220-7493-3a2c-8e26-ccfdf4737682 | -14.59297 | -48.0946 | 2025-09-06 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e5a22981-a72e-33e1-bad3-024dfe996896 | -12.53436 | -48.06418 | 2025-09-06 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 47334d4b-1722-3ebc-a42d-6efaf61e7608 | -11.21393 | -55.02634 | 2025-09-06 04:40:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ae2ff0f8-597f-3ebb-a461-9e65776d2417 | -12.99248 | -54.80988 | 2025-09-06 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3989c507-e3c3-3a69-893f-7ef4df4c2079 | -11.62779 | -52.21899 | 2025-09-06 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0c90334d-39bc-3f82-90f6-792c765fd2a7 | -14.57613 | -48.00381 | 2025-09-06 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0e3aef95-42b9-3f86-8f45-751bf3bd4083 | -10.24355 | -50.55147 | 2025-09-06 04:40:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 945f76f9-9a63-398e-bc34-7e67963349f1 | -15.20846 | -52.37164 | 2025-09-06 04:40:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 00f1ea8a-e37d-3660-afbe-11149705af4f | -16.42047 | -47.82346 | 2025-09-06 04:40:00 | NOAA-20 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 288b57a8-d457-3394-b505-7145ab807b22 | -10.14429 | -46.23275 | 2025-09-06 04:40:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5ce71736-8e06-3b31-948c-045396777083 | -12.8989 | -48.01632 | 2025-09-06 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c9fa202c-6666-3b3d-a5b2-33ce19dc9c7d | -14.57548 | -48.03492 | 2025-09-06 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 439b2209-1146-3a35-8bb4-8c7977ab1ad6 | -12.48079 | -53.85812 | 2025-09-06 04:40:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6b382644-2615-351d-ba59-0492f4a34914 | -11.60613 | -52.18137 | 2025-09-06 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3110ad3e-9a61-345e-92ce-3aaad221700e | -9.74583 | -51.05417 | 2025-09-06 04:40:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9a70fb02-e19b-38da-8144-8cd3ee22dd88 | -12.49723 | -53.8695 | 2025-09-06 04:40:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c1f8fbbf-616f-3c68-acc8-e07f622b7d9a | -15.14827 | -53.51398 | 2025-09-06 04:40:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c8c35b37-7b9f-34fc-b615-c64439db10fa | -14.7194 | -55.92719 | 2025-09-06 04:40:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ffcce625-126e-3975-a96a-693518bb2cb4 | -15.18559 | -48.04169 | 2025-09-06 04:40:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f24d42c4-644e-3615-bd7f-29bb1f80693c | -11.20148 | -55.02916 | 2025-09-06 04:40:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4ac4e815-c02f-3860-9808-fe11849b8ae0 | -12.96343 | -54.79279 | 2025-09-06 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bf8bf421-5846-3e13-8102-987abf4bc397 | -13.33123 | -51.72592 | 2025-09-06 04:40:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 810dd859-9df8-3006-9d22-7d7f18562625 | -11.59221 | -47.74392 | 2025-09-06 04:40:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 24b36d62-c91f-3789-be45-45c91f94af1e | -12.99327 | -54.80535 | 2025-09-06 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5fef6dd6-ecb4-3a07-87cb-a34f9ba26734 | -10.03699 | -48.12734 | 2025-09-06 04:40:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f61422c9-8478-3687-932f-9368a2a25518 | -12.29611 | -49.99716 | 2025-09-06 04:40:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0484d277-c65e-3b57-b9da-2ab3cc95d419 | -12.29889 | -50.00126 | 2025-09-06 04:40:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 91c66a43-377d-395d-a0ec-a91e81bc9c23 | -11.63277 | -52.23118 | 2025-09-06 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 684d8fdf-a330-393a-9ee1-0e495901cd42 | -10.60941 | -44.32761 | 2025-09-06 04:40:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| b769aab6-d09b-3c4d-9503-a7c1b67816cb | -15.12689 | -52.34667 | 2025-09-06 04:40:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 14.2 |
| be612a28-6719-3952-8029-c2395d90eec7 | -11.09411 | -52.00698 | 2025-09-06 04:40:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bbef76bc-eeef-35a6-a728-98f86968c931 | -11.06831 | -51.9952 | 2025-09-06 04:40:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a0fc0316-f152-3c43-b822-f51751839b3c | -11.60356 | -52.15454 | 2025-09-06 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 11122166-d6be-32ab-af62-06ce82c3dfd2 | -14.80329 | -48.11032 | 2025-09-06 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a3457114-e6bb-3868-aa9d-699ad378bcee | -12.49365 | -53.86889 | 2025-09-06 04:40:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 16dd017b-75bc-32cf-9a58-7b8576d2ede6 | -17.96404 | -44.4189 | 2025-09-06 04:40:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3b14e6c1-8962-3717-9e60-d11a7ec99eb8 | -13.05307 | -47.10606 | 2025-09-06 04:40:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 77aeecf8-24fa-375e-b0e2-b6b86b11d7e9 | -12.99677 | -54.82947 | 2025-09-06 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 147ae387-da2d-333f-b29f-3c871400c408 | -12.95286 | -54.81691 | 2025-09-06 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3e8f5f60-4cae-3f2c-a358-fdf64f949b80 | -13.93082 | -53.99593 | 2025-09-06 04:40:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| db5a4eb5-e90d-3faa-85bf-0cd81e8968af | -12.95458 | -54.77718 | 2025-09-06 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f88b1977-1e74-3706-bc3b-ce1f14a2d26d | -13.31662 | -51.64674 | 2025-09-06 04:40:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 78d5746b-e442-3278-a88c-4048f6eb3422 | -9.39635 | -54.75482 | 2025-09-06 04:40:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bf57dcc3-3f3c-3370-b4ee-d8d04576f82f | -10.09063 | -48.07656 | 2025-09-06 04:40:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3948ef09-e553-3dd8-9a9f-8e34b9565cd8 | -12.97307 | -54.81112 | 2025-09-06 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2f8e6a00-25a5-3fc7-9133-002648658002 | -14.43358 | -52.97674 | 2025-09-06 04:40:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c03e6f40-c776-3603-bf40-7c8ff0f7b6fd | -11.36232 | -50.30442 | 2025-09-06 04:40:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7e0d450c-57b4-3b91-b0ad-cb0504d34587 | -12.96352 | -54.79992 | 2025-09-06 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 20b3bd1e-0858-35ec-8834-b13948bf9f63 | -15.8509 | -52.28413 | 2025-09-06 04:40:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 0a3ada0d-500b-33d9-a20b-56ed0c14b3fd | -12.85781 | -47.998 | 2025-09-06 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4067cf4a-120e-36a6-85f9-518145ad254c | -15.06558 | -50.06892 | 2025-09-06 04:40:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6238d43c-e1ca-3cde-85c5-9672b6926f4d | -14.34217 | -60.32875 | 2025-09-06 04:40:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 30b907a6-7094-3933-826f-db8fbbf557f1 | -16.29064 | -45.68869 | 2025-09-06 04:40:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 548170fa-e7aa-32df-afbd-753bae43402f | -16.54531 | -42.34754 | 2025-09-06 04:40:00 | NOAA-20 | VIRGEM DA LAPA | MINAS GERAIS | Brasil | 3171600 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7f857c6b-e939-39ac-b3b1-367962fab7c0 | -13.00343 | -54.83538 | 2025-09-06 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 03bac1a2-bd3a-3476-9bb7-512262dc2033 | -11.2062 | -55.02494 | 2025-09-06 04:40:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4d6efe3b-becb-3b05-98d8-9de588474efa | -11.8488 | -47.56766 | 2025-09-06 04:40:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |


[Clique aqui para ver as próximas entradas](README65.md)
