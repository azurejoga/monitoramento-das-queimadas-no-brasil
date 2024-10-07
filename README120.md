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

## Dados Diários - Página 120

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f9d2a01b-837e-34d5-a8ab-bfec97974eee | -17.13256 | -56.82483 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| ee243596-83a3-35bd-82a3-2e573dfc57b3 | -17.13188 | -56.82985 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| c55de878-d2b3-3542-8d50-ca0abf5ae2c1 | -17.1312 | -56.83488 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 4b48fd61-56a1-3740-b423-65379e2de0e1 | -17.13004 | -56.8142 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 83.2 |
| df4f8428-1ca7-31ef-b2b5-d50e78ec499b | -17.128 | -56.82928 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| a45f0d3e-eff0-33dd-8a77-4bdc75a71716 | -17.12683 | -56.8086 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 28.4 |
| cd632e33-d39d-3da2-89b9-86b324ccc354 | -17.12615 | -56.81364 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 83.2 |
| 26343e6e-df3c-34cc-8b61-b2bef4a8ca08 | -17.12547 | -56.81867 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 83.2 |
| 2ebce103-53e0-38dd-b58c-eac57c6ed8aa | -17.12344 | -56.83374 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.5 |
| dfc6a9e7-3800-340f-b081-d46a85073929 | -17.12294 | -56.80804 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 15.3 |
| 0c73fe40-8a27-34d5-87fa-b04ef3d310cb | -17.12276 | -56.83877 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.5 |
| cac5068a-40e8-35ae-8e83-fa64c2364359 | -17.12226 | -56.81307 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 8b7f4bf5-1984-362a-a562-5cce0a670805 | -17.12091 | -56.82313 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| ac2ce4de-8e9e-3a5c-b369-461730a9a0d6 | -17.11973 | -56.80244 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 15.3 |
| e312ef8b-ba1a-3034-9384-588d0f4b6d5b | -17.1182 | -56.84322 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.9 |
| a40ab443-e35d-32b4-9f7c-bec452479d9b | -17.11432 | -56.84265 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.9 |
| 4c811ff5-a5e3-3f01-98c1-6cb5c203cb0d | -17.11112 | -56.83706 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 6c5ac589-442d-3eb3-9fb9-91027446b7be | -17.11045 | -56.84208 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 47e73842-d8d6-3a94-959d-671b164f4189 | -17.10657 | -56.84152 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 327e0510-0b58-309f-b606-6c725c8b9091 | -17.10589 | -56.84653 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 97d84ed4-8f89-3238-a405-f11491ec68fc | -17.1047 | -56.82589 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| c9bebb20-40e4-361e-b3cd-0a5cec33a350 | -17.10015 | -56.83035 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 6b002639-9b0f-39c1-901d-880432485d54 | -17.09948 | -56.83536 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 9a9f7241-6d92-3f28-995f-44198eab3b0f | -17.09881 | -56.84038 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 6d7bcc5e-2177-3cee-9514-cfc07ea09c9a | -17.09693 | -56.82475 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 2308e0bd-19e1-3414-b7fa-19f9bbab7be4 | -17.09493 | -56.83981 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| f79bd795-08bb-3abe-bb3a-8f204a772f00 | -17.09305 | -56.82418 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 531e2c6a-b71e-34a2-a5a5-26a918e68e04 | -17.09238 | -56.8292 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 63dc42b4-a3b8-3e17-ab04-d46ac01195fc | -17.08784 | -56.83365 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 63defa7c-0c5f-30ad-835d-6571c6a2cc01 | -17.08595 | -56.81802 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 7ac31b35-df84-3d54-be9d-bd244603509a | -17.08529 | -56.82304 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 12af1825-184f-3395-822f-0d9f338f1a46 | -17.08008 | -56.83251 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| fe7bedf6-8c30-388b-a884-ebe0892b9f46 | -17.07885 | -56.81185 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 58b9eab4-8e24-36f7-962e-83374f49e984 | -17.07617 | -56.82943 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| a4104497-cf4f-3668-a973-ee76d4aa5c4a | -17.07487 | -56.84197 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.9 |
| c86d0fb8-4e95-3eec-8e97-241eec949aac | -17.07364 | -56.82132 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 635cd993-7976-39e2-9a94-b436eafdc16d | -17.07298 | -56.82635 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 6d996977-4ae7-3f47-be8c-317fd3338555 | -17.07232 | -56.83137 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 113b439d-387a-354a-a81c-300d0523d7f7 | -17.07166 | -56.83638 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| ce703436-56a3-35a5-8759-0cd820eb2b18 | -17.071 | -56.84139 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 4ba804a1-33a4-315e-8728-875b49f1ae81 | -17.0691 | -56.82578 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 74168a8a-7f01-3eb8-8fb9-785c14d43bd6 | -17.06841 | -56.8283 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 1513f08d-0e5c-388d-97a6-dacda79d000b | -17.06771 | -56.83331 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| ef9824e0-face-30b8-b8e4-a64b3acf8a8e | -17.06521 | -56.82521 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| faf1be57-bc40-337e-a2d2-f818ce3d6d65 | -17.06455 | -56.83024 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 16507c66-9390-322f-a7e7-7bb50ff65fae | -17.06453 | -56.82774 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 3f969e6c-4d7b-3506-b959-b27b1a7cfd40 | -17.06199 | -56.81961 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 804c8b0e-5647-3442-984e-4096298c87e8 | -17.06133 | -56.82465 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 65ea3ea3-809f-33b2-a98d-3600b00f8c13 | -17.06067 | -56.82967 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 5cc89d0c-49b9-3c55-bf92-25730e3a745c | -17.06064 | -56.82718 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| e228a06f-dee4-3ee3-a5e3-45bc7bdadf06 | -17.05883 | -56.81156 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| f252e2b6-c72b-33c0-80cc-396ea1eda958 | -17.05426 | -56.81602 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 9f186174-8e2f-3555-9a46-584d6ca78e22 | -17.05357 | -56.82102 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| c9dc2e72-30a3-3203-aa55-e8062569a3be | -17.0522 | -56.83104 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 6a4461d9-e7b0-38e5-bd2d-63296089a893 | -17.05038 | -56.81545 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 800915a3-7c32-333d-9a6c-e245bf928288 | -17.04969 | -56.82046 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 78f9b02e-745a-3b87-a1da-e1dfc0cd4b0d | -17.04901 | -56.82547 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 7a0a68b0-5b17-3522-9e06-54903eaa63dc | -17.04832 | -56.83047 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| bf3f6b03-1126-38b4-87e9-7c06eb9659ea | -17.04581 | -56.8199 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 38bc7377-bf6a-3da2-867e-0494170c49bb | -17.04513 | -56.82491 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 6f7a4cef-5c90-328b-9544-54cbcde8d200 | -17.04444 | -56.82991 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 8b058241-3276-34ca-8bd1-d950e3984a79 | -17.04193 | -56.81933 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 7d56aaad-a5e0-33b3-ad8a-ffdd89dfe766 | -17.04125 | -56.82434 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| ec85aef5-299e-384a-a066-ae177500a8af | -17.04056 | -56.82936 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 0d3bdd8b-9d4d-3097-9af9-b60e163d6357 | -17.03988 | -56.83437 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| b78d765c-105c-38f8-93e1-2faf66a4e1b3 | -17.03737 | -56.82378 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| d4b58732-888d-3ba6-9998-c4309d28190b | -17.03532 | -56.83881 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| e09df886-73e3-3e52-ab75-148e2e2bdae5 | -17.03349 | -56.82321 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| cafb7843-6e82-32cf-a6a0-ef64856afab7 | -17.03213 | -56.83323 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 390d0bb0-6741-3bb1-b16e-eccaf20f9054 | -17.03144 | -56.83823 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| be82087f-373b-3d68-b2c3-71a902456932 | -17.02893 | -56.82765 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| bf27a005-ca1c-31ed-8184-bfbb52eb54a6 | -17.02757 | -56.83766 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 7b3cac9c-661c-369c-84ec-90ad38ea9c00 | -17.01982 | -56.83653 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 9f9033ce-4eb2-3af8-8dbf-77118b475226 | -17.01594 | -56.83596 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 8f8bafe6-bb35-32f0-9a3d-2c7a25ff68e3 | -17.01274 | -56.83039 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 192d0579-0eac-3b5e-ae40-98e2dfb2c04b | -17.01207 | -56.83539 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| e4859b3d-7d7f-3b52-a295-8bad5ab6e8cd | -17.01139 | -56.84038 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| b010d423-a059-347d-a098-a7a0c0139108 | -17.00886 | -56.82982 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| cc293f52-835c-3b82-a177-4d4f215e47c3 | -17.00819 | -56.83481 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| d26366bd-3353-390a-b348-6f01386b660e | -17.00111 | -56.82868 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| edf60a8e-3914-3008-b483-4aa895858dbe | -16.9979 | -56.8231 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| d2e28cdf-a86c-3986-a6c5-63e3ea26423f | -16.99403 | -56.82253 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| da8dc39d-f874-3cc7-b2ea-2e5e95f45909 | -16.99082 | -56.81695 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 997d132f-4aef-3ea4-af89-6fe8102eaf88 | -16.9876 | -56.81138 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 609a35ba-0312-3d2f-abd9-c705f9052571 | -16.97597 | -56.80967 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 268f5509-2322-39cb-be9f-d3193f58938d | -16.9753 | -56.81468 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| a5e1954b-b2bf-33d5-a198-e9b1dfe24718 | -16.97208 | -56.80911 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 8b6294e7-036f-349f-9f81-f281789cb02e | -16.9715 | -56.80735 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 01827d88-16b8-3344-9b6a-5f5995d6265f | -16.97142 | -56.81413 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 885992e9-20c6-30bb-9776-d6e150886386 | -16.97081 | -56.81237 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 630e03be-d06b-3717-9e9d-a0fcb7246632 | -16.96887 | -56.80352 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.8 |
| 8b7695b6-e02b-3358-a374-b1d5afdc8fa0 | -16.9682 | -56.80854 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.8 |
| ab8639f4-b71b-3291-bf03-48ea7eb60ca1 | -16.96762 | -56.80679 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| ee2294f0-dd00-3b44-a91f-f1386a2ee9c7 | -17.15382 | -56.75583 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| a505d616-c5e4-3f8d-9caf-7d23eec5488b | -17.15313 | -56.76091 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 4dec0c20-40ab-33c5-8a87-6f923807e23e | -17.1467 | -56.74962 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 98941af5-33b9-3d78-a62d-452b3a82a209 | -17.14396 | -56.76992 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| f3bf9874-cbe0-3315-b4d8-6e953cab0a3a | -17.13616 | -56.76878 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| c491fa62-5cb3-3899-bf23-f9dfe8b9b327 | -17.13022 | -56.78339 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.4 |
| d6c8653b-c970-34ab-84d4-6d3d44b5dda0 | -17.12379 | -56.77214 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.9 |


[Clique aqui para ver as próximas entradas](README121.md)
