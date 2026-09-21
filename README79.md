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

## Dados Diários - Página 79

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 189bd889-498a-31e9-babf-07edc0a94bb3 | -9.82055 | -48.30791 | 2026-09-21 05:06:00 | NOAA-21 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 87191745-4d22-3310-9a44-322f5506d311 | -10.3653 | -50.21778 | 2026-09-21 05:06:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 74353fc4-59d5-3874-9df4-bbafaa5d99f7 | -10.79628 | -50.82076 | 2026-09-21 05:06:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c9dee710-bedd-3a88-8e4b-67999aef98b7 | -7.33569 | -55.61525 | 2026-09-21 05:06:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| abf0541a-2fea-35b2-b277-03c7a84a787d | -10.86915 | -53.96096 | 2026-09-21 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 773ee565-b428-38ad-8224-e85295de3a2d | -10.70329 | -50.77571 | 2026-09-21 05:06:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| df191bf1-4006-3c9c-9129-402549ade43e | -11.71273 | -54.56743 | 2026-09-21 05:06:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b42c6f3a-1197-32cc-9a15-f5f0b0e905b5 | -7.57061 | -57.67527 | 2026-09-21 05:06:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 7d2ed02d-75a1-3630-8b2f-7486fdf5fadd | -8.77737 | -44.2823 | 2026-09-21 05:06:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 998acc65-a4d4-3568-9b58-ebac215f9630 | -7.33623 | -55.61177 | 2026-09-21 05:06:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5fa40b21-5eec-37c3-acda-297a812ae444 | -10.53999 | -57.44434 | 2026-09-21 05:06:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4c816f9f-f0ed-3384-b9ed-553b6cc8c900 | -10.71195 | -50.77697 | 2026-09-21 05:06:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cb5fed43-9965-33cd-b7c6-3d98f84b3674 | -8.06582 | -50.97004 | 2026-09-21 05:06:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8fada401-e791-30fd-88cd-ec4b6a96a75a | -11.05295 | -54.90934 | 2026-09-21 05:06:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6d4cfc64-900d-35a7-b673-c712fe87f257 | -7.5836 | -57.69254 | 2026-09-21 05:06:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 6248c30a-33dc-3234-b1b6-6251cce07f93 | -10.48145 | -50.29098 | 2026-09-21 05:06:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 21.1 |
| 9f5c52cd-2403-3484-8ec2-2ffacf1bda8a | -6.795 | -58.78972 | 2026-09-21 05:06:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 40bea716-1c71-3f89-b003-d047d442c424 | -13.24852 | -51.80183 | 2026-09-21 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e1cab4ab-e2b6-3ead-97ac-4283ec6f53fc | -13.26686 | -51.79237 | 2026-09-21 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bcb2c752-f2e9-3912-94d8-81885284df61 | -11.10028 | -48.29275 | 2026-09-21 05:06:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e7987959-e567-3260-96c5-7be719c7c6f1 | -7.62042 | -57.61352 | 2026-09-21 05:06:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 3e1e85ec-649e-3630-a481-e69c19ac62c9 | -10.53204 | -54.502 | 2026-09-21 05:06:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a3d854c1-983d-3c49-b107-d439418bf019 | -9.23704 | -46.177 | 2026-09-21 05:06:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 16ca66d7-d031-3d9b-9562-17df5e1b2c98 | -12.89783 | -51.00877 | 2026-09-21 05:06:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| da8e2399-e3b1-351e-96c0-ff33c179ab99 | -10.12405 | -48.43927 | 2026-09-21 05:06:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f83ad7a4-363f-3f5b-a348-71b48008669e | -6.7124 | -59.45762 | 2026-09-21 05:06:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4fb4efa5-4b26-3571-acfd-83b3cd2088e9 | -9.68053 | -54.33895 | 2026-09-21 05:06:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 609e1ea5-d811-33db-8363-989005e52a2c | -7.32303 | -55.21221 | 2026-09-21 05:06:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 062bbe5d-4ba1-38ed-b959-1618eb556e06 | -12.11047 | -47.04247 | 2026-09-21 05:06:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c97b1785-0315-3289-a55f-e116a44c45a0 | -7.59776 | -57.66891 | 2026-09-21 05:06:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 59054dbf-17b4-3623-bb80-2dc5e622ff08 | -11.01493 | -54.14758 | 2026-09-21 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b4e3caf8-adb4-35c4-9551-5f76003493b4 | -10.45708 | -50.26921 | 2026-09-21 05:06:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 18f836d8-5c0d-37ec-af2b-1ed7f0f6c214 | -11.83696 | -47.61822 | 2026-09-21 05:06:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 57f3faba-1263-3695-9a45-f4052e501259 | -11.22999 | -54.08574 | 2026-09-21 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dba9786e-5fd0-3813-9d81-2092d0b76f0b | -7.57454 | -57.6722 | 2026-09-21 05:06:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 71da1138-549f-3d93-83c6-2531da621354 | -8.14486 | -54.81137 | 2026-09-21 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3668f8c0-ee93-328b-a1f9-7a639a6f4792 | -6.68492 | -58.45532 | 2026-09-21 05:06:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3f000a57-5d31-383f-86f8-3568d2f3cec7 | -13.93112 | -47.84691 | 2026-09-21 05:06:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7979fb75-a950-38e6-be52-c835a7dc2ea9 | -10.46988 | -50.27562 | 2026-09-21 05:06:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 32fe10f2-8ef2-357a-a30a-84bdb9a03f57 | -11.77578 | -54.53484 | 2026-09-21 05:06:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4a130e4f-deff-397e-88fc-a02f7a7dc451 | -10.46724 | -51.33348 | 2026-09-21 05:06:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 23d50244-5a6c-3e90-8d3a-20ca487b18bb | -6.461 | -59.97746 | 2026-09-21 05:06:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 19c1fc9d-eacb-3eb7-a0b3-332c276be98b | -9.03689 | -61.64742 | 2026-09-21 05:06:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4bb75dc7-3397-3872-bcd8-e22d1ade7aea | -11.11409 | -54.0107 | 2026-09-21 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 33fd65e6-5686-3619-902d-b76210180ed1 | -11.04721 | -54.90073 | 2026-09-21 05:06:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 60f106da-0b01-3ce9-b75b-bef662e82b1b | -10.45633 | -61.31162 | 2026-09-21 05:06:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 09f3d22d-0124-32cc-9613-f5f1ffef3666 | -10.87296 | -54.07775 | 2026-09-21 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 27ce7a60-d63e-3baf-8625-8eb085d42820 | -8.18457 | -54.7317 | 2026-09-21 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3bac4515-b9c3-374d-899e-cf1070165875 | -10.11396 | -48.43785 | 2026-09-21 05:06:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 40a928c8-dae0-3bb6-8fc5-69cec76d33e8 | -7.32861 | -55.22032 | 2026-09-21 05:06:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 124a1459-d027-36d9-98ee-25a25a8def68 | -9.98218 | -50.26106 | 2026-09-21 05:06:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 0d4d788c-e1ff-3c5e-97ba-0a9308ff423e | -7.58256 | -57.67757 | 2026-09-21 05:06:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| ca822d89-2fb9-308f-8219-85ab2c2d3603 | -10.09652 | -48.34134 | 2026-09-21 05:06:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2bd4cb36-6a10-31f1-9580-724ed501365e | -10.88126 | -54.09575 | 2026-09-21 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0e9271ea-0e04-3911-b4ed-1b1a8310cb12 | -9.82912 | -48.31346 | 2026-09-21 05:06:00 | NOAA-21 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 26a0fafc-7476-36df-94ab-8fcee2803ad5 | -11.13197 | -54.01347 | 2026-09-21 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5c990e95-d184-3637-b93a-034526b49002 | -10.21989 | -59.40114 | 2026-09-21 05:06:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d2f37c4f-1217-3a2b-b9bb-0075b1b73f6c | -11.73794 | -54.51817 | 2026-09-21 05:06:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 74115f80-42c0-3651-bfd1-eb6995e6746b | -6.72263 | -63.12674 | 2026-09-21 05:06:00 | NOAA-21 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 3a3341e1-e45d-3d38-895e-145dc5adae0e | -8.7767 | -44.28772 | 2026-09-21 05:06:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 1b21ecc9-78e0-30b2-a55e-cbe3ad01a7a7 | -13.27208 | -51.7526 | 2026-09-21 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6032dae4-cbd2-36d5-8e32-0a28b008edd6 | -12.80352 | -54.06256 | 2026-09-21 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b64ff2d9-da4a-3a2a-a010-ad18af66855c | -11.02323 | -54.14052 | 2026-09-21 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9e355e58-120a-3628-a5e5-104fc187f11d | -11.25425 | -54.144 | 2026-09-21 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 68a6dcaf-2693-3f82-8273-d7eb77d637ff | -8.17456 | -54.77496 | 2026-09-21 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a4700435-becb-39ad-8466-a328ec5254d8 | -13.26109 | -51.80375 | 2026-09-21 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a82981c2-5941-371d-a0c1-ca453d1f94a7 | -10.88781 | -53.97485 | 2026-09-21 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bb1bf58e-97fd-347a-8e5b-a84b80b24084 | -7.33194 | -55.22083 | 2026-09-21 05:06:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a5f153ab-7690-3b33-be19-7976739d8d6a | -10.21924 | -59.4051 | 2026-09-21 05:06:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ec5078a0-d157-3d22-ad8b-ecc48a312922 | -6.4497 | -59.97562 | 2026-09-21 05:06:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 53221aa3-f9a8-3971-8a0e-15a2f30d1619 | -10.87178 | -54.08596 | 2026-09-21 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1d1c96ab-7469-3a8c-93e1-03dd2b166af2 | -6.43392 | -59.97514 | 2026-09-21 05:06:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0553f8d9-c810-3b7e-9eab-86a0ebcce6e7 | -9.97774 | -50.26042 | 2026-09-21 05:06:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 070c1d4d-7d14-3759-bc8a-5a9d2a1e6cc4 | -6.75031 | -59.06466 | 2026-09-21 05:06:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4fe48089-3a4d-3521-a21a-842b0a83bb27 | -10.87448 | -56.23568 | 2026-09-21 05:06:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 7a44976c-a1be-3ab6-b300-486bda035e38 | -10.67616 | -48.71201 | 2026-09-21 05:06:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| c0a2b171-2ebc-3261-aa3f-fe32673cca71 | -10.41779 | -50.23445 | 2026-09-21 05:06:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| afa43af7-3aac-3814-8c54-2fde05b62793 | -8.18347 | -54.73898 | 2026-09-21 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4aa3c41a-1d78-3039-a45c-fc8ff5022ee3 | -11.7484 | -54.56878 | 2026-09-21 05:06:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ce5cb7dc-159d-35c1-babb-0f48174690ec | -10.14954 | -47.68378 | 2026-09-21 05:06:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4dde2c16-af8a-37b5-84f7-2e267d4417f9 | -6.82964 | -58.98112 | 2026-09-21 05:06:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 27f81e30-3773-3835-8b91-7e99c097ae0c | -11.05094 | -46.57091 | 2026-09-21 05:06:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 098bdcfd-a512-3bfc-915b-eaf30e67cdb6 | -7.57739 | -57.6542 | 2026-09-21 05:06:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 24dbb2f4-4139-3151-8128-878b79def0ab | -9.30496 | -62.31089 | 2026-09-21 05:06:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5c12e231-6cf1-3ded-92d3-e39b85ab6a6f | -10.72973 | -50.71077 | 2026-09-21 05:06:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 00db480b-58e7-3083-8187-842103e36146 | -8.08947 | -55.33428 | 2026-09-21 05:06:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 57ec7ae1-e69b-3946-b42b-51686bbc8602 | -11.02913 | -54.14972 | 2026-09-21 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8a425ac3-6397-3f0f-9a63-779582b6d596 | -9.82432 | -48.31072 | 2026-09-21 05:06:00 | NOAA-21 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3b3efeba-d95e-3c75-95c5-e5a8923a56f7 | -9.67764 | -54.33455 | 2026-09-21 05:06:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e4bd7f6b-c36c-3412-9b43-31a62b48db35 | -10.82732 | -50.78679 | 2026-09-21 05:06:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8bdf572d-2af7-3b67-aa99-dc37c56c3521 | -9.46311 | -54.92469 | 2026-09-21 05:06:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6d29ef02-7972-38bc-b355-6a6508266a81 | -9.54981 | -66.01511 | 2026-09-21 05:06:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ab3810b1-6a5b-3521-9e5d-42bf9cc90599 | -9.45619 | -45.3971 | 2026-09-21 05:06:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 27.5 |
| ed11b9f7-a03e-3329-8276-d8682b77cf2e | -10.90568 | -53.97761 | 2026-09-21 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e0630016-8069-339a-8754-b934671ddadc | -11.27988 | -54.11842 | 2026-09-21 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b1b7a14f-a494-3977-abd1-6eb11fd6c18f | -10.4776 | -45.10491 | 2026-09-21 05:06:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 27268a59-95cd-3113-ba05-2e5bc4c3e6a3 | -12.4192 | -47.0361 | 2026-09-21 05:06:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 61c9599c-596c-32aa-b2b1-ed6fb4e6c88a | -9.97744 | -46.64056 | 2026-09-21 05:06:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d3582526-2a88-3992-a7d0-909d2c313d79 | -11.34192 | -51.353 | 2026-09-21 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8f4b594e-4f02-368c-848c-1b2e3580387f | -13.94274 | -47.84311 | 2026-09-21 05:06:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README80.md)
