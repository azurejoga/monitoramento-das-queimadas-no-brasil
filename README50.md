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

## Dados Diários - Página 50

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e4a1f6bf-69a0-3207-98c4-8a5d2aac76c2 | -13.41907 | -54.3283 | 2026-08-18 04:59:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 031a0c8d-3937-3c3b-88c2-6367c185a40c | -16.234 | -57.65833 | 2026-08-18 04:59:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 6aecf960-27ec-36e8-86c3-783c083c671c | -14.38803 | -53.07442 | 2026-08-18 04:59:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8677f1cf-6d4a-39c5-a218-38dda0dcb94f | -13.40798 | -54.35549 | 2026-08-18 04:59:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e254d3dd-4bc0-389b-b3c5-5b4c3cab8657 | -16.74151 | -50.22231 | 2026-08-18 04:59:00 | NOAA-20 | PALMINÓPOLIS | GOIÁS | Brasil | 5215900 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7d774f00-ccba-33c8-b7f2-b37386c52162 | -13.4052 | -57.04851 | 2026-08-18 04:59:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6a7829e7-049b-3ea1-9647-315cb82f7345 | -19.68509 | -49.03279 | 2026-08-18 04:59:00 | NOAA-20 | COMENDADOR GOMES | MINAS GERAIS | Brasil | 3116902 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5c4df8fb-8bee-30da-a82c-4a4216ce5861 | -14.16371 | -52.89449 | 2026-08-18 04:59:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 896a8982-ac03-31ba-a6df-ac28c0859646 | -15.38652 | -52.78827 | 2026-08-18 04:59:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 87001bf9-2365-37fa-8941-18bd4181347d | -13.42358 | -57.06826 | 2026-08-18 04:59:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5b858748-3ca6-3eda-b397-073599434686 | -13.56193 | -51.77368 | 2026-08-18 04:59:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1a3e3488-73ab-35cc-aeb0-3d8d74304df6 | -14.43942 | -51.89531 | 2026-08-18 04:59:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5c11b3a7-f123-39f7-b46b-25aebd92d544 | -14.18129 | -52.91619 | 2026-08-18 04:59:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 64.6 |
| d1fedcd0-5a44-3830-b693-2ba994f579fd | -15.815 | -55.51649 | 2026-08-18 04:59:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e62290b8-183b-3995-969e-17e2774723f8 | -15.28758 | -56.43232 | 2026-08-18 04:59:00 | NOAA-20 | ACORIZAL | MATO GROSSO | Brasil | 5100102 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ceb2d843-ca6f-3248-9905-ebf37333efa4 | -15.23244 | -57.65773 | 2026-08-18 04:59:00 | NOAA-20 | LAMBARI D'OESTE | MATO GROSSO | Brasil | 5105234 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8143df5c-fadc-3c76-8626-ec95f70f2cfe | -13.27082 | -54.23524 | 2026-08-18 04:59:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ea93ae59-7153-34bd-8907-46cb6ca4b377 | -14.43709 | -51.88659 | 2026-08-18 04:59:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3c9c0934-3a85-39d1-b205-bb8f4a0acd08 | -16.04527 | -56.51999 | 2026-08-18 04:59:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7df53c45-e74f-3b35-9f9e-f52b1a6d6ee3 | -13.57896 | -51.78037 | 2026-08-18 04:59:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0f3bd169-8592-3f73-8d51-fcf6914e0530 | -15.91971 | -55.54211 | 2026-08-18 04:59:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bc0f8413-a5a4-36f9-a483-1e767050da90 | -14.17957 | -52.92746 | 2026-08-18 04:59:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 5497fc97-d247-3d86-87ca-1703c0ac117e | -14.8233 | -46.6401 | 2026-08-18 04:59:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 08b4b4fc-6390-30b7-b3a1-1267aeca6f7e | -14.1643 | -52.91357 | 2026-08-18 04:59:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 50.5 |
| d6710e39-63c0-3e6a-b6b0-19a441097cf9 | -14.35396 | -51.93636 | 2026-08-18 04:59:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 413c9344-a692-3fa0-9d1d-0ec68cc6a2b2 | -20.29807 | -46.47401 | 2026-08-18 04:59:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 7.0 |
| f2ed1b0d-ebdf-366a-a35c-396efd0ca57e | -15.06907 | -48.71745 | 2026-08-18 04:59:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 58693014-315a-3359-9001-43752dc32bfe | -14.17506 | -52.91139 | 2026-08-18 04:59:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 9ec6d047-6b50-38d3-a0b1-7269d385e39f | -14.54661 | -48.15909 | 2026-08-18 04:59:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f65bae67-f93e-36c2-ad6b-8116cd3f8b6e | -14.03638 | -53.6808 | 2026-08-18 04:59:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 40beadb0-5119-38e8-8d29-06c8c49888cb | -13.42136 | -57.06305 | 2026-08-18 04:59:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6fb6e4dd-19f5-398e-a743-692ca25538d9 | -14.42354 | -51.88034 | 2026-08-18 04:59:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 480b7f2a-36e6-3cd2-a6da-7dc8789ba184 | -13.39529 | -54.34978 | 2026-08-18 04:59:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1ed2e168-1f18-35b9-8e7e-c3c1616e2e98 | -13.413 | -54.32368 | 2026-08-18 04:59:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d4b357a9-e16c-3618-b416-f3295a88da91 | -17.46027 | -47.86375 | 2026-08-18 04:59:00 | NOAA-20 | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2aa11b9c-885d-316c-b8cc-4d559a7efaa0 | -13.4277 | -57.06824 | 2026-08-18 04:59:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 35e8eaaa-b7fe-3c61-8312-7e62535afc2c | -16.30312 | -53.18335 | 2026-08-18 04:59:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b83aa3c5-374d-3f50-82cc-9270d10df4c0 | -13.40359 | -54.34026 | 2026-08-18 04:59:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 97c19258-2478-3d59-9195-2eaaa06a020c | -14.16882 | -52.92959 | 2026-08-18 04:59:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 54e6cf23-fe57-31e8-a7df-7dbdb4f377e9 | -14.43295 | -51.89014 | 2026-08-18 04:59:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ae9d608a-cea9-3369-af34-075d6a1b25f7 | -13.40804 | -57.05314 | 2026-08-18 04:59:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| eed40930-1d9f-3f18-b3ce-dd18005e2e5b | -14.38909 | -53.07339 | 2026-08-18 04:59:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b9d2c70a-533c-3481-9535-9c874747c9d2 | -17.34152 | -54.92878 | 2026-08-18 04:59:00 | NOAA-20 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 74bf6658-011b-310d-80f7-e9fb21f4d92c | -15.2598 | -56.48927 | 2026-08-18 04:59:00 | NOAA-20 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ebe8b37e-6b1a-3531-9210-7c89c72ffc44 | -15.26807 | -56.48669 | 2026-08-18 04:59:00 | NOAA-20 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ad9faf81-fd3c-39cc-8f3c-c136873c9481 | -14.0386 | -53.68852 | 2026-08-18 04:59:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 3ba0092b-9cd0-3cde-aa59-5ac3fdce6379 | -15.9164 | -55.54153 | 2026-08-18 04:59:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1e1e057a-76a2-3d4d-a301-8b4cbe957dea | -15.78368 | -55.56285 | 2026-08-18 04:59:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ce184e6f-1d1a-3f83-9154-3a78d7090476 | -15.25881 | -56.50045 | 2026-08-18 04:59:00 | NOAA-20 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cfd0c5fd-05e5-3296-bf5f-441bafe5ee0c | -14.35631 | -51.92012 | 2026-08-18 04:59:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 834eb0a3-e318-3d74-bb9a-4637e2e9d946 | -14.83527 | -46.6385 | 2026-08-18 04:59:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 40e8aa31-aa29-3f3a-8aad-9897009e0465 | -15.29097 | -56.43291 | 2026-08-18 04:59:00 | NOAA-20 | ACORIZAL | MATO GROSSO | Brasil | 5100102 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bec8b410-b273-3298-87e0-5745212274b2 | -14.25802 | -51.92677 | 2026-08-18 04:59:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 56805910-38a9-3ab2-acc3-0d6ffe976215 | -14.02081 | -53.60445 | 2026-08-18 04:59:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5d645875-6e97-3fcd-b6fc-3576cbd4d97c | -16.22907 | -57.64485 | 2026-08-18 04:59:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| e931d2f5-c48d-38d5-a18f-06fad024557a | -14.5473 | -48.15731 | 2026-08-18 04:59:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 97d2aaf7-4d5c-38d8-b98e-7f5378bd6d5f | -14.42294 | -51.88443 | 2026-08-18 04:59:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 13aa4554-819f-3488-8250-674de0020b2b | -14.16939 | -52.92583 | 2026-08-18 04:59:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 9b2f7e90-e94c-30d1-9039-7207321f03f3 | -13.58541 | -51.78548 | 2026-08-18 04:59:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 0629455e-6885-3b58-9bb2-4a3f7fc2a7ae | -13.42701 | -57.07226 | 2026-08-18 04:59:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3c155e85-553a-38bf-bbca-6dafb746a095 | -13.43892 | -57.06603 | 2026-08-18 04:59:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9150162a-719f-33ca-9015-705e1b6993c4 | -13.58249 | -51.7809 | 2026-08-18 04:59:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 82e9b782-65c4-34a8-983d-4822e889fcc6 | -20.29235 | -46.47721 | 2026-08-18 04:59:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 2e4b87c8-c853-3255-889c-a0ab857f1936 | -14.35574 | -51.87405 | 2026-08-18 04:59:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 88268364-bedb-3e6d-8ee7-d37886330502 | -13.01902 | -56.58284 | 2026-08-18 04:59:00 | NOAA-20 | LUCAS DO RIO VERDE | MATO GROSSO | Brasil | 5105259 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d48a78c5-8e1c-3997-b7f5-a2f795986d5a | -15.91594 | -56.49753 | 2026-08-18 04:59:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8b4f627b-d5f8-3896-8a0d-2032370abae3 | -14.17448 | -52.89232 | 2026-08-18 04:59:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f9f574e8-64f6-39c5-b7fa-76c02364db2b | -13.57843 | -51.75964 | 2026-08-18 04:59:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 02205404-030b-3c93-bd9d-558afcb2671f | -17.08617 | -46.60337 | 2026-08-18 04:59:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3feec17f-cb41-3d4f-afe7-8dfb01572a58 | -14.83181 | -46.65193 | 2026-08-18 04:59:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 39cff19a-b03c-3366-9779-53012d0dc89d | -17.47921 | -48.87443 | 2026-08-18 04:59:00 | NOAA-20 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8ea527b4-2f5b-3d64-b9f6-3f5dbee795aa | -17.45859 | -47.86193 | 2026-08-18 04:59:00 | NOAA-20 | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 9d108ccd-835f-30c2-b1ea-d15566ddf1d3 | -14.80737 | -46.6476 | 2026-08-18 04:59:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 2651364f-90dd-3f11-89f8-63b5f4c6816f | -15.01871 | -52.69691 | 2026-08-18 04:59:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 519dbcb9-3e58-3e6d-a602-6de16865dceb | -14.16033 | -52.91679 | 2026-08-18 04:59:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 11.0 |
| c1b910d1-ed81-3cd0-b2fe-c65a656907ce | -14.35928 | -51.8746 | 2026-08-18 04:59:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c58fa48c-61bd-3382-a55e-5b7f709797c0 | -14.17164 | -52.93389 | 2026-08-18 04:59:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 1aec53f0-9162-3f3a-a079-7d479d444de8 | -14.17789 | -52.91566 | 2026-08-18 04:59:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 2e424cbe-0103-3fdb-ac5b-182280e8f86b | -14.17903 | -52.90819 | 2026-08-18 04:59:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 5e25da4c-1b36-3e42-8cb0-ac92b207476d | -13.2664 | -54.24169 | 2026-08-18 04:59:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 608c2409-48ec-3609-aea5-5952e8845063 | -13.41245 | -54.32721 | 2026-08-18 04:59:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 760094d1-abf4-380c-98f1-290ba1e1a6c9 | -15.38536 | -52.79601 | 2026-08-18 04:59:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8cab3f5c-e3f0-36e4-9d85-f577538be09f | -12.93904 | -56.6458 | 2026-08-18 04:59:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 32b94e5f-bbff-36ac-a673-ee07648254d8 | -12.94251 | -56.6464 | 2026-08-18 04:59:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b2f6ddd4-18ad-3c3e-ae75-d524df5228f9 | -14.10431 | -58.42989 | 2026-08-18 04:59:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 624544fd-e285-3753-97ef-e435aacf2d86 | -13.41129 | -54.35604 | 2026-08-18 04:59:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f5706eb8-f002-3788-9fea-38082b6f5a30 | -17.94849 | -44.4408 | 2026-08-18 04:59:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fea649e6-5872-349f-8a71-2d289367ead5 | -12.23285 | -61.95226 | 2026-08-18 04:59:00 | NOAA-20 | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b0f19a3b-75c8-3cf5-a312-b58bee5865c4 | -13.01557 | -56.58222 | 2026-08-18 04:59:00 | NOAA-20 | LUCAS DO RIO VERDE | MATO GROSSO | Brasil | 5105259 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 83253ef2-e24e-321c-a95c-2271c91bde06 | -13.57484 | -51.78388 | 2026-08-18 04:59:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f69d5565-3299-3d3a-af4d-759f53ea7f83 | -14.81849 | -46.63861 | 2026-08-18 04:59:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 534d3ce4-342b-3390-8f73-9ccbc084d2ea | -14.17843 | -52.93495 | 2026-08-18 04:59:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 13.0 |
| fc8fb28e-89de-3d13-b104-1a7670343fbd | -14.82559 | -46.63575 | 2026-08-18 04:59:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 5d4eec6d-5bbd-3e50-a8b8-6746e07a8596 | -13.666 | -52.19799 | 2026-08-18 04:59:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7e414350-290f-3c8a-938e-f2866173fe35 | -14.25861 | -51.92272 | 2026-08-18 04:59:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 08d8022a-9e16-37d4-a269-8b8da34abe09 | -17.94945 | -44.43157 | 2026-08-18 04:59:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8958c39a-5589-3e05-bf70-f4a299c274b2 | -15.37677 | -52.78278 | 2026-08-18 04:59:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9c1c112f-6af1-39c8-aec3-d69b207c119f | -15.31402 | -56.44075 | 2026-08-18 04:59:00 | NOAA-20 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9db27105-077d-3ada-aa36-5058e7c279bf | -13.41576 | -54.32776 | 2026-08-18 04:59:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b51d4f60-99bf-32c1-850d-b45b28b26541 | -14.17221 | -52.93013 | 2026-08-18 04:59:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 17.0 |


[Clique aqui para ver as próximas entradas](README51.md)
