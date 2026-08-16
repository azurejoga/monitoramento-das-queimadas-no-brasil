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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| edbaa293-0173-33b0-ab2a-d2f66a969a87 | -8.25581 | -57.34376 | 2026-08-16 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c5c6a68a-1d95-30dc-b531-62626d5df13e | -9.08543 | -61.40474 | 2026-08-16 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d758771c-2442-377a-82a6-f6640a5a78a6 | -6.59204 | -58.98534 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1d3272be-1cca-3192-9862-3757f8989f58 | -12.01177 | -46.42585 | 2026-08-16 05:16:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| fec755b1-7e03-3b70-8fdb-740274585cca | -11.06949 | -47.27413 | 2026-08-16 05:16:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 9912b487-ee2c-30aa-9b81-7d460038c5d1 | -6.54194 | -55.17775 | 2026-08-16 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2fc50e9c-c617-3190-932a-7664f21334d3 | -6.83257 | -56.44574 | 2026-08-16 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 071e1bec-578a-395e-9e35-3fe3fdcdfab7 | -8.9548 | -60.51523 | 2026-08-16 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| b7eee55e-b9d8-3416-9792-ffc4a0f9b316 | -6.61069 | -58.98413 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| eb6a36cc-b606-3090-8e4a-7d64a2f8fd2d | -6.82759 | -56.43425 | 2026-08-16 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f4007437-1899-3546-aab8-324691fe4503 | -6.84642 | -56.44437 | 2026-08-16 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7a0a30f2-977e-3509-aad9-ca3e2951d9c2 | -6.58543 | -56.35956 | 2026-08-16 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| df3f65b8-04cc-39c0-9a1c-b819b127ad32 | -10.52885 | -44.85492 | 2026-08-16 05:16:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 13f38657-b07f-3d4b-847b-34546ad9f4e4 | -11.08165 | -47.25616 | 2026-08-16 05:16:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 29ee9b78-400e-35e3-9d0a-51618801260d | -6.82759 | -56.45564 | 2026-08-16 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7f898460-1599-3381-82da-9858d8676428 | -7.34191 | -59.59658 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| c6a36a49-ce0b-30d3-8e59-e64a15bcc928 | -6.59427 | -58.99418 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 075cd5b2-b9d1-38a2-8333-8e88fdec50e9 | -8.90094 | -60.60188 | 2026-08-16 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9bcc7311-b477-3eb9-ac89-a17a81d43ab2 | -8.9668 | -60.5364 | 2026-08-16 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 1a4084c9-e01e-3246-bbeb-a23a29e4bacd | -6.62638 | -59.04617 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cb495d0e-f980-3f20-84a0-8b23344e6153 | -6.69685 | -58.96339 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 66638220-afbc-37be-9f6f-c95b7490a107 | -6.10121 | -57.72002 | 2026-08-16 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f460abd4-5fc2-3fa2-981d-15001317e44d | -11.10598 | -47.24189 | 2026-08-16 05:16:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 73bf2709-1847-3b30-94d7-90804d4430f2 | -9.98122 | -53.94188 | 2026-08-16 05:16:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 61649874-34ae-37e0-9241-3d611d6224cc | -3.59714 | -58.6212 | 2026-08-16 05:16:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cee73ef5-aa88-3e5a-9a97-94a49fe06022 | -8.95022 | -60.51923 | 2026-08-16 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 5ef6d4f6-7c9b-3aba-baf6-2e8ab23ddb26 | -6.71813 | -58.94597 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5b3f3596-4a6e-34f0-bd96-9774bf94b809 | -6.7018 | -58.95575 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 70a67222-9fba-32b4-b08f-65d76f1e9b24 | -6.71118 | -58.96581 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 329116ef-122d-3ef2-878b-3b20c68d9f0c | -6.63223 | -59.05568 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3d199a8a-5014-39d0-84da-d0b2ecb6d796 | -8.90148 | -60.56086 | 2026-08-16 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 705d6cc6-8a88-31c4-aced-243bc0203c70 | -9.48134 | -51.64572 | 2026-08-16 05:16:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ebb7d81d-2665-3a76-97fd-81cad7b3af24 | -9.48885 | -51.6506 | 2026-08-16 05:16:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 007dc348-44bc-3f41-a216-a3dcbc735f3a | -11.46196 | -46.59269 | 2026-08-16 05:16:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d029f86d-1786-349a-b4d0-6f7be9a4ea5e | -6.85306 | -56.42406 | 2026-08-16 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| addceb9b-a62a-35e8-aa4c-56b25886e589 | -8.89768 | -60.56022 | 2026-08-16 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 291d9018-f0e3-394b-b213-061a1092c14a | -8.96693 | -60.51256 | 2026-08-16 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ac1b1d67-1f5b-355e-9ea2-3324d6719773 | -8.61775 | -63.73007 | 2026-08-16 05:16:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3e3dd248-d30e-3072-a8ad-801caa03f942 | -6.63747 | -56.39633 | 2026-08-16 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9d3c5318-a125-3185-a75c-759b58a956ba | -6.83147 | -56.45269 | 2026-08-16 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| cbe8ab23-cbf4-3784-b781-2a789b6fdda4 | -6.60758 | -56.34882 | 2026-08-16 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8d101c10-14da-36a7-a17d-53b7a0903b31 | -8.26978 | -57.34236 | 2026-08-16 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bd8c1362-eaa1-3ad5-9535-06a0ab956ba5 | -8.66879 | -54.76435 | 2026-08-16 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 740fff9f-0ab7-3781-b0c6-d041ea3cb134 | -6.86136 | -56.41469 | 2026-08-16 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 96c2ece0-df56-3f29-97b3-23f4f08368da | -6.83202 | -56.44921 | 2026-08-16 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 979228a2-ad6e-37d5-ab2d-a50b432a4910 | -7.44168 | -55.31145 | 2026-08-16 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d0898b4f-1805-35a3-9f13-4cd50ff5f653 | -6.10568 | -57.73593 | 2026-08-16 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| cce303da-35c2-3188-ab74-486087420b16 | -8.65341 | -54.72802 | 2026-08-16 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3d4b7dee-fa24-352e-ad87-3061ccfc82b1 | -6.77983 | -55.83993 | 2026-08-16 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fa477e13-cab1-3387-983b-903bf2dad3d6 | -6.81725 | -59.8871 | 2026-08-16 05:16:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0f6c187e-4e69-335e-84c5-d090ab47ac71 | -7.38668 | -59.99765 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8c278103-20a6-37ad-8228-3a5e3dc4c483 | -6.54249 | -55.17423 | 2026-08-16 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 89c8afa5-41c5-3d1c-af15-89188ada2fcf | -10.27656 | -48.28888 | 2026-08-16 05:16:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2062500a-97f9-3dac-af77-dacf7a8d9692 | -8.95244 | -60.52916 | 2026-08-16 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 9f37ad63-526b-3724-b04c-261d3bb3f255 | -7.35365 | -59.59412 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b5e18dfd-f98e-3e30-8728-e9854a916553 | -11.33682 | -46.21403 | 2026-08-16 05:16:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 34e832d2-88ea-3959-9c69-9863de1f2335 | -11.51569 | -54.63492 | 2026-08-16 05:16:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 224d179a-6f6a-302b-b130-6549d4fe2f0c | -8.90475 | -60.60253 | 2026-08-16 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 716cc5ec-301a-30f3-a088-fe63401b54bc | -7.25721 | -44.69429 | 2026-08-16 05:16:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a083dfa6-8b78-3b3b-b3a7-62d61b6d8ade | -11.07045 | -47.26673 | 2026-08-16 05:16:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6f3b151f-24dd-3c32-9c30-73482a799279 | -6.97547 | -59.01179 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 85c5c0a5-8a6d-38e0-9d3e-4de9029dad36 | -6.60438 | -59.00004 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6764e4a0-197c-3144-88ed-230f9fb03090 | -7.33823 | -59.59597 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 694b6b82-d7fb-3c23-b46e-6d3af5f46466 | -6.62278 | -59.04556 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f67b7abc-0bc5-3c99-9228-75b744f85dbd | -9.68505 | -57.88671 | 2026-08-16 05:16:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d0fb5cac-938a-3c6f-b48d-461d11538fc5 | -6.86246 | -56.40774 | 2026-08-16 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 28e2848d-14b5-3d5e-ab67-ff7783a5a3f7 | -9.47588 | -60.54683 | 2026-08-16 05:16:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c6c22a58-add8-3cc8-9c7d-1165e4cdace9 | -6.70402 | -58.96459 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0d116e7e-46a9-3884-a033-027bc64e0202 | -6.67832 | -43.99571 | 2026-08-16 05:16:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 4d820fb5-3b24-3573-9a52-5b64165e15dc | -8.40999 | -62.65928 | 2026-08-16 05:16:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 96851f30-2c37-33ec-b2a3-be2b9dbb73b3 | -11.90432 | -45.97733 | 2026-08-16 05:16:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9ab10649-6a33-30f5-9bf8-888e5b4563c7 | -9.25417 | -56.90621 | 2026-08-16 05:16:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0cd327fd-5ae2-37c6-976d-83b148cbcf90 | -8.95623 | -60.5298 | 2026-08-16 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 12.8 |
| e911b3d0-cb4b-3ae3-8b33-2fa0117e2ba5 | -9.25749 | -56.90675 | 2026-08-16 05:16:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b0473132-1d25-3122-b590-2b4e92f491cf | -6.59786 | -58.99476 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1bbd1da4-acd4-3891-82b5-945758203dd9 | -6.86589 | -56.42604 | 2026-08-16 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 88faafd6-0edc-3040-b933-68089419ee49 | -10.53588 | -44.85059 | 2026-08-16 05:16:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| fa16068e-b977-3f4f-8b70-37c65bd71bf9 | -6.65185 | -56.40979 | 2026-08-16 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 12ed3e23-6ec9-31f8-a1e0-1585f5f6ee14 | -8.43044 | -62.67154 | 2026-08-16 05:16:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 425a7de3-4cf9-3674-9e29-c89462a6c47b | -8.61912 | -54.67778 | 2026-08-16 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1a1e0546-f5a9-3c7c-8440-754f2857259d | -6.85348 | -58.95911 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 516cdfae-ddd2-3a30-982c-c68e63025ca6 | -6.65072 | -56.43815 | 2026-08-16 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 82300ba0-dede-3142-b2b8-33d93bf327b1 | -6.85013 | -58.97958 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d7fa28b0-6050-3490-af7f-58f18ddd771c | -11.48566 | -46.58964 | 2026-08-16 05:16:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6794fbad-b73a-3901-9861-5d2a112b1af4 | -6.70963 | -58.95292 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0ce24f49-b6f1-384a-ba15-a86732c63f55 | -9.20535 | -59.67176 | 2026-08-16 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 79309d8a-86c6-3e29-ad2d-43fc046e9e07 | -8.89413 | -60.59594 | 2026-08-16 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bedb8bbd-38fa-3f63-9b3e-6b449cdb7d3c | -11.4608 | -46.60197 | 2026-08-16 05:16:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c16da9d0-4a0e-34ae-bf31-92be285a4f96 | -6.10984 | -57.71 | 2026-08-16 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 22.7 |
| a8a809ab-5b5d-3f8a-abc8-001e904cd2ac | -11.5116 | -54.63834 | 2026-08-16 05:16:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 572b76ea-02b0-388d-a65c-dd801825f633 | -12.44705 | -46.65133 | 2026-08-16 05:16:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d7746f79-cfae-3b72-bf57-eb753489e8d0 | -6.6338 | -59.06878 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 9dc5dc4b-0dae-3ff0-b8d9-231fa8cc4677 | -6.62095 | -59.07945 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 58f3ecb2-b8b7-3374-b733-38b1f5f38ab3 | -8.59068 | -54.68087 | 2026-08-16 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ac24e719-2f74-3f45-bdac-8dfe0650bb3d | -9.47383 | -60.51347 | 2026-08-16 05:16:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2597c729-c68d-38a5-842d-0c568799b535 | -8.34971 | -45.97856 | 2026-08-16 05:16:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1241dc6b-85fe-3c23-a892-b58987211e9d | -8.97829 | -60.51447 | 2026-08-16 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| af263c65-9ef4-3295-a986-a27f53a948f7 | -6.8298 | -56.42035 | 2026-08-16 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 735e5e09-0876-3e72-967d-5bb6ab178d16 | -10.52203 | -44.85355 | 2026-08-16 05:16:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2d56f5ee-c387-363f-be86-dee47d45bd72 | -7.55684 | -61.1703 | 2026-08-16 05:16:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |


[Clique aqui para ver as próximas entradas](README36.md)
