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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e294cbe9-5bf4-3eba-bc0a-d1831eae016b | -12.4759 | -54.183399 | 2026-08-19 01:23:00 | METOP-C | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1abbad8e-5f90-3402-bae0-240c5072bc13 | -6.8855 | -56.429699 | 2026-08-19 01:23:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 490e4f5c-a033-3eba-93d4-cc588aa16abc | -6.754 | -59.154999 | 2026-08-19 01:23:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 23a4526a-ce7f-380d-a284-92f7ade1aa62 | -8.5686 | -54.779701 | 2026-08-19 01:23:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bd2c6006-86a6-322f-aa3b-2b7e91793089 | -6.8992 | -56.444099 | 2026-08-19 01:23:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f91b3b73-6016-378d-8070-168f984c64ed | -6.8739 | -59.0481 | 2026-08-19 01:23:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| acc09cdb-d4ab-3868-9d5e-b6ef5418b8a2 | -15.288 | -56.5037 | 2026-08-19 01:23:00 | METOP-C | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| da90555e-e410-38c6-b844-e9d266cee39b | -6.8448 | -59.011002 | 2026-08-19 01:23:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0abee40d-f251-3805-909c-3f9f18bcc419 | -7.0826 | -56.653801 | 2026-08-19 01:23:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 897c1e5d-ea04-340d-bfb4-278747dabedb | -6.8578 | -59.022598 | 2026-08-19 01:23:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c5ecd04f-182d-3dc2-a0da-ba1e2c7d0816 | -6.1082 | -57.874298 | 2026-08-19 01:23:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7d5de1d5-c874-35f5-a995-a1cca8e4ac34 | -8.5322 | -54.757099 | 2026-08-19 01:23:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0298f89c-3ab1-34d8-a342-03d14e46165f | -8.5396 | -54.7449 | 2026-08-19 01:23:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d6d4df66-0e99-339f-a1ce-c5f87bc2c535 | -6.4557 | -52.7425 | 2026-08-19 01:23:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 41216dba-e7d1-39e7-b7ce-9ed91cac6d6b | -6.8835 | -56.421299 | 2026-08-19 01:23:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 43ab0fa6-e154-36b4-ad58-ca24d6748d48 | -11.2294 | -55.061501 | 2026-08-19 01:23:00 | METOP-C | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 60723828-8f13-36d5-8ef3-e883a3a4fabd | -19.0655 | -57.349499 | 2026-08-19 01:23:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| eaf79c7c-bc6a-3b86-bf63-44f289569ee0 | -11.2336 | -55.079201 | 2026-08-19 01:23:00 | METOP-C | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 79c1d92b-9840-38d9-8dca-955b5244c420 | -6.61 | -58.393501 | 2026-08-19 01:23:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d0c125e8-68cc-3b35-98ba-7647c50b23b2 | -7.4378 | -59.802299 | 2026-08-19 01:23:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5dd15d09-7ae4-3e13-97b8-6590884026a2 | -10.1111 | -54.279701 | 2026-08-19 01:23:00 | METOP-C | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7b557e68-95a3-3a7f-9f5f-c49348a50817 | -6.7922 | -59.457298 | 2026-08-19 01:23:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 798b90f4-b882-3d5e-8e93-000cdaa93076 | -5.4948 | -60.1437 | 2026-08-19 01:23:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a5b5e769-d4a4-3ffa-b5d1-2234e3db06a5 | -15.3171 | -56.4505 | 2026-08-19 01:23:00 | METOP-C | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f1cf2b19-2389-3161-bc07-7688a5ad3fdb | -9.0963 | -50.8097 | 2026-08-19 01:23:00 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3049671c-3412-364e-b284-990a2beb0f8e | -6.7468 | -59.033199 | 2026-08-19 01:23:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 75fd785e-990d-3595-afa2-ec27cc89fbf4 | -6.6323 | -59.073601 | 2026-08-19 01:23:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3c6f4d30-02b3-3b08-a350-24acfcacf01e | -3.0982 | -61.209099 | 2026-08-19 01:23:00 | METOP-C | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 78c001c5-beb5-3066-bbdf-07d4db76c4a7 | -9.4272 | -60.448898 | 2026-08-19 01:23:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6925125c-d406-3bc8-b83a-6d717123615c | -11.2035 | -54.0112 | 2026-08-19 01:23:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| de07ead1-dd35-3897-8314-0b334fa214ba | -6.1082 | -57.740898 | 2026-08-19 01:23:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8be38b6e-41f1-3158-bc73-c591ff1dd5ea | -7.4331 | -59.7817 | 2026-08-19 01:23:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6da147ad-3822-3103-a49b-f2916c7f8d18 | -3.1049 | -61.193199 | 2026-08-19 01:23:00 | METOP-C | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 68c97300-ebcb-3196-987c-cf0958e86e6d | -6.0273 | -50.216999 | 2026-08-19 01:23:00 | METOP-C | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| afe5eb97-0539-311c-aa36-5e10da25b74c | -14.042 | -53.688 | 2026-08-19 01:23:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 200dfb89-7649-3cfc-a59f-2aa6f5e7e9b5 | -6.8417 | -58.997101 | 2026-08-19 01:23:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8f0254fc-0c5c-35bd-8ad4-067791936843 | -15.2863 | -56.496399 | 2026-08-19 01:23:00 | METOP-C | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e5bf323d-8fd3-3867-ba13-f0e5b190ed02 | -15.5874 | -49.844898 | 2026-08-19 01:23:00 | METOP-C | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 276a6c9c-fdc6-3715-a894-12e10bbc4417 | -9.4288 | -60.456001 | 2026-08-19 01:23:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c6872773-939a-34b9-a901-129310edcd8e | -6.0097 | -57.8498 | 2026-08-19 01:23:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a76ab0e3-bce1-330b-9717-014079fea8e0 | -9.3891 | -60.555 | 2026-08-19 01:23:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 28c0c989-d215-3437-8608-b0dc9d15af44 | -6.0989 | -57.9231 | 2026-08-19 01:23:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 52b4a5fc-e13f-3843-888b-b9c853b47149 | -7.5674 | -55.559101 | 2026-08-19 01:23:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 851c8b89-eb02-3539-a33e-d65d66af1b2e | -9.4256 | -60.4417 | 2026-08-19 01:23:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fbdba9de-7439-3048-ac23-6c52259ad4fe | -6.0874 | -57.917999 | 2026-08-19 01:23:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 093d6297-c2f2-33e1-b95d-2ca6794f661b | -10.1136 | -54.2897 | 2026-08-19 01:23:00 | METOP-C | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 401dc351-5099-3308-bffa-0091e77ed656 | -9.0664 | -50.854599 | 2026-08-19 01:23:00 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 489c36d9-e63f-32be-a58f-a6024ae75f50 | -9.4037 | -60.574402 | 2026-08-19 01:23:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f6e0db97-e303-3d56-b3de-32d73afee8c9 | -6.861 | -59.036499 | 2026-08-19 01:23:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| dd038aad-0263-3650-b592-2a76bf0ef8d9 | -15.2766 | -56.498699 | 2026-08-19 01:23:00 | METOP-C | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 40ec8cf9-6ccf-3a2d-8f6d-4168a4746b27 | -9.4119 | -60.564999 | 2026-08-19 01:23:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 32e09296-a084-38a0-b15e-fd6fd9866ac2 | -6.8885 | -59.066601 | 2026-08-19 01:23:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8aae1bfa-d1ae-3384-8629-9dc6c02a9aa5 | -15.2847 | -56.489101 | 2026-08-19 01:23:00 | METOP-C | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f1cdaad6-0dfd-3363-94b6-7c917574d02f | -6.8515 | -58.9949 | 2026-08-19 01:23:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 20f2eec2-1d14-3ed1-8228-0cdb495db2dd | -8.5834 | -54.755299 | 2026-08-19 01:23:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 08aed401-cc3d-3084-bc07-665032752930 | -5.4917 | -60.1301 | 2026-08-19 01:23:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 98696905-3ed8-3fae-9b15-c59355ccfb7a | -8.5443 | -54.764599 | 2026-08-19 01:23:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6ab8aa13-3409-3083-b21c-aabb75cdc5d8 | -19.7735 | -57.9613 | 2026-08-19 01:23:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 57ec94cc-519f-399d-ad00-3d1024122a42 | -6.0148 | -57.872101 | 2026-08-19 01:23:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 88d4661d-6733-3d48-9f6d-d7e783e56d31 | -8.9485 | -60.517899 | 2026-08-19 01:23:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e3705bee-4dea-3f11-ba54-2f7b0daaa551 | -8.5541 | -54.762299 | 2026-08-19 01:23:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0b02c617-6f44-32e3-b55c-c8b369bf3ad5 | -6.6829 | -59.0695 | 2026-08-19 01:23:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ae971a21-5df6-33ce-857a-10dcedf81fb9 | -7.8161 | -56.5686 | 2026-08-19 01:23:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 59ac9a33-27f3-3a2e-a3c6-1827fd48d88d | -6.005 | -57.874401 | 2026-08-19 01:23:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 30102930-3946-35b8-8f7a-b43771b505ee | -6.7654 | -59.159698 | 2026-08-19 01:23:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 078b2d89-9319-3719-95bd-7e513b80dd67 | -6.892 | -59.0368 | 2026-08-19 01:23:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 69a37f7f-747f-3dc3-8cc1-97ac18694d9d | -6.6983 | -58.956699 | 2026-08-19 01:23:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6bf81ee2-897c-33db-a09a-c4bc19e44151 | -6.8853 | -59.052799 | 2026-08-19 01:23:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5872640e-40ee-36fd-8fcc-680f097f70cf | -8.5467 | -54.774502 | 2026-08-19 01:23:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 490bd31e-6ee6-3a5d-84c8-a26cd358199d | -8.9564 | -60.553501 | 2026-08-19 01:23:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b502ccd9-9aa3-3af0-a166-dcc797cfb4e1 | -19.068701 | -57.363998 | 2026-08-19 01:23:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 729c8b58-9627-3fbe-8924-cbb919c7c36b | -6.1323 | -57.7117 | 2026-08-19 01:23:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cbb3bc0d-86a2-3cd0-9903-7e0b9786a4ee | -6.3484 | -54.902901 | 2026-08-19 01:23:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 55d4fab9-c2ee-3dec-bf77-d7c758c0a1c0 | -9.4053 | -60.5816 | 2026-08-19 01:23:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7d1a689b-cd2e-39b1-b8f2-950ce308a7c2 | -6.0131 | -57.8647 | 2026-08-19 01:23:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 01668b07-20af-3500-844c-c1f120696a40 | -7.5446 | -55.593399 | 2026-08-19 01:23:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fba0b644-8dce-39f8-b257-26308b4fac1c | -6.1457 | -57.857899 | 2026-08-19 01:23:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8873d714-8ec1-30bf-8793-cf0ca050d9e6 | -6.6339 | -59.080502 | 2026-08-19 01:23:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 53bef212-de5b-3306-aae3-3924b4b72e96 | -4.285 | -60.851898 | 2026-08-19 01:23:00 | METOP-C | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 18b7307e-76c7-36d5-a35d-c26c7efa7d33 | -6.8464 | -59.017899 | 2026-08-19 01:23:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c2db2daa-9c34-3a58-b76e-a5399b9921bb | -8.5908 | -54.743099 | 2026-08-19 01:23:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f570b4e7-1365-33ed-bd15-4e633e0f81a8 | -8.5349 | -54.725101 | 2026-08-19 01:23:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 81ecd76d-ae2a-3e07-a234-025f92c31edb | -8.5591 | -54.7402 | 2026-08-19 01:23:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d8782a98-f1c2-3a05-9dea-00064ec75420 | -19.054199 | -57.344601 | 2026-08-19 01:23:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| cecee02a-b8ad-3030-b58f-9b10a86da948 | -6.8837 | -59.045898 | 2026-08-19 01:23:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 51041ccc-a94e-3f2a-b48d-67cae2c2f1ae | -6.8822 | -59.039001 | 2026-08-19 01:23:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ca4bc58b-ce82-31a4-88e1-8b58f0c3a4ad | -7.9019 | -61.732498 | 2026-08-19 01:23:00 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5cacbdc1-1804-3789-a2f3-0fa11170a2d4 | -8.5046 | -54.857201 | 2026-08-19 01:23:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3238889f-827d-3e12-ba31-4b3103bc3bea | -7.0526 | -59.831001 | 2026-08-19 01:23:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a96e6470-1250-3e2e-b49c-02cb99af8c12 | -9.0187 | -60.5098 | 2026-08-19 01:23:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c23522b4-b6e5-3283-912d-2a63fee0d216 | -6.0857 | -57.910599 | 2026-08-19 01:23:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f8bb887c-5719-3b73-a396-0f36283cfa11 | -6.8385 | -56.449501 | 2026-08-19 01:23:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9e21c3be-566d-33e3-b3a0-9929d42036ef | -8.542 | -54.754799 | 2026-08-19 01:23:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 347039c3-3c30-3388-b436-7560f9164061 | -8.5712 | -54.747799 | 2026-08-19 01:23:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6b32c420-9c9a-3573-8756-7833805067a1 | -10.1268 | -52.116699 | 2026-08-19 01:23:00 | METOP-C | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 877832f1-938b-3307-a6bc-9c67d9387cb8 | -6.5803 | -51.117699 | 2026-08-19 01:23:00 | METOP-C | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8aa76c16-964c-393b-8a0e-e1eb66033abe | -7.1103 | -59.767601 | 2026-08-19 01:23:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4e2b1535-ef71-35d1-be7c-a7c90e8170d9 | -9.3973 | -60.5457 | 2026-08-19 01:23:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 31665ebf-0410-3a1c-805f-0418ffd018ec | -6.8724 | -59.041199 | 2026-08-19 01:23:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 35662dee-7f42-3aa3-bd75-24acca365071 | -6.8708 | -59.034302 | 2026-08-19 01:23:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README14.md)
