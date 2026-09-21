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

## Dados Diários - Página 90

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9c547a0b-06d4-3f0a-bd57-cde012c5314e | -3.46435 | -58.40179 | 2026-09-21 05:40:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 64f1cd94-cf2a-3929-86ea-b7974e28a843 | -3.01139 | -54.18266 | 2026-09-21 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 66940ded-d0ea-3285-bd13-c275b16e8a91 | -2.61129 | -51.72635 | 2026-09-21 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c4d1bc66-aa1b-3192-a103-749f85cce69a | -2.61626 | -51.73077 | 2026-09-21 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c1f78686-fdb5-3248-9400-9bb1d88831fb | -1.24274 | -54.19189 | 2026-09-21 05:40:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1c23a5c9-347d-381d-9505-57d2675f54af | -3.05974 | -61.27413 | 2026-09-21 05:40:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f99753d8-afb4-3329-845f-f823558af4b3 | -3.60409 | -59.05928 | 2026-09-21 05:40:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 33b07e0a-da49-3221-8f45-158ee2c9fea7 | -3.90112 | -55.83909 | 2026-09-21 05:40:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ded9eb95-3402-3fb4-80ac-6a6e3c6bea9b | -4.52471 | -55.66291 | 2026-09-21 05:40:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f7aff439-794d-3d73-93e9-a56618d4c668 | -3.05419 | -61.26619 | 2026-09-21 05:40:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1a0034c8-54a2-38a9-8ae4-858a738bcf3d | -3.40071 | -61.34515 | 2026-09-21 05:40:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5a8b85b6-e4d9-3edf-a3a7-8472eac0d240 | -3.07159 | -61.09187 | 2026-09-21 05:40:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2d9b6f1b-5ea2-33b4-a08a-f283cad95052 | -3.08282 | -61.17156 | 2026-09-21 05:40:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dbfb653e-0231-3ead-b4bc-e7b15c1a0995 | -3.60803 | -54.04719 | 2026-09-21 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8015c311-55a1-3fdb-b686-3d09f77c60bd | -3.07562 | -61.17397 | 2026-09-21 05:40:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b0b7d8ff-4d2c-3cc5-9dd6-8525915379d2 | -3.53965 | -58.687 | 2026-09-21 05:40:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d84ec8c8-f834-3e42-b0b1-45a91697da50 | -3.05865 | -61.28104 | 2026-09-21 05:40:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 00b8f3d4-8f2f-395f-919a-6d0c2767edbd | -3.37748 | -50.44512 | 2026-09-21 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ae59fba6-3525-3c84-bf2e-2630b4fc0ca3 | -3.05032 | -61.26912 | 2026-09-21 05:40:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4fe59ea2-6dd9-390c-8dce-db5f9d7be876 | -2.96276 | -57.72351 | 2026-09-21 05:40:00 | NPP-375D | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a1ee3e6a-6bab-3a6e-90c0-a131f4f37a73 | -2.68544 | -59.78112 | 2026-09-21 05:40:00 | NPP-375D | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a8fca2ae-c460-3213-9a1d-c0071e1eed39 | -2.87305 | -57.81267 | 2026-09-21 05:40:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 018c8aa7-96ee-3ef1-8bbf-af680d1b009f | -3.44001 | -50.60551 | 2026-09-21 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 34d19f80-9bad-3dfb-879f-84e2f1500c33 | -2.61184 | -51.72277 | 2026-09-21 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 84368ccb-ebee-3557-a9ba-e936a86d07ae | -2.99959 | -60.79962 | 2026-09-21 05:40:00 | NPP-375D | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6f6dce7f-a965-3456-b6bb-b5da515ff82f | -3.01394 | -54.17446 | 2026-09-21 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 54fea62d-aff1-345c-b43b-0faea1aeab84 | -3.33236 | -59.81678 | 2026-09-21 05:40:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7190fac9-bf43-371d-8cdb-78a5f844f908 | -3.36747 | -61.33994 | 2026-09-21 05:40:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 961524bf-0196-3db8-99c8-d31ddce43c66 | 1.77314 | -60.23413 | 2026-09-21 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| af5be65b-075e-361a-bccd-7132bafdd9c0 | -2.58652 | -59.41125 | 2026-09-21 05:40:00 | NPP-375D | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 13a74cd6-8514-344b-8b07-3ddbf697e3b7 | -4.565 | -55.74839 | 2026-09-21 05:40:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 7e709d33-d4e6-3c95-a181-33bce5ca57df | -3.06361 | -61.2712 | 2026-09-21 05:40:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c0eb3618-cc60-3de2-90f3-128629b5b775 | -3.62412 | -54.52652 | 2026-09-21 05:40:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 70e18eda-c7fc-3210-bc53-d0f220481768 | -2.94776 | -51.03993 | 2026-09-21 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3de38e0a-de73-3f65-bcc9-b8ca1e34cbf5 | -3.17222 | -48.61405 | 2026-09-21 05:40:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b3e5bdf8-9b28-3f83-bada-7123c986f9e9 | -3.06639 | -61.27518 | 2026-09-21 05:40:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1c79b5bd-63c3-3772-8087-3f15793994c5 | -3.17484 | -61.16816 | 2026-09-21 05:40:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ff7e8912-bcf3-3012-9b02-311ee38af861 | -3.68908 | -60.56741 | 2026-09-21 05:40:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5e8eedf7-653b-375b-908e-e8b1e8a214e6 | -3.44533 | -50.61092 | 2026-09-21 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 371a9da7-9f1f-3c34-ad5d-501d55d6177d | -2.87385 | -57.79713 | 2026-09-21 05:40:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 115e1472-8ec7-339b-adaf-a7d8c8f393c5 | -3.05587 | -61.27706 | 2026-09-21 05:40:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e4f8fa06-471e-3782-9d0b-e5a8492abf70 | -2.87569 | -57.79524 | 2026-09-21 05:40:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ea482fac-274b-3a60-9d43-3b7d8cccfa40 | -3.22578 | -60.80318 | 2026-09-21 05:40:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cfefaf75-98c3-303e-8647-70ef086576fe | -3.44157 | -58.23726 | 2026-09-21 05:40:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a499448a-4353-334d-8d15-26025d3b5b6f | -3.39034 | -50.44203 | 2026-09-21 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| a56b04af-d8bb-3945-9f9e-0d76e1cf05c5 | -2.45835 | -49.2244 | 2026-09-21 05:40:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 133c4e0a-6529-34c0-834c-fd6dfdccb115 | -3.48516 | -58.9221 | 2026-09-21 05:40:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4bc85f75-d508-329e-820b-e480cefe7f92 | -2.90128 | -54.18077 | 2026-09-21 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 62734507-4085-31c7-92a8-9559c5ce2129 | -3.82124 | -58.88999 | 2026-09-21 05:40:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b4897aaa-13ba-3672-9f76-80203d6305fe | -2.91845 | -57.78847 | 2026-09-21 05:40:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 55081760-0617-3f36-8e3b-8d38cb855fd7 | -4.34686 | -55.65104 | 2026-09-21 05:40:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1ed78912-58c5-32bf-9c94-edb25981f983 | -3.06452 | -59.28082 | 2026-09-21 05:40:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 57a7d6f6-7ab9-376c-b18b-3fe00963d523 | -3.75379 | -59.41753 | 2026-09-21 05:40:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fba4823a-557e-3e9d-9b49-7ec34b11a001 | -2.90866 | -54.15022 | 2026-09-21 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bdeab0b6-54be-31e1-b136-dbbcbe2b9629 | -6.07473 | -57.62956 | 2026-09-21 05:42:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e04890f3-1769-30c3-a116-4f9393ff6264 | -5.88374 | -53.6375 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7d65cd3e-9f73-30b8-8aff-dfa835ac131d | -7.12636 | -59.65038 | 2026-09-21 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 927385f6-fb40-3031-964b-c885bdd039cd | -5.8371 | -53.54746 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0a609238-4065-3b18-97cd-cf7d94852905 | -8.86127 | -68.51466 | 2026-09-21 05:42:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dfa17923-d2a1-37aa-9548-81a2c091de52 | -6.4595 | -59.98166 | 2026-09-21 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 50857d9c-6ea5-3bb1-b3da-d46925e475a2 | -8.23801 | -62.8393 | 2026-09-21 05:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 24561897-8a95-31b9-950d-f470ddcb3857 | -6.25732 | -55.43195 | 2026-09-21 05:42:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 840e8c1e-4952-39ff-abea-c99bdce96eab | -6.03576 | -53.27748 | 2026-09-21 05:42:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c414ab4f-383b-3e93-b8b6-be9979796756 | -10.76114 | -50.79778 | 2026-09-21 05:42:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 3aa3c8ca-b651-34ec-8ee6-5ad339218a02 | -5.85422 | -53.5377 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1c69523b-8fa2-38e9-9126-b34889e7f8ad | -6.41614 | -55.01716 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8488d17d-5851-3c09-b3dd-c5474ecd157f | -9.11085 | -60.94654 | 2026-09-21 05:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9752848d-fa9e-3eed-8925-e6a7a6aeb8ec | -6.10204 | -57.63369 | 2026-09-21 05:42:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b2c1bf3a-444e-31d9-b626-2d224e17381a | -5.72728 | -53.45647 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3042e1ff-46b7-3be4-a32a-123ad56380a2 | -7.81611 | -61.80578 | 2026-09-21 05:42:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e2958938-da5b-3c26-af9c-709e0ee1bd74 | -10.81699 | -50.77653 | 2026-09-21 05:42:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 14.9 |
| aa411749-6134-34a1-9eb2-30503bdf8c07 | -6.43984 | -59.9708 | 2026-09-21 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7224773a-8b12-3ec3-bd76-2fc9e5d2895b | -7.24322 | -55.61068 | 2026-09-21 05:42:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| d2341b64-42cd-30c9-9271-62853e59b66a | -7.32287 | -55.60635 | 2026-09-21 05:42:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b3a70748-1d5c-35bf-b1cb-4175ec7f2ba7 | -5.85044 | -53.52765 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| affa7e68-586a-3395-b5e0-3d7a918c6963 | -6.30923 | -60.01435 | 2026-09-21 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 376b51cf-f4b7-368a-98ce-f25b7c1dfe6a | -9.61167 | -61.81831 | 2026-09-21 05:42:00 | NPP-375D | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5c99873a-e57f-3024-8546-6f3373447ca2 | -7.55819 | -61.3343 | 2026-09-21 05:42:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 888f6f3e-3349-3e80-97aa-7a271c345d67 | -8.17407 | -54.76614 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 112ce239-bba7-3f84-be27-1a501718e941 | -6.30695 | -60.00628 | 2026-09-21 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| daea6459-c95b-35d5-b54e-4874872e72c3 | -6.82968 | -55.53597 | 2026-09-21 05:42:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 7b5774fe-1acb-3030-b3ce-7f670676eb66 | -5.88125 | -57.72044 | 2026-09-21 05:42:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e643e3bd-85b8-309c-a88d-6ff0428bed87 | -10.21051 | -53.91908 | 2026-09-21 05:42:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2d5ff838-15a8-39d3-9760-a3bfafbe0ee6 | -9.30529 | -62.3182 | 2026-09-21 05:42:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 33e322e4-8de7-345b-babb-886d50d772e2 | -9.28098 | -60.63223 | 2026-09-21 05:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2149dd8d-12ab-35fa-8b17-af82d212554a | -5.83515 | -53.48813 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 492a64ed-7cd9-3d6b-bd4e-d90bdf9b449f | -6.34768 | -59.96144 | 2026-09-21 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 03c1ece2-4159-3b32-8e29-17e5b9a6a6d9 | -6.75209 | -59.06088 | 2026-09-21 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0a53bfce-ce75-3209-b7e5-ca9b00ac9a6f | -7.51162 | -61.38199 | 2026-09-21 05:42:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7c369ddf-d4f7-3591-8f2c-02d72cafda14 | -6.14034 | -59.95054 | 2026-09-21 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 92dee9a6-4437-3a39-b954-f51be5bdf559 | -6.72675 | -55.0941 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cf768de0-b5db-3236-8979-50f8db852fac | -9.22259 | -60.25438 | 2026-09-21 05:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6ef32448-c3c2-303e-a4b1-9b75dcc11f18 | -5.9885 | -55.69622 | 2026-09-21 05:42:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 038e5c8a-34d6-3151-a0f9-978c33dae195 | -5.93133 | -59.95012 | 2026-09-21 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d59bf3e3-22e1-3722-8bb9-90d517db35c5 | -6.12023 | -57.75301 | 2026-09-21 05:42:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fdd712e2-a3da-3cc2-b65c-43e1c2993054 | -5.82139 | -53.51098 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 400e72e4-b196-329f-857a-b415a875018f | -5.83592 | -53.51932 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3854141d-69a2-32ca-92b7-dac62d2d7e94 | -9.10686 | -60.94973 | 2026-09-21 05:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ec094318-db32-31dd-9611-80a72a491c3b | -9.55531 | -66.04498 | 2026-09-21 05:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| de2462f2-6daf-335d-8d01-9bf0f36b490b | -5.89854 | -53.6432 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README91.md)
