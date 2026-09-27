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

## Dados Diários - Página 65

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a34d008b-fbe9-39f7-87d4-a71d586155d1 | -10.0162 | -50.1374 | 2026-09-27 16:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 153.4 |
| e51e0441-a29d-397b-b130-b1f429ec3c31 | -12.1938 | -50.3043 | 2026-09-27 16:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 96b73cde-d995-3e2c-bafd-0f3223649228 | -1.3932 | -48.9961 | 2026-09-27 16:00:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 20cabfb2-7f30-3855-bcd8-c68109e0b835 | -11.0991 | -54.0285 | 2026-09-27 16:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 91.4 |
| 70ffeadb-b1c2-3b93-bf7d-79eab3dfeb87 | -1.9489 | -56.3319 | 2026-09-27 16:00:00 | GOES-19 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 176e0325-7f32-3358-9d46-c5acbda296e3 | -12.1027 | -50.0355 | 2026-09-27 16:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 78.6 |
| de8a4bb6-4515-33d9-b127-08d5a336caea | -10.0348 | -50.1569 | 2026-09-27 16:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 102.8 |
| d4d23df5-3326-3361-99a0-f7949a5c46ff | -11.0051 | -49.7109 | 2026-09-27 16:00:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 116.2 |
| 99c64a60-aec0-3325-abfc-a081aec7fba8 | -10.6973 | -50.0456 | 2026-09-27 16:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 88.3 |
| ab0c65b4-78c6-39a7-838d-035ab45f80fb | -12.0352 | -50.709 | 2026-09-27 16:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 82a4a2d0-406c-33c7-9728-d0547c540f99 | -12.1188 | -50.2274 | 2026-09-27 16:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 76.0 |
| e6c2fa3b-2620-3580-9805-33ba17da424f | -11.9619 | -50.5251 | 2026-09-27 16:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 102.9 |
| c0fecf7c-0a72-3d8e-900c-821f7dd9ba5a | -12.1754 | -50.2635 | 2026-09-27 16:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 81.6 |
| bdc1afeb-c25c-30d3-85ce-a361dfb7e49e | -12.0158 | -50.7327 | 2026-09-27 16:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 105.5 |
| 6057e857-6658-32ff-a730-83b989276c14 | -11.7659 | -50.9107 | 2026-09-27 16:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 122.8 |
| 8829dbca-5121-3f8e-a7d0-b6f336068df3 | -12.2894 | -50.2927 | 2026-09-27 16:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 89.0 |
| b2355988-777d-3017-b2cd-9a9df561d513 | -12.3706 | -62.4459 | 2026-09-27 16:10:00 | GOES-19 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 89b55321-1e58-3aff-a300-194182f3c17e | -12.1747 | -50.3066 | 2026-09-27 16:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 91.9 |
| 36c10758-23c9-3eeb-af5d-d54e9bdab5ac | -10.0162 | -50.1374 | 2026-09-27 16:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 150.8 |
| 6270359e-6d76-3c1f-82d8-864528c4d896 | -12.1376 | -50.2466 | 2026-09-27 16:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 101.2 |
| a27b1fb1-c118-32c5-be0c-6e1f43aa63f4 | -12.1938 | -50.3043 | 2026-09-27 16:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 82.4 |
| aab9d6d5-c64e-397d-b8d8-17b14c710bef | 0.4877 | -50.9616 | 2026-09-27 16:10:00 | GOES-19 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 70.3 |
| af06ac7b-921a-3593-97d4-a813a4187c23 | -13.4325 | -57.061 | 2026-09-27 16:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 75.7 |
| d59eea63-d10d-303f-a9c6-7d8748e3b01c | -12.1751 | -50.2851 | 2026-09-27 16:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 97.6 |
| 11d0f403-6caa-328c-93c6-6c65231e6ad6 | -12.7674 | -54.0502 | 2026-09-27 16:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 62.1 |
| e75c2aef-688e-3e9f-8c89-eaeb5c9a7092 | -11.9971 | -50.7135 | 2026-09-27 16:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 104.5 |
| dac285bb-bb34-3291-9a5e-054d7abb02b1 | -11.2859 | -51.3031 | 2026-09-27 16:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 93.0 |
| 3ff52f34-b4b4-369f-96af-211f96b61f60 | -11.978 | -50.7157 | 2026-09-27 16:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 102.4 |
| e206756a-bafb-3126-9269-71dc9f52f96d | -11.8034 | -50.9491 | 2026-09-27 16:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 116.8 |
| cb343e06-b572-31d1-8bb3-26f96cb10d51 | -11.1181 | -51.1091 | 2026-09-27 16:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 143.0 |
| 1f302c84-75a5-3c6c-8ab6-e46e8dbc6a8f | -12.289 | -50.3143 | 2026-09-27 16:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 87.3 |
| ca779836-137e-3564-803a-2759d2055e4a | 2.1266 | -50.8788 | 2026-09-27 16:10:00 | GOES-19 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 77.1 |
| 0b7fecf6-639f-31f6-a1a4-768d03178554 | -15.22 | -48.45 | 2026-09-27 16:15:00 | MSG-03 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 47ccfbe0-2aa8-347d-9f1f-c529c4e1590a | -11.27 | -43.54 | 2026-09-27 16:15:00 | MSG-03 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8258da1a-6186-32cd-bf0c-07c74250fb4c | -12.65 | -47.3 | 2026-09-27 16:15:00 | MSG-03 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 357bcda7-8181-3dca-93f1-cbec9fd54fda | -19.17 | -50.79 | 2026-09-27 16:15:00 | MSG-03 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f4516cdd-703b-3a76-96f7-909c76ce1689 | -10.41 | -53.79 | 2026-09-27 16:15:00 | MSG-03 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fe446767-66cc-307f-825a-b1a9504fc74d | -10.41 | -53.85 | 2026-09-27 16:15:00 | MSG-03 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6207ad85-7341-3ab8-a14f-e8a45cc27293 | -14.56 | -41.37 | 2026-09-27 16:15:00 | MSG-03 | CARAÍBAS | BAHIA | Brasil | 2906899 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| a2bf169f-75b3-3684-ac89-eb066690edec | -15.19 | -48.44 | 2026-09-27 16:15:00 | MSG-03 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| bb09d233-39a3-39c8-8f95-207e692a0a4e | -14.56 | -41.42 | 2026-09-27 16:15:00 | MSG-03 | CARAÍBAS | BAHIA | Brasil | 2906899 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| c881b8f4-083c-3a57-b95a-3689f78e07d8 | -14.47 | -41.39 | 2026-09-27 16:15:00 | MSG-03 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| b830cb20-e6f9-35e7-94a9-d1b7f98e9277 | -12.1754 | -50.2635 | 2026-09-27 16:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 0f76fbcc-2e9e-3060-9707-b0d56f136dec | -11.2853 | -51.3454 | 2026-09-27 16:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 102.1 |
| f23ec2a7-b16b-305c-ba4a-7fa6e945017d | 1.5832 | -56.0417 | 2026-09-27 16:20:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 72.7 |
| e203b1ae-46f6-3f2a-9dcc-30f5c85689c5 | -11.9615 | -50.5465 | 2026-09-27 16:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 348.8 |
| 57a3f254-aadb-334b-83f9-10d4a81864ce | -13.4325 | -57.061 | 2026-09-27 16:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 73.7 |
| b3b5f240-1216-3a86-8458-416a0a8d92b1 | -11.2278 | -51.3938 | 2026-09-27 16:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 99.8 |
| e1cfa9da-c8da-39c9-aa53-290038dc6e2e | -12.156 | -50.2874 | 2026-09-27 16:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 108.7 |
| 6123455b-dcac-3967-87be-e2dd3582b176 | -11.3046 | -51.3222 | 2026-09-27 16:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 102.8 |
| bccddd58-2524-3cdb-9cd1-f5e2b37bc510 | 2.1266 | -50.8788 | 2026-09-27 16:20:00 | GOES-19 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 80.1 |
| 5938b8b6-aac3-32a6-b943-4f02fa57f936 | -12.2508 | -50.3189 | 2026-09-27 16:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 93.7 |
| 6c222ae8-4f6c-37e3-9420-49bc83d2842d | -11.3043 | -51.3434 | 2026-09-27 16:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 105.0 |
| f2a5f8b3-1cc9-3009-a0d0-bf44756e5fa0 | -1.3932 | -48.9961 | 2026-09-27 16:20:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 49b39bc7-cae6-338d-9d96-9540ac057aff | -11.9971 | -50.7135 | 2026-09-27 16:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 101.3 |
| f1abe910-4c19-3c2d-a92c-550c343e6007 | -12.1935 | -50.3259 | 2026-09-27 16:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 98.2 |
| 7fee3e1f-2c79-3aa6-8d72-5ed4a20af101 | -12.0158 | -50.7327 | 2026-09-27 16:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 111.8 |
| 422e84de-d7b4-3ca5-808c-2a447c18e19b | -12.288 | -50.3789 | 2026-09-27 16:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 131.3 |
| 319d61ca-4222-3cbf-9b73-e4e51d933fbc | 0.4877 | -50.9616 | 2026-09-27 16:20:00 | GOES-19 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 4d433eac-f71e-31d9-ba1e-115d557e0c25 | 2.1266 | -50.8788 | 2026-09-27 16:30:00 | GOES-19 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 83.4 |
| 4d019b87-c30f-306c-8f55-caeeb03bf6eb | -11.1524 | -50.0172 | 2026-09-27 16:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 90.1 |
| a235bd73-1050-3c6c-a8ce-0d2d6066f6ec | -12.1935 | -50.3259 | 2026-09-27 16:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 101.6 |
| 1c4ebb00-169d-39b0-8be0-9c41e996fb3a | -12.2502 | -50.362 | 2026-09-27 16:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 98.3 |
| 107b4bbb-7e48-36fb-952d-303b1c781767 | -11.247 | -51.3706 | 2026-09-27 16:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 128.7 |
| 8370c5a6-373c-307c-aefc-92ba324538cb | -12.1751 | -50.2851 | 2026-09-27 16:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 101.9 |
| 76876983-156c-3133-a25f-c195fe653484 | -12.0158 | -50.7327 | 2026-09-27 16:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 120.5 |
| 6cc05789-6f50-3b96-975b-aac404b12b3f | -11.9971 | -50.7135 | 2026-09-27 16:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 107.0 |
| 29f3fd7b-c4e1-3221-a5b6-e890e544df72 | -12.2498 | -50.3835 | 2026-09-27 16:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 98.4 |
| edb5c9b5-c662-357e-a403-c51b9f4d7f7b | -12.1376 | -50.2466 | 2026-09-27 16:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 106.5 |
| 15db0318-9ffc-376e-9dd1-250cec470838 | -11.2281 | -51.3727 | 2026-09-27 16:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 122.1 |
| 73a9ddeb-6a05-34a9-8b65-0cca60ce3e2f | -11.2091 | -51.3746 | 2026-09-27 16:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 107.2 |
| 07be3d58-4db5-383f-b5e7-2b8672dbafd0 | -12.1754 | -50.2635 | 2026-09-27 16:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 5b985fff-c42b-3194-92ea-7d85d2f492c2 | 1.6017 | -55.884 | 2026-09-27 16:30:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 74.9 |
| ffe72757-3b44-3841-8a74-64fc42ecdd16 | -11.2091 | -51.3746 | 2026-09-27 16:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 114.1 |
| 7091e0b7-6826-3ddd-b119-7f9212329e0e | -11.4162 | -45.3486 | 2026-09-27 16:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 139.3 |
| 79f25578-1928-34ab-803b-3d031de12236 | -11.2853 | -51.3454 | 2026-09-27 16:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 103.4 |
| 2eaaeeed-3ec2-3553-92cd-188f98de13ca | -12.2502 | -50.362 | 2026-09-27 16:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 95.5 |
| 48637d36-7ea5-3699-8a41-97c5f140f5ac | 2.1266 | -50.8788 | 2026-09-27 16:40:00 | GOES-19 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 85.6 |
| 29e4ff9a-404a-35b2-96a3-23ca2efd99a4 | -11.3043 | -51.3434 | 2026-09-27 16:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 113.4 |
| 2197eab4-cf26-3344-8994-5539f5dba612 | -12.1938 | -50.3043 | 2026-09-27 16:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 86.9 |
| d19f365b-69a2-3d55-bc65-204b580e1f12 | -12.2123 | -50.3451 | 2026-09-27 16:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 106.9 |
| 22fb4099-0b60-396c-aced-fdfce5493578 | -12.1553 | -50.3305 | 2026-09-27 16:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 85.4 |
| a7f58024-9a66-3294-8f21-75b555a50661 | -11.2281 | -51.3727 | 2026-09-27 16:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 124.4 |
| 0ec8648e-fd2e-398c-a703-c1d74bcce132 | -11.2091 | -51.3746 | 2026-09-27 16:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 112.1 |
| de599ff9-532b-3f4f-bea4-f35ca4bb30dc | -11.2859 | -51.3031 | 2026-09-27 16:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 102.7 |
| df7d8d75-b296-3181-b91a-436dc822efcf | -12.1112 | -50.7215 | 2026-09-27 16:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 114.4 |
| c2c17fd6-fcf5-3e0c-b42c-83ac6bf3f207 | -10.0162 | -50.1374 | 2026-09-27 16:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 165.0 |
| b2aceb87-abfb-3e3a-9b83-236f1e1bfc50 | -12.2123 | -50.3451 | 2026-09-27 16:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 111.1 |
| 941e35d1-4e5f-375f-a7dc-061a83abd0e6 | -11.2853 | -51.3454 | 2026-09-27 16:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 114.0 |
| c105a689-d5bc-370b-880a-af42e54d1c64 | -11.3043 | -51.3434 | 2026-09-27 16:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 115.2 |
| bcceb08c-8493-3d06-ba50-3324b18e8dfb | -11.5818 | -50.5047 | 2026-09-27 16:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 189.1 |
| 6a64c47b-f3be-367b-b952-34ddb281e28c | -12.3706 | -62.4459 | 2026-09-27 16:50:00 | GOES-19 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 48.1 |
| 56bdec86-6ba6-3339-a278-91969935ebae | -12.1112 | -50.7215 | 2026-09-27 17:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 116.6 |
| c0f5ab6c-9016-34da-aa4a-8bf550ebc309 | -11.2844 | -51.409 | 2026-09-27 17:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 115.9 |
| 884f3fb2-f470-30e1-9085-00c128a9a338 | -12.3706 | -62.4459 | 2026-09-27 17:00:00 | GOES-19 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 726aa051-c6dd-3918-8ef9-17cb80142f80 | -12.1938 | -50.3043 | 2026-09-27 17:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 0f59caf5-dc57-322f-a4c7-e11fcd8a3ecf | -12.156 | -50.2874 | 2026-09-27 17:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 119.9 |
| 365d17a1-1484-3e49-9312-dcb87c3e4e4a | -12.1553 | -50.3305 | 2026-09-27 17:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 84.5 |
| e35ae929-b94c-3c9a-948a-63b4b796739b | -11.5818 | -50.5047 | 2026-09-27 17:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 185.3 |
| 0e72e871-2325-354b-b25a-d6380907dc75 | -12.3896 | -62.4255 | 2026-09-27 17:00:00 | GOES-19 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 42.5 |


[Clique aqui para ver as próximas entradas](README66.md)
