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

## Dados Diários - Página 58

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 19688154-8ec4-334d-b185-f7a6d7778f11 | -7.3406 | -55.67556 | 2026-08-21 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8311f39f-0aa7-399d-820a-dff9ddffdd47 | -6.57387 | -58.9654 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6a2e8a28-cc11-37d9-98b0-f85fe1fe6ee3 | -15.16235 | -48.78323 | 2026-08-21 05:23:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c3a02f8e-0473-3b27-aee3-2551fc6c5a7d | -6.57991 | -58.99236 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e5f56238-18ff-3f37-8135-5f22145b0158 | -13.40619 | -54.37431 | 2026-08-21 05:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0bd06d95-ad69-36b5-903d-f2973367b96e | -7.06378 | -59.96648 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 50e1f028-9c3f-3bb8-aa82-9d4e770dff39 | -13.74531 | -51.85954 | 2026-08-21 05:23:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 8bacac74-f556-36a1-a3d3-d141017f6e9f | -8.15951 | -46.73034 | 2026-08-21 05:23:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 84c9519f-2a3b-3e9f-a935-6d40bfb4ee09 | -6.98476 | -55.6725 | 2026-08-21 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9ae549fc-90fd-3100-8f24-6139447d0d9d | -6.81999 | -59.40557 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| fb0359f7-e4b0-3c9d-8c11-9dcac45e4966 | -6.16208 | -55.44262 | 2026-08-21 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 337a1b1d-1bb8-3958-afcf-1ab8871eb7b4 | -6.87296 | -43.74529 | 2026-08-21 05:23:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 8cb97e8c-64c9-3e34-b533-99aab577493f | -13.40099 | -54.366 | 2026-08-21 05:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 0a0f715f-3b53-3e4d-87c7-0366b41ebb85 | -8.11173 | -50.0413 | 2026-08-21 05:23:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 73bb0549-6f05-35b5-b91d-5271879c2117 | -6.82865 | -59.39554 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 03b605f7-a9c5-37da-861a-9655cc6bc3de | -6.89762 | -55.72025 | 2026-08-21 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| aa55778a-c086-3c8b-96ca-bb3950839da4 | -6.00341 | -57.85994 | 2026-08-21 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 23f94628-783b-315f-90ba-2a3900c7f308 | -14.57398 | -52.99102 | 2026-08-21 05:23:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5198ba72-d127-38ce-9008-65fbc00a4241 | -6.38813 | -54.95483 | 2026-08-21 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5214a5d5-d5cd-3446-a6c1-23b8b532deaf | -14.02658 | -58.86952 | 2026-08-21 05:23:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b3c33c55-c298-3810-a72e-34aca207fcf0 | -5.80873 | -55.72196 | 2026-08-21 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eb5c6159-a698-3517-a4e5-6cd0801dd6c6 | -5.86565 | -57.66395 | 2026-08-21 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9e86f415-b0da-32b0-b72b-95d83f5bdba2 | -6.89104 | -59.44373 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1515360d-c1b6-3d43-8c05-b5c92ef49844 | -6.69647 | -58.94024 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0822d37b-70f5-3989-a5f4-6de3d82e9ccb | -7.60669 | -60.97065 | 2026-08-21 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1bb71cbd-a9d6-32bc-91eb-a18964fdea2d | -6.86787 | -59.41332 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e339a32c-68c0-3744-9a30-5f7d5f7b19a7 | -6.41993 | -54.93559 | 2026-08-21 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0b1b6a0b-9848-3adb-9acf-4c205be686e2 | -8.09983 | -51.67093 | 2026-08-21 05:23:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b5ebd224-0542-37b6-b51a-47b73c8a0f47 | -3.26731 | -49.52252 | 2026-08-21 05:23:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 40e58907-8a8e-381a-b079-97a123de4f80 | -6.43917 | -54.9494 | 2026-08-21 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c1baa093-dd27-33bd-8478-79b290a866b8 | -6.69367 | -58.9361 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 2fdb5ed1-3deb-30fa-895f-3b7b38f39072 | -8.60051 | -54.71246 | 2026-08-21 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6e59f763-0bfd-3667-acc2-90fc5b473c22 | -14.72529 | -47.14553 | 2026-08-21 05:23:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9d8d2f6b-97c9-34e0-b443-e3aff363d580 | -6.86588 | -59.44723 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ec4ee109-7aa9-34d1-9845-df5b779e8ee2 | -6.11504 | -53.07374 | 2026-08-21 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 3da8856a-e529-3c5c-8276-ec671ae3c58d | -8.09167 | -51.66558 | 2026-08-21 05:23:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 466f0e33-7ec4-31cf-b05e-6af4714f0dd9 | -6.89092 | -56.43803 | 2026-08-21 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d66fdb50-d39e-3886-850f-f0b258a16636 | -9.06682 | -60.43481 | 2026-08-21 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d408d446-5472-324a-b16a-649534d8cb95 | -6.83367 | -59.40778 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 435aa85d-66f1-30a4-bd2f-e59349459adf | -9.22272 | -59.65506 | 2026-08-21 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fb0d3a94-615f-311d-977c-9441a9a1ced1 | -6.12272 | -59.91067 | 2026-08-21 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 461f4ee1-123a-3d68-8daa-1dc5d1ccd22f | -7.34749 | -55.67664 | 2026-08-21 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| df0658c0-2b2e-310a-b6a8-95fa9de758e6 | -8.38528 | -62.69774 | 2026-08-21 05:23:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d9d2bd91-b3e9-3ea0-b878-7cd95ce12847 | -6.47864 | -55.90211 | 2026-08-21 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d633880b-7006-3b54-bef0-1f693e6fa954 | -7.06664 | -59.97088 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e0ed43b5-e9e4-3212-8a98-71ab30562cf4 | -4.78907 | -62.91947 | 2026-08-21 05:23:00 | NPP-375D | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 0ba0c100-0033-3395-9586-2b416ca7f7c5 | -6.57971 | -55.44677 | 2026-08-21 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 34502db1-a81e-301e-ac78-8e057e61ca3f | -8.58615 | -54.75822 | 2026-08-21 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cbf3e3c9-1ae7-3e85-baa3-237091d06635 | -7.53593 | -55.5806 | 2026-08-21 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fb0141d8-2581-353d-8efd-ab33159e929f | -8.09544 | -51.67037 | 2026-08-21 05:23:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1026b02e-382e-3587-b609-d7f3b3cde54d | -9.46408 | -51.63788 | 2026-08-21 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2eb83228-dff0-340b-84fb-52184226c54d | -8.2215 | -55.02472 | 2026-08-21 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 35d1ea99-b632-3eca-870a-faea90097951 | -8.52324 | -55.33947 | 2026-08-21 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 778c212c-be56-30d3-bd03-dda1d41babac | -8.65672 | -54.63173 | 2026-08-21 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 40e0c512-4810-3844-8bfd-9ed6b3e24bb0 | -9.22213 | -59.65871 | 2026-08-21 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a57e6caf-db4c-3e29-8e05-a73718d173e2 | -6.43356 | -52.76435 | 2026-08-21 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 908fce74-3c10-3cff-be3f-238a0e0ebb4d | -6.5846 | -58.96342 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d9db3204-9c96-3834-8bad-9dec49913ca8 | -10.65633 | -49.0185 | 2026-08-21 05:23:00 | NPP-375D | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f2daf485-49c7-3744-acd5-0f5fe9e2da7c | -8.55329 | -54.77906 | 2026-08-21 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 36d9b6bf-5a08-37b7-9112-7bc59a2cb366 | -6.8854 | -59.4352 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ab403253-f107-3ee3-ad0c-9c078ddef525 | -6.88475 | -56.43341 | 2026-08-21 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fcbdf9bb-bbfc-37a7-bc82-80a669918073 | -6.09318 | -57.91336 | 2026-08-21 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4efbb31d-c03d-3960-a2e9-040544a7adbd | -12.51331 | -54.75661 | 2026-08-21 05:23:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ade438b1-1ddb-33fa-a4ad-266cef0a0cd2 | -8.37649 | -62.7015 | 2026-08-21 05:23:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 21.6 |
| 6ec8ab88-35d7-3a5f-84c5-60be983b8657 | -6.17182 | -55.44805 | 2026-08-21 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0679f2fc-b355-37d9-b606-300cc2dbbecd | -14.46012 | -45.6138 | 2026-08-21 05:23:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 8d3d0c13-4890-39a3-8821-e1f7e08932d6 | -13.94618 | -53.85872 | 2026-08-21 05:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9fdd48f9-b124-3bb4-8b99-107450a94dec | -6.88317 | -59.42724 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| b14d4e3c-d76b-3175-8475-bce21efacafa | -6.85235 | -58.96904 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5dd423e2-7fe4-31ba-9df0-5745d71aa184 | -6.01947 | -57.82331 | 2026-08-21 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cce6d3e9-40c9-3888-9aa9-964b59e6baf9 | -9.44289 | -51.62611 | 2026-08-21 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1bb38be2-95b1-3f1a-8b9d-98ae71cc35f8 | -6.85747 | -57.68686 | 2026-08-21 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ae81a895-d38c-3449-a438-a70b186536f4 | -8.52385 | -55.33548 | 2026-08-21 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 98e98833-3763-3c33-9ef1-18316323f5ba | -7.36503 | -55.51634 | 2026-08-21 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 437ad2a5-0b85-3081-b57f-c30104333aa6 | -13.38696 | -54.37959 | 2026-08-21 05:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 42.4 |
| fcf9a6e1-d304-3a8b-a017-1cd985134bec | -6.23969 | -55.39714 | 2026-08-21 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| adf10bbc-cbd8-3d61-9b44-dc83f2a8977b | -6.77465 | -59.45158 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 04444747-bae2-3b6d-8bdb-ea52c90ba282 | -14.99422 | -52.67374 | 2026-08-21 05:23:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e1b02a15-2215-3f0b-ae9e-bd6967805a10 | -12.51779 | -54.75243 | 2026-08-21 05:23:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b0ed5119-e7a2-3db6-bbbf-e59419173a1b | -3.53417 | -48.18294 | 2026-08-21 05:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 8ede8081-f2a7-3fec-ae51-178713cb8d97 | -6.09652 | -57.87113 | 2026-08-21 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6be6b57b-eb44-326f-8a23-54cef5617f38 | -13.74426 | -51.85695 | 2026-08-21 05:23:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 9670dc6e-1ceb-3643-a926-166674dc4632 | -6.77062 | -59.45473 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a70f943b-18c4-3aff-b3d6-600c647f2159 | -3.2013 | -61.27686 | 2026-08-21 05:23:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e4f47067-cdb1-3448-90dd-b3ad3cbed63d | -6.71087 | -59.08745 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2c7d0f74-2ef2-33eb-a3bf-a0abbf150fd0 | -7.44403 | -59.99892 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| da1b7fca-c024-3f1b-b278-4d92a6c7af60 | -6.88094 | -59.41928 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1cd31c0b-2ef4-324c-8dc8-cb231dc67fdd | -6.66326 | -56.35509 | 2026-08-21 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bceb3d6d-e1b8-30eb-867f-c0bb6aa72695 | -13.4042 | -54.37179 | 2026-08-21 05:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 186a38bf-3bb8-3343-872a-f4ff9a63b970 | -6.13806 | -57.84566 | 2026-08-21 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7a52c581-54da-31b3-9fa2-a8badb199694 | -14.07209 | -58.87664 | 2026-08-21 05:23:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 01d3ef18-c089-317c-8bb4-2b67f6ba2d8b | -6.01283 | -57.82226 | 2026-08-21 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7312d498-872f-316d-85d4-c0727d8112bf | -7.05854 | -59.83634 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e3f0729d-a4d1-3af4-8ad5-ca2a68c8f86f | -7.36688 | -45.81348 | 2026-08-21 05:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| b4074882-056d-39cd-a813-33c9c64d6c79 | -9.05637 | -60.43304 | 2026-08-21 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| af504baa-209d-31d1-8d75-f8137c601a13 | -6.89045 | -59.44743 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fcf30b18-ab81-30fa-92f9-f8c031e52020 | -6.83085 | -59.40351 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 098a150c-5192-32cc-80c3-f9f7b5db726f | -6.81657 | -59.40501 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 907183b5-e8eb-37db-81b5-2c9dc32c43a9 | -6.90192 | -58.98829 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c0d8fa8e-6ade-3850-bef0-114de847cef0 | -8.58233 | -54.78349 | 2026-08-21 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |


[Clique aqui para ver as próximas entradas](README59.md)
