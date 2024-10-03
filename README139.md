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

## Dados Diários - Página 139

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7043def8-726c-32d3-a622-bd385c1fe7f0 | -9.94087 | -64.90559 | 2024-10-03 04:51:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2f68c2f4-b234-35dc-86fe-3a194bd3f482 | -9.94018 | -64.92004 | 2024-10-03 04:51:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5acf87bb-b5e0-3d11-926a-8f4d7a574915 | -9.93991 | -64.91041 | 2024-10-03 04:51:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bf3070be-111a-397a-ba5a-3bf03522031f | -9.93896 | -64.91525 | 2024-10-03 04:51:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6524ec66-4831-3ed0-920f-7705514c895d | -9.938 | -64.92009 | 2024-10-03 04:51:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 73e0b465-e9c8-34e6-bac7-0cda1b51f247 | -9.93696 | -64.76984 | 2024-10-03 04:51:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7c60539f-8273-331d-8c36-d96692c5d9a8 | -9.93088 | -64.76844 | 2024-10-03 04:51:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3b32c56e-dd96-387d-ac0b-d4c8247f612d | -9.89836 | -64.77233 | 2024-10-03 04:51:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8b718edb-c2a2-315b-95ad-fba5805b08d1 | -9.89744 | -64.77705 | 2024-10-03 04:51:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 435623cf-2999-329f-8ee6-1ef4ad0aeaf6 | -9.86526 | -64.9756 | 2024-10-03 04:51:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 380635e2-bd32-3041-a74a-ec0dfcfdc166 | -9.85906 | -64.97439 | 2024-10-03 04:51:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6ae4c009-2a98-381f-b2a9-bc44ad4e244e | -9.8559 | -64.86588 | 2024-10-03 04:51:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 53582bce-1d21-3db4-8dc8-cd31bad08e5f | -9.85498 | -64.87074 | 2024-10-03 04:51:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 166f39ce-bd80-36ab-a453-171c4f93abd0 | -9.85426 | -64.86755 | 2024-10-03 04:51:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 44ccd820-b314-346a-b0cf-19c50ac64d14 | -9.8533 | -64.87244 | 2024-10-03 04:51:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a314bb5b-e072-3916-862d-778c379fa06e | -9.84975 | -64.86459 | 2024-10-03 04:51:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 90b23a42-7071-3392-8258-00d240048b3d | -9.84883 | -64.86942 | 2024-10-03 04:51:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 09823720-4459-3c4a-b416-9af3bc2a9281 | -9.84811 | -64.86629 | 2024-10-03 04:51:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b13d8d80-15e3-3ec4-a4f9-9646ee882e6e | -9.81988 | -64.9544 | 2024-10-03 04:51:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 26c778d1-571c-3f6a-bdda-679374ecbb3d | -9.81891 | -64.95946 | 2024-10-03 04:51:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b975dcce-43eb-3bd4-b9d0-e28dedad5339 | -9.81758 | -64.95602 | 2024-10-03 04:51:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 88dfd06a-2ebd-3ac4-8ac3-91526bfa8a69 | -9.81271 | -64.95827 | 2024-10-03 04:51:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e1748b6d-1c49-3e12-9cec-25787ffe626e | -9.81136 | -64.95492 | 2024-10-03 04:51:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1dd266b7-77d7-30f2-a25d-cb6ed3e06fa9 | -9.68184 | -64.71735 | 2024-10-03 04:51:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2ffbabeb-786b-3af8-8aa3-d609343428ab | -9.6809 | -64.72217 | 2024-10-03 04:51:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 02af7065-c62e-36ee-8e73-93c4747e7542 | -9.67994 | -64.7271 | 2024-10-03 04:51:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 08289f17-bc5a-3cf5-9da9-ea69cca84d31 | -9.67382 | -64.72585 | 2024-10-03 04:51:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8289acdb-c91f-3869-8cf1-7bfa27bc0454 | -9.38074 | -65.47126 | 2024-10-03 04:51:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c75babf7-65bb-316e-8720-d707f0c3f72a | -9.38037 | -65.50494 | 2024-10-03 04:51:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 608036a6-b3db-31d3-a859-1d4dba013b81 | -9.38032 | -65.47154 | 2024-10-03 04:51:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 11b9e567-bb73-367a-b410-baa4dde7ee4b | -9.37469 | -65.53763 | 2024-10-03 04:51:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3f518b37-8af8-339e-ba6f-d3ea6878513f | -9.37431 | -65.46992 | 2024-10-03 04:51:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7c21a9f2-3682-3777-9637-aa88a93d1dde | -9.37389 | -65.47021 | 2024-10-03 04:51:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7bd34210-4de4-364c-a97c-e8d27e26377f | -9.37016 | -65.79572 | 2024-10-03 04:51:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9a198a3f-3e9d-3ea8-ad46-570b59113b95 | -9.36929 | -65.53083 | 2024-10-03 04:51:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3932c5c1-89f5-3910-91ea-cc637199adee | -9.36901 | -65.80157 | 2024-10-03 04:51:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7ef19fbb-d560-3fa2-8f03-e147a00d9f42 | -9.54873 | -64.32865 | 2024-10-03 04:51:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 56b962b7-7221-305a-976d-c95a8a770ee6 | -9.54786 | -64.33319 | 2024-10-03 04:51:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d7477b4b-f342-34ac-af62-a16da669fa19 | -11.68787 | -65.0144 | 2024-10-03 04:51:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f1e4ec68-75bc-3c5e-825a-43f58c5e69f6 | -11.68737 | -64.9854 | 2024-10-03 04:51:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 9.0 |
| d5c64c7e-5bb8-32c2-a64c-8b6d8b9dfcd4 | -11.68645 | -64.99004 | 2024-10-03 04:51:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 4a8ffaa5-1a91-3bb9-8607-6001aaa8324e | -11.6828 | -65.00837 | 2024-10-03 04:51:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d5c8b414-6ad2-384f-b4c9-1d2f5adedd0d | -11.68188 | -65.01296 | 2024-10-03 04:51:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8d93ac0e-1d60-3c7a-95c2-cf033e3002ea | -11.68139 | -64.98399 | 2024-10-03 04:51:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 6d8aa690-70bd-310b-a894-2226e580c1f7 | -11.68095 | -65.01765 | 2024-10-03 04:51:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 34abe217-7fa3-39ab-854a-731f19f9090d | -11.68047 | -64.9886 | 2024-10-03 04:51:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 9.1 |
| e53158ed-7a56-3042-aec6-b361e72a9ca2 | -11.68002 | -65.02232 | 2024-10-03 04:51:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e567889f-c7c9-3716-926b-3e3a80dd9f76 | -11.62367 | -64.99063 | 2024-10-03 04:51:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f8902e11-12db-3d80-87d0-541912e70682 | -11.62221 | -64.99149 | 2024-10-03 04:51:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 55d5d2af-2f30-3afd-b486-72e195f84710 | -11.61766 | -64.98936 | 2024-10-03 04:51:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 83e9dbd4-2861-33c1-94ec-6ecab9a44136 | -11.61531 | -65.18777 | 2024-10-03 04:51:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 88119098-8a72-3747-a4b8-23e53bbdfb17 | -11.6144 | -64.99937 | 2024-10-03 04:51:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 85df0911-084e-3c4c-a35b-96d40b18c032 | -11.60924 | -65.1864 | 2024-10-03 04:51:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 78fd6d7d-ad27-358f-a131-cd0683bfaeaf | -11.60905 | -65.18789 | 2024-10-03 04:51:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| ef2051d8-96fa-3317-890e-0c36176c617d | -11.60842 | -64.9979 | 2024-10-03 04:51:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 03be8301-5896-3ee2-a273-b6fa1c726997 | -11.60812 | -65.19263 | 2024-10-03 04:51:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 3f24a6a2-b77e-364f-a2aa-7bbc9f178e68 | -11.60752 | -65.00246 | 2024-10-03 04:51:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| df8484ea-f7fb-3454-be35-b97b3bc17e29 | -6.97605 | -59.10159 | 2024-10-03 04:51:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b91b59bd-f73b-3c69-91f1-ef348e1b4d8e | -6.97236 | -59.09642 | 2024-10-03 04:51:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ca72c294-b08c-32dc-a76f-f4f121adc2e0 | -6.97161 | -59.10082 | 2024-10-03 04:51:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0909c071-c1d6-30f4-9760-84f9d0740977 | -6.88166 | -59.05051 | 2024-10-03 04:51:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c98c4ff6-8081-3252-8a25-d3a306c05a6b | -6.88092 | -59.05487 | 2024-10-03 04:51:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5ee66d2b-a12c-39b2-8376-23d9b5a273e6 | -6.87945 | -59.03661 | 2024-10-03 04:51:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 702f6214-adca-3776-948e-c0179f7d53cb | -6.87871 | -59.041 | 2024-10-03 04:51:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e60994dd-6c8a-38b5-8694-609ac44ecd23 | -6.87797 | -59.04537 | 2024-10-03 04:51:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| de902d9b-48df-3862-a662-0a103cc8cb7e | -6.87723 | -59.04974 | 2024-10-03 04:51:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 14e83d97-c12e-3f23-82e5-88bd99a08010 | -6.8765 | -59.0541 | 2024-10-03 04:51:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e9d008b5-3cb2-3909-b38e-391d3d4de402 | -6.87578 | -59.03144 | 2024-10-03 04:51:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| de0cb558-4bab-3423-b869-1bd79a340065 | -6.87503 | -59.03585 | 2024-10-03 04:51:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3aecff69-faef-3978-a041-aded1efdc6bc | -12.45081 | -53.46058 | 2024-10-03 04:51:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 47465de7-74b8-3541-b607-49a6467e584d | -12.4447 | -53.45596 | 2024-10-03 04:51:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 80e8f091-4068-3ea3-9490-b5e2e1630778 | -12.44192 | -53.45187 | 2024-10-03 04:51:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b5c32155-6165-3b79-ba5a-c23c86a8e8c1 | -12.70102 | -54.00207 | 2024-10-03 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 61ac4756-7ab7-3e63-a39c-688e61fd2d1a | -12.68929 | -54.09816 | 2024-10-03 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3ec9253a-c68a-3412-b38b-556c46cf0393 | -12.6854 | -54.10115 | 2024-10-03 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e2fd6f18-43ed-3a48-a38b-b619eebda9f4 | -12.68207 | -54.10061 | 2024-10-03 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d8786626-479b-3332-9490-26c6ee9042c3 | -12.67156 | -54.08073 | 2024-10-03 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5a5a03dd-67aa-383a-b381-58d0f2e0e2d1 | -12.671 | -54.08427 | 2024-10-03 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4cf2f01f-00e8-3cd5-92a1-4e69e01286ae | -12.66879 | -54.07664 | 2024-10-03 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d3822963-89b4-3d93-9cb0-a054997ce508 | -12.66823 | -54.08018 | 2024-10-03 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 50cedab4-7680-349e-b9f5-e3e009d846c3 | -12.66716 | -54.04372 | 2024-10-03 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 86b26de2-0b92-3e3c-b4fd-dd6a08d60bdf | -12.6666 | -54.04726 | 2024-10-03 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7b8bce8a-8068-3964-b086-fd70f6678338 | -12.66604 | -54.0508 | 2024-10-03 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cc612a88-9211-39df-8295-c10ee4dcf9ee | -12.66546 | -54.0761 | 2024-10-03 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0df38f01-2e58-3394-9d76-525aa7447954 | -12.66493 | -54.05787 | 2024-10-03 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d3609f7a-9bf7-3c2c-ba75-318598f8d7d8 | -12.6649 | -54.07964 | 2024-10-03 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c5aaf9e4-8cfa-3bfa-abd1-87c311c0e701 | -12.66269 | -54.07202 | 2024-10-03 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 64f140cc-3160-3990-8224-6569126c799c | -12.66214 | -54.07555 | 2024-10-03 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2c32bd9d-146c-3291-8084-693f003008a3 | -12.6616 | -54.05733 | 2024-10-03 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5ac38f43-a59e-3035-9523-31f488230048 | -12.66104 | -54.06086 | 2024-10-03 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6f95000a-8be0-3421-9dd9-bae3cb7882c1 | -12.66048 | -54.0644 | 2024-10-03 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c5f22543-1755-329c-a03e-7d6120c4b44c | -12.65992 | -54.06794 | 2024-10-03 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 84b9d471-fedc-3499-a6ce-967a2d881731 | -12.65937 | -54.07148 | 2024-10-03 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 219e3131-dfa1-3945-a22f-6c4d41bd82f4 | -12.65827 | -54.05679 | 2024-10-03 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b8e303d0-e563-39c9-9064-80c6c74ce075 | -12.65771 | -54.06032 | 2024-10-03 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a9d842b4-82e5-3891-ab3c-f3100c3a1697 | -12.65716 | -54.06386 | 2024-10-03 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f3317c81-0f6b-34ad-a477-07ff108e78d9 | -12.6566 | -54.06739 | 2024-10-03 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fbdaad62-0680-30ce-b329-a9c36c04e3be | -12.65604 | -54.07093 | 2024-10-03 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0dc4ac13-f2a4-3713-8ae2-243640fccd10 | -12.65383 | -54.06331 | 2024-10-03 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7a124685-be5a-3b20-9740-49833d6dda41 | -12.65327 | -54.06685 | 2024-10-03 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |


[Clique aqui para ver as próximas entradas](README140.md)
